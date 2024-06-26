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

class Length4G(AbstractAnim):
    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.LineSegment()
        self.fadeOutCurrentScene()
        self.Anim1()        
        self.fadeOutCurrentScene()
        self.Triangle()
        self.fadeOutCurrentScene()
        self.Type1()
        self.fadeOutCurrentScene()
        self.Anim2()
        self.fadeOutCurrentScene()
        self.Type2()
        self.fadeOutCurrentScene()
        self.Anim3()
        self.fadeOutCurrentScene()
        self.Type3()
        self.fadeOutCurrentScene()
        self.Anim4()
        self.fadeOutCurrentScene()
        self.Type4()
        self.fadeOutCurrentScene()
        self.Anim5()
        self.fadeOutCurrentScene()
        
    # render using CVO data object 
    
    def Length(self):
        self.isRandom=False
        self.positionChoice=[[-4,0,0],[4,0,0]]
        p10=cvo.CVO().CreateCVO("Length","Measurement")
        p11=cvo.CVO().CreateCVO("Types","cm\\\\m\\\\inches")
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def Anim1(self):
        # Title
        title = Text("Measurement Rulers: cm and inches", font_size=48)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Ruler length in centimeters (1 meter = 100 cm)
        ruler_length_cm = 100
        cm_to_inch = 2.54
        ruler_length_inch = int(ruler_length_cm / cm_to_inch)
        
        # Define scale factor for visualization
        scale_factor = 0.1

        # Draw the centimeter ruler
        cm_ruler = Line(start=ORIGIN, end=RIGHT * ruler_length_cm * scale_factor, stroke_width=2).move_to(UP)
        self.play(Create(cm_ruler))
        
        # Draw centimeter markings on the top ruler
        cm_marks = VGroup()
        for i in range(0, ruler_length_cm + 1):
            if i % 10 == 0:
                mark_length = 0.4
            else:
                mark_length = 0.2
            mark = Line(start=UP * mark_length, end=ORIGIN).move_to(cm_ruler.point_from_proportion(i / ruler_length_cm))
            cm_marks.add(mark)
        self.play(*[Create(mark) for mark in cm_marks])
        
        # Add centimeter labels every 10 cm on the top ruler
        cm_labels = VGroup()
        for i in range(0, ruler_length_cm + 1, 10):
            label = Text(f"{i} cm", font_size=24).next_to(cm_marks[i], UP)
            cm_labels.add(label)
        self.play(*[Write(label) for label in cm_labels])
        
        # Draw the inch ruler
        inch_ruler = Line(start=ORIGIN, end=RIGHT * ruler_length_cm * scale_factor, stroke_width=2).next_to(cm_ruler, DOWN, buff=1)
        self.play(Create(inch_ruler))
        
        # Draw inch markings on the bottom ruler
        inch_marks = VGroup()
        for i in range(0, ruler_length_inch + 1):
            if i % 2 == 0:
                mark_length = 0.3
            else:
                mark_length = 0.15
            proportion = i * cm_to_inch / ruler_length_cm
            if proportion <= 1:  # Ensure the proportion is within the ruler's length
                mark = Line(start=DOWN * mark_length, end=ORIGIN).move_to(inch_ruler.point_from_proportion(proportion))
                inch_marks.add(mark)
        self.play(*[Create(mark) for mark in inch_marks])
        
        # Add inch labels every inch on the bottom ruler
        inch_labels = VGroup()
        for i in range(0, ruler_length_inch + 1, 1):
            proportion = i * cm_to_inch / ruler_length_cm
            if proportion <= 1:  # Ensure the proportion is within the ruler's length
                label = Text(f"{i}\nin", font_size=12).next_to(inch_ruler.point_from_proportion(proportion), DOWN)
                inch_labels.add(label)
        self.play(*[Write(label) for label in inch_labels])
        
        # Add meter label at the end of the centimeter ruler
        meter_label = Text(f"1 meter", font_size=36).next_to(cm_ruler.get_end(), UP, buff=0.5).shift(RIGHT+DOWN)
        self.play(Write(meter_label))
        
        self.wait(2)
        
        # Fade out all elements
        all_elements = VGroup(cm_ruler, cm_marks, cm_labels, inch_ruler, inch_marks, inch_labels, meter_label)
        self.play(FadeOut(all_elements))
        self.wait(1)

    def Anim2(self):
        title = Text("Measuring a pencil").to_edge(UP)
        self.play(Write(title))
        ruler_length_cm = 15
        
        # Define scale factor for visualization
        scale_factor = 0.2

        # Draw the centimeter ruler
        cm_ruler = Line(start=ORIGIN, end=RIGHT * ruler_length_cm * scale_factor, stroke_width=2).move_to(UP * 1.5)
        self.play(Create(cm_ruler))
        
        # Draw centimeter markings on the top ruler
        cm_marks = VGroup()
        for i in range(0, ruler_length_cm + 1):
            if i % 5 == 0:
                mark_length = 0.4
            else:
                mark_length = 0.2
            mark = Line(start=UP * mark_length, end=ORIGIN).move_to(cm_ruler.point_from_proportion(i / ruler_length_cm))
            cm_marks.add(mark)
        self.play(*[Create(mark) for mark in cm_marks])
        
        # Add centimeter labels every 5 cm on the top ruler
        cm_labels = VGroup()
        for i in range(0, ruler_length_cm + 1, 5):
            label = Text(f"{i} cm", font_size=24).next_to(cm_marks[i], UP)
            cm_labels.add(label)
        self.play(*[Write(label) for label in cm_labels])
        
        # Draw inch ruler below centimeter ruler
        inch_ruler = Line(start=ORIGIN, end=RIGHT * ruler_length_cm * scale_factor, stroke_width=2).next_to(cm_ruler, DOWN, buff=1.5)
        self.play(Create(inch_ruler))
        
        # Draw inch markings on the bottom ruler
        inch_marks = VGroup()
        inch_length = 15 / 2.54
        for i in range(0, int(inch_length) + 1):
            if i % 2 == 0:
                mark_length = 0.3
            else:
                mark_length = 0.15
            proportion = i * 2.54 / ruler_length_cm
            if proportion <= 1:  # Ensure the proportion is within the ruler's length
                mark = Line(start=DOWN * mark_length, end=ORIGIN).move_to(inch_ruler.point_from_proportion(proportion))
                inch_marks.add(mark)
        self.play(*[Create(mark) for mark in inch_marks])
        
        # Add inch labels every inch on the bottom ruler
        inch_labels = VGroup()
        for i in range(0, int(inch_length) + 1, 1):
            proportion = i * 2.54 / ruler_length_cm
            if proportion <= 1:  # Ensure the proportion is within the ruler's length
                label = Text(f"{i}\nin", font_size=16).next_to(inch_ruler.point_from_proportion(proportion), DOWN)
                inch_labels.add(label)
        self.play(*[Write(label) for label in inch_labels])

        # Draw the pencil with a simple triangular nib
        pencil_length_cm = 10  # Length of the pencil in cm
        pencil_body = Rectangle(height=0.2, width=(pencil_length_cm - 1) * scale_factor, color=BLUE, fill_opacity=1)
        pencil_nib = Polygon(
            pencil_body.get_right()+UP*0.1,
            pencil_body.get_right() + RIGHT * 0.5 * scale_factor, 
            pencil_body.get_right() + DOWN * 0.1, 
            color=ORANGE, fill_opacity=1
        )
        pencil = VGroup(pencil_body, pencil_nib)
        pencil.next_to(cm_ruler, DOWN, buff=0.3)  # Position the pencil below the ruler
        pencil.shift(LEFT * 0.5)  # Shift pencil to start from 0 cm mark
        self.play(FadeIn(pencil))

        # Show measurement label
        measurement_label = Text(f"{pencil_length_cm} cm", font_size=24, color=YELLOW)
        measurement_label.next_to(pencil, DOWN, buff=0.1)
        self.play(Write(measurement_label))

        self.wait(2)
        
        # Fade out all elements
        all_elements = VGroup(cm_ruler, cm_marks, cm_labels, inch_ruler, inch_marks, inch_labels, pencil, measurement_label)
        self.play(FadeOut(all_elements))
        self.wait(1)



    def Type2(self):
        self.isRandom=False
        self.positionChoice=[[-4,0,0],[4,2,0],[4,-2,0]]
        p10=cvo.CVO().CreateCVO("SAS","").setangle(-TAU/4)
        p11=cvo.CVO().CreateCVO("Abbreviation","Side-Angle-Side")
        p12=cvo.CVO().CreateCVO("Rule","")
        p12onameList=["2 sides equal","angle b/w equal"]

        p12.setcircleradius(1.5)
        p11.setcircleradius(1.5)

        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p12.extendOname(p12onameList)
        self.construct1(p10,p10)

    def Anim3(self):
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
        sas_rule = Text("Side-Angle-Side (SAS) Rule").to_edge(UP)

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

    def Type3(self):
        self.isRandom=False
        self.positionChoice=[[-4,0,0],[4,2,0],[4,-2,0]]
        p10=cvo.CVO().CreateCVO("ASA","").setangle(-TAU/4)
        p11=cvo.CVO().CreateCVO("Abbreviation","Angle-Side-Angle")
        p12=cvo.CVO().CreateCVO("Rule","")
        p12onameList=["2 angles equal","side b/w equal"]

        p12.setcircleradius(1.5)
        p11.setcircleradius(1.5)

        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p12.extendOname(p12onameList)
        self.construct1(p10,p10)

    def Anim4(self):
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
        asa_rule = Text("Angle-Side-Angle (ASA) Rule").to_edge(UP)

        # Angle labels
        angle1_label = MathTex(r"\alpha").move_to(triangle1.get_vertices()[1] + 0.6 * LEFT + 0.4 * UP)
        angle2_label = MathTex(r"\beta").move_to(triangle1.get_vertices()[0] + 0.6 * RIGHT + 0.4 * UP)

        angle3_label = MathTex(r"\alpha").move_to(triangle2.get_vertices()[1] + 0.6 * LEFT + 0.4 * UP)
        angle4_label = MathTex(r"\beta").move_to(triangle2.get_vertices()[0] + 0.6 * RIGHT + 0.4 * UP)

        # Angle arcs
        angle1_arc = Arc(radius=0.5, start_angle=90, angle=np.pi/3).move_arc_center_to(triangle1.get_vertices()[1])
        angle2_arc = Arc(radius=0.5, start_angle=66*DEGREES, angle=-np.pi/3).move_arc_center_to(triangle1.get_vertices()[0])

        angle3_arc = Arc(radius=0.5, start_angle=90, angle=np.pi/3).move_arc_center_to(triangle2.get_vertices()[1])
        angle4_arc = Arc(radius=0.5, start_angle=66*DEGREES, angle=-np.pi/3).move_arc_center_to(triangle2.get_vertices()[0])

        # Side lengths
        side1 = Text("a").next_to(Line(triangle1.get_vertices()[0], triangle1.get_vertices()[1]).get_center(), DOWN)
        side2 = Text("a").next_to(Line(triangle2.get_vertices()[0], triangle2.get_vertices()[1]).get_center(), DOWN)

        # Animate the creation of elements
        self.play(Write(asa_rule))
        self.play(Create(triangle1), Write(label1_A), Write(label1_B), Write(label1_C))
        self.play(Create(triangle2), Write(label2_D), Write(label2_E), Write(label2_F))
        self.play(Create(angle1_arc), Create(angle2_arc),Write(angle1_label), Write(angle2_label) )
        self.play(Create(angle3_arc), Create(angle4_arc), Write(angle3_label), Write(angle4_label))
        self.play(Write(side1))
        self.play(Write(side2))

        self.wait(2)
        
        # Animate merging the triangles
        self.play(
            triangle2.animate.move_to(triangle1.get_center()),
            FadeOut(label2_D),
            FadeOut(label2_E),
            FadeOut(label2_F),
            FadeOut(angle3_arc),
            FadeOut(angle4_arc),
            FadeOut(angle3_label),
            FadeOut(angle4_label),
            FadeOut(side2),
            FadeOut(label1_A),
            FadeOut(label1_B),
            FadeOut(label1_C)
        )

        self.wait(2)


    def Type4(self):
        self.isRandom=False
        self.positionChoice=[[-4,0,0],[4,1.5,0],[4,-2,0]]
        p10=cvo.CVO().CreateCVO("RAH","").setangle(-TAU/4)
        p11=cvo.CVO().CreateCVO("Abbreviation","Right-Angle-Hypotenuse")
        p12=cvo.CVO().CreateCVO("Rule","")
        p12onameList=["Hypotenuse equal","another side equal"]

        p12.setcircleradius(2)
        p11.setcircleradius(1.8)

        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p12.extendOname(p12onameList)
        self.construct1(p10,p10)

    def Anim5(self):
        triangle1_vert = [[-2, 0, 0], [2, 0, 0], [-2, 2, 0]] 
        triangle2_vert = [[-2, 0, 0], [2, 0, 0], [-2, 2, 0]]

        # Create triangles
        triangle1 = Polygon(*triangle1_vert, color=BLUE)
        triangle2 = Polygon(*triangle2_vert, color=GREEN)

        # Shift triangles
        triangle1.shift(3 * LEFT + 2 * DOWN)
        triangle2.shift(3 * RIGHT + 2 * DOWN)

        # Labels for vertices
        label1_A = Text("A").next_to(triangle1.get_vertices()[0], LEFT)
        label1_B = Text("B").next_to(triangle1.get_vertices()[1], RIGHT)
        label1_C = Text("C").next_to(triangle1.get_vertices()[2], UP)

        label2_D = Text("D").next_to(triangle2.get_vertices()[0], LEFT)
        label2_E = Text("E").next_to(triangle2.get_vertices()[1], RIGHT)
        label2_F = Text("F").next_to(triangle2.get_vertices()[2], UP)

        # Rule text
        rhs_rule = Text("Right-Angle-Hypotenuse-Side (RHS) Rule").to_edge(UP)

        # Right angle squares
        right_angle1 = Square(side_length=0.5).move_to(triangle1.get_vertices()[0] + np.array([0.25, 0.25, 0]))
        right_angle2 = Square(side_length=0.5).move_to(triangle2.get_vertices()[0] + np.array([0.25, 0.25, 0]))

        # Side lengths
        hypotenuse1 = Text("c").next_to(Line(triangle1.get_vertices()[1], triangle1.get_vertices()[2]).get_center(), RIGHT)
        side1 = Text("a").next_to(Line(triangle1.get_vertices()[0], triangle1.get_vertices()[2]).get_center(), LEFT)
        
        hypotenuse2 = Text("c").next_to(Line(triangle2.get_vertices()[1], triangle2.get_vertices()[2]).get_center(), RIGHT)
        side2 = Text("a").next_to(Line(triangle2.get_vertices()[0], triangle2.get_vertices()[2]).get_center(), LEFT)

        # Animate the creation of elements
        self.play(Write(rhs_rule))
        self.play(Create(triangle1), Write(label1_A), Write(label1_B), Write(label1_C) )
        self.play(Create(triangle2), Write(label2_D), Write(label2_E), Write(label2_F))
        self.play(Create(right_angle1), Write(hypotenuse1), Write(side1))
        self.play(Create(right_angle2), Write(hypotenuse2), Write(side2))

        self.wait(2)
        
        # Animate merging the triangles
        self.play(
            triangle2.animate.move_to(triangle1.get_center()),
            FadeOut(label2_D),
            FadeOut(label2_E),
            FadeOut(label2_F),
            FadeOut(right_angle2),
            FadeOut(hypotenuse2),
            FadeOut(side2),
            FadeOut(side1),
            FadeOut(label1_A),
            FadeOut(label1_B),
            FadeOut(label1_C)
        )

        self.wait(2)

        
   
               
if __name__ == "__main__":
    scene = Length4G()
    scene.render()
    