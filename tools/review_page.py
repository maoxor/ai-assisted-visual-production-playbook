"""Review page: gather the videos, images and measures of a step into a local HTML page to open in a browser.

  python review_page.py --plan review.json --output review/step/index.html [--open]

Plan (JSON):
{
  "title": "Iteration 4 - sample element",
  "lang": "en",
  "intro": "What the page shows and what is expected from the reviewer.",
  "sections": [
    {"title": "Whole scene, desktop", "text": "Forward playback, final size.",
     "media": [{"file": "before.mp4", "caption": "Before"}, {"file": "after.mp4", "caption": "After"}],
     "table": {"columns": ["Measure", "Before", "After"], "rows": [["Flicker", "1.33 %", "0.16 %"]]}}
  ]
}

Rules enforced by the page (method: docs/workflow/07-validation.md):
- looping videos, forward playback, muted, autoplay, side by side at identical size;
- captions are mandatory (a column without a caption is rejected);
- paths relative to the page; a missing file is flagged in red in the page and on standard error;
- no external resource: the page works offline.
"""
import argparse
import html
import json
import os
import subprocess
import sys
from pathlib import Path

VIDEO = {".mp4", ".webm", ".mov"}
IMAGE = {".png", ".jpg", ".jpeg", ".webp", ".avif", ".gif", ".svg"}

STYLE = """
:root { --bg:#f6f5f2; --text:#1d1c1a; --muted:#5f5b55; --line:#d9d5ce; --accent:#8a5a14; --missing:#b3261e; }
@media (prefers-color-scheme: dark) { :root { --bg:#121214; --text:#e8e6e3; --muted:#a9a6a1; --line:#2a2a2e;
  --accent:#f0cd8c; --missing:#ff8a80; } }
* { box-sizing:border-box; }
body { background:var(--bg); color:var(--text); font:15px/1.5 -apple-system,"Helvetica Neue",Arial,sans-serif;
  margin:0 auto; max-width:2600px; padding:0 16px 48px; }
h1 { font-size:24px; margin:24px 0 8px; } h2 { font-size:19px; border-top:1px solid var(--line); padding-top:14px; }
p.intro, p.text { color:var(--muted); max-width:80ch; }
.grid { display:grid; gap:12px; grid-template-columns:repeat(auto-fit, minmax(min(100%, 320px), 1fr)); }
figure { margin:0; } figcaption { color:var(--muted); font-size:13px; margin-top:4px; }
video, img { display:block; width:100%; height:auto; background:#000; }
.missing { border:2px dashed var(--missing); color:var(--missing); padding:24px; text-align:center; }
table { border-collapse:collapse; margin:10px 0; } td, th { border:1px solid var(--line); padding:4px 10px; text-align:left; }
a { color:var(--accent); }
"""


def render_media(item, root, missing):
    file, caption = item.get("file"), item.get("caption")
    if not caption:
        raise ValueError(f"missing caption for {file!r}")
    path = (root / file).resolve()
    e = html.escape
    if not path.exists():
        missing.append(file)
        body = f'<div class="missing">Missing file: {e(file)}</div>'
    elif path.suffix.lower() in VIDEO:
        body = f'<video src="{e(file)}" autoplay loop muted playsinline controls preload="auto"></video>'
    elif path.suffix.lower() in IMAGE:
        body = f'<a href="{e(file)}"><img src="{e(file)}" alt="{e(caption)}" loading="lazy"></a>'
    else:
        body = f'<a href="{e(file)}">{e(file)}</a>'
    return f"<figure>{body}<figcaption>{e(caption)}</figcaption></figure>"


def render_table(t):
    e = html.escape
    head = "".join(f"<th>{e(str(c))}</th>" for c in t["columns"])
    rows = "".join("<tr>" + "".join(f"<td>{e(str(c))}</td>" for c in r) + "</tr>" for r in t["rows"])
    return f"<table><tr>{head}</tr>{rows}</table>"


def build(plan, output):
    output = Path(output)
    root = output.parent
    missing, blocks = [], []
    e = html.escape
    for s in plan.get("sections", []):
        b = [f"<section><h2>{e(s['title'])}</h2>"]
        if s.get("text"):
            b.append(f'<p class="text">{e(s["text"])}</p>')
        if s.get("media"):
            b.append('<div class="grid">' + "".join(render_media(m, root, missing) for m in s["media"]) + "</div>")
        if s.get("table"):
            b.append(render_table(s["table"]))
        b.append("</section>")
        blocks.append("".join(b))
    title = e(plan.get("title", "Review"))
    lang = e(plan.get("lang", "en"))
    intro = f'<p class="intro">{e(plan["intro"])}</p>' if plan.get("intro") else ""
    doc = (f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8">'
           f'<meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title>'
           f"<style>{STYLE}</style></head><body><h1>{title}</h1>{intro}{''.join(blocks)}</body></html>")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(doc, encoding="utf-8")
    return missing


def open_page(path):
    """Open a file with the system's default application; True on success."""
    path = str(Path(path).resolve())
    try:
        if sys.platform == "win32":
            os.startfile(path)  # noqa: S606 (Windows only)
            return True
        cmd = "open" if sys.platform == "darwin" else "xdg-open"
        return subprocess.run([cmd, path]).returncode == 0
    except OSError:
        return False


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--plan", required=True, help="JSON file describing the page")
    ap.add_argument("--output", required=True, help="path of the HTML page")
    ap.add_argument("--open", action="store_true", help="open the page in the default browser")
    a = ap.parse_args(argv)
    plan = json.loads(Path(a.plan).read_text(encoding="utf-8"))
    missing = build(plan, a.output)
    for m in missing:
        print(f"MISSING {m}", file=sys.stderr)
    print(f"PAGE {a.output}")
    if a.open and not open_page(a.output):
        print(f"Could not open the page: open {Path(a.output).resolve()} manually", file=sys.stderr)
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
