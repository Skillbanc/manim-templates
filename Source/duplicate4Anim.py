from AbstractAnim import AbstractAnim
from manim import *

class duplicate4(AbstractAnim):
    def construct(self):


        # Create a point
        point = Dot(point=ORIGIN, color=BLUE).shift(LEFT * 4 )
        point_label = Text("Point",font_size=30).next_to(point, RIGHT)

        # Display the point
        self.play(Write(point), Write(point_label))
        self.wait(2)
        self.play(FadeOut(point), FadeOut(point_label))

        point = Text("Point").to_edge(UP*1)
        sub_title1 = Text("A point is a precise location in space with no size, length, width, or height,",font_size=29).to_edge(UP*3.5)
        sub_title2 = Text("usually represented by a dot and labeled with a letter'.",font_size=29).to_edge(UP*5.5)

        self.play(Write(point))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))

        # Create a line with arrows
        infinite_line = Line(start=LEFT*5, end=RIGHT*5, color=GREEN)
        left_arrow = Arrow(start=LEFT*4.5, end=LEFT*5, color=GREEN, buff=0)
        right_arrow = Arrow(start=RIGHT*4.5, end=RIGHT*5, color=GREEN, buff=0)
        line_label = Text("Line").next_to(infinite_line, UP)

        
        # Display the line with arrows
        self.play(Write(infinite_line), Write(left_arrow), Write(right_arrow), Write(line_label))
        self.wait(2)
        self.play(FadeOut(infinite_line), FadeOut(left_arrow), FadeOut(right_arrow), FadeOut(line_label))


        # Create a line segment with points A and B
        A = Dot(point=LEFT, color=YELLOW)
        B = Dot(point=RIGHT, color=YELLOW)
        line_segment = Line(start=A.get_center(), end=B.get_center(), color=RED)
        line_segment_label = Text("Line Segment").next_to(line_segment, UP)
        A_label = Text("A").next_to(A, DOWN)
        B_label = Text("B").next_to(B, DOWN)


        # Create a ray starting from a point
        ray_start = Dot(point=ORIGIN, color=PURPLE)
        ray = Line(start=ray_start.get_center(), end=RIGHT*5, color=PURPLE)
        ray_arrow = Arrow(start=RIGHT*4.5, end=RIGHT*5, color=PURPLE, buff=0)
        ray_label = Text("Ray").next_to(ray, UP)


        # Display the line segment with points A and B
        self.play(Write(A), Write(B), Write(A_label), Write(B_label))
        self.play(Write(line_segment), Write(line_segment_label))
        self.wait(2)
        self.play(FadeOut(A), FadeOut(B), FadeOut(A_label), FadeOut(B_label), FadeOut(line_segment), FadeOut(line_segment_label))

        # Display the line with arrows
        self.play(Write(infinite_line), Write(left_arrow), Write(right_arrow), Write(line_label))
        self.wait(2)
        self.play(FadeOut(infinite_line), FadeOut(left_arrow), FadeOut(right_arrow), FadeOut(line_label))

        # Display the ray with an arrow
        self.play(Write(ray_start), Write(ray), Write(ray_arrow), Write(ray_label))
        self.wait(2)
        self.play(FadeOut(ray_start), FadeOut(ray), FadeOut(ray_arrow), FadeOut(ray_label))


if __name__ == "__main__":
    from manim import *
    scene = duplicate4()
    scene.render()