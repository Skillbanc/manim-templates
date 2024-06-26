from manim import *
from AbstractAnim import AbstractAnim
import cvo

class Realanim(AbstractAnim):
    def construct(self):
          self.RenderSkillbancLogo()
          self.fadeOutCurrentScene()
          self.EuclidsAlgorithm()
          self.fadeOutCurrentScene()
          self.Euclidsexample()
          self.fadeOutCurrentScene()
          self.FundamentalTheorem()
          self.fadeOutCurrentScene()
          self.Rationalnumbers()
          self.fadeOutCurrentScene()
          self.IrrationalNumbers()
          self.fadeOutCurrentScene()
          self.LawsOfExponents()
          self.fadeOutCurrentScene()
          self.GithubSourceCodeReference()


    def EuclidsAlgorithm(self):
        self.positionChoice=[[-4,0,0],[0,0,0],[4,0,0]]        
        self.isRandom = False

        # Create a CVO object for Euclid's algorithm
        p10 = cvo.CVO().CreateCVO("Method for finding the gcd","") 
        p11 = cvo.CVO().CreateCVO("Euclids algorithm","")
        p12 = cvo.CVO().CreateCVO("Properties", "")
        p12.extendOname(["$a > b$", "a / b = r (remainder)", "if $r = 0$ then divisor = gcd"])
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        self.construct1(p10, p10)

    def Euclidsexample(self):
        title = Text("Euclid's Algorithm").to_edge(UP)
        
        self.play(Write(title))

        explanation = Text("Finding GCD of 98 and 56 using Euclid's Algorithm", font_size=24).next_to(title, DOWN)
        self.play(Write(explanation))

        steps = [
            "a  = b  * q + r",
            "98 = 56 * 1 + 42(a should be written in the multiple of b )",
            "56 = 42 * 1 + 14",
            "42 = 14 * 3 + 0(continue the process till r=0)",
            "GCD is 14(b is the gcd of a,b)"
        ]

        step_mobs = VGroup(*[Text(step, font_size=24) for step in steps])
        step_mobs.arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.5)
        step_mobs.next_to(explanation, DOWN, buff=1)

        self.play(Write(step_mobs))
        self.wait(3)


    def FundamentalTheorem(self):
        self.positionChoice=[[-4,0,0],[0,0,0],[4,0,0]]        
        self.isRandom = False

        # Create a CVO object for Euclid's algorithm
        p10 = cvo.CVO().CreateCVO("Fundamental theorem","") 
        p11 = cvo.CVO().CreateCVO("Product of primes","")
        p12 = cvo.CVO().CreateCVO("Properties", "")
        p12.extendOname(["number should be natural number", "number $>1$","$Ex:15=5*3$"])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10, p10)
        self.fadeOutCurrentScene()


        title = Text("Fundamental Theorem of Arithmetic").to_edge(UP)
        self.play(Write(title))

        theorem = Text("Every integer greater than 1 can be written uniquely as a product of prime numbers.", font_size=24).next_to(title, DOWN)
        self.play(Write(theorem))

        example = Text("Example: 84 = 2 * 2 * 3 * 7", font_size=24).next_to(theorem, DOWN, buff=1)
        self.play(Write(example))

        self.wait(3)

    def Rationalnumbers(self):
        self.positionChoice=[[-4,0,0],[0,0,0],[4,0,0]]        
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Numbers","")
        p11 = cvo.CVO().CreateCVO("Rational numbers", "")
        p12 = cvo.CVO().CreateCVO("Properties", "")
        p12.extendOname(["Expressed in p/q form","$q\\neq0$","numerator =integer","denominator=integer","Is repeating"])
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        self.construct1(p10, p10)
        self.fadeOutCurrentScene()
        title = Text("Rational Numbers").to_edge(UP)
        description = Text("Any number that can be expressed in the form p/q where q ≠ 0", font_size=24).next_to(title, DOWN)

        self.play(Write(title), Write(description))
        number_line = NumberLine(
            x_range=[-0.5, 0.5, 0.1],  
            length=10, 
            color=BLUE,  
            include_numbers=True,  
            label_direction=UP,  
        )
        self.play(Create(number_line))

        rational_numbers = [
            (-0.5, r"-\frac{5}{10}"),
            (-0.4, r"-\frac{4}{10}"),
            (-0.3, r"-\frac{3}{10}"),
            (-0.2, r"-\frac{2}{10}"),
            (-0.1, r"-\frac{1}{10}"),            
            (0, r"\frac{0}{1}"),
            (0.1, r"\frac{1}{10}"),
            (0.2, r"\frac{2}{10}"),
            (0.3, r"\frac{3}{10}"),
            (0.4, r"\frac{4}{10}"),
            (0.5, r"\frac{5}{10}"),
        ]
        for num, label in rational_numbers:
            dot = Dot(point=number_line.number_to_point(num), color=RED)
            label_tex = MathTex(label, font_size=24).next_to(dot, DOWN)
            self.play(FadeIn(dot), Write(label_tex), run_time=0.5)

        self.wait(5)


    def IrrationalNumbers(self):
        self.positionChoice=[[-4,0,0],[0,0,0],[4,0,0]]        
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Numbers","")
        p11 = cvo.CVO().CreateCVO("Irrational", "")
        p12 = cvo.CVO().CreateCVO("Properties", "")
        p12.extendOname(["Cannot expressed in p/q form","$q\\neq0$","numerator =integer","denominator=integer","Is not repeating"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        self.construct1(p10, p10)
        self.fadeOutCurrentScene()

        title = Text("Irrational Numbers",font_size= 36).to_edge(UP)
        description = Text("Any number that cannot be expressed in the form p/q where q ≠ 0", font_size=24).next_to(title, DOWN)
        
        self.play(Write(title), Write(description))

        number_line = NumberLine(
            x_range=[-1, 4, 1],  
            length=10,  
            color=BLUE,  
            include_numbers=True,  
            label_direction=UP, 
        )
        self.play(Create(number_line))

        irrationals = [
            (np.sqrt(2), r"\sqrt{2}"),
            (np.pi, r"\pi"),
            (np.e, r"e"),
        ]

        for value, label in irrationals:
            dot = Dot(point=number_line.number_to_point(value), color=RED)
            label_tex = MathTex(label).next_to(dot, UP)
            self.play(FadeIn(dot), Write(label_tex), run_time=0.5)

        self.wait(3) 

    def LawsOfExponents(self):
        self.positionChoice=[[-4,0,0],[4,2,0],[2,2,0],[2,-2,0],[4,-2,0],[4,0,0]]        
        self.isRandom = False
        self.angleChoice = [TAU/4,TAU/4,TAU/4,TAU/4,TAU/4]


        p10 = cvo.CVO().CreateCVO("Laws of Exponents", "Properties")
        p11 = cvo.CVO().CreateCVO("Property", "$a^m \\cdot a^n = a^{m+n}$")
        p12 = cvo.CVO().CreateCVO("Property", "$(a^m)^n = a^{mn}$")
        p13 = cvo.CVO().CreateCVO("Property", "$a^0 = 1$")
        p14 = cvo.CVO().CreateCVO("Property", "$a^{-n} = \\frac{1}{a^n}$")
        p15 = cvo.CVO().CreateCVO("Property", "$\\frac{a^m}{a^n} = a^{m-n}$")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        self.construct1(p10, p10)
        self.fadeOutCurrentScene()

   
        title = Text("Exponentials").to_edge(UP)
        self.play(Write(title))

        examples = [
            r"a^m \cdot a^n = a^{m+n} \quad \text{example:} 2^3 \cdot 2^4 = 2^{3+4} = 2^7 = 128",
            r"\frac{a^m}{a^n} = a^{m-n} \quad \text{example:} \frac{2^5}{2^2} = 2^{5-2} = 2^3 = 8",
            r"(a^m)^n = a^{m \cdot n} \quad \text{example:} (2^3)^2 = 2^{3 \cdot 2} = 2^6 = 64",
            r"a^{-n} = \frac{1}{a^n} \quad \text{example:}2^{-3} = \frac{1}{2^3} = \frac{1}{8}",
            r"a^0 = 1 \quad \text{example:} 2^0 = 1",
        ]


        # Create and position each example individually
        example1 = MathTex(examples[0]).scale(0.8).next_to(title, DOWN, buff=1)
        example2 = MathTex(examples[1]).scale(0.8).next_to(example1, DOWN, aligned_edge=LEFT, buff=0.5)
        example3 = MathTex(examples[2]).scale(0.8).next_to(example2, DOWN, aligned_edge=LEFT, buff=0.5)
        example4 = MathTex(examples[3]).scale(0.8).next_to(example3, DOWN, aligned_edge=LEFT, buff=0.5)
        example5 = MathTex(examples[4]).scale(0.8).next_to(example4, DOWN, aligned_edge=LEFT, buff=0.5)


        self.play(Write(example1),Write(example2),Write(example3),Write(example4),Write(example5))
        
        self.wait(5)
     
    def SetDeveloperList(self):  
        self.DeveloperList="Shanmukha Priya"
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade10CH1RealNumbers.py"


if __name__ == "__main__":
    scene = Realanim()
    scene.render()
        