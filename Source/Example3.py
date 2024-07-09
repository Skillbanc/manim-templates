from manim import *

class Example3(Scene):
    def construct(self):
        self.CircleExample3()

    def CircleExample3(self):
        # Create a rectangle and lines
        rect = Rectangle(width=7, height=1, color=WHITE, stroke_width=2).shift(LEFT * 3)
        lines = VGroup(*[Line(start=rect.get_corner(DL) + RIGHT * i, end=rect.get_corner(UL) + RIGHT * i) for i in range(1, 6)])

        # Create shaded rectangles (adjusting positions for last two)
        shaded_rect1 = Rectangle(width=1, height=1, color=BLUE, fill_opacity=0.5).move_to(rect.get_center() + RIGHT * 2 )
        shaded_rect2 = Rectangle(width=1, height=1, color=BLUE, fill_opacity=0.5).move_to(rect.get_center() +  RIGHT * 3)

        # Create fraction
        fraction = MathTex(r"\frac{2}{7}", font_size=96).shift(RIGHT*5)

        # Create arrow from rectangle to fraction
        arrow_to_fraction = Arrow(shaded_rect2.get_right(), fraction.get_left(), color=WHITE)

        # Animation sequence
        self.play(Create(rect))
        self.play(Create(lines))
        self.play(Create(shaded_rect1), Create(shaded_rect2))
        self.play(Write(fraction))
        self.play(Create(arrow_to_fraction))

        self.wait(0.5)

if __name__ == "__main__":
    scene = Example3()
    scene.render()
