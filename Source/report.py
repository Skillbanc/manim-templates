import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class report(AbstractAnim):

    def construct(self):
        
        

        # p11=cvo.CVO().CreateCVO("Different Positions","").setPosition([3.5,0.5,0])
        # p12=cvo.CVO().CreateCVO("Top View","").setPosition([5,-1.5,0])
        # p13=cvo.CVO().CreateCVO("Front View","").setPosition([2.5,-2.3,0])
        # p14=cvo.CVO().CreateCVO("Side View","").setPosition([0,-2,0])

        # p11.cvolist.append(p12)
        # p11.cvolist.append(p13)
        # p11.cvolist.append(p14)  
        
        # self.construct1(p11,p11)
        
        # self.play(Write(NumberPlane()))



        # ha = ((-5.25,-2.75,0),(-5.25,-2,0),(-4.5,-2,0),(-4.5,-2.75,0),(-5.25,-2.75,0))
        # ha1 = Polygon(*ha,color=WHITE,fill_color="#6DC9CD",fill_opacity=1,stroke_width=2)
        # self.play(Create(ha1))

        # hb = ((-4.5,-2.75,0),(-4.5,-2,0),(-3.75,-2,0),(-3.75,-2.75,0),(-4.5,-2.75,0))
        # hb2 = Polygon(*hb,color=WHITE,fill_color="#6DC9CD",fill_opacity=1,stroke_width=2)
        # self.play(Create(hb2))

        # hc = ((-4.75,-1.75,0),(-5.25,-2,0),(-4.5,-2,0),(-4,-1.75,0),(-4.75,-1.75,0))
        # hc1 = Polygon(*hc,color=WHITE,fill_color="#6DC9CD",fill_opacity=1,stroke_width=2)
        # self.play(Create(hc1))

        # hd = ((-4,-1.75,0),(-4.5,-2,0),(-3.75,-2,0),(-3.25,-1.75,0),(-4,-1.75,0))
        # hd1 = Polygon(*hd,color=WHITE,fill_color="#6DC9CD",fill_opacity=1,stroke_width=2)
        # self.play(Create(hd1))
        
        # he = ((-3.75,-2,0),(-3.75,-2.75,0),(-3.25,-2.5,0),(-3.25,-1.75,0),(-3.75,-2,0))
        # he1 = Polygon(*he,color=WHITE,fill_color=RED,fill_opacity=1,stroke_width=2)
        # self.play(Create(he1))

        # #

        # a = ((-6.5,-3,0),(-6.5,-2.25,0),(-5.75,-2.25,0),(-5.75,-3,0),(-6.5,-3,0))
        # a1 = Polygon(*a,color=WHITE,fill_color="#6DC9CD",fill_opacity=1,stroke_width=2)
        # self.play(Create(a1))

        # b = ((-5.75,-3,0),(-5.75,-2.25,0),(-5,-2.25,0),(-5,-3,0),(-5.75,-3,0))
        # b2 = Polygon(*b,color=WHITE,fill_color="#6DC9CD",fill_opacity=1,stroke_width=2)
        # self.play(Create(b2))

        # c = ((-6.49,-2.25,0),(-6,-2,0),(-5.25,-2,0),(-5.75,-2.25,0),(-6.5,-2.25,0))
        # c1 = Polygon(*c,color=WHITE,fill_color="#6DC9CD",fill_opacity=1,stroke_width=2)
        # self.play(Create(c1))

        # d = ((-5.25,-2,0),(-5.75,-2.25,0),(-5,-2.25,0),(-4.5,-2,0),(-5.25,-2,0))
        # d1 = Polygon(*d,color=WHITE,fill_color="#6DC9CD",fill_opacity=1,stroke_width=2)
        # self.play(Create(d1))
        
        # e = ((-5,-2.25,0),(-5,-3,0),(-4.5,-2.75,0),(-4.5,-2,0),(-5,-2.25,0))
        # e1 = Polygon(*e,color=WHITE,fill_color=RED,fill_opacity=1,stroke_width=2)
        # self.play(Create(e1))

        # s1 = Text("Side view",font_size=27).move_to([-4,-3.25,0])
        # self.play(Write(s1))

        # #front

        # c = ((-5.75,0,0),(-5.25,0.25,0),(-4.5,0.25,0),(-5,0,0),(-5.75,0,0))
        # c1 = Polygon(*c,color=WHITE,fill_color="#6DC9CD",fill_opacity=1,stroke_width=2)
        # self.play(Create(c1))

        # b = ((-5,-0.75,0),(-5,0,0),(-4.25,0,0),(-4.25,-0.75,0),(-5,-0.75,0))
        # b2 = Polygon(*b,color=WHITE,fill_color="#6DC9CD",fill_opacity=1,stroke_width=2)
        # self.play(Create(b2))

        # d = ((-4.5,0.25,0),(-5,0,0),(-4.25,0,0),(-3.75,0.25,0),(-4.5,0.25,0))
        # d1 = Polygon(*d,color=WHITE,fill_color=RED,fill_opacity=1,stroke_width=2)
        # self.play(Create(d1))
        
        # e = ((-4.25,0,0),(-4.25,-0.75,0),(-3.75,-0.5,0),(-3.75,0.25,0),(-4.25,0,0))
        # e1 = Polygon(*e,color=WHITE,fill_color="#6DC9CD",fill_opacity=1,stroke_width=2)
        # self.play(Create(e1))
        
        # #

        # b = ((-5,-1.5,0),(-5,-0.75,0),(-4.25,-0.75,0),(-4.25,-1.5,0),(-5,-1.5,0))
        # b2 = Polygon(*b,color=WHITE,fill_color="#6DC9CD",fill_opacity=1,stroke_width=2)
        # self.play(Create(b2))

        # e = ((-4.25,-0.75,0),(-4.25,-1.5,0),(-3.75,-1.25,0),(-3.75,-0.5,0),(-4.25,-0.75,0))
        # e1 = Polygon(*e,color=WHITE,fill_color="#6DC9CD",fill_opacity=1,stroke_width=2)
        # self.play(Create(e1))

        # e = ((-3.75,0.25,0),(-3.75,-0.5,0),(-3.25,-0.25,0),(-3.25,0.5,0),(-3.75,0.25,0))
        # e1 = Polygon(*e,color=WHITE,fill_color="#6DC9CD",fill_opacity=1,stroke_width=2)
        # self.play(Create(e1))

        # #

        # b = ((-5,-0.75,0),(-5,0,0),(-4.25,0,0),(-4.25,-0.75,0),(-5,-0.75,0))
        # b2 = Polygon(*b,color=WHITE,fill_color="#6DC9CD",fill_opacity=1,stroke_width=2)
        # self.play(Create(b2))

        # d = ((-4.5,0.25,0),(-5,0,0),(-4.25,0,0),(-3.75,0.25,0),(-4.5,0.25,0))
        # d1 = Polygon(*d,color=WHITE,fill_color=RED,fill_opacity=1,stroke_width=2)
        # self.play(Create(d1))
        
        # e = ((-4.25,0,0),(-4.25,-0.75,0),(-3.75,-0.5,0),(-3.75,0.25,0),(-4.25,0,0))
        # e1 = Polygon(*e,color=WHITE,fill_color="#6DC9CD",fill_opacity=1,stroke_width=2)
        # self.play(Create(e1))
        
        #To over come this\n\n" "problem we use isometric dots paper, in which we can represent\n\n" "length, breadth and height with exact measurment of 3-D objects.",font_size=24).move_to([-2,0,0])
      

        # self.angleChoice = [(TAU/4),(-TAU/4)]

        # p11=cvo.CVO().CreateCVO("3-D Objects","").setPosition([0,2.5,0])
        # p12=cvo.CVO().CreateCVO("Polyhedra","Objects that don't have curved surfaces").setPosition([-3,-1.5,0])
        # p13=cvo.CVO().CreateCVO("Non-Polyhedra","Objects that have curved surfaces").setPosition([3.5,-1.5,0])
        

        # p11.cvolist.append(p12)
        # p11.cvolist.append(p13)  
        
        # self.construct1(p11,p11)

        self.fadeOutCurrentScene()

        # self.play(Write(NumberPlane()))


        a = ((5,-1.75,0),(3.2,-1.75,0),(2.9,-2.25,0),(5,-1.75,0))
        base = Polygon(*a,color="#6DC9CD",fill_opacity=0.5,stroke_width=5)
       

        b = ((5,1.25,0),(3.2,1.25,0),(2.9,0.75,0),(5,1.25,0))
        top = Polygon(*b,color="#6DC9CD",fill_opacity=0.5,stroke_width=5)


        c = ((5.1,-1.75,0),(5.1,1.25,0),(2.9,0.75,0),(2.9,-2.25,0),(5,-1.75,0))
        face1 = Polygon(*c,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)


        d = ((5.1,-1.75,0),(5.1,1.25,0),(3.2,1.25,0),(3.2,-1.75,0),(5.1,-1.75,0))
        face2 = Polygon(*d,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)


        e = ((3.2,1.25,0),(3.2,-1.75,0),(2.9,-2.25,0),(2.9,0.75,0),(3.2,1.25,0))
        face3 = Polygon(*e,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)
        self.play(Write(base))
        self.play(Write(top))
        self.play(Write(face2))
        self.play(Write(face3))
        self.play(Write(face1))

       
        t = Text("The solid object with two parallel and\n\n"
                 "congruent polygonal faces and lateral faces\n\n"
                 "as rectangles/parallelograms is called a prism.",font_size= 22).move_to([3.2,2.5,0])
        self.play(Write(t))

        a = ((-6,-1.25,0),(-4.6,-1,0),(-3.8,-1.7,0),(-6,-1.25,0))
        base = Polygon(*a,color="#6DC9CD",fill_opacity=0.5,stroke_width=5)


        c = ((-4.8,1,0),(-6.1,-1.25,0),(-3.8,-1.7,0),(-4.8,1,0))
        face1 = Polygon(*c,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)


        d = ((-4.8,1,0),(-4.6,-1,0),(-6.1,-1.25,0),(-4.8,1,0))
        face2 = Polygon(*d,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)


        e = ((-4.8,1,0),(-4.6,-1,0),(-3.8,-1.7,0),(-4.8,1,0))
        face3 = Polygon(*e,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)
        self.play(Write(base))
        self.play(Write(face1))
        self.play(Write(face2))
        self.play(Write(face3))
        t1 = Text("A solid object whose base is a polygon and\n\n"
                 "its lateral faces are triangular faces is\n\n"
                  "called pyramid",font_size= 22).move_to([-4,2.5,0])
        self.play(Write(t1))
 



if __name__ == "__main__":
    scene = report()
    scene.render()