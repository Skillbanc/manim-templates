from manim import *
from AbstractAnim import AbstractAnim

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

def continued_division_hcf(a, b):
    """Return the HCF of a and b using the continued division method"""
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    """Return the LCM of a and b using the prime factorization method"""
    factors_a = prime_factors(a)
    factors_b = prime_factors(b)
    all_factors = set(factors_a).union(set(factors_b))
    lcm = 1
    for factor in all_factors:
        lcm *= max(factors_a.count(factor), factors_b.count(factor)) * factor
    return lcm

def division_method_lcm(a, b):
    """Return the LCM of a and b using the division method"""
    original_a, original_b = a, b
    gcd = continued_division_hcf(a, b)
    lcm = (original_a * original_b) // gcd
    return lcm

class HCFAndLCM(AbstractAnim):
    def construct(self):
        self.display_title()
        self.hcf_prime_method(60, 48)
        self.wait(0.1)
        self.clear()
        self.hcf_continued_division_method(60, 48)
        self.wait(2)
        self.clear()
        self.lcm_prime_method(60, 48)
        self.wait(2)
        self.clear()
        self.lcm_division_method(36, 60)
        self.wait(2)

    def display_title(self):
        title = Text("HCF and LCM", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.1)

    def hcf_prime_method(self, a, b):
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
        self.wait(3)

        prime_factors_a = prime_factors(a)
        prime_factors_b = prime_factors(b)
        hcf = find_hcf(a, b)

        factors_text = f"Prime factors of {a}: {prime_factors_a}\nPrime factors of {b}: {prime_factors_b}"
        common_factors_text = f"HCF: {hcf}"

        factors = Text(factors_text, font_size=24)
        factors.next_to(explanation, DOWN, buff=0.5)
        self.play(Write(factors))
        self.wait(1)

        common_factors = Text(common_factors_text, font_size=24)
        common_factors.next_to(factors, DOWN, buff=0.5)
        self.play(Write(common_factors))
        self.wait(2)

    def hcf_continued_division_method(self, a, b):
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

        explanation = VGroup(*[Text(step, font_size=24) for step in steps])
        explanation.arrange(DOWN, aligned_edge=LEFT)
        explanation.next_to(definition, DOWN, buff=0.5)

        self.play(Write(explanation))
        self.wait(3)

        hcf = continued_division_hcf(a, b)
        hcf_text = f"HCF: {hcf}"

        result = Text(hcf_text, font_size=24)
        result.next_to(explanation, DOWN, buff=0.5)
        self.play(Write(result))
        self.wait(2)

    def lcm_prime_method(self, a, b):
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
        self.wait(3)

        prime_factors_a = prime_factors(a)
        prime_factors_b = prime_factors(b)
        lcm = find_lcm(a, b)

        factors_text = f"Prime factors of {a}: {prime_factors_a}\nPrime factors of {b}: {prime_factors_b}"
        lcm_text = f"LCM: {lcm}"

        factors = Text(factors_text, font_size=24)
        factors.next_to(explanation, DOWN, buff=0.5)
        self.play(Write(factors))
        self.wait(1)

        lcm_result = Text(lcm_text, font_size=24)
        lcm_result.next_to(factors, DOWN, buff=0.5)
        self.play(Write(lcm_result))
        self.wait(2)

    def lcm_division_method(self, a, b):
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
        self.wait(3)

        example_text = [
            "Example: Find the LCM of 36 and 60",
            "Step 1: Write the numbers in a horizontal line: 36, 60",
            "Step 2: Divide by the smallest prime (2): 18, 30",
            "Step 3: Continue dividing by common primes:",
            "2: 9, 15",
            "3: 3, 5",
            "Step 4: Multiply all prime factors: 2 * 2 * 3 * 3 * 5",
            "LCM: 180"
        ]

        explanation_example = VGroup(*[Text(line, font_size=24) for line in example_text])
        explanation_example.arrange(DOWN, aligned_edge=LEFT)
        explanation_example.next_to(explanation, DOWN, buff=0.5)

        self.play(Write(explanation_example))
        self.wait(5)

if __name__ == "__main__":
    scene = HCFAndLCM()
    scene.render()