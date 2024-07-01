from AbstractAnim import AbstractAnim
from manim import *

class duplicate7(AbstractAnim):
    def construct(self):
        line = Text("Line").to_edge(UP*1)
        sub_title1 = Text("A line is a straight path that extends infinitely in both directions with",font_size=29).to_edge(UP*3.0)
        sub_title2 = Text("no thickness and is usually defined by two points"'.',font_size=29).to_edge(UP*4.5)

        self.play(Write(line))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))

        # Create a line with arrows   
        infinite_line = Line(start=LEFT*1, end=RIGHT*1, color=GREEN).to_edge(UP*7.0)
        left_arrow = Arrow(start=LEFT*0.5, end=LEFT*1, color=GREEN, buff=0).to_edge(UP*6.859)
        right_arrow = Arrow(start=RIGHT*0.5, end=RIGHT*1, color=GREEN, buff=0).to_edge(UP*6.859)
        line_label = Text("Line",font_size=35).next_to(infinite_line, UP)

        
        # Display the line with arrows
        self.play(Write(infinite_line), Write(left_arrow), Write(right_arrow), Write(line_label))
        self.wait(2)

        properties = Text("Properties"':',font_size=35).shift(LEFT * 5.5 ).to_edge(UP*8.5)
        sub_title1 = Text('1. '"A line has no width or thickness"'.',font_size=29).to_edge(UP*10).shift(LEFT * 3.7 )
        sub_title2 = Text('2. '"A line is perfectly straight with no curves"'.',font_size=29).to_edge(UP*11.5).shift(LEFT * 2.9 )
        sub_title3 = Text('3. '"A line extends infinitely in both directions"'.',font_size=29).to_edge(UP*13).shift(LEFT * 2.75)

        self.play(Write(properties))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)
        self.play(Write(sub_title3))

    
if __name__ == "__main__":
    from manim import *
    scene = duplicate7()
    scene.render()