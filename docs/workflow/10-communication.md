# 10. Communication

**Objective.** At every moment, the lead sees what they need to decide, without having to chase.

## Show [proven]

- **Open the result** (video, page, image) as soon as it is ready, then **check that it actually opened**; otherwise
  give the exact path ([A19](../quality/anti-patterns.md#a19)).
- **Show what was asked for**: if the animated piece is expected, stills are not enough
  ([A1](../quality/anti-patterns.md#a1)).
- **Show early**: a short or partial render is better than a silent wait; opening a page can be scheduled as soon as
  the first results are ready.
- **A local review page** gathers the videos, comparisons and measurements of a step
  ([`review_page.py`](../../tools/README.md#review_pagepy)).
- **Share privately only**, and only with the lead's approval; a third party's artwork does not leave the machine
  without approval.

## Status updates [proven]

An update contains:

1. **What works** (verified).
2. **What remains to fix.**
3. **The next action**, and the estimated time if a computation is running.
4. **What is waiting for the lead**, if anything (decision, approval).

It is **short** ([template](../../templates/status-update.md)). During long tasks, send it **without waiting to be
asked**.

## Answer the question asked [proven]

| Question | Expected answer |
|---|---|
| "How long, and why?" | A figure, its assumptions, the main cause |
| "What is this for?" | The role of the step in one or two sentences, and what would happen without it |
| "Will it work perfectly?" | Yes or no, the evidence, the limit |
| "What did you choose and why?" | The choice, the reasons, the alternatives rejected |

## Stay aligned with the objective [proven]

When the lead asks for the project's objective to be restated, they are checking that the agent has not drifted. The
objective and key criterion from the brief must be restatable at any time; reread them before every report.

## Form [proven]

- The lead's language, with correct spelling and diacritics.
- Absolute values on the **latest version**; past versions only when asked.
- Sides named from the viewer's point of view, and said explicitly ("on the right of the image").
- Short tables for comparisons: profile, measurement, visible difference, recommendation.
- Acknowledge an omission or defect plainly, then show the fix.
