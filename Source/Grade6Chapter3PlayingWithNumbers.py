from manim import *
from AbstractAnim import AbstractAnim
import cvo
class Grade6Chapter3PlayingWithNumbers(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.show_divisibility_rules()
        self.fadeOutCurrentScene()
        self.show_number_concepts()
        self.fadeOutCurrentScene()
        self.PrimeFactorization()
        self.fadeOutCurrentScene()
        self.HCF()
        self.fadeOutCurrentScene()
        self.LCM()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

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
        self.positionChoice = [[0,2.5,0],[5,0,0],[-4,-2,0],[0,-2.5,0],[4,-2,0],[-5,0,0]]
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
        self.positionChoice = [[0,2,0],[-3,-2,0],[3,-2,0]]
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


    def HCF(self):
        self.isRandom=False
        self.positionChoice = [[0,2,0],[-3,-2,0],[3,-2,0]]
        p10=cvo.CVO().CreateCVO("Highest Common Factor(HCF)","Methods of Finding HCF").setangle(-TAU/5)
        p11=cvo.CVO().CreateCVO("","Prime Factorisation")
        p12=cvo.CVO().CreateCVO("","Continued Division Method")
       
        p10.setcircleradius(1.25)
        p11.setcircleradius(1.25)
        p12.setcircleradius(1.25)
    
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        

        self.construct1(p10,p10)
        self.wait(1)
        self.clear()
        self.hcf_prime_factorization_steps()
        self.wait(2)
        self.clear()
        self.hcf_prime_factorization()
        self.wait(2)
        self.clear()
        self.hcf_continued_division_steps()
        self.wait(2)
        self.clear()
        self.hcf_continued_division()


    def hcf_prime_factorization_steps(self):
        definition = Text("HCF (Highest Common Factor) using Prime Factorization", font_size=36)
        definition.to_edge(UP)
        self.play(Write(definition))
        self.wait(1)

        steps = [
            "1. Find the prime factors of each number.",
            "2. Identify the common prime factors.",
            "3. Multiply the lowest powers of the common factors."
        ]

        explanation = VGroup(*[Text(step, font_size=24) for step in steps])
        explanation.arrange(DOWN, aligned_edge=LEFT)
        explanation.next_to(definition, DOWN, buff=0.5)

        self.play(Write(explanation))
        self.wait(2)

    def hcf_prime_factorization(self):
        heading = Text("Prime Factorisation Method", color=DARK_BROWN, font_size=37).to_edge(UP * 1.25 + LEFT * 2)
        sub_title1 = Text("The HCF of 12, 30 and 36 can also be found by prime factorisation as follows:", font_size=29).to_edge(UP * 3 + LEFT * 1)
        sub_title3 = Text("12 = 2 × 3 × 2", font_size=29)
        sub_title4 = Text("30 = 2 × 3 × 5", font_size=29)
        sub_title5 = Text("36 = 2 × 3 × 2 × 3", font_size=29)
        sub_title6 = Text("The common factor of 12, 30 and 36 is 2 x 3 = 6.", font_size=29).to_edge(UP * 12.25 + LEFT * 1)
        sub_title7 = Text("Hence, HCF of 12, 30 and 36 is 6.", font_size=29).to_edge(UP * 13.5)
        sub_title3.move_to([-4, -1, 0])
        sub_title4.move_to([0, -1, 0])
        sub_title5.move_to([4, -1, 0])

        t0 = Table(
            [["2", "12"],
             ["2", "6"],
             ["3", "3"],
             ["", "1"]]).scale(0.4)

        t1 = Table(
            [["2", "30"],
             ["3", "15"],
             ["5", "5"],
             ["", "1"]]).scale(0.4)

        t2 = Table(
            [["3", "36"],
             ["3", "12"],
             ["2", "4"],
             ["2", "2"],
             ["", "1"]]
        ).scale(0.4)

        t0.move_to([-4, 1, 0])
        t1.move_to([0, 1, 0])
        t2.move_to([4, 1, 0])

        self.play(Write(heading))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(t0))
        self.wait(1)
        self.play(Write(sub_title3))
        self.wait(1)
        self.play(Write(t1))
        self.wait(1)
        self.play(Write(sub_title4))
        self.wait(1)
        self.play(Write(t2))
        self.play(Write(sub_title5))
        self.wait(1)
        self.play(Write(sub_title6))
        self.wait(1)
        self.play(Write(sub_title7))
        self.wait(1)
        self.play(FadeOut(sub_title7), FadeOut(sub_title6), FadeOut(sub_title5), FadeOut(t2), FadeOut(sub_title4), FadeOut(t1), FadeOut(sub_title3), FadeOut(t0), FadeOut(sub_title1), FadeOut(heading))

    
    def hcf_continued_division_steps(self):
        definition = Text("HCF (Highest Common Factor) using Continued Division", font_size=36)
        definition.to_edge(UP)
        self.play(Write(definition))
        self.wait(1)

        steps = [
            "1. Divide the larger number by the smaller number.",
            "2. Replace the larger number with the smaller number and the smaller number with the remainder.",
            "3. Repeat the process until the remainder is 0.",
            "4. The last non-zero remainder is the HCF."
        ]

        explanation = VGroup(*[Text(step, font_size=23) for step in steps])
        explanation.arrange(DOWN, aligned_edge=LEFT)
        explanation.next_to(definition, DOWN, buff=0.5)

        self.play(Write(explanation))
        self.wait(2)

    def hcf_continued_division(self):
        heading = Text("Continued Division Method", color=DARK_BROWN, font_size=37).to_edge(UP * 1.25 + LEFT * 2)
        sub_title1 = Text("The HCF of 56 and 98 can be found using the continued division method as follows:", font_size=29).to_edge(UP * 3 + LEFT * 1)
        
        division_steps = [
            "98 ÷ 56 = 1 remainder 42",
            "56 ÷ 42 = 1 remainder 14",
            "42 ÷ 14 = 3 remainder 0"
        ]

        division_texts = [Text(step, font_size=29).move_to([0, 1 - i * 0.75, 0]) for i, step in enumerate(division_steps)]
        conclusion_text = Text("Hence, HCF of 56 and 98 is 14.", font_size=29).move_to([0, -1.75, 0])

        self.play(Write(heading))
        self.play(Write(sub_title1))
        self.wait(1)

        for division_text in division_texts:
            self.play(Write(division_text))
            self.wait(1)

        self.play(Write(conclusion_text))
        self.wait(2)


    def LCM(self):
        self.isRandom=False
        self.positionChoice = [[0,2,0],[-3,-2,0],[3,-2,0]]
        p10=cvo.CVO().CreateCVO("Least Common Multiple (LCM)","Methods of Finding LCM").setangle(-TAU/5)
        p11=cvo.CVO().CreateCVO("","Prime Factorisation")
        p12=cvo.CVO().CreateCVO("","Division Method")
       
        p10.setcircleradius(1.25)
        p11.setcircleradius(1.25)
        p12.setcircleradius(1.25)
    
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        

        self.construct1(p10,p10)
        self.wait(1)
        self.clear()
        self.lcm_prime_factorization_steps()
        self.wait(2)
        self.clear()
        self.lcm_prime_factorization()
        self.wait(2)
        self.clear()
        self.lcm_division_steps()
        self.wait(2)
        self.clear()
        self.lcm_division_method()


    def lcm_prime_factorization_steps(self):
        definition = Text("LCM (Least Common Multiple) using Prime Factorization", font_size=36)
        definition.to_edge(UP)
        self.play(Write(definition))
        self.wait(1)

        steps = [
            "1. Find the prime factors of each number.",
            "2. Identify all prime factors.",
            "3. Multiply the highest powers of all factors."
        ]

        explanation = VGroup(*[Text(step, font_size=24) for step in steps])
        explanation.arrange(DOWN, aligned_edge=LEFT)
        explanation.next_to(definition, DOWN, buff=0.5)

        self.play(Write(explanation))
        self.wait(2)


    def lcm_prime_factorization(self):
        heading = Text("Prime Factorization Method", color=DARK_BROWN, font_size=37).to_edge(UP * 1.25 + LEFT * 2)
        sub_title1 = Text("The LCM of 36 and 60 can be found by prime factorization method as follows:-", font_size=29).to_edge(UP * 3 + LEFT * 1)
        
        factorization_steps = [
            "Factors of 36 = 2 × 2 × 3 × 3",
            "Factors of 60 = 2 × 2 × 3 × 5",
            "Take the common factors of both: 2 × 2 × 3",
            "Take the extra factors of both 36 and 60 i.e. 3 and 5."
        ]

        factorization_text = [Text(step, font_size=29).move_to([0, 1 - i * 0.75, 0]) for i, step in enumerate(factorization_steps)]
        conclusion_text = Text("Hence, the LCM of 36 and 60 = (2 × 2 × 3) × 3 × 5 = 180", font_size=29).move_to([0, -1.75, 0])

        self.play(Write(heading))
        self.play(Write(sub_title1))
        self.wait(1)

        for factorization_text in factorization_text:
            self.play(Write(factorization_text))
            self.wait(1)

        self.play(Write(conclusion_text))
        self.wait(2)

    def lcm_division_steps(self):
        definition = Text("LCM (Least Common Multiple) using Division Method", font_size=36)
        definition.to_edge(UP)
        self.play(Write(definition))
        self.wait(1)

        steps = [
            "1. Write the numbers in a horizontal line.",
            "2. Divide the numbers by their common prime factors, starting with the smallest prime.",
            "3. Write the quotient below each number.",
            "4. Repeat until all quotients are 1.",
            "5. Multiply all the prime factors to get the LCM."
        ]

        explanation = VGroup(*[Text(step, font_size=24) for step in steps])
        explanation.arrange(DOWN, aligned_edge=LEFT)
        explanation.next_to(definition, DOWN, buff=0.5)

        self.play(Write(explanation))
        self.wait(2)

    
    def lcm_division_method(self):
        heading = Text("Division Method", color=DARK_BROWN, font_size=37).to_edge(UP * 1.25 + LEFT * 2)
        sub_title1 = Text("To find the LCM of 24 and 90:", font_size=29).to_edge(UP * 3 + LEFT * 1)
        sub_title2 = Text("Thus, the LCM of 24 and 90 is 2 × 3 × 4 × 15 = 360", font_size=29).to_edge(UP * 12.25 + LEFT * 1)
        

        t0 = Table(
            [["2", "24,90"],
             ["3", "12,45"],
             ["", "4,15"]]).scale(0.6)

        t0.move_to([0, 1, 0])

        self.play(Write(heading))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(t0))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)
        self.play(FadeOut(sub_title2),FadeOut(t0), FadeOut(sub_title1), FadeOut(heading))
    def SetDeveloperList(self):
        self.DeveloperList="Bommi Yaswanth"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade6Chapter3PlayingWithNumbers.py"

if __name__ == "__main__":
    from manim import config

    scene = Grade6Chapter3PlayingWithNumbers()
    scene.render()
