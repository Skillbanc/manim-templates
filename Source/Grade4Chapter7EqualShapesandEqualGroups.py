import json
from manim import*
from AbstractAnim import AbstractAnim
import cvo

class EqualShapesandEqualGroups(AbstractAnim):
    def construct(self):
        self.group()
        self.fadeOutCurrentScene()
        self.division()
        self.fadeOutCurrentScene()
        self.divbig()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

    def group(self):
        self.isRandom=False
        self.setNumberOfCirclePositions(2)
        p10=cvo.CVO().CreateCVO("Group","")
        p11=cvo.CVO().CreateCVO("Definition","A number of people or things.")
        p10.cvolist.append(p11)
        self.construct1(p10,p10)
        
    def division(self):
        t1=Text("To divide a group using division, you split the group into equal parts.",font_size=24).to_edge(UP)
        t2=Text("example:",font_size=24).next_to(t1,DOWN)
        t3=Text(" If 12 is to be divided into 4 equal groups",font_size=24).next_to(t2,DOWN)
        self.play(Write(t1,run_time=4))
        self.play(Write(t2,run_time=2))
        self.play(Write(t3,run_time=3))
        
        problem = MathTex(r"12 \div 4 =").next_to(t3,DOWN)
        self.play(Write(problem))
        self.wait(1)
        struc=MathTex(r"4 \overline{) \,12").next_to(problem, DOWN * 2)
        self.play(Write(struc))
        self.wait(1)
        t4=Text("3",font_size=30).next_to(struc,UP*0.1)
        mul=Text("Multiplication :",font_size=24).to_edge(RIGHT)
        t5=Text("4 x 3 = 12 ",font_size=24).next_to(mul,DOWN*0.3)
        # t5.shift(RIGHT*2.5)
        t6=MathTex(r"12 ").next_to(struc,DOWN*0.1)
        t6.shift(RIGHT*0.25)
        t7=MathTex(r"\overline{ \,0").next_to(t6,DOWN*0.2)
        t8=MathTex(r"\therefore 12 \div4 = 3").to_edge(DOWN*2)
        
        mul.shift(LEFT*2)
        t5.shift(LEFT*2)
        self.play(Write(mul))
        self.play(Write(t5))

        
        self.play(Write(t6))
        self.play(Write(t4))
        self.play(Write(t7))
        self.play(Write(t8,run_time=3))
        self.wait(3)
        
        self.play(FadeOut(t1), FadeOut(t2), FadeOut(t3), FadeOut(problem),FadeOut(t5),FadeOut(mul))
        self.wait(2)

        rem=Text("Remainder",font_size=24).next_to(t7,RIGHT*2)
        quo=Text("Quotient",font_size=24).next_to(t4,UP*2)
        remarrow = Arrow(t7.get_right(), rem.get_left(), buff=0.1)
        quoarrow = Arrow(t4.get_top(), quo.get_bottom(), buff=0.1)
        
        # Animate the remainder and quotient text with arrows
        self.play(FadeIn(rem), FadeIn(remarrow))
        self.play(FadeIn(quo), FadeIn(quoarrow))
        self.wait(2)
        
    def divbig(self):
        t1=Text("Division for larger numbers",font_size=30).to_edge(UP)
        t2=Text("Long Division Methods : ",font_size=24,color=BLUE).next_to(t1,DOWN)
        self.play(Write(t1))
        self.play(Write(t2,run_time=2))
        self.wait(2)
        self.play(FadeOut(t1))
        t2.shift(UP*1)
        
        t3=Text("Method 1:",font_size=24).to_corner(UL)
        self.play(Write(t3))
        problem = MathTex(r"250 \div 2 :").to_edge(UP)
        self.play(Write(problem))
        self.wait(1)
        
        # Structure of the division
        struc = MathTex(r"2 \overline{) \,250}").next_to(problem, DOWN * 3)
        self.play(Write(struc))
        self.wait(1)
       
        # Write the quotient on top
        t4 = Text("1", font_size=30).next_to(struc, UP * 0.5)
        t41 = Text("2", font_size=30).next_to(t4, RIGHT * 0.1)
        t42= Text("5", font_size=30).next_to(t41, RIGHT * 0.1)
        
        # Multiplication steps
        mul = Text("Multiplication:", font_size=24,color=YELLOW).to_edge(RIGHT)
        t5_1 = Text("2 x 1 = 2", font_size=24).next_to(mul, DOWN * 0.3)
        t5_2 = Text("2 x 2 = 4", font_size=24).next_to(t5_1, DOWN * 0.3)
        t5_3 = Text("2 x 5 = 10", font_size=24).next_to(t5_2, DOWN * 0.3)
        
        # Steps of subtraction
        t6_1 = MathTex(r"2").next_to(struc, DOWN * 0.1)#.shift(RIGHT * 0.4)
        t7_1 = MathTex(r"\overline{\,05\phantom{0}}").next_to(t6_1, DOWN * 0.2).shift(RIGHT*0.2)
        start_point = struc.get_bottom() + UP * 0.3 +RIGHT*0.2
        end_point = t7_1.get_top() +DOWN*0.3
        arr1=Arrow(start_point,end_point)

        t6_2 = MathTex(r"4 ").next_to(t7_1, DOWN * 0.1)
        t7_2 = MathTex(r"\overline{\,010\phantom{0}}").next_to(t6_2, DOWN * 0.2).shift(RIGHT*0.1)
        
        t6_3 = MathTex(r"10").next_to(t7_2, DOWN * 0.1).shift(RIGHT*0.1)
        t7_3 = MathTex(r"\overline{\,\phantom{0}0\phantom{0} }").next_to(t6_3, DOWN * 0.2)
        startp=struc.get_bottom() + UP*0.2 +RIGHT*0.5
        endp=t6_3.get_top()+ UP*0.2 +RIGHT*0.1
        arr2=Arrow(startp,endp)

        t8 = MathTex(r"\therefore 250 \div 2 = 125").to_edge(DOWN * 2)
        
        mul.shift(LEFT * 2)
        t5_1.shift(LEFT * 2)
        t5_2.shift(LEFT * 2)
        t5_3.shift(LEFT * 2)
        
        m1=Text("-").next_to(t6_1,LEFT*0.2)
        m2=Text("-").next_to(t6_2,LEFT*0.2)
        m3=Text("-").next_to(t6_3,LEFT*0.2)

        # Play the animations
        
        self.play(Write(mul))
        self.play(Write(t5_1))
        self.play(Write(t4))
        self.play(Write(t6_1))
        self.play(Write(m1))
        self.play(Write(arr1))
        self.play(Write(t7_1))
        
        self.play(Write(t5_2))
        self.play(Write(t41))
        self.play(Write(t6_2))
        self.play(Write(m2))
        self.play(Write(t7_2))
        
        self.play(Write(arr2))
        self.play(Write(t5_3))
        self.play(Write(t42))
        self.play(Write(t6_3))
        self.play(Write(m3))
        self.play(Write(t7_3))
        
        self.play(Write(t8, run_time=3))
        self.wait(3)
        
        self.play(FadeOut(problem), FadeOut(mul), FadeOut(t5_1), FadeOut(t5_2), FadeOut(t5_3))
        self.wait(2)
        
        rem = Text("Remainder", font_size=24).next_to(t7_3, RIGHT * 2)
        quo = Text("Quotient", font_size=24).next_to(t4, UP * 2)
        pt=t7_3.get_right()
        remarrow = Arrow(pt, rem.get_left(), buff=0.1)
        quoarrow = Arrow(t4.get_top(), quo.get_bottom(), buff=0.1)
        
        # Animate the remainder and quotient text with arrows
        self.play(FadeIn(rem), FadeIn(remarrow))
        self.play(FadeIn(quo), FadeIn(quoarrow))
        self.wait(2)
        self.fadeOutCurrentScene()
        
        
        #m2
        p1=Text("Method 2:",font_size=24).to_corner(UL)
        self.play(Write(p1))

        problem = MathTex(r"250 \div 2 =").to_edge(UP)
        self.play(Write(problem))
        self.wait(1)
        struc=MathTex(r"2 \overline{) \,\phantom{00}250\phantom{00}").next_to(problem, DOWN * 2)
        self.play(Write(struc))
        self.wait(1)
        t4=Text("100",font_size=30).next_to(struc,UP*0.1).shift(LEFT*0.5)
        t41=Text("+",font_size=30).next_to(t4,RIGHT*0.3)
        t42=Text("25",font_size=30).next_to(t41,RIGHT*0.3)
        
        mul=Text("Multiplication :",font_size=24).to_edge(RIGHT)
        t5=Text("2 x 100 = 200 ",font_size=24).next_to(mul,DOWN*0.3)
        t51=Text("2 x 25 = 50 ",font_size=24).next_to(t5,DOWN*0.3)
        
        # t5.shift(RIGHT*2.5)
        t6=MathTex(r"200 ").next_to(struc,DOWN*0.1)
        t6.shift(RIGHT*0.25)
        t7=MathTex(r"\overline{ \,\phantom{0}50\phantom{0}").next_to(t6,DOWN*0.2).shift(RIGHT*0.1)
        t71=MathTex(r"50").next_to(t7,DOWN*0.2).shift(RIGHT*0.05)
        
        t72=MathTex(r"\overline{ \,\phantom{0}0\phantom{0}").next_to(t71,DOWN*0.2)
        
        t8=MathTex(r"\therefore 250 \div2 = 125").to_edge(DOWN*2)
        
        m1=Text("-").next_to(t6,LEFT*0.3)
        m2=Text("-").next_to(t71,LEFT*0.3)
        mul.shift(LEFT*2)
        t5.shift(LEFT*2)
        t51.shift(LEFT*2)
        
        self.play(Write(mul))
        self.play(Write(t5))

        
        self.play(Write(t6))
        self.play(Write(m1))
        
        self.play(Write(t4))
        self.play(Write(t7))
        self.play(Write(t51))
        self.play(Write(t41),Write(t42))
        self.play(Write(t71))
        self.play(Write(m2))
        self.play(Write(t72))
        
        self.play(Write(t8,run_time=3))
        self.wait(3)
        
        # self.play(FadeOut(t1), FadeOut(t2), FadeOut(t3), FadeOut(problem),FadeOut(t5),FadeOut(mul))
        self.wait(2)
        self.play(FadeOut(problem), FadeOut(mul), FadeOut(t5), FadeOut(t51))
        rem=Text("Remainder",font_size=24).next_to(t72,RIGHT*2)
        quo=Text("Quotient",font_size=24).next_to(t4,UP*2)
        remarrow = Arrow(t72.get_right(), rem.get_left(), buff=0.1)
        quoarrow = Arrow(t4.get_top(), quo.get_bottom(), buff=0.1)
        
        # Animate the remainder and quotient text with arrows
        self.play(FadeIn(rem), FadeIn(remarrow))
        self.play(FadeIn(quo), FadeIn(quoarrow))
        self.wait(2)

    def SetDeveloperList(self): 
       self.DeveloperList="T Sai Rohith Reddy" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade4Chapter7EqualShapesandEqualGroups.py"

if __name__ == "__main__":
    Scene=EqualShapesandEqualGroups()
    Scene.render()
