from manim import *
from manim_slides import Slide

from lib import slide_title


class LiveNoisePerformanceSystem(Slide):
    def construct(self):
        self.add(
            slide_title(
                "Live Noise Performance System",
                center=True,
            )
        )
        self.wait()
        self.next_slide()
