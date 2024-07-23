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

class Chap8G10_SimilarTriangles(AbstractAnim):
    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.SimTria()
        self.fadeOutCurrentScene()
        self.Anim1()
        self.fadeOutCurrentScene()
        self.bpt()
        self.fadeOutCurrentScene()
        self.T1()
        self.fadeOutCurrentScene()
        self.Anim2()
        self.fadeOutCurrentScene()
        self.cri1()
        self.fadeOutCurrentScene()
        self.Anim3()
        self.fadeOutCurrentScene()
        self.cri2()
        self.fadeOutCurrentScene()
        self.Anim4()
        self.fadeOutCurrentScene()
        self.cri3()
        self.fadeOutCurrentScene()
        self.Anim5()
        self.fadeOutCurrentScene()
        self.constructTri()
        self.fadeOutCurrentScene()
        self.Area()
        self.fadeOutCurrentScene()
        self.Anim6()
        self.fadeOutCurrentScene()
        self.pyth()
        self.fadeOutCurrentScene()
        self.Anim7()
        self.fadeOutCurrentScene()
        self.st()
        self.fadeOutCurrentScene()
        self.st1()
        self.fadeOutCurrentScene()
        self.st2()
        self.fadeOutCurrentScene()
        self.st3()
        self.fadeOutCurrentScene()
        self.Anim8()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        self.fadeOutCurrentScene()

    def SetDeveloperList(self): 
       self.DeveloperList="Prithiv Shiv M V" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade10Chapter8SimilarTriangles.py"


        
    # render using CVO data object 
    
    def SimTria(self):
        self.isRandom=False
        self.positionChoice=[[-4,0,0],[2,0,0]]
        p10=cvo.CVO().CreateCVO("Similarity","Triangles")
        p11=cvo.CVO().CreateCVO("Conditions","")
        p11onamelist=["Corresponding angles equal","corresponding sides proportional"]
        p10.cvolist.append(p11)
        p11.extendOname(p11onamelist)
        p11.setcircleradius(1.5)
        self.construct1(p10,p10)

    def Anim1(self):
        title = Text("Conditions for Similar Triangles").to_edge(UP)
        self.play(Write(title))
        self.wait(2)

        # Vertices of the first triangle
        A1 = [-5, -1, 0]
        B1 = [-3, 2, 0]
        C1 = [-1, -1, 0]

        # Vertices of the second triangle
        A2 = [1, -1, 0]
        B2 = [2, 1.5, 0]
        C2 = [4, -1, 0]

        # Create the first triangle
        triangle1 = Polygon(A1, B1, C1, color=BLUE)
        triangle1.shift(DOWN * 1.5)  # Shift the triangle down to make room for text
        self.play(Create(triangle1))

        # Create the second triangle
        triangle2 = Polygon(A2, B2, C2, color=GREEN)
        triangle2.shift(DOWN * 1.5)  # Shift the triangle down to make room for text
        self.play(Create(triangle2))

        # Mark angles for the first triangle
        arc_A1 = Arc(radius=0.4, start_angle=340 * DEGREES, angle=110 * DEGREES).move_arc_center_to(A1).shift(1.3*DOWN + 0.5*RIGHT)
        arc_B1 = Arc(radius=0.4, start_angle=215 * DEGREES, angle=100 * DEGREES).move_arc_center_to(B1).shift(1.9*DOWN)
        arc_C1 = Arc(radius=0.4, start_angle=55 * DEGREES, angle=145* DEGREES).move_arc_center_to(C1).shift(1.25*DOWN + 0.75*LEFT)

        angle_A1 = MathTex("\\alpha").move_to(A1).shift(1.3*DOWN + 0.5*RIGHT)
        angle_B1 = MathTex("\\beta").move_to(B1).shift(1.9*DOWN)
        angle_C1 = MathTex("\\gamma").move_to(C1).shift(1.25*DOWN + 0.75*LEFT)

        # Mark angles for the second triangle
        arc_A2 = Arc(radius=0.4, start_angle= 0* DEGREES, angle=130 * DEGREES).move_arc_center_to(A2).shift(1.3*DOWN + 0.5*RIGHT)
        arc_B2 = Arc(radius=0.4, start_angle=225 * DEGREES, angle=105 * DEGREES).move_arc_center_to(B2).shift(1.9*DOWN)
        arc_C2 = Arc(radius=0.4, start_angle=70 * DEGREES, angle=140 * DEGREES).move_arc_center_to(C2).shift(1.25*DOWN + 0.75*LEFT)

        angle_A2 = MathTex("\\alpha").move_to(A2).shift(1.3*DOWN + 0.5*RIGHT)
        angle_B2 = MathTex("\\beta").move_to(B2).shift(1.9*DOWN)
        angle_C2 = MathTex("\\gamma").move_to(C2).shift(1.25*DOWN + 0.75*LEFT)

        self.play(Create(arc_A1), Create(arc_B1), Create(arc_C1), Write(angle_A1), Write(angle_B1), Write(angle_C1))
        self.play(Create(arc_A2), Create(arc_B2), Create(arc_C2), Write(angle_A2), Write(angle_B2), Write(angle_C2))

        # Show proportional sides and angles equations
        proportion_text = Text("AB / DE = BC / EF = CA / FD").scale(0.5).next_to(title, DOWN).shift(DOWN * 0.5)
        angles_text = MathTex("\\angle A = \\angle D, \\angle B = \\angle E, \\angle C = \\angle F").scale(0.5).next_to(proportion_text, DOWN)
        self.play(Write(proportion_text))
        self.play(Write(angles_text))

        self.wait(2)

    def bpt(self):
        self.isRandom=False
        self.positionChoice=[[-4,0,0],[4,0,0]]
        p10=cvo.CVO().CreateCVO("Basic proportionality theorem","").setangle(-TAU/4)
        p11=cvo.CVO().CreateCVO("AKA","Thales Theorem")
        p10.setcircleradius(1.25)
        p11.setcircleradius(1.6)
        p10.cvolist.append(p11)      
        self.construct1(p10,p10)

    def T1(self):
        self.isRandom=False
        self.positionChoice=[[-4,0,0],[0,0,0],[4,0,0]]
        p10=cvo.CVO().CreateCVO("Theorem"," 2 Triangles").setangle(-TAU/4)
        p11=cvo.CVO().CreateCVO("Condition","line drawn $\parallel$ to 1 side")
        p12=cvo.CVO().CreateCVO("Conclusion","intersects 2 sides in same ratio")

        p12.setcircleradius(2)
        p11.setcircleradius(2)

        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        self.construct1(p10,p10)

    def Anim2(self):
        title = Text("Basic Proportionality Theorem").to_edge(UP)
        theorem_text = Text("Line drawn parallel to one side intersects other two sides in the same ratio").scale(0.5).next_to(title, DOWN)
        self.play(Write(title), Write(theorem_text))
        self.wait(2)

        # Vertices of the triangle
        A = [-3, -1, 0]
        B = [3, -1, 0]
        C = [1, 3, 0]

        D = [-1, 1, 0]
        E = [2, 1, 0]

        # Create the triangle
        triangle = Polygon(A, B, C, color=WHITE).shift(1.5*DOWN)
        DE = Line(D, E, color=YELLOW).shift(1.5*DOWN)
        self.play(Create(triangle))
        

        # Labels
        A_label = MathTex("B").next_to(A, DOWN).shift(1.5*DOWN)
        B_label = MathTex("C").next_to(B, DOWN).shift(1.5*DOWN)
        C_label = MathTex("A").next_to(C, UP).shift(1.5*DOWN)
        D_label = MathTex("D").next_to(D, LEFT).shift(1.5*DOWN)
        E_label = MathTex("E").next_to(E, RIGHT).shift(1.5*DOWN)

        # Show line DE
        self.play(Create(DE))
        self.play(Write(A_label), Write(B_label), Write(C_label), Write(D_label), Write(E_label))

        # Proportionality text
        proportion_text = MathTex("\\frac{AD}{DB} = \\frac{AE}{EC}").scale(0.7).to_edge(DOWN)
        self.play(Write(proportion_text))

        # Highlight proportional sides
        AD = Line(A, D, color=BLUE).shift(1.5*DOWN)
        DB = Line(D, B, color=GREEN).shift(1.5*DOWN)
        AE = Line(A, E, color=BLUE).shift(1.5*DOWN)
        EB = Line(E, B, color=GREEN).shift(1.5*DOWN)

        self.play(Create(AD), Create(DB), Create(AE), Create(EB))

        self.wait(2)

    def cri1(self):
        self.isRandom=False
        self.positionChoice=[[0,2,0],[-5,-1,0],[-2,-1,0],[2,-1,0],[5,-1,0]]
        p10=cvo.CVO().CreateCVO("AAA","").setangle(-TAU/4)
        p11=cvo.CVO().CreateCVO("Theorem","2 triangles")
        p12=cvo.CVO().CreateCVO("Condition","corresponding angles =\\\\then corresponding sides proportional")
        p14=cvo.CVO().CreateCVO("Conclusion","Triangles similar")

        p12.setcircleradius(2)
        

        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p14)
        
        self.construct1(p10,p10)

    def Anim3(self):
        title = Text("Angle-Angle-Angle (AAA) Similarity Criterion").to_edge(UP)
        self.play(Write(title))
        self.wait(2)

        # Vertices of the triangles
        triangle1_vert = [[-2, 0, 0], [2, 0, 0], [0, 3, 0]] 
        triangle2_vert = [[-2, 0, 0], [2, 0, 0], [0, 3, 0]]

        # Create triangles
        triangle1 = Polygon(*triangle1_vert, color=BLUE)
        triangle2 = Polygon(*triangle2_vert, color=GREEN)

        # Shift triangles
        triangle1.shift(3 * LEFT + 2 * DOWN)
        triangle2.shift(3 * RIGHT + 2 * DOWN)

        # Labels for vertices
        label1_A = Text("A").next_to(triangle1.get_vertices()[0], DOWN)
        label1_B = Text("B").next_to(triangle1.get_vertices()[1], DOWN)
        label1_C = Text("C").next_to(triangle1.get_vertices()[2], UP)

        label2_D = Text("D").next_to(triangle2.get_vertices()[0], DOWN)
        label2_E = Text("E").next_to(triangle2.get_vertices()[1], DOWN)
        label2_F = Text("F").next_to(triangle2.get_vertices()[2], UP)

        # Angle labels
        angle1_label = MathTex(r"\alpha").move_to(triangle1.get_vertices()[1] + 0.6 * LEFT + 0.4 * UP)
        angle2_label = MathTex(r"\beta").move_to(triangle1.get_vertices()[0] + 0.6 * RIGHT + 0.4 * UP)
        angle3_label = MathTex(r"\gamma").move_to(triangle1.get_vertices()[2] + 0.7 * DOWN)

        angle4_label = MathTex(r"\alpha").move_to(triangle2.get_vertices()[1] + 0.6 * LEFT + 0.4 * UP)
        angle5_label = MathTex(r"\beta").move_to(triangle2.get_vertices()[0] + 0.6 * RIGHT + 0.4 * UP)
        angle6_label = MathTex(r"\gamma").move_to(triangle2.get_vertices()[2] + 0.7 * DOWN)

        # Angle arcs
        angle1_arc = Arc(radius=0.5, start_angle=90, angle=np.pi/3).move_arc_center_to(triangle1.get_vertices()[1])
        angle2_arc = Arc(radius=0.5, start_angle=66*DEGREES, angle=-np.pi/3).move_arc_center_to(triangle1.get_vertices()[0])
        angle3_arc = Arc(radius=0.5, start_angle=226*DEGREES, angle=100*DEGREES).move_arc_center_to(triangle1.get_vertices()[2])

        angle4_arc = Arc(radius=0.5, start_angle=90, angle=np.pi/3).move_arc_center_to(triangle2.get_vertices()[1])
        angle5_arc = Arc(radius=0.5, start_angle=66*DEGREES, angle=-np.pi/3).move_arc_center_to(triangle2.get_vertices()[0])
        angle6_arc = Arc(radius=0.5, start_angle=225*DEGREES, angle=100*DEGREES).move_arc_center_to(triangle2.get_vertices()[2])

        # Animate the creation of elements
        self.play(Create(triangle1), Write(label1_A), Write(label1_B), Write(label1_C))
        self.play(Create(triangle2), Write(label2_D), Write(label2_E), Write(label2_F))
        self.play(Create(angle1_arc), Create(angle2_arc), Create(angle3_arc), Write(angle1_label), Write(angle2_label), Write(angle3_label))
        self.play(Create(angle4_arc), Create(angle5_arc), Create(angle6_arc), Write(angle4_label), Write(angle5_label), Write(angle6_label))

        self.wait(2)

        # Animate merging the triangles
        self.play(
            triangle2.animate.move_to(triangle1.get_center()),
            FadeOut(label2_D),
            FadeOut(label2_E),
            FadeOut(label2_F),
            FadeOut(angle4_arc),
            FadeOut(angle5_arc),
            FadeOut(angle6_arc),
            FadeOut(angle4_label),
            FadeOut(angle5_label),
            FadeOut(angle6_label),
            FadeOut(label1_A),
            FadeOut(label1_B),
            FadeOut(label1_C)
        )

        self.wait(2)

    def cri2(self):
        self.isRandom=False
        self.positionChoice=[[0,2,0],[-5,-1,0],[-2,-1,0],[2,-1,0],[5,-1,0]]
        p10=cvo.CVO().CreateCVO("SSS","").setangle(-TAU/4)
        p11=cvo.CVO().CreateCVO("Theorem","2 triangles")
        p12=cvo.CVO().CreateCVO("Condition","corresponding sides proportional\\\\then corresponding angles =")
        p14=cvo.CVO().CreateCVO("Conclusion","Triangles similar")

        p12.setcircleradius(2)
    
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p14)
        
        self.construct1(p10,p10)

    def Anim4(self):
        triangle1_vert=[[-2, 0, 0],[2, 0, 0],[0, 3, 0]] 
        triangle2_vert=[[-2, 0, 0],[2, 0, 0],[0, 3, 0]]

        triangle1 = Polygon(*triangle1_vert, color=BLUE)
        triangle2 = Polygon(*triangle2_vert, color=GREEN)

        triangle1.shift(3 * LEFT)
        triangle2.shift(3 * RIGHT)
        triangle1.shift(2*DOWN)
        triangle2.shift(2*DOWN)

        label1_A = Text("A").next_to(triangle1.get_vertices()[0], DOWN)
        label1_B = Text("B").next_to(triangle1.get_vertices()[1], DOWN)
        label1_C = Text("C").next_to(triangle1.get_vertices()[2], UP)

        label2_D = Text("D").next_to(triangle2.get_vertices()[0], DOWN)
        label2_E = Text("E").next_to(triangle2.get_vertices()[1], DOWN)
        label2_F = Text("F").next_to(triangle2.get_vertices()[2], UP)

        sss_rule = Text("Side-Side-Side (SSS) Similarity Criterion").to_edge(UP)
        
        
        # Side lengths
        side1 = Text("a").next_to(Line(triangle1.get_vertices()[0], triangle1.get_vertices()[1]).get_center(), DOWN)
        side2 = Text("b").next_to(Line(triangle1.get_vertices()[1], triangle1.get_vertices()[2]).get_center(), RIGHT)
        side3 = Text("c").next_to(Line(triangle1.get_vertices()[2], triangle1.get_vertices()[0]).get_center(), LEFT)
        
        side4 = Text("a").next_to(Line(triangle2.get_vertices()[0], triangle2.get_vertices()[1]).get_center(), DOWN)
        side5 = Text("b").next_to(Line(triangle2.get_vertices()[1], triangle2.get_vertices()[2]).get_center(), RIGHT)
        side6 = Text("c").next_to(Line(triangle2.get_vertices()[2], triangle2.get_vertices()[0]).get_center(), LEFT)

        self.play(Write(sss_rule))
        self.play(Create(triangle1), Write(label1_A), Write(label1_B), Write(label1_C))
        self.play(Write(side1), Write(side2), Write(side3))
        self.play(Create(triangle2), Write(label2_D), Write(label2_E), Write(label2_F))
        self.play(Write(side4), Write(side5), Write(side6))

        self.wait(2)
        
        # Animate merging the triangles
        self.play(
            triangle2.animate.move_to(triangle1.get_center()),
            FadeOut(label2_D),
            FadeOut(label2_E),
            FadeOut(label2_F),
            FadeOut(side4),
            FadeOut(side5),
            FadeOut(side6),
            FadeOut(label1_A),
            FadeOut(label1_B),
            FadeOut(label1_C)
        )

        self.wait(2)

    def cri3(self):
        self.isRandom=False
        self.positionChoice=[[0,2,0],[-5,-1,0],[-2,-1,0],[2,-1,0],[5,-1,0]]
        p10=cvo.CVO().CreateCVO("SAS","")
        p11=cvo.CVO().CreateCVO("Theorem","2 triangles")
        p12=cvo.CVO().CreateCVO("Condition","1 corresponding angle =\\\\including sides of angle proportional")
        p14=cvo.CVO().CreateCVO("Conclusion","Triangles similar")

        p12.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p14)
        
        self.construct1(p10,p10)

    def Anim5(self):
        triangle1_vert = [[-2, 0, 0], [2, 0, 0], [0, 3, 0]] 
        triangle2_vert = [[-2, 0, 0], [2, 0, 0], [0, 3, 0]]

        # Create triangles
        triangle1 = Polygon(*triangle1_vert, color=BLUE)
        triangle2 = Polygon(*triangle2_vert, color=GREEN)

        # Shift triangles
        triangle1.shift(3 * LEFT)
        triangle2.shift(3 * RIGHT)
        triangle1.shift(2 * DOWN)
        triangle2.shift(2 * DOWN)

        # Labels for vertices
        label1_A = Text("A").next_to(triangle1.get_vertices()[0], DOWN)
        label1_B = Text("B").next_to(triangle1.get_vertices()[1], DOWN)
        label1_C = Text("C").next_to(triangle1.get_vertices()[2], UP)

        label2_D = Text("D").next_to(triangle2.get_vertices()[0], DOWN)
        label2_E = Text("E").next_to(triangle2.get_vertices()[1], DOWN)
        label2_F = Text("F").next_to(triangle2.get_vertices()[2], UP)

        # Rule text
        sas_rule = Text("Side-Angle-Side (SAS) Similarity Criterion").to_edge(UP)

        # Angle labels
        angle1_label = MathTex(r"\alpha").move_to(triangle1.get_vertices()[1] + 0.6 * LEFT + 0.4 * UP)
        angle2_label = MathTex(r"\alpha").move_to(triangle2.get_vertices()[1] + 0.6 * LEFT + 0.4 * UP)

        # Angle arcs
        angle1_arc = Arc(radius=0.5, start_angle=90, angle=np.pi/3).move_arc_center_to(triangle1.get_vertices()[1])
        angle2_arc = Arc(radius=0.5, start_angle=90, angle=np.pi/3).move_arc_center_to(triangle2.get_vertices()[1])

        # Side lengths
        side1 = Text("a").next_to(Line(triangle1.get_vertices()[0], triangle1.get_vertices()[1]).get_center(), DOWN)
        side2 = Text("b").next_to(Line(triangle1.get_vertices()[1], triangle1.get_vertices()[2]).get_center(), RIGHT)
        
        side4 = Text("a").next_to(Line(triangle2.get_vertices()[0], triangle2.get_vertices()[1]).get_center(), DOWN)
        side5 = Text("b").next_to(Line(triangle2.get_vertices()[1], triangle2.get_vertices()[2]).get_center(), RIGHT)

        # Animate the creation of elements
        self.play(Write(sas_rule))
        self.play(Create(triangle1), Write(label1_A), Write(label1_B), Write(label1_C))
        self.play(Create(angle1_arc),Write(angle1_label), Write(side1), Write(side2),)
        self.play(Create(triangle2), Write(label2_D), Write(label2_E), Write(label2_F))
        self.play(Create(angle2_arc), Write(angle2_label), Write(side4), Write(side5))

        self.wait(2)
        
        # Animate merging the triangles
        self.play(
            triangle2.animate.move_to(triangle1.get_center()),
            FadeOut(label2_D),
            FadeOut(label2_E),
            FadeOut(label2_F),
            FadeOut(angle2_arc),
            FadeOut(angle2_label),
            FadeOut(side4),
            FadeOut(side5),
            FadeOut(label1_A),
            FadeOut(label1_B),
            FadeOut(label1_C)
        )

        self.wait(2)

    def constructTri(self):
        # Step 1: Draw ray BX making an acute angle with BC
        B = LEFT * 3
        C = RIGHT * 3
        A = LEFT * 2 + UP * 3
        X = RIGHT * 4 + DOWN * 1

        # Draw initial points and lines
        B_dot = Dot(B).set_color(BLUE)
        C_dot = Dot(C).set_color(BLUE)
        A_dot = Dot(A).set_color(BLUE)
        X_dot = Dot(X).set_color(BLUE)

        B_label = MathTex("B").next_to(B, DOWN)
        C_label = MathTex("C").next_to(C, DOWN)
        A_label = MathTex("A").next_to(A, UP)
        X_label = MathTex("X").next_to(X, DOWN)

        self.play(Create(B_dot), Write(B_label))
        self.play(Create(C_dot), Write(C_label))
        self.play(Create(A_dot), Write(A_label))
        self.play(Create(X_dot), Write(X_label))

        BC_line = Line(B, C)
        self.play(Create(BC_line))

        CA_line = Line(C,A)
        self.play(Create(CA_line))
        # Draw line from B to A
        BA_line = Line(B, A)
        self.play(Create(BA_line))

        # 1. Draw a ray BX
        BX_ray = Line(B, X, stroke_width=2).set_color(YELLOW)
        self.play(Create(BX_ray))

        # 2. Locate 4 points B1, B2, B3, and B4 on BX
        B1 = B + (X - B) * 0.2
        B2 = B + (X - B) * 0.4
        B3 = B + (X - B) * 0.6
        B4 = B + (X - B) * 0.8

        B1_dot = Dot(B1).set_color(GREEN)
        B2_dot = Dot(B2).set_color(GREEN)
        B3_dot = Dot(B3).set_color(GREEN)
        B4_dot = Dot(B4).set_color(GREEN)

        B1_label = MathTex("B_1").next_to(B1, DOWN)
        B2_label = MathTex("B_2").next_to(B2, DOWN)
        B3_label = MathTex("B_3").next_to(B3, DOWN)
        B4_label = MathTex("B_4").next_to(B4, DOWN)

        self.play(Create(B1_dot), Write(B1_label))
        self.play(Create(B2_dot), Write(B2_label))
        self.play(Create(B3_dot), Write(B3_label))
        self.play(Create(B4_dot), Write(B4_label))

        # 3. Join B4C and draw a line through B3 parallel to B4C
        B4C_line = Line(B4, C)
        self.play(Create(B4C_line))

        # Calculate C'
        C_prime = B3 + (C - B4 - 0.2)
        C_prime_dot = Dot(C_prime).set_color(RED)
        C_prime_label = MathTex("C'").next_to(C_prime, UP)
        B3C_prime_line = Line(B3, C_prime)

        self.play(Create(B3C_prime_line))
        self.play(Create(C_prime_dot), Write(C_prime_label))

        # 4. Draw a line through C' parallel to CA

        A_prime = Line(B, A).get_projection(C_prime+0.6)  # Ensure A' lies on BA line
        A_prime_dot = Dot(A_prime).set_color(RED)
        A_prime_label = MathTex(" A' ").next_to(A_prime, UP)
        C_primeA_prime_line = Line(C_prime, A_prime)

        self.play(Create(C_primeA_prime_line))
        self.play(Create(A_prime_dot), Write(A_prime_label))

        # Draw the final triangle A'BC'
        final_triangle = Polygon(A_prime, B, C_prime, color=RED)
        title=Tex("Construction of Similar triangle").next_to(X_label, 2*DOWN).scale(1).shift(5*LEFT)
        self.play(Create(final_triangle))
        self.play(Write(title))

        self.wait(2)

    def Area(self):
        self.isRandom=False
        self.positionChoice=[[0,2,0],[-4,0,0],[-1.5,0,0],[0.5,0,0],[4,0,0]]
        p10=cvo.CVO().CreateCVO("Area","similar triangles").setangle(-TAU/4)
        p11=cvo.CVO().CreateCVO("Theorem","2 triangles similar")
        p12=cvo.CVO().CreateCVO("Ratio","area")
        p13=cvo.CVO().CreateCVO("Equal","")
        p14=cvo.CVO().CreateCVO("Ratio","$corresponding sides^2$")

        p14.setcircleradius(2)

        

        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        p13.cvolist.append(p14)
        
        self.construct1(p10,p10)

    def Anim6(self):
        title = Text("Area-Side ratio relation equation").set_color(RED).to_edge(UP)
        theorem_text = Text("The ratio of the areas of two similar triangles is equal to the ratio of the squares of their corresponding sides").scale(0.4).next_to(title, DOWN)
        self.play(Write(title), Write(theorem_text))
        self.wait(2)

        # Vertices of the triangles
        triangle1_vert = [[-2, 0, 0], [2, 0, 0], [0, 3, 0]]
        triangle2_vert = [[-1, 0, 0], [1, 0, 0], [0, 1.5, 0]]

        # Create triangles
        triangle1 = Polygon(*triangle1_vert, color=BLUE, fill_opacity=0.5).shift(0.5*DOWN)
        triangle2 = Polygon(*triangle2_vert, color=GREEN, fill_opacity=0.5).shift(0.5*DOWN)

        # Shift triangles
        triangle1.shift(3 * LEFT + 1 * DOWN)
        triangle2.shift(3 * RIGHT + 1 * DOWN)

        # Labels for vertices
        label1_A = MathTex("A").next_to(triangle1.get_vertices()[2], UP)
        label1_B = MathTex("B").next_to(triangle1.get_vertices()[0], DOWN)
        label1_C = MathTex("C").next_to(triangle1.get_vertices()[1], DOWN)

        label2_P = MathTex("P").next_to(triangle2.get_vertices()[2], UP)
        label2_Q = MathTex("Q").next_to(triangle2.get_vertices()[0], DOWN)
        label2_R = MathTex("R").next_to(triangle2.get_vertices()[1], DOWN)

        # Labels for midpoints
        label1_M = MathTex("M").next_to((triangle1.get_vertices()[0] + triangle1.get_vertices()[1]) / 2, DOWN)
        label2_N = MathTex("N").next_to((triangle2.get_vertices()[0] + triangle2.get_vertices()[1]) / 2, DOWN)

        # Animate the creation of triangles and labels
        self.play(Create(triangle1), Create(triangle2))
        self.play(Write(label1_A), Write(label1_B), Write(label1_C), Write(label2_P), Write(label2_Q), Write(label2_R))
        
        self.wait(2)

        # Fill the triangles to show areas
        self.play(triangle1.animate.set_fill(opacity=0.5), triangle2.animate.set_fill(opacity=0.5))
        
        self.wait(2)

        # Highlight corresponding sides
        side1_AB = Line(triangle1.get_vertices()[0], triangle1.get_vertices()[1], color=WHITE)
        side2_PQ = Line(triangle2.get_vertices()[0], triangle2.get_vertices()[1], color=WHITE)

        self.play(Create(side1_AB), Create(side2_PQ))

        self.wait(1)

        # Highlighting sides BC and QR
        side1_BC = Line(triangle1.get_vertices()[1], triangle1.get_vertices()[2], color=WHITE)
        side2_QR = Line(triangle2.get_vertices()[1], triangle2.get_vertices()[2], color=WHITE)

        self.play(Create(side1_BC), Create(side2_QR))

        self.wait(1)

        # Highlighting sides CA and RP
        side1_CA = Line(triangle1.get_vertices()[2], triangle1.get_vertices()[0], color=WHITE)
        side2_RP = Line(triangle2.get_vertices()[2], triangle2.get_vertices()[0], color=WHITE)

        self.play(Create(side1_CA), Create(side2_RP))

        self.wait(1)

        # Conclude with the equation
        final_equation = MathTex(
            "\\frac{\\text{ar}(\\triangle ABC)}{\\text{ar}(\\triangle PQR)} = \\left(\\frac{AB}{PQ}\\right)^2 = \\left(\\frac{BC}{QR}\\right)^2 = \\left(\\frac{CA}{RP}\\right)^2"
        ).to_edge(DOWN).scale(0.7)
        self.play(Write(final_equation))

        self.wait(2)

    def pyth(self):
        self.isRandom=False
        self.positionChoice=[[-5,0,0],[-2,0,0],[1,0,0],[4.5,0,0]]
        p10=cvo.CVO().CreateCVO("Pythagoras Theorem","Right Triangle").setangle(-TAU/4)
        p12=cvo.CVO().CreateCVO("Condition","$Hypotenuse^2$")
        p13=cvo.CVO().CreateCVO("Equal","$sum\ of\ square\ of\ other\ 2\ sides$")
        p14=cvo.CVO().CreateCVO("Equation","$AC^2\ =\ AB^2\ +\ BC^2$")
        
        p13.setcircleradius(1.5)

        p10.cvolist.append(p12)
        p12.cvolist.append(p13)
        p13.cvolist.append(p14)

        p14.setcircleradius(1.5)
        p13.setcircleradius(1.5)
        
        self.construct1(p10,p10)

    def Anim7(self):
        title = Text("Pythagoras Theorem").set_color(RED).scale(1.2).to_edge(UP)
       
        self.play(Write(title))
        self.wait(2)

        # Vertices of the triangle
        A = np.array([-2, -1, 0])
        B = np.array([3, -1, 0])
        C = np.array([-2, 3, 0])

        # Create triangle
        triangle = Polygon(A, B, C, color=BLUE).shift(2*DOWN)
        

        # Labels for vertices
        label_A = MathTex("B").next_to(A, DOWN).shift(2*DOWN)
        label_B = MathTex("C").next_to(B, DOWN).shift(2*DOWN)
        label_C = MathTex("A").next_to(C, LEFT).shift(2*DOWN)
        right_angle = Square(side_length=0.5).move_to(triangle.get_vertices()[0] + np.array([0.25, 0.25, 0]))
        self.play(Create(triangle))
        self.play(Write(label_A), Write(label_B), Write(label_C), Write(right_angle))

        equation = MathTex("AB^2 + BC^2 = AC^2").scale(1.2).next_to(title, DOWN)
        self.play(Write(equation))
        self.wait(2)

    
    def st(self):
        self.isRandom=False
        self.setNumberOfCirclePositions(2)
        p10=cvo.CVO().CreateCVO("Theoretical statements","").setangle(-TAU/4)
        p11=cvo.CVO().CreateCVO("Forms","")
        p11onamelist=["negation","Converse","Proof by contradiction"]
        p10.cvolist.append(p11)
        p11.extendOname(p11onamelist)
        self.construct1(p10,p10)
    
    def st1(self):
        self.isRandom=False
        self.setNumberOfCirclePositions(3)
        p10=cvo.CVO().CreateCVO("Statement","original statement(p)").setangle(-TAU/4)
        p11=cvo.CVO().CreateCVO("Add","not")
        p12=cvo.CVO().CreateCVO("Result","Negation of statement($~p$)")
        
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        self.construct1(p10,p10)

    def st2(self):
        self.isRandom=False
        self.setNumberOfCirclePositions(3)
        p10=cvo.CVO().CreateCVO("Compound statement","combo of 2 statements").setangle(-TAU/4)
        p11=cvo.CVO().CreateCVO("Implication","If and then usage($=>$)")
        p12=cvo.CVO().CreateCVO("Converse","inverse of implication($<=$)")

        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        self.construct1(p10,p10)

    def st3(self):
        self.isRandom=False
        self.setNumberOfCirclePositions(3)
        p10=cvo.CVO().CreateCVO("Assumption","negation of statement true").setangle(-TAU/4)
        p11=cvo.CVO().CreateCVO("Contradiction","occurs in process of proving")
        p12=cvo.CVO().CreateCVO("Conclusion","original statement is true")

        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        self.construct1(p10,p10)

    def Anim8(self):
        title = Text("Theoretical statements").set_color(RED).scale(1.2).to_edge(UP)
        self.play(Write(title))

        # Examples
        examples_text = Text("Examples:").scale(0.8).next_to(title, DOWN).shift(LEFT)
        self.play(Write(examples_text))

        # Example 1: Negation
        negation_text = Text("Negation").scale(0.7).next_to(examples_text, DOWN).shift(0.5*RIGHT)
        self.play(Write(negation_text))
        negation_symbol = MathTex("\\neg P").scale(0.7).next_to(negation_text, RIGHT)
        self.play(Write(negation_symbol))

        # Example 2: Converse
        converse_text = Text("Converse").scale(0.7).next_to(negation_text, 2*DOWN)
        self.play(Write(converse_text))
        converse_symbol = MathTex("If P \Rightarrow Q\ then\ P \Leftarrow Q\ is\ converse").scale(0.5).next_to(converse_text, RIGHT)
        self.play(Write(converse_symbol))

        # Example 3: Proof by Contradiction
        contradiction_text = Text("Proof by Contradiction").scale(0.7).next_to(converse_text, 2*DOWN).shift(0.5*RIGHT)
        self.play(Write(contradiction_text))
        contradiction_symbol = MathTex("\\neg Q \Rightarrow \\neg P").scale(0.7).next_to(contradiction_text, RIGHT)
        self.play(Write(contradiction_symbol))

        self.wait(2)

               
if __name__ == "__main__":
    scene = Chap8G10_SimilarTriangles()
    scene.render()
    