from manim import *

class NumberLine2(Scene):
    def construct(self):
        self.example2()

    def example2(self):
        # Fraction heading
        fraction_heading = MathTex("Example 2: ", r"\frac{5}{2}", font_size=36).to_edge(UP*3 + LEFT)
        self.play(Write(fraction_heading))
        
        # Create NumberLine
        number_line = NumberLine(
            x_range=[0, 3, 0.5],
            length=10,
            color=BLUE,
            include_numbers=True,
            label_direction=DOWN,
            font_size=36
        )

        # Fractions to add
        fractions = {
            0.5: r"\frac{1}{2}",
            1.0: r"\frac{2}{2}",
            1.5: r"\frac{3}{2}",
            2.0: r"\frac{4}{2}",
            2.5: r"\frac{5}{2}"
            
        }

        # Create labels for fractions
        fraction_labels = VGroup()
        for number, label_tex in fractions.items():
            label = MathTex(label_tex, font_size=24).move_to(number_line.number_to_point(number) + UP * 0.5)
            fraction_labels.add(label)
        highlight_rect = Rectangle(width=1, height=1.5, color=RED, fill_opacity=0.2).move_to(number_line.number_to_point(2.5))

        # Animation sequence
        self.play(Create(number_line))
        self.play(Create(fraction_labels))
        self.play(Create(highlight_rect))

if __name__ == "__main__":
    scene = NumberLine2()
    scene.render()
