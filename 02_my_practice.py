from manim import *
from manim_slides import Slide

from lib import ACCENT, MUTED, bullet_rows, slide_title


START_COLOR = ManimColor("#2E7D32")
DURATION_COLOR = ManimColor("#E65100")
PITCH_COLOR = ManimColor("#00695C")
ROLL_BACKGROUND = ManimColor("#A0A0A0")
PIANO_ROLL_X_LEFT = -5.9
PIANO_ROLL_X_RIGHT = 2.3
PIANO_ROLL_Y_BOTTOM = -2.5
PIANO_ROLL_Y_TOP = 2.3
PIANO_ROLL_LOW_MIDI = 60
PIANO_ROLL_HIGH_MIDI = 84
PIANO_ROLL_BEATS = 4


def make_table(pos, n_rows=1, headers=("Start", "Duration", "Note")):
    col_width = 1.3
    row_height = 0.5
    font_size = 18
    padding = 0.1
    width = col_width * len(headers)
    height = row_height * (2 + n_rows)

    table = VGroup()
    table.add(
        Rectangle(
            width=width,
            height=height,
            stroke_color=GREY_B,
            stroke_width=2,
        )
    )
    for i in range(1, 2 + n_rows):
        y = height / 2 - i * row_height
        table.add(
            Line(
                [-width / 2, y, 0],
                [width / 2, y, 0],
                color=GREY_B,
                stroke_width=2,
            )
        )
    for i in range(1, len(headers)):
        x = -width / 2 + i * col_width
        table.add(
            Line(
                [x, -height / 2, 0],
                [x, height / 2 - row_height, 0],
                color=GREY_B,
                stroke_width=2,
            )
        )

    title = Text("Note", font_size=font_size, weight=BOLD, color=MUTED)
    title.move_to(
        [-width / 2 + padding, height / 2 - row_height / 2, 0],
        aligned_edge=LEFT,
    )
    table.add(title)

    title_y = height / 2 - row_height * 1.5
    for i, header in enumerate(headers):
        label = Text(header, font_size=font_size, weight=BOLD, color=MUTED)
        label.move_to(
            [-width / 2 + i * col_width + padding, title_y, 0],
            aligned_edge=LEFT,
        )
        table.add(label)

    table.move_to([pos[0], pos[1], 0])
    cells = []
    top = pos[1] + height / 2
    for row in range(n_rows):
        y = top - (2 + row + 0.5) * row_height
        cells.append(
            [
                [pos[0] - width / 2 + i * col_width + padding, y, 0]
                for i in range(len(headers))
            ]
        )
    return table, cells


def build_piano_roll(
    x_left,
    x_right,
    y_bottom,
    y_top,
    low_midi=PIANO_ROLL_LOW_MIDI,
    high_midi=PIANO_ROLL_HIGH_MIDI,
    n_beats=PIANO_ROLL_BEATS,
):
    width = x_right - x_left
    height = y_top - y_bottom
    n_keys = high_midi - low_midi + 1
    row_h = height / n_keys
    beat_w = width / n_beats

    def px(beat):
        return x_left + beat * beat_w

    def py(midi):
        return y_bottom + (midi - low_midi + 0.5) * row_h

    base = Rectangle(
        width=width,
        height=height,
        fill_color=ROLL_BACKGROUND,
        fill_opacity=1,
        stroke_width=0,
    ).move_to([x_left + width / 2, (y_bottom + y_top) / 2, 0])

    grid = VGroup()
    labels = VGroup()

    black_classes = {1, 3, 6, 8, 10}
    key_width = 0.55

    keyboard = VGroup()
    keyboard.add(
        Rectangle(
            width=key_width,
            height=height,
            fill_color=GREY_A,
            fill_opacity=1,
            stroke_color=GREY_B,
            stroke_width=2,
        ).move_to([x_left - key_width / 2, (y_bottom + y_top) / 2, 0])
    )
    for i in range(n_keys + 1):
        y = y_bottom + i * row_h
        keyboard.add(
            Line(
                [x_left - key_width, y, 0],
                [x_left, y, 0],
                color=GREY_C,
                stroke_width=1,
            )
        )
    for midi in range(low_midi, high_midi + 1):
        if (midi - low_midi) % 12 in black_classes:
            black_width = key_width * 0.62
            keyboard.add(
                Rectangle(
                    width=black_width,
                    height=row_h * 0.9,
                    fill_color=GREY_D,
                    fill_opacity=1,
                    stroke_color=GREY_C,
                    stroke_width=1,
                ).move_to(
                    [x_left - key_width + black_width / 2, py(midi), 0]
                )
            )

    for midi in range(low_midi, high_midi):
        if (midi - low_midi) % 12 in black_classes:
            stripe = Rectangle(
                width=width,
                height=row_h,
                fill_color=GREY_B,
                fill_opacity=1,
                stroke_width=0,
            )
            stripe.move_to(
                [
                    x_left + width / 2,
                    y_bottom + (midi - low_midi + 0.5) * row_h,
                    0,
                ]
            )
            grid.add(stripe)

    for i in range(n_keys + 1):
        y = y_bottom + i * row_h
        grid.add(
            Line([x_left, y, 0], [x_right, y, 0], color=GREY_D, stroke_width=1)
        )

    for i in range(n_beats * 4 + 1):
        x = x_left + i * beat_w / 4
        grid.add(
            Line([x, y_bottom, 0], [x, y_top, 0], color=GREY_E, stroke_width=1)
        )

    for beat in range(n_beats + 1):
        x = px(beat)
        is_bar = beat % 4 == 0
        grid.add(
            Line(
                [x, y_bottom, 0],
                [x, y_top, 0],
                color=BLACK if is_bar else GREY_D,
                stroke_width=3 if is_bar else 2,
            )
        )

    for beat in range(n_beats):
        label = Text(str(beat), font_size=14, color=GREY_B)
        label.move_to([px(beat), y_bottom - 0.2, 0])
        labels.add(label)

    for midi in (60, 72, 84):
        label = Text(f"C{midi // 12 - 1}", font_size=16, color=MUTED)
        label.move_to([x_left - key_width - 0.25, py(midi), 0])
        labels.add(label)

    def note_rect(start_beat, duration, midi, color):
        x0 = px(start_beat)
        x1 = px(start_beat + duration)
        rect = Rectangle(
            width=x1 - x0,
            height=row_h * 0.8,
            fill_color=color,
            fill_opacity=1,
            stroke_color=color,
            stroke_width=2,
        )
        rect.move_to([(x0 + x1) / 2, py(midi), 0])
        return rect

    notes = [note_rect(beat, 0.5, 66, BLUE_E) for beat in range(n_beats)]

    return base, keyboard, grid, labels, notes, px, py, row_h, beat_w


class MyPractice(Slide):
    def construct(self):
        self.compositional_slide()
        self.wait()
        self.next_slide()

        self.clear()
        self.demo_slide()
        self.wait()
        self.next_slide()

        self.clear()
        self.code_slide()
        self.wait()
        self.next_slide()

        self.clear()
        self.composition_title_slide()
        self.wait()
        self.next_slide()

        self.clear()
        self.piano_roll_slide()
        self.next_slide()

        self.clear()
        self.pattern_morph_slide()
        self.next_slide()

        self.clear()
        self.tiling_slide()

    def compositional_slide(self):
        title = slide_title("Compositional, Not Live")

        production = Text("Production", font_size=44, weight=BOLD, color=ACCENT)
        versus = Text("vs.", font_size=30, color=MUTED)
        live = Text("Live Performance", font_size=44, weight=BOLD)

        columns = VGroup(production, versus, live).arrange(RIGHT, buff=1.0)
        columns.move_to(ORIGIN)

        self.add(title, columns)

    def demo_slide(self):
        title = slide_title("Demo: 067_dj_tool")

        rows = bullet_rows(
            [
                "Timeline",
                "Mixer, routing",
                "Subtractive, FM, Cymbal, FDN",
                "Mixer patch",
                "Export to .wav and .mp3",
            ]
        )
        rows.next_to(title, DOWN, buff=0.8)
        rows.move_to([0, rows.get_center()[1], 0])

        self.add(title, rows)

    def code_slide(self):
        title = slide_title("Composition Expressed in Code")

        rows = bullet_rows(
            [
                "The live UI is a helpful tool, not the authority.",
                "The authoritative representation of the song is the code.",
            ],
            font_size=26,
        )
        rows.next_to(title, DOWN, buff=0.8)
        rows.move_to([0, rows.get_center()[1], 0])

        self.add(title, rows)

    def composition_title_slide(self):
        title = slide_title("073_sync_conference", center=True)
        subtitle = Text("16 Bar Composition", font_size=36, color=MUTED)
        subtitle.next_to(title, DOWN, buff=0.35)

        self.add(VGroup(title, subtitle).move_to(ORIGIN))

    def piano_roll_slide(self):
        x_left = -5.9
        x_right = 2.3
        y_bottom = -2.5
        y_top = 2.3
        width = x_right - x_left
        height = y_top - y_bottom
        low_midi = 60
        high_midi = 84
        n_keys = high_midi - low_midi + 1
        row_h = height / n_keys
        n_beats = 4
        beat_w = width / n_beats

        def px(beat):
            return x_left + beat * beat_w

        def py(midi):
            return y_bottom + (midi - low_midi + 0.5) * row_h

        roll = VGroup()

        roll.add(
            Rectangle(
                width=width,
                height=height,
                fill_color=ROLL_BACKGROUND,
                fill_opacity=1,
                stroke_width=0,
            ).move_to([x_left + width / 2, (y_bottom + y_top) / 2, 0])
        )

        black_classes = {1, 3, 6, 8, 10}
        key_width = 0.55

        keyboard = VGroup()
        keyboard.add(
            Rectangle(
                width=key_width,
                height=height,
                fill_color=GREY_A,
                fill_opacity=1,
                stroke_color=GREY_B,
                stroke_width=2,
            ).move_to([x_left - key_width / 2, (y_bottom + y_top) / 2, 0])
        )
        for i in range(n_keys + 1):
            y = y_bottom + i * row_h
            keyboard.add(
                Line(
                    [x_left - key_width, y, 0],
                    [x_left, y, 0],
                    color=GREY_C,
                    stroke_width=1,
                )
            )
        for midi in range(low_midi, high_midi + 1):
            if (midi - low_midi) % 12 in black_classes:
                black_width = key_width * 0.62
                keyboard.add(
                    Rectangle(
                        width=black_width,
                        height=row_h * 0.9,
                        fill_color=GREY_D,
                        fill_opacity=1,
                        stroke_color=GREY_C,
                        stroke_width=1,
                    ).move_to(
                        [x_left - key_width + black_width / 2, py(midi), 0]
                    )
                )
        roll.add(keyboard)
        for midi in range(low_midi, high_midi):
            if (midi - low_midi) % 12 in black_classes:
                stripe = Rectangle(
                    width=width,
                    height=row_h,
                    fill_color=GREY_B,
                    fill_opacity=1,
                    stroke_width=0,
                )
                stripe.move_to(
                    [
                        x_left + width / 2,
                        y_bottom + (midi - low_midi + 0.5) * row_h,
                        0,
                    ]
                )
                roll.add(stripe)

        for i in range(n_keys + 1):
            y = y_bottom + i * row_h
            roll.add(
                Line([x_left, y, 0], [x_right, y, 0], color=GREY_D, stroke_width=1)
            )

        for i in range(n_beats * 4 + 1):
            x = x_left + i * beat_w / 4
            roll.add(
                Line([x, y_bottom, 0], [x, y_top, 0], color=GREY_E, stroke_width=1)
            )

        for beat in range(n_beats + 1):
            x = px(beat)
            is_bar = beat % 4 == 0
            roll.add(
                Line(
                    [x, y_bottom, 0],
                    [x, y_top, 0],
                    color=BLACK if is_bar else GREY_D,
                    stroke_width=3 if is_bar else 2,
                )
            )

        for beat in range(n_beats):
            label = Text(str(beat), font_size=14, color=GREY_B)
            label.move_to([px(beat), y_bottom - 0.2, 0])
            roll.add(label)

        for midi in (60, 72, 84):
            label = Text(f"C{midi // 12 - 1}", font_size=16, color=MUTED)
            label.move_to([x_left - key_width - 0.25, py(midi), 0])
            roll.add(label)

        def note_rect(start_beat, duration, midi, color):
            x0 = px(start_beat)
            x1 = px(start_beat + duration)
            rect = Rectangle(
                width=x1 - x0,
                height=row_h * 0.8,
                fill_color=color,
                fill_opacity=1,
                stroke_color=color,
                stroke_width=2,
            )
            rect.move_to([(x0 + x1) / 2, py(midi), 0])
            return rect

        notes = [note_rect(beat, 0.5, 66, BLUE_E) for beat in range(4)]
        note1 = notes[0]

        table, rows = make_table([4.8, 0.5], n_rows=4)

        self.add(roll, *notes)
        self.wait()
        self.next_slide()

        note1_left = px(0)
        note1_right = px(0.5)
        duration_y = py(66) + row_h * 1.6
        note1_bottom = py(66) - row_h * 0.4

        start_arrow = Arrow(
            start=[note1_left, note1_bottom - 0.05, 0],
            end=[note1_left, y_bottom - 0.08, 0],
            buff=0,
            color=START_COLOR,
            stroke_width=4,
            tip_length=0.2,
            max_tip_length_to_length_ratio=1,
        )
        duration_arrow = DoubleArrow(
            start=[note1_left, duration_y, 0],
            end=[note1_right, duration_y, 0],
            buff=0,
            color=DURATION_COLOR,
            stroke_width=4,
            tip_length=0.2,
            max_tip_length_to_length_ratio=1,
        )
        pitch_half = (py(66) - py(60)) / 2
        pitch_arrow = DoubleArrow(
            start=[note1_right + 0.2, py(66) - pitch_half, 0],
            end=[note1_right + 0.2, py(66) + pitch_half, 0],
            buff=0,
            color=PITCH_COLOR,
            stroke_width=4,
            tip_length=0.2,
            max_tip_length_to_length_ratio=1,
        )

        self.play(
            Create(start_arrow),
            Create(duration_arrow),
            Create(pitch_arrow),
            run_time=1.5,
        )

        start_value = Text(
            "0", font_size=18, color=START_COLOR, fill_opacity=1
        )
        start_value.next_to(start_arrow, RIGHT, buff=0.12)
        start_value.set_y((py(66) + y_bottom) / 2)

        duration_value = Text(
            "0.5", font_size=18, color=DURATION_COLOR, fill_opacity=1
        )
        duration_value.next_to(duration_arrow, UP, buff=0.18)

        pitch_value = Text(
            "F#4", font_size=20, color=PITCH_COLOR, fill_opacity=1
        )
        pitch_value.next_to(pitch_arrow, RIGHT, buff=0.08)

        self.add(start_value, duration_value, pitch_value)
        self.wait()
        self.next_slide()

        self.play(
            Transform(
                start_value,
                Text("0", font_size=18).move_to(rows[0][0], aligned_edge=LEFT),
            ),
            Transform(
                duration_value,
                Text("0.5", font_size=18).move_to(rows[0][1], aligned_edge=LEFT),
            ),
            Transform(
                pitch_value,
                Text("F#4", font_size=18).move_to(rows[0][2], aligned_edge=LEFT),
            ),
            FadeIn(table),
            FadeOut(start_arrow),
            FadeOut(duration_arrow),
            FadeOut(pitch_arrow),
            run_time=1.5,
        )
        self.wait()
        self.next_slide()

        remaining = []
        for note, start in zip(notes[1:], (1, 2, 3)):
            start_label = Text(
                str(start), font_size=18, color=START_COLOR, fill_opacity=1
            )
            duration_label = Text(
                "0.5", font_size=18, color=DURATION_COLOR, fill_opacity=1
            )
            pitch_label = Text(
                "F#4", font_size=18, color=PITCH_COLOR, fill_opacity=1
            )
            labels = VGroup(start_label, duration_label, pitch_label)
            labels.arrange(DOWN, buff=0.05)
            labels.next_to(note, UP, buff=0.12)
            self.add(labels)
            remaining.append((start, labels))

        animations = []
        for (start, labels), row in zip(remaining, rows[1:]):
            animations.extend(
                [
                    Transform(
                        labels[0],
                        Text(str(start), font_size=18).move_to(
                            row[0], aligned_edge=LEFT
                        ),
                    ),
                    Transform(
                        labels[1],
                        Text("0.5", font_size=18).move_to(
                            row[1], aligned_edge=LEFT
                        ),
                    ),
                    Transform(
                        labels[2],
                        Text("F#4", font_size=18).move_to(
                            row[2], aligned_edge=LEFT
                        ),
                    ),
                ]
            )

        self.play(*animations, run_time=1.5)
        self.wait()

    def pattern_morph_slide(self):
        x_left = PIANO_ROLL_X_LEFT
        x_right = PIANO_ROLL_X_RIGHT
        y_bottom = PIANO_ROLL_Y_BOTTOM
        y_top = PIANO_ROLL_Y_TOP
        n_beats = PIANO_ROLL_BEATS

        base, keyboard, grid, labels, notes, *_ = build_piano_roll(
            x_left, x_right, y_bottom, y_top, n_beats=n_beats
        )
        start_notes = VGroup(*notes)
        details = VGroup(keyboard, grid, labels)
        roll_center_x = (x_left + x_right) / 2
        roll_center_y = (y_bottom + y_top) / 2

        timeline_x_left = -6.8
        timeline_x_right = 6.8
        timeline_bars = 16
        timeline_bar_w = (timeline_x_right - timeline_x_left) / timeline_bars
        clip_width = timeline_bar_w * 0.9
        clip_height = 0.98
        clip_center_x = timeline_x_left + timeline_bar_w / 2
        clip_center_y = 0.0
        clip_left = clip_center_x - clip_width / 2
        clip_note_width = clip_width / 8

        clip_bg = Rectangle(
            width=clip_width,
            height=clip_height,
            fill_color=BLUE_E,
            fill_opacity=1,
            stroke_color=BLUE_B,
            stroke_width=2,
        ).move_to([clip_center_x, clip_center_y, 0])

        target_notes = VGroup()
        for beat in range(n_beats):
            note = Rectangle(
                width=clip_note_width,
                height=clip_height * 0.35,
                fill_color=BLUE_B,
                fill_opacity=1,
                stroke_width=0,
            )
            note.move_to(
                [
                    clip_left + beat * clip_width / 4 + clip_note_width / 2,
                    clip_center_y,
                    0,
                ]
            )
            target_notes.add(note)

        details_target = details.copy()
        sx = clip_width / (x_right - x_left)
        sy = clip_height / (y_top - y_bottom)
        roll_center = [roll_center_x, roll_center_y, 0]
        details_target.stretch(sx, 0, about_point=roll_center)
        details_target.stretch(sy, 1, about_point=roll_center)
        details_target.shift(
            [clip_center_x - roll_center_x, clip_center_y - roll_center_y, 0]
        )
        details_target.set_opacity(0)

        timeline_y = 0.0
        timeline_h = 6.4
        timeline_top = timeline_y + timeline_h / 2

        timeline = VGroup()
        timeline.add(
            Rectangle(
                width=timeline_x_right - timeline_x_left,
                height=timeline_h,
                fill_opacity=0,
                stroke_color=GREY_B,
                stroke_width=2,
            ).move_to([0, timeline_y, 0])
        )
        for bar in range(timeline_bars + 1):
            x = timeline_x_left + bar * timeline_bar_w
            timeline.add(
                Line(
                    [x, timeline_top, 0],
                    [x, timeline_top + 0.16, 0],
                    color=GREY_B,
                    stroke_width=2,
                )
            )
        for bar in range(timeline_bars):
            label = Text(str(bar), font_size=16, color=GREY_B)
            label.move_to(
                [
                    timeline_x_left + bar * timeline_bar_w,
                    timeline_top + 0.32,
                    0,
                ],
                aligned_edge=LEFT,
            )
            timeline.add(label)

        self.add(base, details, start_notes)

        self.play(
            Transform(base, clip_bg),
            Transform(details, details_target),
            Transform(start_notes, target_notes),
            run_time=2.0,
        )
        self.remove(details)
        self.play(FadeIn(timeline), run_time=1.0)
        self.wait()

    def tiling_slide(self):
        x_left = -6.8
        x_right = 6.8
        n_bars = 16
        width = x_right - x_left
        bar_w = width / n_bars
        track_y = 0.0
        track_h = 6.4
        pattern_h = 0.98
        track_top = track_y + track_h / 2

        timeline = VGroup()
        timeline.add(
            Rectangle(
                width=width,
                height=track_h,
                fill_opacity=0,
                stroke_color=GREY_B,
                stroke_width=2,
            ).move_to([0, track_y, 0])
        )
        for bar in range(n_bars + 1):
            x = x_left + bar * bar_w
            timeline.add(
                Line(
                    [x, track_top, 0],
                    [x, track_top + 0.16, 0],
                    color=GREY_B,
                    stroke_width=2,
                )
            )
        for bar in range(n_bars):
            label = Text(str(bar), font_size=16, color=GREY_B)
            label.move_to(
                [x_left + bar * bar_w, track_top + 0.32, 0],
                aligned_edge=LEFT,
            )
            timeline.add(label)

        def make_pattern(center_x):
            block_w = bar_w * 0.9
            block_h = pattern_h
            block = VGroup()
            block.add(
                Rectangle(
                    width=block_w,
                    height=block_h,
                    fill_color=BLUE_E,
                    fill_opacity=1,
                    stroke_color=BLUE_B,
                    stroke_width=2,
                )
            )
            note_w = block_w / 8
            note_h = block_h * 0.35
            for beat in range(4):
                note = Rectangle(
                    width=note_w,
                    height=note_h,
                    fill_color=BLUE_B,
                    fill_opacity=1,
                    stroke_width=0,
                )
                note.move_to(
                    [
                        -block_w / 2 + beat * block_w / 4 + block_w / 16,
                        0,
                        0,
                    ]
                )
                block.add(note)
            block.move_to([center_x, track_y, 0])
            return block

        pattern = make_pattern(x_left + bar_w / 2)

        self.add(timeline, pattern)
        self.next_slide()

        copies = [
            make_pattern(x_left + (bar + 0.5) * bar_w)
            for bar in range(1, n_bars)
        ]
        self.play(
            LaggedStart(
                *[FadeIn(copy) for copy in copies],
                lag_ratio=0.06,
            ),
            run_time=2.5,
        )
        self.wait()
        self.next_slide()

        last_pattern = copies[-1]
        cx = last_pattern.get_center()[0]
        cy = last_pattern.get_center()[1]
        half_w = bar_w / 2 - 0.02
        half_h = pattern_h / 2 + 0.08
        red_x = VGroup(
            Line(
                [cx - half_w, cy - half_h, 0],
                [cx + half_w, cy + half_h, 0],
                color=RED,
                stroke_width=8,
            ),
            Line(
                [cx - half_w, cy + half_h, 0],
                [cx + half_w, cy - half_h, 0],
                color=RED,
                stroke_width=8,
            ),
        )
        self.play(Create(red_x[0]), Create(red_x[1]), run_time=0.6)
        self.wait(0.4)
        self.play(
            last_pattern.animate.shift(DOWN * 8),
            red_x.animate.shift(DOWN * 8),
            run_time=1.5,
        )
        self.wait()
