import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class Chap9Anim(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.constructDataByCVO()
       
        
    # render using CVO data object
    def constructDataByCVO(self):
        p10=cvo.CVO().CreateCVO("Area of Plane Figures","")
        p11=cvo.CVO().CreateCVO("Types of plane figures", "Area Formulae")
        p12=cvo.CVO().CreateCVO("Rectangle","l*b")
        p13=cvo.CVO().CreateCVO("Triangle", "1/2(b*h)")
        p14=cvo.CVO().CreateCVO("Square","a*a")
        p15=cvo.CVO().CreateCVO("parallelogram", "b*h")
        p16=cvo.CVO().CreateCVO("Rhombus", "1/2(d1*d2)")
        p17=cvo.CVO().CreateCVO("Trapezium","h*((a+b)/2)")
        p18=cvo.CVO().CreateCVO("Circle", "1/2(3.14)r*r")
        
        
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
        p11.cvolist.append(p14)
        p11.cvolist.append(p15)
        p11.cvolist.append(p16)
        p11.cvolist.append(p17)
        p11.cvolist.append(p18)
       
        self.setNumberOfCirclePositions(20)

        self.construct1(p10,p10)


        
      
if __name__ == "__main__":
    scene = Chap9Anim()
    scene.render()
