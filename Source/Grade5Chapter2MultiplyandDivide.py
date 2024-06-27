import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class MultiplyandDivide(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Multiplication()
        self.Mul_examples()
        self.Pattern_in_Mul()
        self.Division()
        self.Components_of_div()
        self.Div_examples()
        self.Div_formula_check()
        self.Inverse_operation()
        self.GithubSourceCodeReference()

    def Multiplication(self):
        self.angleChoice=[TAU/4]
        p10=cvo.CVO().CreateCVO("Multiplication","").setPosition([-3,0,0])
        p11=cvo.CVO().CreateCVO("Symbol","$\\times$").setPosition([3,0,0])
        p10.cvolist.append(p11)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Mul_examples(self):
        text=Text("Multiplication").scale(0.8).to_edge(UP)
        self.play(Write(text))
        text1=MathTex("\\text{Example :}135\\times 61").scale(0.75).next_to(text,DOWN).shift(LEFT*3.5)
        self.play(Write(text1))
        var1 = MathTex("135").shift(UP*2)
        var2 = MathTex("61").next_to(var1, DOWN)
        sign = MathTex("\\times").next_to(var2, LEFT)
        line = Line(var2.get_right(), var2.get_right() + RIGHT * 2).shift(DOWN*0.5,LEFT*1.5)
        self.play(Write(var1),Write(var2),Write(sign),Write(line))

        var3 = MathTex("135","\\Leftarrow","135 \\times 1").next_to(line, DOWN).shift(RIGHT*1.5)
        self.play(Write(var3))
        self.wait(2)

        var4 = MathTex("\\Leftarrow","135 \\times 6").next_to(var3, DOWN).shift(RIGHT*0.75)
        var5 = MathTex("0").next_to(var4,RIGHT).shift(LEFT*0.15).set_color(PINK)
        self.play(FadeIn(var4,var5))

        curved_arrow = CurvedArrow(RIGHT*3.25,RIGHT*0.5, angle=-PI/4).shift(DOWN*0.5)
        self.play(Create(curved_arrow))
        var9 = MathTex("0").next_to(var4,LEFT).shift(LEFT*0.25)
        self.play(Write(var9))

        var6 = MathTex("135 \\times 6","\\Rightarrow").next_to(var9,LEFT).shift(LEFT*1.5)
        self.play(Write(var6))

        var7 = MathTex("810").next_to(var9, LEFT).shift(RIGHT*0.15)
        self.play(Write(var7))
        self.play(FadeOut(curved_arrow,var6))

        sign1 = MathTex("+").next_to(var7, LEFT)
        line1 = Line(var2.get_right(), var2.get_right() + RIGHT * 2).shift(DOWN*2,LEFT*1.5)
        self.play(Write(sign1),Write(line1))

        var8 =  MathTex("8235").next_to(line1, DOWN).shift(RIGHT*0.15)
        line2 = Line(var2.get_right(), var2.get_right() + RIGHT * 2).shift(DOWN*3,LEFT*1.5)
        self.play(Write(var8),Write(line2))
        self.wait(2)
        self.fadeOutCurrentScene()

        text1=MathTex("\\text{Example :}243\\times 163").scale(0.75).next_to(text,DOWN).shift(LEFT*3.5)
        self.play(Write(text1))
        var1 = MathTex("243").shift(UP*2)
        var2 = MathTex("163").next_to(var1, DOWN)
        sign = MathTex("\\times").next_to(var2, LEFT)
        line = Line(var2.get_right(), var2.get_right() + RIGHT * 2).shift(DOWN*0.5,LEFT*1.5)
        self.play(Write(var1),Write(var2),Write(sign),Write(line))

        var3 = MathTex("729","\\Leftarrow","243 \\times 3").next_to(line, DOWN).shift(RIGHT*1.5)
        self.play(Write(var3))
        self.wait(2)

        var4 = MathTex("\\Leftarrow","243 \\times 6").next_to(var3, DOWN).shift(RIGHT*0.75)
        var5 = MathTex("0").next_to(var4,RIGHT).shift(LEFT*0.15).set_color(PINK)
        self.play(FadeIn(var4,var5))

        curved_arrow = CurvedArrow(RIGHT*3.25,RIGHT*0.5, angle=-PI/4).shift(DOWN*0.5)
        self.play(Create(curved_arrow))
        var9 = MathTex("0").next_to(var4,LEFT).shift(LEFT*0.25)
        self.play(Write(var9))

        var6 = MathTex("243 \\times 6","\\Rightarrow").next_to(var9,LEFT).shift(LEFT*1.5)
        self.play(Write(var6))

        var7 = MathTex("1458").next_to(var9, LEFT).shift(RIGHT*0.15)
        self.play(Write(var7))
        self.play(FadeOut(curved_arrow,var6))

        var10 = MathTex("\\Leftarrow","243 \\times 1").next_to(var4, DOWN)
        var11 = MathTex("00").next_to(var10,RIGHT).shift(LEFT*0.15).set_color(PINK)
        self.play(FadeIn(var10,var11))

        curved_arrow1 = CurvedArrow(RIGHT*3.25,RIGHT*0.5, angle=-PI/4).shift(DOWN*1)
        self.play(Create(curved_arrow1))
        var12 = MathTex("00").next_to(var10,LEFT).shift(LEFT*0.25)
        self.play(Write(var12))

        var13 = MathTex("243 \\times 1","\\Rightarrow").next_to(var12,LEFT).shift(LEFT*1.5)
        self.play(Write(var13))

        var14 = MathTex("243").next_to(var12, LEFT).shift(RIGHT*0.15)
        self.play(Write(var14))
        self.play(FadeOut(curved_arrow1,var13))

        sign1 = MathTex("+").next_to(var14, LEFT)
        line1 = Line(var2.get_right(), var2.get_right() + RIGHT * 2).shift(DOWN*2.5,LEFT*1.5)
        self.play(Write(sign1),Write(line1))

        var8 =  MathTex("39609").next_to(line1, DOWN).shift(RIGHT*0.15)
        line2 = Line(var2.get_right(), var2.get_right() + RIGHT * 2).shift(DOWN*3.5,LEFT*1.5)
        self.play(Write(var8),Write(line2))
        self.wait(2)
        self.fadeOutCurrentScene()
    
    def Pattern_in_Mul(self):
        text = Text("Q) If a box contains 200 chocolates , then").scale(0.75).to_edge(UP)
        text1 = Text("2 boxes contains = ").scale(0.75).shift(UP*2,LEFT*1)
        ans1 = MathTex("200 \\times 2 = 400").scale(0.75).next_to(text1,RIGHT)
        text2 = Text("3 boxes contains = ").scale(0.75).next_to(text1,DOWN).shift(DOWN*0.5)
        ans2 = MathTex("200 \\times 3 = 600").scale(0.75).next_to(text2,RIGHT)
        text3 = Text("4 boxes contains = ").scale(0.75).next_to(text2,DOWN).shift(DOWN*0.5)
        ans3 = MathTex("200 \\times 4 = 800").scale(0.75).next_to(text3,RIGHT)
        text4 = Text("5 boxes contains = ").scale(0.75).next_to(text3,DOWN).shift(DOWN*0.5)
        ans4 = MathTex("200 \\times 5 = 1000").scale(0.75).next_to(text4,RIGHT)
        curved_arrow = CurvedArrow(UP*2,UP*1, angle=-PI/4).shift(RIGHT*4)
        diff = MathTex("+ 200").scale(0.75)
        self.play(Write(text))
        self.wait(1)
        self.play(FadeIn(text1))
        self.wait(1)
        self.play(Write(ans1))
        self.play(FadeIn(text2))
        self.wait(1)
        self.play(Write(ans2))
        self.play(FadeIn(text3))
        self.wait(1)
        self.play(Write(ans3))
        self.play(FadeIn(text4))
        self.wait(1)
        self.play(Write(ans4))
        pattern_text=Text("Observe the PATTERN").scale(0.75).to_edge(DOWN).shift(UP*0.75)
        self.play(Write(pattern_text))
        self.play(Create(curved_arrow))
        self.play(Write(diff.next_to(ans1,RIGHT).shift(DOWN*0.5,RIGHT*0.75)))
        self.play(Create(curved_arrow.shift(DOWN*1.25)))
        self.play(Write(diff.next_to(ans2,RIGHT).shift(DOWN*0.5,RIGHT*0.75)))
        self.play(Create(curved_arrow.shift(DOWN*1.5)))
        self.play(Write(diff.next_to(ans3,RIGHT).shift(DOWN*0.5,RIGHT*0.75)))
        self.fadeOutCurrentScene()

    def Division(self):
        self.angleChoice=[TAU/4]
        p10=cvo.CVO().CreateCVO("Division","").setPosition([-3,0,0])
        p11=cvo.CVO().CreateCVO("Symbol","$\div$").setPosition([3,0,0])
        p10.cvolist.append(p11) 
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Components_of_div(self):
        self.angleChoice=[TAU/4,TAU/4,TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Division","").setPosition([-3,0,0])
        p11=cvo.CVO().CreateCVO("Dividend","").setPosition([0.5,2.5,0])
        p12=cvo.CVO().CreateCVO("Divisor","").setPosition([3,2,0])
        p13=cvo.CVO().CreateCVO("Quotient","").setPosition([3,-2.5,0])
        p14=cvo.CVO().CreateCVO("Remainder","").setPosition([0.5,-2.5,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14) 
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Div_examples(self):
        text = MathTex("\\text{Example : } 8 \div 3").to_edge(UP)
        self.play(Write(text))
        # Parameters
        num_circles = 8
        circle_radius = 0.35
        circle_color = BLUE
        circle_fill_opacity = 0.5

        # Positioning parameters for circles
        start_pos = LEFT * 3 + UP
        h_spacing = 1.5 # horizontal spacing
        v_spacing = 1.5  # vertical spacing

        # Create and position the circles
        circles = VGroup()
        for i in range(num_circles):
            circle = Circle(radius=circle_radius, color=circle_color, fill_opacity=circle_fill_opacity)
            if i < 3:  # First row
                circle.move_to(start_pos + RIGHT * h_spacing * i)
            elif i < 6:  # Second row
                circle.move_to(start_pos + DOWN * v_spacing + RIGHT * h_spacing * (i - 3))
            else:  # Third row
                circle.move_to(start_pos + DOWN * v_spacing * 2 + RIGHT * h_spacing * (i - 6))
            circles.add(circle)

        self.play(FadeIn(circles))

        # Parameters for rectangles
        rectangles = [
            {"width": 1.15, "height": 4.25, "shift": LEFT * 3 + DOWN * 0.5},
            {"width": 1.15, "height": 4.25, "shift": LEFT * 1.5 + DOWN * 0.5}
        ]
        rect_color = ORANGE

        # Create and position the rectangles
        rects = VGroup()
        for rect_params in rectangles:
            rect = Rectangle(width=rect_params["width"], height=rect_params["height"]).shift(rect_params["shift"]).set_color(rect_color)
            rects.add(rect)

        self.play(Create(rects))

        self.wait(2)

        quotient_in_circles = MathTex("3\\times 2").shift(UP*2,LEFT*2).set_color(YELLOW)
        # self.play(Write(quotient_in_circles))
        remainder_in_circles = MathTex("2").next_to(quotient_in_circles,RIGHT,buff=1.5).set_color(PURE_RED)
        # self.play(Write(remainder_in_circles))
        multiline1 = MathTex("Dividend:8", "Divisor:3").arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT).scale(0.65).shift(UP*3,LEFT*0.5).set_color(YELLOW)
        self.play(Write(multiline1))
        dividend = MathTex("8").to_edge(RIGHT).shift(LEFT*3)
        divisor = MathTex("3").next_to(dividend, LEFT).shift(LEFT*0.25)
        division_line = Line(divisor.get_right(), divisor.get_right() + RIGHT * 1.25).shift(UP*0.3,RIGHT*0.2)
        division_linev = Line(divisor.get_right(), divisor.get_right() + DOWN * 1).shift(UP*0.3,RIGHT*0.2)
        quotient = MathTex("2").next_to(division_line, UP).shift(LEFT*0.25)
        multiply1 = MathTex("6").next_to(dividend, DOWN)
        division_line1 = Line(divisor.get_right(), divisor.get_right() + RIGHT * 1.25).next_to(division_line,DOWN*4.95)
        remainder = MathTex("2").next_to(multiply1, DOWN)
        self.play(Write(divisor), Write(division_line), Write(dividend),Write(division_linev))
        self.wait(2)
        self.play(FadeIn(quotient_in_circles))
        self.play(Write(quotient))
        self.wait(1)
        self.play(Write(multiply1),Write(division_line1))
        self.wait(1)
        self.play(FadeIn(remainder_in_circles))
        self.wait(1)
        self.play(Write(remainder))
        self.wait(1)
        multiline2 = MathTex("Quotient:2","Remainder:2").arrange(DOWN, aligned_edge=LEFT).next_to(multiline1,DOWN).scale(0.65).shift(0.25).set_color(YELLOW)
        self.play(Write(multiline2))
        self.wait(2)
        text1 = Text("3 divides 8, resulting in a \n quotient of 2 and a remainder of 2.").to_edge(RIGHT).shift(DOWN*2.5,RIGHT*1).scale(0.5)
        self.play(Write(text1))
        self.wait(2)
        self.fadeOutCurrentScene()


        example = MathTex("\\text{Example : } 1440 \div 3").to_edge(UP).shift(LEFT*2)
        self.play(Write(example))
        multiline1 = MathTex("Dividend:1440", "Divisor:3").arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT).scale(0.65).shift(UP*3,LEFT*1).set_color(YELLOW)
        dividend = MathTex("1440").shift(LEFT*4.5,UP*1.5)
        divisor = MathTex("3").next_to(dividend, LEFT).shift(LEFT*0.25)
        division_line = Line(divisor.get_right(), divisor.get_right() + RIGHT * 2).shift(UP*0.3,RIGHT*0.2)
        division_linev = Line(divisor.get_right(), divisor.get_right() + DOWN * 0.65).shift(UP*0.3,RIGHT*0.2)
        quotient1 = MathTex("4").next_to(division_line, UP,aligned_edge=LEFT)
        multiply1 = MathTex("12").next_to(dividend, DOWN).shift(LEFT*0.25)
        sign1 = MathTex("-").next_to(multiply1,LEFT)
        division_line1 = Line(divisor.get_right(), divisor.get_right() + RIGHT * 2).next_to(division_line,DOWN*4.95)
        result1 = MathTex("2").next_to(multiply1, DOWN).shift(RIGHT*0.15)
        quotient2 = MathTex("8").next_to(quotient1,RIGHT).shift(LEFT*0.15)
        dropdown1 = MathTex("4").next_to(result1, RIGHT).shift(LEFT*0.15)
        multiply2 = MathTex("24").next_to(result1, DOWN).shift(RIGHT*0.15)
        sign2 = MathTex("-").next_to(multiply2,LEFT)
        division_line2 = Line(divisor.get_right(), divisor.get_right() + RIGHT * 2).next_to(division_line1,DOWN*5)
        result2 = MathTex("0").next_to(multiply2, DOWN).shift(RIGHT*0.25,DOWN*0.25)
        dropdown2 = MathTex("0").next_to(result2, RIGHT).shift(LEFT*0.15)
        multiply3 = MathTex("0").next_to(dropdown2, DOWN)
        sign3 = MathTex("-").next_to(multiply3,LEFT)
        quotient3 = MathTex("0").next_to(quotient2,RIGHT).shift(LEFT*0.15)
        division_line3 = Line(divisor.get_right(), divisor.get_right() + RIGHT * 2).next_to(division_line2,DOWN*5)
        result3 = MathTex("0").next_to(multiply3, DOWN)
        multiline2 = MathTex("Quotient:480","Remainder:0").arrange(DOWN, aligned_edge=LEFT).next_to(multiline1,DOWN).scale(0.65).set_color(YELLOW)
        text1 = MathTex("\\text{Find multiple of 3 that is }<= 14","3\\times 4=12").arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT).scale(0.75).shift(UP*1.5)
        # self.play(Write(text1))
        text2 = MathTex("\\text{Subtract 12 from 14 }").next_to(text1,DOWN).scale(0.75).shift(LEFT*1)
        
        rule_text = Text("RULES").shift(RIGHT*1).scale(0.75)
        rule1 = MathTex("\\text{1. If we subtract and get a greater value than divisor,}",
                        "\\text{then the partial quotient isn't great enough}").arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT).scale(0.75).shift(DOWN*1,RIGHT*1.85).set_color(ORANGE)
        rule2 = MathTex("\\text{2. After every subtraction, we need to compare ",
                        "\\text{the results to the divisor to continue dividing}").arrange(DOWN, aligned_edge=LEFT).next_to(rule1,DOWN).shift(LEFT*0.5).scale(0.75).set_color(ORANGE)

        text3 = MathTex("\\text{As 2}< 3",
                        "\\text{Drop down the next digit 4}").arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT).scale(0.75).shift(UP*1.5)
        text4 = MathTex("\\text{Find multiple of 3 that is }<= 24",
                        "3\\times 8=24").arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT).scale(0.75).shift(UP*1.5)
        text5 = MathTex("\\text{Drop down the next digit 0}").to_edge(RIGHT).scale(0.75).shift(UP*1.5)

        self.play(Write(divisor), Write(division_line), Write(dividend),Write(division_linev))
        self.play(Write(multiline1))
        self.wait(2)
        self.play(Write(text1))
        self.wait(1)
        self.play(Write(quotient1))
        self.wait(1)
        self.play(Write(multiply1),Write(division_line1),Write(sign1))
        self.wait(1)
        self.play(Write(text2))
        self.wait(1)
        self.play(FadeOut(text2))
        self.play(Write(result1))
        self.wait(1)
        self.play(Write(rule_text),Write(rule1))
        self.wait(3)
        self.play(Transform(text1,text3))
        self.wait(2)
        self.play(Write(dropdown1))
        self.wait(2)
        self.play(Write(rule2))
        self.wait(3)
        self.play(Transform(text1,text4))
        self.wait(2)
        self.play(Write(quotient2))
        self.wait(1)
        self.play(Write(multiply2),Write(division_line2),Write(sign2))
        self.wait(1)
        self.play(Write(result2))
        self.wait(1)
        self.play(Transform(text1,text5))
        self.play(Write(dropdown2))
        self.wait(1)
        self.play(Write(quotient3))
        self.wait(1)
        self.play(Write(multiply3),Write(division_line3),Write(sign3))
        self.wait(1)
        self.play(Write(result3))
        self.wait(1)
        self.play(FadeOut(text1))
        self.play(Write(multiline2))
        self.wait(2)
        self.fadeOutCurrentScene()

    def Div_formula_check(self):
        title = MathTex("\\text{Check with Division Formula}").to_edge(UP)
        self.play(Write(title))
        text = MathTex("Dividend=(Quotient\\times Divisor)+Remainder").next_to(title,DOWN)
        self.play(Write(text))
        multiline1 = MathTex("Dividend:1440","Divisor:3","Quotient:480","Remainder:0").arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT).scale(0.75).set_color(YELLOW)
        self.play(Write(multiline1))
        text1 = MathTex("\\text{Dividend = }","(480\\times 3)+ 0").shift(RIGHT*1)
        self.play(Write(text1))
        text2 = MathTex("1440 = 1440").next_to(text1,DOWN)
        self.play(Write(text2))
        self.wait(2)
        self.fadeOutCurrentScene()

    def Inverse_operation(self):
        text = MathTex("\\text{Finding value of n with an INVERSE OPERATION}").to_edge(UP)
        self.play(Write(text))
        text1 = MathTex("4\\times 50 = 200").shift(UP*1.5)
        self.play(Write(text1))
        self.wait(1)
        text2 = MathTex("n\div 4=50","n=4\\times 50","n=200").arrange(DOWN, aligned_edge=LEFT)
        self.play(Write(text2))
        self.wait(2)
        self.play(FadeOut(text2))
        text1 = MathTex("200\div 4 = 50").next_to(text1,DOWN)
        self.play(FadeIn(text1))
        self.fadeOutCurrentScene()

    def SetDeveloperList(self):
        self.DeveloperList="Sindhu"
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="MultiplyandDivide.py"

              
if __name__ == "__main__":
    scene = MultiplyandDivide()
    scene.render()