# Quality principles

These sixteen principles hold whatever the project, technique or art direction. They explain **why** the
[workflow](workflow/README.md) is built the way it is. When a step has to be adapted to a domain, the step changes; the
principle stays.

All principles are **[proven]** unless stated otherwise.

---

<a id="p1"></a>

## P1. The perceived result is what counts; measurements inform it without proving it

**Statement.** Work is judged on what its audience will see: the image at its display size, motion at normal speed,
the experience in its real environment. Metrics (SSIM, VMAF, contrast, percentages) serve diagnosis and non-regression.
They never prove success and never become targets.

**Why.** A measurable variation is not necessarily visible. A metric that becomes a target gets optimized at the
expense of what it stood for.

**How.** Every measurement comes with the capture or video to inspect. Write down what you see first, then what the
measurement confirms or qualifies. Thresholds stay indicative; when they come from another source, say so.

**Anti-pattern.** Toning a treatment down because a measurement drops while the lead prefers the rich version
([A12](quality/anti-patterns.md#a12)).

---

<a id="p2"></a>

## P2. "Verified" means run and quoted; the agent's checks are not the lead's approval

**Statement.** A check is reported as done only once it has been run, with its result quoted (command, figure, file).
Always separate *what the agent checked*, *what the lead approved* and *what could not be verified*.

**Why.** A report can be truncated, a box ticked without evidence, an assumption taken for a fact. Trust rests on
traceability.

**How.** Logs carry the line "These observations are mine; they are not your approval". Reports list the checks that
were actually run. What is emulated or untestable is flagged as such.

---

<a id="p3"></a>

## P3. Done means: the final files exist, open and have been checked

**Statement.** A launched command, a running computation, a prototype or a plan is not a delivery. Work is done when
the deliverables exist at their final location, play or open in their target environment and have passed the planned
checks.

**Why.** The gap between "launched" and "delivered" is where defects concentrate: a missing unit, a file unreadable in
the target, a forgotten leftover. It also gives a false sense of being finished.

**How.** The [definition of done](quality/README.md#definition-of-done) is the exit list. The report separates *done*,
*tested* and *limitations*.

---

<a id="p4"></a>

## P4. Separate what is documented, tested, assumed and observed

**Statement.** In research or diagnosis, every claim carries its status: **D** documented (source quoted), **T** tested
in the project, **H** hypothesis, **O** observation on our own results. A technique is never attributed to a studio or
author without a direct source.

**Why.** Otherwise an assumption becomes a fact, forum advice becomes a rule, and the error spreads from one iteration
to the next.

**How.** Research notes follow the [template](../templates/research-note.md). Inaccessible pages are flagged.

---

<a id="p5"></a>

## P5. Targeted research serves a decision, then stops

**Statement.** Research solves a precise problem or settles a technical choice. Primary sources come first; forums are
leads to be verified by a trial. Earlier research is reused, and the work moves to a trial as soon as a method is
sufficiently supported.

**Why.** Endless research delays the evidence; a list of links moves nothing forward; ignoring past trials repeats the
same dead ends.

**How.** See [research](workflow/02-research.md). By default the agent researches by itself and runs queries in
parallel ([decision 0003](decisions/0003-no-subagents.md)).

---

<a id="p6"></a>

## P6. One variable at a time; isolate to understand

**Statement.** A trial changes one thing. A defect is diagnosed **by elimination**: neutralize one possible cause at a
time (a light source, a material painted black, a module disabled, an element hidden) until the defect disappears.
Corrections are grouped into families that can be switched off.

**Why.** Several simultaneous changes make the effect of each unreadable: one correction can hide another or introduce
an invisible regression.

**How.** See [evidence-based iteration](workflow/04-evidence-based-iteration.md) and the
[elimination technique](domains/offline-3d-rendering.md#diagnosis-by-elimination).

---

<a id="p7"></a>

## P7. Sample first, generalize second

**Statement.** A new method is tuned on **a representative sample**: one element, an excerpt of a few seconds, a
difficult frame, a critical screen. Check the result *and* the cost, then extend in measured batches. Full production
starts only with the lead's explicit approval.

**Why.** Iterating on the whole costs hours per trial. A generalized defect has to be fixed everywhere, and a cost
multiplied by a hundred elements can make production impractical.

**How.** [Minimal prototype](workflow/03-prototyping.md), then sample, then a validation excerpt in the final format,
then production.

---

<a id="p8"></a>

## P8. Judge in final conditions

**Statement.** Evaluate:
- at the **final display size**;
- at **normal speed**;
- with the **final processing** (depth of field, downscaling, encoding, production build);
- on the **whole piece**;
- in **forward playback**, never back and forth;
- on the **latest version**, not on a past version taken as the yardstick.

Slow motion, amplification, diagnostic views and close-ups help to understand: they validate nothing.

**Why.** A detail invisible at final size does not count; a defect visible only in motion goes unnoticed on a still; a
back-and-forth loop hides the seam; comparing with an old version blurs the decision.

**How.** Every review video shows the whole piece, forward, at final size; close-ups come in addition. Tables give
absolute values on the current version.

---

<a id="p9"></a>

## P9. Fix the cause, not the symptom

**Statement.** A defect is fixed where it originates. It is not hidden by a global blur, a reduced amplitude, a
denoiser that erases detail, a disabled test or a crop.

**Why.** A masked symptom comes back elsewhere, and the quality you wanted to preserve is lost.

**How.** Find the stage at which the defect appears (generation, rendering, denoising, resizing, encoding, playback,
code, data) and fix it at that stage. An accepted trade-off is shown precisely.

---

<a id="p10"></a>

## P10. Lose nothing: identifiable versions, archives, separate outputs

**Statement.**
- Every version is identifiable.
- Before any significant change, the current state is archived.
- Outputs of different versions never mix.
- A result is reused only if it matches the current state exactly, which a fingerprint of the dependencies verifies.
- Nothing is deleted: what is obsolete is moved.

**Why.** Going back to an earlier state is frequent; mixing outputs of two states produces wrong deliverables that are
hard to detect; a before/after comparison needs the "before".

**How.** See [production](workflow/06-production.md#fingerprint-and-resume) and the
[`fingerprint.py`](../tools/README.md#fingerprintpy) tool.

---

<a id="p11"></a>

## P11. Reproducible by construction

**Statement.**
- Parameters live in declarative configuration, with explicit names.
- Procedural generation derives from a stable seed.
- Dependencies, models and revisions are pinned.
- Every added resource carries its provenance, licence and checksum.
- Regenerate rather than retouch by hand.

**Why.** A manual retouch is lost at the next regeneration; an unstable seed makes two builds differ; a resource
without a verified licence blocks distribution.

**How.** See [reproducibility in rendering](domains/offline-3d-rendering.md#reproducibility) and
[resource provenance](tooling/README.md#provenance-and-licensing).

---

<a id="p12"></a>

## P12. Autonomy on what is reversible; approval for what is irreversible or external

**Statement.** **Reversible** technical and artistic decisions are taken without asking again, based on the reference
and the instructions. Explicit approval is required for:
- publications, purchases, subscriptions;
- sending data or assets to an external service;
- deletions;
- destructive system changes;
- launching a long production when the lead has reserved that decision.

When a blocker truly requires an intervention, ask one precise question and carry on with independent tasks.

**Why.** Asking again at every step exhausts the lead; acting alone on the irreversible can cost rights, money or data.

---

<a id="p13"></a>

## P13. Measure the real cost before producing, and keep costs apart

**Statement.** Before a long production, measure the real cost on representative units, including a difficult one;
separate start-up from steady state; attribute each expense to its cause with isolated tests. Keep apart costs that do
not mix: production time, deliverable weight, playback or execution cost, maintenance. No setting is untouchable: its
usefulness has to be demonstrated.

**Why.** An effect that is expensive to compute can be cheap to distribute, and the reverse. A drifting cost per unit
ends up preventing any iteration.

**How.** See the [cost profile](workflow/06-production.md#cost-profile).

---

<a id="p14"></a>

## P14. Show, and stay aligned with the objective

**Statement.**
- Show the result (open the video, the page, the image) instead of describing it, and check that it actually opened.
- Status updates are short: what works, what remains, the next action.
- Answer the question that was asked.
- Be able to restate the project's objective and key criterion at any time.

**Why.** The lead judges on the evidence. An explanation without a result, a page that does not open or an off-topic
answer forces follow-ups and erodes trust.

**How.** See [communication](workflow/10-communication.md).

---

<a id="p15"></a>

## P15. The latest explicit instruction wins; keep an instruction register

**Statement.** Instructions evolve: a request can explicitly replace another. Keep a **register of active
instructions**, with their date and what they replace. Before presenting an iteration as finished, check that each of
its requests has been handled.

**Why.** An old instruction applied out of inertia contradicts the current direction. A request forgotten in the
middle of a long list is the most frustrating defect for the lead.

**How.** A [register](../templates/instruction-register.md), reviewed at every resume and before every report. The
report restates every request with one status: *done*, *trial rejected (reason)* or *missing*. When an instruction
changes, look for **all** its traces (texts, mentions, settings).

---

<a id="p16"></a>

## P16. Every element has a role; the subject stays at the centre

**Statement.** In a composition, every important element receives a **role**: draw the eye, fragment, add depth, keep
a reading area clear. Effects accompany the subject without competing with it. Motions are coordinated without being
synchronized, without constant agitation. This principle is about the **method** of composition: the roles themselves
and their dosage are decisions of each project, taken by the lead.

**Why.** An effect without a role dilutes attention; identical oscillations everywhere produce mechanical motion.

---

## What the principles do not cover

The principles say nothing about a project's style, formats or tools. Those choices are inputs of each project and are
recorded in its own decisions ([decision 0002](decisions/0002-method-separate-from-aesthetics.md)).
