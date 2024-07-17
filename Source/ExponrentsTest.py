import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo

class ExponentsAnim(AbstractAnim):
    def construct(self):
        self.DecimalsSubstraction()

    def DecimalsSubstraction(self):
        title = Title("Substraction Of Decimals ")
        fraction_heading = MathTex("Example : ", r" 59.5 + 35.2", font_size=36).to_edge(UP*3 + LEFT)
        num1 = Tex("5 9 . 5", font_size=70).shift(LEFT * 3)
        num2 = Tex("3 5 . 2", font_size=70).shift(DOWN * 0.6 + LEFT * 3)
        plus_sign = Tex("-").scale(1.5).shift(DOWN * 0.6 + LEFT * 4.3)
        line_start = num2.get_corner(DOWN + LEFT) + DOWN * 0.3  
        line_end = line_start + RIGHT * 2.2  
        line = Line(line_start, line_end)
        s_result = Tex(r" 5 - 2 = 3", font_size=60,color=BLUE).shift(UP* 1 + RIGHT * 3)
        s_result2= Tex(r" 9 - 5 = 4", font_size=60,color=GREEN).shift(UP* 0.2 + RIGHT * 3)
        s_result3= Tex(r" 5 - 3 = 2", font_size=60,color=YELLOW).shift(DOWN*0.5 + RIGHT * 3)
        self.play(Write(title))
        self.wait(1)
        self.play(Write(fraction_heading))
        self.wait(1)
        self.play(Write(num1), Write(num2))
        self.wait(1)
        self.play(Create(line))
        self.wait(1)
        self.play(Write(plus_sign))
        self.wait(1)
        line2_start  = num2.get_corner(DOWN + LEFT) + DOWN * 1- RIGHT * 0.5
        line2_end = line2_start + RIGHT  * 2.2
        line2 = Line(line2_start, line2_end)
        self.play(Create(line2))
        self.wait(1)

        # Units place addition
        highlight_rect1 = Rectangle(width=0.5, height=1.5, color=RED, fill_opacity=0.2).shift(DOWN * 0.2 + LEFT * 2.2)
        self.play(FadeIn(highlight_rect1))
        result1 = Tex(". 3", font_size=70).shift(DOWN * 1.5 + LEFT * 2.2)
        #carry1 = Tex("1", font_size=60).shift(UP * 1 + LEFT * 3.15)
        self.play(Create(s_result))
        self.wait(1)
        self.play(Create(result1))
        self.wait(1)

        #self.play(FadeIn(carry1))
        self.play(FadeOut(highlight_rect1))
        self.wait(1)
        #self.play(FadeOut(carry1))
        # Tens place addition
        highlight_rect2 = Rectangle(width=0.5, height=2.0, color=RED, fill_opacity=0.2).shift(DOWN * 0.2 + LEFT * 3.25)
        self.play(FadeIn(highlight_rect2))
        result2 = Tex("4", font_size=70).shift(DOWN * 1.5 + LEFT * 3.2)
        #carry2 = Tex("1", font_size=60).shift(UP * 1 + LEFT * 3.8)
        
        self.play(Create(result2),Create(s_result2))
        self.play(FadeOut(highlight_rect2))
        self.wait(1)
        # Hundreds place addition
        highlight_rect3 = Rectangle(width=0.5, height=2.0, color=RED, fill_opacity=0.2).shift(DOWN * 0.2 + LEFT * 3.8)
        self.play(FadeIn(highlight_rect3))
        result3 = Tex("2 ", font_size=70).shift(DOWN * 1.5 + LEFT * 4)
        self.play(Create(s_result3))
        self.wait(1)
        self.play(Create(result3))
        self.wait(1)
        self.play(FadeOut(highlight_rect3))
        self.wait(2)
    

if __name__ == "__main__":
    scene = ExponentsAnim()
    scene.render()
