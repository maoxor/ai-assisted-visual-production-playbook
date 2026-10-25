# Background video for the web

Practices **[proven]** unless stated otherwise. Associated checklist: [`web-video.md`](../quality/checklists/web-video.md).

## Guiding principle

**The video is scenery: the page must be usable and good-looking without it.** The poster (first frame) is displayed
at once and is the main element (LCP). The video takes its place only when it can play without stalling; on failure,
the poster stays.

## Three families of defects, measured separately

1. **In the rendered frames** (flicker, noise): measured on the source frames before any encoding. A defect present
   here is not an encoding problem.
2. **Introduced by encoding** (blocks, banding in the blacks, lost micro-details, quality jump at the seam): decoded
   video compared with the sources frame by frame (VMAF, XPSNR, CAMBI, temporal acceleration) and side-by-side review.
3. **At playback** (decoding, network, browser, page load): dropped frames (`getVideoPlaybackQuality`), regularity and
   seam (`requestVideoFrameCallback`), stalls, long tasks, LCP, CLS, bytes downloaded.

## Exports

- **Variants per framing and per resolution actually displayed** (for example 1440p, 1080p and 720p in landscape; 1080
  and 720 wide in portrait). Downscaling in linear light (Lanczos).
- **Three codecs, in order of preference** (starting settings, to be validated by measurement on each project):

  | Codec | For whom | Starting point |
  |---|---|---|
  | AV1 10-bit (SVT-AV1) | Recent Chrome, Firefox, Android | `-preset 4 -pix_fmt yuv420p10le -svtav1-params tune=0:enable-overlays=1:scd=0:film-grain=0`, CRF around 34 |
  | HEVC 10-bit, `hvc1` | Safari and iOS browsers | `-preset slow -x265-params aq-mode=3:psy-rd=1.5:psy-rdoq=1.0:no-open-gop=1`, CRF around 27 |
  | H.264 8-bit | Universal fallback | `-preset slow -profile:v high -x264-params aq-mode=3:aq-strength=0.9:deblock=-1,-1`, CRF around 23 |

- **A single keyframe per loop** (`-g` equal to the frame count) for a scene that flickers: no quality pumping at each
  group of pictures. Then measure the encoded seam (the keyframe is often slightly sharper) and check that it stays
  invisible.
- **BT.709 metadata, limited range**, no audio, `+faststart`.
- **Files named by content hash** ("immutable" caching) and a JSON manifest inlined in the page.
- **CRF chosen on the final sequence**, from a comparison of perceived quality (VMAF) and weight, not on a provisional
  excerpt.
- **Temporal stabilization also saves weight**: frame-to-frame noise costs bits; stabilizing before encoding reduces
  the weight at equal quality.

## Colour in Apple browsers

Observation **[proven]** in WebKit on macOS: Apple's video stack converts video with a gamma of about 1.96 instead of
the sRGB curve, which brightens midtones, whatever the codec; the transfer tag has no effect. The HEVC stream, served
only to Apple browsers, can be pre-compensated:

```
v = (sRGB→linear(x))^(1/1.961)
ffmpeg -vf "format=rgb48le,lutrgb=r='EXPR':g='EXPR':b='EXPR'"
EXPR = clip(maxval*pow(if(lte(val/maxval,0.04045),(val/maxval)/12.92,pow(((val/maxval)+0.055)/1.055,2.4)),1/1.961),0,maxval)
```

Always measure the on-screen difference (capture of the page compared with the poster) before and after compensation.
Not verified on physical iPhones or iPads: retest on each project.

## Starting budgets

Ceilings to confront with the quality obtained, to be adjusted with a justification.

| Budget | Value | Reason |
|---|---|---|
| Mobile poster (AVIF) | 90 to 150 KB | Slow 4G: LCP ≤ 2.5 s |
| Desktop poster (AVIF) | 150 to 300 KB | Fixed network |
| Initial weight excluding video | ≤ 250 KB mobile, ≤ 400 KB desktop | The video is requested only after `load` |
| Background script | ≤ 6 KB compressed, no library | Native browser capabilities |
| 720p bitrate | ≤ 1.5 Mb/s | Progressive playback on ordinary 4G |
| 1080p bitrate | ≤ 3 Mb/s | More comfortable devices |
| 1440p bitrate | ≤ 5 Mb/s | Dense screens, fixed network |
| Smoothness | 0 dropped frames over 3 loops (desktop, hardware decoding); ≤ 1 % on emulated mobile | No stutter |
| Cost for the page | No long task caused by the background, CLS = 0 | The video blocks nothing |

## Integration

- Choose the variant from the **aspect ratio of the displayed area**, with a neutral zone (between 0.9 and 1.1) to
  avoid ping-pong in split screen, and from a **capped density** (touch devices limited to 1080p, for example).
- Choose the codec with `canPlayType` and Media Capabilities; serve the pre-compensated stream to Apple browsers only.
- Load after the priority resources; start only if loading is ahead of playback.
- `muted playsinline loop`; autoplay refused → poster, then playback on the first gesture.
- `prefers-reduced-motion` → still image, no video downloaded.
- **Pause button** (WCAG 2.2.2), choice remembered.
- Pause when out of view (IntersectionObserver) and when the tab is hidden (Page Visibility).
- **Rotation**: the current video keeps playing, recropped, while the new variant loads; the new one resumes at the
  same position in the loop, then a short crossfade makes the transition. A single new request; never a downgrade on a
  mere resize.
- **Do not rely on `navigator.connection.downlink`**: without history, some browsers report a low default bitrate and
  trigger a wrongful downgrade.
- Expose the engine state in `data-*` attributes (variant, codec, playback state, reason for a fallback) and provide a
  `?debug` mode (variant, codec, dropped frames, stalls, loop cycles).

## Tests

- **A local server with range requests** (`Range`): with `python -m http.server`, Safari and iOS refuse the MP4. A
  local-network listening option allows testing a real phone without publishing anything.
- **A Playwright bench**: installed Chrome (real hardware decoding), WebKit and Firefox; iPhone and Android emulation;
  throttled network; reduced motion; autoplay refused; video not found; scrolling; hidden tab; rotation; CLS; three loop
  cycles measured frame by frame.
- **A real / emulated matrix** written down. Not testable without hardware: real phones and tablets, Windows, real
  mobile networks.
- **Each delivered codec played at least once**: the fallback is often chosen by no engine of the bench; force it
  (`?codec=h264`) to really play it.
- **Under load**, an engine can drop many frames; before blaming the files, rerun the test on an idle machine or A/B
  against older exports.
- **Test the final exports**: the weight and behaviour of provisional exports are not representative.
