import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class Grade8Chapter13Visualising3Din2DAnim(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.intro()
        self.fadeOutCurrentScene()
        self.layers()


    def intro(self):
         
        p1=cvo.CVO().CreateCVO("Visualising 3-D in 2-D","").setPosition([0,2.2,0])
        p2=cvo.CVO().CreateCVO("2-D Shapes","").setPosition([-5,0.5,0])
        p3=cvo.CVO().CreateCVO("3-D Shapes","").setPosition([5,0.5,0])

        p4=cvo.CVO().CreateCVO("Two Measurements","length , breadth").setPosition([-2.6,-2.2,0])
        
        p5=cvo.CVO().CreateCVO("Three Measurements","length, breadth, height").setPosition([2.6,-2.2,0])

        p1.cvolist.append(p2)
        p1.cvolist.append(p3)
        p2.cvolist.append(p4)
        p3.cvolist.append(p5)

        p4.setcircleradius(1.2)
        p5.setcircleradius(1.2)
        self.construct1(p1,p1)

        self.fadeOutCurrentScene()

        
    def layers(self):
        t1 = Text("Triangle, Square, Rectangle are plane figures\n\n"
                  "of 2-dimensions. While, a cube and cuboid are\n\n"
                  "solid objects with 3-dimensions. By arranging\n\n"
                  "2-D objects one above another it occupies some\n\n" 
                  "space and becomes a 3-D. It has volume also.",font_size=28).move_to([-2,1.5,0])
        self.play(Write(t1))

        a = ((5.5,-1.75,0),(3.75,-1.75,0),(2,-2.25,0),(3.75,-2.25,0),(5.5,-1.75,0))
        base = Polygon(*a,color="#6DC9CD",fill_opacity=0.5,stroke_width=5).move_to([-4.5,-2,0])
        n1 = Text("(1)",font_size=22).move_to([-4.5,-3,0])
        self.play(Create(base),Write(n1))

        ar1 = Arrow(start=[-4,-3,0],end=[-1,-3,0])
        self.play(Write(ar1))

        a1 = ((5.5,-1.75,0),(3.75,-1.75,0),(2,-2.25,0),(3.75,-2.25,0),(5.5,-1.75,0))
        spacing = 0.08
        for i in range(10):  
            base1 = Polygon(*a1, color="#6DC9CD", fill_opacity=0.5, stroke_width=5).move_to([-0.5,-2,0])
            base1.shift(UP * i * spacing) 
            n2 = Text("(2)",font_size=22).move_to([-0.5,-3,0])
            self.play(Create(base1),Write(n2))
            

        ar2 = Arrow(start=[0,-3,0],end=[3.25,-3,0])
        self.play(Write(ar2))

        a2 = ((5.4,-1.75,0),(3.75,-1.75,0),(2.1,-2.25,0),(3.75,-2.25,0),(5.4,-1.75,0))
        base_face = Polygon(*a2, color=BLUE, fill_opacity=0.5, stroke_width=5)
        self.play(Create(base_face))

        c = ((5.5,-1,0),(5.5, -1.75, 0),(3.75, -2.25, 0),(3.75, -1.5, 0),(5.5,-1,0))
        face1 = Polygon(*c,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)
        self.play(Create(face1))


        d = ((5.5,-1,0),(3.75, -1, 0),(3.75, -1.75, 0),(5.5, -1.75, 0),(5.5,-1,0))
        face2 = Polygon(*d,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)
        self.play(Create(face2))


        e = ((3.75, -1, 0),(3.75, -1.75, 0),(2, -2.25, 0),(2, -1.5, 0),(3.75, -1, 0))
        face3 = Polygon(*e,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)
        self.play(Create(face3))

 
        f = ((2, -2.25, 0),(3.75, -2.25, 0),(3.75, -1.5, 0),(2, -1.5, 0),(2, -2.25, 0))
        face4 = Polygon(*f,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)
        self.play(Create(face4))

        b1 = ((5.4,-1,0), (3.75, -1.5, 0),(2.1, -1.5, 0),(3.75, -1, 0),(5.5,-1,0))
        top_face = Polygon(*b1, color=BLUE, fill_opacity=0.5, stroke_width=5)
        self.play(Create(top_face))

        n3 = Text("(3)",font_size=22).move_to([3.75,-3,0])
        self.play(Write(n3))




if __name__ == "__main__":
    scene = Grade8Chapter13Visualising3Din2DAnim()
    scene.render()        