import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class Grade1Chapter12Tens10to100Anim(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.page1()
        self.fadeOutCurrentScene()
        self.page2()
        self.fadeOutCurrentScene()
        self.intro()
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
    

    def page1(self):

        self.isRandom =  False
        self.positionChoice=[[-5,2,0],[-2.5,2,0],[0,2,0],[2,2,0],[-5,-2,0],[-2.5,-2,0],[0,-2,0],[2,-2,0],[4,2,0],[4,-2,0]]

        p1 = cvo.CVO().CreateCVO("10","")
        p2 = cvo.CVO().CreateCVO("1 ten","")
        p1.cvolist.append(p2)
        self.construct1(p1,p1)

        p3 = cvo.CVO().CreateCVO("20","")
        p4 = cvo.CVO().CreateCVO("2 tens","")
        p3.cvolist.append(p4)
        self.construct1(p3,p3)

        p5 = cvo.CVO().CreateCVO("30","")
        p6 = cvo.CVO().CreateCVO("3 tens","")
        p5.cvolist.append(p6)
        self.construct1(p5,p5)

        p7 = cvo.CVO().CreateCVO("40","")
        p8 = cvo.CVO().CreateCVO("4 tens","")
        p7.cvolist.append(p8)
        self.construct1(p7,p7)

        p9 = cvo.CVO().CreateCVO("50","")
        p10 = cvo.CVO().CreateCVO("5 tens","")
        p9.cvolist.append(p10)
        self.construct1(p9,p9)


    def page2(self):
        
        self.isRandom =  False
        self.positionChoice=[[-5,2,0],[-2.5,2,0],[0,2,0],[2,2,0],[-5,-2,0],[-2.5,-2,0],[0,-2,0],[2,-2,0],[4,2,0],[4,-2,0]]

        p11 = cvo.CVO().CreateCVO("60","")
        p12 = cvo.CVO().CreateCVO("6 tens","")
        p11.cvolist.append(p12)
        self.construct1(p11,p11)

        p13 = cvo.CVO().CreateCVO("70","")
        p14 = cvo.CVO().CreateCVO("7 tens","")
        p13.cvolist.append(p14)
        self.construct1(p13,p13)

        p15 = cvo.CVO().CreateCVO("80","")
        p16 = cvo.CVO().CreateCVO("8 tens","")
        p15.cvolist.append(p16)
        self.construct1(p15,p15)

        p17 = cvo.CVO().CreateCVO("90","")
        p18 = cvo.CVO().CreateCVO("9 tens","")
        p17.cvolist.append(p18)
        self.construct1(p17,p17)

        p19 = cvo.CVO().CreateCVO("100","")
        p20 = cvo.CVO().CreateCVO("10 tens","")
        p19.cvolist.append(p20)
        self.construct1(p19,p19)


    def intro(self):

        t0 = Tex(" Introduction of Tens from 10 to 100")

        self.play((Write(t0)),run_time=2)
    
    def extro1(self):

        # self.play(Write(NumberPlane()))

        rec= Rectangle(height=4,width=0.4)
        rec.move_to([-4,1.5,0])
        self.play(Write(rec))
        rec1= Rectangle(height=4,width=0.4)
        rec1.move_to([-4.4,1.5,0])
        self.play(Write(rec1))
        r1 = Line(start=[-4.6,3,0],end=[-3.8,3,0])
        r2= Line(start=[-4.6,2.5,0],end=[-3.8,2.5,0])
        r3= Line(start=[-4.6,2,0],end=[-3.8,2,0])
        r4= Line(start=[-4.6,1.5,0],end=[-3.8,1.5,0])
        r5= Line(start=[-4.6,1,0],end=[-3.8,1,0])
        r6= Line(start=[-4.6,0.5,0],end=[-3.8,0.5,0])
        r7= Line(start=[-4.6,0,0],end=[-3.8,0,0])
       
        self.play(Write(r1))
        self.play(Write(r2))
        self.play(Write(r3))
        self.play(Write(r4))
        self.play(Write(r5))
        self.play(Write(r6))
        self.play(Write(r7))

        ans1 = Rectangle(height=1,width=1.5)
        ans1.move_to([-4.2,-1.5,0])
        self.play(Write(ans1))

        rec3= Rectangle(height=4,width=0.4)
        rec3.move_to([-1,1.5,0])
        self.play(Write(rec3))
        rec4= Rectangle(height=4,width=0.4)
        rec4.move_to([-1.4,1.5,0])
        self.play(Write(rec4))
        rec5= Rectangle(height=4,width=0.4)
        rec5.move_to([-0.6,1.5,0])
        self.play(Write(rec5))
        r11 = Line(start=[-1.6,3,0],end=[-0.4,3,0])
        r21= Line(start=[-1.6,2.5,0],end=[-0.4,2.5,0])
        r31= Line(start=[-1.6,2,0],end=[-0.4,2,0])
        r41= Line(start=[-1.6,1.5,0],end=[-0.4,1.5,0])
        r51= Line(start=[-1.6,1,0],end=[-0.4,1,0])
        r61= Line(start=[-1.6,0.5,0],end=[-0.4,0.5,0])
        r71= Line(start=[-1.6,0,0],end=[-0.4,0,0])
       
        self.play(Write(r11))
        self.play(Write(r21))
        self.play(Write(r31))
        self.play(Write(r41))
        self.play(Write(r51))
        self.play(Write(r61))
        self.play(Write(r71))

        ans2 = Rectangle(height=1,width=1.5)
        ans2.move_to([-1,-1.5,0])
        self.play(Write(ans2))

        t3 = Text("Count the grid and Find\n\n"
                  "out the number of tiny boxes.",font_size=32)
        t3.move_to([3.5,0,0])
        self.play(Write(t3))

        a1 = Text("16")
        a1.move_to([-4.2,-1.5,0])
        a2 = Text("24")
        a2.move_to([-1,-1.5,0])

        self.play(Write(a1))
        self.play(Write(a2))


    def extro(self):
        
        h1 = Tex("Count in Tens")
        h1.move_to([-5,3.5,0])
        self.play(Write(h1))

        t1 = Table(
            [["10","1 ten","10\n\nten"],
            ["10 + 10", "2 tens","20\n\ntwenty"],["20 + 10", "3 tens","30\n\nthirty"],
            ["30 + 10", "4 tens","40\n\nforty"],["40 + 10","5 tens","50\n\nfifty"]],
           
            top_left_entry=Star().scale(0.3),
            include_outer_lines=True,
            arrange_in_grid_config={"cell_alignment": LEFT})
        
        t2 = Table(
            [["50 + 10", "6 tens","60\n\nsixty"],["60 + 10", "7 tens","70\n\nseventy"],
            ["70 + 10","8 tens","80\n\neighty"],["80 + 10","9 tens","90\n\nninety"],
            ["90 + 10","10 tens","100\n\nhundred"]],
           
            top_left_entry=Star().scale(0.3),
            include_outer_lines=True,
            arrange_in_grid_config={"cell_alignment": LEFT})
        
        t1.move_to([-3.5,-0.5,0])
        t2.move_to([3.5,-0.5,0])
        t1.scale(0.5)
        self.play((Create(t1)),run_time=5)
        self.wait(1)     
        t2.scale(0.5)
        self.play((Create(t2)),run_time=5)
        self.wait(2)
    

    def intro2(self):

        h2 = Text("Match the following with the correct answers:", font_size=30)
        h2.move_to([-2.7,3.5,0])
        self.play(Write(h2))

        t11 = Table(
            [["\n10 + 10\n"],["\n30 + 10\n"],["\n40 + 10\n"],
             ["\n70 + 10\n"],["\n80 + 10\n"]],
           
            top_left_entry=Star().scale(0.3),
            include_outer_lines=True,
            arrange_in_grid_config={"cell_alignment": LEFT})
        
        t21 = Table(
            [["40"],["50"],
            ["80"],["20"],
            ["90"]],
           
            top_left_entry=Star().scale(0.3),
            include_outer_lines=True,
            arrange_in_grid_config={"cell_alignment": LEFT})
        
        t11.move_to([-3.5,-0.5,0])
        t21.move_to([3.5,-0.5,0])
        t11.scale(1)
        self.play((Create(t11)),run_time=5)
        self.wait(1)     
        t21.scale(1)
        self.play((Create(t21)),run_time=5)
        self.wait(2)

        # self.play(Write(NumberPlane()))

        a1 = DashedLine(end=[-1.7,2,0],start=[2.4,-1.5,0]).add_tip(at_start=True)
        a2 = DashedLine(end=[-1.7,0.7,0],start=[2.4,2,0]).add_tip(at_start=True)
        a3 = DashedLine(end=[-1.7,-0.5,0],start=[2.4,0.7,0]).add_tip(at_start=True)
        a4 = DashedLine(end=[-1.7,-1.5,0],start=[2.4,-0.5,0]).add_tip(at_start=True)
        a5 = DashedLine(end=[-1.7,-3,0],start=[2.4,-3,0]).add_tip(at_start=True)

        self.play((Write(a1)), run_time=0.5)
        self.play((Write(a2)), run_time=0.5)
        self.play((Write(a3)), run_time=0.5)
        self.play((Write(a4)), run_time=0.5)
        self.play((Write(a5)), run_time=0.5)

if __name__ == "__main__":
    scene = Grade1Chapter12Tens10to100Anim()
    scene.render()