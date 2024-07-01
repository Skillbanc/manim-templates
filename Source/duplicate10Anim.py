from AbstractAnim import AbstractAnim
from manim import *

class duplicate10(AbstractAnim):
     def construct(self):
        polygon = Text("Polygon",font_size=40).to_edge(UP*1)
        sub_title1 = Text("A polygon is a two-dimensional figure consisting of a finite number of straight",font_size=29).to_edge(UP*3.0)
        sub_title2 = Text("line segments connected end-to-end to form a closed loop or circuit"'.',font_size=29).to_edge(UP*4.5)

        self.play(Write(polygon))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))

        example = Text("Example of Polygon with 5 Line Segments"':',font_size=30).to_edge(UP*7.5).shift(LEFT * 2.5 )

        self.play(Write(example))

        # Create a regular pentagon
        pentagon = RegularPolygon(n=5, color=BLUE, fill_opacity=0.5).to_edge(UP*10)
        pentagon.set_fill(BLUE, opacity=0.5)
        pentagon.set_stroke(BLUE, width=2)

        # Add the pentagon to the scene
        self.play(Create(pentagon))
        self.wait(0)

        

if __name__ == "__main__":
    from manim import *
    scene = duplicate10()
    scene.render()