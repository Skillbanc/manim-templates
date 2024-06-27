from manim import *

class ImproperFraction(Scene):
    def construct(self):
        self.ImproperFraction()

    def ImproperFraction(self):
        examples_title = Text("Improper Fractions Examples ", font_size=30).to_edge(UP)
        self.play(Write(examples_title))
        circle = Circle(fill_color=PINK, fill_opacity=1).shift(LEFT*4)  # create a circle and move it to the left
        # Create vertical and horizontal lines
        vertical_line = Line(ORIGIN, UP * 2, color=BLACK).shift(LEFT*3)
        horizontal_line = Line(ORIGIN, RIGHT * 2, color=BLACK).shift(LEFT*3)

        # Position the lines at the center
        vertical_line.move_to(circle.get_center())
        horizontal_line.move_to(circle.get_center())

        self.play(Create(circle), Create(vertical_line), Create(horizontal_line))
        # Indicate the fraction 3/4
        arc_1 = Sector(radius=2.5, start_angle=5 * PI / 2, angle=PI / 2, color=PINK).shift(LEFT*1)
        self.play(Create(arc_1))
        sector = Sector(radius=2, start_angle=PI/2, angle=PI/2, color=BLUE, fill_opacity=0.5).shift(RIGHT*1)
        self.play(Create(sector))



        fraction = Tex(r"$\frac{6}{4}$", font_size=96).shift(RIGHT*5)
        self.play(Write(fraction))

        # Create arrow from circle to fraction
        arrow_to_fraction = Arrow(sector.get_bottom(), fraction, color=WHITE)

        self.play(Create(arrow_to_fraction))
        

if __name__ == "__main__":
    scene = ImproperFraction()
    scene.render()
