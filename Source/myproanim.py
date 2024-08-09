from venv import create
from manim import *

class createcircle():
    def construct(self):
        circle=circle()
        circle.set_fill(PINK, optacity=0.5)
        self.play(create(circle))