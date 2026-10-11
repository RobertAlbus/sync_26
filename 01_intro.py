from manim import *
from manim_slides import Slide


class Intro(Slide):
    def construct(self):
        self.add(Text("Intro", font_size=44))
        self.wait()
        self.next_slide()
