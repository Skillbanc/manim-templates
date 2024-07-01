from AbstractAnim import AbstractAnim
from manim import *


class duplicate12(AbstractAnim):
    def construct(self):
        triangle = Text("Triangle",font_size=40).to_edge(UP*1)
        sub_title1 = Text("The simple closed figure formed by three line segments is a triangle"'.',font_size=29).to_edge(UP*3.0)
        sub_title2 = Text("The line segments are called sides"'.',font_size=29).to_edge(UP*4.5)
        sub_title3 = Text("Example: The triangle formed by three line segments AB, BC, CA"'.',font_size=29).to_edge(UP*6).shift(LEFT * 1)
        sub_title4 = Text("Here A, B, C are called three vertices of the triangle ABC"'.',font_size=29).to_edge(UP*7.5).shift(LEFT * 1)

        self.play(Write(triangle))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)
        self.play(Write(sub_title3))
        self.wait(1)
        self.play(Write(sub_title4))



        # Create a triangle ABC
        A = np.array([-2, -3, 0])
        B = np.array([2, -3, 0])
        C = np.array([0, -1, 0])

        triangle = Polygon(A, B, C, color=PINK,fill_opacity=0.3)
        label_A = MathTex("A",font_size=30).next_to(A, LEFT)
        label_B = MathTex("B",font_size=30).next_to(B, RIGHT)
        label_C = MathTex("C",font_size=30).next_to(C, UP)

        self.play(Create(triangle), Write(label_A), Write(label_B), Write(label_C))
        self.wait(1)
        

if __name__ == "__main__":
    from manim import *
    scene = duplicate12()
    scene.render()