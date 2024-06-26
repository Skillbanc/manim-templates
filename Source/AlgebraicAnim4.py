# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla
# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla
import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

# Configure Manim to allow more cached files
config.max_files_cached = 550  # Change this number to your desired value

class AlgebraicAnim4(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.Types()
        self.fadeOutCurrentScene()
        self.monomial()
        self.fadeOutCurrentScene()
        self.binomial()
        self.fadeOutCurrentScene()
        self.trinomial()
        self.fadeOutCurrentScene()
        self.polynomial()
        self.fadeOutCurrentScene()
        self.Polynomials()
        self.fadeOutCurrentScene()
        self.linearpolynomial()
        self.fadeOutCurrentScene()
        self.quadraticpolynomial()
        self.fadeOutCurrentScene()
        self.cubicpolynomial()
        self.fadeOutCurrentScene()
        self.quarticpolynomial()
        self.fadeOutCurrentScene()
        self.quinticpolynomial()
        self.fadeOutCurrentScene()
        self.sexticpolynomial()
        self.fadeOutCurrentScene()
        self.Relations()
        self.fadeOutCurrentScene()
        self.identities()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        self.fadeOutCurrentScene()
    
    def RenderSkillbancLogo(self):
        
        self.orange = "#D76800"
        self.blue = "#3F64A7"
        self.green = "#96D24D"
        self.circles = VGroup(
            Circle(radius=1).rotate(PI/2).set_fill(self.orange, opacity=1).set_stroke(self.orange, opacity=1).shift(LEFT*3),
            Circle(radius=1).rotate(PI/2).set_fill(self.blue, opacity=1).set_stroke(self.blue, opacity=1),
            Circle(radius=1).rotate(PI/2).set_fill(self.green, opacity=1).set_stroke(self.green, opacity=1).shift(RIGHT*3)
        )
        circle1, circle2, circle3 = self.circles
        
        lines = VGroup(
            Arrow(circle1.get_right(), circle2.get_left(), max_tip_length_to_length_ratio=2),
            Arrow(circle2.get_right(), circle3.get_left(), max_tip_length_to_length_ratio=2),
            CurvedArrow(circle1.get_top(), circle3.get_top(), angle=-TAU/4),
            CurvedArrow(circle1.get_bottom(), circle3.get_bottom(), angle=TAU/4)
        )

        # Adjust the starting points of the straight arrows to touch the circumference
        lines[0].put_start_and_end_on(circle1.get_right(), circle2.get_left())
        lines[1].put_start_and_end_on(circle2.get_right(), circle3.get_left())

        # Add the text "skillbanc" below the curved arrows
        self.play(Create(circle1), Create(circle2), Create(circle3), rate_func=smooth, run_time=1)
        self.play(Create(lines), rate_func=smooth, run_time=1)
        text = Text("Skillbanc.com, Inc.").next_to(lines[3], DOWN)
        self.play(Create(text), rate_func=smooth, run_time=0.75)
        
        self.logoGroup = VGroup().add(self.circles).add(lines).add(text)
        self.play(self.logoGroup.animate.scale(0),run_time=1)
        # self.play(self.circles.animate.scale(0),lines.animate.scale(0),text.animate.scale(0),run_time=3)

    def Introduction(self):
        self.setNumberOfCirclePositions(3)
        self.isRandom = False
        p10 = cvo.CVO().CreateCVO("algebraic expression", "ax+by+c=0")
        p12 = cvo.CVO().CreateCVO("like terms", "having same variables(eg..,3x,3y)")
        p13 = cvo.CVO().CreateCVO("unlike term", "having different variables(eg..,3xy,7yz")

        p10.cvolist.append(p12)
        p10.cvolist.append(p13)

        self.construct1(p10, p10)

    def Types(self):
        self.setNumberOfCirclePositions(5)
        p10 = cvo.CVO().CreateCVO("algebraic expression", "types").setPosition([0, 2.5, 0])
        p11 = cvo.CVO().CreateCVO("monomial", "An algebraic expression with a single term").setPosition([4, 2, 0])
        p12 = cvo.CVO().CreateCVO("binomial", "An algebraic expression with two terms").setPosition([5, -2, 0])
        p13 = cvo.CVO().CreateCVO("trinomial", "An algebraic expression with three terms").setPosition([-4, 2, 0])
        p14 = cvo.CVO().CreateCVO("polynomial", "An algebraic expression with one or more terms").setPosition([-4, -2, 0])

        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)

        self.construct1(p10, p10)

    def monomial(self):
        self.setNumberOfCirclePositions(3)
        self.isRandom = False
        p11 = cvo.CVO().CreateCVO("monomial", "").setPosition([0, 2.5, 0])
        p11.SetIsMathText(True)
        p11_def = cvo.CVO().CreateCVO("definition", "An algebraic expression with a single term.")
        p11_example = cvo.CVO().CreateCVO("example", "Examples: 2x, 3y, 4z^2")
        p11_example.SetIsMathText(True)
        p11.cvolist.append(p11_def)
        p11.cvolist.append(p11_example)

        self.construct1(p11, p11)

    def binomial(self):
        self.setNumberOfCirclePositions(3)
        self.isRandom = False
        p11 = cvo.CVO().CreateCVO("binomial", "").setPosition([0, 2.5, 0])
        p11.SetIsMathText(True)
        p11_def = cvo.CVO().CreateCVO("definition", "An algebraic expression with two terms.")
        p11_example = cvo.CVO().CreateCVO("example", "Examples: 3x + 2, 4x^2 - 9")
        p11_example.SetIsMathText(True)
        p11.cvolist.append(p11_def)
        p11.cvolist.append(p11_example)

        self.construct1(p11, p11)

    def trinomial(self):
        self.setNumberOfCirclePositions(3)
        self.isRandom = False
        p11 = cvo.CVO().CreateCVO("trinomial", "").setPosition([0, 2.5, 0])
        p11.SetIsMathText(True)
        p11_def = cvo.CVO().CreateCVO("definition", "An algebraic expression with three terms.")
        p11_example = cvo.CVO().CreateCVO("example", "Examples: x^2 + 3x + 2, 2a^3 - 3a + 5")
        p11_example.SetIsMathText(True)
        p11.cvolist.append(p11_def)
        p11.cvolist.append(p11_example)

        self.construct1(p11, p11)

    def polynomial(self):
        self.setNumberOfCirclePositions(3)
        self.isRandom = False
        p11 = cvo.CVO().CreateCVO("polynomial", "").setPosition([0, 2.5, 0])
        p11.SetIsMathText(True)
        p11_def = cvo.CVO().CreateCVO("definition", "An algebraic expression with one or more terms.")
        p11_example = cvo.CVO().CreateCVO("example", "Examples: 4x^3 + 3x^2 - x + 7, x^4 - 2x^3 + x - 1")
        p11_example.SetIsMathText(True)
        p11.cvolist.append(p11_def)
        p11.cvolist.append(p11_example)

        self.construct1(p11, p11)

    def Polynomials(self):
        self.setNumberOfCirclePositions(7)
        p10 = cvo.CVO().CreateCVO("polynomials", "types").setPosition([0, 2.5, 0])
        p11 = cvo.CVO().CreateCVO("Linear Polynomial", "Degree 1 ").setPosition([4, 2, 0])
        p12 = cvo.CVO().CreateCVO("Quadratic Polynomial", "Degree 2 ").setPosition([5, -2, 0])
        p13 = cvo.CVO().CreateCVO("Cubic Polynomial", "Degree 3 ").setPosition([-4, 2, 0])
        p14 = cvo.CVO().CreateCVO("Quartic Polynomial", "Degree 4 ").setPosition([-4, -2, 0])
        p15 = cvo.CVO().CreateCVO("Quintic Polynomial", "Degree 5 ").setPosition([0, -2.5, 0])
        p16 = cvo.CVO().CreateCVO("Sextic Polynomial", "Degree 6 ").setPosition([0, -4.5, 0])

        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        p10.cvolist.append(p16)

        self.construct1(p10, p10)

    def linearpolynomial(self):
        self.setNumberOfCirclePositions(3)
        self.isRandom = False
        p11 = cvo.CVO().CreateCVO("Linear Polynomial", "Degree 1").setPosition([0, 2.5, 0])
        p11.SetIsMathText(True)
        p11_def = cvo.CVO().CreateCVO("definition", "A polynomial of degree 1.")
        p11_example = cvo.CVO().CreateCVO("example", "Examples: x + 1, 3x + 2")
        p11_example.SetIsMathText(True)
        p11.cvolist.append(p11_def)
        p11.cvolist.append(p11_example)

        self.construct1(p11, p11)

    def quadraticpolynomial(self):
        self.setNumberOfCirclePositions(3)
        self.isRandom = False
        p11 = cvo.CVO().CreateCVO("Quadratic Polynomial", "Degree 2").setPosition([0, 2.5, 0])
        p11.SetIsMathText(True)
        p11_def = cvo.CVO().CreateCVO("definition", "A polynomial of degree 2.")
        p11_example = cvo.CVO().CreateCVO("example", "Examples: x^2 + 2x + 1, 4x^2 - 3x + 2")
        p11_example.SetIsMathText(True)
        p11.cvolist.append(p11_def)
        p11.cvolist.append(p11_example)

        self.construct1(p11, p11)

    def cubicpolynomial(self):
        self.setNumberOfCirclePositions(3)
        self.isRandom = False
        p11 = cvo.CVO().CreateCVO("Cubic Polynomial", "Degree 3").setPosition([0, 2.5, 0])
        p11.SetIsMathText(True)
        p11_def = cvo.CVO().CreateCVO("definition", "A polynomial of degree 3.")
        p11_example = cvo.CVO().CreateCVO("example", "Examples: x^3 + 3x^2 + 3x + 1, 2x^3 - x^2 + 3x - 5")
        p11_example.SetIsMathText(True)
        p11.cvolist.append(p11_def)
        p11.cvolist.append(p11_example)

        self.construct1(p11, p11)

    def quarticpolynomial(self):
        self.setNumberOfCirclePositions(3)
        self.isRandom = False
        p11 = cvo.CVO().CreateCVO("Quartic Polynomial", "Degree 4 ").setPosition([0, 2.5, 0])
        p11.SetIsMathText(True)
        p11_def = cvo.CVO().CreateCVO("definition", "A polynomial of degree 4.")
        p11_example = cvo.CVO().CreateCVO("example", "Examples: x^4 + 4x^3 + 6x^2 + 4x + 1, 5x^4 - 2x^3 + x^2 - 7")
        p11_example.SetIsMathText(True)
        p11.cvolist.append(p11_def)
        p11.cvolist.append(p11_example)

        self.construct1(p11, p11)

    def quinticpolynomial(self):
        self.setNumberOfCirclePositions(3)
        self.isRandom = False
        p11 = cvo.CVO().CreateCVO("Quintic Polynomial", "Degree 5").setPosition([0, 2.5, 0])
        p11.SetIsMathText(True)
        p11_def = cvo.CVO().CreateCVO("definition", "A polynomial of degree 5.")
        p11_example = cvo.CVO().CreateCVO("example", "Examples: x^5 + 5x^4 + 10x^3 + 10x^2 + 5x + 1, 3x^5 - 2x^3 + x - 4")
        p11_example.SetIsMathText(True)
        p11.cvolist.append(p11_def)
        p11.cvolist.append(p11_example)

        self.construct1(p11, p11)

    def sexticpolynomial(self):
        self.setNumberOfCirclePositions(3)
        self.isRandom = False
        p11 = cvo.CVO().CreateCVO("Sextic Polynomial", "Degree 6").setPosition([0, 2.5, 0])
        p11.SetIsMathText(True)
        p11_def = cvo.CVO().CreateCVO("definition", "A polynomial of degree 6.")
        p11_example = cvo.CVO().CreateCVO("example", "Examples: x^6 + 6x^5 + 15x^4 + 20x^3 + 15x^2 + 6x + 1, 2x^6 - 3x^4 + x^2 - 1")
        p11_example.SetIsMathText(True)
        p11.cvolist.append(p11_def)
        p11.cvolist.append(p11_example)

        self.construct1(p11, p11)

    def Relations(self):
        self.setNumberOfCirclePositions(4)
        p10 = cvo.CVO().CreateCVO("relations", "types").setPosition([0, 2.5, 0])
        p11 = cvo.CVO().CreateCVO("addition", "Combining like terms(eg..,(3a^2 + 2a^2) = 5a^2)").setPosition([4, 2, 0])
        p12 = cvo.CVO().CreateCVO("substraction", "Finding the difference between like terms(ex,,.(2x^2 + 3x) - (x^2 + 2x) = x^2 + x)").setPosition([5, -2, 0])
        p13 = cvo.CVO().CreateCVO("multiplication", "Distributing terms and combining like terms(eg..,(x + 2)(x + 3) = x^2 + 5x + 6)").setPosition([-4, 2, 0])

        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)

        self.construct1(p10, p10)

    def identities(self):
        self.setNumberOfCirclePositions(5)
        self.isRandom = False
        p10 = cvo.CVO().CreateCVO("identities", "").setPosition([0, 2.5, 0])
        p11 = cvo.CVO().CreateCVO("(a+b)^2", "a^2+b^2+2ab")
        p11.SetIsMathText(True)
        p12 = cvo.CVO().CreateCVO("(a-b)^2", "a^2+b^2-2ab")
        p12.SetIsMathText(True)
        p13 = cvo.CVO().CreateCVO("(a+b)(a-b)", "a^2-b^2")
        p13.SetIsMathText(True)
        p14 = cvo.CVO().CreateCVO("(x+a)(x+b)", "x^2+(a+b)x+ab")
        p14.SetIsMathText(True)
        
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        
        self.construct1(p10, p10)


        
        
if __name__ == "__main__":
    scene = AlgebraicAnim4()
    scene.render()
