from manim import *
from manim_slides import Slide

from lib import ACCENT, MUTED, bullet_rows, slide_title


class CompletedSong(Slide):
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
