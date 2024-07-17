import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class Grade2Chapter19RecordAnim(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.intro()
        self.fadeOutCurrentScene()
        self.stars()
        self.fadeOutCurrentScene()
        self.graph()
        self.fadeOutCurrentScene()
        self.new()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()


    def SetDeveloperList(self):
        self.DeveloperList = "Lasya Nannapaneni"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName = "Grade2Chapter19RecordAnim.py"        

    def intro(self):

        title = Text("LET US RECORD",font_size=45,color=BLUE).move_to([-3.5,3.3,0])
        u = Underline(title)
        subtil = Text("To observe and record information about shapes,\n\nsizes, quantities, or other measurable attributes.\n\nand organize recorded data into simple charts, graphs,\n\nor tables to visually represent information. ",font_size=28).move_to([-2,1,0])
        self.play(Write(title))
        self.play(Write(u))
        self.play(Write(subtil,run_time=10))
        self.wait(2)
         
        self.fadeOutCurrentScene()

        p11=cvo.CVO().CreateCVO("Methods of Recording","").setPosition([0,2.5,0])
        p12=cvo.CVO().CreateCVO("Counting","").setPosition([-5,-1,0])
        p13=cvo.CVO().CreateCVO("Sequencing","").setPosition([5,-1,0])
        p14=cvo.CVO().CreateCVO("Graphical Representation","").setPosition([0,-2.7,0])

       
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
        p11.cvolist.append(p14)  
        
        self.construct1(p11,p11)


    def stars(self):

        tex = Text("Let us look at colour of stars and Count them:",font_size=30)
        tex.move_to([-2.5,3.5,0])
        self.play(Write(tex))

        box1 = Rectangle(height=3,width=8)
        box1.move_to([0,1.5,0])
        self.play(Write(box1))

        s1 = Star(fill_opacity=0.5,color=PINK).scale(0.3)
        s1.move_to([-3.5,2.5,0])
        self.play(Write(s1))

        s2 = Star(fill_opacity=0.5,color=GREEN).scale(0.3)
        s2.move_to([-2.5,2.5,0])
        self.play(Write(s2))

        s3 = Star(fill_opacity=0.5,color=ORANGE).scale(0.3)
        s3.move_to([-1.5,2.5,0])
        self.play(Write(s3))

        s4 = Star(fill_opacity=0.5,color=GREEN).scale(0.3)
        s4.move_to([-0.5,2.5,0])
        self.play(Write(s4))

        s5 = Star(fill_opacity=0.5,color=PINK).scale(0.3)
        s5.move_to([0.5,2.5,0])
        self.play(Write(s5))

        s7 = Star(fill_opacity=0.5,color=ORANGE).scale(0.3)
        s7.move_to([2.5,2.5,0])
        self.play(Write(s7))

        s8 = Star(fill_opacity=0.5,color=GREEN).scale(0.3)
        s8.move_to([3.5,2.5,0])
        self.play(Write(s8))


        s11 = Star(fill_opacity=0.5,color=PINK).scale(0.3)
        s11.move_to([3.5,1.5,0])
        self.play(Write(s11))

        s21 = Star(fill_opacity=0.5,color=GREEN).scale(0.3)
        s21.move_to([2.5,1.5,0])
        self.play(Write(s21))

        s31 = Star(fill_opacity=0.5,color=ORANGE).scale(0.3)
        s31.move_to([1.5,1.5,0])
        self.play(Write(s31))

        s41 = Star(fill_opacity=0.5,color=GREEN).scale(0.3)
        s41.move_to([0.5,1.5,0])
        self.play(Write(s41))

        s51 = Star(fill_opacity=0.5,color=PINK).scale(0.3)
        s51.move_to([-0.5,1.5,0])
        self.play(Write(s51))

        s71 = Star(fill_opacity=0.5,color=ORANGE).scale(0.3)
        s71.move_to([-2.5,1.5,0])
        self.play(Write(s71))

        s81 = Star(fill_opacity=0.5,color=GREEN).scale(0.3)
        s81.move_to([-3.5,1.5,0])
        self.play(Write(s81))

        s12 = Star(fill_opacity=0.5,color=PINK).scale(0.3)
        s12.move_to([-3.5,0.5,0])
        self.play(Write(s12))

        s22 = Star(fill_opacity=0.5,color=GREEN).scale(0.3)
        s22.move_to([-2.5,0.5,0])
        self.play(Write(s22))

        s32 = Star(fill_opacity=0.5,color=ORANGE).scale(0.3)
        s32.move_to([-1.5,0.5,0])
        self.play(Write(s32))

        s42 = Star(fill_opacity=0.5,color=GREEN).scale(0.3)
        s42.move_to([-0.5,0.5,0])
        self.play(Write(s42))

        s52 = Star(fill_opacity=0.5,color=PINK).scale(0.3)
        s52.move_to([0.5,0.5,0])
        self.play(Write(s52))

        s62 = Star(fill_opacity=0.5,color=GREEN).scale(0.3)
        s62.move_to([1.5,0.5,0])
        self.play(Write(s62))

        s72 = Star(fill_opacity=0.5,color=ORANGE).scale(0.3)
        s72.move_to([2.5,0.5,0])
        self.play(Write(s72))

        s82 = Star(fill_opacity=0.5,color=GREEN).scale(0.3)
        s82.move_to([3.5,0.5,0])
        self.play(Write(s82))


        table_data = [
            ["Pink", "6"],
            ["Green", "10"],
            ["Orange", "6"]
        ]
        
        col_labels = [Text("Colour of the star"), Text("Number of stars")]
        table = Table(
            table_data,
            col_labels=col_labels,
            include_outer_lines=True,
            arrange_in_grid_config={"cell_alignment": LEFT}
        )

        table.move_to([0, -2, 0])
        table.scale(0.5)
        

        for i, row in enumerate(table.get_rows()):
            self.play(Create(row))
            self.wait(1) 

        self.wait(2)

    def graph(self):

        # self.play(Write(NumberPlane()))
        
        yl = Line(start=[-6,-2.5,0],end=[-6,2.8,0])
        xl = Line(start=[-6,-2.5,0],end=[0.5,-2.5,0])
       
        t1 = Text("5 ").move_to([-6.3,2.5,0])
        t2 = Text("4 ").move_to([-6.3,1.5,0])
        t3 = Text("3 ").move_to([-6.3,0.5,0])
        t4 = Text("2 ").move_to([-6.3,-0.5,0])
        t5 = Text("1 ").move_to([-6.3,-1.5,0])
        t6 = Text("0 ").move_to([-6.3,-2.5,0])

        self.play(Write(xl))
        self.play(Write(yl))
        self.play(Write(t6))
        self.play(Write(t5))
        self.play(Write(t4))
        self.play(Write(t3))
        self.play(Write(t2))
        self.play(Write(t1))

        s1 = Star(fill_opacity=0.5,color=PINK).scale(0.3).move_to([-5,-3,0])
        self.play(Write(s1))

        ss = Rectangle(height=5,width=1,fill_opacity=0.5,color=PINK).next_to(s1,UP)
        self.play(Write(ss))

        
        c1 = Circle(fill_opacity=0.5,color=GREEN).scale(0.3).move_to([-3.5,-3,0])
        self.play(Write(c1))
        cs = Rectangle(height=3,width=1,fill_opacity=0.5,color=GREEN).next_to(c1,UP)
        self.play(Write(cs))

        
        b1 = Square(fill_opacity=0.5,color=BLUE).scale(0.3).move_to([-2,-3,0])
        self.play(Write(b1))
        bs = Rectangle(height=4,width=1,fill_opacity=0.5,color=BLUE).next_to(b1,UP)
        self.play(Write(bs))


        d1 = Rectangle(fill_opacity=0.5,color=ORANGE).scale(0.3).move_to([-0.5,-3,0])
        self.play(Write(d1))
        ds = Rectangle(height=2,width=1,fill_opacity=0.5,color=ORANGE).next_to(d1,UP)
        self.play(Write(ds))

        tg = Text("Look at the graph and count the shapes respectively",font_size=30).move_to([-2,3.2,0])
        self.play(Write(tg))
        self.wait(1)


        tab = Table(
            [["Star","5"],
            ["Circle","3"],["Square","4"],["Rectangle","2"]],
            col_labels=[Text("Shape"), Text("It's Number")],
            include_outer_lines=True,
            arrange_in_grid_config={"cell_alignment": LEFT})
        tab.move_to([3.5,0.5,0])
        tab.scale(0.65)
        self.play(Create(tab),run_time=6)


    def new(self):
        
        tex = Text("Sequencing",font_size=30)
        tex.move_to([-2.5,3.5,0])
        self.play(Write(tex))

        s1 = Square(side_length=0.5,fill_color=BLUE,color=WHITE,fill_opacity=0.5).move_to([-5,2,0])
        s2 = Square(side_length=2,fill_color=BLUE,color=WHITE,fill_opacity=0.5).move_to([-3,2,0])
        s3 = Square(side_length=1,fill_color=BLUE,color=WHITE,fill_opacity=0.5).move_to([-0.5,2,0])
        s4 = Square(side_length=1.5,fill_color=BLUE,color=WHITE,fill_opacity=0.5).move_to([1.5,2,0])
        s5 = Square(side_length=2.5,fill_color=BLUE,color=WHITE,fill_opacity=0.5).move_to([4,2,0])

        self.play(Write(s1))       
        self.play(Write(s2))
        self.play(Write(s3))
        self.play(Write(s4))
        self.play(Write(s5))

        subtil = Text("Now, let's arrange them in ascending order or increasing order.",font_size=28).move_to([-1,0,0])
    
        self.play(Write(subtil))

        self.play(s1.animate.move_to([-5,-2,0]))
        self.play(s3.animate.move_to([-3,-2,0]))
        self.play(s4.animate.move_to([-1,-2,0]))
        self.play(s2.animate.move_to([1.5,-2,0]))
        self.play(s5.animate.move_to([4.5,-2,0]))


        self.fadeOutCurrentScene()

        
        s1 = Triangle(fill_color=GREEN,color=WHITE,fill_opacity=0.5).scale(0.5).move_to([5,2,0])
        s11 = Triangle(fill_color=GREEN,color=WHITE,fill_opacity=0.5).scale(0.5).move_to([-2,2,0])
        s12= Triangle(fill_color=GREEN,color=WHITE,fill_opacity=0.5).scale(0.5).move_to([1.5,2,0])
        s3 = Circle(radius=0.5,fill_color=BLUE,color=WHITE,fill_opacity=0.5).move_to([-5,2,0])
        s31 = Circle(radius=0.5,fill_color=BLUE,color=WHITE,fill_opacity=0.5).move_to([2.5,2,0])
        s32 = Circle(radius=0.5,fill_color=BLUE,color=WHITE,fill_opacity=0.5).move_to([0.5,2,0])
        s5 = Square(fill_color=RED,color=WHITE,fill_opacity=0.5).scale(0.5).move_to([-3.2,2,0])
        s51 = Square(fill_color=RED,color=WHITE,fill_opacity=0.5).scale(0.5).move_to([3.8,2,0])
        s52 = Square(fill_color=RED,color=WHITE,fill_opacity=0.5).scale(0.5).move_to([-0.8,2,0])


        self.play(Write(s1))       
        self.play(Write(s32))
        self.play(Write(s51))
        self.play(Write(s12))
        self.play(Write(s31))
        self.play(Write(s11)) 
        self.play(Write(s5))
        self.play(Write(s3))
        self.play(Write(s52))

        subtil = Text("Now, let's arrange them.",font_size=28).move_to([-1,0,0])
        self.play(Write(subtil))
        
        t1 =  Text("Triangles",font_size=22).move_to([-4.5,-1,0])
        self.play(Write(t1))
        t2 =  Text("Circles",font_size=22).move_to([0,-1,0])
        self.play(Write(t2))
        t3 =  Text("Squares",font_size=22).move_to([4.5,-1,0])
        self.play(Write(t3))

        self.play(s1.animate.move_to([-5,-2,0]))
        self.play(s11.animate.move_to([-4,-2,0]))
        self.play(s12.animate.move_to([-4.5,-3,0]))
        self.play(s3.animate.move_to([-0.5,-2,0]))
        self.play(s31.animate.move_to([0.5,-2,0]))
        self.play(s32.animate.move_to([0,-3,0]))
        self.play(s5.animate.move_to([5,-2,0]))
        self.play(s51.animate.move_to([4,-2,0]))
        self.play(s52.animate.move_to([4.5,-3,0]))
        



if __name__ == "__main__":
    scene = Grade2Chapter19RecordAnim()
    scene.render()    