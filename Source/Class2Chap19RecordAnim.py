import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class Class2Chap19RecordAnim(AbstractAnim):

    def construct(self):
        # self.stars()
        # self.fadeOutCurrentScene()
        self.graph()
        self.pics()



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


        tab = Table(
            [["Pink","6"],
            ["Green","10"],["Orange","6"]],
            col_labels=[Text("Colour of the star"), Text("Number of stars")],
            include_outer_lines=True,
            arrange_in_grid_config={"cell_alignment": LEFT})
        tab.move_to([-0,-2,0])
        tab.scale(0.5)
        self.play(Create(tab))
        self.wait(2)

    def graph(self):

        self.play(Write(NumberPlane()))
        
        yl = Line(start=[-6,-2,0],end=[-6,3.5,0])
        xl = Line(start=[-6,-2,0],end=[0,-2,0])
        x1 = Line(start=[-6,-1,0],end=[0,-1,0])
        y1 = Line(start=[-6,0,0],end=[0,0,0])
        x2 = Line(start=[-6,1,0],end=[0,1,0])
        y2 = Line(start=[-6,2,0],end=[0,2,0])
        x3 = Line(start=[-6,3,0],end=[0,3,0])
       
        t1 = Text("5 ").move_to([-6.3,3,0])
        t2 = Text("4 ").move_to([-6.3,2,0])
        t3 = Text("3 ").move_to([-6.3,1,0])
        t4 = Text("2 ").move_to([-6.3,0,0])
        t5 = Text("1 ").move_to([-6.3,-1,0])
        t6 = Text("0 ").move_to([-6.3,-2,0])

        self.play(Write(xl))
        self.play(Write(yl))
        self.play(Write(t6))
        self.play(Write(x1))
        self.play(Write(t5))
        self.play(Write(y1))
        self.play(Write(t4))
        self.play(Write(x2))
        self.play(Write(t3))
        self.play(Write(y2))
        self.play(Write(t2))
        self.play(Write(x3))
        self.play(Write(t1))


    def pics(self):

        s1 = Star(fill_opacity=0.5,color=PINK).scale(0.3).move_to([-5,-1.5,0])
        self.play(Write(s1))

        s2 = Star(fill_opacity=0.5,color=PINK).scale(0.3).move_to([-5,-0.5,0])
        self.play(Write(s2))

        s3 = Star(fill_opacity=0.5,color=PINK).scale(0.3).move_to([-5,0.5,0])
        self.play(Write(s3))

        s4 = Star(fill_opacity=0.5,color=PINK).scale(0.3).move_to([-5,1.5,0])
        self.play(Write(s4))

        s5 = Star(fill_opacity=0.5,color=PINK).scale(0.3).move_to([-5,2.5,0])
        self.play(Write(s5))

        
        c1 = Circle(fill_opacity=0.5,color=GREEN).scale(0.3).move_to([-4,-1.5,0])
        self.play(Write(c1))

        c2 = Circle(fill_opacity=0.5,color=GREEN).scale(0.3).move_to([-4,-0.5,0])
        self.play(Write(c2))

        c3 = Circle(fill_opacity=0.5,color=GREEN).scale(0.3).move_to([-4,0.5,0])
        self.play(Write(c3))

        
        b1 = Square(fill_opacity=0.5,color=BLUE).scale(0.3).move_to([-3,-1.5,0])
        self.play(Write(b1))

        b2 = Square(fill_opacity=0.5,color=BLUE).scale(0.3).move_to([-3,-0.5,0])
        self.play(Write(b2))

        b3 = Square(fill_opacity=0.5,color=BLUE).scale(0.3).move_to([-3,0.5,0])
        self.play(Write(b3))

        b4 = Square(fill_opacity=0.5,color=BLUE).scale(0.3).move_to([-3,1.5,0])
        self.play(Write(b4))


        d1 = Prism(fill_opacity=0.5,fill_color=ORANGE).scale(0.3).move_to([-2,-1.5,0])
        self.play(Write(d1))

        d2 = Prism(fill_opacity=0.5,fill_color=ORANGE).scale(0.3).move_to([-2,-0.5,0])
        self.play(Write(d2))


        t1 = Star(fill_opacity=0.5,color=PINK).scale(0.3).move_to([-5,-1.5,0])
        self.play(Write(t1))

        t2 = Star(fill_opacity=0.5,color=PINK).scale(0.3).move_to([-5,-0.5,0])
        self.play(Write(t2))

        t3 = Star(fill_opacity=0.5,color=PINK).scale(0.3).move_to([-5,0.5,0])
        self.play(Write(t3))

        t4 = Star(fill_opacity=0.5,color=PINK).scale(0.3).move_to([-5,1.5,0])
        self.play(Write(t4))

        t5 = Star(fill_opacity=0.5,color=PINK).scale(0.3).move_to([-5,2.5,0])
        self.play(Write(t5))





        

      
      
        








if __name__ == "__main__":
    scene = Class2Chap19RecordAnim()
    scene.render()    