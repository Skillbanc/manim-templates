from AbstractAnim import AbstractAnim
from manim import *

class duplicate8(AbstractAnim):
    def construct(self):
        Ray = Text("Ray").to_edge(UP*1)
        sub_title1 = Text("A ray is a part of a line that starts at one point and extends infinitely",font_size=29).to_edge(UP*3.0)
        sub_title2 = Text("in one direction"'.',font_size=29).to_edge(UP*4.5)

        self.play(Write(Ray))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))

        properties = Text("Properties"':',font_size=30).to_edge(UP*8.0).shift(LEFT * 5.7 )
        sub_title1 = Text('1. '"A ray is straight with no curves"'.',font_size=29).to_edge(UP*9.5).shift(LEFT * 3.8 )
        sub_title2 = Text('2. '"A ray has one fixed endpoint where it begins"'.',font_size=29).to_edge(UP*11).shift(LEFT * 2.5)
        sub_title3 = Text('3. '"A ray extends infinitely in one direction from its starting point"'.',font_size=29).to_edge(UP*12.5).shift(LEFT * 1)

        self.play(Write(properties))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)
        self.play(Write(sub_title3))

       # Create a ray starting from a point
        ray_start = Dot(point=ORIGIN, color=PURPLE)
        ray = Line(start=ray_start.get_center(), end=RIGHT*5.5, color=PURPLE)
        ray_arrow = Arrow(start=RIGHT*4.5, end=RIGHT*5.5, color=PURPLE, buff=0)
        ray_label = Text("Ray",font_size=30).next_to(ray, UP)

        self.play(Write(ray_start), Write(ray), Write(ray_arrow), Write(ray_label))

        # Display the ray with an arrow
        self.play(Write(ray_start), Write(ray), Write(ray_arrow), Write(ray_label))
        self.wait(0)


if __name__ == "__main__":
    from manim import *
    scene = duplicate8()
    scene.render()