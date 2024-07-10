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

class trianglesAnim(AbstractAnim):
     # use the appropriate method based on how the data is stored
    def construct(self):
         self.RenderSkillbancLogo()
         self.constructDataByCVO()
         self.fadeOutCurrentScene() 
         self.trianglepqr()
         self.fadeOutCurrentScene() 
         self.triangles()
         self.fadeOutCurrentScene() 
         self.type1()
         self.fadeOutCurrentScene()
         self.type2()
         self.fadeOutCurrentScene()
         self.type3()
         self.fadeOutCurrentScene()
         self.triangles111()
         self.fadeOutCurrentScene() 
         self.type11()
         self.fadeOutCurrentScene() 
         self.triangles1155()
         self.fadeOutCurrentScene()
       
         self.triangles1122()
         self.fadeOutCurrentScene()
         self.triangles1133()
         self.fadeOutCurrentScene()
         self.triangles1144()
         self.fadeOutCurrentScene() 
       
         self.fadeOutCurrentScene() 
         self.GithubSourceCodeReference()


# render using CVO data object
    def constructDataByCVO(self):
        p10=cvo.CVO().CreateCVO("Triangles and its Properties","").setPosition(-TAU/4)
        p11=cvo.CVO().CreateCVO("Properties","")
        p12=cvo.CVO().CreateCVO("Sides","PQ,QR,RP")
        p13=cvo.CVO().CreateCVO("Angles","angle Q,angle P,angle R")
        p14=cvo.CVO().CreateCVO("Vertices","p,q,r")
        
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
        p11.cvolist.append(p14)
        self.setNumberOfCirclePositions(5)

        self.construct1(p10,p10)
  


    def trianglepqr(self):

        # Define the vertices of the equilateral triangle
        P = np.array([0, 2, 0])
        Q = np.array([np.sqrt(3), -1, 0])
        R = np.array([-np.sqrt(3), -1, 0])

        # Create the triangle and shift it to the left
        triangle = Polygon(P, Q, R, color=GREEN).shift(LEFT * 2)

        # Function to create an arc at a given vertex
        def create_arc(vertex, left, right, label_text, label_direction, label_shift):
            angle = angle_between_vectors(left - vertex, right - vertex)
            arc = Arc(radius=0.5, start_angle=angle_of_vector(left - vertex), angle=angle, color=RED)
            arc.move_arc_center_to(vertex + LEFT * 2)
            label = MathTex(label_text).next_to(arc, label_direction).shift(label_shift)
            return arc, label

        # Create arcs and labels
        arc_p, label_p = create_arc(P, R, Q, '', UP, 0.3 * UP)
        arc_q, label_q = create_arc(Q, P, R, '', RIGHT, 0.3 * RIGHT + 0.2 * UP)
        arc_r, label_r = create_arc(R, Q, P, '', LEFT, 0.3 * LEFT + 0.2 * UP)

        # Create vertex labels
        label_P = MathTex('P', color=RED).next_to(P + LEFT * 2, direction=UP)
        label_Q = MathTex('Q', color=RED).next_to(Q + LEFT * 2, direction=RIGHT + DOWN)
        label_R = MathTex('R', color=RED).next_to(R + LEFT * 2, direction=LEFT + DOWN)

        # Add the title
        title = Text("Triangle PQR", font_size=36).to_edge(UP)

        # Add the conclusion
        conclusion = VGroup(
            Text("Properties", font_size=30),
            MathTex(r"\text{1) Sides} - PQ, QR, RP", font_size=28),
            MathTex(r"\text{2) Angles} - \angle P, \angle Q, \angle R", font_size=28),
            MathTex(r"\text{3) Vertices} - P, Q, R", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT).shift(RIGHT * 3)

        # Add elements to the scene
        self.add(triangle, arc_p, arc_q, arc_r, label_p, label_q, label_r, label_P, label_Q, label_R, title, conclusion)

        self.wait(3)

    def triangles(self):
      
        p20 = cvo.CVO().CreateCVO("triangles", "based on sides").setPosition(-TAU/4)
        p21 = cvo.CVO().CreateCVO("Isosceles", "$PQ = QR \\neq RP$")
        p22 = cvo.CVO().CreateCVO("Scalene", "$PQ \\neq QR \\neq RP$")
        p23 = cvo.CVO().CreateCVO("Equilateral", "PQ = QR = RP")

        p20.cvolist.append(p21)
        p20.cvolist.append(p22)
        p20.cvolist.append(p23)
        p21.setcircleradius(1.5)
        p22.setcircleradius(1.5)
        p23.setcircleradius(1.5)
        
        self.setNumberOfCirclePositions(4)

        self.construct1(p20, p20)



    def type1(self):
       
    
     
    
        # Create the points for the triangle, scaled to make it bigger
        A = 2 * LEFT + 2 * DOWN
        B = 2 * UP
        C = 2 * RIGHT + 2 * DOWN

        # Create the triangle
        triangle = Polygon(A, B, C, color=GREEN)

        # Labels for the vertices
        label_A = Text("P").next_to(A, LEFT)
        label_B = Text("Q").next_to(B, UP)
        label_C = Text("R").next_to(C, RIGHT)

        # Title
        title = Text("Isosceles Triangle").to_edge(UP)

        # Add hash marks to indicate equal sides
        hash_mark = Line(LEFT * 0.1, RIGHT * 0.1).rotate(PI/4)
        hash_mark_opposite = Line(LEFT * 0.1, RIGHT * 0.1).rotate(-PI/4)

        hash_marks_a = VGroup(hash_mark.copy().move_to(Line(B, C).point_from_proportion(0.45)),
                              hash_mark.copy().move_to(Line(B, C).point_from_proportion(0.55)))
        hash_marks_c = VGroup(hash_mark_opposite.copy().move_to(Line(A, B).point_from_proportion(0.45)),
                              hash_mark_opposite.copy().move_to(Line(A, B).point_from_proportion(0.55)))

        # Add a single vertical hash mark on the third side
        hash_mark_b = Line(UP * 0.1, DOWN * 0.1).move_to(Line(A, C).point_from_proportion(0.5))

        # Add all elements to the scene
        self.add(triangle, label_A, label_B, label_C, title, hash_marks_a, hash_marks_c, hash_mark_b)

        # Conclusion statement
        conclusion = Tex("$PQ = QR \\neq RP$").next_to(triangle, DOWN)
        self.play(Write(conclusion))

        self.wait(2)  # Optional: Wait for 2 seconds at the end



    def type2(self):
   
    
        # Create the points for the triangle, scaled to make it bigger
        A = 2 * LEFT + 2 * DOWN
        B = 2 * UP
        C = 2 * RIGHT + 2 * DOWN

        # Create the triangle
        triangle = Polygon(A, B, C, color=RED)  # Changed color to RED for a scalene triangle

        # Labels for the vertices
        label_A = Text("P").next_to(A, LEFT)
        label_B = Text("Q").next_to(B, UP)
        label_C = Text("R").next_to(C, RIGHT)

        # Title
        title = Text("Scalene Triangle").to_edge(UP)

        # Add hash marks to indicate unequal sides
        hash_mark_horizontal_pq = Line(LEFT * 0.1, RIGHT * 0.1).move_to(Line(A, B).point_from_proportion(0.45))  # Horizontal hash mark on PQ
        
        hash_mark_horizontal_qr = VGroup(
            Line(LEFT * 0.1, RIGHT * 0.1).move_to(Line(B, C).point_from_proportion(0.48)),  # First horizontal hash mark on QR
            Line(LEFT * 0.1, RIGHT * 0.1).move_to(Line(B, C).point_from_proportion(0.52))   # Second horizontal hash mark on QR
        )
        
        hash_mark_rp = VGroup(
            Line(UP * 0.1, DOWN * 0.1).move_to(Line(A, C).point_from_proportion(0.4)),  # First hash mark on RP
            Line(UP * 0.1, DOWN * 0.1).move_to(Line(A, C).point_from_proportion(0.5)),  # Second hash mark on RP
            Line(UP * 0.1, DOWN * 0.1).move_to(Line(A, C).point_from_proportion(0.6))   # Third hash mark on RP
        )

        # Add all elements to the scene
        self.add(triangle, label_A, label_B, label_C, title, hash_mark_horizontal_pq, hash_mark_horizontal_qr, hash_mark_rp)

        # Conclusion statement
        conclusion = Tex("$PQ \\neq QR \\neq RP$").next_to(triangle, DOWN)
        self.play(Write(conclusion))

        self.wait(2)  # Optional: Wait for 2 seconds at the end


    def type3(self):
       
      
     
       
        # Create the points for the triangle, scaled to make it bigger
        A = 2 * LEFT + 2 * DOWN
        B = 2 * UP
        C = 2 * RIGHT + 2 * DOWN

        # Create the triangle
        triangle = Polygon(A, B, C, color=BLUE)  # Changed color to BLUE for an equilateral triangle

        # Labels for the vertices
        label_A = Text("P").next_to(A, LEFT)
        label_B = Text("Q").next_to(B, UP)
        label_C = Text("R").next_to(C, RIGHT)

        # Title
        title = Text("Equilateral Triangle").to_edge(UP)

        # Add hash marks to indicate equal sides
        hash_mark_vertical = Line(UP * 0.1, DOWN * 0.1).move_to(Line(A, B).point_from_proportion(0.5))  # Vertical hash mark on PQ
        hash_mark = Line(LEFT * 0.1, RIGHT * 0.1).rotate(PI/3)  # 60 degrees for equilateral triangle
        hash_marks = VGroup(
            hash_mark_vertical,
            hash_mark.copy().move_to(Line(B, C).point_from_proportion(0.5)),  # Hash mark on QR
            Line(UP * 0.1, DOWN * 0.1).move_to(Line(A, C).point_from_proportion(0.5))  # Hash mark on PR
        )

        # Add all elements to the scene
        self.add(triangle, label_A, label_B, label_C, title, hash_marks)

        # Conclusion statement
        conclusion = Tex("$PQ = QR = RP$").next_to(triangle, DOWN)
        self.play(Write(conclusion))

        self.wait(2)  # Optional: Wait for 2 seconds at the end



    def triangles111(self):
        p24=cvo.CVO().CreateCVO("triangles","based on angles ").setPosition(-TAU/4)
        p25=cvo.CVO().CreateCVO("Acute angled triangle","angle ($A= B=C>90$)")
        p26=cvo.CVO().CreateCVO("Right angled triangle ","angle(A/B/C=90)")
        p27=cvo.CVO().CreateCVO("Obtuse angled triangle","angle ($A=B=C<90$)")

        p24.cvolist.append(p25)
        p24.cvolist.append(p26)
        p24.cvolist.append(p27)

        self.setNumberOfCirclePositions(4)

        self.construct1(p24,p24)

    def type11(self):
       
      
     
        # Scale factor to make the figures larger
        scale_factor = 1.5
        
        # Acute Triangle
        acute_triangle = Polygon(
            np.array([-1, -1, 0]),
            np.array([1, -1, 0]),
            np.array([0, 1, 0]),
            color=WHITE
        ).scale(scale_factor)
        acute_label = Text("Acute Angled Triangle", font_size=35).to_edge(UP)
        acute_angle_text = Text("3 angles < 90°", font_size=25).next_to(acute_triangle, DOWN)
        
        acute_points = [acute_triangle.get_vertices()[i] for i in range(3)]
        acute_labels = [
            Text("P", font_size=24).move_to(acute_points[0] + LEFT * 0.2 + DOWN * 0.2),
            Text("Q", font_size=24).move_to(acute_points[1] + RIGHT * 0.2 + DOWN * 0.2),
            Text("R", font_size=24).move_to(acute_points[2] + UP * 0.2),
        ]
        
        # Obtuse Triangle
        obtuse_triangle = Polygon(
            np.array([-1.5, -1, 0]),
            np.array([1.5, -1, 0]),
            np.array([-0.5, 1, 0]),
            color=WHITE
        ).scale(scale_factor)
        obtuse_label = Text("Obtuse Angled Triangle", font_size=35).to_edge(UP)
        obtuse_angle_text = Text("1 angle > 90°", font_size=25).next_to(obtuse_triangle, DOWN)
        
        obtuse_points = [obtuse_triangle.get_vertices()[i] for i in range(3)]
        obtuse_labels = [
            Text("P", font_size=24).move_to(obtuse_points[0] + LEFT * 0.2 + DOWN * 0.2),
            Text("Q", font_size=24).move_to(obtuse_points[1] + RIGHT * 0.2 + DOWN * 0.2),
            Text("R", font_size=24).move_to(obtuse_points[2] + UP * 0.2),
        ]
        
        # Right Triangle
        right_triangle = Polygon(
            np.array([-1, -1, 0]),
            np.array([1, -1, 0]),
            np.array([-1, 1, 0]),
            color=WHITE
        ).scale(scale_factor)
        right_label = Text("Right Angled Triangle", font_size=35).to_edge(UP)
        right_angle_text = Text("1 angle = 90°", font_size=25).next_to(right_triangle, DOWN)
        
        right_points = [right_triangle.get_vertices()[i] for i in range(3)]
        right_labels = [
            Text("P", font_size=24).move_to(right_points[0] + LEFT * 0.2 + DOWN * 0.2),
            Text("Q", font_size=24).move_to(right_points[1] + RIGHT * 0.2 + DOWN * 0.2),
            Text("R", font_size=24).move_to(right_points[2] + UP * 0.2),
        ]
        
        # Animation
        self.play(Write(acute_label))
        self.play(Create(acute_triangle))
        for label in acute_labels:
            self.play(Write(label))
        self.play(Write(acute_angle_text))
        self.wait(2)
        
        self.play(FadeOut(acute_triangle), FadeOut(acute_label), FadeOut(acute_angle_text))
        for label in acute_labels:
            self.play(FadeOut(label))
        
        self.play(Write(obtuse_label))
        self.play(Create(obtuse_triangle))
        for label in obtuse_labels:
            self.play(Write(label))
        self.play(Write(obtuse_angle_text))
        self.wait(2)
        
        self.play(FadeOut(obtuse_triangle), FadeOut(obtuse_label), FadeOut(obtuse_angle_text))
        for label in obtuse_labels:
            self.play(FadeOut(label))
        
        self.play(Write(right_label))
        self.play(Create(right_triangle))
        for label in right_labels:
            self.play(Write(label))
        self.play(Write(right_angle_text))
        self.wait(2)






    def triangles1155(self):
     

        # Create the vertices of the triangle
        A = np.array([2, 2, 0])
        B = np.array([-2, -2, 0])
        C = np.array([2, -2, 0])

        # Create the points
        point_A = Dot(A, color=BLUE)
        point_B = Dot(B, color=BLUE)
        point_C = Dot(C, color=BLUE)

        # Create the labels for the points
        label_A = Text("A").next_to(point_A, UP)
        label_B = Text("B").next_to(point_B, DOWN)
        label_C = Text("C").next_to(point_C, DOWN)

        # Create the triangle
        triangle = Polygon(A, B, C, color=WHITE)

        # Calculate the midpoint of BC
        M = (B + C) / 2

        # Create the midpoint and its label
        point_M = Dot(M, color=GREEN)
        label_M = Text("M").next_to(point_M, DOWN)

        # Create the median AM
        median = DashedLine(A, M, color=RED)

        # Add title
        title = Text("Median of the Triangle").to_edge(UP)

        # Add definition of median
        definition = Text(
            "Median: A line segment joining \na vertex to the midpoint \nof the opposite side.",
            font_size=24
        ).to_edge(LEFT)

        # Add elements to the scene
        self.add(title, triangle, point_A, point_B, point_C, point_M)
        self.add(label_A, label_B, label_C, label_M, definition)
        self.play(Create(triangle))
        self.play(Create(median))

        # Add conclusion text
        conclusion = Text("M is the median").to_edge(DOWN)
        self.play(Write(conclusion))

        # Wait before ending the scene
        self.wait(2)


    def triangles1122(self):
        p30=cvo.CVO().CreateCVO("relationship between sides of triangles","a,b,c").setPosition(-TAU/4)
        p31=cvo.CVO().CreateCVO("condition","$sum>c,diff<c$")
        p32=cvo.CVO().CreateCVO("sum","a+b,b+c,c+a")
        p33=cvo.CVO().CreateCVO("difference","a-b,b-c,c-a")

        p30.cvolist.append(p31)
        p30.cvolist.append(p32)
        p30.cvolist.append(p33)

        self.setNumberOfCirclePositions(4)
       
        self.construct1(p30,p30)

    def triangles1133(self):
     
        # Create the vertices of the triangle
        A = np.array([2, 2, 0])
        B = np.array([-2, -2, 0])
        C = np.array([2, -2, 0])

        # Create the points
        point_A = Dot(A, color=BLUE)
        point_B = Dot(B, color=BLUE)
        point_C = Dot(C, color=BLUE)

        # Create the labels for the points
        label_A = MathTex("A").next_to(point_A, UP)
        label_B = MathTex("B").next_to(point_B, DOWN)
        label_C = MathTex("C").next_to(point_C, DOWN)

        # Create the triangle
        triangle = Polygon(A, B, C, color=WHITE)

        # Define the angles
        angle_A = 60
        angle_B = 70
        angle_C = 50

        # Create the angle labels
        label_angle_A = MathTex(r"\angle A = 40^\circ").next_to(A, RIGHT)
        label_angle_B = MathTex(r"\angle B = 50^\circ").next_to(B, LEFT)
        label_angle_C = MathTex(r"\angle C = 90^\circ").next_to(C, RIGHT)

        # Create the title
        title = Text("Angle Sum Property of a Triangle").to_edge(UP)

        # Create the definition text
        definition = Text(
            "The sum of the interior angles\nof a triangle is always 180 degrees.",
            font_size=24
        ).to_edge(LEFT)

        # Add elements to the scene
        self.add(title, triangle, point_A, point_B, point_C)
        self.add(label_A, label_B, label_C)
        self.add(label_angle_A, label_angle_B, label_angle_C)
        self.add(definition)
        self.play(Create(triangle))

        # Add conclusion text
        conclusion = MathTex(r"60^\circ + 70^\circ + 50^\circ = 180^\circ").to_edge(DOWN)
        self.play(Write(conclusion))

        # Wait before ending the scene
        self.wait(2)

       
    
    def triangles1144(self):
      
    
        # Create the vertices of the triangle
        A = np.array([2, 2, 0])
        B = np.array([-2, -2, 0])
        C = np.array([2, -2, 0])

        # Create the points
        point_A = Dot(A, color=BLUE)
        point_B = Dot(B, color=BLUE)
        point_C = Dot(C, color=BLUE)

        # Create the labels for the points
        label_A = MathTex("A").next_to(point_A, UP)
        label_B = MathTex("B").next_to(point_B, DOWN)
        label_C = MathTex("C").next_to(point_C, DOWN)

        # Create the triangle
        triangle = Polygon(A, B, C, color=WHITE)

        # Extend side BC to form exterior angle at C
        extended_BC = Line(B, C + 2 * (C - B), color=WHITE)

        # Define the angles
        angle_A = 50 * DEGREES
        angle_B = 60 * DEGREES
        angle_C = 70 * DEGREES
        exterior_angle_C = angle_A + angle_B

        # Create the angle labels
        label_angle_A = MathTex(r"\angle A = 50^\circ").next_to(A, RIGHT)
        label_angle_B = MathTex(r"\angle B = 60^\circ").next_to(B, LEFT)
        label_angle_C = MathTex(r"\angle ACB").next_to(extended_BC, UP, buff=0.3)

        # Create the title
        title = Text("Exterior Angle Property of a Triangle").to_edge(UP)

        # Create the definition text and adjust its position
        definition = Text(
            "The measure of an exterior angle\n"
            "of a triangle is equal to the sum\n"
            "of the measures of the two\n"
            "non-adjacent interior angles.",
            font_size=24
        ).to_edge(LEFT, buff=0.5).shift(UP * 0.5)

        # Add elements to the scene
        self.add(title)
        self.play(Write(definition))

        # Create a group for the triangle and scale it down
        triangle_group = VGroup(triangle, point_A, point_B, point_C, label_A, label_B, label_C, extended_BC, label_angle_A, label_angle_B, label_angle_C)
        triangle_group.scale(0.6).to_edge(RIGHT)

        self.play(Create(triangle_group))

        # Show the conclusion about the exterior angle property in four lines on the left
        conclusion = VGroup(
            MathTex(r"\angle ACB = \angle A + \angle B", font_size=28),
            MathTex(r"\angle ACB = 50^\circ + 60^\circ", font_size=28),
            MathTex(r"\angle ACB = 110^\circ", font_size=28),
            MathTex(r"\therefore \angle ACB = 70^\circ", font_size=28)
        ).arrange(DOWN).to_edge(LEFT).shift(DOWN * 1.5)
        self.play(Write(conclusion))

        # Wait before ending the scene
        self.wait(2)

       
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="trianglesandproperties.py"

        
    def SetDeveloperList(self):  
        self.DeveloperList="Habeeb unissa"
        
if __name__ == "__main__":
    scene = trianglesAnim()
    scene.render()