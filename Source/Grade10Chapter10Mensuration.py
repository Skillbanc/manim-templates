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

class Mensuration(AbstractAnim,ThreeDScene):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.Cuboid()
        self.fadeOutCurrentScene()
        self.Cuboidanim()
        self.fadeOutCurrentScene()
        self.Cube()
        self.fadeOutCurrentScene()
        self.Cubeanim()
        self.fadeOutCurrentScene()
        self.Rightprism()
        self.fadeOutCurrentScene()
        self.Rightprismanim()
        self.fadeOutCurrentScene()
        self.Cylinder()
        self.fadeOutCurrentScene()
        self.Cylinderanim()
        self.fadeOutCurrentScene()
        self.Rightpyramid()
        self.fadeOutCurrentScene()
        self.Rightpyramidanim()
        self.fadeOutCurrentScene()
        self.Rightcircularcone()
        self.fadeOutCurrentScene()
        self.Rightcircularconeanim()
        self.fadeOutCurrentScene()
        self.Sphere()
        self.fadeOutCurrentScene()
        self.Sphereanim()
        self.fadeOutCurrentScene()
        self.Hemisphere()
        self.fadeOutCurrentScene()
        self.Hemisphereanim()
        self.fadeOutCurrentScene()
        self.CombinationOfSolids()
        self.fadeOutCurrentScene()
        self.COSanim()
        self.fadeOutCurrentScene()
        self.Conversion()
        self.fadeOutCurrentScene()
        self.SolidConversion3D()
        self.fadeOutCurrentScene()
        self.Volume()
        self.fadeOutCurrentScene()
        self.VolumeAnim()
        self.fadeOutCurrentScene()

        self.GithubSourceCodeReference()
        


    # render using CVO data object  
    def Cuboid(self):
        self.positionChoice = [[-4,0,0],[0,2,0],[2,-2,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Cuboid","")
        p11=cvo.CVO().CreateCVO("Lateral Surface Area","2h(l+b)")
        p12=cvo.CVO().CreateCVO("Total Surface Area","2(lb+bh+lh)")
        p13=cvo.CVO().CreateCVO("Volume","l*b*h").setPosition([0,2,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.setcircleradius(1.6)
        p11.setcircleradius(1.6)
        p12.setcircleradius(1.6)
        p13.setcircleradius(1.6)
        self.setNumberOfCirclePositions(4)
        self.construct1(p10,p10)

    def Cuboidanim(self):
        # Title
        title = Text("Cuboid", color=RED, weight=BOLD)
        title.move_to([0, 3, 0])
        underline = Underline(title)

        # Coordinates for the wider cuboid centered around the origin
        a = ((3, -2.25, 0), (-3, -2.25, 0), (-4, -2.75, 0), (2, -2.75, 0), (3, -2.25, 0))
        base = Polygon(*a, stroke_width=5,color=WHITE)
        
        b = ((3, 0.75, 0), (-3, 0.75, 0), (-4, 0.25, 0), (2, 0.25, 0), (3, 0.75, 0))
        top = Polygon(*b, stroke_width=5,color=WHITE)
        
        c = ((3.1, 0.75, 0), (3.1, -2.25, 0), (2, -2.75, 0), (2, 0.25, 0), (3, 0.75, 0))
        face1 = Polygon(*c, stroke_width=5,color=WHITE)
        
        d = ((3, 0.75, 0), (-3, 0.75, 0), (-3, -2.25, 0), (3.1, -2.25, 0), (3.1, 0.75, 0))
        face2 = Polygon(*d, stroke_width=5,color=WHITE)
        
        e = ((-3, 0.75, 0), (-3, -2.25, 0), (-4, -2.75, 0), (-4, 0.25, 0), (-3, 0.75, 0))
        face3 = Polygon(*e,  stroke_width=5,color=WHITE)
        
        f = ((2, 0.25, 0), (2, -2.75, 0), (-4, -2.75, 0), (-4, 0.25, 0), (2, 0.25, 0))
        face4 = Polygon(*f, stroke_width=5,color=WHITE)
         
        
        # Labels for dimensions
        l_label = Text("l", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        l_label.next_to(base.get_edge_center(DOWN), DOWN)
        b_label = Text("b", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        b_label.next_to(base.get_edge_center(RIGHT), DOWN)
        h_label = Text("h", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        h_label.next_to(top.get_edge_center(RIGHT), RIGHT)

        self.play(Write(title))
        self.play(Create(underline))
        self.play(Write(base))
        self.play(Write(top))
        self.play(Write(face1))
        self.play(Write(face2))
        self.play(Write(face3))
        self.play(Write(face4))
        self.play(Write(l_label))
        self.play(Write(b_label))
        self.play(Write(h_label))
        self.wait()

    def Cube(self):
        self.positionChoice = [[-4,0,0],[0,2,0],[2,-2,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Cube","")
        p11=cvo.CVO().CreateCVO("Lateral Surface Area","$4a^2$")
        p12=cvo.CVO().CreateCVO("Total Surface Area","$6a^2$")
        p13=cvo.CVO().CreateCVO("Volume","$a^3$").setPosition([0,2,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.setcircleradius(1.6)
        p11.setcircleradius(1.6)
        p12.setcircleradius(1.6)
        p13.setcircleradius(1.6)
        self.setNumberOfCirclePositions(4)
        self.construct1(p10,p10)

    def Cubeanim(self):
        # Title
        title = Text("Cube", color=RED, weight=BOLD)
        title.move_to([0, 2.5, 0])
        underline = Underline(title)

         # Coordinates for the cuboid centered around the origin with increased height
        a = ((-1, -0.75, 0), (1, -0.75, 0), (2, -1.25, 0), (0, -1.25, 0), (-1, -0.75, 0))
        base = Polygon(*a,stroke_width=5,color=WHITE)
    
    # Adjusted y-coordinates for the top to increase height
        b = ((-1, 1.0, 0), (1, 1.0, 0), (2, 0.5, 0), (0, 0.5, 0), (-1, 1.0, 0))
        top = Polygon(*b, stroke_width=5,color=WHITE)
    
        c = ((-1.1, 1.0, 0), (-1.1, -0.75, 0), (0, -1.25, 0), (0, 0.5, 0), (-1, 1.0, 0))
        face1 = Polygon(*c,stroke_width=5,color=WHITE)
    
        d = ((-1, 1.0, 0), (1, 1.0, 0), (1, -0.75, 0), (-1.1, -0.75, 0), (-1.1, 1.0, 0))
        face2 = Polygon(*d,stroke_width=5,color=WHITE)
    
        e = ((1, 1.0, 0), (1, -0.75, 0), (2.1, -1.25, 0), (2.1, 0.5, 0), (1, 1.0, 0))
        face3 = Polygon(*e, stroke_width=5,color=WHITE)
    
        f = ((0, 0.5, 0), (0, -1.25, 0), (2.1, -1.25, 0), (2.1, 0.5, 0), (0, 0.5, 0))
        face4 = Polygon(*f, stroke_width=5,color=WHITE)
    
        
    
        # Labels for dimensions
        l_label = Text("a", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        l_label.next_to(base.get_edge_center(DOWN), DOWN)
        b_label = Text("a", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        b_label.next_to(base.get_edge_center(LEFT), DOWN)
        h_label = Text("a", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        h_label.next_to(base.get_edge_center(RIGHT*0.5), UP*2)
    
        cube_group = VGroup(title,underline,base, top, face1, face2, face3, face4, l_label, b_label, h_label)

        self.play(Write(title))
        self.play(Write(underline))
        self.play(Write(base))
        self.play(Write(top))
        self.play(Write(face1))
        self.play(Write(face2))
        self.play(Write(face3))
        self.play(Write(face4))
        self.play(Write(l_label))
        self.play(Write(b_label))
        self.play(Write(h_label))
        self.wait()
    
    # Apply rotation to the whole cube
        self.play(Rotate(cube_group, angle=PI/2, axis=RIGHT), run_time=2)
        self.wait()
    
    def Rightprism(self):
        self.positionChoice = [[-4,0,0],[0,2,0],[2,-2,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Right Prism","")
        p11=cvo.CVO().CreateCVO("Lateral Surface Area","Perimeter of base*height")
        p12=cvo.CVO().CreateCVO("Total Surface Area","LSA+2(area of end surface)")
        p13=cvo.CVO().CreateCVO("Volume","Area of base*height").setPosition([0,2,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.setcircleradius(1.6)
        p11.setcircleradius(1.8)
        p12.setcircleradius(1.8)
        p13.setcircleradius(1.8)
        self.setNumberOfCirclePositions(4)
        self.construct1(p10,p10)

    def Rightprismanim(self):
        # Title
        title = Text("Right Prism", color=RED, weight=BOLD)
        title.move_to([0, 3, 0])
        underline = Underline(title)

        # Define vertices of the prism
        a = ((-1.1, -1.75, 0), (-2.9, -1.75, 0), (-3.2, -2.25, 0), (-1.1, -1.75, 0))
        base = Polygon(*a, stroke_width=5, color=WHITE)

        b = ((-1.1, 1.25, 0), (-2.9, 1.25, 0), (-3.2, 0.75, 0), (-1.1, 1.25, 0))
        top = Polygon(*b, stroke_width=5, color=WHITE)

        c = ((-1.1, -1.75, 0), (-1.1, 1.25, 0), (-3.2, 0.75, 0), (-3.2, -2.25, 0), (-1.1, -1.75, 0))
        face1 = Polygon(*c, stroke_width=5, color=WHITE)

        d = ((-1.1, -1.75, 0), (-1.1, 1.25, 0), (-2.9, 1.25, 0), (-2.9, -1.75, 0), (-1.1, -1.75, 0))
        face2 = Polygon(*d, stroke_width=5, color=WHITE)

        e = ((-2.9, 1.25, 0), (-2.9, -1.75, 0), (-3.2, -2.25, 0), (-3.2, 0.75, 0), (-2.9, 1.25, 0))
        face3 = Polygon(*e, stroke_width=5, color=WHITE)

        # Create a VGroup for the prism and center it
        prism = VGroup(base, top, face1, face2, face3)
        prism.move_to(ORIGIN)

        # Animation to display the title and underline
        self.play(Write(title))
        self.play(Write(underline))

        # Animations to display the prism
        self.play(Write(base))
        self.play(Write(top))
        self.play(Write(face1))
        self.play(Write(face2))
        self.play(Write(face3))

        # Wait before ending the scene
        self.wait()  

    def Cylinder(self):
        self.positionChoice = [[-4,0,0],[0,2,0],[2,-2,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Cylinder","")
        p11=cvo.CVO().CreateCVO("Lateral surface Area","$2\pi rh$")
        p12=cvo.CVO().CreateCVO("Total Surface Area","$2\pi r(r+h)$")
        p13=cvo.CVO().CreateCVO("Volume","$\pi r^2h$").setPosition([0,2,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.setcircleradius(1.6)
        p11.setcircleradius(1.6)
        p12.setcircleradius(1.6)
        p13.setcircleradius(1.6)
        self.setNumberOfCirclePositions(4)
        self.construct1(p10,p10)

    def Cylinderanim(self):
         # Create the text
        title = Text("Cylinder", color=RED, weight=BOLD)
        title.move_to([0, 3, 0])
        underline = Underline(title)

        # Create base and top ellipses
        base = Ellipse(color=WHITE)
        top = Ellipse(color=WHITE)

        # Set the angle for the ellipses
        angle = PI / 4  # 45 degrees in radians
        base.rotate(angle, axis=RIGHT)
        top.rotate(angle, axis=RIGHT)

        # Create the lines
        line1 = Line(start=[-1, -1.5, 0], end=[-1, 1.5, 0], color=WHITE)
        line2 = Line(start=[1, -1.5, 0], end=[1, 1.5, 0], color=WHITE)
        # Position the base and top
        base.move_to([0, -1.5, 0])
        top.move_to([0, 1.5, 0])
         # Create labels
        l_label = Text("r", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        l_label.next_to(base.get_edge_center(DOWN), DOWN)
        h_label = Text("h", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        h_label.next_to(base.get_edge_center(RIGHT) + RIGHT * 0.5, UP * 2)

        # Play animations
        self.play(Write(title))
        self.play(Write(underline))
        self.play(Write(base))
        self.play(Write(top))
        self.play(Write(line1))
        self.play(Write(line2))
        self.play(Write(l_label), Write(h_label))

    def Rightpyramid(self):
        self.positionChoice = [[-4,0,0],[0,2,0],[2,-2,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Right Pyramid","")
        p11=cvo.CVO().CreateCVO("Lateral surface Area","1/2(perimeter of base)*slant height")
        p12=cvo.CVO().CreateCVO("Total Surface Area","LSA+area of base")
        p13=cvo.CVO().CreateCVO("Volume","1/3area of base*height").setPosition([0,2,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.setcircleradius(1.6)
        p11.setcircleradius(2.0)
        p12.setcircleradius(1.8)
        p13.setcircleradius(1.8)
        self.setNumberOfCirclePositions(4)
        self.construct1(p10,p10)

    def Rightpyramidanim(self):
        # Title
        title = Text("Right Pyramid", color=RED, weight=BOLD)
        title.move_to([0, 3, 0])
        underline = Underline(title)
        
        # Define the base of the pyramid (square)
        base_points = [(-2, -1, 0), (2, -1, 0), (1, -3, 0), (-3, -3, 0)]
        base = Polygon(*base_points, stroke_width=5, color=WHITE)

        # Apex of the pyramid
        apex = [0, 2, 0]

        # Faces of the pyramid
        face1 = Polygon(apex, base_points[0], base_points[1], stroke_width=5, color=WHITE)
        face2 = Polygon(apex, base_points[1], base_points[2], stroke_width=5, color=WHITE)
        face3 = Polygon(apex, base_points[2], base_points[3], stroke_width=5, color=WHITE)
        face4 = Polygon(apex, base_points[3], base_points[0], stroke_width=5, color=WHITE)

        # Dotted line for the height
        height_line = DashedLine(start=apex, end=[0, -2, 0], color=RED)

        # Dot at the end of the height line
        center_dot = Dot(point=[0, -2, 0], color=WHITE)

        # Normal line for slant height
        slant_height_line = Line(start=apex, end=base_points[1], color=RED)

        # Labels
        height_label = Text("height", color=WHITE).scale(0.5)
        slant_height_label = Text("slant height", color=WHITE).scale(0.5)

        # Adjust labels' positions
        height_label.next_to(height_line, LEFT)
        slant_height_label.next_to(slant_height_line, RIGHT)

        # Group all objects to move them together
        group = VGroup(title, underline, base, face1, face2, face3, face4, height_line, center_dot, slant_height_line, height_label, slant_height_label)
        
        # Center the group
        group.move_to([0, 0, 0]) 

        # Animation to display the group
        self.play(Write(group))
        self.wait()

    def Rightcircularcone(self):
        self.positionChoice = [[-4,0,0],[0,2,0],[2,-2,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Right Circular Cone","")
        p11=cvo.CVO().CreateCVO("Lateral Surface Area","$\pi rl$")
        p12=cvo.CVO().CreateCVO("Total Surface Area","$\pi r(r+l)$")
        p13=cvo.CVO().CreateCVO("Volume","$1/3 \pi r^2h$").setPosition([0,2,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.setcircleradius(1.6)
        p11.setcircleradius(1.6)
        p12.setcircleradius(1.6)
        p13.setcircleradius(1.6)
        self.setNumberOfCirclePositions(4)
        self.construct1(p10,p10)

    def Rightcircularconeanim(self):
        # Title
        title = Text("Right Circular Cone", color=RED, weight=BOLD)
        title.move_to([0, 3, 0])
        underline = Underline(title)
        # Create the cone
        cone = Polygon(
            [0, 2, 0],  # Top point of the cone
            [-2, -1, 0],  # Bottom left point
            [2, -1, 0],  # Bottom right point
            color=WHITE
        )
        
        # Create the horizontal ellipse (base)
        base = Ellipse(width=4, height=0.4, color=WHITE).shift(DOWN*1.5)
        
        # Create the vertical line representing the height
        height_line = Line(start=[0, 2, 0], end=[0, -1, 0], color=WHITE)
        
        # Create the small filled circle at the center of the base
        center_dot = Dot(point=[0, -1, 0], color=WHITE)
        
        # Create the labels "h", "l", and "r"
        height_label = MathTex("h", color=WHITE)
        height_label.next_to(height_line, LEFT)
        
        slant_label = MathTex("l", color=WHITE)
        slant_label.move_to([1, 1, 0])
        
        radius_label = MathTex("r", color=WHITE)
        radius_label.move_to([1, -1.5, 0])
        
        # Position elements
        cone.shift(DOWN*0.5)
        height_line.shift(DOWN*0.5)
        center_dot.shift(DOWN*0.5)
        height_label.shift(DOWN*0.5)
        slant_label.shift(DOWN*0.5)
        radius_label.shift(DOWN*0.5)
        
        # Play animations
        self.play(Create(title))
        self.play(Create(underline))
        self.play(Create(cone))
        self.play(Create(base))
        self.play(Create(height_line))
        self.play(Create(center_dot))
        self.play(Write(height_label))
        self.play(Write(slant_label))
        self.play(Write(radius_label))
        
        # Final animation
        self.wait(2)

    def Sphere(self):
        self.positionChoice = [[-4,0,0],[2,2,0],[2,-2,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Sphere","")
        p11=cvo.CVO().CreateCVO("Lateral Surface Area","$4\pi r^2$")
        p12=cvo.CVO().CreateCVO("Total Surface Area","$4\pi r^2$")
        p13=cvo.CVO().CreateCVO("Volume","$4/3 \pi r^3$").setPosition([0,2,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.setcircleradius(1.6)
        p11.setcircleradius(1.6)
        p12.setcircleradius(1.6)
        p13.setcircleradius(1.6)
        self.setNumberOfCirclePositions(4)
        self.construct1(p10,p10)

    def Sphereanim(self):
        # Title
        title = Text("Sphere", color=RED, weight=BOLD)
        title.move_to([0, 3, 0])
        underline = Underline(title)

         # Create the circle representing the sphere
        sphere = Circle(radius=2, color=WHITE)
        
        # Create the horizontal ellipse (equator)
        equator = Ellipse(width=4, height=0.4, color=WHITE).shift(DOWN*0.5)
        
        # Create the dashed line representing the radius
        radius_line_horizontal = DashedLine(start=[0, 0, 0], end=[2, 0, 0], color=WHITE).shift(DOWN*0.5)
        
        # Create the small filled circle at the center of the horizontal ellipse
        center_dot = Dot(point=[0, 0, 0], color=WHITE).shift(DOWN*0.5)
        
        # Create the label "r"
        radius_label_horizontal = MathTex("r", color=WHITE)
        radius_label_horizontal.next_to(radius_line_horizontal, UP*0.1)
        
        # Position elements
        sphere.shift(DOWN*0.5)
        radius_label_horizontal.shift(DOWN*0.5)
        
        # Play animations
        self.play(Create(title))
        self.play(Create(underline))
        self.play(Create(sphere))
        self.play(Create(equator))
        self.play(Create(radius_line_horizontal))
        self.play(Create(center_dot))
        self.play(Write(radius_label_horizontal))
        
        # Final animation
        self.wait(2)

    def Hemisphere(self):
        
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Hemisphere","").setPosition([-4,-2,0])
        p11=cvo.CVO().CreateCVO("Lateral Surface Area","$2\pi r^2$").setPosition([2,2,0])
        p12=cvo.CVO().CreateCVO("Total Surface Area","$3\pi r^2$").setPosition([3.5,-1.5,0])
        p13=cvo.CVO().CreateCVO("Volume","$2/3\pi r^3$").setPosition([-3,2,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.setcircleradius(1.6)
        p11.setcircleradius(1.6)
        p12.setcircleradius(1.6)
        p13.setcircleradius(1.6)
        self.construct1(p10,p10)

    def Hemisphereanim(self):
        title = Text("Hemisphere", color=RED, weight=BOLD)
        title.move_to([0, 3, 0])
        underline = Underline(title)
        
         # Create the semicircle representing the hemisphere
        hemisphere = Arc(radius=2, start_angle=PI, angle=PI, color=WHITE)
        
        # Create the horizontal ellipse (equator)
        equator = Ellipse(width=4, height=0.75, color=WHITE).shift(DOWN*1)
        
        # Create the dashed lines representing the radius
        radius_line_horizontal = DashedLine(start=[0, 0, 0], end=[2, 0, 0], color=WHITE)
        radius_line_vertical = DashedLine(start=[0, 0, 0], end=[0, -2, 0], color=WHITE)
        
        # Create the small filled circle at the center
        center_dot = Dot(point=[0, 0, 0], color=WHITE)
        
        # Create the label "r"
        radius_label_horizontal = MathTex("r", color=WHITE)
        radius_label_horizontal.next_to(radius_line_horizontal, UP)
        radius_label_vertical = MathTex("r", color=WHITE)
        radius_label_vertical.next_to(radius_line_vertical, LEFT)
        
        # Position elements

        hemisphere.shift(DOWN*1)
        radius_line_horizontal.shift(DOWN*1)
        radius_line_vertical.shift(DOWN*1)
        center_dot.shift(DOWN*1)
        radius_label_horizontal.shift(DOWN*0.7)
        radius_label_vertical.shift(DOWN*1)
        
        # Play animations
        self.play(Create(title))
        self.play(Create(underline))
        self.play(Create(hemisphere))
        self.play(Create(equator))
        self.play(Create(radius_line_horizontal))
        self.play(Create(radius_line_vertical))
        self.play(Create(center_dot))
        self.play(Write(radius_label_horizontal))
        self.play(Write(radius_label_vertical))
        
        # Final animation
        self.wait(2)

    def CombinationOfSolids(self):
        
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Combination of Solids","").setPosition([-4,-2,0])
        p11=cvo.CVO().CreateCVO("Example","oil tanker").setPosition([0,2,0])
        p12=cvo.CVO().CreateCVO("Formula","TSA of new solid=CSA of Hemisphere1+CSA of Cylinder+CSA of Hemisphere2").setPosition([3.5,-1.5,0])
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p10.setcircleradius(1.6)
        p11.setcircleradius(2.0)
        p12.setcircleradius(2.8)
        self.construct1(p10,p10)

    def COSanim(self):
        # Title
        title = Text("Surface Area Of The Combination Of Solids", font_size=36,color=RED)
        title.to_edge(UP)
        underline = Underline(title)
        self.play(Write(title))
        self.play(Create(underline))
        self.wait(1)

        # Info text in multiple lines
        info_text = Paragraph(
            "An oil tanker was made up of a cylinder with two hemispheres stuck at either ends.\n"
            "If we consider the surface of newly formed we would be able to see the curved surface \n"
            "of the two hemispheres and curved surface of cylinder.",
            alignment="left",
            font_size=24
        )
        info_text.next_to(title, DOWN, buff=0.5)
        self.play(Write(info_text))
        self.wait(2)

        # Set up the scene
        # self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Create the central cylinder
        cylinder = Cylinder(radius=1, height=3, direction=OUT, resolution=(24, 24))
        
        # Create the left hemisphere
        left_hemisphere = Sphere(radius=1)
        left_hemisphere.scale([1, 1, 1])
        left_hemisphere.shift(1.5 * LEFT)
        
        # Create the right hemisphere
        right_hemisphere = Sphere(radius=1)
        right_hemisphere.scale([1, 1, 1])
        right_hemisphere.shift(1.5 * RIGHT)
        
        # Rotate hemispheres to match the correct orientation
        left_hemisphere.rotate(PI / 2, axis=RIGHT)
        right_hemisphere.rotate(PI / 2, axis=RIGHT)
        
        # Add shapes to scene
        self.add(cylinder, left_hemisphere, right_hemisphere)

        # Animate the shapes
        self.play(
            Create(cylinder),
            Create(left_hemisphere),
            Create(right_hemisphere)
        )
        self.wait(1)
        self.play(Rotate(cylinder, PI / 2, axis=UP))
        self.wait(1)

        # New Solid
        new_solid = Text("TSA of new solid = CSA of one hemisphere + CSA of cylinder + CSA of another hemisphere", font_size=24)
        new_solid.next_to(info_text, DOWN * 7, buff=0.5)
        self.play(Write(new_solid))
        self.wait(2)

# Further adjust the position of the new_solid text
        # new_solid.shift(DOWN * 3)
        # self.play(Write(new_solid))
        # self.wait(2)

        
        
    def Conversion(self):
        
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Conversion ","Solid").setPosition([-5,0,0])
        p11=cvo.CVO().CreateCVO("shape 1","Cuboid").setPosition([-2,0,0])
        p12=cvo.CVO().CreateCVO("shape 2","Cylinder").setPosition([1,0,0])
        p13=cvo.CVO().CreateCVO("shape 3","Sphere").setPosition([4,0,0])
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        p10.setcircleradius(1.6)
        p11.setcircleradius(1.6)
        p12.setcircleradius(1.6)
        p13.setcircleradius(1.6)
        self.setNumberOfCirclePositions(4)
        self.construct1(p10,p10)

    def SolidConversion3D(self):
        # Title
        title = Text("Conversion of Solid from One Shape to Another", font_size=36,color=RED)
        title.to_edge(UP)
        underline = Underline(title)
        self.play(Write(title))
        self.play(Create(underline))
        
        self.wait(1)

        # Info text in multiple lines
        info_text = Paragraph(
            "If you want a candle of any special shape, you have to heat the wax in a metal container\n till it is completely melted.",
            "Then, you pour it into another container which has the special shape that you wanted.",
            "For example, let's take a candle in the shape of a cuboid,\n melt it, and pour the whole of the molten wax into another container shaped like a cylinder.\n",
            "On cooling, you can obtain a candle in the shape of a sphere. \nThe volume of the new candle will be the same as the volume of the earlier candle.",
            alignment="left",
            font_size=24
        )
        info_text.next_to(title, DOWN, buff=0.5)
        self.play(Write(info_text))
        self.wait(2)

        # Setup camera orientation
        # self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)

        # Cuboid
        cuboid = Prism(dimensions=[2, 1, 1], fill_opacity=0.5, fill_color=BLUE).shift(LEFT * 4 + DOWN * 2)
        cuboid_label = MathTex("Cuboid").next_to(cuboid, DOWN)

        # Cylinder
        cylinder = Cylinder(radius=1, height=2, direction=UP, fill_opacity=0.5, fill_color=GREEN).shift(DOWN * 2)
        cylinder_label = MathTex("Cylinder").next_to(cylinder, DOWN)

        # Sphere
        sphere = Sphere(radius=1, fill_opacity=0.5, fill_color=RED).shift(RIGHT * 4 + DOWN * 2)
        sphere_label = MathTex("Sphere").next_to(sphere, DOWN)

        # Display Cuboid
        self.play(Create(cuboid), Write(cuboid_label))
        self.wait(1)

        # Melt Cuboid (Fade out)
        self.play(FadeOut(cuboid, shift=DOWN))
        self.wait(1)

        # Pour into Cylinder (Fade in)
        self.play(FadeIn(cylinder, shift=UP), Write(cylinder_label))
        self.wait(1)

        # Melt Cylinder (Fade out)
        self.play(FadeOut(cylinder, shift=DOWN))
        self.wait(1)

        # Pour into Sphere (Fade in)
        self.play(FadeIn(sphere, shift=UP), Write(sphere_label))
        self.wait(1)

        # Volume Conservation
        volume_text = Text("Volume of the new candle is the same as the volume of the earlier candle", font_size=24)
        volume_text.next_to(info_text, DOWN, buff=0.5)
        self.play(Write(volume_text))
        self.wait(2)


    def Volume(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("volume of combinations of solid","").setPosition([-3,0,0])
        p11=cvo.CVO().CreateCVO("Example","").setPosition([3,0,0])
        p10.cvolist.append(p11)
        p10.setcircleradius(1.6)
        p11.setcircleradius(1.6)
        self.construct1(p10,p10)

    def VolumeAnim(self):
       
        # Title
        title = Text("VOLUME OF COMBINATION OF SOLIDS",color=RED).to_edge(UP)
        underline = Underline(title)
        self.play(Write(title))
        self.play(Create(underline))
        
        self.wait(1)

        # Description text
        description = Text(
            "Let us understand the volume of a combined solid through an example:"
        ).scale(0.6).next_to(title, DOWN, buff=0.5)
        self.play(Write(description))
        self.wait(1)

        # Example setup
        example_text = Text(
            "Suresh runs an industry in a shed which is in the shape of a cuboid\n"
            "surmounted by a half-cylinder.The base of the shed is 7m x 15m and\n"
            "the height of the cuboid portion is 8m.Find the volume of air that\n"
            "the shed can hold.Next, the total space occupied by the machinery\n"
            "is 300 m³ and there are 20 workers, each occupying about 0.08 m³\n"
            "space.Then, the volume of the air in the shed is given by.The\n"
            "length,breadth,height of the cuboid are 15m,7m,8m respectively.\n"
            "Diameter of half cylinder is 7m and its height is 15m.\n"
        ).scale(0.6).next_to(description, DOWN, buff=0.5)
        self.play(Write(example_text))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(underline), FadeOut(description), FadeOut(example_text))

        # Step by step calculations
        required_volume_text = Text("Required Volume = Volume of the cuboid + 1/2 Volume of the cylinder", font_size=30).shift(UP*3.5)
        volume_eq_text1 = MathTex("15 \\times 7 \\times 8 + \\frac{1}{2} \\times \\pi \\times \\left(\\frac{7}{2}\\right)^2 \\times 15", font_size=50).next_to(required_volume_text, DOWN)
        volume_result_text = Text("= 1128.75 m³", font_size=30).next_to(volume_eq_text1, DOWN)
        machinery_text = Text("Total space occupied by machinery = 300 m³", font_size=30).next_to(volume_result_text, DOWN)
        workers_text = MathTex(" Total space occupied by workers= 20 \\times 0.08 m^3", font_size=40).next_to(machinery_text, DOWN)
        workers_calc_text = Text("= 1.6 m³", font_size=30).next_to(workers_text, DOWN)
        total_space_text = Text("The volume of the air, inside the shed when there are machinery and workers", font_size=30).next_to(workers_calc_text, DOWN)
        calc_text1 = Text("= 1128.75 - (300.00 + 1.60)", font_size=30).next_to(total_space_text, DOWN)
        calc_text2 = Text("= 1128.75 - 301.60", font_size=30).next_to(calc_text1, DOWN)
        final_volume_text = Text("= 827.15 m³", font_size=30).next_to(calc_text2, DOWN)
        
        # Animation sequence
        self.play(Write(required_volume_text))
        self.wait(2)
        self.play(Write(volume_eq_text1))
        self.wait(2)
        self.play(Write(volume_result_text))
        self.wait(2)
        self.play(Write(machinery_text))
        self.wait(2)
        self.play(Write(workers_text))
        self.wait(2)
        self.play(Write(workers_calc_text))
        self.wait(2)
        self.play(Write(total_space_text))
        self.wait(2)
        self.play(Write(calc_text1))
        self.wait(2)
        self.play(Write(calc_text2))
        self.wait(2)
        self.play(Write(final_volume_text))
        self.wait(5)


    def SetDeveloperList(self): 
       self.DeveloperList="Potluri Divya Reddy" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade10Chapter10Mensuration.py"



if __name__ == "__main__":
    scene = Mensuration()
    scene.render()
    