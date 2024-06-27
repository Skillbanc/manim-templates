from manim import *

class test87(Scene):
    def construct(self):
        # Create a horizontal line to represent a measuring stick
        line = Line(LEFT * 4, RIGHT * 4, color=WHITE)
        self.play(Create(line))

        # Hand breadth
        hand_breadth = Rectangle(width=0.5, height=1, color=BLUE)
        hand_breadth.next_to(line, UP)
        hand_breadth_text = Text("Hand breadth", font_size=24).next_to(hand_breadth, UP)
        self.play(Create(hand_breadth), Write(hand_breadth_text))
        self.wait(1)
        self.play(FadeOut(hand_breadth), FadeOut(hand_breadth_text))

        # Hand span
        hand_span = Rectangle(width=1.5, height=1, color=GREEN)
        hand_span.next_to(line, UP)
        hand_span_text = Text("Hand span", font_size=24).next_to(hand_span, UP)
        self.play(Create(hand_span), Write(hand_span_text))
        self.wait(1)
        self.play(FadeOut(hand_span), FadeOut(hand_span_text))

        # Cubit
        cubit = Rectangle(width=3, height=1, color=RED)
        cubit.next_to(line, UP)
        cubit_text = Text("Cubit", font_size=24).next_to(cubit, UP)
        self.play(Create(cubit), Write(cubit_text))
        self.wait(1)
        self.play(FadeOut(cubit), FadeOut(cubit_text))

        # Foot
        foot = Rectangle(width=2, height=0.5, color=YELLOW)
        foot.next_to(line, UP)
        foot_text = Text("Foot", font_size=24).next_to(foot, UP)
        self.play(Create(foot), Write(foot_text))
        self.wait(1)
        self.play(FadeOut(foot), FadeOut(foot_text))

        self.wait(1)


if __name__ == "__main__":
    scene = test87()
    scene.render()