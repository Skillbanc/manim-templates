import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo
class Examples(AbstractAnim):
 def construct(self):
        self.CircleExample()
    

 def CircleExample(self):
    p10 = cvo.CVO().CreateCVO("Fractions Example", "").setPosition([3, 3, 0])
    circle = Circle(fill_color=PINK, fill_opacity=0.5).shift(UP * 2)  # create a circle and move it to the top

    # Create vertical and horizontal lines
    vertical_line = Line(ORIGIN, UP * 2, color=BLACK).shift(UP * 2)
    horizontal_line = Line(ORIGIN, RIGHT * 2, color=BLACK).shift(UP * 2)

    # Position the lines at the center
    vertical_line.move_to(circle.get_center())
    horizontal_line.move_to(circle.get_center())

    # Create labels for each quarter circle at their midpoints
    label_1 = Text("1", color=BLACK).move_to(UP * 0.5 + LEFT * 0.5 + UP * 2)
    label_2 = Text("2", color=BLACK).move_to(UP * 0.5 + RIGHT * 0.5 + UP * 2)
    label_3 = Text("3", color=BLACK).move_to(DOWN * 0.5 + LEFT * 0.5 + UP * 2)
    label_4 = Text("4", color=BLACK).move_to(DOWN * 0.5 + RIGHT * 0.5 + UP * 2)

    self.play(Create(circle), Create(vertical_line), Create(horizontal_line))  # show the circle and lines on screen
    self.play(Write(label_1), Write(label_2), Write(label_3), Write(label_4))  # show the labels on screen

    # Shade quarters 1, 2, and 3 in green
    quarter_1 = Sector(outer_radius=1, start_angle=PI / 2, angle=PI / 2, color=GREEN, fill_opacity=0.5).shift(UP * 2)
    quarter_2 = Sector(outer_radius=1, start_angle=0, angle=PI / 2, color=GREEN, fill_opacity=0.5).shift(UP * 2)
    quarter_3 = Sector(outer_radius=1, start_angle=PI, angle=PI / 2, color=GREEN, fill_opacity=0.5).shift(UP * 2)

    self.play(Create(quarter_1), Create(quarter_2), Create(quarter_3))  # show the shaded quarters
    p10.cvolist.append(circle)
    self.wait()  # wait for the animation to finish

    # Indicate the fraction 3/4
    fraction = Tex(r"$\frac{3}{4}$", font_size=96).shift(UP * 4)  # Shifted further up
    self.play(Write(fraction))

    # Create arrow from circle to fraction
    arrow_to_fraction = Arrow(circle.get_top() + UP * 0.5, fraction, color=WHITE)  # Adjusted position of the arrow

    self.play(Create(arrow_to_fraction))

    self.wait(2)

    # Move down to make space for the next example
    self.play(ApplyMethod(p10.shift, DOWN * 4))

    # Example 2
    p20 = cvo.CVO().CreateCVO("Fractions Example", "").setPosition([3, 3, 0])
    circle_2 = Circle(fill_color=YELLOW, fill_opacity=0.5).shift(UP * 2)  # create a circle and move it to the top
    vertical_line_2 = Line(ORIGIN, UP * 2, color=BLACK).shift(UP * 2)
    horizontal_line_2 = Line(ORIGIN, RIGHT * 2, color=BLACK).shift(UP * 2)
    vertical_line_2.move_to(circle_2.get_center())
    horizontal_line_2.move_to(circle_2.get_center())
    label_21 = Text("1", color=BLACK).move_to(UP * 0.5 + LEFT * 0.5 + UP * 2)
    label_22 = Text("2", color=BLACK).move_to(UP * 0.5 + RIGHT * 0.5 + UP * 2)
    label_23 = Text("3", color=BLACK).move_to(DOWN * 0.5 + LEFT * 0.5 + UP * 2)
    label_24 = Text("4", color=BLACK).move_to(DOWN * 0.5 + RIGHT * 0.5 + UP * 2)
    quarter_21 = Sector(outer_radius=1, start_angle=PI / 2, angle=PI / 2, color=YELLOW, fill_opacity=0.5).shift(UP * 2)
    quarter_22 = Sector(outer_radius=1, start_angle=0, angle=PI / 2, color=YELLOW, fill_opacity=0.5).shift(UP * 2)
    quarter_23 = Sector(outer_radius=1, start_angle=PI, angle=PI / 2, color=YELLOW, fill_opacity=0.5).shift(UP * 2)
    self.play(Create(circle_2), Create(vertical_line_2), Create(horizontal_line_2))
    self.play(Write(label_21), Write(label_22), Write(label_23), Write(label_24))
    self.play(Create(quarter_21), Create(quarter_22), Create(quarter_23))
    p20.cvolist.append(circle_2)
    self.wait()
    fraction_2 = Tex(r"$\frac{1}{2}$", font_size=96).shift(UP * 4)
    self.play(Write(fraction_2))
    arrow_to_fraction_2 = Arrow(circle_2.get_top() + UP * 0.5, fraction_2, color=WHITE)
    self.play(Create(arrow_to_fraction_2))
    self.wait(2)

    # Move down to make space for the next example
    self.play(ApplyMethod(p20.shift, DOWN * 4))

    # Example 3
    p30 = cvo.CVO().CreateCVO("Fractions Example", "").setPosition([3, 3, 0])
    circle_3 = Circle(fill_color=BLUE, fill_opacity=0.5).shift(UP * 2)  # create a circle and move it to the top
    vertical_line_3 = Line(ORIGIN, UP * 2, color=BLACK).shift(UP * 2)
    horizontal_line_3 = Line(ORIGIN, RIGHT * 2, color=BLACK).shift(UP * 2)
    vertical_line_3.move_to(circle_3.get_center())
    horizontal_line_3.move_to(circle_3.get_center())
    label_31 = Text("1", color=BLACK).move_to(UP * 0.5 + LEFT * 0.5 + UP * 2)
    label_32 = Text("2", color=BLACK).move_to(UP * 0.5 + RIGHT * 0.5 + UP * 2)
    label_33 = Text("3", color=BLACK).move_to(DOWN * 0.5 + LEFT * 0.5 + UP * 2)
    label_34 = Text("4", color=BLACK).move_to(DOWN * 0.5 + RIGHT * 0.5 + UP * 2)
    quarter_31 = Sector(outer_radius=1, start_angle=PI / 2, angle=PI / 2, color=BLUE, fill_opacity=0.5).shift(UP * 2)
    quarter_32 = Sector(outer_radius=1, start_angle=0, angle=PI / 2, color=BLUE, fill_opacity=0.5).shift(UP * 2)
    quarter_33 = Sector(outer_radius=1, start_angle=PI, angle=PI / 2, color=BLUE, fill_opacity=0.5).shift(UP * 2)
    self.play(Create(circle_3), Create(vertical_line_3), Create(horizontal_line_3))
    self.play(Write(label_31), Write(label_32), Write(label_33), Write(label_34))
    self.play(Create(quarter_31), Create(quarter_32), Create(quarter_33))
    p30.cvolist.append(circle_3)
    self.wait()
    fraction_3 = Tex(r"$\frac{5}{6}$", font_size=96).shift(UP * 4)
    self.play(Write(fraction_3))
    arrow_to_fraction_3 = Arrow(circle_3.get_top() + UP * 0.5, fraction_3, color=WHITE)
    self.play(Create(arrow_to_fraction_3))
    self.wait(2)

    self.play(FadeOut(circle), FadeOut(vertical_line), FadeOut(horizontal_line), FadeOut(quarter_1),
              FadeOut(quarter_2), FadeOut(quarter_3), FadeOut(label_1), FadeOut(label_2), FadeOut(label_3),
              FadeOut(label_4), FadeOut(fraction), FadeOut(arrow_to_fraction), FadeOut(circle_2),
              FadeOut(vertical_line_2), FadeOut(horizontal_line_2), FadeOut(quarter_21), FadeOut(quarter_22),
              FadeOut(quarter_23), FadeOut(label_21), FadeOut(label_22), FadeOut(label_23), FadeOut(label_24),
              FadeOut(fraction_2), FadeOut(arrow_to_fraction_2), FadeOut(circle_3), FadeOut(vertical_line_3),
              FadeOut(horizontal_line_3), FadeOut(quarter_31), FadeOut(quarter_32), FadeOut(quarter_33),
              FadeOut(label_31), FadeOut(label_32), FadeOut(label_33), FadeOut(label_34), FadeOut(fraction_3),
              FadeOut(arrow_to_fraction_3))


if __name__ == "__main__":
    scene = Examples()
    scene.render()
