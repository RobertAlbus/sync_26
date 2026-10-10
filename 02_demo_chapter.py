from manim import *
from manim_slides import Slide


class Chapter2(Slide):
    def construct(self):
        self.skip_reversing = True
        self.wait_time_between_slides = 0.1

        heading = Text("Chapter 2: Quantization", font_size=44)
        self.play(FadeIn(heading))
        self.next_slide(notes="Chapter opener. Introduce quantization.")

        self.play(heading.animate.scale(0.6).to_corner(UL))
        self.next_slide(notes="Keep the heading in the corner for the chapter.")

        body = Rectangle(width=6, height=2, color=BLUE)
        caption = Text("placeholder content", font_size=28).move_to(body)
        self.play(Create(body), FadeIn(caption))
        self.next_slide(
            direction="vertical",
            notes="Vertical child slide grouped under this chapter.",
        )

        self.play(caption.animate.set_color(YELLOW))
        self.next_slide(notes="Next topic in this chapter.")

        self.play(FadeOut(heading), FadeOut(body), FadeOut(caption))
