from manim import *

class StandardFormFractions(Scene):
    def construct(self):
        self.show_title()
        self.Standerd()

    def show_title(self):
        title = Text("Standard Form of Fractions", font_size=30).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

    def Standerd(self):
        eq1 = Tex(r"$\frac{1}{3}$",font_size = 30).shift(LEFT * 5)
        eq2 = Tex(r"$\frac{2}{3}$",font_size = 30).shift(LEFT * 3)
        eq3 = Tex(r"$\frac{1}{5}$",font_size = 30).shift(LEFT * 1)
        eq4 = Tex(r"$\frac{3}{11}$",font_size = 30).shift(RIGHT * 1)

        self.play(Write(eq1))
        self.play(Write(eq2))
        self.play(Write(eq3))
        self.play(Write(eq4))

        fraction = Text("Standard Form", font_size=30).shift(RIGHT * 7)
        self.play(Write(fraction))

        arrow_to_fraction = Arrow(eq4.get_center(), fraction.get_center(), color=WHITE)
        self.play(Create(arrow_to_fraction))

        self.wait()

if __name__ == "__main__":
    from manim import config
    config.media_width = "100%"
    scene = StandardFormFractions()
    scene.render()
