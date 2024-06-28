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

class cordinateAnim(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.constructDataByCVO()
        self.fadeOutCurrentScene()
        #self.RenderNaturalNumbers()
        #self.fadeOutCurrentScene()
        #self.RenderNegativeNumbers()
        #self.fadeOutCurrentScene()
        #self.RenderRationalNumbers()
        #self.fadeOutCurrentScene()
        #self.RenderSkillbancLogo()
        #self.fadeOutCurrentScene()
        self.geo1()
        self.fadeOutCurrentScene()
        self.add_quadrants()
        self.fadeOutCurrentScene()
        self.origin00()
        self.fadeOutCurrentScene()
        self.origin()
        self.fadeOutCurrentScene()
        self.parallel()
        self.fadeOutCurrentScene()
        self.parallelogram()
        self.fadeOutCurrentScene()
   
    def constructDataByCVO(self):
        p10=cvo.CVO().CreateCVO("co-rdinate geometry","cordinates")
        p11=cvo.CVO().CreateCVO("quadrant","any two points on the number line form a quadrant")
        
        p10.cvolist.append(p11)

        self.setNumberOfCirclePositions(2)
   

    def geo1(self):

        p20=cvo.CVO().CreateCVO("co-ordinate geometry", "quadrants")
        p21=cvo.CVO().CreateCVO("quadrant 1", "positive,positive")
        p22=cvo.CVO().CreateCVO("quadrant 2", "-,+")
        p23=cvo.CVO().CreateCVO("quadrant 3", "-,-")
        p24=cvo.CVO().CreateCVO("quadrant 4", "+,-")
       
        p20.cvolist.append(p21)
        p20.cvolist.append(p22)
        p20.cvolist.append(p23)
        p20.cvolist.append(p24)

        self.setNumberOfCirclePositions(5)

        self.construct1(p20,p20)

    def add_quadrants(self):
        # Set up the axes
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"color": BLUE},
        )

        # Create vertical and horizontal lines at the origin to divide quadrants
        v_line = Line(start=axes.c2p(0, -5), end=axes.c2p(0, 5), color=WHITE)
        h_line = Line(start=axes.c2p(-5, 0), end=axes.c2p(5, 0), color=WHITE)

        # Add labels for each quadrant
        label_1 = Text("I").move_to(axes.c2p(2, 2))
        label_2 = Text("II").move_to(axes.c2p(-2, 2))
        label_3 = Text("III").move_to(axes.c2p(-2, -2))
        label_4 = Text("IV").move_to(axes.c2p(2, -2))

        # Add everything to the scene
        self.add(axes, v_line, h_line, label_1, label_2, label_3, label_4)

    def origin00(self):

        p30=cvo.CVO().CreateCVO("origin","")
        p31=cvo.CVO().CreateCVO("","intersecting point of x and y axis")
        p32=cvo.CVO().CreateCVO("example", "0,0")
        p33=cvo.CVO().CreateCVO("x cordinate", "aka abscissa")
        p34=cvo.CVO().CreateCVO("y cordinate", "aka ordinate")
       
        p30.cvolist.append(p31)
        p30.cvolist.append(p32)
        p30.cvolist.append(p33)
        p30.cvolist.append(p34)

        self.setNumberOfCirclePositions(5)

        self.construct1(p30,p30)

    def origin(self):
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"color": BLUE},
        )

        # Create vertical and horizontal lines at the origin to divide quadrants
        v_line = Line(start=axes.c2p(0, -5), end=axes.c2p(0, 5), color=WHITE)
        h_line = Line(start=axes.c2p(-5, 0), end=axes.c2p(5, 0), color=WHITE)

        # Add labels for each quadrant
        label_1 = Text("I").move_to(axes.c2p(2, 2))
        label_2 = Text("II").move_to(axes.c2p(-2, 2))
        label_3 = Text("III").move_to(axes.c2p(-2, -2))
        label_4 = Text("IV").move_to(axes.c2p(2, -2))

        # Add everything to the scene
        self.add(axes, v_line, h_line, label_1, label_2, label_3, label_4)
        # Create axes
        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 5, 1],
            axis_config={"color": BLUE},
        )
        axes.add_coordinates()
        
        # Create points
        points = [(2, 3)]
        dots = [Dot(axes.c2p(x, y), color=GREEN) for x, y in points]
        labels = [MathTex(f"({x},{y})").next_to(dot, UP) for (x, y), dot in zip(points, dots)]
        
        # Create moving origin
        origin = Dot(color=RED)
        origin_label = MathTex("(0,0)").next_to(origin, DOWN+LEFT)
        
        animations = []
        for dot, label in zip(dots, labels):
            animations.append(AnimationGroup(
                FadeIn(dot),
                Write(label),
                run_time=1
            ))
            animations.append(ApplyMethod(origin.move_to, dot.get_center(), run_time=1))
            animations.append(FadeOut(dot))
            animations.append(FadeOut(label))
        
        self.play(FadeIn(origin), Write(origin_label))

        self.wait(3)
        self.play(*animations)
        


    def parallel(self):
         
        A = [-2, -1, 0]
        B = [2, -1, 0]
        C = [3, 1, 0]
        D = [-1, 1, 0]

        parallelogram = Polygon(A, B, C, D, color=WHITE)
        label_A = Text("A").next_to(A, DOWN)
        label_B = Text("B").next_to(B, DOWN)
        label_C = Text("C").next_to(C, UP)
        label_D = Text("D").next_to(D, UP)
        diagonal = Line(A, C, color=YELLOW)
        diagonal2 = Line(D, B, color=YELLOW)
        line_BC = Line(A, B)
        D_proj = line_BC.get_projection(D)
        altitude_DP = DashedLine(D, D_proj, color=BLUE)
        label_P = Text("P").next_to(D_proj, DOWN)

        self.play(Create(parallelogram), Write(label_A), Write(label_B), Write(label_C), Write(label_D))
        self.play(Create(diagonal), Create(diagonal2), Create(altitude_DP), Write(label_P))


   

    def parallelogram(self):
       
        p10=cvo.CVO().CreateCVO("Parallelogram","")
        p11=cvo.CVO().CreateCVO("Area", "product of its base and the corresponding altitude.").setPosition([0,0,0])
        p12=cvo.CVO().CreateCVO("Example", "ABCD is parallelogram").setPosition([-4,2,0])
        p13=cvo.CVO().CreateCVO("", "AB is base and DP is altitude").setPosition([2,3,0])
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        
        A = [-2, -1, 0]
        B = [2, -1, 0]
        C = [3, 1, 0]
        D = [-1, 1, 0]

        parallelogram = Polygon(A, B, C, D, color=WHITE)
                
        label_A = Text("A").next_to(A, DOWN)
        label_B = Text("B").next_to(B, DOWN)
        label_C = Text("C").next_to(C, UP)
        label_D = Text("D").next_to(D, UP)
        diagonal = Line(A, C, color=YELLOW)
        diagonal2 = Line(D, B, color=YELLOW)
        line_BC = Line(A, B)
        D_proj = line_BC.get_projection(D)
        altitude_DP = DashedLine(D, D_proj, color=BLUE)
        label_P = Text("P").next_to(D_proj, DOWN)
        self.play(Create(parallelogram),Write(label_A), Write(label_B), Write(label_C), Write(label_D))
        self.play(Create(diagonal),Create(diagonal2),Create(altitude_DP), Write(label_P))
        
        parallelogram.shift(4 * RIGHT)
        label_A.shift(4 * RIGHT)
        label_B.shift(4 * RIGHT)
        label_C.shift(4 * RIGHT)
        label_D.shift(4 * RIGHT)
        diagonal.shift(4 * RIGHT)
        diagonal2.shift(4 * RIGHT)
        altitude_DP.shift(4 * RIGHT)
        label_P.shift(4 * RIGHT)
        
        self.setNumberOfCirclePositions(4)
        self.construct1(p10,p10)

if __name__ == "__main__":
         scene = cordinateAnim()
         scene.render()
        
