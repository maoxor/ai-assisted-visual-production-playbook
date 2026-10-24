"""Repository checks: internal links, anchors, maturity levels, structure, confidentiality.

  python3 scripts/check_repo.py                          # exit code 1 on any error
  python3 scripts/check_repo.py --deny-list terms.txt    # also reject workstation-specific terms

Checks:
1. Every relative link in a Markdown file points to an existing file; every anchor (#...) exists in the target
   (explicit <a id="..."> or heading, using GitHub's slug algorithm). Code blocks are ignored.
2. Method documents carry at least one maturity level: [éprouvé], [extrapolé] or [proposé].
3. Every top-level documentation folder has a README.md referenced from the root README.
4. Confidentiality (decision 0007): no secrets (GitHub tokens, API keys, private keys), no email addresses other than
   "noreply", no absolute workstation paths, no media or binary assets, ASCII-only file names.
5. Optional deny list: one term per line ('#' starts a comment), matched case-insensitively as whole words in every
   text file and file name. Default location: .git/info/deny-list.txt (local, never versioned).
Standard library only.
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IGNORED = {".git", ".pytest_cache", ".venv", "__pycache__", "node_modules", ".ruff_cache"}
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HTML_ANCHOR = re.compile(r'<a\s+id="([^"]+)"', re.I)
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
MATURITY = re.compile(r"\[(éprouvé|extrapolé|proposé)\]")
SECRETS = [
    (re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}"), "GitHub token"),
    (re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}"), "GitHub token"),
    (re.compile(r"\bsk-[A-Za-z0-9_-]{20,}"), "API key"),
    (re.compile(r"\bAKIA[0-9A-Z]{16}\b"), "AWS key"),
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"), "private key"),
    (re.compile(r"[A-Za-z0-9._%+-]+@(?!users\.noreply\.github\.com|anthropic\.com)[A-Za-z0-9.-]+\.[a-z]{2,}"),
     "email address"),
    (re.compile(r"(?:/Users|/home)/[a-z][a-z0-9_-]+/"), "absolute workstation path"),
]
MEDIA = {".png", ".jpg", ".jpeg", ".webp", ".avif", ".gif", ".mp4", ".mov", ".webm", ".mkv", ".exr", ".blend",
         ".blend1", ".psd", ".zip", ".tar", ".gz", ".pdf"}
TEXT = {".md", ".py", ".js", ".json", ".yml", ".yaml", ".toml", ".txt", ".sh", ".cfg", ".ini", ""}
MATURITY_REQUIRED = ["docs/principles.md", "docs/workflow/*.md", "docs/quality/README.md",
                     "docs/quality/anti-patterns.md", "docs/quality/collaboration.md", "docs/domains/*.md",
                     "docs/tooling/*.md", "skills/README.md"]
MATURITY_EXEMPT = {"docs/domains/README.md"}
DOC_FOLDERS = ["docs", "templates", "skills", "tools"]


def files(pattern="**/*"):
    for p in sorted(ROOT.glob(pattern)):
        if p.is_file() and not (set(p.relative_to(ROOT).parts) & IGNORED):
            yield p


def strip_code(text):
    """Text without fenced code blocks or inline code (example links there are not checked)."""
    text = re.sub(r"^```.*?^```", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S | re.M)
    return re.sub(r"`[^`\n]*`", "", text)


def github_slug(title):
    t = re.sub(r"<[^>]+>", "", title).strip().lower()
    t = re.sub(r"[^\w\- ]", "", t)
    return t.replace(" ", "-")


def anchors(path, cache={}):
    if path not in cache:
        text = path.read_text(encoding="utf-8")
        found = set(HTML_ANCHOR.findall(text))
        seen = {}
        for line in re.sub(r"^```.*?^```", "", text, flags=re.S | re.M).splitlines():
            m = HEADING.match(line)
            if m:
                s = github_slug(m.group(2))
                n = seen.get(s, 0)
                found.add(s if n == 0 else f"{s}-{n}")
                seen[s] = n + 1
        cache[path] = found
    return cache[path]


def check_links(errors):
    count = 0
    for md in files("**/*.md"):
        text = strip_code(md.read_text(encoding="utf-8"))
        for num, line in enumerate(text.splitlines(), 1):
            for target in LINK.findall(line):
                if re.match(r"^[a-z]+:", target) or target.startswith("<"):
                    continue
                count += 1
                path, _, anchor = target.partition("#")
                dest = (md.parent / path).resolve() if path else md
                where = f"{md.relative_to(ROOT)}:{num}"
                if not dest.exists():
                    errors.append(f"{where}: broken link -> {target}")
                    continue
                if anchor and dest.suffix == ".md" and anchor not in anchors(dest):
                    errors.append(f"{where}: missing anchor -> {target}")
    return count


def check_maturity(errors):
    for pattern in MATURITY_REQUIRED:
        for p in files(pattern):
            rel = p.relative_to(ROOT).as_posix()
            if rel not in MATURITY_EXEMPT and not MATURITY.search(p.read_text(encoding="utf-8")):
                errors.append(f"{rel}: no maturity level [éprouvé] / [extrapolé] / [proposé]")


def check_structure(errors):
    root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for d in DOC_FOLDERS:
        if not (ROOT / d).is_dir():
            errors.append(f"{d}/: missing folder")
            continue
        if d != "docs" and not (ROOT / d / "README.md").exists():
            errors.append(f"{d}/: missing README.md")
        if f"{d}/" not in root_readme:
            errors.append(f"{d}/: not referenced from the root README")


def load_deny_list(path):
    if path is None:
        default = ROOT / ".git" / "info" / "deny-list.txt"
        if not default.exists():
            return []
        path = default
    terms = []
    for line in Path(path).expanduser().read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip()
        if line:
            terms.append(line)
    return terms


def check_confidentiality(errors, deny_terms):
    deny = [(t, re.compile(rf"(?<!\w){re.escape(t)}(?!\w)", re.I)) for t in deny_terms]
    for p in files():
        rel = p.relative_to(ROOT).as_posix()
        if not rel.isascii():
            errors.append(f"{rel}: non-ASCII file name")
        if p.suffix.lower() in MEDIA:
            errors.append(f"{rel}: media or binary asset (decision 0007)")
            continue
        for term, rx in deny:
            if rx.search(rel):
                errors.append(f"{rel}: deny-listed term in file name ({term})")
        if p.suffix not in TEXT or p.resolve() == Path(__file__).resolve():
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"{rel}: undecodable file")
            continue
        for rx, name in SECRETS:
            for m in rx.finditer(text):
                line = text[:m.start()].count("\n") + 1
                errors.append(f"{rel}:{line}: possible {name} ({m.group(0)[:24]}...)")
        for term, rx in deny:
            for m in rx.finditer(text):
                line = text[:m.start()].count("\n") + 1
                errors.append(f"{rel}:{line}: deny-listed term ({term})")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--deny-list", default=None, help="file of forbidden terms (default: .git/info/deny-list.txt)")
    a = ap.parse_args(argv)
    errors = []
    deny_terms = load_deny_list(a.deny_list)
    n_links = check_links(errors)
    check_maturity(errors)
    check_structure(errors)
    check_confidentiality(errors, deny_terms)
    n_md = sum(1 for _ in files("**/*.md"))
    for e in errors:
        print("ERROR", e)
    print(f"{n_md} Markdown files, {n_links} internal links checked, {len(deny_terms)} deny-listed terms, "
          f"{len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
