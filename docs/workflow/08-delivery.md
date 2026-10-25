# 8. Delivery

**Objective.** Hand over deliverables that exist, open and have been checked, with a report that makes them usable
and reproducible.

## What is delivered [proven]

- **Reproducible sources**: project and bundled dependencies, generation, computation and export scripts,
  configuration and seeds.
- **Final deliverables** in every target format, with their **fallbacks** (stills, posters, degraded versions).
- **The integration**, tested in the target environment, or a minimal local demonstration page.
- **The evidence**: check captures, before/after, review videos, an up-to-date review page.
- **A short report**: checks actually run, defects fixed, remaining limitations
  ([template](../../templates/delivery-report.md)).
- **A README**: open, modify, regenerate, export; sources and licences of added resources.

## The final report [proven]

It always separates:

1. **Done**: what exists at its final location.
2. **Tested**: what was verified, how, with which results, in which environments (real or emulated).
3. **Limitations**: what could not be done or verified, with the reason and how to do it.

It also restates the choices made and their reason, one line each.

<a id="delivery-under-time-pressure"></a>

## Delivery under time pressure [proven]

When the lead has run out of time and asks for whatever is ready now:

- deliver immediately what is **ready and verified**, in a clear location, with the integration snippet to copy;
- say in one line what is not tested;
- then resume the ongoing work without breaking what was delivered: **same file names**, old versions archived next to
  them, an explicit announcement when new files replace the old ones.

## After delivery

- **Retrospective**: a report in the project ([template](../../templates/retrospective.md)), then the **generic**
  lessons brought back to this playbook ([`CONTRIBUTING.md`](../../CONTRIBUTING.md#after-each-project)).
- **Clean-up proposed, not imposed**: regenerable intermediate files may be deleted, but propose it instead of doing
  it.

## Exit criterion

The [definition of done](../quality/README.md#definition-of-done) is met; the report is delivered; the location of the
deliverables is given; usage is explained (code snippet, command).
