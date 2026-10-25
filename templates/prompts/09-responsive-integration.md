# Responsive integration: rotation, tablets, split screen

```markdown
Check that our integration also covers **screen rotation on mobile and display on tablets**, taking framing, loading
and performance into account.

Define and then test the behaviour in each situation: phone portrait and landscape; tablet portrait and landscape;
rotation during loading or playback; resizing and split screen.

Choose the variants from the dimensions and aspect ratio of the displayed area, rather than from a "mobile or desktop"
distinction. Check whether the existing variants are enough or whether an intermediate variant is really needed.

Preserve the composition: <important elements> visible, room for the interface, no stretching, controlled cropping.

During a rotation: no black screen, no repeated source changes, no unnecessary downloads or disruptive restart. If a
change is needed, a clean transition keeping the position <in the loop>.

Adapt resolution and bitrate to capabilities: a high-density device must not automatically receive the heaviest file.
Provide a still fallback.

State precisely what is already covered, what is missing and what remains to test. A table of the formats, framings
and sources kept; check smoothness and responsiveness before, during and after rotation. Separate physical devices
from emulation.
```
