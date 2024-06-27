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
        self.Remainder_theory()
        self.fadeOutCurrentScene()
        self.Factorising()
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
        self.angleChoice=[TAU/4,TAU/4,TAU/4]
        self.colorChoice=[BLUE,ORANGE,YELLOW,PURPLE]
        p10=cvo.CVO().CreateCVO("Degree of polynomial","highest degree among all the terms").setPosition([-4,1.5,0])
        p11=cvo.CVO().CreateCVO("Degree of term","Sum of exponents of its variable").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("Example","3x^2y^3 + 4xy + 7").setPosition([-1.5,-1,0])
        p12.SetIsMathText(True)
        p12.setcircleradius(1.5)
        p13=cvo.CVO().CreateCVO("Degree","5").setPosition([2,-1,0])
        p10.cvolist.append(p12)
        p12.cvolist.append(p13)
        self.construct1(p11,p11)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
    
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
        title = Text("Types of Polynomials(Based on Degree)").scale(0.8).to_edge(UP)
        self.play(Write(title))
        text1 = MathTex("\\text{1. Constant Polynomial}:p(x)=constant",
                        "Example:p(x)=3").arrange(DOWN, aligned_edge=LEFT).scale(0.65).shift(LEFT*2,UP*2)
        self.play(Write(text1))
        self.wait(2)
        text2 = MathTex("\\text{2. Linear Polynomial}:p(x)=ax+b;a \\neq 0",
                        "Example:p(x)= 2x + 1").arrange(DOWN, aligned_edge=LEFT).scale(0.65).next_to(text1,DOWN).shift(DOWN*0.25)
        self.play(Write(text2))
        self.wait(2)
        text3 = MathTex("\\text{3. Quadratic Polynomial}:p(x)=ax^2+bx+c;a \\neq 0",
                        "Example:p(x)=x^2 + x + 1").arrange(DOWN, aligned_edge=LEFT).scale(0.65).next_to(text2,DOWN).shift(RIGHT*0.75,DOWN*0.25)
        self.play(Write(text3))
        self.wait(2)
        text4 = MathTex("\\text{4. Cubic Polynomial}:p(x)=ax^3+bx^2+cx+d;a \\neq 0",
                        "Example:p(x)=x^3 - x^2 + 2").arrange(DOWN, aligned_edge=LEFT).scale(0.65).next_to(text3,DOWN).shift(DOWN*0.25)
        self.play(Write(text4))
        self.wait(2)

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
        text1 = MathTex("Monomial").scale(0.75).shift(LEFT*2,UP*1)
        self.play(Write(text1))
        text2 = MathTex("\\text{: no. of non-zero terms }").scale(0.75).next_to(text1,RIGHT)
        self.play(Write(text2))
        text3 = MathTex("=1").scale(0.75).next_to(text2,RIGHT)
        self.play(Write(text3))
        text4 = MathTex("Example:p(x)=x").scale(0.75).next_to(text1,DOWN).shift(RIGHT*1)
        self.play(Write(text4))
        self.wait(3)
        text5 = MathTex("Binomial").scale(0.75).shift(LEFT*2,UP*1)
        self.play(Transform(text1,text5))
        text6 = MathTex("=2").scale(0.75).next_to(text2,RIGHT)
        self.play(Transform(text3,text6))
        text7 = MathTex("Example:p(x)=x + 2").scale(0.75).next_to(text2,DOWN).shift(LEFT*1)
        self.play(Transform(text4,text7))
        self.wait(3)
        text8 = MathTex("Trinomial").scale(0.75).shift(LEFT*2,UP*1)
        self.play(Transform(text1,text8))
        text9 = MathTex("=3").scale(0.75).next_to(text2,RIGHT)
        self.play(Transform(text3,text9))
        text10 = MathTex("Example:p(x)=x^3 + 2x + 2").scale(0.75).next_to(text2,DOWN)
        self.play(Transform(text4,text10))
        self.wait(3)
        text11 = MathTex("Multinomial ").scale(0.75).shift(LEFT*2,UP*1)
        self.play(Transform(text1,text11))
        text12 = MathTex(">=3").scale(0.65).next_to(text2,RIGHT)
        self.play(Transform(text3,text12))
        text13 = MathTex("Example:p(x)=3x^3 + x^2 + 2x - 7").scale(0.75).next_to(text2,DOWN).shift(LEFT*0.5)
        self.play(Transform(text4,text13))
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

        Step1 = MathTex("\\text{Step 1: Divide } \\frac{3x^2}{x}=3x,","\\text{it becomes first term in quotient}").arrange(DOWN).scale(0.65).shift(UP*1,RIGHT*2).set_color(YELLOW)
        Step2 = MathTex("\\text{Step 2: Multiply } (x + 1)3x = 3x^2 + 3x").scale(0.65).shift(UP*1,RIGHT*2).set_color(YELLOW)
        Step3 = MathTex("\\text{Step 3: Divide }\\frac{-2x}{x}=-2,","\\text{it becomes second term in quotient}").arrange(DOWN).scale(0.65).shift(UP*1,RIGHT*2).set_color(YELLOW)
        Step4 = MathTex("\\text{Step 4: Multiply } (x + 1)-2 = -2x - 2").scale(0.65).shift(UP*1,RIGHT*2).set_color(YELLOW)
        Step5 = MathTex("\\text{Step 5: We stop here as the }","\\text{remainder is 1, a constant}").arrange(DOWN).scale(0.65).shift(UP*1,RIGHT*2).set_color(YELLOW)
        Note = Text("The division process is said to be complete \n if we get the remainder 0 or the \n degree of the remainder is less than\n the degree of the divisor",font_size=25).shift(RIGHT*2,UP*1).set_color(YELLOW)
        divisor = MathTex("x + 1").to_edge(LEFT).shift(UP*1.5)
        dividend = MathTex("3x^2 + x - 1").next_to(divisor, RIGHT)
        division_line = Line(divisor.get_right(), divisor.get_right() + RIGHT * 3.5).shift(UP*0.3,RIGHT*0.2)
        division_linev = Line(divisor.get_right(), divisor.get_right() + DOWN * 1).shift(UP*0.3,RIGHT*0.2)
        self.play(Write(multiline1))
        self.play(Write(divisor), Write(division_line), Write(dividend.shift(RIGHT*0.25)),Write(division_linev))
        self.wait(1)
        self.play(FadeIn(Step1))
        self.wait(3)

        quotient1 = MathTex("3x").next_to(division_line, UP, aligned_edge=LEFT)
        multiply1 = MathTex("-3x^2 + 3x").next_to(dividend, DOWN).shift(LEFT*0.15)
        division_line1 = Line(divisor.get_right(), divisor.get_right() + RIGHT * 3.5).next_to(division_line,DOWN*5.5)
        result1 = MathTex("-2x - 1").next_to(multiply1, DOWN).shift(RIGHT*1)
        self.play(Write(quotient1))
        self.wait(1)
        self.play(Transform(Step1,Step2))
        self.wait(3)
        self.play(Write(multiply1))
        self.wait(1)
        self.play(Write(division_line1),Write(result1))
        self.wait(1)

        quotient2 = MathTex("-2").next_to(quotient1,RIGHT)
        multiply2 = MathTex("-2x - 2").next_to(result1, DOWN)
        division_line2 = Line(divisor.get_right(), divisor.get_right() + RIGHT * 3.5).next_to(division_line1,DOWN*5)
        result2 = MathTex("+1").next_to(multiply2, DOWN).shift(RIGHT*0.5)
        self.play(Transform(Step1,Step3))
        self.wait(2)
        self.play(Write(quotient2))
        self.wait(1)
        self.play(Transform(Step1,Step4))
        self.wait(2)
        self.play(Write(multiply2))
        self.play(Write(division_line2),Write(result2))
        self.wait(1)
        self.play(Transform(Step1,Step5))
        self.wait(1)
        multiline2 = MathTex("Quotient:3x-2","Remainder:1").arrange(DOWN, aligned_edge=LEFT).next_to(multiline1,DOWN).scale(0.65).shift(LEFT*0.5)
        self.play(Write(multiline2))
        self.wait(2)
        self.play(Transform(Step1,Note))
        self.wait(3)

    def Remainder_theory(self):
        self.angleChoice=[TAU/4,TAU/4,TAU/4]
        self.colorChoice=[BLUE,ORANGE,YELLOW]
        p15=cvo.CVO().CreateCVO("Remainder Theory","").setPosition([-4.5,-2,0])
        p16=cvo.CVO().CreateCVO("condition","if p(x) is any polynomial of degree $>= 1$ and p(x)/(x-a)").setPosition([-3,1,0])
        p17=cvo.CVO().CreateCVO("Result","Remainder is p(a)").setPosition([3,1,0])
        p17.setcircleradius(1.5)
        p15.cvolist.append(p16)
        p16.cvolist.append(p17)
        self.construct1(p15,p15)

    def Factorising(self):
        title = Text("Factorizing Using Sum and Product Method").scale(0.8).to_edge(UP)
        self.play(Write(title))
        text = MathTex("Expression:ax^2+bx+c").scale(0.65).next_to(title,DOWN)
        self.play(Write(text))
        text1 = MathTex("\\text{Find p and q such that } p+q=b , p \\times q= a \\times c").scale(0.65).next_to(text,DOWN)
        self.play(Write(text1))
        self.wait(2)
        text2 = MathTex("Example:3x^2+11x+6").scale(0.65).next_to(text1,DOWN).shift(LEFT*4,DOWN*1)
        self.play(Write(text2))
        text3 = MathTex("\\text{Let } p=2,q=9",
                        "\\text{as } p+q=b \\Rightarrow 2+9=11",
                        "\\text{as } p \\times q= a \\times c \\Rightarrow 2 \\times 9= 18").arrange(DOWN).scale(0.65).next_to(text2,RIGHT).shift(RIGHT*2,DOWN*1)
        self.play(Write(text3))
        self.wait(3)
        text4 = MathTex("=3x^2+2x+9x+6").scale(0.65).next_to(text2,DOWN).shift(RIGHT*1)
        self.play(Write(text4))
        self.wait(2)
        text5 = MathTex("=x(3x+2)+3(3x+2)").scale(0.65).next_to(text4,DOWN)
        self.play(Write(text5))
        self.wait(3)
        text6 = MathTex("Factors=(3x+2)(x+3)").scale(0.65).next_to(text5,DOWN).shift(LEFT*1,DOWN*0.5)
        self.play(Write(text6))
        self.wait(2)

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
        self.DeveloperList="Sindhu"
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Polynomial.py"


if __name__ == "__main__":
    scene = Polynomial()
    scene.render()
