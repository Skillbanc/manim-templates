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
class quadraticAnim(AbstractAnim):
    def construct(self):
           self.RenderSkillbancLogo()
           self.constructDataByCVO()
           self.fadeOutCurrentScene()
           self.quad111()
           self.fadeOutCurrentScene()
           self.roots()
           self.fadeOutCurrentScene()
           self.quad1122()
           self.fadeOutCurrentScene() 
           self.quad1133()
           self.fadeOutCurrentScene()
           self.quad1155()
           self.fadeOutCurrentScene() 
           self.quad1166()
           self.fadeOutCurrentScene()
           self.RenderEquality1()
           self.fadeOutCurrentScene()
           self.tryfile()
           self.fadeOutCurrentScene()
           self.Sol()
           self.fadeOutCurrentScene()
           self.GithubSourceCodeReference()

    def constructDataByCVO(self):
         self.setNumberOfCirclePositions(4)
         p10 = cvo.CVO().CreateCVO("Quadratic Equations", "").setPosition([-3, 2, 0]).setangle(-TAU / 4)
         p11 = cvo.CVO().CreateCVO("Standard form", "$ax^2 + bx + c = 0$").setPosition([2, 2, 0]).setangle(-TAU / 4)
         p12 = cvo.CVO().CreateCVO("Real Numbers", "a, b, c are real numbers").setPosition([-3, -2, 0]).setangle(-TAU / 4)
         p13 = cvo.CVO().CreateCVO("Condition", "$a \\neq 0$").setPosition([3,-2, 0]).setangle(-TAU / 4)
        
         p11.setcircleradius(1.5)
         p12.setcircleradius(1.5)
         p10.cvolist.append(p11)
         p11.cvolist.append(p12)
         p11.cvolist.append(p13)
         self.construct1(p10, p10) 
    
    def quad111(self):
   
        self.setNumberOfCirclePositions(6)
        self.isRandom = False
        self.angleChoice = [TAU / 6,TAU / 6,TAU / 6,TAU / 6,TAU / 6]
        p20 = cvo.CVO().CreateCVO("Equation", "$3x^2-5x+7 = 0$").setPosition([-4, 0, 0])
        p21 = cvo.CVO().CreateCVO("$Coefficient of x^2$", "3").setPosition([3.5, 0, 0]).setangle(-TAU / 6)
        p22 = cvo.CVO().CreateCVO("Coefficient of x", "-5").setPosition([0,2, 0]).setangle(-TAU / 6)
        p23 = cvo.CVO().CreateCVO("Constant", "7").setPosition([3, 2, 0]).setangle(-TAU / 6)
        p24 = cvo.CVO().CreateCVO("Nature of roots", "Imaginary roots").setPosition([3, -2, 0]).setangle(-TAU / 6)
        p25 = cvo.CVO().CreateCVO("Formula to Find Roots", "$x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$").setPosition([0,-3, 0]).setangle(-TAU / 6)
        p20.cvolist.append(p21)
        p20.cvolist.append(p22)
        p20.cvolist.append(p23)
        p20.cvolist.append(p24)
        p20.cvolist.append(p25)
        p20.setcircleradius(1.5)
        p25.setcircleradius(1.5)

        self.construct1(p20, p20)

    def roots(self):
        title = MathTex(r"\text{Find the roots of } x^2 + 2x - 4 = 0").to_edge(UP)
        self.play(Write(title))
        
        equation = MathTex("x^2 + 2x - 4 = 0", font_size=36)
        formula = MathTex("x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}", font_size=36)
        a_eq = MathTex("a = 1", font_size=36)
        b_eq = MathTex("b = 2", font_size=36)
        c_eq = MathTex("c = -4", font_size=36)
        
        left_column = VGroup(equation, formula, a_eq, b_eq, c_eq).arrange(DOWN, buff=0.5)
        left_column.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=1)

        subs_formula = MathTex("x = \\frac{-2 \\pm \\sqrt{2^2 - 4 \\cdot 1 \\cdot (-4)}}{2 \\cdot 1}", font_size=36)
        simplify1 = MathTex("x = \\frac{-2 \\pm \\sqrt{4 + 16}}{2}", font_size=36)
        simplify2 = MathTex("x = \\frac{-2 \\pm \\sqrt{20}}{2}", font_size=36)

        right_column = VGroup(subs_formula, simplify1, simplify2).arrange(DOWN, buff=0.5)
        right_column.next_to(title, DOWN, buff=0.5).to_edge(RIGHT, buff=1)

        divider_line = Line(start=3*UP, end=1*DOWN).move_to(ORIGIN)
        self.play(Write(left_column), Write(right_column), Create(divider_line))
        self.wait(2)

        final_answer = VGroup(
            MathTex("x_1 = -1 + \\sqrt{5},   x_2 = -1 - \\sqrt{5}", font_size=24),
            Text("These are the roots of the equation", font_size=24) 
        ).arrange(DOWN, buff=0.5).scale(1.5).move_to(DOWN*3)

        self.play(Write(final_answer))
        self.wait(2)

    def quad1122(self):
        self.setNumberOfCirclePositions(5)
        self.isRandom = False
        self.angleChoice = [TAU / 6,TAU / 6,TAU / 6,TAU / 6,TAU / 6]
        p30 = cvo.CVO().CreateCVO("Equation", "$2x^2+5x+47 = 0$")
        p31 = cvo.CVO().CreateCVO("Degree", "2").setPosition([3, -2, 0])
        p32 = cvo.CVO().CreateCVO("Constant", "47").setPosition([0, 2, 0])
        p33 = cvo.CVO().CreateCVO("Roots", "$1, \\frac{47}{2}$").setPosition([3, 2, 0])
        p34 = cvo.CVO().CreateCVO("Nature of roots", "imaginary roots").setPosition([-2, 2, 0])

        p30.cvolist.append(p31)
        p30.cvolist.append(p32)
        p30.cvolist.append(p33)
        p30.cvolist.append(p34)
        p30.setcircleradius(1.5)

        self.construct1(p30, p30)

    def quad1133(self):
       
        title = Text("Checking if the Equation is Quadratic").scale(0.8).to_edge(UP)
        self.play(Write(title))
        equation = MathTex("x(2x + 3) = x^2 + 1").scale(1.2).next_to(title, DOWN, buff=0.5)
        self.play(Write(equation))
        explanation = Text("Let's simplify and check if it's quadratic...").scale(0.6).next_to(equation, DOWN, buff=0.5)
        self.play(Write(explanation))
        steps = VGroup(
            MathTex("x(2x + 3)", "=", "x^2 + 1").scale(0.8),
            MathTex("2x^2 + 3x", "=", "x^2 + 1").scale(0.8),
            MathTex("2x^2 + 3x - x^2", "=", "1").scale(0.8),
            MathTex("x^2 + 3x", "=", "1").scale(0.8)
        ).arrange(DOWN, buff=0.3).next_to(explanation, DOWN, buff=0.5)
        
        for step in steps:
            self.play(Write(step))
        conclusion = MathTex("x^2 + 3x - 1 = 0").scale(0.8).next_to(steps, DOWN, buff=0.5)
        conclusion_text = MathTex("\\text{The equation is quadratic as it is in the form of } ax^2 + bx + c = 0, \\ (a \\neq 0)").scale(0.6).next_to(conclusion, DOWN, buff=0.3)
        self.play(Write(conclusion))
        self.play(Write(conclusion_text))
        self.wait(2)

    def quad1155(self):
        title = Text("Finding Roots of Equation by Factorisation", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        intro_text = Text("The given equation is", font_size=24)
        equation = MathTex("2x^2 - 5x + 3 = 0")
        intro_group = VGroup(intro_text, equation).arrange(RIGHT, buff=0.5)
        intro_group.next_to(title, DOWN)
        intro_group.shift(RIGHT * 2) 
        self.play(Write(intro_group))
        self.wait(1)
        
        explanation_text = Text("The middle term ‘-5x’ can be written as -2x -3x", font_size=24)
        explanation_text.next_to(intro_group, DOWN, buff=0.5)

        self.play(Write(explanation_text))
        self.wait(1)
        box_height = 6
        box_width = 3.5
        vertical_box = Rectangle(height=box_height, width=box_width, color=BLUE)
        vertical_box.to_edge(LEFT, buff=1)  

        self.play(Create(vertical_box))
        text_inside_box = VGroup(
            Text("a=2, b=-5, c=3", font_size=24),
            Text("p=-2, q=-3", font_size=24),
            Text("b = p + q = –5", font_size=24),
            Text("ac = p * q = 6", font_size=24),
            Text("Possible pairs", font_size=24),
            Text("of factors", font_size=24),
            Text("of 6 are", font_size=24),
            Text("(1, 6), (–1, –6),", font_size=24),
            Text("(2, 3), (–2, –3).", font_size=24),
        ).arrange(DOWN, buff=0.2).move_to(vertical_box.get_center())

        self.play(Write(text_inside_box))

        step1 = MathTex("2x^2 - 2x -3x + 3 = 0")
        step2 = MathTex("2x(x-1) -3(x-1) = 0")
        step3 = MathTex("(2x - 3)(x - 1) = 0")
        
        steps = VGroup(step1, step2, step3).arrange(DOWN, buff=0.5)
        steps.next_to(explanation_text, DOWN, buff=0.5) 

        steps.scale(0.75)

        for step in steps:
            self.play(Write(step))
            self.wait(1)
      
        step5 = MathTex("x = \\frac{3}{2} \\text{ or } x = 1")
        concluding_text = Text("are the roots of the given equation", font_size=24)
        
        step5_group = VGroup(step5, concluding_text).arrange(RIGHT, buff=0.5)
        step5_group.next_to(steps, DOWN, buff=0.5)
        step5_group.shift(RIGHT * 0.5) 

        self.play(Write(step5_group))
        self.wait(5)

    def quad1166(self):

        self.setNumberOfCirclePositions(7)
        self.isRandom = False
        self.angleChoice = [TAU / 6,TAU / 6,TAU / 6,TAU / 6,TAU / 6,TAU / 6]
        p70 = cvo.CVO().CreateCVO("Example", "Solution of equation by completing the square").setPosition([-4.5, 2, 0])   
        p71 = cvo.CVO().CreateCVO("Equation", "$ax^2 + bx + c = 0$").setPosition([0, 2, 0])
        p72 = cvo.CVO().CreateCVO("Step 1", "Divide each side by a").setPosition([4.5,1,0])
        p73 = cvo.CVO().CreateCVO("Step 2", "Take c/a on RHS").setPosition([3.5, -1.8, 0])
        p74 = cvo.CVO().CreateCVO("Step 3", "$Add \\left(\\frac{1}{2}\\frac{b}{a}\\right)^2$").setPosition([1, -2.5, 0])
        p75 = cvo.CVO().CreateCVO("Step 4", "Square LHS and simplify RHS").setPosition([-2.5, -2, 0])
        p76 = cvo.CVO().CreateCVO("Step 5", "Solve").setPosition([-4.5, -1, 0])

        p70.cvolist.append(p71)
        p71.cvolist.append(p72)
        p71.cvolist.append(p73)
        p71.cvolist.append(p74)
        p71.cvolist.append(p75)
        p71.cvolist.append(p76)
        p71.setcircleradius(1.5)

        self.construct1(p70, p70)

    def RenderEquality1(self):
  
        title = Text("Example: Finding Roots by Completing the Square Method").scale(0.8).to_edge(UP, buff=0.5)
        self.play(Write(title))
        equation = MathTex("4x^2 + 3x + 5 = 0").scale(1.2).move_to(LEFT * 3 + UP * 2)
        self.play(Write(equation))
        self.wait(1)
        step1_text = MathTex("x^2 + \\frac{3}{4}x + \\frac{5}{4} = 0").scale(0.8).next_to(equation, DOWN, buff=0.5).align_to(equation, LEFT)
        self.play(Write(step1_text))
        self.wait(1)
        step2_text = MathTex("x^2 + \\frac{3}{4}x = -\\frac{5}{4}").scale(0.8).next_to(step1_text, DOWN, buff=0.5).align_to(step1_text, LEFT)
        self.play(Write(step2_text))
        self.wait(1)
        step3_text = MathTex("x^2 + \\frac{3}{4}x + \\left(\\frac{3}{8}\\right)^2 = -\\frac{5}{4} + \\left(\\frac{3}{8}\\right)^2").scale(0.8).next_to(step2_text, DOWN, buff=0.5).align_to(step2_text, LEFT)
        self.play(Write(step3_text))
        self.wait(1)
        step4_text = MathTex("\\left(x + \\frac{3}{8}\\right)^2 = -\\frac{71}{64}<0").scale(0.8).next_to(step3_text, DOWN, buff=0.5).align_to(step3_text, LEFT)
        self.play(Write(step4_text))

        self.wait(1)
        step5_text = MathTex("\\left(x + \\frac{3}{8}\\right)^2 = -\\frac{71}{64}").scale(0.8).next_to(step4_text, DOWN, buff=0.5).align_to(step4_text, LEFT)
        self.play(Write(step5_text))

        self.wait(1)
        conclusion_text = VGroup(
            Text("The equation has no real roots", font_size=24),
            Text("because the value is less than 0", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT, buff=1).shift(DOWN)
        self.play(Write(conclusion_text))

        self.wait(2)

    def tryfile(self):
    
        title = Text("Solving for the sides of a right-angled triangle").to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        hypotenuse = 25
        difference = 5

        equation_text = MathTex(
            r"\text{Let the length of the smaller side be } x \text{ cm}",
            r"\text{Then length of the longer side } = (x + 5) \text{ cm}",
            r"\text{Given length of the hypotenuse } = 25 \text{ cm}"
        ).scale(0.7).arrange(DOWN, buff=0.5).to_edge(LEFT)
        self.play(Write(equation_text))
        self.wait(1)

        steps_text = MathTex(
            r"\text{In a right-angled triangle, } c^2 = a^2 + b^2",
            r"\text{So, } x^2 + (x + 5)^2 = 25^2",
            r"x^2 + x^2 + 10x + 25 = 625",
            r"2x^2 + 10x - 600 = 0",
            r"x^2 + 5x - 300 = 0"
        ).scale(0.7).arrange(DOWN, buff=0.3).next_to(equation_text, DOWN, buff=0.5).to_edge(LEFT)
        self.play(Write(steps_text))
        self.wait(2)

        self.play(
            equation_text.animate.to_edge(LEFT).shift(UP),
            steps_text.animate.to_edge(LEFT).shift(UP)
        )

        A = ORIGIN
        B = RIGHT * 4
        C = ORIGIN + UP * 3
        triangle = Polygon(A, B, C, color=BLUE, fill_opacity=0.5)
        hyp_line = Line(A, B, color=RED)

        side_label_x = MathTex("x", color=WHITE).next_to(A, DOWN).scale(0.7)
        side_label_x_plus_5 = MathTex("x + 5 \, {cm}", color=WHITE).next_to(C, UP).scale(0.7)
        hyp_label = MathTex("25 \, {cm}", color=WHITE).next_to(triangle.get_center(), RIGHT, buff=0.25).scale(0.7)
     
        triangle_group = VGroup(triangle, hyp_line, side_label_x, side_label_x_plus_5, hyp_label)
        triangle_group.scale(0.9).move_to([3, 0, 0])
        
        self.play(Create(triangle), Create(hyp_line))
        self.play(Write(side_label_x), Write(side_label_x_plus_5), Write(hyp_label))
        self.wait(5)


    def Sol(self):
        
        title = Text("Solving for the sides of a right-angled triangle").to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        A = ORIGIN
        B = RIGHT * 4
        C = ORIGIN + UP * 3
        
        triangle = Polygon(A, B, C, color=BLUE, fill_opacity=0.5)
        hyp_line = Line(A, B, color=RED)

        side_label_x = MathTex("x", color=WHITE).next_to(A, DOWN).scale(0.6)
        side_label_x_plus_5 = MathTex("x + 5 \\, {\\text{cm}}", color=WHITE).next_to(C, UP).scale(0.6)
        hyp_label = MathTex("25 \\, {\\text{cm}}", color=WHITE).next_to(triangle.get_center(), RIGHT, buff=0.25).scale(0.6)
   
        triangle_group = VGroup(triangle, hyp_line, side_label_x, side_label_x_plus_5, hyp_label)
        triangle_group.scale(0.9).move_to([4, 0, 0])
   
        self.play(Create(triangle), Create(hyp_line))
        self.play(Write(side_label_x), Write(side_label_x_plus_5), Write(hyp_label))
        self.wait(2)
        
        quadratic_solution_steps = MathTex(
            r"\text{Solving the quadratic equation: }",
            r"x^2 + 5x - 300 = 0",
            r"\text{Factorize the quadratic equation: }",
            r"(x + 20)(x - 15) = 0",
            r"\text{So, } x + 20 = 0 \text{ or } x - 15 = 0",
            r"x = -20 \text{ or } x = 15",
            r"\text{Reject } x = -20 \text{ since side length can't be negative}"
        ).scale(0.7).arrange(DOWN, buff=0.3).to_edge(LEFT).shift(UP * 0.5)
        self.play(Write(quadratic_solution_steps))
        self.wait(2)
        
        final_lengths_text = MathTex(
            r"\text{So, the lengths of the sides are: }",
            r"x = 15 \, \text{cm, and } x + 5 = 20 \, \text{cm}"
        ).scale(0.7).next_to(quadratic_solution_steps, DOWN, buff=0.5).to_edge(LEFT)
        
        self.play(Write(final_lengths_text))
        self.wait(5)

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade10Chapter5quadraticEquations.py"

    def SetDeveloperList(self):  
        self.DeveloperList="Habeeb Unissa"

if __name__ == "__main__":
    scene = quadraticAnim()
    scene.render()