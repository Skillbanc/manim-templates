from manim import *

class TransformExample(Scene):
    def construct(self):
        # Create objects
        square1 = Square(color=BLUE, fill_opacity=0.5)
        circle1 = Circle(color=RED, fill_opacity=0.5)


        # Add objects to scene
        self.play(Create(circle1))
        # Transform square into circle
        self.play(Transform(circle1, square1))
        self.wait(1)
        self.play(FadeOut(circle1))
        self.wait(1)