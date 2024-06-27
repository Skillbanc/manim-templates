from manim import *

class MultiplicationWithZero(Scene):
    def construct(self):
        # Title
        title = Text("Multiplication with Zero", font_size=48).to_edge(UP)
        underline = Line(
            start=title.get_left() + DOWN * 0.3,
            end=title.get_right() + DOWN * 0.3,
            color=YELLOW
        )
        self.play(Write(title))
        self.play(Create(underline))
        self.wait(1)

        # Summary
        summary1 = Text(
            "Multiplying any number by zero always results in zero.",
            font_size=30
        ).next_to(title, DOWN, buff=0.8)
        self.play(Write(summary1))
        self.wait(1)

        # Examples title
        example1 = Text("Examples:", font_size=36).next_to(summary1.get_left(), DOWN+RIGHT*0.1, buff=1)
        self.play(Write(example1))
        self.wait(1)

        # Examples for multiplication with zero
        multiply1 = Text("0 x 1 = 0", font_size=36).next_to(example1, RIGHT, buff=0.5)
        multiply2 = Text("0 x 2 = 0", font_size=36).next_to(multiply1, DOWN, buff=0.3).align_to(multiply1, LEFT)
        multiply3 = Text("0 x 3 = 0", font_size=36).next_to(multiply2, DOWN, buff=0.3).align_to(multiply1, LEFT)
        multiply4 = Text("0 x 4 = 0", font_size=36).next_to(multiply3, DOWN, buff=0.3).align_to(multiply1, LEFT)
        multiply5 = Text("0 x 5 = 0", font_size=36).next_to(multiply4, DOWN, buff=0.3).align_to(multiply1, LEFT)
        multiply6 = Text("0 x 6 = 0", font_size=36).next_to(multiply5, DOWN, buff=0.3).align_to(multiply1, LEFT)

        # Display examples
        self.play(Write(multiply1))
        self.play(Write(multiply2))
        self.play(Write(multiply3))
        self.play(Write(multiply4))
        self.play(Write(multiply5))
        self.play(Write(multiply6))
        self.wait(1)

        # Fade out all elements
        self.play(FadeOut(title, underline, summary1, example1, multiply1, multiply2, multiply3, multiply4, multiply5, multiply6))

# To render the scene
if __name__ == "__main__":
    scene = MultiplicationWithZero()
    scene.render()
