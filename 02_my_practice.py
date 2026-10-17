from manim import *
from manim_slides import Slide


class MyPractice(Slide):
    def construct(self):
        self.add(Text("My Practice", font_size=44))
        self.wait()
        self.next_slide()
