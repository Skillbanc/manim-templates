import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class Polynomial(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.Poly_example()
        self.fadeOutCurrentScene()
        self.Degree()
        self.fadeOutCurrentScene()
        self.Typesofpoly()
        self.fadeOutCurrentScene()
        self.Poly_BasedonDegree()
        self.fadeOutCurrentScene()
        self.Poly_BasedonNoofTerms()
        self.fadeOutCurrentScene()
        self.Zeroofpoly()
        self.fadeOutCurrentScene()
        self.Dividingthepoly()
        self.fadeOutCurrentScene()
        self.PolyDivExample()
        self.fadeOutCurrentScene()
        self.Remainder_Theorem()
        self.fadeOutCurrentScene()
        self.Factorising()
        self.fadeOutCurrentScene()
        self.Factor_Theorem()
        self.fadeOutCurrentScene()
        self.Algebraic_Identities()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

    def Introduction(self):
        self.angleChoice=[TAU/4,TAU/4,TAU/4,TAU/4,TAU/4]
        self.colorChoice=[BLUE,ORANGE,PINK,ORANGE,PURPLE,BLUE]
        p16=cvo.CVO().CreateCVO("Polynomial in one variable","").setPosition([-4,-2.5,0])
        p10=cvo.CVO().CreateCVO("General Form","p(x) = a_nx^n + a_{n-1}x^{n-1}+..+a_1x + a_0").setPosition([-3,0,0])
        p10.SetIsMathText(True)
        p11=cvo.CVO().CreateCVO("Variable"," x ").setPosition([0,2.5,0])
        p12=cvo.CVO().CreateCVO("Coefficients","a_n,a_{n-1}..a_1,a_0").setPosition([3,2.5,0])
        p12.SetIsMathText(True)
        p12.setcircleradius(1.5)
        p13=cvo.CVO().CreateCVO("Degree","n").setPosition([3,-2,0])
        p14=cvo.CVO().CreateCVO("condition","n should be non-negative integer").setPosition([3,0,0])
        p16.cvolist.append(p10)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p13.cvolist.append(p14)
        self.construct1(p16,p16)

    def Poly_example(self):
        self.angleChoice=[TAU/4,TAU/4,TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Polynomial","").setPosition([-4,2.5,0])
        p11=cvo.CVO().CreateCVO("Example","3x^2+7x+5").setPosition([-2,0,0])
        p11.SetIsMathText(True)
        p12=cvo.CVO().CreateCVO("Coefficients","3 , 7").setPosition([3,2,0])
        p13=cvo.CVO().CreateCVO("Terms","$3x^2$ , 7x , 5").setPosition([3,-2,0])
        p10.cvolist.append(p11)
        p11.cvolist.append(p13)
        p11.cvolist.append(p12)
        self.construct1(p10,p10)

    def Degree(self):
        Degree = VGroup(
            Text("Degree of the Polynomial:").set_color(YELLOW),
            Text("Highest degree among all the terms"),
            Text("Degree of the Term:").set_color(YELLOW),
            Text("Sum of exponents of its variable")
        ).arrange(DOWN).scale(0.75).to_edge(UP)

        for deg in Degree:
            self.play(Write(deg))
            self.wait(1)
        
        example = VGroup(
            MathTex("Example: 3x^2y^3 + 4xy + 7"),
            Text("Degree of the polynomial : 5",font_size=40).set_color(YELLOW)
        ).arrange(DOWN).scale(0.75).shift(LEFT*3).shift(DOWN*1)

        Degreeofterms = VGroup(
            Text("Degree of terms:").set_color(YELLOW),
            MathTex("3x^2y^3\\Rightarrow 5"),
            MathTex("4xy\\Rightarrow 2"),
            MathTex("7\\Rightarrow 0")
        ).arrange(DOWN).scale(0.75).next_to(example,RIGHT,buff=1.5)

        self.play(Write(example[0]))

        for termsdeg in Degreeofterms:
            self.play(Write(termsdeg))
            self.wait(1)

        self.play(Write(example[1]))
    
    def Typesofpoly(self):
        self.angleChoice=[TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Types of Polynomials","").setPosition([-3,0,0])
        p11=cvo.CVO().CreateCVO("Based on degree","").setPosition([1,2,0])
        p12=cvo.CVO().CreateCVO("Based on no. of terms","").setPosition([1,-2,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)

    def Poly_BasedonDegree(self):
        self.angleChoice=[TAU/4]
        self.colorChoice=[BLUE,PURPLE]
        p12=cvo.CVO().CreateCVO("Types of Polynomials","").setPosition([-3,0,0])
        p13=cvo.CVO().CreateCVO("Based on degree","").setPosition([3,0,0])
        p13onamelist=["Constant Polynomial","Linear Polynomial","Quadratic Polynomial","Cubic Polynomial"]
        p13.setcircleradius(2)
        p13.extendOname(p13onamelist)
        p12.cvolist.append(p13)
        self.construct1(p12,p12)
        self.fadeOutCurrentScene()
        title = Text("Types of Polynomials(Based on Dergree)").scale(0.8).to_edge(UP)
        self.play(Write(title))
        Terms = VGroup(
            MathTex("\\text{1. Constant Polynomial}:p(x)=constant"),
            MathTex("\\text{2. Linear Polynomial}:p(x)=ax+b;a \\neq 0"),
            MathTex("\\text{3. Quadratic Polynomial}:p(x)=ax^2+bx+c;a \\neq 0"),
            MathTex("\\text{4. Cubic Polynomial}:p(x)=ax^3+bx^2+cx+d;a \\neq 0")
            ).scale(0.8).set_color(BLUE).shift(UP*1)
        text = MathTex("Degree").scale(0.75).next_to(Terms,DOWN,buff=0.5).set_color(YELLOW)

        Degree = VGroup(
            MathTex("=0"),
            MathTex("=1"),
            MathTex("=2"),
            MathTex("=3")
            ).scale(0.8).next_to(text,RIGHT,buff=0.2).set_color(YELLOW)
        
        Examples = VGroup(
            MathTex("Example:p(x)=3"),
            MathTex("Example:p(x)=2x + 1"),
            MathTex("Example:p(x)=x^2 + x + 1"),
            MathTex("Example:p(x)=x^3 - x^2 + 2")
            ).scale(0.8).next_to(text,DOWN,buff=0.5)
        
        self.play(Write(Terms[0]))
        self.play(Write(text))
        self.play(Write(Degree[0]))
        self.wait(2)
        self.play(Write(Examples[0]))
        self.wait(3)
        
        for i in range(1, len(Terms)):
            self.play(Transform(Terms[0], Terms[i]))
            self.play(Transform(Degree[0], Degree[i]))
            self.play(Transform(Examples[0], Examples[i]))
            self.wait(4)

    def Poly_BasedonNoofTerms(self):
        self.angleChoice=[TAU/4]
        self.colorChoice=[BLUE,PINK]
        p12=cvo.CVO().CreateCVO("Types of Polynomials","").setPosition([-3,0,0])
        p13=cvo.CVO().CreateCVO("Based on no. of terms","").setPosition([3,0,0])
        p13onamelist=["Monomial","Binomial","Trinomial","Multinomial"]
        p13.setcircleradius(2)
        p13.extendOname(p13onamelist)
        p12.cvolist.append(p13)
        self.construct1(p12,p12)
        self.fadeOutCurrentScene()
        title = Text("Types of Polynomials(Based on no. of terms)").scale(0.8).to_edge(UP)
        self.play(Write(title))
        Terms = VGroup(
            MathTex("Monomial"),
            MathTex("Binomial"),
            MathTex("Trinomial"),
            MathTex("Multinomial")
            ).scale(0.8).shift(LEFT*2,UP*1).set_color(YELLOW)
        
        text = MathTex("\\text{: no. of non-zero terms }").scale(0.75).next_to(Terms,RIGHT,buff=0.3)

        Steps = VGroup(
            MathTex("=1"),
            MathTex("=2"),
            MathTex("=3"),
            MathTex(">=3")
            ).scale(0.8).next_to(text,RIGHT,buff=0.3).set_color(YELLOW)
        
        Examples = VGroup(
            MathTex("Example:p(x)=x"),
            MathTex("Example:p(x)=x + 2"),
            MathTex("Example:p(x)=x^3 + 2x + 2"),
            MathTex("Example:p(x)=3x^3 + x^2 + 2x - 7")
            ).scale(0.8).next_to(text,DOWN,buff=1).shift(LEFT*1.5)
        
        self.play(Write(Terms[0]))
        self.play(Write(text))
        self.play(Write(Steps[0]))
        self.wait(1)
        self.play(Write(Examples[0]))
        self.wait(3)
        
        for i in range(1, len(Terms)):
            self.play(Transform(Terms[0], Terms[i]))
            self.play(Transform(Steps[0], Steps[i]))
            self.play(Transform(Examples[0], Examples[i]))
            self.wait(3)

    def Zeroofpoly(self):
        self.colorChoice=[BLUE,ORANGE,YELLOW,PURPLE]
        self.angleChoice=[TAU/4,TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Zero of polynomial","").setPosition([-4.5,2.5,0])
        p11=cvo.CVO().CreateCVO("Condition","at value of x,p(x)=0").setPosition([3,2.5,0])
        p11.setcircleradius(1.5)
        p12=cvo.CVO().CreateCVO("Example","p(x)=3x + 1").setPosition([-2,-0.75,0])
        p13=cvo.CVO().CreateCVO("Zero of the polynomial","-1/3").setPosition([3,-0.75,0])
        text = Text("Fact:A polynomial of degree n can have at most n zeros").scale(0.65).to_edge(DOWN).shift(UP*1)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p12.cvolist.append(p13)
        self.construct1(p10,p10)
        self.play(Write(text))
        self.wait(2)
        self.fadeOutCurrentScene()

    def Dividingthepoly(self):
        self.angleChoice=[TAU/4,TAU/4,TAU/4]
        self.colorChoice=[YELLOW,ORANGE]
        p10=cvo.CVO().CreateCVO("Division of polynomial","").setPosition([-3,0,0])
        p11=cvo.CVO().CreateCVO("Formula","Dividend=(Divisor*Quotient)+Remainder").setPosition([3,0,0])
        p11.setcircleradius(3)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
    
    def PolyDivExample(self):
        title = Text("Polynomial Division").scale(0.8).to_edge(UP)
        self.play(Write(title))
        text = Text("Example").scale(0.5).next_to(title,DOWN)
        self.play(Write(text))
        multiline1 = MathTex("Dividend:3x^2 + x - 1", "Divisor:x + 1").arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT).scale(0.65).shift(DOWN*1)

        Steps = VGroup(
            MathTex("\\text{Step 1: Divide } \\frac{3x^2}{x}=3x,","\\text{it becomes first term in quotient}").arrange(DOWN),
            MathTex("\\text{Step 2: Multiply } (x + 1)3x = 3x^2 + 3x"),
            MathTex("\\text{Step 3: Divide }\\frac{-2x}{x}=-2,","\\text{it becomes second term in quotient}").arrange(DOWN),
            MathTex("\\text{Step 4: Multiply } (x + 1)-2 = -2x - 2"),
            MathTex("\\text{Step 5: We stop here as the }","\\text{remainder is 1, a constant}").arrange(DOWN),
            Text("The division process is said to be complete \n if we get the remainder 0 or the \n degree of the remainder is less than\n the degree of the divisor",font_size=30)
            ).scale(0.65).shift(UP*1,RIGHT*2).set_color(YELLOW)
        
        divisor = MathTex("x + 1").to_edge(LEFT).shift(UP*1.5)
        dividend = MathTex("3x^2 + x - 1").next_to(divisor, RIGHT)
        division_line = Line(divisor.get_right(), divisor.get_right() + RIGHT * 3.5).shift(UP*0.3,RIGHT*0.2)
        division_linev = Line(divisor.get_right(), divisor.get_right() + DOWN * 1).shift(UP*0.3,RIGHT*0.2)
        self.play(Write(multiline1))
        self.play(Write(divisor), Write(division_line), Write(dividend.shift(RIGHT*0.25)),Write(division_linev))
        self.wait(1)
        self.play(FadeIn(Steps[0]))
        self.wait(3)

        quotient1 = MathTex("3x").next_to(division_line, UP, aligned_edge=LEFT)
        multiply1 = MathTex("-3x^2 + 3x").next_to(dividend, DOWN).shift(LEFT*0.15)
        division_line1 = Line(divisor.get_right(), divisor.get_right() + RIGHT * 3.5).next_to(division_line,DOWN*5.5)
        result1 = MathTex("-2x - 1").next_to(multiply1, DOWN).shift(RIGHT*1)
        self.play(Write(quotient1))
        self.wait(1)
        self.play(Transform(Steps[0],Steps[1]))
        self.wait(3)
        self.play(Write(multiply1))
        self.wait(1)
        self.play(Write(division_line1),Write(result1))
        self.wait(1)

        quotient2 = MathTex("-2").next_to(quotient1,RIGHT)
        multiply2 = MathTex("-2x - 2").next_to(result1, DOWN)
        division_line2 = Line(divisor.get_right(), divisor.get_right() + RIGHT * 3.5).next_to(division_line1,DOWN*5)
        result2 = MathTex("+1").next_to(multiply2, DOWN).shift(RIGHT*0.5)
        self.play(Transform(Steps[0],Steps[2]))
        self.wait(3)
        self.play(Write(quotient2))
        self.wait(1)
        self.play(Transform(Steps[0],Steps[3]))
        self.wait(2)
        self.play(Write(multiply2))
        self.play(Write(division_line2),Write(result2))
        self.wait(1)
        self.play(Transform(Steps[0],Steps[4]))
        self.wait(1)
        multiline2 = MathTex("Quotient:3x-2","Remainder:1").arrange(DOWN, aligned_edge=LEFT).next_to(multiline1,DOWN).scale(0.65).shift(LEFT*0.5)
        self.play(Write(multiline2))
        self.wait(2)
        self.play(Transform(Steps[0],Steps[5]))
        self.wait(3)

    def Remainder_Theorem(self):
        self.angleChoice=[TAU/4,TAU/4]
        self.colorChoice=[BLUE,ORANGE,YELLOW]
        p15=cvo.CVO().CreateCVO("Remainder Theorem","").setPosition([-4.5,-2,0])
        p16=cvo.CVO().CreateCVO("Condition","if p(x) is any polynomial of degree $>= 1$ and p(x)/(x-a)").setPosition([-3,1,0])
        p17=cvo.CVO().CreateCVO("Result","Remainder is p(a)").setPosition([3,1,0])
        p17.setcircleradius(1.5)
        p15.cvolist.append(p16)
        p16.cvolist.append(p17)
        self.construct1(p15,p15)

    def Factorising(self):
        title = Text("Factorizing Using Sum and Product Method").scale(0.8).to_edge(UP)
        self.play(Write(title))
        example_text = MathTex("Expression:ax^2+bx+c").scale(0.75).next_to(title,DOWN)
        self.play(Write(example_text))
        steps = VGroup(
            MathTex("\\text{Step 1: Find two numbers p and q such that:}","p + q = b","p \\times q = a \\times c").arrange(DOWN, center=True),
            MathTex("\\text{Step 2: Rewrite the middle term bx using p and q:}","ax^2 + px + qx + c").arrange(DOWN, center=True),
            Text("Step 3: Factor by grouping", font_size=30).shift(LEFT*1)
        ).next_to(example_text, DOWN, buff=0.3).scale(0.75).set_color(YELLOW)
        
        example_steps = VGroup(
            MathTex("Example:3x^2+11x+6"),
            MathTex("3x^2 + 2x + 9x + 6"),
            MathTex("= x(3x + 2) + 3(3x + 2)"),
            MathTex("= (3x + 2)(x + 3)")
            ).arrange(DOWN, center=False, aligned_edge=LEFT).scale(0.75).move_to(LEFT*3+DOWN*1)
        
        steps_text = VGroup(
            Text("Let p = 2, q=9",font_size=28),
            MathTex("2 + 9 = 11"),
            MathTex("2 \\times 9 = 3 \\times 6 = 18"),
            Text("Rewrite 11x using 2 and 9",font_size=28)
            ).arrange(DOWN, center=False, aligned_edge=LEFT).scale(0.75).next_to(example_steps, RIGHT, buff=2)
        
        self.play(Write(example_steps[0]))
        
        self.play(Write(steps[0]))
        self.wait(3)

        self.play(Write(steps_text[0]))
        self.wait(1)
        self.play(Write(steps_text[1:3]))
        self.wait(3)

        self.play(Transform(steps[0],steps[1]))
        self.wait(3)
        self.play(Write(steps_text[3]))
        self.wait(2)

        self.play(Write(example_steps[1]))
        self.wait(2)

        self.play(Transform(steps[0],steps[2]))
        self.wait(1)
        
        self.play(Write(example_steps[2]))
        self.wait(2)

        self.play(Write(example_steps[3]))
        self.wait(2)

        final_text = MathTex("Factors=(3x+2)(x+3)").scale(0.75).next_to(example_steps,DOWN,buff=0.5)
        self.play(Write(final_text))
        self.wait(2)

    def Factor_Theorem(self):
        self.angleChoice=[TAU/4,TAU/4,TAU/4,TAU/4]
        self.colorChoice=[BLUE,ORANGE,YELLOW,YELLOW,ORANGE]
        p10=cvo.CVO().CreateCVO("Factor Theorem","").setPosition([-4,0,0])
        p11=cvo.CVO().CreateCVO("Condition","if (x-a) is a factor of polynomial p(x)").setPosition([0,2,0])
        p12=cvo.CVO().CreateCVO("Result","p(a) = 0").setPosition([3,2,0])
        p13=cvo.CVO().CreateCVO("Condition","if p(a) = 0").setPosition([0,-2,0])
        p14=cvo.CVO().CreateCVO("Result","(x-a) is a factor of polynomial p(x)").setPosition([3,-2,0])
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p10.cvolist.append(p13)
        p13.cvolist.append(p14)
        self.construct1(p10,p10)

    def Algebraic_Identities(self):
        title = Text("ALGEBRAIC IDENTITIES").scale(0.8).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        text = MathTex("\\text{Identitiy 1}:(x+y)^2 \equiv x^2+2xy+y^2").scale(0.65).next_to(title,DOWN*1.5)
        self.play(Write(text))
        self.wait(2)
        text1 = MathTex("\\text{Identitiy 2}:(x-y)^2 \equiv x^2-2xy+y^2").scale(0.65).next_to(text,DOWN)
        self.play(Write(text1))
        self.wait(2)
        text2 = MathTex("\\text{Identitiy 3}:(x+y)(x-y) \equiv x^2-y^2").scale(0.65).next_to(text1,DOWN)
        self.play(Write(text2))
        self.wait(2)
        text3 = MathTex("\\text{Identitiy 4}:(x+a)(x+b) \equiv x^2+(a+b)x+ab").scale(0.65).next_to(text2,DOWN)
        self.play(Write(text3))
        self.wait(2)
        text4 = MathTex("\\text{Identitiy 5}:(x+y+z)^2 \equiv x^2+y^2+z^2+2xy+2yz+2zx").scale(0.65).next_to(text3,DOWN)
        self.play(Write(text4))
        self.wait(2)
        text5 = MathTex("\\text{Identitiy 6}:(x+y)^3 \equiv x^3+y^3+3xy(x+y)").scale(0.65).next_to(text4,DOWN)
        self.play(Write(text5))
        self.wait(2)
        text6 = MathTex("\\text{Identitiy 7}:(x-y)^3 \equiv x^3-y^3-3xy(x-y)").scale(0.65).next_to(text5,DOWN)
        self.play(Write(text6))
        self.wait(2)
        text7 = MathTex("\\text{Identitiy 8}:(x+y+z)(x^2+y^2+z^2-xy-yz-xz) \equiv x^3+y^3+z^3-3xyz").scale(0.65).next_to(text6,DOWN)
        self.play(Write(text7))
        self.wait(3)

    def SetDeveloperList(self):
        self.DeveloperList="A.Sindhu sri"
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade9Chapter2PolynomialsandFactorising.py"


if __name__ == "__main__":
    scene = Polynomial()
    scene.render()
