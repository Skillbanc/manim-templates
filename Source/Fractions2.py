import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo

class Fractions(Scene):
    def construct(self):
        self.Intro()
        self.FractionDefinition()
        self.NumeratorAndDenominator()
        self.VisualRepresentation()

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

        definition = Text("A fraction represents a part of a whole.", font_size=36)
        self.play(Write(definition))
        self.wait(2)
        self.play(FadeOut(definition))

    def NumeratorAndDenominator(self):
        title = Text("Numerator and Denominator", font_size=64)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        fraction = Tex(r"$\frac{3}{4}$", font_size=96)
        numerator = Text("Numerator", font_size=36, color=BLUE).next_to(fraction, UP)
        denominator = Text("Denominator", font_size=36, color=RED).next_to(fraction, DOWN)
        arrow_numerator = Arrow(numerator.get_bottom(), fraction[0][0].get_top(), buff=0.1, color=BLUE)
        arrow_denominator = Arrow(denominator.get_top(), fraction[0][2].get_bottom(), buff=0.1, color=RED)

        self.play(Write(fraction))
        self.wait(1)
        self.play(Write(numerator), Write(denominator))
        self.play(Create(arrow_numerator), Create(arrow_denominator))
        self.wait(2)
        self.play(FadeOut(fraction), FadeOut(numerator), FadeOut(denominator), FadeOut(arrow_numerator), FadeOut(arrow_denominator))

    def VisualRepresentation(self):
        title = Text("Visual Representation", font_size=64)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Create a circle divided into 4 parts
        circle = Circle().shift(LEFT*3)
        radius = circle.get_width() / 2
        lines = VGroup(
            Line(circle.get_center(), circle.get_center() + UP*radius, color=BLACK),
            Line(circle.get_center(), circle.get_center() + LEFT*radius, color=BLACK),
            Line(circle.get_center(), circle.get_center() + DOWN*radius, color=BLACK),
            Line(circle.get_center(), circle.get_center() + RIGHT*radius, color=BLACK),
        )
        
        # Shade 3 out of 4 parts
        sector_1 = Sector(outer_radius=radius, angle=PI/2, color=GREEN, fill_opacity=0.5).shift(LEFT*3)
        sector_2 = Sector(outer_radius=radius, start_angle=PI/2, angle=PI/2, color=GREEN, fill_opacity=0.5).shift(LEFT*3)
        sector_3 = Sector(outer_radius=radius, start_angle=PI, angle=PI/2, color=GREEN, fill_opacity=0.5).shift(LEFT*3)

        # Labels for each quarter
        label_1 = Text("1", color=BLACK).move_to(UP * 0.5 + LEFT * 0.5 + LEFT*3)
        label_2 = Text("2", color=BLACK).move_to(UP * 0.5 + RIGHT * 0.5 + LEFT*3)
        label_3 = Text("3", color=BLACK).move_to(DOWN * 0.5 + LEFT * 0.5 + LEFT*3)
        label_4 = Text("4", color=BLACK).move_to(DOWN * 0.5 + RIGHT * 0.5 + LEFT*3)

        self.play(Create(circle), Create(lines))  # Show the circle and lines
        self.play(Create(sector_1), Create(sector_2), Create(sector_3))  # Shade the sectors
        self.play(Write(label_1), Write(label_2), Write(label_3), Write(label_4))  # Show the labels

        # Indicate the fraction 3/4
        fraction = Tex(r"$\frac{3}{4}$", font_size=96).shift(RIGHT*3)
        self.play(Write(fraction))

        # Create arrow from circle to fraction
        arrow_to_fraction = Arrow(circle.get_right(), fraction, color=WHITE)

        self.play(Create(arrow_to_fraction))

        self.wait(2)
        self.play(FadeOut(circle), FadeOut(lines), FadeOut(sector_1), FadeOut(sector_2), FadeOut(sector_3), FadeOut(label_1), FadeOut(label_2), FadeOut(label_3), FadeOut(label_4), FadeOut(fraction), FadeOut(arrow_to_fraction))

if __name__ == "__main__":
    scene = Fractions()
    scene.render()
