# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla

from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class Chap8G9_Quadrilaterals(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.Definition()
        self.fadeOutCurrentScene()
        self.Type1()
        self.fadeOutCurrentScene()
        self.Type2()
        self.fadeOutCurrentScene()
        self.Type3()
        self.fadeOutCurrentScene()
        self.Type4()
        self.fadeOutCurrentScene()
        self.Type5()
        self.fadeOutCurrentScene()
        self.Type6()
        self.fadeOutCurrentScene()
        self.pprop1()
        self.fadeOutCurrentScene()
        self.pprop2()
        self.fadeOutCurrentScene()
        self.pprop3()
        self.fadeOutCurrentScene()
        self.pprop4()
        self.fadeOutCurrentScene()        
        self.pprop5()
        self.fadeOutCurrentScene()
        self.mpt()
        self.fadeOutCurrentScene()
        self.mptanim()
        self.fadeOutCurrentScene()
        self.mpt2()
        self.fadeOutCurrentScene()


    def Definition(self):
        self.isRandom=False
        self.positionChoice=[[-4,0,0],[4,2.25,0],[4,-1.5,0]]
        p10=cvo.CVO().CreateCVO("Quadrilaterals","").setangle(-TAU/4)
        p11=cvo.CVO().CreateCVO("Definition","4 sided close polygon")
        p12=cvo.CVO().CreateCVO("Types","")
        p12onamelist=["trapezium","parallelogram","rectangle","square","rhombus","kite"]
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p12.extendOname(p12onamelist)

        p12.setcircleradius(1.6)
        p11.setcircleradius(1.5)
        self.construct1(p10,p10)
    
    def Type1(self):
        heading = Text("Trapezium", font_size=48).to_edge(UP)

        # Create vertices of the trapezium
        A = [-2, 0, 0]
        B = [2, 0, 0]
        C = [1, 2, 0]
        D = [-1, 2, 0]

        # Create sides of the trapezium
        AB = Line(A, B, color=WHITE)  # Parallel side
        BC = Line(B, C, color=GREEN)  # Non-parallel side
        CD = Line(C, D, color=WHITE)  # Parallel side
        DA = Line(D, A, color=GREEN)  # Non-parallel side

        # Create a trapezium
        trapezium = VGroup(AB, BC, CD, DA).shift(2 * DOWN)

        # Labels for vertices
        label_A = Text("A").next_to(A, DOWN).shift(2 * DOWN)
        label_B = Text("B").next_to(B, DOWN).shift(2 * DOWN)
        label_C = Text("C").next_to(C, UP).shift(2 * DOWN)
        label_D = Text("D").next_to(D, UP).shift(2 * DOWN)

        # Properties text
        property1 = Text("One pair of parallel sides", font_size=24).next_to(heading, DOWN)

        self.play(Write(heading))
        self.play(Create(trapezium))
        self.play(Write(label_A), Write(label_B), Write(label_C), Write(label_D))
        self.play(Write(property1))
        self.wait(2)
    
    def Type2(self):
        heading = Text("Parallelogram", font_size=48).to_edge(UP)

        # Create vertices of the parallelogram
        A = [-2, 0, 0]
        B = [2, 0, 0]
        C = [3, 2, 0]
        D = [-1, 2, 0]

        # Create sides of the parallelogram
        AB = Line(A, B, color=WHITE)  # Parallel side
        BC = Line(B, C, color=GREEN)  # Non-parallel side
        CD = Line(C, D, color=WHITE)  # Parallel side
        DA = Line(D, A, color=GREEN)  # Non-parallel side

        # Create a parallelogram
        parallelogram = VGroup(AB, BC, CD, DA).shift(2 * DOWN)

        # Labels for vertices
        label_A = Text("A").next_to(A, DOWN).shift(2 * DOWN)
        label_B = Text("B").next_to(B, DOWN).shift(2 * DOWN)
        label_C = Text("C").next_to(C, UP).shift(2 * DOWN)
        label_D = Text("D").next_to(D, UP).shift(2 * DOWN)

        # Properties text
        property1 = Text("Opposite sides are equal", font_size=24).next_to(heading, DOWN)
        property2 = Text("Opposite angles are equal", font_size=24).next_to(property1, DOWN)

        # Display the parallelogram and labels
        self.play(Write(heading))
        self.play(Create(parallelogram))
        self.play(Write(label_A), Write(label_B), Write(label_C), Write(label_D))
        self.play(Write(property1))
        self.play(Write(property2))
        self.wait(2)
    
    def Type3(self):
        # Heading
        heading = Text("Rectangle", font_size=48).to_edge(UP)

        # Create a rectangle
        rectangle = Polygon([-2, 0, 0], [2, 0, 0], [2, 3, 0], [-2, 3, 0], color=RED)
        rectangle.shift(2 * DOWN)

        # Labels for vertices
        vertices = rectangle.get_vertices()
        label_A = Text("A").next_to(vertices[0], DOWN)
        label_B = Text("B").next_to(vertices[1], DOWN)
        label_C = Text("C").next_to(vertices[2], UP)
        label_D = Text("D").next_to(vertices[3], UP)

        # Properties text
        property1 = Text("Opposite sides are equal", font_size=24).next_to(heading, DOWN)
        property2 = Text("All angles are 90°", font_size=24).next_to(property1, DOWN)

        # Create hollow squares to represent 90-degree angles
        square_size = 0.3
        angle_squares = [
            Square(side_length=square_size, stroke_width=2, color=WHITE).move_to(vertices[0] + [square_size/2, square_size/2, 0]),
            Square(side_length=square_size, stroke_width=2, color=WHITE).move_to(vertices[1] + [-square_size/2, square_size/2, 0]),
            Square(side_length=square_size, stroke_width=2, color=WHITE).move_to(vertices[2] + [-square_size/2, -square_size/2, 0]),
            Square(side_length=square_size, stroke_width=2, color=WHITE).move_to(vertices[3] + [square_size/2, -square_size/2, 0]),
        ]

        self.play(Write(heading))
        self.play(Create(rectangle))
        self.play(Write(label_A), Write(label_B), Write(label_C), Write(label_D))
        self.play(Write(property1))
        self.play(Write(property2))
        
        for square in angle_squares:
            self.play(Create(square))

        self.wait(2)
    
    def Type4(self):
        heading = Text("Square", font_size=48).to_edge(UP)

        # Create a square
        square = Square(side_length=4, color=YELLOW)
        square.shift(DOWN)

        # Extract vertices of the square
        vertices = square.get_vertices()

        # Labels for vertices
        label_A = Text("A").next_to(vertices[0],  2*RIGHT)
        label_B = Text("B").next_to(vertices[1],  2*LEFT)
        label_C = Text("C").next_to(vertices[2],  2*LEFT)
        label_D = Text("D").next_to(vertices[3],  2*RIGHT)

        # Properties text
        property1 = Text("All sides are equal", font_size=24).next_to(heading, DOWN)
        property2 = Text("All angles are 90°", font_size=24).next_to(property1, DOWN)

        # Create small squares to represent 90-degree angles
        square_size = 0.3
        angle_squares = [
            Square(side_length=square_size, stroke_width=2, color=WHITE, fill_opacity=0).move_to(vertices[0] + [square_size / 2, square_size / 2, 0]).shift(0.3*LEFT+0.3*DOWN),
            Square(side_length=square_size, stroke_width=2, color=WHITE, fill_opacity=0).move_to(vertices[1] + [-square_size / 2, square_size / 2, 0]).shift(0.3*RIGHT+0.3*DOWN),
            Square(side_length=square_size, stroke_width=2, color=WHITE, fill_opacity=0).move_to(vertices[2] + [-square_size / 2, -square_size / 2, 0]).shift(0.3*RIGHT+0.3*UP),
            Square(side_length=square_size, stroke_width=2, color=WHITE, fill_opacity=0).move_to(vertices[3] + [square_size / 2, -square_size / 2, 0]).shift(0.3*LEFT++0.3*UP),
        ]

        # Display the square and labels
        self.play(Write(heading))
        self.play(Create(square))
        self.play(Write(label_A), Write(label_B), Write(label_C), Write(label_D))
        self.play(Write(property1))
        self.play(Write(property2))

        # Display the angle squares
        for small_square in angle_squares:
            self.play(Create(small_square))

        self.wait(2)
    
    def Type5(self):
        heading = Text("Rhombus", font_size=48).to_edge(UP)

        A = np.array([-2, 0, 0])
        B = np.array([2, 0, 0])
        C = np.array([3, 2, 0])
        D = np.array([-1, 2, 0])

        AB = Line(A, B, color=WHITE)
        BC = Line(B, C, color=WHITE)
        CD = Line(C, D, color=WHITE)
        DA = Line(D, A, color=WHITE)

        rhombus = VGroup(AB, BC, CD, DA)
        rhombus.shift(2 * DOWN)

        # Labels for vertices
        label_A = Text("A").next_to(A + 2 * DOWN, DOWN)
        label_B = Text("B").next_to(B + 2 * DOWN, DOWN)
        label_C = Text("C").next_to(C + 2 * DOWN, UP)
        label_D = Text("D").next_to(D + 2 * DOWN, UP)

        # Create diagonals
        AC = Line(A, C, color=YELLOW).shift(2*DOWN)
        BD = Line(B, D, color=YELLOW).shift(2*DOWN)

        # Properties text
        property1 = Text("All sides are equal", font_size=24).next_to(heading, DOWN)
        property2 = Text("Diagonals bisect each other at right angles", font_size=24).next_to(property1, DOWN)

        # Intersection point of diagonals
        intersection = ORIGIN +DOWN + 0.5*RIGHT

        # Small squares at right angles
        angle_square_1 = Square(side_length=0.2, color=BLUE).move_to(intersection + np.array([0, 0.1, 0])).rotate(35*DEGREES)
        angle_square_2 = Square(side_length=0.2, color=BLUE).move_to(intersection + np.array([0, -0.1, 0])).rotate(35*DEGREES)

        self.play(Write(heading))
        self.play(Create(rhombus))
        self.play(Write(label_A), Write(label_B), Write(label_C), Write(label_D))
        
        # Draw diagonals
        self.play(Create(AC), Create(BD))
        
        # Highlight the intersection point of the diagonals
        self.play(GrowFromCenter(Dot(intersection, color=RED)))
        
        # Draw right angle squares at the intersection
        self.play(FadeIn(angle_square_1), FadeIn(angle_square_2))
        
        self.play(Write(property1))
        self.play(Write(property2))
        self.wait(2)
    
    def Type6(self):
        heading = Text("Kite", font_size=48).to_edge(UP)
        
        # Create a kite
        kite = Polygon([0, 2, 0], [2, 0, 0], [0, -2, 0], [-2, 0, 0], color=ORANGE)
        kite.shift(DOWN)
        
        # Labels for vertices
        label_A = Text("A").next_to(kite.get_vertices()[0], UP)
        label_B = Text("B").next_to(kite.get_vertices()[1], RIGHT)
        label_C = Text("C").next_to(kite.get_vertices()[2], DOWN)
        label_D = Text("D").next_to(kite.get_vertices()[3], LEFT)

        # Properties text
        property1 = Text("Two pairs of adjacent sides are equal", font_size=24).next_to(heading, DOWN)
        property2 = Text("Diagonals intersect at right angles", font_size=24).next_to(property1, DOWN)

        # Diagonals
        diagonal_AC = Line(kite.get_vertices()[0], kite.get_vertices()[2], color=YELLOW)
        diagonal_BD = Line(kite.get_vertices()[1], kite.get_vertices()[3], color=YELLOW)

        # Intersection point of diagonals
        intersection = kite.get_center()

        # Small square at right angle
        angle_square = Square(side_length=0.3, color=BLUE, fill_opacity=1).move_to(intersection).rotate(PI/4)

        # Mark equal sides with braces
        brace_AB = Brace(Line(kite.get_vertices()[0], kite.get_vertices()[1]), direction=kite.get_vertices()[1] - kite.get_vertices()[0], color=GREEN)
        brace_AD = Brace(Line(kite.get_vertices()[0], kite.get_vertices()[3]), direction=kite.get_vertices()[3] - kite.get_vertices()[0], color=GREEN)
        brace_BC = Brace(Line(kite.get_vertices()[1], kite.get_vertices()[2]), direction=kite.get_vertices()[2] - kite.get_vertices()[1], color=GREEN)
        brace_CD = Brace(Line(kite.get_vertices()[2], kite.get_vertices()[3]), direction=kite.get_vertices()[3] - kite.get_vertices()[2], color=GREEN)

        self.play(Write(heading))
        self.play(Create(kite))
        self.play(Write(label_A), Write(label_B), Write(label_C), Write(label_D))

        # Draw diagonals
        self.play(Create(diagonal_AC), Create(diagonal_BD))
        
        # Highlight the intersection point of the diagonals with a right angle square
        self.play(FadeIn(angle_square))
        
        # Draw braces to show equal sides
        self.play(GrowFromCenter(brace_AB), GrowFromCenter(brace_AD), GrowFromCenter(brace_BC), GrowFromCenter(brace_CD))
        
        self.play(Write(property1))
        self.play(Write(property2))
        self.wait(2)

    def pprop1(self):
        title = Text("Parallelogram").to_edge(UP)
        property_text = Text("A diagonal of a parallelogram divides it into two congruent triangles").next_to(title, DOWN).scale(0.5)
        self.play(Write(title), Write(property_text))

        # Vertices
        A = [-2, -1, 0]
        B = [2, -1, 0]
        C = [3, 1, 0]
        D = [-1, 1, 0]

        # Parallelogram
        parallelogram = Polygon(A, B, C, D, color=WHITE)
        self.play(Create(parallelogram))

        # Diagonal
        diagonal = Line(A, C, color=YELLOW)
        self.play(Create(diagonal))

        # Labels
        label_A = Text("A").next_to(A, DOWN)
        label_B = Text("B").next_to(B, DOWN)
        label_C = Text("C").next_to(C, UP)
        label_D = Text("D").next_to(D, UP)

        self.play(Write(label_A), Write(label_B), Write(label_C), Write(label_D))

        # Triangles
        triangle_ABC = Polygon(A, B, C, color=BLUE, fill_opacity=0.5)
        triangle_ADC = Polygon(A, D, C, color=GREEN, fill_opacity=0.5)

        self.play(FadeIn(triangle_ABC), FadeIn(triangle_ADC))

        # Arcs for diagonal vertices
        arc_A = Arc(radius=0.25, start_angle=5 * DEGREES, angle=90 * DEGREES).move_arc_center_to(A)
        arc_C = Arc(radius=0.25, start_angle=150 * DEGREES, angle=90 * DEGREES).move_arc_center_to(C)

        double_arc_A = Arc(radius=0.5, start_angle=5 * DEGREES, angle=90 * DEGREES).move_arc_center_to(A)
        double_arc_C = Arc(radius=0.5, start_angle=150* DEGREES, angle=90 * DEGREES).move_arc_center_to(C)

        self.play(Create(arc_A), Create(arc_C))
        self.play(Create(double_arc_A), Create(double_arc_C))

        self.wait(2)

    def pprop2(self):
        title = Text("Parallelogram").to_edge(UP)
        property_text = Text("In a parallelogram, opposite sides are equal and opposite angles are equal").next_to(title, DOWN).scale(0.5)
        self.play(Write(title), Write(property_text))

        # Vertices
        A = [-3, -1, 0]
        B = [1, -1, 0]
        C = [3, 1, 0]
        D = [-1, 1, 0]

        # Parallelogram
        parallelogram = Polygon(A, B, C, D, color=WHITE)
        self.play(Create(parallelogram))

        # Labels for vertices
        label_A = Text("A").next_to(A, DOWN)
        label_B = Text("B").next_to(B, DOWN)
        label_C = Text("C").next_to(C, UP)
        label_D = Text("D").next_to(D, UP)

        self.play(Write(label_A), Write(label_B), Write(label_C), Write(label_D))

        # Side labels
        side_AB = Text("a").next_to(Line(A, B).get_center(), DOWN)
        side_CD = Text("a").next_to(Line(C, D).get_center(), UP)
        side_AD = Text("b").next_to(Line(A, D).get_center(), LEFT)
        side_BC = Text("b").next_to(Line(B, C).get_center(), RIGHT)

        self.play(Write(side_AB), Write(side_CD), Write(side_AD), Write(side_BC))

        # Angle arcs and labels
        arc_A = Arc(radius=0.5, start_angle=0, angle=PI/4).move_arc_center_to(A)
        arc_C = Arc(radius=0.5, start_angle=PI, angle=PI/4).move_arc_center_to(C)

        angle_A_label = MathTex(r"\alpha").move_to(A + 0.7*RIGHT + 0.3*UP)
        angle_C_label = MathTex(r"\alpha").move_to(C + 0.7*LEFT + 0.3*DOWN)

        arc_B = Arc(radius=0.4, start_angle=PI, angle=(2*-PI)/3).move_arc_center_to(B)
        arc_D = Arc(radius=0.4, start_angle=0, angle=(2*-PI)/3).move_arc_center_to(D)

        angle_B_label = MathTex(r"\beta").move_to(B + 0.7*LEFT + 0.3*UP)
        angle_D_label = MathTex(r"\beta").move_to(D + 0.7*RIGHT + 0.3*DOWN)

        self.play(Create(arc_A), Create(arc_C), Write(angle_A_label), Write(angle_C_label))
        self.play(Create(arc_B), Create(arc_D), Write(angle_B_label), Write(angle_D_label))

        self.wait(2)
    
    def pprop3(self):
        title = Text("Parallelogram").to_edge(UP)
        property_text = Text("If each pair of opposite sides of a quadrilateral is equal, then it is a parallelogram").next_to(title, DOWN).scale(0.5)
        self.play(Write(title), Write(property_text))

        # Vertices
        A = [-3, -1, 0]
        B = [1, -1, 0]
        C = [3, 1, 0]
        D = [-1, 1, 0]

        # Parallelogram
        parallelogram = Polygon(A, B, C, D, color=WHITE)
        self.play(Create(parallelogram))

        # Labels for vertices
        label_A = Text("A").next_to(A, DOWN)
        label_B = Text("B").next_to(B, DOWN)
        label_C = Text("C").next_to(C, UP)
        label_D = Text("D").next_to(D, UP)

        self.play(Write(label_A), Write(label_B), Write(label_C), Write(label_D))

        # Equal sides
        side_AB = Line(A, B)
        side_CD = Line(C, D)
        side_AD = Line(A, D)
        side_BC = Line(B, C)

        # Midpoints
        mid_AB = side_AB.get_center()
        mid_CD = side_CD.get_center()
        mid_AD = side_AD.get_center()
        mid_BC = side_BC.get_center()

        # Color sides
        side_AB.set_color(RED)
        side_CD.set_color(RED)
        side_AD.set_color(BLUE)
        side_BC.set_color(BLUE)

        # Length labels
        length_label_AB = MathTex("4").next_to(mid_AB, UP)
        length_label_CD = MathTex("4").next_to(mid_CD, UP)
        length_label_AD = MathTex("3").next_to(mid_AD, LEFT)
        length_label_BC = MathTex("3").next_to(mid_BC, RIGHT)

        self.play(Create(side_AB), Create(side_CD), Create(side_AD), Create(side_BC))
        self.play(Write(length_label_AB), Write(length_label_CD), Write(length_label_AD), Write(length_label_BC))

        self.wait(2)

    def pprop4(self):
        title = Text("Parallelogram").to_edge(UP)
        property_text = Text("In a parallelogram, opposite sides are equal and opposite angles are equal").next_to(title, DOWN).scale(0.5)
        self.play(Write(title), Write(property_text))

        # Vertices
        A = [-3, -1, 0]
        B = [1, -1, 0]
        C = [3, 1, 0]
        D = [-1, 1, 0]

        # Parallelogram
        parallelogram = Polygon(A, B, C, D, color=WHITE)
        self.play(Create(parallelogram))

        # Labels for vertices
        label_A = Text("A").next_to(A, DOWN)
        label_B = Text("B").next_to(B, DOWN)
        label_C = Text("C").next_to(C, UP)
        label_D = Text("D").next_to(D, UP)

        self.play(Write(label_A), Write(label_B), Write(label_C), Write(label_D))

        # Side labels
        side_AB = Text("a").next_to(Line(A, B).get_center(), DOWN)
        side_CD = Text("a").next_to(Line(C, D).get_center(), UP)
        side_AD = Text("b").next_to(Line(A, D).get_center(), LEFT)
        side_BC = Text("b").next_to(Line(B, C).get_center(), RIGHT)

        self.play(Write(side_AB), Write(side_CD), Write(side_AD), Write(side_BC))

        # Angle arcs and labels
        arc_A = Arc(radius=0.5, start_angle=0, angle=PI/4).move_arc_center_to(A)
        arc_C = Arc(radius=0.5, start_angle=PI, angle=PI/4).move_arc_center_to(C)

        angle_A_label = MathTex(r"\alpha").move_to(A + 0.7*RIGHT + 0.3*UP)
        angle_C_label = MathTex(r"\alpha").move_to(C + 0.7*LEFT + 0.3*DOWN)

        arc_B = Arc(radius=0.5, start_angle=-PI, angle=-3*PI/4).move_arc_center_to(B)
        arc_D = Arc(radius=0.5, start_angle=0, angle=2*-PI/3).move_arc_center_to(D)

        angle_B_label = MathTex(r"\beta").move_to(B + 0.7*LEFT + 0.3*UP)
        angle_D_label = MathTex(r"\beta").move_to(D + 0.7*RIGHT + 0.3*DOWN)

        self.play(Create(arc_A), Create(arc_C), Write(angle_A_label), Write(angle_C_label))
        self.play(Create(arc_B), Create(arc_D), Write(angle_B_label), Write(angle_D_label))

        self.wait(2)

    def pprop5(self):
        title = Text("Parallelogram").to_edge(UP)
        property_text = Text("The diagonals of a parallelogram bisect each other").next_to(title, DOWN).scale(0.5)
        self.play(Write(title), Write(property_text))

        # Vertices
        A = [-3, -1, 0]
        B = [1, -1, 0]
        C = [3, 1, 0]
        D = [-1, 1, 0]

        # Parallelogram
        parallelogram = Polygon(A, B, C, D, color=WHITE)
        self.play(Create(parallelogram))

        # Diagonals
        diagonal_AC = Line(A, C)
        diagonal_BD = Line(B, D)

        # Midpoint of diagonal
        diagonal_intersection = np.mean([diagonal_AC.get_start(), diagonal_AC.get_end()], axis=0)

        # Mark diagonal intersection point
        dot = Dot(diagonal_intersection)

        # Arcs for angles at each vertex
        arc_A = Arc(start_angle=0, angle=PI/4, radius=1).move_arc_center_to(A)
        arc_B = Arc(start_angle=PI, angle=-PI/4, radius=0.5).move_arc_center_to(B)
        arc_C = Arc(start_angle=PI, angle=PI/4, radius=1).move_arc_center_to(C)
        arc_D = Arc(start_angle=0, angle=-PI/4, radius=0.5).move_arc_center_to(D)

        # Arcs for bisected angles
        arc_midpoint_BC = Arc(start_angle=3*PI/4, angle=-PI/2, radius=0.5).move_arc_center_to(diagonal_intersection)
        arc_midpoint_DA = Arc(start_angle=-3*PI/4, angle=PI/2, radius=0.5).move_arc_center_to(diagonal_intersection)

        # Lines connecting vertex to diagonal intersection point
        line_AD_inter = Line(A, diagonal_intersection)
        line_BC_inter = Line(B, diagonal_intersection)
        line_AB_inter = Line(A, diagonal_intersection)
        line_CD_inter = Line(C, diagonal_intersection)

        # Play animations
        self.play(Create(diagonal_AC), Create(diagonal_BD))
        self.play(Create(dot))
        self.play(Create(arc_A), Create(arc_B), Create(arc_C), Create(arc_D))
        self.play(Create(arc_midpoint_BC), Create(arc_midpoint_DA))
        self.play(Create(line_AD_inter), Create(line_BC_inter), Create(line_AB_inter), Create(line_CD_inter))

        self.wait(2)

    def mpt(self):
        self.isRandom=False
        self.positionChoice=[[-5,0,0],[0,0,0],[4,0,0]]
        p11=cvo.CVO().CreateCVO("Midpoint Theorem","Triangle")
        p12=cvo.CVO().CreateCVO("Condition","Line segment\\\\ joining Midpoint of 2 sides")
        p13=cvo.CVO().CreateCVO("Conclusion","")
        p13onamelist=["parallel to third side","Half of third side"]
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        p13.extendOname(p13onamelist)
        p12.setcircleradius(1.8)
        p13.setcircleradius(2)

        self.construct1(p11,p11)

    def mptanim(self):
        heading = Text("Midsegment Theorem", font_size=48).to_edge(UP)

        # Define triangle vertices (inverted triangle)
        A = np.array([0, 2, 0])
        B = np.array([-3, -1, 0])
        C = np.array([3, -1, 0])

        # Create triangle
        triangle = Polygon(A, B, C, color=PINK)

        # Midpoints of two sides
        E = (A + B) / 2
        F = (A + C) / 2

        # Midsegment EF
        midsegment = Line(E, F, color=ORANGE)

        # New vertex D for the protruding triangle
        D = F + (F - E)

        # New triangle FDC
        triangle_FDC = Polygon(F, D, C, color=GREEN)

        # Labels for vertices
        label_A = Text("A").next_to(A, UP)
        label_B = Text("B").next_to(B, LEFT)
        label_C = Text("C").next_to(C, RIGHT)
        label_E = Text("E").next_to(E, LEFT)
        label_F = Text("F").next_to(F, RIGHT)
        label_D = Text("D").next_to(D, UP)

        # Properties text
        property1 = Text("EF is parallel to BC", font_size=24).next_to(label_A, 15*DOWN)
        property2 = Text("EF is half the length of BC", font_size=24).next_to(property1, DOWN)

        # Parallel lines annotation (not shown in your image but can be useful)
        parallel_line1 = Line(E, E + (C - B), color=BLUE, stroke_width=2, stroke_opacity=0.5)
        parallel_line2 = Line(F, F + (C - B), color=BLUE, stroke_width=2, stroke_opacity=0.5)

        # Animation
        self.play(Write(heading))
        self.play(Create(triangle))
        self.play(Write(label_A), Write(label_B), Write(label_C))

        # Draw midpoints and midsegment
        self.play(Create(Dot(E, color=RED)), Write(label_E))
        self.play(Create(Dot(F, color=RED)), Write(label_F))
        self.play(Create(midsegment))

        # Draw new triangle FDC
        self.play(Create(triangle_FDC))
        self.play(Create(Dot(D, color=RED)), Write(label_D))

        # Show properties text
        self.play(Write(property1))
        self.play(Write(property2))

        self.wait(2)

    def mpt2(self):
        self.isRandom=False
        self.positionChoice=[[-5,0,0],[0,0,0],[4,0,0]]
        p11=cvo.CVO().CreateCVO("Midpoint Theorem","Triangle")
        p12=cvo.CVO().CreateCVO("Condition","Midpoint of 1 side\\\\ parallel to another side")
        p13=cvo.CVO().CreateCVO("Conclusion","Bisects third side")

        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        p12.setcircleradius(2)
        p11.setcircleradius(2)
        p13.setcircleradius(1.5)

        self.construct1(p11,p11)


    # use the appropriate method based on how the data is stored              

if __name__ == "__main__":
    scene = Chap8G9_Quadrilaterals()
    scene.render()
    