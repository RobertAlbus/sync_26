from manim import *
from manim_slides import Slide

from lib import ACCENT, MUTED, bullet_rows, slide_title


class Intro(Slide):
    def construct(self):
        self.title_slide()
        self.wait()
        self.next_slide()

        self.clear()
        self.bio_slide()
        self.wait()
        self.next_slide()

        self.clear()
        self.premise_slide()
        self.wait()
        self.next_slide()

        self.clear()
        self.overview_slide()
        self.wait()

    def bio_slide(self):
        name = Text("Rob Albus", font_size=72, weight=BOLD)

        role = Text("Music producer and computer programmer", font_size=30)
        role.next_to(name, DOWN, buff=0.35)

        practice = Text("I make music using C++ code", font_size=30, color=ACCENT)
        practice.next_to(role, DOWN, buff=0.3)

        rule = Line(LEFT, RIGHT, color=MUTED, stroke_width=3).set_width(3.5)
        rule.next_to(practice, DOWN, buff=0.55)

        aliases = Paragraph(
            "DFK",
            "A City Of Bridges",
            "Ten Speed Audio",
            font_size=32,
            color=MUTED,
            alignment="center",
            line_spacing=0.8,
        )
        aliases.next_to(rule, DOWN, buff=0.55)

        self.add(VGroup(name, role, practice, rule, aliases).move_to(ORIGIN))

    def title_slide(self):
        title = slide_title("Writing Electronic Music\n Literally from Scratch")

        subtitle = Text(
            "Using the C++ programming language to build an audio engine,\n"
            "instruments, and the compositional method from first principles.",
            font_size=24,
            color=MUTED,
            line_spacing=1.0,
        )
        subtitle.next_to(title, DOWN, buff=0.7)

        rule = Line(LEFT, RIGHT, color=ACCENT, stroke_width=4).set_width(6)
        rule.next_to(subtitle, DOWN, buff=0.6)

        author = Text("Rob Albus", font_size=30)
        author.next_to(rule, DOWN, buff=0.5)

        self.add(title, subtitle, rule, author)

    def premise_slide(self):
        title = slide_title("An unconventional approach\nto music production")

        rows = bullet_rows(
            [
                "Each song is a computer program",
                "Code is the compositional medium",
                "Custom audio engine, instruments, workflows",
            ]
        )
        rows.next_to(title, DOWN, buff=0.8)
        rows.move_to([0, rows.get_center()[1], 0])

        self.add(title, rows)

    def overview_slide(self):
        title = slide_title("Presentation Overview")

        rows = bullet_rows(
            [
                "Demo a completed song",
                "Technical deep dive: what is an audio engine?",
                "Write a song",
            ]
        )
        rows.next_to(title, DOWN, buff=0.8)
        rows.move_to([0, rows.get_center()[1], 0])

        self.add(title, rows)
