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
        self.GithubSourceCodeReference()
        # self.fadeOut()
        # self.constructDataByJSON()
        # self.fadeOut()
        
    def SetDeveloperList(self):  
        self.DeveloperList="Hriday Bhushan"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Chap12Class7QuadAnim.py"

    # render using CVO data object
    def Quadrilaterals(self):
        self.isRandom = False
        self.angleChoice=[TAU/2]
        p10=cvo.CVO().CreateCVO("Quadrilaterals","").setPosition([-3,2,0])
        p11=cvo.CVO().CreateCVO("Properties","").setPosition([-3,-2,0])
        p11onameList=["Closed figure","Has 4 Sides","Has 4 Vertices","Has 4 Angles"]
        p10.cvolist.append(p11)
        p11.extendOname(p11onameList)
        triangle = Polygon([-1, -0.5, 0], [1, -0.5, 0], [0, 1.5, 0], color=BLUE)
        triangle.shift(RIGHT * 2 + DOWN *2)
        trianglelabel=Tex("Not Quadrilateral").next_to(triangle, DOWN, buff = 0.1)
        Quadrilaterals = Polygon([-1, 0.5, 0], [1, 0.5, 0], [2, 1.5, 0], [-2,1.5,0], color=BLUE)
        Quadrilaterals.shift(RIGHT * 2 + UP * 2)
        quadlabel=Tex("Quadrilateral").next_to(Quadrilaterals, DOWN, buff = 0.1)

        
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        self.play(Create(Quadrilaterals),Create(quadlabel),Create(triangle),Create(trianglelabel))
        self.wait(3)
        self.fadeOutCurrentScene()
    
    def Diagonals(self):
        self.isRandom = False
        self.angleChoice=[TAU/2]
        p10=cvo.CVO().CreateCVO("Diagonals", "").setPosition([-3,2,0])
        p11=cvo.CVO().CreateCVO("Definition", "Line segment joining opposite vertices").setPosition([-3,-2,0])
        p10.cvolist.append(p11)
        
        diagonalline = Line(start=[-1,0.5,0], end=[2,1.5,0], color = RED )
        diagonalline.shift(RIGHT * 2)
        diaglabel=Tex("Diagonal").next_to(diagonalline, LEFT, buff=0.1).set_color(RED).scale(0.5).shift(RIGHT*1.8)
        
        Quadrilaterals = Polygon([-1, 0.5, 0], [1, 0.5, 0], [2, 1.5, 0], [-2,1.5,0], color=BLUE)
        Quadrilaterals.shift(RIGHT * 2 )
        quadlabel=Tex("Quadrilateral").next_to(Quadrilaterals, DOWN, buff = 0.1)
        
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        self.play(Create(Quadrilaterals),Create(quadlabel))
        self.play(Create(diagonalline),Create(diaglabel))
        self.wait(3)
        self.fadeOutCurrentScene()

    def Adjacent(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Adjacent", "Sides and Angles").setPosition([-3,2,0])
        p11=cvo.CVO().CreateCVO("Definition(Sides)", "Sides with a common vertex").setPosition([-3.5,-2,0])
        p12=cvo.CVO().CreateCVO("Definition(Angles)", "Angles with a common side").setPosition([0,-2,0])

        diagonalline1 = Line(start=[-1, 0.5, 0], end=[1, 0.5, 0], color = RED )
        diagonalline1.shift(RIGHT * 2 + UP * 1)
        
        diagonalline2 = Line(start=[-1, 0.5, 0], end=[-2,1.5,0], color = RED )
        diagonalline2.shift(RIGHT * 2 + UP * 1)

        Quadrilaterals = Polygon([-1, 0.5, 0], [1, 0.5, 0], [2, 1.5, 0], [-2,1.5,0], color=BLUE)
        Quadrilaterals.shift(RIGHT * 2 + UP * 1)
        quadlabel=Tex("Adjacent Sides").next_to(Quadrilaterals, DOWN, buff = 0.1)
        

        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)
        self.play(Create(Quadrilaterals),Create(quadlabel))
        self.play(Create(diagonalline1),Create(diagonalline2))
        self.wait(3)
        self.fadeOutCurrentScene()

    def Opposite(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Opposite", "Sides and Angles").setPosition([-3,2,0])
        p11=cvo.CVO().CreateCVO("Definition(Sides)", "Sides without a common vertex").setPosition([-3.5,-2,0])
        p12=cvo.CVO().CreateCVO("Definition(Angles)", "Angles without a common side").setPosition([0,-2,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)

        diagonalline1 = Line(start=[-1, 0.5, 0], end=[1, 0.5, 0], color = RED)
        diagonalline1.shift(RIGHT * 2 + UP * 1)
        
        diagonalline2 = Line(start=[2, 1.5, 0], end=[-2,1.5,0], color = RED)
        diagonalline2.shift(RIGHT * 2 + UP * 1)


        Quadrilaterals = Polygon([-1, 0.5, 0], [1, 0.5, 0], [2, 1.5, 0], [-2,1.5,0], color=BLUE)
        Quadrilaterals.shift(RIGHT * 2 + UP * 1)
        quadlabel=Tex("Opposite Sides").next_to(Quadrilaterals, DOWN, buff = 0.1)

        

        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)
        self.play(Create(Quadrilaterals),Create(quadlabel))
        self.play(Create(diagonalline1),Create(diagonalline2))
        self.wait(3)
        self.fadeOutCurrentScene()
    
    def Position(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Quadrilateral", "Interior and Exterior")
        p11=cvo.CVO().CreateCVO("Interior", "Points inside quadrilateral")
        p12=cvo.CVO().CreateCVO("Exterior", "Points outside quadrilateral")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.setcircleradius(1.5)
        p11.setcircleradius(1.5)
        p12.setcircleradius(1.5)
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
        p10.setcircleradius(1.5)
        p11.setcircleradius(1.5)
        p12.setcircleradius(1.5)
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
        self.angleChoice=[TAU/2]
        p10=cvo.CVO().CreateCVO("Trapezium", "").setPosition([-3,2,0])
        p11=cvo.CVO().CreateCVO("Properties", "one pair of parallel sides").setPosition([-3,-2,0])
        p11.setcircleradius(2)

        Quadrilaterals = Polygon([-1, 0.5, 0], [1, 0.5, 0], [2.5, 1.5, 0], [-2,1.5,0], color=BLUE)
        Quadrilaterals.shift(RIGHT * 2 )
        quadlabel=Tex("Trapezium").next_to(Quadrilaterals, DOWN, buff = 0.1)

        p10.cvolist.append(p11)
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)

        self.play(Create(Quadrilaterals),Create(quadlabel))
        self.wait(3)

        self.fadeOutCurrentScene()
    
    def Kite(self):
        self.isRandom = False
        self.angleChoice=[TAU/2]
        p10=cvo.CVO().CreateCVO("Kite", "").setPosition([-3,2,0])
        p11=cvo.CVO().CreateCVO("Properties", "").setPosition([-3,-2,0])
        p11onameList=["Has 4 Sides","Two distinct, consecutive pairs of sides of equal length"]
        p10.cvolist.append(p11)
        p11.extendOname(p11onameList)
        p11.setcircleradius(2)

        Quadrilaterals = Polygon([-1,2, 0], [0, 0, 0], [1, 2, 0], [0,3,0], color=BLUE)
        Quadrilaterals.shift(RIGHT * 2)
        quadlabel=Tex("Kite").next_to(Quadrilaterals, DOWN, buff = 0.1)

        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)

        self.play(Create(Quadrilaterals),Create(quadlabel))
        self.wait(3)

        self.fadeOutCurrentScene()
    
    def Parallelogram(self):
        self.isRandom = False
        self.angleChoice=[TAU/2]
        p10=cvo.CVO().CreateCVO("Parallelogram", "").setPosition([-3,2,0])
        p11=cvo.CVO().CreateCVO("Properties", "").setPosition([-3,-2,0])
        p11onameList=["Opposite sides are equal in length","Opposite angles are equal", "Adjacent angles are supplementary", "Diagonals bisect each other"]
        p10.cvolist.append(p11)
        p11.extendOname(p11onameList)
        p11.setcircleradius(2)

        Quadrilaterals = Polygon([-1, 0.5, 0], [0, 0.5, 0], [-0.5, 1.5, 0], [-1.5,1.5,0], color=BLUE)
        Quadrilaterals.shift(RIGHT * 2 )
        quadlabel=Tex("Parallelogram").next_to(Quadrilaterals, DOWN, buff = 0.1)

        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)

        self.play(Create(Quadrilaterals),Create(quadlabel))
        self.wait(3)

        self.fadeOutCurrentScene()
    
    def Rhombus(self):
        self.isRandom = False
        self.angleChoice=[TAU/2]
        p10=cvo.CVO().CreateCVO("Rhombus", "").setPosition([-3,2,0])
        p11=cvo.CVO().CreateCVO("Properties", "Diagonals bisect perpendicularly").setPosition([-3,-2,0])
        p10.cvolist.append(p11)
        p11.setcircleradius(2)

        Quadrilaterals = Polygon([-1,1.5, 0], [0, 0, 0], [1, 1.5, 0], [0,3,0], color=BLUE)
        Quadrilaterals.shift(RIGHT * 2)
        quadlabel=Tex("Rhombus").next_to(Quadrilaterals, DOWN, buff = 0.1)

        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)

        self.play(Create(Quadrilaterals),Create(quadlabel))
        self.wait(3)

        self.fadeOutCurrentScene()

    def Rectangle(self):
        self.isRandom = False
        self.angleChoice=[TAU/2]
        p10=cvo.CVO().CreateCVO("Rectangle", "").setPosition([-3,2,0])
        p11=cvo.CVO().CreateCVO("Properties", "").setPosition([-3,-2,0])
        p11onameList=["Parallelogram with equal angles","Each angle is right angle","Opposite sides of equal length","Diagonals bisect each other","Diagonals of equal length"]
        p10.cvolist.append(p11)
        p11.extendOname(p11onameList)
        p11.setcircleradius(1.5)

        Quadrilaterals = Polygon([-1, 0.5, 0], [1, 0.5, 0], [1, 1.5, 0], [-1,1.5,0], color=BLUE)
        Quadrilaterals.shift(RIGHT * 2 )
        quadlabel=Tex("Rectangle").next_to(Quadrilaterals, DOWN, buff = 0.1)

        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)

        self.play(Create(Quadrilaterals),Create(quadlabel))
        self.wait(3)

        self.fadeOutCurrentScene()

    def Square(self):
        self.isRandom = False
        self.angleChoice=[TAU/2]
        p10=cvo.CVO().CreateCVO("Square", "").setPosition([-3,2,0])
        p11=cvo.CVO().CreateCVO("Properties", "").setPosition([-3,-2,0])
        p11onameList=["Adjacent sides of equal length","Diagonals bisect each other","Diagonals are of equal length","Diagonals are perpendicular"]
        p10.cvolist.append(p11)
        p11.extendOname(p11onameList)
        p11.setcircleradius(2)

        Quadrilaterals = Polygon([-1, 0.5, 0], [1, 0.5, 0], [1, 2.5, 0], [-1,2.5,0], color=BLUE)
        Quadrilaterals.shift(RIGHT * 2 )
        quadlabel=Tex("Square").next_to(Quadrilaterals, DOWN, buff = 0.1)

        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)

        self.play(Create(Quadrilaterals),Create(quadlabel))
        self.wait(3)

        self.fadeOutCurrentScene()
    



if __name__ == "__main__":
    scene = QuadrilateralsAnim()
    scene.render()