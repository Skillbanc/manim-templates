from AbstractAnim import AbstractAnim
from manim import *
import numpy as np


class duplicate9(AbstractAnim):
    def construct(self):
        quadrilateral = Text("Quadrilateral",font_size=40).to_edge(UP*1)
        sub_title1 = Text("Quadrilateral is a simple closed polygon with four line segments"'.',font_size=29).to_edge(UP*3.5)
        sub_title2 = Text("Example: A Quadrilateral formed by four line segments AB, BC, CD, DA"'.',font_size=29).to_edge(UP*6 + LEFT * 1)
        sub_title3 = Text("∠A, ∠B, ∠C and ∠D are its four angles"'.',font_size=29).to_edge(UP*8 + LEFT * 1)
        sub_title4 = Text("line segments joining opposite vertices A, C and B, D"'.',font_size=29).to_edge(UP*10 + LEFT * 1)
        sub_title5 = Text("namely AC and BD , are called its two diagonals"'.',font_size=29).to_edge(UP*12 + LEFT * 1)

        self.play(Write(quadrilateral))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)
        self.play(Write(sub_title3))
        self.wait(1)
        self.play(Write(sub_title4))
        self.wait(1)
        self.play(Write(sub_title5))

        # Define points A, B, C, D
        A = np.array([2, -3, 0])
        B = np.array([6, -3, 0])
        C = np.array([5, 0, 0])
        D = np.array([3,-1, 0])

        # Create quadrilateral ABCD
        quadrilateral = Polygon(A, B, C, D, color=BLUE)
        label_A = MathTex("A").next_to(A, DOWN)
        label_B = MathTex("B").next_to(B, DOWN)
        label_C = MathTex("C").next_to(C, UP)
        label_D = MathTex("D").next_to(D, UP)

        # Calculate midpoints for diagonals
        diagonal_AC = Line(A, C, color=DARK_BROWN)
        diagonal_BD = Line(B, D, color=GREEN)

        # Create labels for diagonals
        label_AC = MathTex("AC").move_to((A + C) / 2).shift(UP * 0.5)
        label_BD = MathTex("BD").move_to((B + D) / 2).shift(DOWN * 0.5)

        self.play(Create(quadrilateral),
        Write(label_A), Write(label_B), Write(label_C), Write(label_D))
        self.play(Create(diagonal_AC), Write(label_AC))
        self.play(Create(diagonal_BD), Write(label_BD))
        self.wait(2)


        

if __name__ == "__main__":
    from manim import *
    scene = duplicate9()
    scene.render()
