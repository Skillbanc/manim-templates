from manim import*
import json
import cvo
from AbstractAnim import AbstractAnim

class AdditionOfNumbersTotalNotExceeding9(AbstractAnim):
    def construct(self):
        self.addition()
        self.fadeOutCurrentScene()
        self.example()
        self.fadeOutCurrentScene()
        self.excircles()
        self.fadeOutCurrentScene()
        self.examples()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        self.fadeOutCurrentScene()

    def addition(self):
        self.isRandom=False
        self.setNumberOfCirclePositions(2)
        p10=cvo.CVO().CreateCVO("Addition","")
        p11=cvo.CVO().CreateCVO("Symbol","+")
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def example(self):
        example=Text("Examples:").to_edge(UP)
        
        box1 = Square(side_length=1, color=BLUE)
        box2 = Square(side_length=1, color=BLUE)

        box1.shift(LEFT+UP*2)
        box2.shift(RIGHT+UP*2)
        box1.shift(LEFT*2)    
        box2.shift(LEFT*2)    


        symb=Text("+").next_to(box1,RIGHT*1.2)
        oneb=Text("1").next_to(box1,DOWN)
        onea=Text("1").next_to(box2,DOWN)
        
        equ=Text("=").next_to(box2,RIGHT*1.2)

        box3 = Square(side_length=1, color=BLUE).next_to(equ,RIGHT*1.2)
        box4 = Square(side_length=1, color=BLUE).next_to(box3,RIGHT*0.5)
        two=Text("2").next_to(box4,DOWN).shift(LEFT*0.5)

        self.play(Write(example))

        self.play(Write(box1,run_time=3), Write(box2,run_time=3))
        self.play(Write(onea),Write(oneb),Write(symb))
        
        self.play(Write(equ))
        
        self.play(Write(box3,run_time=3), Write(box4,run_time=3))
        self.play(Write(two))
        
        #e2
        box5 = Square(side_length=1, color=BLUE)
        box6 = Square(side_length=1, color=BLUE)
        box7 = Square(side_length=1, color=BLUE).next_to(box6,RIGHT*0.5)
        box8 = Square(side_length=1, color=BLUE).next_to(box7,RIGHT*0.5)

        box5.shift(LEFT * 4)
        box6.shift(LEFT * 2)
        box7.shift(LEFT * 2)
        box8.shift(LEFT * 2)
        symb2 = Text("+").next_to(box5, RIGHT * 1.2)
        oneb2 = Text("1").next_to(box5, DOWN)
        three = Text("3").next_to(box7, DOWN)
        
        equ2 = Text("=").next_to(box8, RIGHT * 1.2)
        
        box9 = Square(side_length=1, color=BLUE).next_to(equ2, RIGHT * 1.2)
        box10 = Square(side_length=1, color=BLUE).next_to(box9, RIGHT * 0.5)
        box11 = Square(side_length=1, color=BLUE).next_to(box10, RIGHT * 0.5)
        box12 = Square(side_length=1, color=BLUE).next_to(box11, RIGHT * 0.5)
        four = Text("4").next_to(box12, DOWN).shift(LEFT * 1.5)

        self.play(Write(box5, run_time=2),Write(box6, run_time=2),Write(box7, run_time=2), Write(box8, run_time=2))
        self.play(Write(oneb2), Write(three), Write(symb2))
        self.play(Write(equ2))
        self.play(Write(box9, run_time=2), Write(box10, run_time=2), Write(box11, run_time=2), Write(box12, run_time=2))
        self.play(Write(four))

        # Example 3: 1 + 4 = 5
        box13 = Square(side_length=1, color=BLUE)
        box14 = Square(side_length=1, color=BLUE)
        box15 = Square(side_length=1, color=BLUE).next_to(box14,RIGHT*0.5)
        box16 = Square(side_length=1, color=BLUE).next_to(box15,RIGHT*0.5)
        box17 = Square(side_length=1, color=BLUE).next_to(box16,RIGHT*0.5)
        
        box13.shift(LEFT * 6 + DOWN * 2)
        box14.shift(LEFT * 4 + DOWN * 2)
        box15.shift(LEFT * 4 + DOWN * 2)
        box16.shift(LEFT * 4 + DOWN * 2)
        box17.shift(LEFT * 4 + DOWN * 2)
        
        symb3 = Text("+").next_to(box13, RIGHT * 1.2)
        oneb3 = Text("1").next_to(box13, DOWN)
        four3 = Text("4").next_to(box16, DOWN).shift(LEFT*0.7)
        
        equ3 = Text("=").next_to(box17, RIGHT * 1.2)
        
        box18 = Square(side_length=1, color=BLUE).next_to(equ3, RIGHT * 1.2)
        box19 = Square(side_length=1, color=BLUE).next_to(box18, RIGHT * 0.5)
        box20 = Square(side_length=1, color=BLUE).next_to(box19, RIGHT * 0.5)
        box21 = Square(side_length=1, color=BLUE).next_to(box20, RIGHT * 0.5)
        box22 = Square(side_length=1, color=BLUE).next_to(box21, RIGHT * 0.5)
        five = Text("5").next_to(box22, DOWN).shift(LEFT * 2)
        
        self.play(Write(box13, run_time=2), Write(box14, run_time=2),Write(box15, run_time=2),Write(box16, run_time=2), Write(box17, run_time=2))
        self.play(Write(oneb3), Write(four3), Write(symb3))
        self.play(Write(equ3))
        self.play(Write(box18, run_time=2), Write(box19, run_time=2), Write(box20, run_time=2), Write(box21, run_time=2), Write(box22, run_time=2))
        self.play(Write(five))
        # Move the second box to the right to show addition
        # self.play(ApplyMethod(box2.shift, RIGHT))
        
        self.wait(3)

    def excircles(self):
        example = Text("Examples:", font_size=34).to_edge(UP)
        
        # Example 1: 3 + 2 = 5
        c1 = Circle(radius=0.3, color=RED).shift(LEFT * 6 + UP * 2)
        c2 = Circle(radius=0.3, color=RED).next_to(c1, RIGHT * 1.2)
        c3 = Circle(radius=0.3, color=RED).next_to(c2, RIGHT * 1.2)
        
        plus = Text("+").next_to(c3, RIGHT * 1.2)
        c4 = Circle(radius=0.3, color=RED).next_to(plus, RIGHT * 1.2)
        c5 = Circle(radius=0.3, color=RED).next_to(c4, RIGHT * 1.2)
        
        three = Text("3").next_to(c2, DOWN)
        two = Text("2").next_to(c4, DOWN).shift(RIGHT * 0.6)
        
        equal = Text("=").next_to(c5, RIGHT * 1.2)
        
        result_c1 = Circle(radius=0.3, color=RED).next_to(equal, RIGHT * 1.2)
        result_c2 = Circle(radius=0.3, color=RED).next_to(result_c1, RIGHT * 0.5)
        result_c3 = Circle(radius=0.3, color=RED).next_to(result_c2, RIGHT * 0.5)
        result_c4 = Circle(radius=0.3, color=RED).next_to(result_c3, RIGHT * 0.5)
        result_c5 = Circle(radius=0.3, color=RED).next_to(result_c4, RIGHT * 0.5)
        
        five = Text("5").next_to(result_c5, DOWN).shift(LEFT * 2)

        self.play(Write(example))
        self.play(Write(c1), Write(c2), Write(c3), Write(c4), Write(c5))
        self.play(Write(three), Write(two), Write(plus))
        self.play(Write(equal))
        self.play(Write(result_c1), Write(result_c2), Write(result_c3), Write(result_c4), Write(result_c5))
        self.play(Write(five))

        # Example 2: 4 + 2 = 6
        c6 = Circle(radius=0.3, color=GREEN).shift(LEFT * 6)
        c7 = Circle(radius=0.3, color=GREEN).next_to(c6, RIGHT * 1.2)
        c8 = Circle(radius=0.3, color=GREEN).next_to(c7, RIGHT * 1.2)
        c9 = Circle(radius=0.3, color=GREEN).next_to(c8, RIGHT * 1.2)
        
        plus2 = Text("+").next_to(c9, RIGHT * 1.2)
        c10 = Circle(radius=0.3, color=GREEN).next_to(plus2, RIGHT * 1.2)
        c11 = Circle(radius=0.3, color=GREEN).next_to(c10, RIGHT * 1.2)
        
        four = Text("4").next_to(c6, DOWN).shift(RIGHT * 2)
        two2 = Text("2").next_to(c10, DOWN).shift(RIGHT * 0.6)
        
        equal2 = Text("=").next_to(c11, RIGHT * 1.2)
        
        result_c6 = Circle(radius=0.3, color=GREEN).next_to(equal2, RIGHT * 1.2)
        result_c7 = Circle(radius=0.3, color=GREEN).next_to(result_c6, RIGHT * 0.5)
        result_c8 = Circle(radius=0.3, color=GREEN).next_to(result_c7, RIGHT * 0.5)
        result_c9 = Circle(radius=0.3, color=GREEN).next_to(result_c8, RIGHT * 0.5)
        result_c10 = Circle(radius=0.3, color=GREEN).next_to(result_c9, RIGHT * 0.5)
        result_c11 = Circle(radius=0.3, color=GREEN).next_to(result_c10, RIGHT * 0.5)
        
        six = Text("6").next_to(result_c11, DOWN).shift(LEFT * 2.5)
        
        self.play(Write(c6), Write(c7), Write(c8), Write(c9), Write(c10), Write(c11))
        self.play(Write(four), Write(two2), Write(plus2))
        self.play(Write(equal2))
        self.play(Write(result_c6), Write(result_c7), Write(result_c8), Write(result_c9), Write(result_c10), Write(result_c11))
        self.play(Write(six))

        # Example 3: 7 + 1 = 8
        c12 = Circle(radius=0.3, color=BLUE).shift(LEFT * 6 + DOWN * 2)
        c13 = Circle(radius=0.3, color=BLUE).next_to(c12, RIGHT * 1.2)
        c14 = Circle(radius=0.3, color=BLUE).next_to(c13, RIGHT * 1.2)
        c15 = Circle(radius=0.3, color=BLUE).next_to(c14, RIGHT * 1.2)
        c16 = Circle(radius=0.3, color=BLUE).next_to(c15, RIGHT * 1.2)
        c17 = Circle(radius=0.3, color=BLUE).next_to(c16, RIGHT * 1.2)
        c18 = Circle(radius=0.3, color=BLUE).next_to(c17, RIGHT * 1.2)
        
        plus3 = Text("+").next_to(c18, RIGHT * 1.2)

        c19 = Circle(radius=0.3, color=BLUE).next_to(plus3,RIGHT*1.2)
        
        seven = Text("7").next_to(c12, DOWN).shift(RIGHT * 3.6)
        one = Text("1").next_to(c19, DOWN)
        
        equal3 = Text("=").next_to(c19, RIGHT * 1.2)
        
        result_c12 = Circle(radius=0.3, color=BLUE).next_to(equal3, RIGHT * 1.2)
        result_c13 = Circle(radius=0.3, color=BLUE).next_to(result_c12, RIGHT * 0.5)
        result_c14 = Circle(radius=0.3, color=BLUE).next_to(result_c13, RIGHT * 0.5)
        result_c15 = Circle(radius=0.3, color=BLUE).next_to(result_c14, RIGHT * 0.5)
        result_c16 = Circle(radius=0.3, color=BLUE).next_to(result_c15, RIGHT * 0.5)
        result_c17 = Circle(radius=0.3, color=BLUE).next_to(result_c16, RIGHT * 0.5)
        result_c18 = Circle(radius=0.3, color=BLUE).next_to(result_c17, RIGHT * 0.5)
        result_c19 = Circle(radius=0.3, color=BLUE).next_to(result_c18, RIGHT * 0.5)
        
        eight = Text("8").next_to(result_c19, DOWN).shift(LEFT * 3)

        self.play(Write(c12,run_time=2), Write(c13,run_time=2), Write(c14,run_time=2), Write(c15,run_time=2), Write(c16,run_time=2), Write(c17,run_time=2), Write(c18,run_time=2), Write(c19,run_time=2))
        self.play(Write(seven), Write(one), Write(plus3))
        self.play(Write(equal3))
        self.play(Write(result_c12,run_time=2), Write(result_c13,run_time=2), Write(result_c14,run_time=2), Write(result_c15,run_time=2), Write(result_c16,run_time=2), Write(result_c17,run_time=2), Write(result_c18,run_time=2), Write(result_c19,run_time=2))
        self.play(Write(eight))

        self.wait(4)

    def examples(self):
        t1=Text("Some examples to work on :",font_size=36).to_edge(UP)
        s1=Text("4 + 2 = ",color=YELLOW,font_size=30).next_to(t1,DOWN*1.4)
        ss1=Square(side_length=0.7).next_to(s1,RIGHT)
        s12=Text("6",color=BLUE,font_size=30).move_to(ss1.get_center())
        self.play(Write(t1))
        self.play(Write(s1,run_time=3))
        self.play(Write(ss1,run_time=2))
        self.play(Write(s12))
        
        s2=Text("4 + 3 = ",color=YELLOW,font_size=30).next_to(s1,DOWN*2)
        ss2=Square(side_length=0.7).next_to(s2,RIGHT)
        s22=Text("7",color=BLUE,font_size=30).move_to(ss2.get_center())
        self.play(Write(s2,run_time=3))
        self.play(Write(ss2,run_time=2))
        self.play(Write(s22))

        s3=Text("7 + 2 = ",color=YELLOW,font_size=30).next_to(s2,DOWN*2)
        ss3=Square(side_length=0.7).next_to(s3,RIGHT)
        s32=Text("9",color=BLUE,font_size=30).move_to(ss3.get_center())
        self.play(Write(s3,run_time=3))
        self.play(Write(ss3,run_time=2))
        self.play(Write(s32))




    def SetDeveloperList(self): 
       self.DeveloperList="T Sai Rohith Reddy" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade1Chapter7AdditionOfNumbersTotalNotExceeding9.py"

if __name__=="__main__":
    Scene=AdditionOfNumbersTotalNotExceeding9()
    Scene.render()