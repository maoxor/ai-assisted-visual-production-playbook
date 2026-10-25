# Video for a web page

Details and reasons: [web video guide](../../domains/web-background-video.md).

## Exports

- [ ] Variants per **framing** and per **resolution actually displayed**, not just "mobile / desktop".
- [ ] Codecs: an efficient format (AV1), a format for Apple (HEVC, pre-compensated if needed), a universal fallback
      (H.264).
- [ ] Bitrates or CRF chosen from a measured comparison (VMAF or other) on the difficult passages, **on the final
      sequence**.
- [ ] A single keyframe per loop if the scene flickers, or a justified choice.
- [ ] Consistent colour metadata; colour rendering checked in WebKit.
- [ ] Blacks without banding; micro-details and motion preserved (side-by-side review).
- [ ] Encoded loop seam measured: no visible jump when returning to the first frame.
- [ ] Each file fully decoded (expected frame count).
- [ ] Posters (first frame) in modern formats and a fallback; weight within budget.

## Integration

- [ ] The page is usable and good-looking **without** the video; the poster is the main element (LCP).
- [ ] Video loaded after the priority resources; started only if playback can happen without stalling.
- [ ] `muted`, `playsinline`, `loop`; autoplay refused → poster, then playback on the first gesture.
- [ ] `prefers-reduced-motion` → still image, no video downloaded.
- [ ] Pause button (WCAG 2.2.2: animation longer than 5 s); choice remembered.
- [ ] Paused off screen and when the tab is hidden; resumed on return.
- [ ] Rotation, resizing, split screen: no black screen, a single new request, position in the loop kept, no
      variant ping-pong.
- [ ] Touch devices capped at a reasonable resolution; never the heaviest file by default.
- [ ] Test server with **range requests** (otherwise Safari and iOS refuse the MP4).
- [ ] Failures (video not found, codec refused): the poster stays, no script error.

## Tests

- [ ] Real / emulated matrix written; what cannot be tested is listed.
- [ ] Physical devices tested with the [procedure](../../domains/web-background-video.md#physical-devices), or the
      absence of physical tests stated in the report.
- [ ] Dropped frames, intervals at the seams, stalls, long tasks, CLS, bytes downloaded: measured in each engine.
- [ ] **Each delivered codec played at least once** by an engine, fallback included (force the codec if needed).
- [ ] Tests rerun on the **final exports**, not only on provisional ones.
- [ ] Results under load kept apart from an idle machine; a loss blamed on the environment only with evidence (an A/B
      on older exports, for example).
