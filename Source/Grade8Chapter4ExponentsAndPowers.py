import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo

class Exponents(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.ExpForm()
        self.fadeOutCurrentScene()
        self.ExponentFormAnim()
        self.fadeOutCurrentScene()
        self.ExpEx()
        self.fadeOutCurrentScene()
        self.PowersTextExamples()
        self.fadeOutCurrentScene()
        self.ExpNegPower()
        self.fadeOutCurrentScene()
        self.NegativePowerExample()
        self.fadeOutCurrentScene()
        self.NegativePowerTextExamples()
        self.fadeOutCurrentScene()
        self.Law1()
        self.fadeOutCurrentScene()
        self.Law1TextExamples()
        self.fadeOutCurrentScene()
        self.Law2()
        self.fadeOutCurrentScene()
        self.Law2TextExamples()
        self.fadeOutCurrentScene()
        self.Law3()
        self.fadeOutCurrentScene()
        self.Law3TextExamples()
        self.fadeOutCurrentScene()
        self.Law4()
        self.fadeOutCurrentScene()
        self.Law4TextExamples()
        self.fadeOutCurrentScene()
        self.Law5()
        self.fadeOutCurrentScene()
        self.Law5TextExamples()
        self.fadeOutCurrentScene()
        self.ExpConversion()
        self.fadeOutCurrentScene()
        self.ExpComparison()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        


    def ExpForm(self):
        self.isRandom = False
        self.angleChoice = [TAU/2,TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Mathematics Exponents","").setPosition([-4,2,0])
        p11=cvo.CVO().CreateCVO("Exponent Form ", "$a^n$").setPosition([-4,-2,0])
        p12=cvo.CVO().CreateCVO("Base", "a").setPosition([3,2,0])
        p13=cvo.CVO().CreateCVO("Power", "n").setPosition([3,-0.5,0])
       
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
        self.construct1(p10,p10)

    def ExponentFormAnim(self):
        title = Text(" Exponent Form Example : ",font_size = 30).shift(UP*3+LEFT*4)
        self.play(Write(title))
        base = Text("10", font_size=72)
        exponent = Text("9", font_size=36).next_to(base, UR, buff=0.1)
        
        # Create a square around the base and exponent
        square = Square(side_length=2.5,color=BLUE).move_to(base)
        
        # Create the power and base labels
        power_label = Text("Power", font_size=30,color=ORANGE).next_to(square, LEFT, buff=1.2)
        base_label = Text("Base", font_size=30,color=YELLOW).next_to(square, UP*0.6, buff=1.2)
        exponent_label = Text("Exponent", font_size=30,color=BLUE).next_to(exponent, RIGHT, buff=0.8)
        
        # Add larger arrows
        arrow_config = {"stroke_width": 5, "tip_length": 0.2}
        power_arrow = Arrow(power_label.get_right(), square.get_left(), buff=0.1, **arrow_config)
        base_arrow = Arrow(base_label.get_bottom()*0.8, square.get_center(), buff=0.1, **arrow_config).shift(UP*0.2)
        exponent_arrow = Arrow(exponent_label.get_left(), exponent.get_right(), buff=0.1, **arrow_config)
        read = Tex("We read " + "$10^9$" + "as 10 raised to the power of 9",font_size = 45).shift(DOWN*2+LEFT*2)
        
        # Add elements to the scene
        self.play(Create(square))
        self.wait(1)
        self.play(Write(base))
        self.play(Write(exponent))
        
        self.wait(1)
        self.play(Write(read))
        self.wait(1.5)
        
        self.play(Create(base_arrow))
        self.wait(1)
        self.play(Write(base_label))
        self.play(Create(exponent_arrow))
        self.wait(1)
        self.play(Write(exponent_label))
        self.play(Create(power_arrow))
        self.wait(1)
        self.play(Write(power_label))

        # Pause to view the final result
        self.wait(2)

    def ExpEx(self):
        self.isRandom = False
        p11=cvo.CVO().CreateCVO("Exponents Example ", "$2^3$").setPosition([-4,0, 0]).setangle(-TAU/4) 
        p12=cvo.CVO().CreateCVO("Base", "2").setPosition([3,2,0]).setangle(-TAU/4)
        p13=cvo.CVO().CreateCVO("Power", "3").setPosition([3, 0, 0]).setangle(-TAU/4)

        p14=cvo.CVO().CreateCVO("Result", "2*2*2 = 8").setPosition([3,-2, 0]).setangle(-TAU/4)
        
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
        p11.cvolist.append(p14)
        self.construct1(p11,p11)
    def ExpNegPower(self):
        self.isRandom = False
        p11 = cvo.CVO().CreateCVO("Negative Power", "$a^{-n}$").setPosition([-4,0, 0]).setangle(-TAU/4) 
        p12 = cvo.CVO().CreateCVO("Base", "a").setPosition([3,2.5,0]).setangle(-TAU/4)
        p13 = cvo.CVO().CreateCVO("Power", "-n").setPosition([3, 0.5, 0]).setangle(-TAU/4)
        p14 = cvo.CVO().CreateCVO("Result", "$1/a^n$").setPosition([3,-2, 0]).setangle(-TAU/4)
        #p15 = cvo.CVO().CreateCVO("Example", "$2^{-3}$").setPosition([0, -2, 0]).setangle(-TAU/3)
        #p16 = cvo.CVO().CreateCVO("Result", "$\\frac{1}{2^3} = \\frac{1}{8}$").setPosition([3,-2,0]).setangle(TAU/3)
        p14.setcircleradius(1.5)
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
        p11.cvolist.append(p14)
        #p14.cvolist.append(p15)
        #p15.cvolist.append(p16)

        self.construct1(p11, p11)
    def PowersTextExamples(self):
        examples_title = MathTex("Examples : ", font_size=50).shift(LEFT*5 +UP*3)
        self.play(Write(examples_title))
        self.wait(1)
        
        # Example 1
        sn01 = MathTex(r"1.", font_size=50).shift(LEFT*5 + UP*1.9)
        equall = Tex("=", font_size=50).shift(LEFT*3 + UP*1.9)
        self.play(Write(sn01))
        eg1 = MathTex(r"3^4", font_size=50, color=GREEN).shift(LEFT*4 + UP*2)
        self.wait(1)
        self.play(Write(eg1))
        self.wait(1)
        self.play(Write(equall))
        components = [
            MathTex(r"3", font_size=50, color=GREEN),
            MathTex(r"\times", font_size=50, color=WHITE),
            MathTex(r"3", font_size=50, color=GREEN),
            MathTex(r"\times", font_size=50, color=WHITE),
            MathTex(r"3", font_size=50, color=GREEN),
            MathTex(r"\times", font_size=50, color=WHITE),
            MathTex(r"3", font_size=50, color=GREEN)
        ]
        spacing = 0.7
        for i, component in enumerate(components):
            component.shift(LEFT * (2 - i*spacing) + UP * 1.9)
        for component in components:
            self.play(Write(component))
        equall2 = Tex("=", font_size=50).shift(RIGHT*3 + UP*1.9)
        self.play(Write(equall2))
        self.wait(1)
        result = Tex("81", font_size=50, color=GREEN).shift(RIGHT*4 + UP*1.9)
        self.play(Write(result))
        self.wait(2)
        
        # Example 2
        sn02 = MathTex(r"2.", font_size=50).shift(LEFT*5 + UP*0.4)
        equall = Tex("=", font_size=50).shift(LEFT*3 + UP*0.4)
        self.play(Write(sn02))
        eg2 = MathTex(r"2^3", font_size=50, color=BLUE).shift(LEFT*4 + UP*0.5)
        self.wait(1)
        self.play(Write(eg2))
        self.wait(1)
        self.play(Write(equall))
        components = [
            MathTex(r"2", font_size=50, color=BLUE),
            MathTex(r"\times", font_size=50, color=WHITE),
            MathTex(r"2", font_size=50, color=BLUE),
            MathTex(r"\times", font_size=50, color=WHITE),
            MathTex(r"2", font_size=50, color=BLUE)
        ]
        for i, component in enumerate(components):
            component.shift(LEFT * (2 - i*spacing) + UP * 0.4)
        for component in components:
            self.play(Write(component))
        equall2 = Tex("=", font_size=50).shift(RIGHT*3 + UP*0.4)
        self.play(Write(equall2))
        self.wait(1)
        result = Tex("8", font_size=50, color=BLUE).shift(RIGHT*4 + UP*0.4)
        self.play(Write(result))
        self.wait(2)

        # Example 3
        sn03 = MathTex(r"3.", font_size=50).shift(LEFT*5 + DOWN*1.1)
        equall = Tex("=", font_size=50).shift(LEFT*3 + DOWN*1.1)
        self.play(Write(sn03))
        eg3 = MathTex(r"4^2", font_size=50, color=RED).shift(LEFT*4 + DOWN*1)
        self.wait(1)
        self.play(Write(eg3))
        self.wait(1)
        self.play(Write(equall))
        components = [
            MathTex(r"4", font_size=50, color=RED),
            MathTex(r"\times", font_size=50, color=WHITE),
            MathTex(r"4", font_size=50, color=RED)
        ]
        for i, component in enumerate(components):
            component.shift(LEFT * (2 - i*spacing) + DOWN * 1.1)
        for component in components:
            self.play(Write(component))
        equall2 = Tex("=", font_size=50).shift(RIGHT*3 + DOWN*1.1)
        self.play(Write(equall2))
        self.wait(1)
        result = Tex("16", font_size=50, color=RED).shift(RIGHT*4 + DOWN*1.1)
        self.play(Write(result))
        self.wait(2)

    def NegativePowerExample(self):
        self.isRandom = False
        p11=cvo.CVO().CreateCVO("Negative Power Example ", "$2^{-3}$").setPosition([-4,0, 0]).setangle(-TAU/4) 
        p12=cvo.CVO().CreateCVO("Base", "2").setPosition([3,2,0]).setangle(-TAU/4)
        p13=cvo.CVO().CreateCVO("Power", "-3").setPosition([3, 0, 0]).setangle(-TAU/4)

        p14=cvo.CVO().CreateCVO("Result", "$\\frac{1}{2^3} = \\frac{1}{8}$").setPosition([3,-2, 0]).setangle(-TAU/4)
        
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
        p11.cvolist.append(p14)
        self.construct1(p11,p11)
    
    def NegativePowerTextExamples(self):
        examples_title = Text("Negative Power Examples : ", font_size=36).shift(LEFT*3.5 + UP*3)
        self.play(Write(examples_title))
        self.wait(1)
        
        # Example 1: Negative exponent (-1)
        sn01 = MathTex(r"1.", font_size=50).shift(LEFT*5 + UP*1.9)
        equall1 = Tex("=", font_size=50).shift(LEFT*3 + UP*1.9)
        self.play(Write(sn01))
        eg1 = MathTex(r"10^{-1}", font_size=50, color=GREEN).shift(LEFT*4 + UP*2)
        self.wait(1)
        self.play(Write(eg1))
        self.wait(1)
        self.play(Write(equall1))
        result1 = MathTex(r"\frac{1}{10}", font_size=50, color=GREEN).shift(LEFT*1 + UP*1.9)
        self.play(Write(result1))
        self.wait(2)
        
        # Example 2: Negative exponent (-2)
        sn02 = MathTex(r"2.", font_size=50).shift(LEFT*5 + UP*0.4)
        equall2 = Tex("=", font_size=50).shift(LEFT*3 + UP*0.4)
        self.play(Write(sn02))
        eg2 = MathTex(r"5^{-2}", font_size=50, color=BLUE).shift(LEFT*4 + UP*0.5)
        self.wait(1)
        self.play(Write(eg2))
        self.wait(1)
        self.play(Write(equall2))
        result2 = MathTex(r"\frac{1}{5^2}", font_size=50, color=BLUE).shift(LEFT*1 + UP*0.4)
        self.play(Write(result2))
        self.wait(2)
        
        # Example 3: Negative exponent (-3)
        sn03 = MathTex(r"3.", font_size=50).shift(LEFT*5 + DOWN*1.1)
        equall3 = Tex("=", font_size=50).shift(LEFT*3 + DOWN*1.1)
        self.play(Write(sn03))
        eg3 = MathTex(r"8^{-3}", font_size=50, color=RED).shift(LEFT*4 + DOWN*1)
        self.wait(1)
        self.play(Write(eg3))
        self.wait(1)
        self.play(Write(equall3))
        result3 = MathTex(r"\frac{1}{8^3}", font_size=50, color=RED).shift(LEFT*1 + DOWN*1.1)
        self.play(Write(result3))
        self.wait(2)



    def Law1(self):
        self.isRandom = False
        p11 = cvo.CVO().CreateCVO("Laws of Exponents", "").setPosition([-4,0, 0]).setangle(-TAU/4) 
        p12 = cvo.CVO().CreateCVO("Product Rule ", "$(a^m*a^n = a^{m + n})$").setPosition([4,0,0]).setangle(-TAU/4)
        #p13 = cvo.CVO().CreateCVO("Example ", "$(2^3*2^2 = 2^5)$").setPosition([4,2,0]).setangle(-TAU/4)
        #p14 = cvo.CVO().CreateCVO("Example 2", "$(5^3*5^3 = 5^6)$").setPosition([4.4,0, 0]).setangle(-TAU/4)
        p11.setcircleradius(1.5)
        p12.setcircleradius(1.5)
        #p13.setcircleradius(1.5)
       # p14.setcircleradius(1.3)
        p11.cvolist.append(p12)
        #p12.cvolist.append(p13)
        #p12.cvolist.append(p14)
        self.construct1(p11, p11)
    def Law1TextExamples(self):
        examples_title = Text(" Product Rule Examples : ", font_size=36).shift(LEFT*4.3 + UP*3)
        self.play(Write(examples_title))
        self.wait(1)

        # Example 1
        sn01 = MathTex(r"1.", font_size=54).shift(LEFT*5.3 + UP*1.8)
        equals_sign = Tex("=", font_size=50).shift(RIGHT*1 + UP*3)
        
        self.wait(1)
        
        # Left side of the equation
        left_side = MathTex(r"(a^m \cdot a^n)", font_size=50, color=GREEN).shift(LEFT*0.5 + UP*3)
        self.play(Write(left_side))
        self.wait(1)
        self.play(Write(equals_sign))
        
        # Right side of the equation
        right_side = MathTex(r"a^{m+n}", font_size=50, color=GREEN).shift(RIGHT*2.5 + UP*3)
        self.play(Write(right_side))
        self.wait(1)
        self.play(Write(sn01))
        self.wait(1.5)
        # Annotating with an example
        example_expansion = MathTex(r"2^3 \cdot 2^2", font_size=50, color=BLUE).shift(LEFT*4 + UP*1.9)
        equals_sign_2 = Tex("=", font_size=50).shift(LEFT*2.5 + UP*1.9)
        self.play(Write(example_expansion))
        self.play(Write(equals_sign_2))
        
        # Simplified example
        simplified_example = MathTex(r"2^{3+2} = 2^5 = 32", font_size=50, color=BLUE).shift(LEFT*0.1 + UP*1.9)
        self.play(Write(simplified_example))
        self.wait(1)

        sn02 = MathTex(r"2.", font_size=54).shift(LEFT*5.3 + UP*0.1)
        self.play(Write(sn02))
        self.wait(2)
        
        
        # Annotating with an example
        example_expansion_2 = MathTex(r"5^2 \cdot 5^3", font_size=50, color=YELLOW).shift(LEFT*4 + UP*0.1)
        equals_sign_4 = Tex("=", font_size=50).shift(LEFT*2.5 + UP*0.1)
        self.play(Write(example_expansion_2))
        self.play(Write(equals_sign_4))
        
        # Simplified example
        simplified_example_2 = MathTex(r"5^{2+3} = 5^5 = 3125", font_size=50, color=YELLOW).shift(LEFT*0.1 + UP*0.1)
        self.play(Write(simplified_example_2))
        self.wait(2)
    def Law2(self):
        self.isRandom = False
        p10 = cvo.CVO().CreateCVO("Law 2", "").setPosition([-4,0,0]).setangle(-TAU/4)
        p11 = cvo.CVO().CreateCVO("Quotient Rule", "$\\frac{a^m}{a^n} = a^{m - n}$").setPosition([4,0,0]).setangle(-TAU/4)
       # p12 = cvo.CVO().CreateCVO("Example 1", "$\\frac{3^4}{3^2} = 3^{2}$").setPosition([3,0,0]).setangle(-TAU/4)
        #p13 = cvo.CVO().CreateCVO("Example 2", "$\\frac{5^3}{5^2} = 5^{1}$").setPosition([-3,-1.5,0]).setangle(-TAU/4)
        p11.setcircleradius(1.5)
        p10.setcircleradius(1.5)
        
        p10.cvolist.append(p11)
        #p11.cvolist.append(p12)
        #p11.cvolist.append(p13)
        
        self.construct1(p10, p10)
    def Law2TextExamples(self):
        examples_title = Text("Quotient Rule Examples:", font_size=36).shift(LEFT*4.3 + UP*3)
        self.play(Write(examples_title))
        self.wait(1)

        # Example 1
        sn01 = MathTex(r"1.", font_size=54).shift(LEFT*5.3 + UP*1.8)
        equals_sign = Tex("=", font_size=50).shift(RIGHT*1 + UP*3)
        
        self.wait(1)
        
        # Left side of the equation
        left_side = MathTex(r"\left(\frac{a^m}{a^n}\right)", font_size=50, color=GREEN).shift(LEFT*0.5 + UP*3)
        self.play(Write(left_side))
        self.wait(1)
        self.play(Write(equals_sign))
        
        # Right side of the equation
        right_side = MathTex(r"a^{m-n}", font_size=50, color=GREEN).shift(RIGHT*2.5 + UP*3)
        self.play(Write(right_side))
        self.wait(1)
        self.play(Write(sn01))
        self.wait(1)
        # Annotating with an example
        example_expansion = MathTex(r"\frac{2^5}{2^2}", font_size=50, color=BLUE).shift(LEFT*4 + UP*1.9)
        equals_sign_2 = Tex("=", font_size=50).shift(LEFT*2.5 + UP*1.9)
        self.play(Write(example_expansion))
        self.wait(1)
        self.play(Write(equals_sign_2))
        
        # Simplified example
        simplified_example = MathTex(r"2^{5-2} = 2^3 = 8", font_size=50, color=BLUE).shift(LEFT*0.1 + UP*1.9)
        self.play(Write(simplified_example))
        self.wait(1)

        # Example 2
        sn02 = MathTex(r"2.", font_size=54).shift(LEFT*5.3 + UP*0.1)
        
        self.play(Write(sn02))
        self.wait(1)

        
        
        # Annotating with an example
        example_expansion_2 = MathTex(r"\frac{7^4}{7^2}", font_size=50, color=YELLOW).shift(LEFT*4 + UP*0.1)
        equals_sign_4 = Tex("=", font_size=50).shift(LEFT*2.5 + UP*0.1)
        self.play(Write(example_expansion_2))
        self.wait(1)
        self.play(Write(equals_sign_4))
        
        # Simplified example
        simplified_example_2 = MathTex(r"7^{4-2} = 7^2 = 49", font_size=50, color=YELLOW).shift(LEFT*0.1 + UP*0.1)
        self.play(Write(simplified_example_2))
        self.wait(2)
        
        # Example 3
        sn03 = MathTex(r"3.", font_size=54).shift(LEFT*5.3 + DOWN*2.1)
        self.play(Write(sn03))
        self.wait(1)
        
        
        # Annotating with an example
        example_expansion_3 = MathTex(r"\frac{10^6}{10^3}", font_size=50, color=RED).shift(LEFT*4 + DOWN*2.1)
        equals_sign_6 = Tex("=", font_size=50).shift(LEFT*2.5 + DOWN*2.1)
        self.play(Write(example_expansion_3))
        self.wait(1)
        self.play(Write(equals_sign_6))
        
        # Simplified example
        simplified_example_3 = MathTex(r"10^{6-3} = 10^3 = 1000", font_size=50, color=RED).shift(RIGHT*0.1 + DOWN*2.1)
        self.play(Write(simplified_example_3))
        self.wait(2)
    
    def Law3(self):
        self.isRandom = False
        p11 = cvo.CVO().CreateCVO("Law 3", "").setPosition([-4,0,0]).setangle(-TAU/4)
        p12 = cvo.CVO().CreateCVO("Power Rule", "$((a^m)^n = a^{m*n})$").setPosition([4,0,0]).setangle(-TAU/4)
       # p13 = cvo.CVO().CreateCVO("Example 1", "$((5^3)^2 = 5^{6})$").setPosition([3,0,0]).setangle(-TAU/4)
       # p14 = cvo.CVO().CreateCVO("Example 2", "$((8^5)^2 = 8^{10})$").setPosition([-3,-1.5,0]).setangle(-TAU/4)
        
        p12.setcircleradius(1.5)
        p11.setcircleradius(1.5)
       
        p11.cvolist.append(p12)
       # p12.cvolist.append(p13)
       # p12.cvolist.append(p14)

        self.construct1(p11, p11)
    def Law3TextExamples(self):
        examples_title = Text("Power Rule Examples:", font_size=36).shift(LEFT*4 + UP*3)
        self.play(Write(examples_title))
        self.wait(1)

        # Example 1
        sn01 = MathTex(r"1.", font_size=54).shift(LEFT*5.3 + UP*1.8)
        equals_sign = Tex("=", font_size=50).shift(RIGHT*1 + UP*3)
        
        
        self.wait(1)
        
        # Left side of the equation
        left_side = MathTex(r"(a^m)^n", font_size=50, color=GREEN).shift(LEFT*0.5 + UP*3)
        self.play(Write(left_side))
        self.wait(1)
        self.play(Write(equals_sign))
        
        # Right side of the equation
        right_side = MathTex(r"a^{m \cdot n}", font_size=50, color=GREEN).shift(RIGHT*2.5 + UP*3)
        self.play(Write(right_side))
        self.wait(1)
        self.play(Write(sn01))
        self.wait(1)
        # Annotating with an example
        example_expansion = MathTex(r"(2^3)^2", font_size=50, color=BLUE).shift(LEFT*4 + UP*1.9)
        equals_sign_2 = Tex("=", font_size=50).shift(LEFT*2.5 + UP*1.9)
        self.play(Write(example_expansion))
        self.wait(1)
        self.play(Write(equals_sign_2))
        
        # Simplified example
        simplified_example = MathTex(r"2^{3 \cdot 2} = 2^6 = 64", font_size=50, color=BLUE).shift(LEFT*0.1 + UP*1.9)
        self.play(Write(simplified_example))
        self.wait(2)

        # Example 2
        sn02 = MathTex(r"2.", font_size=54).shift(LEFT*5.3 + UP*0.1)
        
        self.play(Write(sn02))
        self.wait(1)
        
        
    
        
        # Annotating with an example
        example_expansion_2 = MathTex(r"(3^2)^3", font_size=50, color=YELLOW).shift(LEFT*4 + UP*0.1)
        equals_sign_4 = Tex("=", font_size=50).shift(LEFT*2.5 + UP*0.1)
        self.play(Write(example_expansion_2))
        self.wait(1)
        self.play(Write(equals_sign_4))
        
        # Simplified example
        simplified_example_2 = MathTex(r"3^{2 \cdot 3} = 3^6 = 729", font_size=50, color=YELLOW).shift(LEFT*0.1 + UP*0.1)
        self.play(Write(simplified_example_2))
        self.wait(2)
        
        # Example 3
        sn03 = MathTex(r"3.", font_size=54).shift(LEFT*5.3 + DOWN*2.1)
        
        self.play(Write(sn03))
        self.wait(1)
        
        # Left side of the equation
        
        
        # Annotating with an example
        example_expansion_3 = MathTex(r"(4^2)^3", font_size=50, color=RED).shift(LEFT*4 + DOWN*2.1)
        equals_sign_6 = Tex("=", font_size=50).shift(LEFT*2.5 + DOWN*2.1)
        self.play(Write(example_expansion_3))
        self.wait(1)
        self.play(Write(equals_sign_6))
        
        # Simplified example
        simplified_example_3 = MathTex(r"4^{2 \cdot 3} = 4^6 = 4096", font_size=50, color=RED).shift(RIGHT*0.1 + DOWN*2.1)
        self.play(Write(simplified_example_3))
        self.wait(2)
    def Law4(self):
        self.isRandom = False
        p11 = cvo.CVO().CreateCVO("Law 4", "").setPosition([-4,0,0]).setangle(-TAU/4)
        p12 = cvo.CVO().CreateCVO("Product of Powers", "$(a^m*b^m = (a*b)^m)$").setPosition([4,0, 0]).setangle(-TAU/4)
       # p13 = cvo.CVO().CreateCVO("Example 1", "$(5^3*2^3 = (10)^3)$").setPosition([3, 0, 0]).setangle(-TAU/4)
       # p14 = cvo.CVO().CreateCVO("Example 2", "$(7^3*2^3 = (14)^3)$").setPosition([-3, -1.5, 0]).setangle(-TAU/4)
        
        p12.setcircleradius(1.5)
        p11.setcircleradius(1.5)
       
       # p13.setcircleradius(1.3)
       # p14.setcircleradius(1.3)
        p11.cvolist.append(p12)
       # p12.cvolist.append(p13)
       # p12.cvolist.append(p14)
        self.construct1(p11, p11)
    def Law4TextExamples(self):
        examples_title = Text("Product of Powers Examples:", font_size=36).shift(LEFT*3.8 + UP*3)
        self.play(Write(examples_title))
        self.wait(1)

        # Example 1
        sn01 = MathTex(r"1.", font_size=54).shift(LEFT*5.3 + UP*1.8)
        equals_sign = Tex("=", font_size=50).shift(RIGHT*2.5 + UP*3)
        self.wait(1)
        
        # Left side of the equation
        left_side = MathTex(r"(a^m) \cdot (b^m)", font_size=50, color=GREEN).shift(RIGHT*0.8 + UP*3)
        self.play(Write(left_side))
        self.wait(1)
        self.play(Write(equals_sign))
        
        # Right side of the equation
        right_side = MathTex(r"(a \cdot b)^m", font_size=50, color=GREEN).shift(RIGHT*4 + UP*3)
        self.play(Write(right_side))
        self.wait(1)
        self.play(Write(sn01))
        self.wait(1.5)
        
        # Annotating with an example
        example_expansion = MathTex(r"(2^3) \cdot (3^3)", font_size=50, color=BLUE).shift(LEFT*4 + UP*1.9)
        equals_sign_2 = Tex("=", font_size=50).shift(LEFT*2.5 + UP*1.9)
        self.play(Write(example_expansion))
        self.wait(1)
        self.play(Write(equals_sign_2))
        
        # Simplified example
        simplified_example = MathTex(r"(2 \cdot 3)^3 = 6^3 = 216", font_size=50, color=BLUE).shift(LEFT*0.1 + UP*1.9)
        self.play(Write(simplified_example))
        self.wait(2)

        # Example 2
        sn02 = MathTex(r"2.", font_size=54).shift(LEFT*5.3 + UP*0.1)
        self.play(Write(sn02))
        self.wait(1)
        
        # Annotating with an example
        example_expansion_2 = MathTex(r"(4^2) \cdot (5^2)", font_size=50, color=YELLOW).shift(LEFT*4 + UP*0.1)
        equals_sign_4 = Tex("=", font_size=50).shift(LEFT*2.5 + UP*0.1)
        self.play(Write(example_expansion_2))
        self.wait(1)
        self.play(Write(equals_sign_4))
        
        # Simplified example
        simplified_example_2 = MathTex(r"(4 \cdot 5)^2 = 20^2 = 400", font_size=50, color=YELLOW).shift(LEFT*0.1 + UP*0.1)
        self.play(Write(simplified_example_2))
        self.wait(2)
        
        # Example 3
        sn03 = MathTex(r"3.", font_size=54).shift(LEFT*5.3 + DOWN*2.1)
        self.play(Write(sn03))
        self.wait(1)
        
        # Annotating with an example
        example_expansion_3 = MathTex(r"(3^2) \cdot (2^2)", font_size=50, color=RED).shift(LEFT*4 + DOWN*2.1)
        equals_sign_6 = Tex("=", font_size=50).shift(LEFT*2.5 + DOWN*2.1)
        self.play(Write(example_expansion_3))
        self.wait(1)
        self.play(Write(equals_sign_6))
        
        # Simplified example
        simplified_example_3 = MathTex(r"(3 \cdot 2)^2 = 6^2 = 36", font_size=50, color=RED).shift(LEFT*0.1 + DOWN*2.1)
        self.play(Write(simplified_example_3))
        self.wait(2)
    def Law5(self):
        self.isRandom = False
        p11 = cvo.CVO().CreateCVO("Law 5", "").setPosition([-4,0,0]).setangle(-TAU/4)
        p12 = cvo.CVO().CreateCVO("Zero Exponent Rule", "$(a^0 = 1)$").setPosition([4, 0, 0]).setangle(-TAU/4)
      #  p13 = cvo.CVO().CreateCVO("Example 1", "$(5^0 = 1)$").setPosition([3, 0, 0]).setangle(-TAU/4)
       # p14 = cvo.CVO().CreateCVO("Example 2", "$(8^0 = 1)$").setPosition([-3, -1.5, 0]).setangle(-TAU/4)
        p11.setcircleradius(1.5)
        p12.setcircleradius(1.5)
        p11.cvolist.append(p12)
      #  p12.cvolist.append(p13)
       # p12.cvolist.append(p14)

        self.construct1(p11, p11)
    def Law5TextExamples(self):
        examples_title = Text("Zero Exponent Rule Examples:", font_size=36).shift(LEFT*3.7 + UP*3)
        self.play(Write(examples_title))
        self.wait(1)
        
        formula = MathTex(r"a^0 = 1",font_size = 50).shift(RIGHT*2 + UP*3)
        self.play(Write(formula))
        # Example 1
        sn01 = MathTex(r"1.", font_size=54).shift(LEFT*5.3 + UP*1.8)
        equals_sign = Tex("=", font_size=50).shift(RIGHT*1 + UP*3)
        self.wait(1)
        self.play(Write(sn01))
        # Annotating with an example
        example_expansion = MathTex(r"(2^0)", font_size=50, color=BLUE).shift(LEFT*4 + UP*1.9)
        equals_sign_2 = Tex("=", font_size=50).shift(LEFT*2.5 + UP*1.9)
        self.play(Write(example_expansion))
        self.wait(1)
        self.play(Write(equals_sign_2))
        
        # Simplified example
        simplified_example = MathTex(r"1", font_size=50, color=BLUE).shift(LEFT*0.1 + UP*1.9)
        self.play(Write(simplified_example))
        self.wait(2)

        # Example 2
        sn02 = MathTex(r"2.", font_size=54).shift(LEFT*5.3 + UP*0.1)
        self.play(Write(sn02))
        self.wait(1)
        
        # Annotating with an example
        example_expansion_2 = MathTex(r"(3^0)", font_size=50, color=YELLOW).shift(LEFT*4 + UP*0.1)
        equals_sign_4 = Tex("=", font_size=50).shift(LEFT*2.5 + UP*0.1)
        self.play(Write(example_expansion_2))
        self.wait(1)
        self.play(Write(equals_sign_4))
        
        # Simplified example
        simplified_example_2 = MathTex(r"1", font_size=50, color=YELLOW).shift(LEFT*0.1 + UP*0.1)
        self.play(Write(simplified_example_2))
        self.wait(2)
        
        # Example 3
        sn03 = MathTex(r"3.", font_size=54).shift(LEFT*5.3 + DOWN*2.1)
        self.play(Write(sn03))
        self.wait(1)
        
        # Annotating with an example
        example_expansion_3 = MathTex(r"(5^0)", font_size=50, color=RED).shift(LEFT*4 + DOWN*2.1)
        equals_sign_6 = Tex("=", font_size=50).shift(LEFT*2.5 + DOWN*2.1)
        self.play(Write(example_expansion_3))
        self.wait(1)
        self.play(Write(equals_sign_6))
        
        # Simplified example
        simplified_example_3 = MathTex(r"1", font_size=50, color=RED).shift(LEFT*0.1 + DOWN*2.1)
        self.play(Write(simplified_example_3))
        self.wait(2)


    def ExpConversion(self):
        self.isRandom=False
        p10 = cvo.CVO().CreateCVO("Application of Exponents", "Expressing Numbers in Standard Form").setPosition([-4, 0, 0]).setangle(-TAU/4)
        p11 = cvo.CVO().CreateCVO("Example 1", "$12345 = 1.2345*10^4$").setPosition([4, 2, 0]).setangle(-TAU/4)
        p12 = cvo.CVO().CreateCVO("Example  2", "$0.00123 = 1.23*10^{-3}$").setPosition([4,-1, 0]).setangle(-TAU/4)
        #p13 = cvo.CVO().CreateCVO("Example 3", "$987000 = 9.87*10^5$").setPosition([-4, -2, 0]).setangle(-TAU/3)
        #p14 = cvo.CVO().CreateCVO("Example 4", "$0.0000456 = 4.56*10^{-5}$").setPosition([0, -2, 0]).setangle(-TAU/4)
        
        p10.setcircleradius(2)
        p11.setcircleradius(1.5)
        p12.setcircleradius(1.5)
        #p13.setcircleradius(1.5)
        #p14.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
       # p10.cvolist.append(p13)
       # p10.cvolist.append(p14)
        
        self.construct1(p10, p10)


    def ExpComparison(self):
        self.isRandom=False
        p10 = cvo.CVO().CreateCVO("Comparing Numbers with Exponents", "").setPosition([-4, 0, 0]).setangle(-TAU/4)
        p11 = cvo.CVO().CreateCVO("Large Number ", "$5.97*10^{24}$ (Mass of Earth)").setPosition([4, 2, 0]).setangle(-TAU/4)
        p12 = cvo.CVO().CreateCVO("Small Number ", "$9.11*10^{-31}$ (Mass of Electron)").setPosition([4, -2, 0]).setangle(-TAU/4)
        #p13 = cvo.CVO().CreateCVO("Small Number 1", "$9.11*10^{-31}$ (Mass of Electron)").setPosition([-4, -2, 0]).setangle(-TAU/3)
        #p14 = cvo.CVO().CreateCVO("Small Number 2", "$6.63*10^{-34}$ (Planck's Constant)").setPosition([0, -2, 0]).setangle(-TAU/4)
        
        p10.setcircleradius(2)
        p11.setcircleradius(1.5)
        p12.setcircleradius(1.5)
       # p13.setcircleradius(1.5)
       # p14.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
       # p10.cvolist.append(p13)
       # p10.cvolist.append(p14)
        
        self.construct1(p10, p10)
    
    def SetDeveloperList(self):  
        self.DeveloperList = "Mukthanand Reddy"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName = "Grade8Chapter4ExponentsAndPowers.py"
         
if __name__ == "__main__":
    scene = Exponents()
    scene.render()
