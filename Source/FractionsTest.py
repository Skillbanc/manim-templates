import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo

class ExponentsReview(AbstractAnim):
    def construct(self):
        self.read()
    

   
    def Law1(self):
        self.isRandom = False
        p11 = cvo.CVO().CreateCVO("Laws of Exponents", "").setPosition([-4,2, 0]).setangle(-TAU/4) 
        p12 = cvo.CVO().CreateCVO("Product Rule ", "$(a^m*a^n = a^{m + n})$").setPosition([-4,-2,0]).setangle(-TAU/4)
        p13 = cvo.CVO().CreateCVO("Example 1", "$(2^3*2^2 = 2^5)$").setPosition([3,2,0]).setangle(-TAU/4)
        p14 = cvo.CVO().CreateCVO("Example 2", "$(5^3*5^3 = 5^6)$").setPosition([3,-0.4, 0]).setangle(-TAU/4)
        
        p12.setcircleradius(1.5)
        p13.setcircleradius(1.3)
        p14.setcircleradius(1.3)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        p12.cvolist.append(p14)
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
        self.wait(1)
        
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
        self.wait(1)

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
        self.wait(1)

  
    def NegativePowerTextExamples(self):
        examples_title = MathTex("Negative Power Examples : ", font_size=50).shift(LEFT*3.5 + UP*3)
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
        self.wait(1)
        
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
        self.wait(1)
        
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
        self.wait(1)

    def ExponentFormAnim(self):
        title = Text(" Exponent Example : ",font_size = 30).shift(UP*3+LEFT*4)
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
        read = Text("We read 10^9 as 10 raised to the power of 9",font_size = 30).shift(DOWN*2+LEFT*2)
        
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
    
    def Law1TextExamples(self):
        examples_title = Text(" Product Rule Examples : ", font_size=36).shift(LEFT*2.1 + UP*3)
        self.play(Write(examples_title))
        self.wait(1)

        # Example 1
        sn01 = MathTex(r"1.", font_size=54).shift(LEFT*5.3 + UP*1.8)
        equals_sign = Tex("=", font_size=50).shift(RIGHT*1 + UP*3)
        self.play(Write(sn01))
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

    def Law2TextExamples(self):
        examples_title = Text("Quotient Rule Examples:", font_size=36).shift(LEFT*2.1 + UP*3)
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
        self.wait(1.5)

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
        self.wait(1.5)
        
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
        self.wait(1)
        
        # Annotating with an example
        example_expansion = MathTex(r"(2^3) \cdot (3^3)", font_size=50, color=BLUE).shift(LEFT*4 + UP*1.9)
        equals_sign_2 = Tex("=", font_size=50).shift(LEFT*2.5 + UP*1.9)
        self.play(Write(example_expansion))
        self.wait(1)
        self.play(Write(equals_sign_2))
        
        # Simplified example
        simplified_example = MathTex(r"(2 \cdot 3)^3 = 6^3 = 216", font_size=50, color=BLUE).shift(LEFT*0.1 + UP*1.9)
        self.play(Write(simplified_example))
        self.wait(1.5)

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
        self.wait(1.5)
        
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
        self.wait(1.5)

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
        self.wait(1.5)
        
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
    

    def Definition(self):
        self.isRandom= False
        p10 = cvo.CVO().CreateCVO("Fractions", "").setPosition([-4, 0, 0]).setangle(-TAU/4)
        p11 = cvo.CVO().CreateCVO("Definition", "A fraction represents a part of a whole").setPosition([4,2, 0]).setangle(-TAU/4)
        p12 = cvo.CVO().CreateCVO("Fraction Form", "$(p/q)$").setPosition([4,-2 , 0]).setangle(-TAU/4)
        #p13 = cvo.CVO().CreateCVO(r"$\frac{p}{q}$", "").setPosition([-4, -2, 0]).setangle(-TAU/3)
       # p14 = cvo.CVO().CreateCVO("Numerator", "p").setPosition([3,2,0]).setangle(-TAU/4)
       # p15 = cvo.CVO().CreateCVO("Denominator", "q").setPosition([3,-1,0]).setangle(-TAU/2)
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        #p12.cvolist.append(p14)
       # p12.cvolist.append(p15)
       # p13.cvolist.append(p15)
        self.construct1(p10, p10)

    def ImproperExp3(self):
        examples_title = MathTex("Example 3: ", r"\frac{4}{3}", font_size=36).to_edge(UP*3 + LEFT)
        
        self.play(Write(examples_title))
        self.wait(1)
        # Create a circle and move it to the left
        circle = Circle(radius=1, fill_color=BLUE, fill_opacity=0.5).shift(LEFT * 4)
        self.play(Create(circle))
        self.wait(1)

        # Create the dividing lines
        lines = VGroup()
        for i in range(3):
            angle = i * 2 * PI / 3
            line = Line(circle.get_center(), circle.point_at_angle(angle), color=YELLOW)
            lines.add(line)

        self.play(Create(lines))
        self.wait(1)

        sector_boundary_lines = VGroup(
            Line(circle.get_center(), circle.point_at_angle(0), color=RED).shift(LEFT * 4),
            Line(circle.get_center(), circle.point_at_angle(2 * PI / 3), color=RED).shift(LEFT * 4)
            
        )
        
        
        #self.play(Create(sector_boundary_lines))
        sector1 = Sector(radius=2.5, start_angle=5 * PI / 2, angle=PI / 2, fill_color=BLUE, fill_opacity=0.5).shift(LEFT*1)
        self.play(Create(sector1))
        self.wait(1)
        # Indicate the fraction 1/3
        fraction = MathTex(r"\frac{4}{3}", font_size=96).shift(RIGHT * 5)
        self.play(Write(fraction))
        self.wait(1)

        # Create an arrow from the circle to the fraction
        arrow_to_fraction = Arrow(sector1.get_bottom(), fraction, color=WHITE)
        self.play(Create(arrow_to_fraction))
        self.wait(2)
    
    def MixedFractionExp1(self):
        title = Text(" Mixed Fractions Examples", font_size=36).to_edge(UP)
        self.play(Write(title))
        # Create circles
        circle1 = Circle(radius=1, fill_color=BLUE, fill_opacity=1).shift(LEFT * 4)
        circle2 = Circle(radius=1, fill_color=BLUE, fill_opacity=1).shift(LEFT * 1)

        # Get centers of circles
        center_circle1 = circle1.get_center()
        center_circle2 = circle2.get_center()
        
        # Calculate endpoints for the vertical line within circle1
        start_point1 = center_circle1 + UP * 1  # Start slightly above the center
        end_point1 = center_circle1 + DOWN * 1  # End slightly below the center

        # Calculate endpoints for the vertical line within circle2
        start_point2 = center_circle2 + UP * 1  # Start slightly left of the center
        end_point2 = center_circle2 + DOWN * 1  # End slightly right of the center

        # Create vertical lines inside circles
        vertical_line1 = Line(start=start_point1, end=end_point1, color=BLACK)
        vertical_line2 = Line(start=start_point2, end=end_point2, color=BLACK)

        # Create an arc
        arc = Arc(radius=1, start_angle=PI/2, angle=PI, fill_color=BLUE, fill_opacity=1).shift(RIGHT * 2)
        fraction = Tex(r"$2\frac{1}{2}$", font_size=80).shift(RIGHT*5)
         

        arrow_to_fraction = Arrow(arc.get_center(), fraction.get_left(), color=WHITE)

       
        # Show animations
        self.play(Create(circle1))
        self.wait(1)
        self.play(Create(vertical_line1))
        self.wait(1)
        self.play(Create(circle2))
        self.wait(1)
        self.play(Create(vertical_line2))
        self.wait(1)
        self.play(Create(arc))
        self.wait(1)
        self.play(Create(arrow_to_fraction))
        self.wait(1)
        self.play(Write(fraction))
        self.wait(2)
    
    def AdditionExample1(self):
        #title = Title("Additions Of Numbers (with Carry over)")
        fraction_heading = MathTex("Example 1: ", r" 15 + 25", font_size=36).to_edge(UP*3 + LEFT)
        
        num1 = Tex("1 5", font_size=70).shift(LEFT * 3)
        num2 = Tex("2 5", font_size=70).shift(DOWN * 0.6 + LEFT * 3)
        note = Text("Note: Tens place is the carry-over",font_size= 36,color=YELLOW).shift(UP* 2.5 + RIGHT * 3)
        #self.play(Write(title))
        self.play(Write(fraction_heading))
        self.play(Write(num1))
        self.wait(1)
        self.play(Write(num2))
        s_result = Tex(r" 5 + 5 = 10", font_size=60,color=BLUE).shift(UP* 1 + RIGHT * 3)
        s_result2= Tex(r" 2 + 1 + 1 = 4", font_size=60,color=GREEN).shift(UP* 0.2 + RIGHT * 3)

        plus_sign = Tex("+").scale(1.5).shift(DOWN * 0.6 + LEFT * 3.9)
        self.play(Write(plus_sign))
        
        highlight_rect = Rectangle(width=0.5, height=1.5, color=BLUE, fill_opacity=0.2).shift(DOWN * 0.2 + LEFT * 2.7)
        self.wait(1)
        line2_start  = num2.get_corner(DOWN + LEFT) + DOWN * 1- RIGHT * 0.5
        line2_end = line2_start + RIGHT  * 2
        line2 = Line(line2_start, line2_end)
        
        
        line_start = num2.get_corner(DOWN + LEFT) + DOWN * 0.3- RIGHT * 0.5  # Adjust vertical position as needed
        line_end = line_start + RIGHT * 2  # Adjust horizontal length as needed
        line = Line(line_start, line_end)
        result1 = Tex("0", font_size=70).shift(DOWN * 1.5 + LEFT * 2.7)
        result2 = Tex("1", font_size=60,color=YELLOW).shift(UP * 1 + LEFT * 3.3)
        self.play(Create(line))
        self.wait(1)
        self.play(Create(line2))
        self.wait(1)
        self.play(FadeIn(highlight_rect))
        self.wait(1)
        self.play(Create(s_result)) 
        self.wait(1) 
        self.play(Write(note)) 
        self.wait(1)                            
        self.play(Create(result1))
        self.wait(1)
        self.play(FadeIn(result2)) 
        self.wait(1) 
        self.play(FadeOut(highlight_rect))
        highlight_rect2 = Rectangle(width=0.5, height=2.5, color=BLUE, fill_opacity=0.2).shift(LEFT * 3.3 + UP * 0.25)
        self.wait(1)
        self.play(FadeIn(highlight_rect2))
        result3 = Tex("4", font_size=70).shift(DOWN * 1.5 + LEFT * 3.3)
        self.play(Create(s_result2))
        self.wait(2)
        self.play(Create(result3))
        self.wait(1)
        self.play(FadeOut(highlight_rect2))
        

        self.wait(2)

    def AdditionExample3(self):
        fraction_heading = MathTex("Example 3: ", r" 472 + 548", font_size=36).to_edge(UP*3 + LEFT)
        num1 = Tex("4 7 2", font_size=70).shift(LEFT * 3)
        num2 = Tex("5 4 8", font_size=70).shift(DOWN * 0.6 + LEFT * 3)
        plus_sign = Tex("+").scale(1.5).shift(DOWN * 0.6 + LEFT * 4.1)
        note = Text("Note: Tens place is the carry-over",font_size= 36,color=YELLOW).shift(UP* 2.5 + RIGHT * 3)
        
        line_start = num2.get_corner(DOWN + LEFT) + DOWN * 0.3- RIGHT * 0.5   
        line_end = line_start + RIGHT * 3 
        line = Line(line_start, line_end)
        s_result = Tex(r" 2 + 8 = 10", font_size=60,color=BLUE).shift(UP* 1 + RIGHT * 3)
        s_result2= Tex(r" 1 + 7 + 4 = 12", font_size=60,color=GREEN).shift(UP* 0.2 + RIGHT * 3)
        s_result3= Tex(r" 1 + 4 + 5 = 10", font_size=60,color=YELLOW).shift(DOWN*0.5 + RIGHT * 3)
        line2_start  = num2.get_corner(DOWN + LEFT) + DOWN * 1.3- RIGHT * 0.5
        line2_end = line2_start + RIGHT  * 3
        line2 = Line(line2_start, line2_end)
        
        self.play(Write(fraction_heading))
        self.play(Write(num1))
        self.wait(1)
        self.play(Write(num2))
        self.wait(1)
        self.play(Create(line))
        self.wait(1)
        self.play(Create(line2))
        self.wait(1)
        self.play(Write(plus_sign))
        self.wait(1)
        # Units place addition
        highlight_rect1 = Rectangle(width=0.5, height=1.5, color=RED, fill_opacity=0.2).shift(DOWN * 0.2 + LEFT * 2.4)
        self.play(FadeIn(highlight_rect1))
        self.wait(1)
        result1 = Tex("0", font_size=70).shift(DOWN * 1.5 + LEFT * 2.4)
        carry1 = Tex("1", font_size=60,color=YELLOW).shift(UP * 1 + LEFT * 3)
        self.play(Create(s_result))
        self.wait(1)
        self.play(Write(note))
        self.wait(1)
        self.play(Create(result1))
        self.wait(1)

        self.play(FadeIn(carry1))
        self.wait(1)
        self.play(FadeOut(highlight_rect1))
        # Tens place addition
        highlight_rect2 = Rectangle(width=0.5, height=2.5, color=RED, fill_opacity=0.2).shift(UP * 0.1 + LEFT * 3)
        self.play(FadeIn(highlight_rect2))
        self.wait(1)
        result2 = Tex("2", font_size=70).shift(DOWN * 1.5 + LEFT * 3)
        carry2 = Tex("1", font_size=60,color=YELLOW).shift(UP * 1 + LEFT * 3.6)
        self.play(Create(s_result2))
        self.wait(1)
        self.play(Create(result2))
        self.wait(1)
        self.play(FadeIn(carry2))
        self.play(FadeOut(highlight_rect2))

        # Hundreds place addition
        highlight_rect3 = Rectangle(width=0.5, height=2.5, color=RED, fill_opacity=0.2).shift(UP * 0.1 + LEFT * 3.6)
        self.play(FadeIn(highlight_rect3))
        self.wait(1)
        result3 = Tex("1 0 ", font_size=70).shift(DOWN * 1.5 + LEFT * 3.8)
        self.play(Create(s_result3))
        self.wait(1)
        self.play(Create(result3))
        self.wait(1)
        self.play(FadeOut(highlight_rect3))
        
        
        self.wait(2)
    def ImproperFraction(self):  
        self.isRandom = False
        self.angleChoice = [TAU/2,TAU/4]
        p10=cvo.CVO().CreateCVO("Improper Fractions","").setPosition([-4,2,0])
        p11=cvo.CVO().CreateCVO( r" Is $\frac{p}{q}$" ,"Yes" ).setPosition([-4,-2,0])
        p12=cvo.CVO().CreateCVO("Condition ", "$p \geq q$").setPosition([3,2,0])
        #p13=cvo.CVO().CreateCVO("Example",  r"$\frac{6}{5}$").setPosition([5,0.5,0]).setangle(-TAU/4)
       # p10.setcircleradius(1.5)
       # p11.setcircleradius(1.5)
       # p12.setcircleradius(1.5)
        #p13.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        #p11.cvolist.append(p13)
        self.construct1(p10,p10)

    def MixedFractions(self):
        self.isRandom = False
        self.angleChoice=[TAU/2,TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Mixed Fractions ","").setPosition([-4,2,0])
        #p11=cvo.CVO().CreateCVO("Defination  ", "A fraction that has both a whole number and a fractional part").setPosition([0,1,0])
        p12=cvo.CVO().CreateCVO("Example",r"$(2\frac{3}{4})$").setPosition([-4,-2,0])
        p13=cvo.CVO().CreateCVO("Whole Number ", "$2$").setPosition([1,2,0])
        p14=cvo.CVO().CreateCVO("Fraction Part  ", "$(3/4)$").setPosition([5,2,0])
        
        p10.setcircleradius(1.5)
        p12.setcircleradius(1.5)
        p13.setcircleradius(1.5)
        p14.setcircleradius(1.5)
       
        #p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p12.cvolist.append(p13)
        p12.cvolist.append(p14)
        self.construct1(p10,p10)
    
    
    def StanderdForm(self):
        self.isRandom = False
        self.angleChoice = [TAU/2,TAU/4,TAU/4]
        p10 = cvo.CVO().CreateCVO("Standard Form of Fractions", "").setPosition([-4,2,0])
        p11 = cvo.CVO().CreateCVO("Definition", "Fraction with no common factors").setPosition([-4,-2,0])
        p12 = cvo.CVO().CreateCVO("Example 1 ","$(1/3)$" ).setPosition([3,2,0])
        p13 = cvo.CVO().CreateCVO("Example 2", "$(2/3)$").setPosition([3,-1,0])
        #p14 = cvo.CVO().CreateCVO("Example 3", r"$\frac{3}{11}$").setPosition([1,-2,0])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        #p13.cvolist.append(p14)
        self.construct1(p10, p10)

    def LikeFractions(self):
        self.isRandom = False
        self.angleChoice = [TAU/2,TAU/4,TAU/4]
        p10 = cvo.CVO().CreateCVO("Like Fractions", "").setPosition([-4,2,0])
        p11 = cvo.CVO().CreateCVO("Definition","Fractions with same denominator.").setPosition([-4,-2,0])
        p12 = cvo.CVO().CreateCVO("Example 1 ", r"$\frac{2}{7}$,$\frac{3}{7}$,$\frac{5}{7}$").setPosition([3,2,0])
        p13 = cvo.CVO().CreateCVO("Example 2", r"$\frac{1}{9}$,$\frac{2}{9}$,$\frac{4}{9}$").setPosition([3,-1,0])
       # p14 = cvo.CVO().CreateCVO("Exp3", r"$\frac{16}{36}$").setPosition([0,-2,0])
        p11.setcircleradius(1.5)
        p13.setcircleradius(1.5)
        p12.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        #p10.cvolist.append(p14)
        self.construct1(p10, p10)

    def MixedFractionExp2(self):
        examples_title = MathTex("Example 2: ", font_size=36).to_edge(UP*3 + LEFT)
        
        self.play(Write(examples_title))
        # Create a circle and move it to the left
        circle = Circle(radius=1, fill_color=BLUE, fill_opacity=0.5).shift(LEFT * 4)
        self.wait(1)
        self.play(Create(circle))

        # Create the dividing lines for the circle
        lines = VGroup()
        for i in range(3):
            angle = i * 2 * PI / 3
            line = Line(circle.get_center(), circle.point_at_angle(angle), color=YELLOW)
            lines.add(line)
        self.wait(1)
        self.play(Create(lines))

        # Create two sectors with 120 degrees each
        radius = 1
        angle = 120 * DEGREES  # Convert degrees to radians

        sector1 = Sector(radius=radius, angle=angle, fill_color=BLUE, fill_opacity=0.5).shift(LEFT * 1)
        sector2 = Sector(radius=radius, angle=angle, start_angle=angle, fill_color=BLUE, fill_opacity=0.5).shift(LEFT * 1)

        self.play(Create(sector1))
        self.wait(1)
        self.play(Create(sector2))

        # Create the dividing lines for the sectors
        sector_lines = VGroup()
        sector_angles = [0, 120 * DEGREES, 240 * DEGREES]
        for sector in [sector1, sector2]:
            center = LEFT*1
            for angle in sector_angles:
                # Update the calculation for the end point
                end_point = center + radius * np.array([np.cos(angle), np.sin(angle), 0])
                line = Line(center, end_point, color=YELLOW)
                sector_lines.add(line)
        self.wait(1)
        self.play(Create(sector_lines))
        self.wait(1)
        # Indicate the fraction 1/3
        fraction = Tex(r"$1\frac{2}{3}$", font_size=96).shift(RIGHT * 5.3)
        # Create an arrow from sector2 to the fraction
        arrow_to_fraction = Arrow(sector1.get_bottom(), fraction.get_left(), color=WHITE)
        self.play(Create(arrow_to_fraction))
        self.wait(1)
        self.play(Write(fraction))  
        self.wait(2)

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

    def read(self):
         examples_title = MathTex("Example 2: 1 ", font_size=36).to_edge(UP*3 + LEFT)
        
         self.play(Write(examples_title))
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
        
if __name__ == "__main__":
    scene = ExponentsReview()
    scene.render()
