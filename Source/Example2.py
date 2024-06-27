import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo

class Example2(AbstractAnim):
    def construct(self):
        self.CircleExample3()
    def  CircleExample3(self):
        '''' circle3 = Circle().shift(LEFT * 5)
         sector2_1 = Sector(outer_radius=1, angle=PI / 2, start_angle=0, color=BLUE, fill_opacity=0.5).shift(LEFT * 5)
         line2_1 = Line(circle3.get_center(), circle3.point_at_angle(PI / 2)).shift(LEFT * 5)
         line2_2 = Line(circle3.get_center(), circle3.point_at_angle(PI)).shift(LEFT * 5)
         line2_3 = Line(circle3.get_center(), circle3.point_at_angle(3 * PI / 2)).shift(LEFT * 5)

         self.play(Create(circle3), Create(sector2_1), Create(line2_1), Create(line2_2), Create(line2_3))
         fraction = Tex(r"$\frac{1}{4}$", font_size=96).shift(RIGHT * 5)
         self.play(Write(fraction))

         # Create arrow from circle to fraction
         arrow_to_fraction = Arrow(circle3.get_right(), fraction, color=WHITE)
         self.play(Create(arrow_to_fraction))
        

         self.wait()'''
        circle = Circle(fill_color=PINK, fill_opacity=0.5).shift(LEFT*3)  # create a circle and move it to the left

        # Create vertical and horizontal lines
        vertical_line = Line(ORIGIN, UP * 2, color=BLACK).shift(LEFT*3)
        horizontal_line = Line(ORIGIN, RIGHT * 2, color=BLACK).shift(LEFT*3)

        # Position the lines at the center
        vertical_line.move_to(circle.get_center())
        horizontal_line.move_to(circle.get_center())

        # Create labels for each quarter circle at their midpoints
        label_1 = Text("1", color=BLACK).move_to(UP * 0.5 + LEFT * 0.5 + LEFT*3)
        label_2 = Text("2", color=BLACK).move_to(UP * 0.5 + RIGHT * 0.5 + LEFT*3)
        label_3 = Text("3", color=BLACK).move_to(DOWN * 0.5 + LEFT * 0.5 + LEFT*3)
        label_4 = Text("4", color=BLACK).move_to(DOWN * 0.5 + RIGHT * 0.5 + LEFT*3)

        self.play(Create(circle), Create(vertical_line), Create(horizontal_line))  # show the circle and lines on screen
        self.play(Write(label_1), Write(label_2), Write(label_3), Write(label_4))  # show the labels on screen

        # Shade quarters 1, 2, and 3 in green
        #quarter_1 = Sector(outer_radius=1, start_angle=PI / 2, angle=PI / 2, color=GREEN, fill_opacity=0.5).shift(LEFT*3)
        #quarter_2 = Sector(outer_radius=1, start_angle=0, angle=PI / 2, color=GREEN, fill_opacity=0.5).shift(LEFT*3)
        #quarter_3 = Sector(outer_radius=1, start_angle=PI, angle=PI / 2, color=GREEN, fill_opacity=0.5).shift(LEFT*3)

       # self.play(Create(quarter_1))  # show the shaded quarters

        self.wait() 
        # Indicate the fraction 3/4
        fraction = Tex(r"$\frac{1}{4}$", font_size=96).shift(RIGHT*3)
        self.play(Write(fraction))

        # Create arrow from circle to fraction
        arrow_to_fraction = Arrow(circle.get_right(), fraction, color=WHITE)

        self.play(Create(arrow_to_fraction))
        
if __name__ == "__main__":
    scene = Example2()
    scene.render()
