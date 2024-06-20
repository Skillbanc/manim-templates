import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class planefiguresAnim(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Intro()
        self.fadeOutCurrentScene()
        self.Square()
        self.fadeOutCurrentScene()
        self.Rectangle()
        self.fadeOutCurrentScene()
        self.Rhombus()
        self.fadeOutCurrentScene()
        self.Triangle()
        self.fadeOutCurrentScene()
        self.Parallelogram()
        self.fadeOutCurrentScene()
        self.Trapezium()
        self.fadeOutCurrentScene()
        self.Circle()
        self.fadeOutCurrentScene()

    def Intro(self):
        
        self.isRandom = False
        self.positionChoice=[[-4.5,2,0],[0,2,0],[-5,-2,0],[-1,0,0],[-1,-2,0],[1,0,0],[1,-2,0],[5,0,0],[5,-2,0]]
        p1=cvo.CVO().CreateCVO("Plane Figures and their Areas","")
        p2=cvo.CVO().CreateCVO("Types of plane figures", "")
       
        p12=cvo.CVO().CreateCVO("Rectangle","")
        p13=cvo.CVO().CreateCVO("Triangle", "")
        p14=cvo.CVO().CreateCVO("Square","")
        p15=cvo.CVO().CreateCVO("parallelogram", "")
        p16=cvo.CVO().CreateCVO("Rhombus", "")
        p17=cvo.CVO().CreateCVO("Trapezium","")
        p18=cvo.CVO().CreateCVO("Circle", "")
        p1.cvolist.append(p2)
        p2.cvolist.append(p12)
        p2.cvolist.append(p13)
        p2.cvolist.append(p14)
        p2.cvolist.append(p15)
        p2.cvolist.append(p16)
        p2.cvolist.append(p17)
        p2.cvolist.append(p18)
        
        self.construct1(p1,p1)

    def Square(self):
        
        self.isRandom = False
        self.positionChoice=[[-4.5,2,0],[0,2,0],[-5,-2,0],[-1,0,0],[1,-2,0]]

        p3=cvo.CVO().CreateCVO("Square","")
        p4=cvo.CVO().CreateCVO("Side","a")
        p5=cvo.CVO().CreateCVO("Area Formula","a*a")
        p6=cvo.CVO().CreateCVO("Example", "a=4")
        p7=cvo.CVO().CreateCVO("Area of Square", "4*4=16")
        p3.cvolist.append(p4)
        p3.cvolist.append(p5)
        p5.cvolist.append(p6)
        p6.cvolist.append(p7)
        self.construct1(p3,p3)
    


    def Rectangle(self):
    
        self.isRandom = False
        self.positionChoice=[[-4.5,2,0],[0,2,0],[-5,-2,0],[-1,0,0],[1,-2,0],[5,0,0]]
   
        p1=cvo.CVO().CreateCVO("Rectangle","")
        p2=cvo.CVO().CreateCVO("Area Formula", "l*b")
        p3=cvo.CVO().CreateCVO("length","l")
        p4=cvo.CVO().CreateCVO("breadth","b")
        p5=cvo.CVO().CreateCVO("Example","l=6 b=8")
        p6=cvo.CVO().CreateCVO("Area of Rectangle", "6*8=48")
        
        p1.cvolist.append(p3)
        p1.cvolist.append(p4)
        p1.cvolist.append(p2)
        p2.cvolist.append(p5)
        p5.cvolist.append(p6)
        
        self.construct1(p1,p1)
    

    def Rhombus(self):
    
        self.isRandom = False
        self.positionChoice=[[-4.5,2,0],[0,2,0],[-5,-2,0],[-1,0,0],[1,-2,0],[5,0,0]]

        p1=cvo.CVO().CreateCVO("Rhombus", "")
        p2=cvo.CVO().CreateCVO("Area Formula", "1/2(d1*d2)")
        p3=cvo.CVO().CreateCVO("diagonal 1","d1")
        p4=cvo.CVO().CreateCVO("diagonal 2","d2")
        p5=cvo.CVO().CreateCVO("Example","d1=8 d2=6")
        p6=cvo.CVO().CreateCVO("Area of Rhombus", "24")

        p1.cvolist.append(p3)
        p1.cvolist.append(p4)
        p1.cvolist.append(p2)
        p2.cvolist.append(p5)
        p5.cvolist.append(p6)
        self.construct1(p1,p1)
    

    def Triangle(self):

        self.isRandom = False
        self.positionChoice=[[-4.5,2,0],[0,2,0],[-5,-2,0],[-1,0,0],[1,-2,0],[5,0,0]]

        p1=cvo.CVO().CreateCVO("Triangle", "")
        p2=cvo.CVO().CreateCVO("Area Formula", "1/2(b*h)")
        p3=cvo.CVO().CreateCVO("breadth","b")
        p4=cvo.CVO().CreateCVO("height","h")
        p5=cvo.CVO().CreateCVO("Example", "b=8 h=8")
        p6=cvo.CVO().CreateCVO("Area of Triangle", "32")
        p1.cvolist.append(p3)
        p1.cvolist.append(p4)
        p1.cvolist.append(p2)
        p2.cvolist.append(p5)
        p5.cvolist.append(p6)
        self.construct1(p1,p1)
    
    
    def Parallelogram(self):
   
        self.isRandom = False
        self.positionChoice=[[-4.5,2,0],[0,2,0],[-5,-2,0],[-1,0,0],[1,-2,0],[5,0,0]]

        p1=cvo.CVO().CreateCVO("Parallelogram", "")
        p2=cvo.CVO().CreateCVO("Area Formula", "b*h")
        p3=cvo.CVO().CreateCVO("breadth","b")
        p4=cvo.CVO().CreateCVO("height","h")
        p5=cvo.CVO().CreateCVO("Example", "b=8 h=8")
        p6=cvo.CVO().CreateCVO("Area of Parallelogram", "64")
        p1.cvolist.append(p3)
        p1.cvolist.append(p4)
        p1.cvolist.append(p2)
        p2.cvolist.append(p5)
        p5.cvolist.append(p6)
        self.construct1(p1,p1)


    def Trapezium(self):
    
        self.isRandom = False
        self.positionChoice=[[-4.5,2,0],[0,2,0],[-5,-2,0],[-1,0,0],[1,-2,0],[5,0,0],[5,-2,0]]

        p1=cvo.CVO().CreateCVO("Trapezium","")
        p2=cvo.CVO().CreateCVO("Area Formula", "h*((a+b)/2)")
        p3=cvo.CVO().CreateCVO("height","h")
        p4=cvo.CVO().CreateCVO("parallel side 1","a")
        p5=cvo.CVO().CreateCVO("parallel side 2","b")
        p6=cvo.CVO().CreateCVO("Example", "a=8 b=8 h=4")
        p7=cvo.CVO().CreateCVO("Area of Trapezium", "24")
        p1.cvolist.append(p3)
        p1.cvolist.append(p4)
        p1.cvolist.append(p5)
        p1.cvolist.append(p2)
        p2.cvolist.append(p6)
        p6.cvolist.append(p7)
        self.construct1(p1,p1)

    def Circle(self):
   
        self.isRandom = False
        self.positionChoice=[[-4.5,2,0],[0,2,0],[-5,-2,0],[-1,0,0],[1,-2,0],[5,0,0]]

        p1=cvo.CVO().CreateCVO("Circle","")
        p2=cvo.CVO().CreateCVO("Area Formula","1/2(3.14)r*r")
        p3=cvo.CVO().CreateCVO("Radius","r")
        p4=cvo.CVO().CreateCVO("Example", "r=7")
        p5=cvo.CVO().CreateCVO("Area of Circle", "77")
        p1.cvolist.append(p3)
        p1.cvolist.append(p2)
        p2.cvolist.append(p4)
        p4.cvolist.append(p5)
        self.construct1(p1,p1)
    
if __name__ == "__main__":
    scene = planefiguresAnim()
    scene.render()