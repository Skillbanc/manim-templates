from manim import *
from AbstractAnim import AbstractAnim
import cvo

class DivisionMethod(Scene):
    def construct(self):
        self.number = 42  # Example number for prime factorization
        self.definition_text()
        self.division_method()

    def definition_text(self):
        definition = Text("Division Method of Prime Factorization", font_size=36)
        definition.to_edge(UP)
        self.play(Write(definition))
        self.wait(1)

        steps = [
            "1. Start with the smallest prime number (2).",
            "2. Divide the number by this prime.",
            "3. If divisible, write down the quotient and repeat with the quotient.",
            "4. If not divisible, move to the next prime number.",
            "5. Continue until the quotient is 1.",
            "6. The prime factors are the divisors used."
        ]

        explanation = VGroup(*[Text(step, font_size=24) for step in steps])
        explanation.arrange(DOWN, aligned_edge=LEFT)
        explanation.next_to(definition, DOWN, buff=0.5)

        self.play(Write(explanation))
        self.wait(3)
        self.play(FadeOut(explanation))

    def division_method(self):
        factors = self.long_division_method(self.number)
        self.display_division_steps(factors, self.number)

    def long_division_method(self, n):
        factors = []
        divisor = 2
        while n > 1:
            if n % divisor == 0:
                factors.append((n, divisor))
                n = n // divisor
            else:
                divisor += 1
        if not factors:
            factors.append((n, 1))  # Handle the prime number case
        return factors

    def display_division_steps(self, factors, number):
        start_y = 2
        x_offset = 0

        number_text = Text(str(number)).move_to(UP * start_y + LEFT * 2)
        self.play(Write(number_text))

        for i, (num, div) in enumerate(factors):
            div_text = Text(str(div)).move_to(UP * start_y + RIGHT * 2 + DOWN * i)
            line = Line(start=UP * (start_y - i) + LEFT, end=UP * (start_y - i) + RIGHT)
            quotient = num // div
            quotient_text = Text(str(quotient)).next_to(line, DOWN)

            self.play(Write(div_text))
            self.play(Create(line))
            self.play(Write(quotient_text))

            start_y -= 1.5

        if len(factors) == 1 and factors[0][1] == 1:
            prime_indicator = Text("Prime Number").next_to(quotient_text, DOWN)
            self.play(Write(prime_indicator))

if __name__ == "__main__":
    scene = DivisionMethod()
    scene.render()