# Anti-patterns

Classic mistakes of a collaboration between a lead and an agent, each with its symptom, cost and prevention. All are
**[proven]**: they were made, then corrected, in real conditions. The most expensive come first.

Format: **symptom** → **cost** → **prevention**.

---

<a id="a1"></a>

### A1. Presenting stills when motion is expected

- **Symptom.** The approval is about an animated piece, and the agent presents images.
- **Cost.** Repeated follow-ups, loss of trust.
- **Prevention.** The validation deliverable has the shape of the final deliverable: a real continuous excerpt, with
  the delivery settings. Stills complement a video; they do not replace it ([P8](../principles.md#p8)).

<a id="a2"></a>

### A2. Forgetting a requested fix

- **Symptom.** A request was part of a long message, often next to an order to launch, and was not handled.
- **Cost.** Production to relaunch, frustration.
- **Prevention.** Instruction register; before any long launch and before every report, restate each request with its
  status ([P15](../principles.md#p15)).

<a id="a3"></a>

### A3. Leaving a leftover in the deliverables

- **Symptom.** A signature, a logo, a provisional mention ("demo", "rights not confirmed") or a trial setting remains in
  a deliverable or in the integration page, sometimes after an instruction changed.
- **Cost.** A visible defect discovered by the lead.
- **Prevention.**
  - A leftover check is part of every delivery checklist. Look for **where** an element is added (computation,
    post-processing, page), not only whether it is visible ([delivery checklist](checklists/delivery.md)).
  - Such an addition can be switched off in the configuration, and its absence is checked on every unit.
  - When an instruction changes, look for **all** its traces: texts, mentions, settings.

<a id="a4"></a>

### A4. Letting production cost drift until iteration is impossible

- **Symptom.** Settings pile up (samples, supersampling, invisible micro-details) until a few seconds take hours to
  compute.
- **Cost.** No iteration possible within the deadline.
- **Prevention.** The cost per unit is tracked at every iteration; any increase is justified visually; a cost profile
  precedes production ([P13](../principles.md#p13)).

<a id="a5"></a>

### A5. Presenting an imperceptible change

- **Symptom.** "I can't see any difference": the modified details are too small for the display size.
- **Prevention.** Before presenting, check yourself, at final size and normal speed, that the difference is visible;
  work at a perceptible scale.

<a id="a6"></a>

### A6. Comparing with an old version instead of the latest

- **Symptom.** Tables and messages take a past version as the yardstick.
- **Prevention.** Absolute values on the current version, before and after the fix. A past version is the yardstick
  only on request. A solution measured on an old state is revalidated on the current state.

<a id="a7"></a>

### A7. Back-and-forth review videos

- **Symptom.** Comparisons play 0 → n → 0, which hides the real motion and the seam.
- **Prevention.** Forward playback only, looping, on the whole piece
  ([`review_video.py`](../../tools/README.md#review_videopy)).

<a id="a8"></a>

### A8. Delegating to sub-agents against the lead's preference

- **Symptom.** The agent splits research among sub-agents while the lead wants it to do the research itself.
- **Prevention.** Research done by the agent, running tool calls in parallel
  ([decision 0003](../decisions/0003-no-subagents.md)). More generally: honour the delegation preference recorded in
  the instruction register.

<a id="a9"></a>

### A9. Taking a parameter without effect for a fix

- **Symptom.** A parameter has been set for several versions to fix a defect, but it does not act in the project's
  conditions (for example a specular setting on a fully transmissive surface).
- **Prevention.** Check the meaning and effect of each parameter **in the engine and version in use**: measure the
  result, do not settle for setting the value.

<a id="a10"></a>

### A10. Silent configuration error

- **Symptom.** A key ends up in the wrong section after a structural edit (TOML table order, for example), and several
  trials are run without it.
- **Prevention.** After any structural edit of the configuration, run a semantic diff against the archived version:
  only intended changes may appear.

<a id="a11"></a>

### A11. Non-deterministic seed

- **Symptom.** The same procedural element differs from one build to the next, because its seed comes from an unstable
  function (Python's `hash()` changes with every process) or from iteration order.
- **Prevention.** Every seed derives from a stable value (name, number, CRC32 of a string); a rebuild test checks
  bit-for-bit identity.

<a id="a12"></a>

### A12. Defending your artistic recommendation against the lead's choice

- **Symptom.** The agent recommends a restrained treatment, measurements in hand, while the lead prefers the rich
  version.
- **Prevention.** Propose contrasting variants, present measurements as checks and not as arguments; the final choice
  belongs to the lead.

<a id="a13"></a>

### A13. Showing a version with an undetected defect

- **Symptom.** A generated geometry has flipped normals or is not closed; the defect is discovered after the
  presentation.
- **Prevention.** An automatic validity check on any generated geometry (orientation from the signed volume, closure,
  intersections). A defect discovered afterwards is always reported, with a before/after of the fix.

<a id="a14"></a>

### A14. Judging stability on degraded previews

- **Symptom.** Low-sample previews strongly exaggerate flicker and skew the decision.
- **Prevention.** Noise and flicker are judged at final quality and final size. Previews are for motion and
  composition.

<a id="a15"></a>

### A15. Letting the machine sleep during a long computation

- **Symptom.** A laptop switches to battery with the lid closed, and a few minutes of computation take hours.
- **Prevention.** Before a long computation, check power, sleep settings and disk space; launch through a script that
  waits for mains power; choose a resumable pipeline ([production](../workflow/06-production.md)).

<a id="a16"></a>

### A16. Taking an aberrant first timing for the truth

- **Symptom.** The first unit includes preparation (loading, compilation) or the machine is busy; the announced time is
  wrong.
- **Prevention.** Measure again any surprising timing, cross-check on an idle machine, separate the first unit from the
  steady state.

<a id="a17"></a>

### A17. Leaving a misunderstanding of an ambiguous instruction

- **Symptom.** An instruction allowed two readings (orientation of a face or direction of a relief, for example) and
  the agent handled the wrong one.
- **Prevention.** Write down what you understood, handle the most likely reading, flag the other one in the report.

<a id="a18"></a>

### A18. Copying checks that no longer fit

- **Symptom.** After a change of scope (a static subject becomes animated, for example), the inherited checks produce
  false positives or no longer check anything useful.
- **Prevention.** At every change of scope, reread the inherited checks and adapt them.

<a id="a19"></a>

### A19. Announcing that a file or page is open when it is not

- **Symptom.** "The page did not open."
- **Prevention.** Check that opening succeeded (process, window, URL); otherwise give the exact path.

<a id="a20"></a>

### A20. Proposing art directions without ambition

- **Symptom.** Several rounds of proposals are rejected because they rework the existing state instead of aiming at the
  best references of the domain (space, motion, responses to actions, real 3D when it serves).
- **Prevention.** Set the bar at the best references of the domain; prototype in motion and record it before
  concluding.

<a id="a21"></a>

### A21. Every check passes on a rudimentary result

- **Symptom.** All automated checks are green, yet the result is sketchy: parts missing or rudimentary, details
  unreadable. The checks only measured global properties.
- **Cost.** A delivery that does not meet the bar; a second full pass.
- **Prevention.** Before generating, write an inventory of the expected features, each with an independent
  measurement, a threshold and a review view; a written review note per feature after reading its close-up next to
  the reference; a feature judged "sketchy" or "absent" blocks delivery ([P1](../principles.md#p1)).

<a id="a22"></a>

### A22. A measurement reported without a threshold

- **Symptom.** A tool has computed and written a measurement in its report for several versions, but nothing compares
  it with a limit; the defect it reveals goes unnoticed.
- **Cost.** A known-but-unread defect reaches the deliverable.
- **Prevention.** A measurement enters a gate (threshold, exit code) or it does not count; measure on the delivered
  file, not on an intermediate.

---

## Adding an anti-pattern

As soon as a mistake is corrected in a project: open a **Lesson learned** issue, then add the entry here in **generic**
form, with no project name or deliverable detail ([`CONTRIBUTING.md`](../../CONTRIBUTING.md)). A mistake that repeats
becomes a rule in a principle, a workflow step or a checklist.
