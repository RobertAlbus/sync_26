import numpy as np
from manim import *
from manim_slides import Slide


class DigitalAudio(Slide):
    def construct(self):
        self.skip_reversing = True
        self.wait_time_between_slides = 0.1

        freq = 1.0
        t_end = 2.0
        n_samples = 16
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

        self.add(title)
        self.play(Create(axes))
        self.play(Create(wave), run_time=2)
        y_labels = [
            n for n in axes.y_axis.numbers if abs(abs(n.get_value()) - 1.0) < 1e-6
        ]
        self.next_slide()

        for _ in range(5):
            self.play(*[n.animate.scale(1.5) for n in y_labels], run_time=0.5)
            self.play(*[n.animate.scale(1 / 1.5) for n in y_labels], run_time=0.5)
        self.next_slide()

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
                    stroke_width=1,
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
        self.next_slide()

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

        array_label = Text("sample array (32 bit floating point)", font_size=22).next_to(
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

        self.play(
            *[dot.animate.set_color(RED) for dot in dots],
            FadeIn(travelling_group, scale=0.5),
            run_time=0.5,
        )
        self.next_slide()

        self.play(LaggedStart(*[Create(c) for c in cells], lag_ratio=0.06), run_time=1.2)
        self.add(array_label)

        self.play(Transform(travelling_group, landed_group), run_time=1.0)
