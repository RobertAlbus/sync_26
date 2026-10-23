import numpy as np
from manim import *
from manim_slides import Slide


def make_speaker(scale=1.0):
    square = Rectangle(
        width=0.8,
        height=0.8,
        stroke_color=WHITE,
        stroke_width=4,
        fill_color=WHITE,
        fill_opacity=0.1,
    )
    cone = Polygon(
        [0.4, 0.25, 0],
        [0.4, -0.25, 0],
        [1.2, -0.75, 0],
        [1.2, 0.75, 0],
        stroke_color=WHITE,
        stroke_width=4,
        fill_color=WHITE,
        fill_opacity=0.1,
    )
    return VGroup(square, cone).scale(scale)


class EngineDeepDive(Slide):
    def construct(self):
        self.add(Text("Engine Technical Deep Dive", font_size=44))
        self.wait()
        self.next_slide()


class DigitalAudio(Slide):
    def construct(self):
        self.skip_reversing = True
        self.wait_time_between_slides = 0.1

        t_end = 2.0
        n_samples = 16
        wave_period_samples = 7.5
        freq = n_samples / (wave_period_samples * t_end)
        amplitude = 1.0

        title = Text("Digital Audio: From a Continuous Wave to Samples", font_size=30)
        title.to_edge(UP, buff=0.25)

        axes = Axes(
            x_range=[0, t_end, 0.5],
            y_range=[-1.25, 1.25, 0.5],
            x_length=11,
            y_length=3.0,
            tips=False,
            axis_config={"include_numbers": True, "font_size": 22},
            x_axis_config={"include_numbers": False},
            y_axis_config={
                "numbers_to_include": [-1, 0, 1],
                "decimal_number_config": {"num_decimal_places": 0},
            },
        )
        axes.move_to([0, 1.4, 0])

        wave = axes.plot(
            lambda t: amplitude * np.sin(2 * np.pi * freq * t),
            x_range=[0, t_end],
            color=BLUE,
        )

        self.add(title, axes)
        self.play(Create(wave), run_time=2)
        y_labels = [
            n for n in axes.y_axis.numbers if abs(abs(n.get_value()) - 1.0) < 1e-6
        ]
        self.next_slide()

        box_width = max(label.width for label in y_labels) + 0.2
        box_height = max(label.height for label in y_labels) + 0.2
        y_boxes = VGroup(
            *[
                Rectangle(
                    width=box_width,
                    height=box_height,
                    color=YELLOW,
                    stroke_width=4,
                ).move_to(label.get_center())
                for label in y_labels
            ]
        )
        self.play(*[Create(box) for box in y_boxes])
        self.next_slide()

        self.play(FadeOut(y_boxes), run_time=0.5)

        ts = np.linspace(0.0, t_end, n_samples)
        values = amplitude * np.sin(2 * np.pi * freq * ts)
        pts = [axes.c2p(t, v) for t, v in zip(ts, values)]
        center_y = axes.c2p(0, 0)[1]

        grid = VGroup(
            *[
                DashedLine(
                    start=[axes.c2p(t, 0)[0], axes.c2p(0, -1.25)[1], 0],
                    end=[axes.c2p(t, 0)[0], axes.c2p(0, 1.25)[1], 0],
                    color=BLUE_E,
                    stroke_width=2,
                    dash_length=0.06,
                )
                for t in ts
            ]
        )
        self.play(LaggedStart(*[Create(g) for g in grid], lag_ratio=0.05), run_time=1.2)

        sample_labels = VGroup(
            *[
                Text(str(i), font_size=18, color=GREY_B).next_to(
                    axes.c2p(t, -1.25), DOWN, buff=0.15
                )
                for i, t in enumerate(ts)
            ]
        )
        self.play(FadeIn(sample_labels))

        stems = VGroup(
            *[
                Line(
                    start=[p[0], center_y, 0],
                    end=p,
                    color=YELLOW,
                    stroke_width=3,
                )
                for p in pts
            ]
        )
        dots = VGroup(*[Dot(p, color=YELLOW, radius=0.075) for p in pts])
        self.play(
            LaggedStart(
                *[GrowFromPoint(stem, [stem.get_start()[0], center_y, 0]) for stem in stems],
                lag_ratio=0.08,
            ),
            run_time=1.5,
        )
        self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in dots], lag_ratio=0.08), run_time=1.0)
        self.play(FadeOut(wave), FadeOut(stems), run_time=1.0)
        self.next_slide()

        x_left = axes.c2p(0, 0)[0]
        x_right = axes.c2p(t_end, 0)[0]
        cell_w = (x_right - x_left) / n_samples
        cell_h = 0.72
        array_y = -1.5

        cells = VGroup()
        for t in ts:
            cell = Rectangle(
                width=cell_w,
                height=cell_h,
                stroke_color=GREY_B,
                stroke_width=2,
            )
            cell.move_to([axes.c2p(t, 0)[0], array_y, 0])
            cells.add(cell)

        array_label = Text("audio buffer", font_size=22).next_to(
            cells, DOWN, buff=0.35
        )

        travelling_group = VGroup()
        landed_group = VGroup()
        for i, (dot, cell) in enumerate(zip(dots, cells)):
            travelling = DecimalNumber(
                values[i], num_decimal_places=2, font_size=20, color=YELLOW
            )
            travelling.next_to(dot, RIGHT, buff=0.08)
            landed = DecimalNumber(
                values[i], num_decimal_places=2, font_size=20, color=YELLOW
            )
            landed.move_to(cell)
            if landed.width > cell_w - 0.12:
                landed.scale((cell_w - 0.12) / landed.width)
            travelling_group.add(travelling)
            landed_group.add(landed)

        self.play(FadeIn(travelling_group, scale=0.5), run_time=0.5)
        self.next_slide()

        self.play(LaggedStart(*[Create(c) for c in cells], lag_ratio=0.06), run_time=1.2)
        self.add(array_label)

        self.play(Transform(travelling_group, landed_group), run_time=1.0)
        self.next_slide()

        speaker = make_speaker()
        speaker.move_to([4.8, -3.2, 0])
        self.play(FadeIn(speaker, shift=UP * 0.2), run_time=0.5)

        target = speaker[0].get_center()
        self.play(
            FadeOut(dots),
            LaggedStart(
                *[number.animate.move_to(target) for number in travelling_group],
                lag_ratio=0.08,
            ),
            run_time=2.2,
        )
        self.play(FadeOut(travelling_group, scale=0.3), run_time=0.4)

        cone_tip = speaker[1].get_right() + RIGHT * 0.1
        for _ in range(2):
            waves = VGroup(
                *[
                    Arc(
                        radius=radius,
                        start_angle=-60 * DEGREES,
                        angle=120 * DEGREES,
                        color=YELLOW,
                        stroke_width=5,
                    ).shift(cone_tip)
                    for radius in (0.25, 0.45, 0.65)
                ]
            )
            self.play(
                LaggedStart(*[Create(wave) for wave in waves], lag_ratio=0.25),
                run_time=0.8,
            )
            self.play(FadeOut(waves), run_time=0.2)

        self.next_slide()

        speaker_target = speaker[0].get_center()

        max_segments = 12
        phase_offsets = []
        phase = 2 * np.pi * freq * t_end
        for segment in range(max_segments):
            phase_offsets.append(phase)
            period_samples = wave_period_samples + 0.5 * segment
            segment_freq = n_samples / (period_samples * t_end)
            phase += 2 * np.pi * segment_freq * t_end

        def segment_values(segment):
            period_samples = wave_period_samples + 0.5 * segment
            segment_freq = n_samples / (period_samples * t_end)
            return amplitude * np.sin(
                2 * np.pi * segment_freq * ts + phase_offsets[segment]
            )

        def make_graph_dots(segment):
            return VGroup(
                *[
                    Dot(axes.c2p(t, value), color=YELLOW, radius=0.075)
                    for t, value in zip(ts, segment_values(segment))
                ]
            )

        def make_buffer_numbers(segment):
            numbers = VGroup(
                *[
                    DecimalNumber(
                        value,
                        num_decimal_places=2,
                        font_size=20,
                        color=YELLOW,
                    ).move_to(cell)
                    for value, cell in zip(segment_values(segment), cells)
                ]
            )
            for number in numbers:
                if number.width > cell_w - 0.12:
                    number.scale((cell_w - 0.12) / number.width)
            return numbers

        graph_dots = make_graph_dots(0)
        self.play(
            LaggedStart(
                *[FadeIn(dot, scale=0.4) for dot in graph_dots],
                lag_ratio=0.03,
            ),
            run_time=0.6,
        )

        next_dots = make_graph_dots(1)
        current_numbers = make_buffer_numbers(0)
        self.play(
            AnimationGroup(
                LaggedStart(
                    *[
                        Transform(dot, number)
                        for dot, number in zip(graph_dots, current_numbers)
                    ],
                    lag_ratio=0.02,
                    run_time=1.0,
                ),
                Succession(
                    Wait(0.2),
                    LaggedStart(
                        *[FadeIn(dot, scale=0.4) for dot in next_dots],
                        lag_ratio=0.02,
                        run_time=0.8,
                    ),
                ),
            )
        )
        buffer_items = graph_dots
        graph_dots = next_dots

        speaker_batch = None
        for cycle in range(10):
            next_dots = make_graph_dots(cycle + 2)
            current_numbers = make_buffer_numbers(cycle + 1)
            graph_to_buffer = LaggedStart(
                *[
                    Transform(dot, number)
                    for dot, number in zip(graph_dots, current_numbers)
                ],
                lag_ratio=0.02,
                run_time=1.0,
            )
            buffer_to_speaker = LaggedStart(
                *[
                    number.animate.move_to(speaker_target)
                    for number in buffer_items
                ],
                lag_ratio=0.02,
                run_time=0.8,
            )
            graph_redraw = LaggedStart(
                *[FadeIn(dot, scale=0.4) for dot in next_dots],
                lag_ratio=0.02,
                run_time=0.8,
            )
            animations = [
                graph_to_buffer,
                Succession(
                    Wait(0.2),
                    AnimationGroup(buffer_to_speaker, graph_redraw),
                ),
            ]
            if speaker_batch is not None:
                animations.append(FadeOut(speaker_batch, run_time=0.2))
            self.play(AnimationGroup(*animations))
            if speaker_batch is not None:
                self.remove(speaker_batch)
            speaker_batch = buffer_items
            buffer_items = graph_dots
            graph_dots = next_dots

        if speaker_batch is not None:
            self.play(FadeOut(speaker_batch), run_time=0.2)
            self.remove(speaker_batch)

        self.play(
            LaggedStart(
                *[
                    number.animate.move_to(speaker_target)
                    for number in buffer_items
                ],
                lag_ratio=0.02,
                run_time=0.8,
            )
        )
        self.play(
            FadeOut(buffer_items),
            FadeOut(graph_dots),
            run_time=0.3,
        )
        self.remove(dots, travelling_group, buffer_items, graph_dots, next_dots)
        self.wait(0.3)
