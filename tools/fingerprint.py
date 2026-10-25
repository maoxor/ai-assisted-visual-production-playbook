"""Fingerprint the dependencies of a production and resume safely: never mix outputs from different states.

  python fingerprint.py compute --dep scene.blend --dep config/scene.toml --dep 'layers/*.png' --extra tool="4.2"
  python fingerprint.py ensure --outputs renders/v1/desktop --dep ... [--extra quality=final] [--stale <folder>]
  python fingerprint.py pending --outputs renders/v1/desktop/final --count 300 [--template 'frame_{:04d}.png']
  python fingerprint.py run --outputs renders/v1/desktop -- python scripts/render.py --batch 0

- "compute": SHA-256 of each dependency (files or glob patterns, sorted) and of the "extra" values (tool version,
  quality profile...), combined into a single fingerprint.
- "ensure": compares the fingerprint with the one stored in <outputs>/VERSION.json. If it differs, or if outputs exist
  without a fingerprint, the whole folder is MOVED to the stale folder (never deleted), then recreated with the new
  fingerprint. Exit code 0 in every case; the message says what was done.
- "pending": lists the units to (re)do: missing or incomplete files (PNG without its IEND chunk, empty file).
- "run": runs a command while <outputs>/RUNNING exists (it holds the process id), then removes it. The marker tells
  guards such as hooks/guard_production.py that the dependencies listed in VERSION.json must not change.

Usage rule: call "ensure" before each production batch; never modify a dependency during the computation (the
fingerprint would change and the resume would start over).
"""
import argparse
import contextlib
import hashlib
import json
import os
import subprocess
import sys
import time
from glob import glob
from pathlib import Path

PNG_END = b"IEND\xaeB`\x82"


def sha256_file(path, block=1 << 20):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(block), b""):
            h.update(chunk)
    return h.hexdigest()


def expand(dependencies):
    """Sorted, de-duplicated list of the designated files (paths or glob patterns)."""
    out = []
    for d in dependencies:
        d = str(d)
        if any(c in d for c in "*?["):
            found = sorted(glob(d, recursive=True))
            if not found:
                raise FileNotFoundError(f"pattern matches no file: {d}")
            out += found
        else:
            if not Path(d).is_file():
                raise FileNotFoundError(d)
            out.append(d)
    return sorted(set(out))


def fingerprint(dependencies, extra=None):
    """(hex fingerprint, details) for dependencies and additional values."""
    h = hashlib.sha256()
    details = {"files": {}, "extra": dict(sorted((extra or {}).items()))}
    for f in expand(dependencies):
        digest = sha256_file(f)
        details["files"][f] = digest[:16]
        h.update(f.encode() + b"\0" + digest.encode() + b"\0")
    for k, v in details["extra"].items():
        h.update(f"{k}={v}".encode() + b"\0")
    return h.hexdigest(), details


def ensure(outputs, dependencies, extra=None, stale=None):
    """Prepare <outputs> for the described state; move outputs of another state. Returns (fingerprint, action)."""
    outputs = Path(outputs)
    fp, details = fingerprint(dependencies, extra)
    version_file = outputs / "VERSION.json"
    has_content = outputs.exists() and any(p.name != "VERSION.json" for p in outputs.rglob("*") if p.is_file())
    reason = None
    if version_file.exists():
        if json.loads(version_file.read_text()).get("fingerprint") == fp:
            return fp, "unchanged"
        reason = "different fingerprint"
    elif has_content:
        reason = "outputs without fingerprint"
    if reason:
        stale_dir = Path(stale) if stale else outputs.parent / "_stale"
        dst = stale_dir / f"{outputs.name}_{time.strftime('%Y%m%d_%H%M%S')}"
        stale_dir.mkdir(parents=True, exist_ok=True)
        outputs.rename(dst)
        action = f"{reason}: previous outputs moved to {dst}"
    else:
        action = "new"
    outputs.mkdir(parents=True, exist_ok=True)
    version_file.write_text(json.dumps({"fingerprint": fp, "date": time.strftime("%Y-%m-%d %H:%M:%S"), **details},
                                       indent=1))
    return fp, action


def is_complete(path):
    """True if the file exists, is not empty and, for a PNG, ends with the IEND chunk."""
    path = Path(path)
    if not path.is_file() or path.stat().st_size == 0:
        return False
    if path.suffix.lower() == ".png":
        with open(path, "rb") as f:
            f.seek(-len(PNG_END), 2)
            return f.read() == PNG_END
    return True


def pending(folder, count, template="frame_{:04d}.png"):
    return [i for i in range(count) if not is_complete(Path(folder) / template.format(i))]


@contextlib.contextmanager
def running(outputs):
    """Mark <outputs> as being produced (RUNNING file with the process id) for the duration of the block."""
    marker = Path(outputs) / "RUNNING"
    marker.parent.mkdir(parents=True, exist_ok=True)
    marker.write_text(json.dumps({"pid": os.getpid(), "since": time.strftime("%Y-%m-%d %H:%M:%S")}))
    try:
        yield marker
    finally:
        marker.unlink(missing_ok=True)


def _extra(values):
    out = {}
    for v in values or []:
        k, _, val = v.partition("=")
        out[k] = val
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    helps = {"compute": "print the fingerprint of the dependencies",
             "ensure": "prepare an output folder for the current state; move outputs of another state",
             "pending": "list the missing or incomplete units"}
    for name in ("compute", "ensure"):
        p = sub.add_parser(name, help=helps[name])
        p.add_argument("--dep", action="append", required=True, help="file or glob pattern (repeatable)")
        p.add_argument("--extra", action="append", help="key=value added to the fingerprint (repeatable)")
        if name == "ensure":
            p.add_argument("--outputs", required=True, help="output folder protected by VERSION.json")
            p.add_argument("--stale", default=None, help="where stale outputs go (default: <outputs>/../_stale)")
    p = sub.add_parser("run", help="run a command while <outputs>/RUNNING marks the production as in progress")
    p.add_argument("--outputs", required=True, help="output folder protected by VERSION.json")
    p.add_argument("command", nargs=argparse.REMAINDER, help="command to run, after --")
    p = sub.add_parser("pending", help=helps["pending"])
    p.add_argument("--outputs", required=True, help="folder of the units")
    p.add_argument("--count", type=int, required=True, help="expected number of units")
    p.add_argument("--template", default="frame_{:04d}.png", help="file name of unit i (default: frame_{:04d}.png)")
    a = ap.parse_args(argv)
    if a.cmd == "compute":
        fp, details = fingerprint(a.dep, _extra(a.extra))
        print(json.dumps({"fingerprint": fp, **details}, indent=1))
    elif a.cmd == "ensure":
        fp, action = ensure(a.outputs, a.dep, _extra(a.extra), a.stale)
        print(f"{fp[:16]} {action}")
    elif a.cmd == "run":
        command = a.command[1:] if a.command[:1] == ["--"] else a.command
        if not command:
            ap.error("run: give the command after --")
        with running(a.outputs):
            return subprocess.run(command).returncode
    else:
        units = pending(a.outputs, a.count, a.template)
        print(json.dumps({"pending": len(units), "units": units}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
