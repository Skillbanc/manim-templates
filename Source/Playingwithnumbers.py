from manim import *
from AbstractAnim import AbstractAnim
import cvo

class PlayingWithNumbers(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.show_divisibility_rules()
        self.fadeOutCurrentScene()
        self.show_number_concepts()
        self.fadeOutCurrentScene()
        self.PrimeFactorization()
        self.fadeOutCurrentScene()

    def show_divisibility_rules(self):
        self.display_title("Divisibility Rules")
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
            self.wait(1)
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

    def show_number_concepts(self):
        self.isRandom=False
        self.positionChoice = [[-4,-2,0],[4,-2,0],[3,2,0],[-4,2,0],[-3,2,0],[3,-2,0]]
        p10=cvo.CVO().CreateCVO("Number Concepts","Types").setangle(-TAU/5)
        p11=cvo.CVO().CreateCVO("","Factors")
        p12=cvo.CVO().CreateCVO("","Prime")
        p13=cvo.CVO().CreateCVO("","Composite")
        p14=cvo.CVO().CreateCVO("","Co-Prime")
        p15=cvo.CVO().CreateCVO("","Twin Prime")

        p10.setcircleradius(1.25)
        p11.setcircleradius(1.25)
        p12.setcircleradius(1.25)
        p13.setcircleradius(1.25)
        p14.setcircleradius(1.25)
        p15.setcircleradius(1.25)
    
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)

        self.construct1(p10,p10)
        self.wait(1)
        self.clear_screen()

        self.display_title("Number Concepts")
        self.show_factors()
        self.wait(1)
        self.clear_screen()

        self.show_prime_numbers()
        self.wait(1)
        self.clear_screen()

        self.show_composite_numbers()
        self.wait(1)
        self.clear_screen()

        self.show_co_prime_numbers()
        self.wait(1)
        self.clear_screen()

        self.show_twin_prime_numbers()
        self.wait(1)
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

    def PrimeFactorization(self):
        self.isRandom=False
        self.positionChoice = [[-4,-2,0],[4,-2,0],[3,2,0],[-4,2,0]]
        p10=cvo.CVO().CreateCVO("Prime Factorisation","Methods of Prime Factorisation").setangle(-TAU/5)
        p11=cvo.CVO().CreateCVO("","Division Method")
        p12=cvo.CVO().CreateCVO("","Factor Tree Method")

        p10.setcircleradius(1.25)
        p11.setcircleradius(1.25)
        p12.setcircleradius(1.25)
    
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)

        self.construct1(p10,p10)
        self.wait(1)
        self.clear_screen()

        self.show_factor_tree()
        self.wait(1)
        self.clear_screen()

        self.show_division_method()
        self.wait(1)
        self.clear_screen()

    def show_factor_tree(self):
        title = Text("Factor Tree Method").scale(0.8).to_edge(UP)
        
        lines1 = [
            "A factor tree breaks down a number into its prime factors.",
            "For example, the factor tree of 18:",]
        self.wait(1)
        self.clear_screen()
        lines2 = [     "18",
                     "/  \\",
                     "2    9",
                     "    / \\",
                     "   3   3"
        ]
        self.show_concept(title, lines1)
        self.clear_screen()
        self.show_concept(title, lines2)

    def show_division_method(self):
        title = Text("Division Method").to_edge(UP)
        lines1 = [
            "The division method finds the prime factors of a number by dividing it.",
            "For example, the division method for 18:",]
        self.wait(1)
        self.clear_screen()

        lines2 = [
            "18 ÷ 2 = 9",
            "9 ÷ 3 = 3",
            "3 ÷ 3 = 1",
            "So, the prime factors of 18 are 2 and 3."
        ]
        self.show_concept(title, lines1)
        self.clear_screen()
        self.show_concept(title, lines2)

    def show_concept(self, title, lines):
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

    config.pixel_height = 1080
    config.pixel_width = 1920
    config.frame_height = 8.0
    config.frame_width = 14.0

    scene = PlayingWithNumbers()
    scene.render()
