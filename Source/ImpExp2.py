from manim import *

class ImproperExp2(Scene):
    def construct(self):
        self.ImproperFraction()

    def ImproperFraction(self):
        
        circle = Circle(radius=1, fill_color=BLUE, fill_opacity=0.5).shift(LEFT * 4)
        self.play(Create(circle))

        # Create the sectors and the dividing lines
        sectors = VGroup()
        lines = VGroup()

        for i in range(6):
            start_angle = i * PI / 3
            end_angle = (i + 1) * PI / 3

            # Create each sector
            sector = Sector(radius=1, start_angle=start_angle, angle=PI / 3, color=BLUE, fill_opacity=0.5).shift(LEFT * 4)
            sectors.add(sector)

            # Create each dividing line
            line = Line(circle.get_center(), circle.point_at_angle(start_angle), color=BLACK)
            lines.add(line)

        self.play(Create(sectors), Create(lines))

        # Add vertical and horizontal lines
        vertical_line = Line(circle.get_top(), circle.get_bottom(), color=BLACK).shift(LEFT * 4)
        horizontal_line = Line(circle.get_left(), circle.get_right(), color=BLACK).shift(LEFT * 4)

        self.play(Create(vertical_line), Create(horizontal_line))

        sector1 = Sector(radius=2.5, start_angle=5 * PI / 2, angle=PI / 2, color=BLUE).shift(LEFT*1)
        self.play(Create(sector1))
        sector2 = Sector(radius=2, start_angle=PI/2, angle=PI/2, color=BLUE).shift(RIGHT*1)
        self.play(Create(sector2))


        # Indicate the fraction 6/4
        fraction = Tex(r"$\frac{8}{6}$", font_size=96).shift(RIGHT * 5)
        self.play(Write(fraction))

        # Create an arrow from the circle to the fraction
        arrow_to_fraction = Arrow(sector2.get_bottom(), fraction, color=WHITE)
        self.play(Create(arrow_to_fraction))

        self.wait()

if __name__ == "__main__":
    scene = ImproperExp2()
    scene.render()
