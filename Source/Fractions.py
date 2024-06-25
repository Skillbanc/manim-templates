from manim import *

class FractionsAndDecimals(Scene):
    def construct(self):
        self.Intro()
        self.FractionDefinition()
        self.FractionOperations()
        self.FractionToDecimal()

    def Intro(self):
        title = Text("Fractions and Decimals", font_size=72)
        subtitle = Text("An Introduction", font_size=48)
        VGroup(title, subtitle).arrange(DOWN)
        self.play(FadeIn(title, shift=UP), FadeIn(subtitle, shift=DOWN))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))

    def FractionDefinition(self):
        title = Text("What is a Fraction?", font_size=64)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Example of a fraction
        fraction = MathTex(r"\frac{3}{4}", font_size=96)
        self.play(Write(fraction))
        self.wait(2)

        # Visual representation using a pie chart
        circle = Circle()
        part = Sector(angle=PI/2, fill_color=BLUE, fill_opacity=0.5)
        VGroup(circle, part).arrange(RIGHT)
        self.play(FadeIn(circle), FadeIn(part))
        self.wait(2)

    def FractionOperations(self):
        title = Text("Operations with Fractions", font_size=64)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Addition of fractions example
        addition = MathTex(r"\frac{1}{2} + \frac{1}{3} = \frac{3}{6} + \frac{2}{6} = \frac{5}{6}", font_size=48)
        self.play(Write(addition))
        self.wait(2)
        self.play(FadeOut(addition))

        # Multiplication of fractions example
        multiplication = MathTex(r"\frac{2}{3} \times \frac{3}{4} = \frac{6}{12} = \frac{1}{2}", font_size=48)
        self.play(Write(multiplication))
        self.wait(2)
        self.play(FadeOut(multiplication))

    def FractionToDecimal(self):
        title = Text("Converting Fractions to Decimals", font_size=64)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Simple conversion example
        conversion = MathTex(r"\frac{1}{4} = 0.25", font_size=48)
        self.play(Write(conversion))
        self.wait(2)
        self.play(FadeOut(conversion))

if __name__ == "__main__":
    scene = FractionsAndDecimals()
    scene.render()
