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
config.max_files_cached = 600  # Change this number to your desired value

class AlgebraicExpression(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.heading()
        self.fadeOutCurrentScene()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.intro()
        self.fadeOutCurrentScene()
        self.Types()
        self.fadeOutCurrentScene()
        self.Polynomials()
        self.fadeOutCurrentScene()
        self.Relations()
        self.fadeOutCurrentScene()
        self.AdditionOfAlgebraicExpressions()
        self.SubtractionOfAlgebraicExpressions()
        self.MultiplyingMonomials()
        self.MultiplyingBinomialByMonomial()
        self.MultiplyingTrinomialByMonomial()
        self.MultiplyingBinomialByBinomial()
        self.MultiplyingBinomialByTrinomial()
        self.MultiplyingTrinomialByTrinomial()
        self.identities()
        self.fadeOutCurrentScene()
        self.ApplicationOfIdentities()
        self.fadeOutCurrentScene()
        self.finding1962()
        self.fadeOutCurrentScene()
        self.application2()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        
    def SetDeveloperList(self):
       self.DeveloperList="Vasudha"
       
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade8CH11AlgebraicExpressions.py"
    
    def heading(self):
        title = Text("              CHAPTER 11\n\nALGEBRAIC EXPRESSIONS", font_size=48, color=PURPLE)
        
        # Animate the title text
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.to_edge(UP))
    
    def Introduction(self):
        self.setNumberOfCirclePositions(3)
        self.isRandom = False
        p10 = cvo.CVO().CreateCVO("Algebraic Expression", "ax+by+c=0")
        p12 = cvo.CVO().CreateCVO("like terms", "")
        p13 = cvo.CVO().CreateCVO("unlike term", "")

        p10.cvolist.append(p12)
        p10.cvolist.append(p13)

        self.construct1(p10, p10)
        
    def intro(self):
        
        heading = Text("Differentiating like terms and unlike terms",font_size=28,color=PURPLE)
        heading.to_edge(ORIGIN + UP*3) 
        self.play(Write(heading))
        self.wait(2)
        # Define the terms
        terms = [
            MathTex(r"ax^2y"),
            MathTex(r"2x"),
            MathTex(r"5y^2"),
            MathTex(r"-9x^2"),
            MathTex(r"-6x"),
            MathTex(r"7xy"),
            MathTex(r"18y^2")
        ]

        # Scale down the terms
        for term in terms:
            term.scale(0.8)

        # Position the terms at the center horizontally
        terms_group = VGroup(*terms).arrange(RIGHT, buff=1)  # Arrange terms with equal spacing

        # Center the group of terms on the screen
        terms_group.move_to(ORIGIN + UP*1)

        # Display the terms
        self.play(FadeIn(terms_group))
        self.wait(2)

        # Highlight like terms
        like_terms = [terms[2], terms[6]]
        self.play(*[Transform(term, term.copy().set_color(YELLOW)) for term in like_terms])
        self.wait(1)

        # Create boxes around like terms
        like_boxes = VGroup(*[SurroundingRectangle(term, color=YELLOW, buff=0.2) for term in like_terms])
        self.play(Create(like_boxes))
        self.wait(1)
        
        self.play(FadeOut(like_boxes))

        # Fade out and move like terms to one side, then fade in
        like_target_positions = [DOWN * 0.5 + LEFT * 2.5, DOWN * 0.5 + LEFT * 1.5]
        self.play(*[FadeOut(term) for term in like_terms])
        for term, pos in zip(like_terms, like_target_positions):
            term.move_to(pos)
        self.play(*[FadeIn(term) for term in like_terms])

        # Fade out and move unlike terms to the other side, then fade in
        unlike_terms = [terms[0], terms[1], terms[3], terms[4], terms[5]]
        unlike_target_positions = [
            DOWN * 0.5 + RIGHT * 1,
            DOWN * 0.5 + RIGHT * 2,
            DOWN * 0.5 + RIGHT * 3,
            DOWN * 0.5 + RIGHT * 4,
            DOWN * 0.5 + RIGHT * 5
        ]
        self.play(*[FadeOut(term) for term in unlike_terms])
        for term, pos in zip(unlike_terms, unlike_target_positions):
            term.move_to(pos)
        self.play(*[FadeIn(term) for term in unlike_terms])
        self.wait(2)

        # Label the groups
        like_label = Text("Like Terms", color=YELLOW).scale(0.8).next_to(VGroup(*like_terms), UP)
        unlike_label = Text("Unlike Terms", color=WHITE).scale(0.8).next_to(VGroup(*unlike_terms), UP)
        self.play(FadeIn(like_label), FadeIn(unlike_label))
        self.wait(2)

    def Types(self):
        self.setNumberOfCirclePositions(5)
        self.isRandom = False
        self.angleChoice = [TAU/4,TAU/4,TAU/4,TAU/4]
        p10 = cvo.CVO().CreateCVO("Algebraic Expression", "").setPosition([-3.5, 0, 0])
        p11 = cvo.CVO().CreateCVO("monomial", "2x, 4z^2").setPosition([2, 2.5, 0])
        p11.SetIsMathText(True)
        p12 = cvo.CVO().CreateCVO("binomial", "3x + 2").setPosition([3.5, 1.5, 0])
        p12.SetIsMathText(True)
        p13 = cvo.CVO().CreateCVO("trinomial", "x^2 + 3x + 2").setPosition([3.5, -1, 0])
        p13.SetIsMathText(True)
        p14 = cvo.CVO().CreateCVO("polynomial", "4x^3 + 3x^2 - x + 7").setPosition([1.7, -2.5, 0])
        p14.SetIsMathText(True)

        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)

        self.construct1(p10, p10)
        
    def Polynomials(self):
        self.setNumberOfCirclePositions(7)
        self.isRandom = False
        self.angleChoice = [TAU/4,TAU/4,TAU/4,TAU/4,-TAU/2,TAU/2]
        p10 = cvo.CVO().CreateCVO("polynomials", "").setPosition([-3.5, 0, 0])
        p11 = cvo.CVO().CreateCVO("Linear Polynomial", "A polynomial of degree 1 ").setPosition([2, 2.5, 0])
        p12 = cvo.CVO().CreateCVO("Quadratic Polynomial", "A polynomial of degree 2 ").setPosition([4.7, 1.5, 0])
        p13 = cvo.CVO().CreateCVO("Cubic Polynomial", "A polynomial of degree 3 ").setPosition([4.7, -0.8, 0])
        p14 = cvo.CVO().CreateCVO("Quartic Polynomial", "A polynomial of degree 4").setPosition([2, -2.5, 0])
        p15 = cvo.CVO().CreateCVO("Quintic Polynomial", "A polynomial of degree 5").setPosition([-3.5, 2.5, 0])
        p16 = cvo.CVO().CreateCVO("Sextic Polynomial", "A polynomial of degree 6 ").setPosition([-3.5, -2.5, 0])

        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        p10.cvolist.append(p16)

        self.construct1(p10, p10)
        

    def Relations(self):
        self.setNumberOfCirclePositions(4)
        p10 = cvo.CVO().CreateCVO("operations", "").setPosition([0, 2.5, 0])
        p11 = cvo.CVO().CreateCVO("addition", "").setPosition([4, 2, 0])
        p11.SetIsMathText(True)
        p12 = cvo.CVO().CreateCVO("subtraction", "").setPosition([2, -2.5, 0])
        p12.SetIsMathText(True)
        p13 = cvo.CVO().CreateCVO("multiplication", "").setPosition([-3, -1, 0])
        p13.SetIsMathText(True)

        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)

        self.construct1(p10, p10)
        
    def AdditionOfAlgebraicExpressions(self):
        # Title
        title = Text("Addition of Algebraic Expressions",color=PINK)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Expressions
        expr1 = MathTex("eq(1):3x + 2y",color=YELLOW)
        expr2 = MathTex("eq(2):5x - 3y",color=YELLOW)
        add_expr_step1 = MathTex("eq(1) + eq(2)")
        add_expr_step2 = MathTex("(3x + 2y) + (5x - 3y)")
        add_expr_step3 = MathTex("= (3x + 5x) + (2y - 3y)")
        add_expr_step4 = MathTex("= 8x - y")

        # Positioning
        expr1.shift(UP*2 + 3*LEFT)
        expr2.shift(UP*2 + 3*RIGHT)
        add_expr_step1.next_to(expr1, DOWN, buff=1).shift(1.5*RIGHT)
        add_expr_step2.next_to(add_expr_step1, DOWN, buff=0.5)
        add_expr_step3.next_to(add_expr_step2, DOWN, buff=0.5)
        add_expr_step4.next_to(add_expr_step3, DOWN, buff=0.5)

        # Writing expressions
        self.play(Write(expr1))
        self.play(Write(expr2))
        self.wait(1)

        # Showing addition step by step
        self.play(Write(add_expr_step1))
        self.wait(1)
        self.play(Write(add_expr_step2))
        self.wait(1)
        self.play(Write(add_expr_step3))
        self.wait(1)
        self.play(Write(add_expr_step4))
        self.wait(1)
        
        # Clean up
        self.play(FadeOut(expr1), FadeOut(expr2), FadeOut(add_expr_step1), FadeOut(add_expr_step2), FadeOut(add_expr_step3), FadeOut(add_expr_step4), FadeOut(title))
        self.wait(1)

    def SubtractionOfAlgebraicExpressions(self):
         # Title
        title = Text("Subtraction of Algebraic Expressions",color=PINK)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Expressions
        expr1 = MathTex("eq(1):3x + 2y",color=YELLOW)
        expr2 = MathTex("eq(2):5x - 3y",color=YELLOW)
        add_expr_step1 = MathTex("eq(1) - eq(2)")
        add_expr_step2 = MathTex("(3x + 2y) - (5x - 3y)")
        add_expr_step3 = MathTex("= (3x - 5x) + (2y + 3y)")
        add_expr_step4 = MathTex("= -2x + 5y")

        # Positioning
        expr1.shift(UP*2 + 3*LEFT)
        expr2.shift(UP*2 + 3*RIGHT)
        add_expr_step1.next_to(expr1, DOWN, buff=1).shift(1.5*RIGHT)
        add_expr_step2.next_to(add_expr_step1, DOWN, buff=0.5)
        add_expr_step3.next_to(add_expr_step2, DOWN, buff=0.5)
        add_expr_step4.next_to(add_expr_step3, DOWN, buff=0.5)

        # Writing expressions
        self.play(Write(expr1))
        self.play(Write(expr2))
        self.wait(1)

        # Showing addition step by step
        self.play(Write(add_expr_step1))
        self.wait(1)
        self.play(Write(add_expr_step2))
        self.wait(1)
        self.play(Write(add_expr_step3))
        self.wait(1)
        self.play(Write(add_expr_step4))
        self.wait(1)
        
        # Clean up
        self.play(FadeOut(expr1), FadeOut(expr2), FadeOut(add_expr_step1), FadeOut(add_expr_step2), FadeOut(add_expr_step3), FadeOut(add_expr_step4), FadeOut(title))
        self.wait(1)
        
    def MultiplyingMonomials(self):
         # Title
        title = Text("Multiplying Monomials",color=PINK)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Expressions
        expr1 = MathTex("eq(1):2x^2",color=YELLOW)
        expr2 = MathTex("eq(2):3x^3",color=YELLOW)
        mul_expr_step1 = MathTex("eq(1) * eq(2)")
        mul_expr_step2 = MathTex("2x^2 \\cdot 3x^3 = 2 \\cdot 3 \\cdot x^2 \\cdot x^3")
        mul_expr_step3 = MathTex("= 6 \\cdot x^{2+3}")
        mul_expr_step4 = MathTex("= 6x^5")

        # Positioning
        expr1.shift(UP*2 + 3*LEFT)
        expr2.shift(UP*2 + 3*RIGHT)
        mul_expr_step1.next_to(expr1, DOWN, buff=1).shift(1.5*RIGHT)
        mul_expr_step2.next_to(mul_expr_step1, DOWN, buff=0.5)
        mul_expr_step3.next_to(mul_expr_step2, DOWN, buff=0.5)
        mul_expr_step4.next_to(mul_expr_step3, DOWN, buff=0.5)

        # Writing expressions
        self.play(Write(expr1))
        self.play(Write(expr2))
        self.wait(1)

        # Showing addition step by step
        self.play(Write(mul_expr_step1))
        self.wait(1)
        self.play(Write(mul_expr_step2))
        self.wait(1)
        self.play(Write(mul_expr_step3))
        self.wait(1)
        self.play(Write(mul_expr_step4))
        self.wait(1)
        
        # Clean up
        self.play(FadeOut(expr1), FadeOut(expr2), FadeOut(mul_expr_step1), FadeOut(mul_expr_step2), FadeOut(mul_expr_step3), FadeOut(mul_expr_step4), FadeOut(title))
        self.wait(1)
        
    def MultiplyingBinomialByMonomial(self):
        # Title
        title = Text("Multiplying a Binomial and a Monomial",color=PINK)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Expressions
        binomial = MathTex("binomial:2x + 3",color=YELLOW)
        monomial = MathTex("monomial:4x",color=YELLOW)
        multiply_expr_step1 = MathTex("binomial * monomial")
        multiply_expr_step2 = MathTex("4x(2x + 3)")
        multiply_expr_step3 = MathTex("= 4x \\cdot 2x + 4x \\cdot 3")
        multiply_expr_step4 = MathTex("= 8x^2 + 12x")

        # Positioning
        binomial.shift(UP*2 + 3*LEFT)
        monomial.shift(UP*2 + 3*RIGHT)
        multiply_expr_step1.next_to(binomial, DOWN, buff=1).shift(1.5*RIGHT)
        multiply_expr_step2.next_to(multiply_expr_step1, DOWN, buff=0.5)
        multiply_expr_step3.next_to(multiply_expr_step2, DOWN, buff=0.5)
        multiply_expr_step4.next_to(multiply_expr_step3, DOWN, buff=0.5)
    
        # Writing expressions
        self.play(Write(binomial))
        self.play(Write(monomial))
        self.wait(1)

        # Showing multiplication step by step
        self.play(Write(multiply_expr_step1))
        self.wait(1)
        self.play(Write(multiply_expr_step2))
        self.wait(1)
        self.play(Write(multiply_expr_step3))
        self.wait(1)
        self.play(Write(multiply_expr_step4))
        self.wait(1)

        # Clean up
        self.play(FadeOut(binomial), FadeOut(monomial), FadeOut(multiply_expr_step1), FadeOut(multiply_expr_step2), FadeOut(multiply_expr_step3), FadeOut(multiply_expr_step4), FadeOut(title))
        self.wait(1)

    def MultiplyingTrinomialByMonomial(self):
        # Title
        title = Text("Multiplying a Trinomial and a Monomial",color=PINK)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Expressions
        trinomial = MathTex("trinomial:x^2 + 2x + 3",color=YELLOW)
        monomial = MathTex("monomial:4x",color=YELLOW)
        multiply_expr_step1 = MathTex("trinomial * monomial")
        multiply_expr_step2 = MathTex("4x(x^2 + 2x + 3)")
        multiply_expr_step3 = MathTex("= 4x \\cdot x^2 + 4x \\cdot 2x + 4x \\cdot 3")
        multiply_expr_step4 = MathTex("= 4x^3 + 8x^2 + 12x")

        # Positioning
        trinomial.shift(UP*2 + 3*LEFT)
        monomial.shift(UP*2 + 3*RIGHT)
        multiply_expr_step1.next_to(trinomial, DOWN, buff=1).shift(1.5*RIGHT)
        multiply_expr_step2.next_to(multiply_expr_step1, DOWN, buff=0.5)
        multiply_expr_step3.next_to(multiply_expr_step2, DOWN, buff=0.5)
        multiply_expr_step4.next_to(multiply_expr_step3, DOWN, buff=0.5)

        # Writing expressions
        self.play(Write(trinomial))
        self.play(Write(monomial))
        self.wait(1)

        # Showing multiplication step by step
        self.play(Write(multiply_expr_step1))
        self.wait(1)
        self.play(Write(multiply_expr_step2))
        self.wait(1)
        self.play(Write(multiply_expr_step3))
        self.wait(1)
        self.play(Write(multiply_expr_step4))
        self.wait(1)

        # Clean up
        self.play(FadeOut(trinomial), FadeOut(monomial), FadeOut(multiply_expr_step1), FadeOut(multiply_expr_step2),FadeOut(multiply_expr_step3),FadeOut(multiply_expr_step4), FadeOut(title))
        self.wait(1)

    def MultiplyingBinomialByBinomial(self):
        # Title
        title = Text("Multiplying a Binomials",color=PINK)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Expressions
        binomial1 = MathTex("eq(1):a + b",color=YELLOW)
        binomial2 = MathTex("eq(2):c + d",color=YELLOW)
        multiply_expr_step1 = MathTex("eq(1) * eq(2)")
        multiply_expr_step2 = MathTex("(a + b)(c + d)")
        multiply_expr_step3 = MathTex("= a(c + d) + b(c + d) ")
        multiply_expr_step4 = MathTex("= ac + ad + bc + bd")
        # Positioning
        binomial1.shift(UP*2 + 3*LEFT)
        binomial2.shift(UP*2 + 3*RIGHT)
        multiply_expr_step1.next_to(binomial1, DOWN, buff=1).shift(1.5*RIGHT)
        multiply_expr_step2.next_to(multiply_expr_step1, DOWN, buff=0.5)
        multiply_expr_step3.next_to(multiply_expr_step2, DOWN, buff=0.5)
        multiply_expr_step4.next_to(multiply_expr_step3, DOWN, buff=0.5)
    
        # Writing expressions
        self.play(Write(binomial1))
        self.play(Write(binomial2))
        self.wait(1)

        # Showing multiplication step by step
        self.play(Write(multiply_expr_step1))
        self.wait(1)
        self.play(Write(multiply_expr_step2))
        self.wait(1)
        self.play(Write(multiply_expr_step3))
        self.wait(1)
        self.play(Write(multiply_expr_step4))
        self.wait(1)

        # Clean up
        self.play(FadeOut(binomial1), FadeOut(binomial2), FadeOut(multiply_expr_step1), FadeOut(multiply_expr_step2), FadeOut(multiply_expr_step3), FadeOut(multiply_expr_step4), FadeOut(title))
        self.wait(1)

    def MultiplyingBinomialByTrinomial(self):
        # Title
        title = Text("Multiplying a Binomial and a Trinomial",color=PINK)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Expressions
        binomial = MathTex("binomial:a + b",color=YELLOW)
        trinomial = MathTex("trinomial:c + d + e",color=YELLOW)
        multiply_expr_step1 = MathTex("binomial * trinomial")
        multiply_expr_step2 = MathTex("(a + b)(c + d + e)")
        multiply_expr_step3 = MathTex("= a(c + d + e) + b(c + d + e)")
        multiply_expr_step4 = MathTex("= ac + ad + ae + bc + bd + be")
       
        # Positioning
        binomial.shift(UP*2 + 3*LEFT)
        trinomial.shift(UP*2 + 3*RIGHT)
        multiply_expr_step1.next_to(binomial, DOWN, buff=1).shift(1.5*RIGHT)
        multiply_expr_step2.next_to(multiply_expr_step1, DOWN, buff=0.5)
        multiply_expr_step3.next_to(multiply_expr_step2, DOWN, buff=0.5)
        multiply_expr_step4.next_to(multiply_expr_step3, DOWN, buff=0.5)

        # Writing expressions
        self.play(Write(binomial))
        self.play(Write(trinomial))
        self.wait(1)

        # Showing multiplication step by step
        self.play(Write(multiply_expr_step1))
        self.wait(1)
        self.play(Write(multiply_expr_step2))
        self.wait(1)
        self.play(Write(multiply_expr_step3))
        self.wait(1)
        self.play(Write(multiply_expr_step4))
        self.wait(1)

        # Clean up
        self.play(FadeOut(binomial), FadeOut(trinomial), FadeOut(multiply_expr_step1), FadeOut(multiply_expr_step2), FadeOut(multiply_expr_step3), FadeOut(multiply_expr_step4), FadeOut(title))
        self.wait(1)
        
    def MultiplyingTrinomialByTrinomial(self):
        # Title
        title = Text("Multiplying Trinomials",color=PINK)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Expressions
        binomial = MathTex("eq(1):a + b + c",color=YELLOW)
        trinomial = MathTex("eq(2):d + e + f",color=YELLOW)
        multiply_expr_step1 = MathTex("eq(1) * eq(2)")
        multiply_expr_step2 = MathTex("(a + b + c)(d + e + f)")
        multiply_expr_step3 = MathTex("= a(d + e + f) + b(d + e + f) + C(d + e + f)")
        multiply_expr_step4 = MathTex("= ad + ae + af + bd + be + bf + cd + ce + cf")
       
        # Positioning
        binomial.shift(UP*2 + 3*LEFT)
        trinomial.shift(UP*2 + 3*RIGHT)
        multiply_expr_step1.next_to(binomial, DOWN, buff=1).shift(1.5*RIGHT)
        multiply_expr_step2.next_to(multiply_expr_step1, DOWN, buff=0.5)
        multiply_expr_step3.next_to(multiply_expr_step2, DOWN, buff=0.5)
        multiply_expr_step4.next_to(multiply_expr_step3, DOWN, buff=0.5)

        # Writing expressions
        self.play(Write(binomial))
        self.play(Write(trinomial))
        self.wait(1)

        # Showing multiplication step by step
        self.play(Write(multiply_expr_step1))
        self.wait(1)
        self.play(Write(multiply_expr_step2))
        self.wait(1)
        self.play(Write(multiply_expr_step3))
        self.wait(1)
        self.play(Write(multiply_expr_step4))
        self.wait(1)

        # Clean up
        self.play(FadeOut(binomial), FadeOut(trinomial), FadeOut(multiply_expr_step1), FadeOut(multiply_expr_step2), FadeOut(multiply_expr_step3), FadeOut(multiply_expr_step4), FadeOut(title))
        self.wait(1)

    def identities(self):
        self.setNumberOfCirclePositions(5)
        self.isRandom = False
        self.angleChoice = [TAU/4,TAU/4,TAU/4,TAU/4]
        p10 = cvo.CVO().CreateCVO("identities", "").setPosition([-3.5, 0, 0])
        p11 = cvo.CVO().CreateCVO("(a+b)^2", "a^2+b^2+2ab").setPosition([2, 2.5, 0])
        p11.SetIsMathText(True)
        p12 = cvo.CVO().CreateCVO("(a-b)^2", "a^2+b^2-2ab").setPosition([3.5, 1.5, 0])
        p12.SetIsMathText(True)
        p13 = cvo.CVO().CreateCVO("(a+b)(a-b)", "a^2-b^2").setPosition([3.5, -1, 0])
        p13.SetIsMathText(True)
        p14 = cvo.CVO().CreateCVO("(x+a)(x+b)", "x^2+(a+b)x+ab").setPosition([1.7, -2.5, 0])
        p14.SetIsMathText(True)
        
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        
        self.construct1(p10, p10)
   
    def ApplicationOfIdentities(self):
        # Title
        title = Text("Applications of Identities")
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Step by step calculation
        original_expression = MathTex("204^2")
        split_expression = MathTex("= (200 + 4)^2")
        expanded_expression = MathTex("= (200)^2 + 2(200)(4) + 4^2")
        calculated_terms = MathTex("= 40000 + 1600 + 16")
        final_result = MathTex("= 41616")

        # Positioning
        original_expression.next_to(title, DOWN, buff=1.5)
        split_expression.next_to(original_expression, DOWN, buff=0.5)
        expanded_expression.next_to(split_expression, DOWN, buff=0.5)
        calculated_terms.next_to(expanded_expression, DOWN, buff=0.5)
        final_result.next_to(calculated_terms, DOWN, buff=0.5)

        # Writing expressions step by step
        self.play(Write(original_expression))
        self.wait(1)
        self.play(Write(split_expression))
        self.wait(1)
        self.play(Write(expanded_expression))
        self.wait(1)
        self.play(Write(calculated_terms))
        self.wait(1)
        self.play(Write(final_result))
        self.wait(2)

        # Clean up
        self.play(FadeOut(original_expression), FadeOut(split_expression), FadeOut(expanded_expression), FadeOut(calculated_terms), FadeOut(final_result), FadeOut(title))
        self.wait(1)

    def finding1962(self):
        # Title
        title = Tex("Finding","$ (196)^2 $")
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Step by step calculation
        original_expression = MathTex("196^2")
        split_expression = MathTex("= (200 - 4)^2")
        expanded_expression = MathTex("= (200)^2 - 2(200)(4) + 4^2")
        calculated_terms = MathTex("= 40000 - 1600 + 16")
        final_result = MathTex("= 38416")

        # Positioning
        original_expression.next_to(title, DOWN, buff=1.5)
        split_expression.next_to(original_expression, DOWN, buff=0.5)
        expanded_expression.next_to(split_expression, DOWN, buff=0.5)
        calculated_terms.next_to(expanded_expression, DOWN, buff=0.5)
        final_result.next_to(calculated_terms, DOWN, buff=0.5)

        # Writing expressions step by step
        self.play(Write(original_expression))
        self.wait(1)
        self.play(Write(split_expression))
        self.wait(1)
        self.play(Write(expanded_expression))
        self.wait(1)
        self.play(Write(calculated_terms))
        self.wait(1)
        self.play(Write(final_result))
        self.wait(2)

        # Clean up
        self.play(
            FadeOut(original_expression),
            FadeOut(split_expression),
            FadeOut(expanded_expression),
            FadeOut(calculated_terms),
            FadeOut(final_result),
            FadeOut(title)
        )
        self.wait(1)
        
    def application2(self):
        
        # Title
        title = Text("Finding 407 × 393")
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Step by step calculation
        original_expression = MathTex("407 \\times 393")
        split_expression = MathTex("= (400 + 7)(400 - 7)")
        expanded_expression = MathTex("= 400^2 - 7^2")
        calculated_terms = MathTex("= 160000 - 49")
        final_result = MathTex("= 159951")

        # Positioning
        original_expression.next_to(title, DOWN, buff=1.5)
        split_expression.next_to(original_expression, DOWN, buff=0.5)
        expanded_expression.next_to(split_expression, DOWN, buff=0.5)
        calculated_terms.next_to(expanded_expression, DOWN, buff=0.5)
        final_result.next_to(calculated_terms, DOWN, buff=0.5)

        # Writing expressions step by step
        self.play(Write(original_expression))
        self.wait(1)
        self.play(Write(split_expression))
        self.wait(1)
        self.play(Write(expanded_expression))
        self.wait(1)
        self.play(Write(calculated_terms))
        self.wait(1)
        self.play(Write(final_result))
        self.wait(2)

        # Clean up
        self.play(
            FadeOut(original_expression),
            FadeOut(split_expression),
            FadeOut(expanded_expression),
            FadeOut(calculated_terms),
            FadeOut(final_result),
            FadeOut(title)
        )
        self.wait(1)


if __name__ == "__main__":
    scene = AlgebraicExpression()
    scene.render()
