from manim import *

class CreateCircle(Scene):
    def construct(self):
        self.Intro()
        self.FractionDefinition()
        self.Circle()
    def Intro(self):
        title = Text("Fractions and Decimals", font_size=72)
        self.play(FadeIn(title, shift=UP))
        self.wait(2)
        self.play(FadeOut(title))
    def FractionDefinition(self):
        title = Text("What is a Fraction?", font_size=64)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))
    def Circle(self):
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
        quarter_1 = Sector(outer_radius=1, start_angle=PI / 2, angle=PI / 2, color=GREEN, fill_opacity=0.5).shift(LEFT*3)
        quarter_2 = Sector(outer_radius=1, start_angle=0, angle=PI / 2, color=GREEN, fill_opacity=0.5).shift(LEFT*3)
        quarter_3 = Sector(outer_radius=1, start_angle=PI, angle=PI / 2, color=GREEN, fill_opacity=0.5).shift(LEFT*3)

        self.play(Create(quarter_1), Create(quarter_2), Create(quarter_3))  # show the shaded quarters

        self.wait()  # wait for the animation to finish

if __name__ == "__main__":
    scene = CreateCircle()
    scene.render()
