from manim import *
from AbstractAnim import AbstractAnim
import cvo 

class AbstractAnim(Scene):
    def construct(self):
        pass

def prime_factors(n):
    """Return the list of prime factors of n"""
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def find_hcf(a, b):
    """Return the HCF of a and b using the prime factorization method"""
    factors_a = prime_factors(a)
    factors_b = prime_factors(b)
    common_factors = set(factors_a).intersection(set(factors_b))
    hcf = 1
    for factor in common_factors:
        hcf *= min(factors_a.count(factor), factors_b.count(factor)) * factor
    return hcf

def find_lcm(a, b):
    """Return the LCM of a and b using the prime factorization method"""
    factors_a = prime_factors(a)
    factors_b = prime_factors(b)
    all_factors = set(factors_a).union(set(factors_b))
    lcm = 1
    for factor in all_factors:
        lcm *= max(factors_a.count(factor), factors_b.count(factor)) * factor
    return lcm

class HCFAndLCM(AbstractAnim):
    def construct(self):
        self.display_title()
        self.hcf_method(60, 48)
        self.wait(2)
        self.clear()
        self.lcm_method(60, 48)

    def display_title(self):
        title = Text("HCF and LCM", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

    def hcf_method(self, a, b):
        definition = Text("HCF (Highest Common Factor)", font_size=36)
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
        self.wait(3)

        self.play(FadeOut(explanation))

        prime_factors_a = prime_factors(a)
        prime_factors_b = prime_factors(b)
        hcf = find_hcf(a, b)

        factors_text = f"Prime factors of {a}: {prime_factors_a}\nPrime factors of {b}: {prime_factors_b}"
        common_factors_text = f"HCF: {hcf}"

        factors = Text(factors_text, font_size=24)
        factors.next_to(definition, DOWN, buff=0.5)
        self.play(Write(factors))
        self.wait(1)

        common_factors = Text(common_factors_text, font_size=24)
        common_factors.next_to(factors, DOWN, buff=0.5)
        self.play(Write(common_factors))
        self.wait(2)

    def lcm_method(self, a, b):
        definition = Text("LCM (Least Common Multiple)", font_size=36)
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
        self.wait(3)

        self.play(FadeOut(explanation))

        prime_factors_a = prime_factors(a)
        prime_factors_b = prime_factors(b)
        lcm = find_lcm(a, b)

        factors_text = f"Prime factors of {a}: {prime_factors_a}\nPrime factors of {b}: {prime_factors_b}"
        lcm_text = f"LCM: {lcm}"

        factors = Text(factors_text, font_size=24)
        factors.next_to(definition, DOWN, buff=0.5)
        self.play(Write(factors))
        self.wait(1)

        lcm_result = Text(lcm_text, font_size=24)
        lcm_result.next_to(factors, DOWN, buff=0.5)
        self.play(Write(lcm_result))
        self.wait(2)

if __name__ == "__main__":
    scene = HCFAndLCM()
    scene.render()