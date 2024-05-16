from manim import *

class ReplacementTransformExample(Scene):
    def construct(self):

        square2 = Square(color=RED, fill_opacity=0.5)
        circle2 = Circle(color=BLUE, fill_opacity=0.5)

        #Replace circle with square
        self.play(Create(square2))
        self.play(ReplacementTransform(square2, circle2))
        self.wait(1)
        self.play(FadeOut(circle2))
        self.wait(1)
if __name__=="__main__":
    vt=ReplacementTransformExample()
    vt.render()