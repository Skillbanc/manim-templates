from manim import *

class MixedExample2(Scene):
    def construct(self):
        self.example2()

    def example2(self):
        # Create a circle and move it to the left
        circle = Circle(radius=1, fill_color=BLUE, fill_opacity=0.5).shift(LEFT * 4)
        self.play(Create(circle))

        # Create the dividing lines for the circle
        lines = VGroup()
        for i in range(3):
            angle = i * 2 * PI / 3
            line = Line(circle.get_center(), circle.point_at_angle(angle), color=YELLOW)
            lines.add(line)

        self.play(Create(lines))

        # Create two sectors with 120 degrees each
        radius = 1
        angle = 120 * DEGREES  # Convert degrees to radians

        sector1 = Sector(radius=radius, angle=angle, fill_color=BLUE, fill_opacity=0.5).shift(LEFT * 1)
        sector2 = Sector(radius=radius, angle=angle, start_angle=angle, fill_color=BLUE, fill_opacity=0.5).shift(LEFT * 1)

        self.play(Create(sector1))
        self.play(Create(sector2))

        # Create the dividing lines for the sectors
        sector_lines = VGroup()
        sector_angles = [0, 120 * DEGREES, 240 * DEGREES]
        for sector in [sector1, sector2]:
            center = LEFT*1
            for angle in sector_angles:
                # Update the calculation for the end point
                end_point = center + radius * np.array([np.cos(angle), np.sin(angle), 0])
                line = Line(center, end_point, color=YELLOW)
                sector_lines.add(line)

        self.play(Create(sector_lines))

        # Indicate the fraction 1/3
        fraction = Tex(r"$1\frac{2}{3}$", font_size=96).shift(RIGHT * 5)
        self.play(Write(fraction))

        # Create an arrow from sector2 to the fraction
        arrow_to_fraction = Arrow(sector1.get_bottom(), fraction.get_center(), color=WHITE)
        self.play(Create(arrow_to_fraction))

if __name__ == "__main__":
    scene = MixedExample2()
    scene.render()