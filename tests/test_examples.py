"""The end-to-end demonstration must keep working and keep showing what it claims.

  uv run pytest tests/test_examples.py
"""
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "examples"))

import demo  # noqa: E402


def test_demo_reduces_flicker_and_keeps_the_loop(tmp_path):
    result = demo.main(["--output", str(tmp_path / "demo")])
    before, after, loop = result["before"]["flicker_pct"], result["after"]["flicker_pct"], result["loop"]
    assert before > 0.1
    assert after <= 0.3 * before
    assert loop["ok"] and loop["frames"] == 80
    assert 0.8 <= loop["seam_ratio"] <= 1.25
    page = Path(result["page"]).read_text(encoding="utf-8")
    assert "Toolkit demonstration" in page and "Missing file" not in page
    if shutil.which("ffmpeg"):
        assert (tmp_path / "demo" / "review" / "raw_vs_stable.mp4").stat().st_size > 0
