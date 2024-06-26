from manim import *
from AbstractAnim import AbstractAnim
import cvo

class divisibility_rules(Scene):
    def construct(self):
        self.display_title()
        self.show_divisibility_rules()

    def display_title(self):
        title = Text("Divisibility Rules").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

    def show_divisibility_rules(self):
        rules = [
            ("Divisibility Rule for 2", [
                "A number is divisible by 2 if",
                "the last digit is even (0, 2, 4, 6, 8)."
            ]),
            ("Divisibility Rule for 3", [
                "A number is divisible by 3 if",
                "the sum of its digits is divisible by 3."
            ]),
            ("Divisibility Rule for 4", [
                "A number is divisible by 4 if",
                "the last two digits form a number",
                "that is divisible by 4."
            ]),
            ("Divisibility Rule for 5", [
                "A number is divisible by 5 if",
                "the last digit is 0 or 5."
            ]),
            ("Divisibility Rule for 6", [
                "A number is divisible by 6 if",
                "it is divisible by both 2 and 3."
            ]),
            ("Divisibility Rule for 7", [
                "A number is divisible by 7 if",
                "doubling the last digit and",
                "subtracting it from the rest of",
                "the number gives a result",
                "that is divisible by 7."
            ]),
            ("Divisibility Rule for 8", [
                "A number is divisible by 8 if",
                "the last three digits form a number",
                "that is divisible by 8."
            ]),
            ("Divisibility Rule for 9", [
                "A number is divisible by 9 if",
                "the sum of its digits is divisible by 9."
            ]),
            ("Divisibility Rule for 10", [
                "A number is divisible by 10 if",
                "the last digit is 0."
            ]),
            ("Divisibility Rule for 11", [
                "A number is divisible by 11 if",
                "the difference between the sum of the digits",
                "in the odd positions and the sum of the digits",
                "in the even positions is divisible by 11."
            ])
        ]

        for rule in rules:
            self.show_rule(rule)
            self.wait(0.5)
            self.clear_screen()

    def show_rule(self, rule):
        title_text, lines = rule
        title = Text(title_text).scale(0.8).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        for i, line in enumerate(lines):
            text = Text(line).scale(0.6).shift(DOWN * (i - 1))
            self.play(Write(text))
            self.wait(0.5)

    def clear_screen(self):
        self.play(*[FadeOut(mob) for mob in self.mobjects])

if __name__ == "__main__":
    from manim import config
    scene = divisibility_rules()
    scene.render()
    # config.pixel_height = 1080
    # config.pixel_width = 1920
    # config.frame_height = 8.0
    # config.frame_width = 14.0
    # config.output_file = "divisibility_rules.mp4"