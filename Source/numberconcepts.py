from manim import *
from AbstractAnim import AbstractAnim
import cvo


class NumberConcepts(Scene):
    def construct(self):
        self.display_title("Number Concepts")
        self.wait(1)
        self.clear_screen()
        
        self.show_factors()
        self.wait(2)
        self.clear_screen()
        
        self.show_prime_numbers()
        self.wait(2)
        self.clear_screen()
        
        self.show_composite_numbers()
        self.wait(2)
        self.clear_screen()
        
        self.show_co_prime_numbers()
        self.wait(2)
        self.clear_screen()
        
        self.show_twin_prime_numbers()
        self.wait(2)
        self.clear_screen()

    def display_title(self, title_text):
        title = Text(title_text).scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

    def show_factors(self):
        title = Text("Factors").scale(0.8).to_edge(UP)
        lines = [
            "Factors of a number are the numbers that divide",
            "it exactly without leaving a remainder.",
            "For example, factors of 12 are 1, 2, 3, 4, 6, and 12."
        ]
        self.show_concept(title, lines)

    def show_prime_numbers(self):
        title = Text("Prime Numbers").scale(0.8).to_edge(UP)
        lines = [
            "A prime number is a natural number greater than 1",
            "that has no positive divisors other than 1 and itself.",
            "For example, 2, 3, 5, 7, 11, etc."
        ]
        self.show_concept(title, lines)

    def show_composite_numbers(self):
        title = Text("Composite Numbers").scale(0.8).to_edge(UP)
        lines = [
            "A composite number is a natural number greater than 1",
            "that is not a prime number.",
            "It has factors other than 1 and itself.",
            "For example, 4, 6, 8, 9, 10, etc."
        ]
        self.show_concept(title, lines)

    def show_co_prime_numbers(self):
        title = Text("Co-prime Numbers").scale(0.8).to_edge(UP)
        lines = [
            "Two numbers are co-prime if their greatest",
            "common divisor (GCD) is 1.",
            "For example, 8 and 15 are co-prime."
        ]
        self.show_concept(title, lines)

    def show_twin_prime_numbers(self):
        title = Text("Twin Prime Numbers").scale(0.8).to_edge(UP)
        lines = [
            "Twin prime numbers are pairs of prime numbers",
            "that have a difference of 2.",
            "For example, (3, 5), (11, 13), (17, 19), etc."
        ]
        self.show_concept(title, lines)

    def show_concept(self, title, lines):
        self.play(Write(title))
        self.wait(1)

        for i, line in enumerate(lines):
            text = Text(line).scale(0.6).shift(DOWN * (i - 1))
            self.play(Write(text))
            self.wait(1)

    def clear_screen(self):
        self.play(*[FadeOut(mob) for mob in self.mobjects])

if __name__ == "__main__":
    from manim import config
    scene = NumberConcepts()
    scene.render()
    config.pixel_height = 1080
    config.pixel_width = 1920
    config.frame_height = 8.0
    config.frame_width = 14.0
    config.output_file = "number_concepts.mp4"