from manim import *
from manim_slides import Slide

from lib import slide_title


class Conclusion(Slide):
    def construct(self):
        self.add(slide_title("Conclusion", center=True))
        self.wait()
        self.next_slide()
