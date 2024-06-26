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

class Surfaceareasandvolumes(AbstractAnim,ThreeDScene):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.Cuboid()
        self.fadeOutCurrentScene()
        self.Cuboidanim()
        self.fadeOutCurrentScene()
        self.Example1()
        self.fadeOutCurrentScene()
        self.Ex1Anim()
        self.fadeOutCurrentScene()


        self.Cylinder()
        self.fadeOutCurrentScene()
        self.Cylinderanim()
        self.fadeOutCurrentScene()
        self.Example2()
        self.fadeOutCurrentScene()
        self.ExAnim2()
        self.fadeOutCurrentScene()


        self.Cone()
        self.fadeOutCurrentScene()
        self.Coneanim()
        self.fadeOutCurrentScene()
        self.Example3()
        self.fadeOutCurrentScene()
        self.ExAnim3()
        self.fadeOutCurrentScene()


        self.Sphere()
        self.fadeOutCurrentScene()
        self.Sphereanim()
        self.fadeOutCurrentScene()
        self.Example4()
        self.fadeOutCurrentScene()
        self.ExAnim4()
        self.fadeOutCurrentScene()


        self.Hemisphere()
        self.fadeOutCurrentScene()
        self.Hemisphereanim()
        self.fadeOutCurrentScene()
        self.Example5()
        self.fadeOutCurrentScene()
        self.ExAnim5()
        self.fadeOutCurrentScene()

        self.GithubSourceCodeReference()
       
        
     # render using CVO data object  
    def Cuboid(self):
        self.positionChoice = [[-4,0,0],[0,2,0],[2,-2,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Cuboid","")
        p11=cvo.CVO().CreateCVO("Surface Area","2(lb+bh+lh)")
        p12=cvo.CVO().CreateCVO("Lateral Surface Area","2h(l+b)")
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

        self.play(Write(title))
        self.play(Create(underline))
        self.wait()

        # Cuboid Animation (Scaled down and positioned to the left)
        scale_factor = 0.7  # Adjust as needed
        a = ((-1*scale_factor, -2.25*scale_factor, 0), (-7*scale_factor, -2.25*scale_factor, 0),
             (-8*scale_factor, -2.75*scale_factor, 0), (-2*scale_factor, -2.75*scale_factor, 0), (-1*scale_factor, -2.25*scale_factor, 0))
        base = Polygon(*a, stroke_width=3, color=WHITE)

        b = ((-1*scale_factor, 0.75*scale_factor, 0), (-7*scale_factor, 0.75*scale_factor, 0),
             (-8*scale_factor, 0.25*scale_factor, 0), (-2*scale_factor, 0.25*scale_factor, 0), (-1*scale_factor, 0.75*scale_factor, 0))
        top = Polygon(*b, stroke_width=3, color=WHITE)

        c = ((-0.9*scale_factor, 0.75*scale_factor, 0), (-0.9*scale_factor, -2.25*scale_factor, 0),
             (-2*scale_factor, -2.75*scale_factor, 0), (-2*scale_factor, 0.25*scale_factor, 0), (-1*scale_factor, 0.75*scale_factor, 0))
        face1 = Polygon(*c, stroke_width=3, color=WHITE)

        d = ((-1*scale_factor, 0.75*scale_factor, 0), (-7*scale_factor, 0.75*scale_factor, 0),
             (-7*scale_factor, -2.25*scale_factor, 0), (-0.9*scale_factor, -2.25*scale_factor, 0), (-0.9*scale_factor, 0.75*scale_factor, 0))
        face2 = Polygon(*d, stroke_width=3, color=WHITE)

        e = ((-7*scale_factor, 0.75*scale_factor, 0), (-7*scale_factor, -2.25*scale_factor, 0),
             (-8*scale_factor, -2.75*scale_factor, 0), (-8*scale_factor, 0.25*scale_factor, 0), (-7*scale_factor, 0.75*scale_factor, 0))
        face3 = Polygon(*e, stroke_width=3, color=WHITE)

        f = ((-2*scale_factor, 0.25*scale_factor, 0), (-2*scale_factor, -2.75*scale_factor, 0),
             (-8*scale_factor, -2.75*scale_factor, 0), (-8*scale_factor, 0.25*scale_factor, 0), (-2*scale_factor, 0.25*scale_factor, 0))
        face4 = Polygon(*f, stroke_width=3, color=WHITE)

        # Labels for dimensions
        l_label = Text("l", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        l_label.next_to(base.get_edge_center(DOWN), DOWN)
        b_label = Text("b", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        b_label.next_to(base.get_edge_center(RIGHT), DOWN)
        h_label = Text("h", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        h_label.next_to(top.get_edge_center(RIGHT), RIGHT)

        cuboid_group = VGroup(base, top, face1, face2, face3, face4, l_label, b_label, h_label)
        cuboid_group.move_to([-2, 0, 0])

        self.play(Create(cuboid_group))
        self.wait()


        # LSA of Cuboid (Blue color)
        lsa_text = Text("LSA = 2h(l+b)", color="#ffb3b3", weight=BOLD,font_size=30)
        lsa_text.next_to(cuboid_group, RIGHT*2, buff=1)
        self.play(Write(lsa_text))
        face1.set_fill("#ffb3b3", opacity=0.5)
        self.wait(1)
        face2.set_fill("#ffb3b3", opacity=0.5)
        self.wait(1)
        face3.set_fill("#ffb3b3", opacity=0.5)
        self.wait(1)
        face4.set_fill("#ffb3b3", opacity=0.5)
        self.wait(1)
        


        # Formulas beside the cuboid
        # TSA of Cuboid (Yellow color)
        tsa_text = Text("Surface area = 2(lb+bh+hl)", color="#80ff80", weight=BOLD,font_size=30)
        tsa_text.next_to(lsa_text, DOWN)
        self.play(Write(tsa_text))
        face1.set_fill("#80ff80", opacity=0.5)
        self.wait(1)
        face2.set_fill("#80ff80", opacity=0.5)
        self.wait(1)
        face3.set_fill("#80ff80", opacity=0.5)
        self.wait(1)
        face4.set_fill("#80ff80", opacity=0.5)
        self.wait(1)
        top.set_fill("#80ff80", opacity=0.5)
        self.wait(1)
        base.set_fill("#80ff80", opacity=0.5)
        self.wait(1)
        

        # Volume of Cuboid (Red color)
        volume_text = Text("Volume = lbh", color="#99ffff", weight=BOLD,font_size=30)
        volume_text.next_to(tsa_text, DOWN)
        self.play(Write(volume_text))
        face1.set_fill("#99ffff", opacity=0.5)
        face2.set_fill("#99ffff", opacity=0.5)
        face3.set_fill("#99ffff", opacity=0.5)
        face4.set_fill("#99ffff", opacity=0.5)
        base.set_fill("#99ffff", opacity=0.5)
        top.set_fill("#99ffff", opacity=0.5)
        self.wait(3)


    def Example1(self):
        self.positionChoice = [[-4,0,0],[0,2,0],[2,-2,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Cuboid","l=4cm,b=3cm,h=5cm")
        p11=cvo.CVO().CreateCVO("Surface Area","$2(4*3+3*5+4*5)=94cm^2$")
        p12=cvo.CVO().CreateCVO("Lateral Surface Area","$2*5(4+3)=70cm^2$")
        p13=cvo.CVO().CreateCVO("Volume","$4*3*5=60cm^3$").setPosition([0,2,0])
        p10.setcircleradius(1.10)
        p11.setcircleradius(1.10)
        p12.setcircleradius(1.10)
        p13.setcircleradius(1.10)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.setNumberOfCirclePositions(4)
        self.construct1(p10,p10)
    

    def Ex1Anim(self):
        title = Text("Cuboid",color=RED, weight=BOLD).to_edge(UP)
        underline = Underline(title)
        self.play(Write(title))
        self.play(Create(underline))

        # Dimensions of the cuboid
        length = 4  # cm
        breadth = 3  # cm
        height = 5  # cm
        dimensions_text = Text(f"For Example,l={length} cm, b={breadth} cm, h={height} cm").next_to(title, DOWN, buff=1)
        dimensions_text.set_height(0.5)  # Set font size
        self.play(Write(dimensions_text))
        self.wait(1)

        # Calculate surface area, lateral surface area, and volume
        surface_area = 2 * (length * breadth + breadth * height + height * length)
        lateral_surface_area = 2 * height * (length + breadth)
        volume = length * breadth * height

        # Create LaTeX texts for surface area, lateral surface area, and volume with substituted values
        surface_area_text1 = MathTex(
            "\\text{Surface Area} = 2(lb + bh + hl)"
        ).next_to(dimensions_text, DOWN)
        
        surface_area_text2 = MathTex(
            f"2({length} \\times {breadth} + {breadth} \\times {height} + {height} \\times {length}) = {surface_area}\\ \\text{{cm}}^2"
        ).next_to(surface_area_text1, DOWN)

        lateral_surface_area_text1 = MathTex(
            "\\text{Lateral Surface Area} = 2h(l + b)"
        ).next_to(surface_area_text2, DOWN)

        lateral_surface_area_text2 = MathTex(
            f" 2 \\times {height}({length} + {breadth}) = {lateral_surface_area}\\ \\text{{cm}}^2"
        ).next_to(lateral_surface_area_text1, DOWN)

        volume_text1 = MathTex(
            "\\text{Volume} = l \\times b \\times h"
        ).next_to(lateral_surface_area_text2, DOWN)

        volume_text2 = MathTex(
            f" {length} \\times {breadth} \\times {height} = {volume}\\ \\text{{cm}}^3"
        ).next_to(volume_text1, DOWN)

        # Animate the texts
        self.play(Write(surface_area_text1))
        self.wait(1)
        self.play(Write(surface_area_text2))
        self.wait(1)
        self.play(Write(lateral_surface_area_text1))
        self.wait(1)
        self.play(Write(lateral_surface_area_text2))
        self.wait(1)
        self.play(Write(volume_text1))
        self.wait(1)
        self.play(Write(volume_text2))
        self.wait(2)

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
        t1 = Text("Cylinder", color=RED, weight=BOLD)
        t1.move_to([0, 2.7, 0])
        underline = Underline(t1)

        # Create base and top ellipses
        base = Ellipse(width=2, height=0.5, color=WHITE, fill_opacity=1, fill_color=BLACK)
        top = Ellipse(width=2, height=0.5, color=WHITE, fill_opacity=1, fill_color=BLACK)

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
        r_label = Text("r", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        r_label.next_to(base.get_edge_center(DOWN), DOWN)
        h_label = Text("h", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        h_label.next_to(base.get_edge_center(RIGHT) + RIGHT * 0.5, UP * 4.5)

        # Play animations
        self.play(Write(t1))
        self.play(Create(underline))
        self.wait(1)
        self.play(Write(base), Write(top))
        self.play(Write(line1), Write(line2))
        self.play(Write(r_label), Write(h_label))
        self.wait(1)

        # Surface Area annotations
        # Lateral Surface Area (LSA)
        lsa_text = Text("LSA = 2πrh", color="#ffb3b3", weight=BOLD, font_size=30)
        lsa_text.next_to(h_label, RIGHT, buff=1)
        self.play(Write(lsa_text))

        # Create polygon to fill LSA area between line1 and line2
        lsa_area = Polygon(line1.get_start(), line1.get_end(), line2.get_end(), line2.get_start())
        lsa_area.set_fill(color="#ffb3b3", opacity=0.5)
        lsa_area.set_stroke(color=WHITE, width=0)  # Ensure no border around the polygon
        b11 = Ellipse(width=2, height=0.5, color=WHITE, fill_opacity=1, fill_color=BLACK)
        t11 = Ellipse(width=2, height=0.5, color=WHITE, fill_opacity=1, fill_color=BLACK)
        b11.move_to([0, -1.5, 0])
        t11.move_to([0, 1.5, 0])
        self.play(Create(lsa_area))
        self.play(Write(b11), Write(t11))
        self.wait(1)

        # Total Surface Area (TSA)
        tsa_text = Text("TSA = 2πr(r + h)", color="#80ff80", weight=BOLD, font_size=30)
        tsa_text.next_to(lsa_text, DOWN)
        self.play(Write(tsa_text))

        # Fade out previous fills and set new color for TSA
        # Fade out previous fills and set new color for TSA
        self.play(lsa_area.animate.set_fill(color="#80ff80", opacity=1))
        self.wait(1)
        self.play(b11.animate.set_fill(color="#80ff80", opacity=1))
        self.wait(1)
        self.play(t11.animate.set_fill(color="#80ff80", opacity=1))
        self.wait(1)

        # Volume annotation
        volume_text = Text("Volume = πr²h", color="#99ffff", weight=BOLD, font_size=30)
        volume_text.next_to(tsa_text, DOWN)
        self.play(Write(volume_text))

        # Fade out previous fills and set new color for volume
        self.play(
            AnimationGroup(
                lsa_area.animate.set_fill(color="#99ffff", opacity=1),
                b11.animate.set_fill(color="#99ffff", opacity=1),
                t11.animate.set_fill(color="#99ffff", opacity=1),
                lag_ratio=0
            )
        )
        self.wait()
    
    def Example2(self):
        self.positionChoice = [[-4,0,0],[0,2,0],[2,-2,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Cylinder","r=5cm,h=8cm")
        p11=cvo.CVO().CreateCVO("Lateral surface Area","$2*3.14*5*8=251.2cm^2$")
        p12=cvo.CVO().CreateCVO("Total Surface Area","$2*3.14*5(5+8)=408.2cm^2$")
        p13=cvo.CVO().CreateCVO("Volume","$3.14*5*5*8=628cm^3$").setPosition([0,2,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.setcircleradius(1.10)
        p11.setcircleradius(1.10)
        p12.setcircleradius(1.10)
        p13.setcircleradius(1.10)
        self.setNumberOfCirclePositions(4)
        self.construct1(p10,p10)

    def ExAnim2(self):
        # Create a title
        # Create a title
        title = Text("Cylinder",color=RED, weight=BOLD).to_edge(UP)
        underline = Underline(title)
        self.play(Write(title))
        self.play(Create(underline))

        

        # Dimensions of the cylinder
        radius = 5  # cm
        height = 8  # cm

        # Dimensions text below the title with smaller font size
        dimensions_text = Text(f"For Example,r={radius} cm, h={height} cm").next_to(title, DOWN, buff=1)
        dimensions_text.set_height(0.5)  # Set font size
        self.play(Write(dimensions_text))
        self.wait(1)

        # Calculate the lateral surface area, total surface area, and volume using pi = 3.14
        pi = 3.14
        lateral_surface_area = 2 * pi * radius * height
        total_surface_area = 2 * pi * radius * (height + radius)
        volume = pi * radius ** 2 * height

        # Create LaTeX texts for lateral surface area, total surface area, and volume
        lateral_surface_area_formula = MathTex(
            "\\text{Lateral Surface Area} = 2\\pi rh"
        ).next_to(dimensions_text, DOWN)

        lateral_surface_area_calc = MathTex(
            f" 2 \\times 3.14 \\times {radius} \\times {height} = {lateral_surface_area:.1f}\\ \\text{{cm}}^2"
        ).next_to(lateral_surface_area_formula, DOWN)

        total_surface_area_formula = MathTex(
            "\\text{Total Surface Area} = 2\\pi r(h + r)"
        ).next_to(lateral_surface_area_calc, DOWN)

        total_surface_area_calc = MathTex(
            f"  2 \\times 3.14 \\times {radius} \\times ({height} + {radius}) = {total_surface_area:.1f}\\ \\text{{cm}}^2"
        ).next_to(total_surface_area_formula, DOWN)

        volume_formula = MathTex(
            "\\text{Volume} = \\pi r^2 h"
        ).next_to(total_surface_area_calc, DOWN)

        volume_calc = MathTex(
            f"  3.14 \\times {radius}^2 \\times {height} = {volume:.1f}\\ \\text{{cm}}^3"
        ).next_to(volume_formula, DOWN)

        # Animate the texts
        self.play(Write(lateral_surface_area_formula))
        self.wait(1)
        self.play(Write(lateral_surface_area_calc))
        self.wait(1)
        self.play(Write(total_surface_area_formula))
        self.wait(1)
        self.play(Write(total_surface_area_calc))
        self.wait(1)
        self.play(Write(volume_formula))
        self.wait(1)
        self.play(Write(volume_calc))
        self.wait(2)

   
    def Cone(self):
        self.positionChoice = [[-4,0,0],[-2,2,0],[2,-2,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Cone","")
        p11=cvo.CVO().CreateCVO("Slant Height","$l=\sqrt (h^2 + r^2)$")
        p12=cvo.CVO().CreateCVO("Lateral Surface Area","$\pi rl$").setPosition([-4,2,0])
        p13=cvo.CVO().CreateCVO("Total Surface Area","$\pi r(r+l)$").setPosition([-0.5,2,0])
        p14=cvo.CVO().CreateCVO("Volume","$1/3 \pi r^2h$").setPosition([2,2,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.setcircleradius(1.6)
        p11.setcircleradius(1.6)
        p12.setcircleradius(1.6)
        p13.setcircleradius(1.6)
        p14.setcircleradius(1.6)
        self.setNumberOfCirclePositions(5)
        self.construct1(p10,p10)


    def Coneanim(self):
        # Title
        title = Text("Cone", color=RED, weight=BOLD)
        title.move_to([0, 3, 0])
        underline = Underline(title)
        self.play(Write(title))
        self.play(Create(underline))
        self.wait()

        # Create the cone
        # self.play(Write(NumberPlane()))
        cone = Polygon(
            [0, 2, 0],  # Top point of the cone
            [-2, -1, 0],  # Bottom left point
            [2, -1, 0],  # Bottom right point
            color=WHITE,
            
        )
        cone.shift([-4, 0, 0])  # Shifted towards the left
        self.play(Create(cone))

        # Create the horizontal ellipse (base)
        base = Ellipse(width=4, height=0.4, color=WHITE)
        base.move_to(cone.get_center() + DOWN * 1.5)  # Positioned below the cone
        self.play(Create(base))

        # Create the vertical line representing the height
        height_line = Line(start=[-4, 2, 0], end=[-4, -1, 0], color=WHITE)  # Shifted towards the left
        self.play(Create(height_line))

        
        # Create the small filled circle at the center of the base
        center_dot = Dot(point=[-4, -1, 0], color=WHITE)  # Shifted towards the left
        self.play(Create(center_dot))

        # Create the labels "h", "l", and "r"
        height_label = Text("h", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        height_label.move_to([-4.2, 0.5, 0])  # Adjusted position
        self.play(Write(height_label))

        slant_label = Text("l", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        slant_label.move_to([-3, 1, 0])  # Shifted towards the left
        self.play(Write(slant_label))

        radius_label = Text("r", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        radius_label.move_to([-3, -1.7, 0])  # Shifted towards the left
        self.play(Write(radius_label))

        # Slant height formula
        slant_height_formula = MathTex("\\textbf{Slant height (l)} = \\sqrt{r^2 + h^2}", color="#a3a3c2")
        slant_height_formula.next_to(slant_label, RIGHT * 8)
        self.play(Write(slant_height_formula))
        cone1 = Polygon(
            [-4, 2, 0],  # Top point of the cone
            [-2, -1, 0],  # Bottom left point
            [-4, -1, 0],  # Bottom right point
            color=WHITE,
            
        )
        
        self.play(Create(cone1))
        cone1.set_fill("#a3a3c2", opacity=0.5)
        base1 = Ellipse(width=4, height=0.4, color=WHITE,fill_opacity=1, fill_color=BLACK)
        base1.move_to(cone.get_center() + DOWN * 1.5)  # Positioned below the cone
        self.play(Create(base1))

        # Create the vertical line representing the height
        height_line1 = Line(start=[-4, 2, 0], end=[-4, -1, 0], color=WHITE)  # Shifted towards the left
        self.play(Create(height_line1))

        # Create the small filled circle at the center of the base
        center_dot1 = Dot(point=[-4, -1, 0], color=WHITE)  # Shifted towards the left
        self.play(Create(center_dot1))
        self.wait()
        L1=Line(start=[-6,-1,0],end=[-2,-1,0])
        self.play(Write(L1))
        self.wait()
        self.play(Uncreate(cone1))

        # Highlight LSA
        lsa_formula = MathTex("\\textbf{LSA} = \\pi r l", color="#ffb3b3")
        lsa_formula.next_to(slant_height_formula, DOWN)
        self.play(Write(lsa_formula))
        cone.set_fill("#ffb3b3", opacity=0.5)
        
        base1 = Ellipse(width=4, height=0.4, color=WHITE,fill_opacity=1, fill_color=BLACK)
        base1.move_to(cone.get_center() + DOWN * 1.5)  # Positioned below the cone
        self.play(Create(base1))

        # Create the vertical line representing the height
        height_line1 = Line(start=[-4, 2, 0], end=[-4, -1, 0], color=WHITE)  # Shifted towards the left
        self.play(Create(height_line1))

        # Create the small filled circle at the center of the base
        center_dot1 = Dot(point=[-4, -1, 0], color=WHITE)  # Shifted towards the left
        self.play(Create(center_dot1))
        self.wait()
        L1=Line(start=[-6,-1,0],end=[-2,-1,0])
        self.play(Write(L1))
        self.wait()

        # Highlight TSA
        tsa_formula = MathTex("\\textbf{TSA} = \\pi r (l + r)", color="#80ff80")
        tsa_formula.next_to(lsa_formula, DOWN)
        self.play(Write(tsa_formula))
        cone.set_fill("#80ff80", opacity=1)
        self.wait(1)
        base1.set_fill("#80ff80", opacity=1)
        self.wait(1)
        
        # Highlight Volume
        volume_formula = MathTex("\\textbf{Volume} = \\frac{1}{3} \\pi r^2 h", color="#99ffff")
        volume_formula.next_to(tsa_formula, DOWN)
        self.play(Write(volume_formula))
        cone.set_fill("#99ffff", opacity=1)
        base1.set_fill("#99ffff", opacity=1)
        self.wait(3)

    def Example3(self):
        self.positionChoice = [[-4,0,0],[-2,2,0],[2,-2,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Cone","r=6cm,h=10cm")
        p11=cvo.CVO().CreateCVO("Slant Height","$l=\sqrt (10^2+16^2)=11.66cm$")
        p12=cvo.CVO().CreateCVO("Lateral Surface Area","$3.14*6*11.66=219.71cm^2$").setPosition([-4,2,0])
        p13=cvo.CVO().CreateCVO("Total Surface Area","$3.14*6*(6+11.66)=332.75cm^2$").setPosition([-0.7,2,0])
        p14=cvo.CVO().CreateCVO("Volume","$1/3*3.14*6*6*10=376.80cm^3$").setPosition([2.2,2.3,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.setcircleradius(1.10)
        p11.setcircleradius(1.10)
        p12.setcircleradius(1.10)
        p13.setcircleradius(1.10)
        p14.setcircleradius(1.10)
        self.setNumberOfCirclePositions(5)
        self.construct1(p10,p10)

        
    def ExAnim3(self):
        title = Text("Cone",color=RED, weight=BOLD).to_edge(UP)
        underline = Underline(title)
        self.play(Write(title))
        self.play(Create(underline))

        # Dimensions of the cone
        base_radius = 6  # cm
        height = 10  # cm  # changed height to 10 cm
        slant_height = (height**2 + base_radius**2)**0.5

        # Display dimensions
        dimensions_text = Text(f"For Example,r={base_radius} cm, h={height} cm").next_to(title, DOWN, buff=0.5)
        dimensions_text.set_height(0.5)  # Set font size
        self.play(Write(dimensions_text))
        self.wait(1)

        # Calculate properties using π = 3.14
        pi_value = 3.14
        lateral_surface_area = pi_value * base_radius * slant_height
        total_surface_area = lateral_surface_area + pi_value * base_radius**2
        volume = (1/3) * pi_value * base_radius**2 * height

        # Create LaTeX texts for properties including slant height
        slant_height_formula  = MathTex(r"\text{Slant Height} &= \sqrt{h^2 + r^2} \\",
            f"&= \\sqrt{{{height}^2 + {base_radius}^2}}",f"&= {slant_height:.2f}\\ \\text{{cm}}").next_to(dimensions_text, DOWN)

        lateral_surface_area_text = MathTex(
            f"\\text{{Lateral Surface Area}} = \\pi r l \\",
            f"& = {pi_value} \\times {base_radius} \\times {slant_height:.2f}\\, = {lateral_surface_area:.2f}\\ \\text{{cm}}^2"
        ).next_to(slant_height_formula, DOWN)

        total_surface_area_text = MathTex(
            f"\\text{{Total Surface Area}} = \\pi r l + \\pi r^2 \\,",
            f"& = {lateral_surface_area:.2f} + {pi_value} \\times {base_radius}^2 \\, = {total_surface_area:.2f}\\ \\text{{cm}}^2"
        ).next_to(lateral_surface_area_text, DOWN)

        volume_text = MathTex(
            f"\\text{{Volume}} = \\frac{{1}}{{3}} \\pi r^2 h \\",
            f"& = \\frac{{1}}{{3}} \\times {pi_value} \\times {base_radius}^2 \\times {height} = {volume:.2f}\\ \\text{{cm}}^3"
        ).next_to(total_surface_area_text, DOWN)

        # Animate the texts
        self.play(Write(slant_height_formula))
        self.wait(1)
        self.play(Write(lateral_surface_area_text))
        self.wait(1)
        self.play(Write(total_surface_area_text))
        self.wait(1)
        self.play(Write(volume_text))
        self.wait(2)
        

    def Sphere(self):
        self.positionChoice = [[-4,0,0],[2,2,0],[2,-2,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Sphere","")
        p11=cvo.CVO().CreateCVO("Surface Area","$4\pi r^2$")
        p12=cvo.CVO().CreateCVO("Volume","$4/3 \pi r^3$")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.setcircleradius(1.6)
        p11.setcircleradius(1.6)
        p12.setcircleradius(1.6)
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)

    def Sphereanim(self):
        # Title and underline
        title = Text("Sphere", color=RED, weight=BOLD)
        title.move_to([0, 3, 0])
        underline = Underline(title)
        
        # Create the circle representing the sphere
        sphere = Circle(radius=2, color=WHITE)
        
        # Create the horizontal ellipse (equator)
        equator = Ellipse(width=4, height=0.4, color=WHITE)
        
        # Create the dashed line representing the radius
        radius_line_horizontal = DashedLine(start=[0, 0, 0], end=[2, 0, 0], color=WHITE)
        
        # Create the small filled circle at the center of the horizontal ellipse
        center_dot = Dot(point=[0, 0, 0], color=WHITE)
        
        # Create the label "r"
        radius_label_horizontal = Text("r", font="Comic Sans MS", color=WHITE,weight=BOLD).scale(0.5)
        radius_label_horizontal.next_to(radius_line_horizontal, DOWN*0.9)
        
        # Position elements
        sphere.shift(LEFT*3)  
        equator.shift(LEFT*3)  
        radius_line_horizontal.shift(LEFT*3)  
        center_dot.shift(LEFT*3)  
        radius_label_horizontal.shift(LEFT*3)  
        
        # Surface area formula
        surface_area_formula = MathTex(r"4\pi r^2", color="#80FF80").move_to(RIGHT*3 + UP*1)
        
        # Volume formula
        volume_formula = MathTex(r"\frac{4}{3}\pi r^3", color="#99FFFF").move_to(RIGHT*3 + DOWN*1)
        
        # Play animations for sphere
        self.play(Create(title))
        self.play(Create(underline))
        self.play(Create(sphere))
        self.play(Create(equator))
        self.play(Create(radius_line_horizontal))
        self.play(Create(center_dot))
        self.play(Write(radius_label_horizontal))
        
        # Highlight Surface Area Formula
        surface_area_highlight = MathTex(r"\textbf{Surface Area} = 4\pi r^2", color="#80FF80")
        surface_area_highlight.next_to(volume_formula, UP*3)
        self.play(Write(surface_area_highlight))
        sphere.set_fill("#80FF80", opacity=0.5)
        self.wait(1)
        
        # Highlight Volume Formula
        volume_highlight = MathTex(r"\textbf{Volume} = \frac{4}{3}\pi r^3", color="#99FFFF")
        volume_highlight.next_to(surface_area_highlight, DOWN)
        self.play(Write(volume_highlight))
        sphere.set_fill("#99FFFF", opacity=0.5)
        self.wait(3)
        
    def Example4(self):
        self.positionChoice = [[-4,0,0],[2,2,0],[2,-2,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Sphere","r=3cm")
        p11=cvo.CVO().CreateCVO("Surface Area","$4*3.14*3*3=113.09cm^2$")
        p12=cvo.CVO().CreateCVO("Volume","$4/3*3.14*3*3*3=113.09cm^3$")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.setcircleradius(1.10)
        p11.setcircleradius(1.10)
        p12.setcircleradius(1.10)
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)


    def ExAnim4(self):
        title = Text("Sphere",color=RED, weight=BOLD).to_edge(UP)
        underline = Underline(title)
        self.play(Write(title))
        self.play(Create(underline))

        # Dimensions of the sphere
        radius = 3  # cm

        # Display dimensions
        dimensions_text = Text(f"For Example,r={radius} cm").next_to(title, DOWN, buff=1)
        dimensions_text.set_height(0.5)  # Set font size
        self.play(Write(dimensions_text))
        self.wait(1)

        # Calculate properties
        PI = 3.14  # Assuming PI value for calculation
        surface_area = 4 * PI * radius ** 2
        volume = (4/3) * PI * radius ** 3

        # Format results to two decimal places
        surface_area_formatted = f"{surface_area:.2f}"
        volume_formatted = f"{volume:.2f}"

        # Create LaTeX texts for properties
        surface_area_text1 = MathTex(f"\\text{{Surface Area}} = 4 \pi r^2").next_to(dimensions_text, DOWN)
        surface_area_text2 = MathTex(
            f" 4 \\times {PI} \\times {radius}^2 = {surface_area_formatted}\\ \\text{{cm}}^2"
        ).next_to(surface_area_text1, DOWN)
        volume_text1 = MathTex(f"\\text{{Volume}} = \\frac{{4}}{{3}} \pi r^3").next_to(surface_area_text2, DOWN)
        volume_text2 = MathTex(
            f" \\frac{{4}}{{3}} \\times {PI} \\times {radius}^3 = {volume_formatted}\\ \\text{{cm}}^3"
        ).next_to(volume_text1, DOWN)

        # Animate the texts
        self.play(Write(surface_area_text1))
        self.play(Write(surface_area_text2))
        self.wait(1)
        self.play(Write(volume_text1))
        self.play(Write(volume_text2))
        self.wait(2)

    def Hemisphere(self):
        self.positionChoice = [[-4,-2,0],[0,2,0],[2,-2,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Hemisphere","")
        p11=cvo.CVO().CreateCVO("Surface Area","$2\pi r^2$")
        p12=cvo.CVO().CreateCVO("Total Surface Area","$3\pi r^2$")
        p13=cvo.CVO().CreateCVO("Volume","$2/3\pi r^3$").setPosition([-4,2,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.setcircleradius(1.6)
        p11.setcircleradius(1.6)
        p12.setcircleradius(1.6)
        p13.setcircleradius(1.6)
        self.construct1(p10,p10)

    def Hemisphereanim(self):
        # Title and underline
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
        radius_label_horizontal = Text("r", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        radius_label_horizontal.next_to(radius_line_horizontal, UP)
        radius_label_vertical = Text("r", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        radius_label_vertical.next_to(radius_line_vertical, LEFT)
        
        # Position elements
        hemisphere.shift(LEFT*3 + DOWN*1)
        equator.shift(LEFT*3)
        radius_line_horizontal.shift(LEFT*3 + DOWN*1)
        radius_line_vertical.shift(LEFT*3 + DOWN*1)
        center_dot.shift(LEFT*3 + DOWN*1)
        radius_label_horizontal.shift(LEFT*3 + DOWN*0.7)
        radius_label_vertical.shift(LEFT*3 + DOWN*1)
        
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
        
        # Highlight LSA
        lsa_formula = MathTex("\\textbf{LSA} = 2\\pi r^2", color="#ffb3b3")
        lsa_formula.next_to(title, DOWN*7 + RIGHT*1)
        self.play(Write(lsa_formula))
        hemisphere.set_fill("#ffb3b3", opacity=0.5)
        self.wait(1)
        equator1 = Ellipse(width=4, height=0.75, color=WHITE,fill_opacity=1, fill_color=BLACK).shift(DOWN*1)
        equator1.shift(LEFT*3)
        radius_line_horizontal1 = DashedLine(start=[0, 0, 0], end=[2, 0, 0], color=WHITE)
        radius_line_vertical1 = DashedLine(start=[0, 0, 0], end=[0, -2, 0], color=WHITE)
        radius_line_horizontal1.shift(LEFT*3 + DOWN*1)
        radius_line_vertical1.shift(LEFT*3 + DOWN*1)
        center_dot1 = Dot(point=[0, 0, 0], color=WHITE)
        center_dot1.shift(LEFT*3 + DOWN*1)
        
        self.play(Create(equator1),Create(radius_line_horizontal1),Create(radius_line_vertical1),Create(center_dot1))
        self.wait(2)
        # Highlight TSA
        tsa_formula = MathTex("\\textbf{TSA} = 3\\pi r^2", color="#80ff80")
        tsa_formula.next_to(lsa_formula, DOWN)
        self.play(Write(tsa_formula))
        hemisphere.set_fill("#80ff80", opacity=1)
        self.wait(1)
        equator1.set_fill("#80ff80", opacity=1)
        self.wait(1)
        
        # Highlight Volume
        volume_formula = MathTex("\\textbf{Volume} = \\frac{2}{3} \\pi r^3", color="#99ffff")
        volume_formula.next_to(tsa_formula, DOWN)
        self.play(Write(volume_formula))
        hemisphere.set_fill("#99ffff", opacity=1)
        equator1.set_fill("#99ffff", opacity=1)
        self.wait(3)

        # Final animation
        self.wait(2)
        
    def Example5(self):
        self.positionChoice = [[-4,-2,0],[0,2,0],[2,-2,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Hemisphere","r=4")
        p11=cvo.CVO().CreateCVO("Surface Area","$2*3.14*4*4=100.48cm^2$")
        p12=cvo.CVO().CreateCVO("Total Surface Area","$3*3.14*4*4*4=150.72cm^2$")
        p13=cvo.CVO().CreateCVO("Volume","$2/3*3.14*4*4*4=133.97cm^3$").setPosition([-4,2,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.setcircleradius(1.10)
        p11.setcircleradius(1.10)
        p12.setcircleradius(1.10)
        p13.setcircleradius(1.10)
        self.construct1(p10,p10)


    def ExAnim5(self):
         # Create a title
        # Create a title
        title = Text("Hemisphere",color=RED, weight=BOLD).to_edge(UP)
        underline = Underline(title)
        self.play(Write(title))
        self.play(Create(underline))

        # Dimensions of the hemisphere
        radius = 4  # cm

        # Display dimensions
        dimensions_text = Text(f"For Example,r={radius} cm").next_to(title, DOWN, buff=0.8)
        dimensions_text.set_height(0.5)  # Set font size
        self.play(Write(dimensions_text))
        self.wait(1)

        # Calculate properties
        PI = 3.14  # Assuming PI value for calculation
        surface_area = 2 * PI * radius ** 2
        total_surface_area = 3 * PI * radius ** 2
        volume = (2/3) * PI * radius ** 3

        # Create LaTeX texts for properties
        surface_area_text1 = MathTex(f"\\text{{Surface Area}} = 2 \pi r^2").next_to(dimensions_text, DOWN)
        surface_area_text2 = MathTex(
            f"2 \\times {PI} \\times {radius}^2 = {surface_area}\\ \\text{{cm}}^2"
        ).next_to(surface_area_text1, DOWN)
        total_surface_area_text = MathTex(f"\\text{{Total Surface Area}} = 3 \pi r^2").next_to(surface_area_text2, DOWN)
        total_surface_area_text2 = MathTex(
            f"3 \\times {PI} \\times {radius}^2 = {total_surface_area}\\ \\text{{cm}}^2"
        ).next_to(total_surface_area_text, DOWN)
        volume_text1 = MathTex(f"\\text{{Volume}} = \\frac{{2}}{{3}} \pi r^3").next_to(total_surface_area_text2, DOWN)
        volume_text2 = MathTex(
            f"\\frac{{2}}{{3}} \\times {PI} \\times {radius}^3 = 133.97\\ \\text{{cm}}^3"
        ).next_to(volume_text1, DOWN)

        # Animate the texts
        self.play(Write(surface_area_text1))
        self.play(Write(surface_area_text2))
        self.wait(1)
        self.play(Write(total_surface_area_text))
        self.play(Write(total_surface_area_text2))
        self.wait(1)
        self.play(Write(volume_text1))
        self.play(Write(volume_text2))
        self.wait(2)

    def SetDeveloperList(self): 
       self.DeveloperList="Potluri Divya Reddy" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="SurfaceAreasAndVolumes.py"



    
if __name__ == "__main__":
    scene = Surfaceareasandvolumes()
    scene.render()
    