from manim import *

class ImproperExp3(Scene):
    def construct(self):
        self.Example3()
        
    def Example3(self):
        # Create a circle and move it to the left
        circle = Circle(radius=1, fill_color=BLUE, fill_opacity=0.5).shift(LEFT * 4)
        self.play(Create(circle))

        # Create the dividing lines
        lines = VGroup()
        for i in range(3):
            angle = i * 2 * PI / 3
            line = Line(circle.get_center(), circle.point_at_angle(angle), color=YELLOW)
            lines.add(line)

        self.play(Create(lines))

        # Create a sector to highlight one part
        #sector = Sector(outer_radius=1, angle=2 * PI / 3, start_angle=0, color=GREEN, fill_opacity=0.5).shift(LEFT * 4)
        #self.play(Create(sector))

        # Add boundaries to the sector
        sector_boundary_lines = VGroup(
            Line(circle.get_center(), circle.point_at_angle(0), color=RED).shift(LEFT * 4),
            Line(circle.get_center(), circle.point_at_angle(2 * PI / 3), color=RED).shift(LEFT * 4)
            
        )
        
        
        self.play(Create(sector_boundary_lines))
        sector1 = Sector(radius=2.5, start_angle=5 * PI / 2, angle=PI / 2, fill_color=BLUE, fill_opacity=0.5).shift(LEFT*1)
        self.play(Create(sector1))
        # Indicate the fraction 1/3
        fraction = MathTex(r"\frac{1}{3}", font_size=96).shift(RIGHT * 5)
        self.play(Write(fraction))

        # Create an arrow from the circle to the fraction
        arrow_to_fraction = Arrow(sector1.get_bottom(), fraction, color=WHITE)
        self.play(Create(arrow_to_fraction))

        self.wait()

# To render the scene, save it in a file and run it with Manim
if __name__ == "__main__":
  #  from manim import config
   # config.media_width = "75%"
    scene = ImproperExp3()
    scene.render()
