# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla
import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class QuadrilateralsAnim(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.Quadrilaterals()
        self.Diagonals()
        self.Adjacent()
        self.Opposite()
        self.Position()
        self.ConCaveEx()
        self.AngleSum()
        self.Types()
        self.Trapezium()
        self.Kite()
        self.Parallelogram()
        self.Rhombus()
        self.Rectangle()
        self.Square()
        # self.fadeOut()
        # self.constructDataByJSON()
        # self.fadeOut()
        
    # render using CVO data object
    def Quadrilaterals(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Quadrilaterals","")
        p11=cvo.CVO().CreateCVO("Properties","")
        p11onameList=["Closed figure","Has 4 Sides","Has 4 Vertices","Has 4 Angles"]
        p10.cvolist.append(p11)
        p11.extendOname(p11onameList)
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
    
    def Diagonals(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Diagonals", "")
        p11=cvo.CVO().CreateCVO("Definition", "Line segment joining opposite vertices")
        p10.cvolist.append(p11)
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Adjacent(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Adjacent", "Sides and Angles")
        p11=cvo.CVO().CreateCVO("Definition(Sides)", "Sides with a common vertex")
        p12=cvo.CVO().CreateCVO("Definition(Angles)", "Angles with a common side")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Opposite(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Opposite", "Sides and Angles")
        p11=cvo.CVO().CreateCVO("Definition(Sides)", "Sides without a common vertex")
        p12=cvo.CVO().CreateCVO("Definition(Angles)", "Angles without a common side")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
    
    def Position(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Quadrilateral", "Interior and Exterior")
        p11=cvo.CVO().CreateCVO("Interior", "Points inside quadrilateral")
        p12=cvo.CVO().CreateCVO("Exterior", "Points outside quadrilateral")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def ConCaveEx(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Quadrilateral", "Concave and Convex")
        p11=cvo.CVO().CreateCVO("Concave", "All line segments joining points may not be in the interior")
        p12=cvo.CVO().CreateCVO("Convex", "All line segments joining points is in the interior")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
    
    def AngleSum(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Angle Sum Property", "Sum of Angles: A+B+C+D").setPosition([-5,0,0])
        p11=cvo.CVO().CreateCVO("Angle 1", "A").setPosition([0,2.9,0])
        p12=cvo.CVO().CreateCVO("Angle 2", "B").setPosition([0,1,0])
        p13=cvo.CVO().CreateCVO("Angle 3", "C").setPosition([0,-1,0])
        p14=cvo.CVO().CreateCVO("Angle 4", "D").setPosition([0,-3.1,0])
        p15=cvo.CVO().CreateCVO("Sum of all Angles", "360 Degrees").setPosition([5,0,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        self.setNumberOfCirclePositions(6)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Types(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Quadrilateral", "Types").setPosition([0,0,0])
        p11=cvo.CVO().CreateCVO("Trapezium", "").setPosition([0,2.5,0])
        p12=cvo.CVO().CreateCVO("Kite", "").setPosition([3,2,0])
        p13=cvo.CVO().CreateCVO("Rhombus", "").setPosition([3,-2,0])
        p14=cvo.CVO().CreateCVO("Square","").setPosition([0,-2.5,0])
        p15=cvo.CVO().CreateCVO("Parallelogram", "").setPosition([-3,-2,0])
        p16=cvo.CVO().CreateCVO("Rectangle", "").setPosition([-3,2,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        p10.cvolist.append(p16)
        self.setNumberOfCirclePositions(7)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Trapezium(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Trapezium", "")
        p11=cvo.CVO().CreateCVO("Properties", "one pair of parallel sides")
        p10.cvolist.append(p11)
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
    
    def Kite(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Kite", "")
        p11=cvo.CVO().CreateCVO("Properties", "").setPosition([1,2,0])
        p11onameList=["Has 4 Sides","Two distinct, consecutive pairs of sides of equal length"]
        p10.cvolist.append(p11)
        p11.extendOname(p11onameList)
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
    
    def Parallelogram(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Parallelogram", "")
        p11=cvo.CVO().CreateCVO("Properties", "")
        p11onameList=["Opposite sides are equal in length","Opposite angles are equal", "Adjacent angles are supplementary", "Diagonals bisect each other"]
        p10.cvolist.append(p11)
        p11.extendOname(p11onameList)
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
    
    def Rhombus(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Rhombus", "")
        p11=cvo.CVO().CreateCVO("Properties", "Diagonals bisect perpendicularly")
        p10.cvolist.append(p11)
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Rectangle(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Rectangle", "")
        p11=cvo.CVO().CreateCVO("Properties", "")
        p11onameList=["Parallelogram with equal angles","Each angle is right angle","Opposite sides of equal length","Diagonals bisect each other","Diagonals of equal length"]
        p10.cvolist.append(p11)
        p11.extendOname(p11onameList)
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Square(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Square", "")
        p11=cvo.CVO().CreateCVO("Properties", "")
        p11onameList=["Adjacent sides of equal length","Diagonals bisect each other","Diagonals are of equal length","Diagonals are perpendicular"]
        p10.cvolist.append(p11)
        p11.extendOname(p11onameList)
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
    



if __name__ == "__main__":
    scene = QuadrilateralsAnim()
    scene.render()