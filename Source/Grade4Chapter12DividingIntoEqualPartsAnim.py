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

class EqualPartsAnim(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.Division()
        self.FracRep1()
        self.ShapeExample()
        self.FracRep2()
        self.Example1()
        self.GithubSourceCodeReference()

        
        # self.fadeOut()
        # self.constructDataByJSON()
        # self.fadeOut()
        
    def SetDeveloperList(self):  
        self.DeveloperList="Hriday Bhushan"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade4Chapter12DividingIntoEqualParts.py"
    
    # render using CVO data object
    def Division(self):
        title = Text("Dividing into Equal Parts", font_size=36).to_edge(UP)
        self.play(Create(title))
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Division of Parts","")
        p11=cvo.CVO().CreateCVO("Definition","Dividing an object or item into its equal parts")
        
        p10.setcircleradius(1.2)
        p11.setcircleradius(1.2)
        p10.cvolist.append(p11)
        
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def FracRep1(self):
        title = Text("Representation in Fractions", font_size=36).to_edge(UP)
        self.play(Create(title))
        self.isRandom = False
        self.angleChoice = [TAU/2]
        p10=cvo.CVO().CreateCVO("How to Represent","")
        p11=cvo.CVO().CreateCVO("Formula","Total Items/Total Segments")
        
        p10.cvolist.append(p11)
        
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        
        self.fadeOutCurrentScene()


    def ShapeExample(self):
         # Title
        title = Text("Shape Transformations and Divisions").scale(1).to_edge(UP)
        self.play(Write(title))
       
        
        # Create shapes
        circle = Circle()
        square = Square()
        triangle = Polygon([0, 1, 0], [-1, -1, 0], [1, -1, 0])
        #height_line = Line(start=[0.5, -1, 0], end=[0, 1, 0], color=YELLOW)

        # Positions
        circle.shift(LEFT * 4)
        square.shift(RIGHT * 4)
        triangle.shift(DOWN * 2)
        #height_line.shift(DOWN*2)

        circletext = Text("Dividing a circle into 4 parts").scale(0.8).next_to(title, DOWN*1.5)
        self.play(Write(circletext))
        # Show circle
        self.play(Create(circle))
        self.wait(2)
        
        # Divide circle into 4 parts
        circle_lines = VGroup(
            Line(circle.get_top(), circle.get_bottom()),
            Line(circle.get_left(), circle.get_right())
        )
        self.play(Create(circle_lines))
        self.wait(2)
        self.play(FadeOut(circletext))

        squaretext = Text("Dividing a square into 4 parts").scale(0.8).next_to(title, DOWN*1.5)
        self.play(Write(squaretext))

        # Transform circle to square
        #self.play(Transform(circle, square))
        #self.wait(2)
        
        # Divide square into 4 parts
        square_lines = VGroup(
            Line(square.get_top(), square.get_bottom()),
            Line(square.get_left(), square.get_right())
        )
        self.play(Transform(circle, square),Transform(circle_lines, square_lines))
        self.wait(2)
        self.play(FadeOut(squaretext))

        triangletext = Text("Dividing a triangle into 6 parts").scale(0.8).next_to(title, DOWN*1.5)
        self.play(Write(triangletext))
        
        # Transform square to triangle
        self.play(Transform(circle, triangle), FadeOut(circle_lines))
        self.wait(2)
        
        # Divide triangle into 3 parts
        triangle_lines = VGroup(
            Line(triangle.get_vertices()[0], triangle.get_vertices()[1]),
            Line(triangle.get_vertices()[1], triangle.get_vertices()[2]),
            Line(triangle.get_vertices()[2], triangle.get_vertices()[0])
        )
        triangle_divisions = VGroup(
            Line(triangle.get_vertices()[0], midpoint(triangle.get_vertices()[1], triangle.get_vertices()[2])),
            Line(triangle.get_vertices()[1], midpoint(triangle.get_vertices()[0], triangle.get_vertices()[2])),
            Line(triangle.get_vertices()[2], midpoint(triangle.get_vertices()[0], triangle.get_vertices()[1]))
        )
        self.play(Create(triangle_lines))
        self.play(Create(triangle_divisions))
        self.wait(2)
        
        # Fade out
        self.play(FadeOut(circle), FadeOut(triangle_lines), FadeOut(triangle_divisions), FadeOut(triangletext))
        self.wait(2)

        
        self.fadeOutCurrentScene()

    
    def FracRep2(self):
        title = Text("Representation in Fractions", font_size=36).to_edge(UP)
        self.play(Create(title))
        self.isRandom = False
        self.angleChoice = [TAU/2]
        p10=cvo.CVO().CreateCVO("How to Represent","").setPosition([4.5,1.5,0])
        p11=cvo.CVO().CreateCVO("Formula","Total Items/Total Segments").setPosition([4.5,-1.5,0])
        
        p10.cvolist.append(p11)
        
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        
        self.play(FadeOut(title))

    def Example1(self):
        title = Text("Example", font_size=36).to_edge(UP)
        self.play(Write(title))

        ex11 = Text("Divide 6 Balls between 3 Children", font_size=26).move_to(LEFT*3 + UP*1.5)
        self.play(Create(ex11))
        self.wait(2)
        ex12 = Text("Balls = 6 (Total Items)", font_size=26).next_to(ex11, DOWN*1.5)
        self.play(Create(ex12))
        self.wait(2)
        ex13 = Text("Children = 3 (Total Segments)", font_size=26).next_to(ex12, DOWN*1.5)
        self.play(Create(ex13))
        self.wait(2)
        ex14 = Text("6/3= 2 Balls per Children", font_size=26).next_to(ex13, DOWN*1.5)
        self.play(Create(ex14))
        self.wait(2)
        ex15 = Text("Hence, every child gets 2 balls", font_size=30).move_to(DOWN*2)
        self.play(Create(ex15))
        self.wait(2)
        self.fadeOutCurrentScene()
    

    
if __name__ == "__main__":
    scene = EqualPartsAnim()
    scene.render()