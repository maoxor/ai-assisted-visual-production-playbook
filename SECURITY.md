# Security policy

## Scope

This repository contains documentation, templates, agent skills and small Python command-line tools that run locally
on files you give them. The tools make no network request, need no credentials and execute no downloaded code.
`tools/review_video.py` calls the `ffmpeg` binary found in your `PATH`; `tools/review_page.py --open` asks the system
to open the generated page.

## Supported versions

Only the latest release receives fixes.

## Reporting a vulnerability

Please do **not** open a public issue for a vulnerability. Use GitHub's private vulnerability reporting instead
(**Security** tab → **Report a vulnerability**). Describe the affected file, the input that triggers the problem and
its effect. You should receive an answer within two weeks.

## Good practice for users

- Inspect any script before running it, including the ones in this repository
  ([provenance and licensing](docs/tooling/README.md#provenance-and-licensing)).
- Skills and plugins give instructions to your agent: read them before installing them.
