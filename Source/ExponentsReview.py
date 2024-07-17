import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo

class ExponentsTest(AbstractAnim):
    def construct(self):
        self.ExpComparison()

   
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
        p10 = cvo.CVO().CreateCVO("Comparing Numbers with Exponents", "Very Large and Very Small Numbers").setPosition([-4, 0, 0]).setangle(-TAU/4)
        p11 = cvo.CVO().CreateCVO("Large Number 1", "$5.97*10^{24}$ (Mass of Earth)").setPosition([4, 2, 0]).setangle(-TAU/4)
        p12 = cvo.CVO().CreateCVO("Small Number 1", "$9.11*10^{-31}$ (Mass of Electron)").setPosition([4, -2, 0]).setangle(-TAU/4)
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

if __name__ == "__main__":
    scene = ExponentsTest()
    scene.render()
