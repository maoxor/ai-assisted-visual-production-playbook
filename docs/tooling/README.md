# Tooling: role, use, contribution to quality

Tools used with the method, their role and what they bring to quality. Check the available versions at the start of
each project: the versions given here are landmarks, not requirements.

| Document | Content |
|---|---|
| This file | Inventory, provenance and licensing, shared machine |
| [`claude-code.md`](claude-code.md) | Configuring and using Claude Code: instructions, memory, skills, plugin, hooks, permissions |
| [`../../tools/`](../../tools/README.md) | Reusable, tested scripts |
| [`../../skills/`](../../skills/README.md) | Skills ready to install |

## Inventory [proven]

| Tool | Role | When | Contribution to quality |
|---|---|---|---|
| **Claude Code** | Agent: research, code, trials, checks, documentation | The whole project | Runs and verifies; keeps logs and memory |
| **Blender** (LTS version) | Scene generation by Python script, Cycles rendering on GPU, OIDN denoising | Build, trials, production | Physical materials, real refraction of the animated state, reproducible by script |
| **Python** and **uv** | Preparation, checks, post-processing, encoding, tests; locked environment (`uv.lock`) | Everywhere | Reproducibility; tailor-made measurement tools |
| **numpy, OpenCV, Pillow, scikit-image** | Image measurements, optical flow (DIS), downscaling | Checks, stabilization | Objective measurements alongside the eye |
| **ꟻLIP** (`flip-evaluator`) | Perceptual difference between images | Fidelity | Closer to perception than PSNR |
| **PyTorch, transformers** | Local inference of segmentation and depth models | Preparation | Masks and depth without regenerating the image |
| **ffmpeg** (libsvtav1, libx265, libx264, libvmaf) | Encoding, review videos, VMAF, XPSNR | Review, exports | Measured exports; side-by-side comparisons |
| **Playwright** (Chrome, WebKit, Firefox) | Page tests: playback, dropped frames, rotation, emulation | Integration | Real playback measured; real and emulated kept apart |
| **pytest, Vitest, ruff, ESLint, import-linter** | Tests and architecture contracts | Development | Automatic non-regression |
| **GitHub Actions** | CI: lint, tests, e2e, migrations, audit, secrets | Every push | Checks independent of the agent |
| **gitleaks** | Secret detection | CI | No secret published |
| **iOS simulators (Xcode), Android emulators** | Mobile tests close to real | Mobile integration | Safari iOS and Chrome Android behaviours |
| **caffeinate, pmset, nohup** (macOS) | Prevent sleep, wait for mains power, detach computations | Long production | Computations that survive interruptions |

<a id="provenance-and-licensing"></a>

## Provenance and licensing [proven]

Before adding a tool, model, texture, repository, MCP server or skill:

1. **Provenance**: official source, stable version, maintained dependencies.
2. **Licence** compatible with the intended use, checked on the exact variant.
3. **Compatibility** with the machine (architecture, GPU, memory).
4. **Concrete usefulness** demonstrated: an MCP server, skill or model is added only if it brings a measurable gain;
   scripts are often enough.
5. **Inspection of scripts** before running them.
6. **Record**: version or commit, source, licence, role, checksums (provenance manifest, `SHA256SUMS`, README table).

What was **considered then rejected** is recorded too, with the reason (feature missing from the version in use,
non-commercial licence, no benefit).

<a id="shared-machine"></a>

## Shared machine [proven]

When several projects or sessions share the same machine:

- **never** kill the processes of another project or session;
- route heavy machine-learning computations through a **common lock** (for example `flock` on a shared file), because
  several simultaneous inferences can exhaust memory and bring the machine down;
- before concluding that a computation is slow, check who holds the lock and the load (`uptime`); flag measurements made
  under load;
- after stopping a script, check that no child process (render engine, browser) was left orphaned.
