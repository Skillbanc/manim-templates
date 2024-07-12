import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class Grade1Chapter12Tens10to100Anim(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.first()
        self.fadeOutCurrentScene()
        self.page1()
        self.fadeOutCurrentScene()
        self.page2()
        self.fadeOutCurrentScene()
        self.extro()
        self.fadeOutCurrentScene()
        self.extro1()
        self.fadeOutCurrentScene()
        self.intro2()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

    def SetDeveloperList(self):
        self.DeveloperList = "Lasya Nannapaneni" 

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName = "Grade1Chapter12Tens10to100Anim.py"     
    
    def first(self):
        title = Text("Tens from 10 to 100",font_size=45,color=BLUE).move_to([-3.5,3.3,0])
        u = Underline(title)
        subtil = Text("Numbers can be grouped into tens. This helps us\n\n"
                      "understand and count larger numbers easily.",font_size=28).move_to([-2.25,2,0])
        self.play(Write(title))
        self.play(Write(u))
        self.play(Write(subtil,run_time=6))
        self.wait()


        formula_steps = [
            Text("What are tens?",font_size=30,color=BLUE).shift(LEFT*3),
            Text("A 'ten' is a group of 10 units. \n\n Example, 10 ones make one ten" ,font_size=28,color=WHITE).shift(DOWN),           
                       
        ]
         
        for step in formula_steps:
            self.play(Write(step))
            self.wait(2)

        self.fadeOutCurrentScene()    


        title1 = Text("PATTERN",font_size=45,color=BLUE).move_to([-3.5,3.3,0])
        u1 = Underline(title1) 
        self.play(Write(title1))
        self.play(Write(u1))  

        pattern_steps = [
            Text("10 (one ten and zero ones)",font_size=30,color=WHITE).shift(UP*2),
            Text("20 (two tens and zero ones)" ,font_size=30,color=WHITE).shift(UP),           
            Text("30 (three tens and zero ones)",font_size=30,color=WHITE),           
            Text("So on...This continues upto \n 100 (ten tens and zero ones).",font_size=30,color=WHITE).shift(DOWN),
        ]
         
        for step in pattern_steps:
            self.play(Write(step))
            self.wait(2) 


    def page1(self):

        self.isRandom =  False
        self.positionChoice=[[-5,2,0],[-2.5,2,0],[0,2,0],[2,2,0],[-5,-2,0],[-2.5,-2,0],[0,-2,0],[2,-2,0],[4,2,0],[4,-2,0]]

        p1 = cvo.CVO().CreateCVO("Number","10")
        p2 = cvo.CVO().CreateCVO("tens place","1")
        p1.cvolist.append(p2)
        self.construct1(p1,p1)

        p3 = cvo.CVO().CreateCVO("Number","20")
        p4 = cvo.CVO().CreateCVO("tens place","2")
        p3.cvolist.append(p4)
        self.construct1(p3,p3)

        p5 = cvo.CVO().CreateCVO("Number","30")
        p6 = cvo.CVO().CreateCVO("tens place","3")
        p5.cvolist.append(p6)
        self.construct1(p5,p5)

        p7 = cvo.CVO().CreateCVO("Number","40")
        p8 = cvo.CVO().CreateCVO("tens place","4")
        p7.cvolist.append(p8)
        self.construct1(p7,p7)

        p9 = cvo.CVO().CreateCVO("Number","50")
        p10 = cvo.CVO().CreateCVO("tens place","5")
        p9.cvolist.append(p10)
        self.construct1(p9,p9)


    def page2(self):
        
        self.isRandom =  False
        self.positionChoice=[[-5,2,0],[-2.5,2,0],[0,2,0],[2,2,0],[-5,-2,0],[-2.5,-2,0],[0,-2,0],[2,-2,0],[4,2,0],[4,-2,0]]

        p11 = cvo.CVO().CreateCVO("Number","60")
        p12 = cvo.CVO().CreateCVO("tens place","6")
        p11.cvolist.append(p12)
        self.construct1(p11,p11)

        p13 = cvo.CVO().CreateCVO("Number","70")
        p14 = cvo.CVO().CreateCVO("tens place","7")
        p13.cvolist.append(p14)
        self.construct1(p13,p13)

        p15 = cvo.CVO().CreateCVO("Number","80")
        p16 = cvo.CVO().CreateCVO("tens place","8")
        p15.cvolist.append(p16)
        self.construct1(p15,p15)

        p17 = cvo.CVO().CreateCVO("Number","90")
        p18 = cvo.CVO().CreateCVO("tens place","9")
        p17.cvolist.append(p18)
        self.construct1(p17,p17)

        p19 = cvo.CVO().CreateCVO("Number","100")
        p20 = cvo.CVO().CreateCVO("tens place","10")
        p19.cvolist.append(p20)
        self.construct1(p19,p19)


    
    def extro1(self):

    
        i3= [-4.6,-0.5,0]
        s3=0.5
        squares = VGroup()

        for i in range(8):  
            for j in range(2):  
            
                x = i3[0] + j * s3
                y = i3[1] + i * s3

                square = Square(color=WHITE, side_length=0.5, fill_opacity=0.2).move_to([x, y, 0])
                squares.add(square)

        self.play(Create(squares, lag_ratio=0))  
        self.wait(1)  

        ans1 = Rectangle(height=1,width=1.5)
        ans1.move_to([-4.2,-1.5,0])
        self.play(Write(ans1))        


        i4= [-1,-0.5,0]
        s4=0.5
        squares = VGroup()

        for i in range(8):
            for j in range(3):
                x = i4[0] + j * s4
                y = i4[1] + i * s4

                square = Square(color=WHITE, side_length=0.5, fill_opacity=0.2).move_to([x, y, 0])
                squares.add(square)

        self.play(Create(squares, lag_ratio=0))  
        self.wait(1)       
        
        ans2 = Rectangle(height=1,width=1.5)
        ans2.move_to([-0.4,-1.5,0])
        self.play(Write(ans2)) 

        t3 = Text("Count the grid and Find\n\n"
                  "out the number of tiny boxes.",font_size=32)
        t3.move_to([3.5,0,0])
        self.play(Write(t3))
        self.wait(3)

        a1 = Text("16")
        a1.move_to([-4.2,-1.5,0])
        a2 = Text("24")
        a2.move_to([-0.4,-1.5,0])

        self.play(Write(a1))
        self.play(Write(a2))


    def extro(self):
        
        h1 = Tex("Count in Tens")
        h1.move_to([-5,3.5,0])
        self.play(Write(h1))

        table_data1 = [
            ["10", "1 ten", "10\n\nten"],
            ["10 + 10", "2 tens", "20\n\ntwenty"],
            ["20 + 10", "3 tens", "30\n\nthirty"],
            ["30 + 10", "4 tens", "40\n\nforty"],
            ["40 + 10", "5 tens", "50\n\nfifty"]
        ]
        
        table_data2 = [
            ["50 + 10", "6 tens", "60\n\nsixty"],
            ["60 + 10", "7 tens", "70\n\nseventy"],
            ["70 + 10", "8 tens", "80\n\neighty"],
            ["80 + 10", "9 tens", "90\n\nninety"],
            ["90 + 10", "10 tens", "100\n\nhundred"]
        ]

        table1 = Table(
            table_data1,
            top_left_entry=Star().scale(0.3),
            include_outer_lines=True,
            arrange_in_grid_config={"cell_alignment": LEFT}
        )
        
        table1.move_to([-3.5, -0.5, 0]).scale(0.5)

        
        self.play(Create(table1.get_horizontal_lines()), Create(table1.get_vertical_lines()))
        for row in table1.get_rows():
            self.play(Create(row), run_time=1)
        self.wait(1)
        
        table2 = Table(
            table_data2,
            top_left_entry=Star().scale(0.3),
            include_outer_lines=True,
            arrange_in_grid_config={"cell_alignment": LEFT}
        )
        
        table2.move_to([3.5, -0.5, 0]).scale(0.5)


        self.play(Create(table2.get_horizontal_lines()), Create(table2.get_vertical_lines()))
        for row in table2.get_rows():
            self.play(Create(row), run_time=1)
        self.wait(5)
    

    def intro2(self):

        h2 = Text("Match the following with the correct answers:", font_size=30)
        h2.move_to([-2.7,3.5,0])
        self.play(Write(h2))

        r1 = Rectangle(height=1,width=2.5,color=ORANGE,fill_opacity=0.5).move_to([-3.5,2,0])
        self.play(Write(r1))
        r2 = Rectangle(height=1, width=2.5, color=BLUE, fill_opacity=0.5).next_to(r1,DOWN)
        self.play(Write(r2))
        r3= Rectangle(height=1, width=2.5, color=GREEN, fill_opacity=0.5).next_to(r2,DOWN)
        self.play(Write(r3))
        r4= Rectangle(height=1, width=2.5, color=RED, fill_opacity=0.5).next_to(r3,DOWN)
        self.play(Write(r4))
        r5= Rectangle(height=1, width=2.5, color=YELLOW, fill_opacity=0.5).next_to(r4,DOWN)
        self.play(Write(r5))

        m =Text("10+10\n\n30+10\n\n40+10\n\n70+10\n\n80+10").move_to([-3.5,-0.5,0])
        self.play(Write(m))

        a1 = Rectangle(height=1,width=2.5,color=BLUE,fill_opacity=0.5).move_to([3.5,2,0])
        self.play(Write(a1))
        a2 = Rectangle(height=1, width=2.5, color=YELLOW, fill_opacity=0.5).next_to(a1,DOWN)
        self.play(Write(a2))
        a3= Rectangle(height=1, width=2.5, color=RED, fill_opacity=0.5).next_to(a2,DOWN)
        self.play(Write(a3))
        a4= Rectangle(height=1, width=2.5, color=ORANGE, fill_opacity=0.5).next_to(a3,DOWN)
        self.play(Write(a4))
        a5= Rectangle(height=1, width=2.5, color=GREEN, fill_opacity=0.5).next_to(a4,DOWN)
        self.play(Write(a5))

        m1 =Text("40\n\n90\n\n80\n\n20\n\n50").move_to([3.5,-0.5,0])
        self.play(Write(m1))

        a1 = Arrow(start=[-1.7,2,0],end=[2.4,-1.5,0],color=ORANGE)
        a2 = Arrow(start=[-1.7,0.7,0],end=[2.4,2,0],color=BLUE)
        a3 = Arrow(start=[-1.7,-0.5,0],end=[2.4,-3,0],color=GREEN)
        a4 = Arrow(start=[-1.7,-1.5,0],end=[2.4,-0.5,0],color=RED)
        a5 = Arrow(start=[-1.7,-3,0],end=[2.4,0.7,0],color=YELLOW)
 
        self.play((Write(a1)), run_time=1)
        self.play((Write(a2)), run_time=1)
        self.play((Write(a3)), run_time=1)
        self.play((Write(a4)), run_time=1)
        self.play((Write(a5)), run_time=1)     


if __name__ == "__main__":
    scene = Grade1Chapter12Tens10to100Anim()
    scene.render()