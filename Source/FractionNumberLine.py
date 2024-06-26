from manim import *

class FractionNumberLine(Scene):
    def construct(self):
        self.example2()

    def example2(self):
        # Title
        examples_title = Text("Fractions on Number Line", font_size=40).to_edge(UP)
        self.play(Write(examples_title))
        
        # Fraction heading
        fraction_heading = MathTex("Example 1: ", r"\frac{7}{6}", font_size=36).to_edge(UP*3 + LEFT)
        self.play(Write(fraction_heading))
        
        # Create NumberLine
        number_line = NumberLine(
            x_range=[0, 1.5, 0.16],
            length=10,
            color=BLUE,
            include_numbers=True,
            label_direction=DOWN,
            font_size=36
        )

        # Fractions to add
        fractions = {
            0.16: r"\frac{1}{6}",
            0.32: r"\frac{2}{6}",
            0.48: r"\frac{3}{6}",
            0.64: r"\frac{4}{6}",
            0.80: r"\frac{5}{6}",
            0.96: r"\frac{6}{6}",
            1.12: r"\frac{7}{6}",
            1.28: r"\frac{8}{6}",
            1.44: r"\frac{9}{6}"
        }

        # Create labels for fractions
        fraction_labels = VGroup()
        for number, label_tex in fractions.items():
            label = MathTex(label_tex, font_size=24).move_to(number_line.number_to_point(number) + UP * 0.5)
            fraction_labels.add(label)
        highlight_rect = Rectangle(width=1, height=1.5, color=RED, fill_opacity=0.3).move_to(number_line.number_to_point(1.12))

        # Animation sequence
        self.play(Create(number_line))
        self.play(Create(fraction_labels))
        self.play(Create(highlight_rect))

if __name__ == "__main__":
    scene = FractionNumberLine()
    scene.render()
