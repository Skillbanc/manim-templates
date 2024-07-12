import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo
class AdditionAnim(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.Addition()
        self.fadeOutCurrentScene()
        self.AdditionExample1()
        self.fadeOutCurrentScene()
        self.AdditionExample2()
        self.fadeOutCurrentScene()
        self.AdditionExample3()
        self.fadeOutCurrentScene()
        self.AdditionExample4()
        self.fadeOutCurrentScene()
        
        self.GithubSourceCodeReference()

    def SetDeveloperList(self):  
        self.DeveloperList = "Mukthanand Reddy"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName = "Grade2Chapter6Additions.py"
        
    def Addition(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Additions ","$(+)$").setPosition([-4,0,0]).setangle(-TAU/4)
        p11=cvo.CVO().CreateCVO("Definition" ,"Combining numbers or quantities" ).setPosition([4,2,0]).setangle(-TAU/4)
        p12=cvo.CVO().CreateCVO("Special Case  ", "With Carry over").setPosition([4,-2.5,0]).setangle(-TAU/4)
        p11.setcircleradius(2)
        p10.setcircleradius(1.5)
        p12.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)


    def AdditionExample1(self):
        #title = Title("Additions Of Numbers (with Carry over)")
        fraction_heading = MathTex("Example 1: ", r" 15 + 25", font_size=36).to_edge(UP*3 + LEFT)
        
        num1 = Tex("1 5", font_size=70).shift(LEFT * 3)
        num2 = Tex("2 5", font_size=70).shift(DOWN * 0.6 + LEFT * 3)
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
        
        
        line_start = num2.get_corner(DOWN + LEFT) + DOWN * 0.3- RIGHT * 0.5  # Adjust vertical position as needed
        line_end = line_start + RIGHT * 2  # Adjust horizontal length as needed
        line = Line(line_start, line_end)
        result1 = Tex("0", font_size=70).shift(DOWN * 1.5 + LEFT * 2.7)
        result2 = Tex("1", font_size=60).shift(UP * 1 + LEFT * 3.3)
        self.play(Create(line))
        self.wait(1)
        self.play(FadeIn(highlight_rect))
        self.wait(1)
        self.play(Create(s_result)) 
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
        line2_start  = num2.get_corner(DOWN + LEFT) + DOWN * 1- RIGHT * 0.5
        line2_end = line2_start + RIGHT  * 2
        line2 = Line(line2_start, line2_end)
        self.play(Create(line2))

        self.wait(2)
    def AdditionExample2(self):
        #title = Title("Additions Of Numbers (with Carry over)")
        fraction_heading = MathTex("Example 2: ", r" 29 + 48", font_size=36).to_edge(UP*3 + LEFT)
        
        num1 = Tex("2 9", font_size=70).shift(LEFT * 3)
        num2 = Tex("4 8", font_size=70).shift(DOWN * 0.6 + LEFT * 3)
        #self.play(Write(title))
        self.play(Write(fraction_heading))
        self.play(Write(num1))
        self.wait(1)
        self.play(Write(num2))
        s_result = Tex(r" 9 + 8 = 17", font_size=60,color=BLUE).shift(UP* 1 + RIGHT * 3)
        s_result2= Tex(r" 4 + 2 + 1 = 7", font_size=60,color=GREEN).shift(UP* 0.2 + RIGHT * 3)

        plus_sign = Tex("+").scale(1.5).shift(DOWN * 0.6 + LEFT * 3.9)
        self.play(Write(plus_sign))
        
        highlight_rect = Rectangle(width=0.5, height=1.5, color=BLUE, fill_opacity=0.2).shift(DOWN * 0.2 + LEFT * 2.7)
        self.wait(1)
        
        
        line_start = num2.get_corner(DOWN + LEFT) + DOWN * 0.3- RIGHT * 0.5  # Adjust vertical position as needed
        line_end = line_start + RIGHT * 2  # Adjust horizontal length as needed
        line = Line(line_start, line_end)
        result1 = Tex("7", font_size=70).shift(DOWN * 1.5 + LEFT * 2.7)
        result2 = Tex("1", font_size=60).shift(UP * 1 + LEFT * 3.3)
        self.play(Create(line))
        self.wait(1)
        self.play(FadeIn(highlight_rect))
        self.wait(1)
        self.play(Create(s_result)) 
        self.wait(1)                              
        self.play(Create(result1))
        self.wait(1)
        self.play(FadeIn(result2)) 
        self.wait(1) 
        self.play(FadeOut(highlight_rect))
        highlight_rect2 = Rectangle(width=0.5, height=2.5, color=BLUE, fill_opacity=0.2).shift(LEFT * 3.3 + UP * 0.25)
        self.wait(1)
        self.play(FadeIn(highlight_rect2))
        result3 = Tex("7", font_size=70).shift(DOWN * 1.5 + LEFT * 3.3)
        self.play(Create(s_result2))
        self.wait(2)
        self.play(Create(result3))
        self.wait(1)
        self.play(FadeOut(highlight_rect2))
        line2_start  = num2.get_corner(DOWN + LEFT) + DOWN * 1- RIGHT * 0.5
        line2_end = line2_start + RIGHT  * 2
        line2 = Line(line2_start, line2_end)
        self.play(Create(line2))

        self.wait(2)
    
    def AdditionExample3(self):
        fraction_heading = MathTex("Example 3: ", r" 472 + 548", font_size=36).to_edge(UP*3 + LEFT)
        num1 = Tex("4 7 2", font_size=70).shift(LEFT * 3)
        num2 = Tex("5 4 8", font_size=70).shift(DOWN * 0.6 + LEFT * 3)
        plus_sign = Tex("+").scale(1.5).shift(DOWN * 0.6 + LEFT * 4.1)
        line_start = num2.get_corner(DOWN + LEFT) + DOWN * 0.3- RIGHT * 0.5   
        line_end = line_start + RIGHT * 3 
        line = Line(line_start, line_end)
        s_result = Tex(r" 2 + 8 = 10", font_size=60,color=BLUE).shift(UP* 1 + RIGHT * 3)
        s_result2= Tex(r" 1 + 7 + 4 = 12", font_size=60,color=GREEN).shift(UP* 0.2 + RIGHT * 3)
        s_result3= Tex(r" 1 + 4 + 5 = 10", font_size=60,color=YELLOW).shift(DOWN*0.5 + RIGHT * 3)

        self.play(Write(fraction_heading))
        self.play(Write(num1))
        self.wait(1)
        self.play(Write(num2))
        self.wait(1)
        self.play(Create(line))
        self.wait(1)
        self.play(Write(plus_sign))
        self.wait(1)
        # Units place addition
        highlight_rect1 = Rectangle(width=0.5, height=1.5, color=RED, fill_opacity=0.2).shift(DOWN * 0.2 + LEFT * 2.4)
        self.play(FadeIn(highlight_rect1))
        self.wait(1)
        result1 = Tex("0", font_size=70).shift(DOWN * 1.5 + LEFT * 2.4)
        carry1 = Tex("1", font_size=60).shift(UP * 1 + LEFT * 3)
        self.play(Create(s_result))
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
        carry2 = Tex("1", font_size=60).shift(UP * 1 + LEFT * 3.6)
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
        
        line2_start  = num2.get_corner(DOWN + LEFT) + DOWN * 1.3- RIGHT * 0.5
        line2_end = line2_start + RIGHT  * 3
        line2 = Line(line2_start, line2_end)
        self.play(Create(line2))
        self.wait(2)
        
    
    def AdditionExample4(self):
        fraction_heading = MathTex("Example 4: ", r" 472 + 548", font_size=36).to_edge(UP*3 + LEFT)
        num1 = Tex("5 4 3", font_size=70).shift(LEFT * 3)
        num2 = Tex("6 9 8", font_size=70).shift(DOWN * 0.6 + LEFT * 3)
        plus_sign = Tex("+").scale(1.5).shift(DOWN * 0.6 + LEFT * 4.1)
        line_start = num2.get_corner(DOWN + LEFT) + DOWN * 0.3- RIGHT * 0.5   
        line_end = line_start + RIGHT * 3 
        line = Line(line_start, line_end)
        s_result = Tex(r" 3 + 8 = 11", font_size=60,color=BLUE).shift(UP* 1 + RIGHT * 3)
        s_result2= Tex(r" 9 + 4 + 1 = 14", font_size=60,color=GREEN).shift(UP* 0.2 + RIGHT * 3)
        s_result3= Tex(r" 5 + 6 + 1 = 12", font_size=60,color=YELLOW).shift(DOWN*0.5 + RIGHT * 3)

        self.play(Write(fraction_heading))
        self.play(Write(num1))
        self.wait(1)
        self.play(Write(num2))
        self.wait(1)
        self.play(Create(line))
        self.wait(1)
        self.play(Write(plus_sign))
        self.wait(1)
        # Units place addition
        highlight_rect1 = Rectangle(width=0.5, height=1.5, color=RED, fill_opacity=0.2).shift(DOWN * 0.2 + LEFT * 2.4)
        self.play(FadeIn(highlight_rect1))
        self.wait(1)
        result1 = Tex("1", font_size=70).shift(DOWN * 1.5 + LEFT * 2.4)
        carry1 = Tex("1", font_size=60).shift(UP * 1 + LEFT * 3)
        self.play(Create(s_result))
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
        result2 = Tex("4", font_size=70).shift(DOWN * 1.5 + LEFT * 3)
        carry2 = Tex("1", font_size=60).shift(UP * 1 + LEFT * 3.6)
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
        result3 = Tex("1 2 ", font_size=70).shift(DOWN * 1.5 + LEFT * 3.8)
        self.play(Create(s_result3))
        self.wait(1)
        self.play(Create(result3))
        self.wait(1)
        self.play(FadeOut(highlight_rect3))
        
        line2_start  = num2.get_corner(DOWN + LEFT) + DOWN * 1.3- RIGHT * 0.5
        line2_end = line2_start + RIGHT  * 3
        line2 = Line(line2_start, line2_end)
        self.play(Create(line2))
        self.wait(2)
        

if __name__ == "__main__":
    scene = AdditionAnim()
    scene.render()
