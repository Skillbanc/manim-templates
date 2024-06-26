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

class AlgebraicAnim5(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.Introduction()
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
        self.MultiplyingBinomialByTrinomial()
        self.identities()
        self.fadeOutCurrentScene()
        self.ApplicationOfIdentities()
        self.GeometricVerification1()
        self.GeometricVerification2()
        self.GeometricVerification3()
        self.GithubSourceCodeReference()
        
    def SetDeveloperList(self):
       self.DeveloperList="Vasudha"
       
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade8CH11AlgebraicExpressions.py"
    
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
        p11 = cvo.CVO().CreateCVO("monomial", "An algebraic expression with a single term(eg..,2x, 4z^2)").setPosition([4, 2, 0])
        p11.SetIsMathText(True)
        p12 = cvo.CVO().CreateCVO("binomial", "An algebraic expression with two terms(eg..,3x + 2)").setPosition([3.5, -2, 0])
        p12.SetIsMathText(True)
        p13 = cvo.CVO().CreateCVO("trinomial", "An algebraic expression with three terms(eg..,x^2 + 3x + 2)").setPosition([-4, 2, 0])
        p13.SetIsMathText(True)
        p14 = cvo.CVO().CreateCVO("polynomial", "An algebraic expression with one or more terms(eg..,4x^3 + 3x^2 - x + 7)").setPosition([-3, -2, 0])
        p14.SetIsMathText(True)

        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)

        self.construct1(p10, p10)

    
    def Polynomials(self):
        self.setNumberOfCirclePositions(7)
        p10 = cvo.CVO().CreateCVO("polynomials", "types").setPosition([0, 2.5, 0])
        p11 = cvo.CVO().CreateCVO("Linear Polynomial", "A polynomial of degree 1 ").setPosition([4, 2, 0])
        p12 = cvo.CVO().CreateCVO("Quadratic Polynomial", "A polynomial of degree 2 ").setPosition([5, -2, 0])
        p13 = cvo.CVO().CreateCVO("Cubic Polynomial", "A polynomial of degree 3 ").setPosition([-4, 2, 0])
        p14 = cvo.CVO().CreateCVO("Quartic Polynomial", "A polynomial of degree 4").setPosition([-4, -2, 0])
        p15 = cvo.CVO().CreateCVO("Quintic Polynomial", "A polynomial of degree 5").setPosition([0, -2.5, 0])
        p16 = cvo.CVO().CreateCVO("Sextic Polynomial", "A polynomial of degree 6 ").setPosition([0, 0, 0])

        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        p10.cvolist.append(p16)

        self.construct1(p10, p10)

    def Relations(self):
        self.setNumberOfCirclePositions(4)
        p10 = cvo.CVO().CreateCVO("operations", "+,-,x").setPosition([0, 2.5, 0])
        p11 = cvo.CVO().CreateCVO("addition", "Combining like terms(eg..,(3a^2 + 2a^2) = 5a^2)").setPosition([4, 2, 0])
        p11.SetIsMathText(True)
        p12 = cvo.CVO().CreateCVO("substraction", "Finding the difference between like terms(ex,,.(2x^2 + 3x) - (x^2 + 2x) = x^2 + x)").setPosition([2, -2.5, 0])
        p12.SetIsMathText(True)
        p13 = cvo.CVO().CreateCVO("multiplication", "Distributing terms and combining like terms(eg..,(x + 2)(x + 3) = x^2 + 5x + 6)").setPosition([-3, -1, 0])
        p13.SetIsMathText(True)

        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)

        self.construct1(p10, p10)
        
    def AdditionOfAlgebraicExpressions(self):
        # Title
        title = Text("Addition of Algebraic Expressions")
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Expressions
        expr1 = MathTex("3x + 2y")
        expr2 = MathTex("5x - 3y")
        add_expr_step1 = MathTex("(3x + 2y) + (5x - 3y)")
        add_expr_step2 = MathTex("= (3x + 5x) + (2y - 3y)= 8x - y")


        # Positioning
        expr1.shift(UP + 3*LEFT)
        expr2.shift(UP + 3*RIGHT)
        add_expr_step1.next_to(expr1, DOWN, buff=1.5).shift(1.5*RIGHT)
        add_expr_step2.next_to(add_expr_step1, DOWN, buff=1)

        # Writing expressions
        self.play(Write(expr1))
        self.play(Write(expr2))
        self.wait(1)

        # Showing addition step by step
        self.play(Write(add_expr_step1))
        self.wait(1)
        self.play(Write(add_expr_step2))
        self.wait(1)
        # Clean up
        self.play(FadeOut(expr1), FadeOut(expr2), FadeOut(add_expr_step1), FadeOut(add_expr_step2), FadeOut(title))
        self.wait(1)

    def SubtractionOfAlgebraicExpressions(self):
        # Title
        title = Text("Subtraction of Algebraic Expressions")
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Expressions
        expr1 = MathTex("3x + 2y")
        expr2 = MathTex("5x - 3y")
        sub_expr_step1 = MathTex("(3x + 2y) - (5x - 3y)")
        sub_expr_step2 = MathTex("= (3x - 5x) + (2y + 3y) = -2x + 5y")
    
        # Positioning
        expr1.shift(UP + 3*LEFT)
        expr2.shift(UP + 3*RIGHT)
        sub_expr_step1.next_to(expr1, DOWN, buff=1.5).shift(1.5*RIGHT)
        sub_expr_step2.next_to(sub_expr_step1, DOWN, buff=1)


        # Writing expressions
        self.play(Write(expr1))
        self.play(Write(expr2))
        self.wait(1)

        # Showing subtraction step by step
        self.play(Write(sub_expr_step1))
        self.wait(1)
        self.play(Write(sub_expr_step2))
        self.wait(1)
        
        # Clean up
        self.play(FadeOut(expr1), FadeOut(expr2), FadeOut(sub_expr_step1), FadeOut(sub_expr_step2), FadeOut(title))
        self.wait(1)

    def MultiplyingMonomials(self):
        # Title
        title = Text("Multiplying Monomials")
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Expressions
        expr1 = MathTex("2x^2")
        expr2 = MathTex("3x^3")
        multiply_expr_step1 = MathTex("2x^2 \\cdot 3x^3 = 2 \\cdot 3 \\cdot x^2 \\cdot x^3")
        multiply_expr_step2 = MathTex("= 6 \\cdot x^{2+3} = 6x^5")

        # Positioning
        expr1.shift(UP + 3*LEFT)
        expr2.shift(UP + 3*RIGHT)
        multiply_expr_step1.next_to(expr1, DOWN, buff=1.5).shift(1.5*RIGHT)
        multiply_expr_step2.next_to(multiply_expr_step1, DOWN, buff=1)
    
        # Writing expressions
        self.play(Write(expr1))
        self.play(Write(expr2))
        self.wait(1)

        # Showing multiplication step by step
        self.play(Write(multiply_expr_step1))
        self.wait(1)
        self.play(Write(multiply_expr_step2))
        self.wait(1)
        
        # Clean up
        self.play(FadeOut(expr1), FadeOut(expr2), FadeOut(multiply_expr_step1), FadeOut(multiply_expr_step2), FadeOut(title))
        self.wait(1)

    def MultiplyingBinomialByMonomial(self):
        # Title
        title = Text("Multiplying a Binomial by a Monomial")
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Expressions
        binomial = MathTex("2x + 3")
        monomial = MathTex("4x")
        multiply_expr_step1 = MathTex("4x(2x + 3)")
        multiply_expr_step2 = MathTex("= 4x \\cdot 2x + 4x \\cdot 3 = 8x^2 + 12x")


        # Positioning
        binomial.shift(UP + 3*LEFT)
        monomial.shift(UP + 3*RIGHT)
        multiply_expr_step1.next_to(binomial, DOWN, buff=1.5).shift(1.5*RIGHT)
        multiply_expr_step2.next_to(multiply_expr_step1, DOWN, buff=1)
    
        # Writing expressions
        self.play(Write(binomial))
        self.play(Write(monomial))
        self.wait(1)

        # Showing multiplication step by step
        self.play(Write(multiply_expr_step1))
        self.wait(1)
        self.play(Write(multiply_expr_step2))
        self.wait(1)

        # Clean up
        self.play(FadeOut(binomial), FadeOut(monomial), FadeOut(multiply_expr_step1), FadeOut(multiply_expr_step2), FadeOut(title))
        self.wait(1)

    def MultiplyingTrinomialByMonomial(self):
        # Title
        title = Text("Multiplying a Trinomial by a Monomial")
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Expressions
        trinomial = MathTex("x^2 + 2x + 3")
        monomial = MathTex("4x")
        multiply_expr_step1 = MathTex("4x(x^2 + 2x + 3)")
        multiply_expr_step2 = MathTex("= 4x \\cdot x^2 + 4x \\cdot 2x + 4x \\cdot 3 = 4x^3 + 8x^2 + 12x")


        # Positioning
        trinomial.shift(UP + 3*LEFT)
        monomial.shift(UP + 3*RIGHT)
        multiply_expr_step1.next_to(trinomial, DOWN, buff=1.5).shift(1.5*RIGHT)
        multiply_expr_step2.next_to(multiply_expr_step1, DOWN, buff=1)

        # Writing expressions
        self.play(Write(trinomial))
        self.play(Write(monomial))
        self.wait(1)

        # Showing multiplication step by step
        self.play(Write(multiply_expr_step1))
        self.wait(1)
        self.play(Write(multiply_expr_step2))
        self.wait(1)

        # Clean up
        self.play(FadeOut(trinomial), FadeOut(monomial), FadeOut(multiply_expr_step1), FadeOut(multiply_expr_step2), FadeOut(title))
        self.wait(1)

    def MultiplyingBinomialByBinomial(self):
        # Title
        title = Text("Multiplying a Binomial by a Binomial")
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Expressions
        binomial1 = MathTex("a + b")
        binomial2 = MathTex("c + d")
        multiply_expr_step1 = MathTex("(a + b)(c + d)")
        multiply_expr_step2 = MathTex("= a(c + d) + b(c + d) = ac + ad + bc + bd")
    
        # Positioning
        binomial1.shift(UP + 3*LEFT)
        binomial2.shift(UP + 3*RIGHT)
        multiply_expr_step1.next_to(binomial1, DOWN, buff=1.5).shift(1.5*RIGHT)
        multiply_expr_step2.next_to(multiply_expr_step1, DOWN, buff=1)
    
        # Writing expressions
        self.play(Write(binomial1))
        self.play(Write(binomial2))
        self.wait(1)

        # Showing multiplication step by step
        self.play(Write(multiply_expr_step1))
        self.wait(1)
        self.play(Write(multiply_expr_step2))
        self.wait(1)

        # Clean up
        self.play(FadeOut(binomial1), FadeOut(binomial2), FadeOut(multiply_expr_step1), FadeOut(multiply_expr_step2), FadeOut(title))
        self.wait(1)

    def MultiplyingBinomialByTrinomial(self):
        # Title
        title = Text("Multiplying a Binomial by a Trinomial")
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Expressions
        binomial = MathTex("a + b")
        trinomial = MathTex("c + d + e")
        multiply_expr_step1 = MathTex("(a + b)(c + d + e) = a(c + d + e) + b(c + d + e)")
        multiply_expr_step2 = MathTex("= ac + ad + ae + bc + bd + be")
       
        # Positioning
        binomial.shift(UP + 3*LEFT)
        trinomial.shift(UP + 3*RIGHT)
        multiply_expr_step1.next_to(binomial, DOWN, buff=1.5).shift(1.5*RIGHT)
        multiply_expr_step2.next_to(multiply_expr_step1, DOWN, buff=1)

        # Writing expressions
        self.play(Write(binomial))
        self.play(Write(trinomial))
        self.wait(1)

        # Showing multiplication step by step
        self.play(Write(multiply_expr_step1))
        self.wait(1)
        self.play(Write(multiply_expr_step2))
        self.wait(1)

        # Clean up
        self.play(FadeOut(binomial), FadeOut(trinomial), FadeOut(multiply_expr_step1), FadeOut(multiply_expr_step2), FadeOut(title))
        self.wait(1)

    def identities(self):
        self.setNumberOfCirclePositions(5)
        self.isRandom = False
        p10 = cvo.CVO().CreateCVO("identities", "").setPosition([0, 2.5, 0])
        p11 = cvo.CVO().CreateCVO("(1) (a+b)^2", "a^2+b^2+2ab")
        p11.SetIsMathText(True)
        p12 = cvo.CVO().CreateCVO("(2) (a-b)^2", "a^2+b^2-2ab")
        p12.SetIsMathText(True)
        p13 = cvo.CVO().CreateCVO("(3) (a+b)(a-b)", "a^2-b^2")
        p13.SetIsMathText(True)
        p14 = cvo.CVO().CreateCVO("(4) (x+a)(x+b)", "x^2+(a+b)x+ab")
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

    def GeometricVerification1(self):
        # Title
        title = Text("Geometrical Verification of Identity(1)")
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Create squares and rectangles
        a_square = Square(side_length=2, color=BLUE)
        b_square = Square(side_length=2, color=GREEN)
        ab_rectangle = Rectangle(width=4, height=2, color=WHITE)

        # Positioning squares and rectangles
        a_square.move_to(LEFT * 3)
        b_square.move_to(RIGHT * 3)
        ab_rectangle.move_to(ORIGIN)

        # Labels for squares and rectangle
        a_label = MathTex("a^2", color=BLUE).next_to(a_square, DOWN)
        b_label = MathTex("b^2", color=GREEN).next_to(b_square, DOWN)
        ab_label = MathTex("2ab", color=WHITE).next_to(ab_rectangle, DOWN)

        # Group all objects together
        shapes_group = VGroup(a_square, b_square, ab_rectangle, a_label, b_label, ab_label)

        # Show squares and rectangles
        self.play(Create(a_square), Create(b_square), Create(ab_rectangle))
        self.wait()

        # Show labels
        self.play(Write(a_label), Write(b_label), Write(ab_label))
        self.wait()

        # Identity text
        identity_text = MathTex("(a + b)^2 = a^2 + 2ab + b^2").to_edge(DOWN)
        self.play(Write(identity_text))
        self.wait(2)

        # Fade out all objects
        self.play(FadeOut(shapes_group), FadeOut(identity_text), FadeOut(title))
        self.wait()

    def GeometricVerification2(self):
        # Title
        title = Text("Geometrical Verification of Identity(2)")
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Create squares and rectangles
        a_square = Square(side_length=2, color=BLUE)
        b_square = Square(side_length=2, color=GREEN)
        ab_rectangle = Rectangle(width=4, height=2, color=WHITE)

        # Positioning squares and rectangles
        a_square.move_to(LEFT * 3)
        b_square.move_to(RIGHT * 3)
        ab_rectangle.move_to(ORIGIN)

        # Labels for squares and rectangle
        a_label = MathTex("a^2", color=BLUE).next_to(a_square, DOWN)
        b_label = MathTex("b^2", color=GREEN).next_to(b_square, DOWN)
        ab_label = MathTex("-2ab", color=WHITE).next_to(ab_rectangle, DOWN)

        # Group all objects together
        shapes_group = VGroup(a_square, b_square, ab_rectangle, a_label, b_label, ab_label)

        # Show squares and rectangles
        self.play(Create(a_square), Create(b_square), Create(ab_rectangle))
        self.wait()

        # Show labels
        self.play(Write(a_label), Write(b_label), Write(ab_label))
        self.wait()

        # Identity text
        identity_text = MathTex("(a - b)^2 = a^2 - 2ab + b^2").to_edge(DOWN)
        self.play(Write(identity_text))
        self.wait(2)

        # Fade out all objects
        self.play(FadeOut(shapes_group), FadeOut(identity_text), FadeOut(title))
        self.wait()

    def GeometricVerification3(self):
       # Title
        title = Text("Geometrical Verification of Identity(3)")
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Create squares and rectangles
        a_square = Square(side_length=2, color=BLUE)
        b_square = Square(side_length=2, color=GREEN)
        ab_rect_outer = Rectangle(width=6, height=2, color=WHITE)
        ab_rect_inner = Rectangle(width=2, height=2, color=WHITE)

        # Positioning squares and rectangles
        a_square.move_to(LEFT * 3 + UP)
        b_square.move_to(RIGHT * 3 + UP)
        ab_rect_outer.move_to(ORIGIN)
        ab_rect_inner.move_to(ORIGIN)

        # Labels for squares and rectangle
        a_label = MathTex("a^2", color=BLUE).next_to(a_square, DOWN)
        b_label = MathTex("b^2", color=GREEN).next_to(b_square, DOWN)
        ab_label_outer = MathTex("(a+b)(a-b)", color=WHITE).next_to(ab_rect_outer, DOWN)
        ab_label_inner = MathTex("=a^2-b^2", color=WHITE).next_to(ab_rect_inner, DOWN)

        # Group all objects together
        shapes_group = VGroup(a_square, b_square, ab_rect_outer, ab_rect_inner, a_label, b_label, ab_label_outer, ab_label_inner)

        # Show squares and rectangles
        self.play(Create(a_square), Create(b_square), Create(ab_rect_outer))
        self.wait()

        # Show labels
        self.play(Write(a_label), Write(b_label), Write(ab_label_outer))
        self.wait()

        # Inner rectangle for subtraction
        self.play(Transform(ab_rect_outer, ab_rect_inner))
        self.play(Transform(ab_label_outer, ab_label_inner))
        self.wait(2)

        # Fade out all objects
        self.play(FadeOut(shapes_group), FadeOut(title))
        self.wait()

if __name__ == "__main__":
    scene = AlgebraicAnim5()
    scene.render()
