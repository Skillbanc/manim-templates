from manim import *

class MixedExample1(Scene):
    def construct(self):
        self.example1()

    def example1(self):
        # Create circles
        circle1 = Circle(radius=1, fill_color=BLUE, fill_opacity=1).shift(LEFT * 4)
        circle2 = Circle(radius=1, fill_color=BLUE, fill_opacity=1).shift(LEFT * 1)

        # Get centers of circles
        center_circle1 = circle1.get_center()
        center_circle2 = circle2.get_center()
        
        # Calculate endpoints for the vertical line within circle1
        start_point1 = center_circle1 + UP * 1  # Start slightly above the center
        end_point1 = center_circle1 + DOWN * 1  # End slightly below the center

        # Calculate endpoints for the vertical line within circle2
        start_point2 = center_circle2 + UP * 1  # Start slightly left of the center
        end_point2 = center_circle2 + DOWN * 1  # End slightly right of the center

        # Create vertical lines inside circles
        vertical_line1 = Line(start=start_point1, end=end_point1, color=BLACK)
        vertical_line2 = Line(start=start_point2, end=end_point2, color=BLACK)

        # Create an arc
        arc = Arc(radius=1, start_angle=PI/2, angle=PI, fill_color=BLUE, fill_opacity=1).shift(RIGHT * 2)
        fraction = Tex(r"$2\frac{1}{2}$", font_size=80).shift(RIGHT*5)
        

        arrow_to_fraction = Arrow(arc.get_center(), fraction, color=WHITE)

       
        # Show animations
        self.play(Create(circle1))
        self.play(Create(vertical_line1))
        self.play(Create(circle2))
        self.play(Create(vertical_line2))
        self.play(Create(arc))
        self.play(Write(fraction))
        self.play(Create(arrow_to_fraction))
       

if __name__ == "__main__":
    scene = MixedExample1()
    scene.render()
