from AbstractAnim import AbstractAnim
from manim import *

class duplicate6(AbstractAnim):
    def construct(self):
        linesegment = Text("Line Segment").to_edge(UP*1)
        sub_title1 = Text("A line segment is a part of a line that has two endpoints and a definite length"'.',font_size=29).to_edge(UP*3.0)
        

        self.play(Write(linesegment))
        self.play(Write(sub_title1))

        A = Dot(point=LEFT, color=YELLOW).to_edge(UP*5.5)
        B = Dot(point=RIGHT, color=YELLOW).to_edge(UP*5.5)
        line_segment = Line(start=A.get_center(), end=B.get_center(), color=RED)
        A_label = Text("A",font_size=30).next_to(A, DOWN).to_edge(UP*5.5).shift(LEFT * 0.3)
        B_label = Text("B",font_size=30).next_to(B, DOWN).to_edge(UP*5.5).shift(RIGHT * 0.3 )

        # Display the line with arrows
        self.play(Write(A), Write(B), Write(line_segment),Write(A_label),Write(B_label))
        self.wait(2)
    

        properties = Text("Properties"':',font_size=35).shift(LEFT * 5.5 ).to_edge(UP*7.5)
        sub_title1 = Text('1. '"A line segment has a fixed length"'.',font_size=29).to_edge(UP*9).shift(LEFT * 3.5 )
        sub_title2 = Text('2. '"A line segment is straight with no curves"'.',font_size=29).to_edge(UP*10.5).shift(LEFT * 2.9 )
        sub_title3 = Text('3. '"A line segment has two distinct endpoints"'.',font_size=29).to_edge(UP*12).shift(LEFT * 2.75)
        

        self.play(Write(properties))
        self.play(Write(sub_title1))
        self.wait(0)
        self.play(Write(sub_title2))
        self.wait(0)
        self.play(Write(sub_title3))

        

if __name__ == "__main__":
    from manim import *
    scene = duplicate6()
    scene.render()