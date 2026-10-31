# Audio DSP Icon Set
## Design Specification

## 1. Overview

Create a cohesive set of four minimalist, monochromatic vector line art icons representing fundamental audio DSP operations.

The icons, in order, are:

1. **Oscillator:** Sinusoidal waveform
2. **Envelope:** ADSR amplitude envelope
3. **Filter:** Resonant low pass frequency response
4. **Delay:** Pure temporal signal displacement

Each icon should communicate its function through a recognizable signal shape rather than a metaphorical object.

The visual language should be precise, geometric, minimal, and consistent across the set.

The icons must remain recognizable at small presentation sizes.

## 2. Shared Design System

### 2.1 Canvas and Coordinate System

Each icon occupies an identical square canvas enclosed by a square border.

Use a normalized coordinate system:

- Horizontal axis: x = 0 to 1, increasing left to right.
- Vertical axis: y = 0 to 1, increasing bottom to top.
- Origin: Bottom left corner of the square border.
- All specified coordinates refer to the square border, not the overall image dimensions.

The border defines the common visual bounds of all four icons.

Maintain identical border dimensions, placement, and proportions throughout the set.

### 2.2 Stroke Specifications

All icons inherit their stroke properties from the existing icon design system.

This includes:

- Stroke width
- Line caps
- Line joins
- Border treatment
- Antialiasing
- Scaling behavior

Do not independently introduce different stroke weights or stylistic treatments for individual icons.

Use clean vector paths with smooth curves where appropriate.

Avoid unnecessary detail, ornamentation, gradients, shadows, text, labels, arrows, or decorative elements.

### 2.3 Visual Consistency

The four icons should appear to belong to the same family.

Maintain consistent:

- Square border dimensions
- Stroke treatment
- Visual density
- Overall scale
- Geometric precision
- Curve smoothness
- Negative space distribution

Each icon should have a strong, recognizable silhouette.

Favor mathematical clarity over decorative interpretation.

All signal paths must remain inside their respective square borders, with sufficient clearance to prevent visible clipping or unintended contact.

Where a signal intentionally meets the border, its endpoint should align precisely with the border.

Unless otherwise specified, all elements use 100% stroke intensity.

## 3. Icon 1: Oscillator

### 3.1 Concept

Represent a sinusoidal audio oscillator using a continuous, constant amplitude sine wave.

The icon should immediately communicate periodic oscillation.

### 3.2 Geometry

Draw a smooth sinusoidal waveform.

Waveform parameters:

- **Number of cycles:** 2 complete cycles.
- **Waveform extent:** x = 0 to x = 1. The waveform touches the left and right borders.
- **Amplitude:** ±0.35 of the square height.
- **Positive peaks:** y = 0.85.
- **Negative troughs:** y = 0.15.
- **Stroke intensity:** 100%.

The waveform begins and ends at zero crossings on the left and right borders.

Do not draw a zero baseline.

Use a mathematically accurate sinusoid with constant amplitude and frequency.

### 3.3 Visual Requirements

- Exactly two complete oscillations.
- Equal positive and negative excursions.
- Uniform horizontal spacing between peaks.
- Smooth curvature throughout.
- No amplitude modulation, frequency modulation, or distortion.
- No discontinuities or additional waveform components.

The oscillator should appear stable, continuous, and periodic.

### 3.4 Design Intent

Communicate the generation of a periodic signal.

The sine wave is the primary visual element.

Avoid speaker symbols, musical notes, knobs, or other metaphorical representations of sound generation.

## 4. Icon 2: Envelope (ADSR)

### 4.1 Concept

Represent a conventional four stage ADSR amplitude envelope:

1. Attack
2. Decay
3. Sustain
4. Release

The icon should resemble the familiar envelope graphs found in synthesizers and audio production software.

### 4.2 Geometry

Draw a single continuous piecewise linear envelope consisting of four distinct stages.

Use the following normalized coordinates:

| Point | X | Y | Function |
|---|---:|---:|---|
| Start | 0.00 | 0.12 | Initial zero amplitude at left border |
| Attack peak | 0.25 | 0.88 | Maximum amplitude |
| Decay end | 0.42 | 0.55 | Sustain level reached |
| Sustain end | 0.72 | 0.55 | End of sustain |
| Release end | 1.00 | 0.12 | Return to zero amplitude at right border |

Connect the points in order.

### 4.3 Stage Characteristics

**Attack**

A steep, straight ascending segment from the initial baseline to maximum amplitude.

**Decay**

A descending segment from the attack peak to the sustain level.

The decay should be visibly less steep than the attack.

**Sustain**

A clearly identifiable horizontal plateau.

The sustain level should be substantially below the attack peak but above the initial baseline.

**Release**

A descending segment from the sustain plateau back to the initial baseline.

The release should be visually distinct from the decay.

### 4.4 Visual Requirements

- **Stroke intensity:** 100%.
- One continuous envelope path.
- Four clearly recognizable stages.
- No labels, stage markers, or control points.
- No overshoot, resonance, or oscillation.
- Straight segments with geometrically precise transitions.

The envelope spans the full square width. It meets the left and right borders at zero amplitude.

### 4.5 Design Intent

Communicate amplitude shaping over time.

The silhouette should be recognizable to anyone familiar with synthesizer envelopes.

Avoid additional axes, numerical markings, or annotations.

## 5. Icon 3: Filter (Resonant Low Pass)

### 5.1 Concept

Represent the magnitude response of a resonant low pass filter.

The response should feature:

1. A flat low frequency passband.
2. A small resonant bump near the cutoff frequency.
3. A straight, uniform rolloff into the high frequency stopband.

The resonant Q bump is an essential feature.

### 5.2 Geometry

Draw one continuous response path with three parts: a flat passband line, a small smooth resonance bump, and a straight stopband slope.

Use the following normalized control points:

| Region | X | Y | Description |
|---|---:|---:|---|
| Passband start | 0.00 | 0.70 | Flat response at left border |
| Passband end | 0.40 | 0.70 | End of flat passband |
| Resonance peak | 0.50 | 0.78 | Wide, small rounded bump |
| Rolloff start | 0.60 | 0.72 | Start of stopband slope |
| Stopband end | 1.00 | 0.12 | End of uniform slope at right border |

Use a straight line for the passband. Use cubic Bezier segments for the bump. Use a straight line for the stopband. Keep the full path continuous. Do not split it into separate mobjects.

### 5.3 Passband

The passband is flat. It spans x = 0.00 to x = 0.40 at y = 0.70.

It meets the left border.

It represents frequencies passed without attenuation.

### 5.4 Resonant Q Peak

Use a wide, small, rounded bump at the cutoff.

The peak is at x = 0.50, y = 0.78.

The bump ends at x = 0.60, y = 0.72.

The bump must have a single local maximum. Do not add ringing or multiple peaks.

Keep the bump small and wide. It must not dominate the flat passband.

### 5.5 Rolloff

The stopband is a straight line. It runs from x = 0.60, y = 0.72 to x = 1.00, y = 0.12.

The slope is uniform.

It meets the right border.

The line must not curve or wobble.

### 5.6 Visual Requirements

- **Stroke intensity:** 100%.
- One continuous response silhouette: flat passband, smooth bump, straight slope.
- No numerical axes, tick marks, or frequency labels.
- No additional filter bands.
- No multiple resonance peaks.
- No phase response curve.

### 5.7 Design Intent

Communicate frequency selective attenuation with a resonant cutoff.

The silhouette should be immediately recognizable as a synthesizer style resonant low pass filter.

The resonant bump provides the characteristic visual identity.

## 6. Icon 4: Delay (Pure Temporal Displacement)

### 6.1 Concept

Represent a pure temporal delay using two identical single cycle sine wave pulses, separated horizontally in time.

The icon must not suggest an echo, feedback loop, repeated signal, or decaying sequence.

The original signal appears first.

The delayed signal appears later, with identical waveform geometry.

A slight vertical separation and reduced stroke intensity distinguish the delayed signal from the original.

### 6.2 Geometry

Draw two identical, horizontally separated, single cycle sine wave pulses.

Each pulse consists of exactly:

1. One positive half cycle.
2. One negative half cycle.
3. A zero crossing at the beginning.
4. A zero crossing at the midpoint.
5. A zero crossing at the end.

Both waveforms have:

- Identical shape.
- Identical frequency.
- Identical amplitude.
- Identical horizontal duration.
- Smooth sinusoidal curvature.
- No additional oscillations.

### 6.3 Common Waveform Parameters

- **Peak to peak amplitude:** 85% of the square's height.
- **Amplitude:** ±0.425 from the respective zero baseline.
- **Horizontal duration:** 16% of the square's width.
- **Waveform type:** Exactly one complete sine cycle.
- **Zero baselines:** Horizontal lines extending across the entire square, from x = 0 to x = 1.

The two waveforms overlap in vertical range but do not overlap horizontally.

### 6.4 Original Signal (Upper)

- **Stroke intensity:** 100%.
- **Zero baseline:** y = 0.55.
- **Waveform begins:** x = 0.20.
- **Waveform ends:** x = 0.36.
- **Positive peak:** y = 0.975.
- **Negative trough:** y = 0.125.

The baseline remains perfectly horizontal before and after the waveform.

The waveform begins with a positive excursion and completes exactly one sinusoidal cycle.

### 6.5 Delayed Signal (Lower)

- **Stroke intensity:** 50%.
- **Zero baseline:** y = 0.45.
- **Waveform begins:** x = 0.64.
- **Waveform ends:** x = 0.80.
- **Positive peak:** y = 0.875.
- **Negative trough:** y = 0.025.

The baseline remains perfectly horizontal before and after the waveform.

The delayed waveform is geometrically identical to the original.

Only its horizontal position, vertical baseline, and stroke intensity differ.

### 6.6 Relative Positioning

The two zero baselines are separated vertically by exactly 10% of the square's height.

The delayed waveform is displaced horizontally to the right by 44% of the square's width.

Both zero baselines extend from the left border to the right border.

The upper waveform approaches the top border.

The lower waveform approaches the bottom border.

Neither waveform may cross or touch the border.

Preserve the specified amplitude and baseline positions while ensuring the rendered strokes do not visually clip against the border.

### 6.7 Stroke Intensity

The original signal uses 100% foreground intensity.

The delayed signal uses 50% foreground intensity.

Apply these intensities to the entire respective signal, including its horizontal zero baseline.

The square border remains at 100% foreground intensity.

### 6.8 Mathematical Definition

Let the normalized horizontal coordinate be x.

Define a single cycle sine pulse:

`P(x, s, w) = sin(2π(x − s)/w)` when `s ≤ x ≤ s + w`, and `0` otherwise.

The original signal is:

`y₁(x) = 0.55 + 0.425 × P(x, 0.20, 0.16)`

The delayed signal is:

`y₂(x) = 0.45 + 0.425 × P(x, 0.64, 0.16)`

Render both functions across the full horizontal interval x = 0 to 1.

This construction guarantees identical waveform geometry, exact single cycle oscillations, and full width zero baselines.

### 6.9 Design Intent

Communicate **a signal being displaced forward in time without alteration**.

The earlier, full intensity waveform represents the original signal.

The later, reduced intensity waveform represents the delayed signal.

The vertical separation distinguishes the two signals visually.

Their identical shapes communicate signal preservation.

Avoid all visual conventions associated with:

- Echo
- Feedback
- Repetition
- Decay
- Reverb
- Phase modulation
- Recirculation

Do not add arrows, clocks, feedback loops, multiple delayed copies, or attenuation envelopes.

## 7. Final Implementation Requirements

### 7.1 Vector Construction

Prefer SVG or an equivalent resolution independent vector format.

Use mathematical paths for the sine waves and smooth response curves.

Avoid raster approximations where vector geometry is practical.

All four icons should use a common viewBox and consistent border geometry.

### 7.2 Visual Validation

Verify that:

1. All four icons use identical square borders and shared stroke specifications.
2. All elements remain within their intended bounds without clipping.
3. The oscillator contains exactly two complete sine cycles.
4. The envelope clearly expresses attack, decay, sustain, and release.
5. The filter includes one small rounded resonant bump followed by a straight uniform rolloff.
6. The delay contains exactly two identical single cycle sine pulses.
7. The delay's zero baselines extend across the full square width.
8. The delay's original and delayed signals use 100% and 50% stroke intensity, respectively.
9. All icons remain legible at their intended presentation sizes.

### 7.3 Deliverables

Produce four individual vector icons in this exact order:

1. `oscillator`
2. `envelope`
3. `filter`
4. `delay`

Each icon must be independently usable while preserving the shared design system.

Do not introduce additional symbols, labels, or decorative treatments.

The final result should feel like a unified family of technical audio DSP symbols suitable for a professional presentation.

## 8. Implementation

These functions are defined in `03_engine_deep_dive.py`. Each function returns a square `VGroup`. Set `size` to change the icon size.

```python
import numpy as np
from manim import *

ICON_STROKE = 4.0


def icon_point(size, x, y):
    return np.array([(x - 0.5) * size, (y - 0.5) * size, 0.0])


def make_icon_frame(size=2.4):
    return Square(
        side_length=size,
        stroke_color=WHITE,
        stroke_width=ICON_STROKE,
        fill_opacity=0.0,
    )


def make_oscillator_icon(size=2.4):
    frame = make_icon_frame(size)
    wave = ParametricFunction(
        lambda t: icon_point(
            size,
            t,
            0.50 + 0.35 * np.sin(2 * TAU * t),
        ),
        t_range=[0, 1],
        color=WHITE,
        stroke_width=ICON_STROKE,
    )
    return VGroup(frame, wave)


def make_adsr_icon(size=2.4):
    frame = make_icon_frame(size)
    envelope = VMobject(color=WHITE, stroke_width=ICON_STROKE)
    envelope.set_points_as_corners(
        [
            icon_point(size, 0.0, 0.12),
            icon_point(size, 0.25, 0.88),
            icon_point(size, 0.42, 0.55),
            icon_point(size, 0.72, 0.55),
            icon_point(size, 1.0, 0.12),
        ]
    )
    return VGroup(frame, envelope)


def make_filter_icon(size=2.4):
    frame = make_icon_frame(size)
    response = VMobject(color=WHITE, stroke_width=ICON_STROKE)
    response.start_new_path(icon_point(size, 0.0, 0.70))
    response.add_line_to(icon_point(size, 0.40, 0.70))
    response.add_cubic_bezier_curve_to(
        icon_point(size, 0.43, 0.70),
        icon_point(size, 0.47, 0.78),
        icon_point(size, 0.50, 0.78),
    )
    response.add_cubic_bezier_curve_to(
        icon_point(size, 0.53, 0.78),
        icon_point(size, 0.57, 0.765),
        icon_point(size, 0.60, 0.72),
    )
    response.add_line_to(icon_point(size, 1.0, 0.12))
    return VGroup(frame, response)


def make_delay_icon(size=2.4):
    frame = make_icon_frame(size)

    def pulse(x, start, width):
        if start <= x <= start + width:
            return np.sin(TAU * (x - start) / width)
        return 0.0

    def signal(baseline, start, opacity):
        path = ParametricFunction(
            lambda t: icon_point(
                size,
                t,
                baseline + 0.425 * pulse(t, start, 0.16),
            ),
            t_range=[0, 1],
            color=WHITE,
            stroke_width=ICON_STROKE,
            use_smoothing=False,
        )
        path.set_stroke(opacity=opacity)
        return path

    original = signal(0.55, 0.20, 1.0)
    delayed = signal(0.45, 0.64, 0.5)
    return VGroup(frame, original, delayed)
```

Use this layout for the primitives slide:

```python
icons = VGroup(
    make_oscillator_icon(size=2.8),
    make_adsr_icon(size=2.8),
    make_filter_icon(size=2.8),
    make_delay_icon(size=2.8),
).arrange_in_grid(rows=2, cols=2, buff=(1.4, 0.6))
```