import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class report(AbstractAnim):

    def construct(self):
        
       
        t1 = Text("If we observe a 3-D object from different positions,\n\n"
                  "it seems to be different. But the object is same.",font_size=28).move_to([-2,2.5,0])
        self.play(Write(t1))

        # p11=cvo.CVO().CreateCVO("Different Positions","").setPosition([3.5,0.5,0])
        # p12=cvo.CVO().CreateCVO("Top View","").setPosition([5,-1.5,0])
        # p13=cvo.CVO().CreateCVO("Front View","").setPosition([2.5,-2.3,0])
        # p14=cvo.CVO().CreateCVO("Side View","").setPosition([0,-2,0])

        # p11.cvolist.append(p12)
        # p11.cvolist.append(p13)
        # p11.cvolist.append(p14)  
        
        # self.construct1(p11,p11)
        
        self.play(Write(NumberPlane()))



        ha = ((-5.25,-2.75,0),(-5.25,-2,0),(-4.5,-2,0),(-4.5,-2.75,0),(-5.25,-2.75,0))
        ha1 = Polygon(*ha,color=WHITE,fill_color="#6DC9CD",fill_opacity=1,stroke_width=2)
        self.play(Create(ha1))

        hb = ((-4.5,-2.75,0),(-4.5,-2,0),(-3.75,-2,0),(-3.75,-2.75,0),(-4.5,-2.75,0))
        hb2 = Polygon(*hb,color=WHITE,fill_color="#6DC9CD",fill_opacity=1,stroke_width=2)
        self.play(Create(hb2))

        hc = ((-4.75,-1.75,0),(-5.25,-2,0),(-4.5,-2,0),(-4,-1.75,0),(-4.75,-1.75,0))
        hc1 = Polygon(*hc,color=WHITE,fill_color="#6DC9CD",fill_opacity=1,stroke_width=2)
        self.play(Create(hc1))

        hd = ((-4,-1.75,0),(-4.5,-2,0),(-3.75,-2,0),(-3.25,-1.75,0),(-4,-1.75,0))
        hd1 = Polygon(*hd,color=WHITE,fill_color="#6DC9CD",fill_opacity=1,stroke_width=2)
        self.play(Create(hd1))
        
        he = ((-3.75,-2,0),(-3.75,-2.75,0),(-3.25,-2.5,0),(-3.25,-1.75,0),(-3.75,-2,0))
        he1 = Polygon(*he,color=WHITE,fill_color=RED,fill_opacity=1,stroke_width=2)
        self.play(Create(he1))

        #

        a = ((-6.5,-3,0),(-6.5,-2.25,0),(-5.75,-2.25,0),(-5.75,-3,0),(-6.5,-3,0))
        a1 = Polygon(*a,color=WHITE,fill_color="#6DC9CD",fill_opacity=1,stroke_width=2)
        self.play(Create(a1))

        b = ((-5.75,-3,0),(-5.75,-2.25,0),(-5,-2.25,0),(-5,-3,0),(-5.75,-3,0))
        b2 = Polygon(*b,color=WHITE,fill_color="#6DC9CD",fill_opacity=1,stroke_width=2)
        self.play(Create(b2))

        c = ((-6.49,-2.25,0),(-6,-2,0),(-5.25,-2,0),(-5.75,-2.25,0),(-6.5,-2.25,0))
        c1 = Polygon(*c,color=WHITE,fill_color="#6DC9CD",fill_opacity=1,stroke_width=2)
        self.play(Create(c1))

        d = ((-5.25,-2,0),(-5.75,-2.25,0),(-5,-2.25,0),(-4.5,-2,0),(-5.25,-2,0))
        d1 = Polygon(*d,color=WHITE,fill_color="#6DC9CD",fill_opacity=1,stroke_width=2)
        self.play(Create(d1))
        
        e = ((-5,-2.25,0),(-5,-3,0),(-4.5,-2.75,0),(-4.5,-2,0),(-5,-2.25,0))
        e1 = Polygon(*e,color=WHITE,fill_color=RED,fill_opacity=1,stroke_width=2)
        self.play(Create(e1))

        s1 = Text("Side view",font_size=27).move_to([-4,-3.25,0])
        self.play(Write(s1))

        #front

        c = ((-5.75,0,0),(-5.25,0.25,0),(-4.5,0.25,0),(-5,0,0),(-5.75,0,0))
        c1 = Polygon(*c,color=WHITE,fill_color="#6DC9CD",fill_opacity=1,stroke_width=2)
        self.play(Create(c1))

        b = ((-5,-0.75,0),(-5,0,0),(-4.25,0,0),(-4.25,-0.75,0),(-5,-0.75,0))
        b2 = Polygon(*b,color=WHITE,fill_color="#6DC9CD",fill_opacity=1,stroke_width=2)
        self.play(Create(b2))

        d = ((-4.5,0.25,0),(-5,0,0),(-4.25,0,0),(-3.75,0.25,0),(-4.5,0.25,0))
        d1 = Polygon(*d,color=WHITE,fill_color=RED,fill_opacity=1,stroke_width=2)
        self.play(Create(d1))
        
        e = ((-4.25,0,0),(-4.25,-0.75,0),(-3.75,-0.5,0),(-3.75,0.25,0),(-4.25,0,0))
        e1 = Polygon(*e,color=WHITE,fill_color="#6DC9CD",fill_opacity=1,stroke_width=2)
        self.play(Create(e1))
        
        #

        b = ((-5,-1.5,0),(-5,-0.75,0),(-4.25,-0.75,0),(-4.25,-1.5,0),(-5,-1.5,0))
        b2 = Polygon(*b,color=WHITE,fill_color="#6DC9CD",fill_opacity=1,stroke_width=2)
        self.play(Create(b2))

        e = ((-4.25,-0.75,0),(-4.25,-1.5,0),(-3.75,-1.25,0),(-3.75,-0.5,0),(-4.25,-0.75,0))
        e1 = Polygon(*e,color=WHITE,fill_color="#6DC9CD",fill_opacity=1,stroke_width=2)
        self.play(Create(e1))

        e = ((-3.75,0.25,0),(-3.75,-0.5,0),(-3.25,-0.25,0),(-3.25,0.5,0),(-3.75,0.25,0))
        e1 = Polygon(*e,color=WHITE,fill_color="#6DC9CD",fill_opacity=1,stroke_width=2)
        self.play(Create(e1))

        #

        b = ((-5,-0.75,0),(-5,0,0),(-4.25,0,0),(-4.25,-0.75,0),(-5,-0.75,0))
        b2 = Polygon(*b,color=WHITE,fill_color="#6DC9CD",fill_opacity=1,stroke_width=2)
        self.play(Create(b2))

        d = ((-4.5,0.25,0),(-5,0,0),(-4.25,0,0),(-3.75,0.25,0),(-4.5,0.25,0))
        d1 = Polygon(*d,color=WHITE,fill_color=RED,fill_opacity=1,stroke_width=2)
        self.play(Create(d1))
        
        e = ((-4.25,0,0),(-4.25,-0.75,0),(-3.75,-0.5,0),(-3.75,0.25,0),(-4.25,0,0))
        e1 = Polygon(*e,color=WHITE,fill_color="#6DC9CD",fill_opacity=1,stroke_width=2)
        self.play(Create(e1))
        
        




        

        



if __name__ == "__main__":
    scene = report()
    scene.render()