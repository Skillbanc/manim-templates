from AbstractAnim import AbstractAnim
from manim import *

class duplicate5(AbstractAnim):
    def construct(self):

        point = Text("Point").to_edge(UP*1)
        sub_title1 = Text("A point is a precise location in space with no size, length, width, or height,",font_size=29).to_edge(UP*3.0)
        sub_title2 = Text("usually represented by a dot and labeled with a letter"'.',font_size=29).to_edge(UP*4.5)

        self.play(Write(point))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))

        # Create a point
        point = Dot(point=ORIGIN, color=BLUE).shift(RIGHT * -1).to_edge(UP*6.5)
        point_label = Text("Point",font_size=30).next_to(point, RIGHT)

        # Display the point
        self.play(Write(point), Write(point_label))
        self.wait(2)

        properties = Text("Properties "':',font_size=35).shift(LEFT * 5.5 ).to_edge(UP*8)
        sub_title1 = Text('1. '"A point determines a location"'.',font_size=29).to_edge(UP*9.5).shift(LEFT * 3.8 )
        sub_title2 = Text('2. '"A point has no length, width, or height"'.',font_size=29).to_edge(UP*11).shift(LEFT * 3.0 )
        sub_title3 = Text('3. '"Points are usually denoted by a single capital letter"'.',font_size=29).to_edge(UP*12.5).shift(LEFT * 1.9)

        self.play(Write(properties))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)
        self.play(Write(sub_title3))


if __name__ == "__main__":
    from manim import *
    scene = duplicate5()
    scene.render()