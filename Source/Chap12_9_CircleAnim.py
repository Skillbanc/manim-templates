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

class CircleAnim(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.Circle()
        self.Circumference()
        self.Diameter()
        self.Arc()
        self.Segment()
        self.Sector()
        self.AngleSubtend()
        self.Theorem1()
        self.Theorem2()
        self.Theorem3()
        self.ArcSubtend()
        self.ArcSubtend2()
        self.ArcSubtend3()
        self.ArcSubtend4()
        self.cyclicQuad()
        self.Quad2()
        
        # self.fadeOut()
        # self.constructDataByJSON()
        # self.fadeOut()
        

    # render using CVO data object
    def Circle(self):
            self.isRandom = False
            self.angleChoice=[TAU/2]
            p10=cvo.CVO().CreateCVO("Circle","").setPosition([-4,2,0])
            p11=cvo.CVO().CreateCVO("Properties","").setPosition([-4,-2,0])
            p11onameList=["No Sides","Centre marked 'O'"]
            p10.cvolist.append(p11)
            p11.extendOname(p11onameList)
            self.setNumberOfCirclePositions(2)
            self.construct1(p10,p10)

            # Create a circle
            circle = Circle(radius=1, color=BLUE)

            # Move the circle to the center of the screen
            circle.move_to(ORIGIN)

            # Create animation to draw the circle
            self.play(Create(circle))

            # Add label 'O' at the center of the circle
            center=Dot(point=ORIGIN, color=GOLD)
            center_label = Tex("O").next_to(center, RIGHT)
            self.play(Create(center), Write(center_label))

            # Add properties of the circle
            properties = ["No Sides", "Centre marked 'O'"]
            property_text = VGroup(
                *[Text(prop).scale(0.5).next_to(circle, DOWN).shift(DOWN * (i * 0.3)) for i, prop in enumerate(properties)]
                )

            for text in property_text:
                    self.play(Write(text))

            # Wait for a moment
            self.wait(2)

            # Fade out the circle and the labels
            self.play(FadeOut(circle), FadeOut(center_label), FadeOut(property_text))
            self.fadeOutCurrentScene()


    
    def Circumference(self):
        self.isRandom = False
        self.angleChoice=[TAU/2]
        p10=cvo.CVO().CreateCVO("Circumference", "").setPosition([-4,2.5,0])
        p11=cvo.CVO().CreateCVO("Definition", "Complete length of a circle").setPosition([-4,-2.5,0])
        p10.cvolist.append(p11)
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)

        # Create a circle
        circle = Circle(radius=1, color=BLUE)

            # Move the circle to the center of the screen
        circle.move_to(ORIGIN)

            # Create animation to draw the circle
        self.play(Create(circle))

            # Add label for the circumference definition
        circumference_label = Tex("Circumference", color=YELLOW).next_to(circle, UP)
        definition_label = Tex("Complete length of a circle", color=RED).next_to(circle, DOWN)
        self.play(Write(circumference_label), Write(definition_label))

            # Wait for a moment
        self.wait(2)

            # Fade out the circle and the labels
        self.play(FadeOut(circle), FadeOut(circumference_label), FadeOut(definition_label))
        self.fadeOutCurrentScene()

    def Diameter(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Chord", "").setPosition([-3.5,2.5,0])
        p11=cvo.CVO().CreateCVO("Definition", "Line segment joining two points on a circle").setPosition([3.5,2.5,0])
        p12=cvo.CVO().CreateCVO("Diameter", "Line segment joining two points through center").setPosition([-3.5,-2.5,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)

         #create a circle
        circle = Circle(radius=1, color=BLUE).shift(RIGHT + DOWN)

        

            # Create animation to draw the circle
        self.play(Create(circle))
        

            # Draw a chord
        chord = Line(start=LEFT*1.5 + UP*1.5, end=RIGHT*1.5 + DOWN*1.5, color=RED).move_to(circle.get_center())
        self.play(Create(chord))

            # Wait for a moment
        self.wait(2)

            # Draw a diameter
        diameter = Line(start=LEFT*2, end=RIGHT*2, color=GREEN).move_to(circle.get_center())
        self.play(Transform(chord, diameter))

            # Wait for a moment
        self.wait(2)

            # Fade out the circle, chord/diameter, and the labels
        self.play(FadeOut(circle), FadeOut(chord),)


        self.fadeOutCurrentScene()
        

    def Arc(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Arc", "Part of circle between two points").setPosition([-3.5,2.5,0])
        p12=cvo.CVO().CreateCVO("Major Arc", "Arc larger than Semi-Circle").setPosition([3.5,2.5,0])
        p11=cvo.CVO().CreateCVO("Minor Arc", "Arc smaller than Semi-Circle").setPosition([-3.5,-2.5,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)


        circle = Circle(radius=2, color=BLUE).shift(RIGHT*3 + DOWN*1)
        
        self.play(Create(circle))

        point_A = circle.point_at_angle(PI/4)
        point_B = circle.point_at_angle(3*PI/4)
        center = circle.get_center()

            # Draw arcs of equal length
        arc_A = Arc(start_angle=PI/4, angle=PI/2, radius=2, color=RED, arc_center=center)
        arc_B = Arc(start_angle=3*PI/4, angle=-PI/2, radius=2, color=GREEN, arc_center=center)
        self.play(Create(arc_A), Create(arc_B))

            # Draw radii OA and OB
        radius_OA = Line(center, point_A, color=PURPLE)
        radius_OB = Line(center, point_B, color=PURPLE)
        self.play(Create(radius_OA), Create(radius_OB))

        angle_text_A = Tex("Minor Arc", color=ORANGE).scale(0.5).next_to(circle, UP)
        angle_text_B = Tex("Major Arc", color=ORANGE).scale(0.5).next_to(circle, DOWN)
        self.play(Write(angle_text_A), Write(angle_text_B))

        self.wait(2)

            # Fade out all elements
        self.play(FadeOut(circle), FadeOut(arc_A), FadeOut(arc_B), FadeOut(radius_OA), FadeOut(radius_OB), FadeOut(angle_text_A), FadeOut(angle_text_B))

    
        self.fadeOutCurrentScene()
        
    
    def Segment(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Segment", "Minor and Major")
        p11=cvo.CVO().CreateCVO("Minor", "Region between chord and minor arc")
        p12=cvo.CVO().CreateCVO("Major", "Region between chord and major arc")
        p13=cvo.CVO().CreateCVO("Exception", "If chord is diameter, circle split equally")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.setNumberOfCirclePositions(4)
        self.construct1(p10,p10)

         # Create a circle
        circle = Circle(radius=1, color=BLUE)
        circle.move_to(ORIGIN)
        self.play(Create(circle))

            # Create a chord
        chord = Line(circle.point_at_angle(PI/4), circle.point_at_angle(3*PI/4), color=RED)
        self.play(Create(chord))

        

        minor_label = Tex("Minor Segment", color=RED).scale(0.7).next_to(circle, UP)
        self.play(Write(minor_label))

        self.wait(2)

        major_label = Tex("Major Segment", color=GREEN).scale(0.7).next_to(circle, DOWN)
        self.play(Write(major_label))

        self.wait(2)

            # Draw exception (if chord is diameter)
        exception_label = Tex("Exception", color=PURPLE).scale(0.7).next_to(circle, RIGHT)
        self.play(Write(exception_label))

        diameter = Line(start=circle.point_at_angle(0), end=circle.point_at_angle(PI), color=PURPLE)
        self.play(Transform(chord, diameter))

        self.wait(2)

            # Fade out all elements
        self.play(FadeOut(circle), FadeOut(chord), FadeOut(minor_label), FadeOut(major_label), FadeOut(exception_label))

        self.fadeOutCurrentScene()
        

    def Sector(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Sector", "Region enclosed by an arc and two radii").setPosition([-3.5,2.5,0])
        p11=cvo.CVO().CreateCVO("Minor Sector", "").setPosition([4.5,2.5,0])
        p12=cvo.CVO().CreateCVO("Major Sector", "").setPosition([-3.5,-2.5,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)

        circle = Circle(radius=1, color=BLUE).shift(RIGHT*2 + DOWN*1)
        
        self.play(Create(circle))

            # Label for sector definition
        sector_label = Tex("", color=YELLOW).scale(0.7).to_edge(UP)
        self.play(Write(sector_label))

            # Create points for sectors
        start_angle = PI/4
        end_angle = 3*PI/4
        mid_angle = PI/2

            # Draw minor sector
        minor_sector = Sector(arc_center=circle.get_center(), angle=end_angle - start_angle, start_angle=start_angle, color=RED, fill_opacity=0.5)
        self.play(Create(minor_sector))

        minor_label = Tex("Minor Sector", color=RED).scale(0.7).next_to(circle, UP)
        self.play(Write(minor_label))

        self.wait(2)

            # Draw major sector
        major_sector = Sector(arc_center=circle.get_center(), angle=start_angle - end_angle + 2*PI, start_angle=end_angle, color=GREEN, fill_opacity=0.5)
        self.play(Create(major_sector))

        major_label = Tex("Major Sector", color=GREEN).scale(0.7).next_to(circle, DOWN)
        self.play(Write(major_label))

        self.wait(2)

            # Fade out all elements
        self.play(FadeOut(circle), FadeOut(minor_sector), FadeOut(major_sector), FadeOut(sector_label), FadeOut(minor_label), FadeOut(major_label))

        self.fadeOutCurrentScene()
        
    
    def AngleSubtend(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Angle Subtended by a Chord", "Central Angle created after joining two points").setPosition([-3.5,2.5,0])
        self.setNumberOfCirclePositions(1)
        self.construct1(p10,p10)

        circle = Circle(radius=1.5, color=BLUE)
        circle.move_to(ORIGIN)
        self.play(Create(circle))

            # Label for the angle subtended by a chord definition
        angle_label = Tex("", color=YELLOW).scale(0.7).next_to(circle, UP)
        self.play(Write(angle_label))

            # Create points on the circle
        point_A = circle.point_at_angle(PI/4)
        point_B = circle.point_at_angle(3*PI/4)
        center = circle.get_center()

            # Draw chord AB
        chord = Line(point_A, point_B, color=RED)
        self.play(Create(chord))

        pointAlabel = Tex("A").next_to(point_A, RIGHT)
        pointBlabel = Tex("B").next_to(point_B, LEFT)
        centerlabel = Tex("O").next_to(center, UP).scale(0.5)
        self.play(Create(pointAlabel),Create(pointBlabel), Create(centerlabel))

            # Draw radii OA and OB
        radius_OA = Line(center, point_A, color=GREEN)
        radius_OB = Line(center, point_B, color=GREEN)
        self.play(Create(radius_OA), Create(radius_OB))

            # Highlight the angle at the center
        central_angle = Angle(radius_OA, radius_OB, radius=0.5, color=ORANGE)
        self.play(Create(central_angle))

            # Angle label
        angle_text = Tex("Central Angle", color=ORANGE).scale(0.7).next_to(central_angle, DOWN)
        self.play(Write(angle_text))

        self.wait(2)

            # Fade out all elements
        self.play(FadeOut(circle), FadeOut(chord), FadeOut(radius_OA), FadeOut(radius_OB), FadeOut(central_angle),
                   FadeOut(angle_label), FadeOut(angle_text),FadeOut(pointAlabel),FadeOut(pointBlabel), FadeOut(centerlabel))

        self.fadeOutCurrentScene()

    def Theorem1(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Theorem", "Equal chords of a circle subtend equal angles at the centre").setPosition([-3.5,2.5,0])
        self.setNumberOfCirclePositions(1)
        self.construct1(p10,p10)

        circle = Circle(radius=2, color=BLUE)
        circle.move_to(ORIGIN)
        self.play(Create(circle))

            # Label for the theorem
        theorem_label = Tex("", color=YELLOW).scale(0.7).to_edge(UP)
        self.play(Write(theorem_label))

            # Create points on the circle
        point_A1 = circle.point_at_angle(PI/4)
        point_B1 = circle.point_at_angle(3*PI/4)
        point_A2 = circle.point_at_angle(-PI/4)
        point_B2 = circle.point_at_angle(-3*PI/4)
        center = circle.get_center()

            # Draw chords AB and CD
        chord_AB = Line(point_A1, point_B1, color=RED)
        chord_CD = Line(point_A2, point_B2, color=GREEN)
        self.play(Create(chord_AB), Create(chord_CD))

        pointA1label = Tex("A").next_to(point_A1, RIGHT)
        pointB1label = Tex("B").next_to(point_B1, LEFT)
        pointA2label = Tex("C").next_to(point_A2, RIGHT)
        pointB2label = Tex("D").next_to(point_B2, LEFT)
        centerlabel = Tex("O").next_to(center, RIGHT).scale(0.5)
        self.play(Create(pointA1label), Create(pointA2label), Create(pointB1label), Create(pointB2label), Create(centerlabel))

            # Draw radii OA, OB, OC, and OD
        radius_OA = Line(center, point_A1, color=PURPLE)
        radius_OB = Line(center, point_B1, color=PURPLE)
        radius_OC = Line(center, point_A2, color=ORANGE)
        radius_OD = Line(center, point_B2, color=ORANGE)
        self.play(Create(radius_OA), Create(radius_OB), Create(radius_OC), Create(radius_OD))

            # Highlight the angles at the center
        central_angle_AOB = Angle(radius_OA, radius_OB, radius=0.5, color=ORANGE)
        central_angle_COD = Angle(radius_OC, radius_OD, radius=0.5, color=YELLOW)
        self.play(Create(central_angle_AOB), Create(central_angle_COD))

            # Angle labels
        angle_text_AOB = Tex("Angle AOB", color=ORANGE).scale(0.5).next_to(central_angle_AOB, UP)
        angle_text_COD = Tex("Angle COD", color=YELLOW).scale(0.5).next_to(central_angle_COD, DOWN)
        self.play(Write(angle_text_AOB), Write(angle_text_COD))

        self.wait(2)

            # Fade out all elements
        self.play(FadeOut(circle), FadeOut(chord_AB), FadeOut(chord_CD), FadeOut(radius_OA), FadeOut(radius_OB),
                   FadeOut(radius_OC), FadeOut(radius_OD), FadeOut(central_angle_AOB), FadeOut(central_angle_COD), 
                   FadeOut(theorem_label), FadeOut(angle_text_AOB), FadeOut(angle_text_COD)
                   ,FadeOut(pointA1label), FadeOut(pointA2label), FadeOut(pointB1label), FadeOut(pointB2label), FadeOut(centerlabel))


        self.fadeOutCurrentScene()

    def Theorem2(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Theorem", "Chords are equal if angle subtended at centre are also equal").setPosition([-3.5,2.5,0])
        self.setNumberOfCirclePositions(1)
        self.construct1(p10,p10)

        circle = Circle(radius=2, color=BLUE)
        circle.move_to(ORIGIN)
        self.play(Create(circle))

            # Label for the theorem
        theorem_label = Tex("", color=YELLOW).scale(0.7).to_edge(UP)
        self.play(Write(theorem_label))

            # Create points on the circle
        point_A1 = circle.point_at_angle(PI/4)
        point_B1 = circle.point_at_angle(3*PI/4)
        point_A2 = circle.point_at_angle(-PI/4)
        point_B2 = circle.point_at_angle(-3*PI/4)
        center = circle.get_center()

            # Draw chords AB and CD
        chord_AB = Line(point_A1, point_B1, color=RED)
        chord_CD = Line(point_A2, point_B2, color=GREEN)
        self.play(Create(chord_AB), Create(chord_CD))

        pointA1label = Tex("A").next_to(point_A1, RIGHT)
        pointB1label = Tex("B").next_to(point_B1, LEFT)
        pointA2label = Tex("C").next_to(point_A2, RIGHT)
        pointB2label = Tex("D").next_to(point_B2, LEFT)
        centerlabel = Tex("O").next_to(center, RIGHT).scale(0.5)
        self.play(Create(pointA1label), Create(pointA2label), Create(pointB1label), Create(pointB2label), Create(centerlabel))


            # Draw radii OA, OB, OC, and OD
        radius_OA = Line(center, point_A1, color=PURPLE)
        radius_OB = Line(center, point_B1, color=PURPLE)
        radius_OC = Line(center, point_A2, color=ORANGE)
        radius_OD = Line(center, point_B2, color=ORANGE)
        self.play(Create(radius_OA), Create(radius_OB), Create(radius_OC), Create(radius_OD))

            # Highlight the angles at the center
        central_angle_AOB = Angle(radius_OA, radius_OB, radius=0.5, color=ORANGE)
        central_angle_COD = Angle(radius_OC, radius_OD, radius=0.5, color=YELLOW)
        self.play(Create(central_angle_AOB), Create(central_angle_COD))

            # Angle labels
        angle_text_AOB = Tex("Angle AOB", color=ORANGE).scale(0.5).next_to(central_angle_AOB, UP)
        angle_text_COD = Tex("Angle COD", color=YELLOW).scale(0.5).next_to(central_angle_COD, DOWN)
        self.play(Write(angle_text_AOB), Write(angle_text_COD))

        self.wait(2)

            # Fade out all elements
        self.play(FadeOut(circle), FadeOut(chord_AB), FadeOut(chord_CD), FadeOut(radius_OA), FadeOut(radius_OB), 
                  FadeOut(radius_OC), FadeOut(radius_OD), FadeOut(central_angle_AOB), FadeOut(central_angle_COD), 
                  FadeOut(theorem_label), FadeOut(angle_text_AOB), FadeOut(angle_text_COD),
                  FadeOut(pointA1label), FadeOut(pointA2label), FadeOut(pointB1label), FadeOut(pointB2label), FadeOut(centerlabel))


        self.fadeOutCurrentScene()
    
    def Theorem3(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Theorem", "Perpendicular from centre to a chord bisects the chord").setPosition([-3.5,2.5,0])
        self.setNumberOfCirclePositions(1)
        self.construct1(p10,p10)

        circle = Circle(radius=2, color=BLUE)
        circle.move_to(ORIGIN)
        self.play(Create(circle))

            # Label for the theorem
        theorem_label = Tex("", color=YELLOW).scale(0.7).to_edge(UP)
        self.play(Write(theorem_label))

            # Create points on the circle
        point_A = circle.point_at_angle(PI/4)
        point_B = circle.point_at_angle(3*PI/4)
        center = circle.get_center()

            # Draw chord AB
        chord = Line(point_A, point_B, color=RED)
        self.play(Create(chord))

        pointAlabel = Tex("A").next_to(point_A, RIGHT)
        pointBlabel = Tex("B").next_to(point_B, LEFT)
        centerlabel = Tex("O").next_to(center, RIGHT)
        self.play(Create(pointAlabel),Create(pointBlabel), Create(centerlabel))

            # Draw radii OA and OB
        radius_OA = Line(center, point_A, color=PURPLE)
        radius_OB = Line(center, point_B, color=PURPLE)
        self.play(Create(radius_OA), Create(radius_OB))

            # Find midpoint of chord AB
        midpoint_AB = (point_A + point_B) / 2
        midpoint_dot = Dot(midpoint_AB, color=GREEN)
        midpointlabel = Tex("M").next_to(midpoint_AB, UP)
        self.play(Create(midpoint_dot), Create(midpointlabel))

            # Draw perpendicular from center to chord AB
        perpendicular = Line(center, midpoint_AB, color=ORANGE)
        self.play(Create(perpendicular))

            # Mark lengths to show bisecting
        perpend = Tex("Perpendicular bisects chord", color=YELLOW).scale(0.5).next_to(midpoint_dot, DOWN)
        chordbisect = Tex("", color=YELLOW).scale(0.5).next_to(perpendicular, DOWN)
        self.play(Write(perpend), Write(chordbisect))

        self.wait(2)

            # Fade out all elements
        self.play(FadeOut(circle), FadeOut(chord), FadeOut(radius_OA), FadeOut(radius_OB), 
                  FadeOut(perpendicular), FadeOut(midpoint_dot), FadeOut(theorem_label), FadeOut(perpend), FadeOut(chordbisect),
                  FadeOut(pointAlabel),FadeOut(pointBlabel), FadeOut(centerlabel), FadeOut(midpointlabel))


        self.fadeOutCurrentScene()
    
    def ArcSubtend(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Statement", "Arcs of equal length subtend equal angles at centre").setPosition([-3.5,2.5,0])
        self.setNumberOfCirclePositions(1)
        self.construct1(p10,p10)

# Create a circle
        circle = Circle(radius=2, color=BLUE)
        circle.move_to(ORIGIN)
        self.play(Create(circle))

            # Label for the statement
        statement_label = Tex("", color=YELLOW).scale(0.7).to_edge(UP)
        self.play(Write(statement_label))

            # Create points on the circle
        point_A = circle.point_at_angle(PI/4)
        point_B = circle.point_at_angle(3 * PI/4)
        Point_C = circle.point_at_angle(7 * PI/4)
        center = circle.get_center()

            # Draw arcs of equal length
        arc_A = Arc(start_angle=PI/4, angle=PI/2, radius=2, color=RED, arc_center=center)
        arc_B = Arc(start_angle=PI/4, angle=-PI/2, radius=2, color=GREEN, arc_center=center)
        arc_C = Arc(start_angle=7 * PI/4, angle=-PI, radius=2, arc_center=center)
        self.play(Create(arc_A), Create(arc_B), Create(arc_C))

        pointAlabel = Tex("A").next_to(point_A, RIGHT)
        pointBlabel = Tex("B").next_to(point_B, LEFT)
        pointClabel = Tex("C").next_to(Point_C, RIGHT)
        centerlabel = Tex("O").next_to(center, DOWN).scale(0.5)
        self.play(Create(pointAlabel),Create(pointBlabel), Create(pointClabel), Create(centerlabel))

            # Draw radii OA and OB
        radius_OA = Line(center, point_A, color=PURPLE)
        radius_OB = Line(center, point_B, color=PURPLE)
        radius_OC = Line(center, Point_C, color = PURPLE)
        self.play(Create(radius_OA), Create(radius_OB), Create(radius_OC))

            # Draw central angles
        central_angle_A = Angle(radius_OA, Line(center, arc_A.points[-1]), color=ORANGE)
        central_angle_B = Angle(radius_OB, Line(center, arc_B.points[1]), color=PINK)
        
        self.play(Create(central_angle_A), Create(central_angle_B))

            # Angle labels
        angle_text_A = Tex("Angle subtended=AOB", color=ORANGE).scale(0.5).next_to(central_angle_A, UP)
        angle_text_B = Tex("Angle subtended=BOC", color=ORANGE).scale(0.5).next_to(central_angle_B, RIGHT)
        self.play(Write(angle_text_A), Write(angle_text_B))

        self.wait(2)

            # Fade out all elements
        self.play(FadeOut(circle), FadeOut(arc_A), FadeOut(arc_B),FadeOut(arc_C), FadeOut(radius_OA), FadeOut(radius_OB), FadeOut(radius_OC), FadeOut(central_angle_A), FadeOut(central_angle_B), FadeOut(statement_label), FadeOut(angle_text_A), FadeOut(angle_text_B))

        self.fadeOutCurrentScene()
    
    def ArcSubtend2(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Theorem", "The angle subtended by an arc at the centre 'O' is twice the angle subtended by it on the remaining arc of the circle")
        self.setNumberOfCirclePositions(1)
        p10.setcircleradius(2)
        self.construct1(p10,p10)
        
        self.fadeOutCurrentScene()

    def ArcSubtend3(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Theorem", "Angles subtended by an arc in the same segment are equal")
        self.setNumberOfCirclePositions(1)
        p10.setcircleradius(2)
        self.construct1(p10,p10)

        self.fadeOutCurrentScene()

    def ArcSubtend4(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Theorem", "Points are concylic if line segment joining two points, subtends equal angles at two other points lying on the same side of the line")
        self.setNumberOfCirclePositions(1)
        p10.setcircleradius(2)
        self.construct1(p10,p10)

        self.fadeOutCurrentScene()

    def cyclicQuad(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Cyclic Quadrilateral", "").setPosition([-4,2.5,0])
        p12=cvo.CVO().CreateCVO("Property", "Opposite angles are supplementary").setPosition([-4,-2.5,0])
        p11=cvo.CVO().CreateCVO("Definition", "A quadrilateral with all 4 sides and vertices inside the circle").setPosition([4,2.5,0])
        self.setNumberOfCirclePositions(2)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)

        circle = Circle(radius=1.5, color=BLUE).shift(RIGHT*2 + DOWN*1)
        
        self.play(Create(circle))

            # Label for the theorem
        theorem_label = Tex("Cyclic Quadrilateral", color=YELLOW).scale(0.7).next_to(circle, DOWN)
        self.play(Write(theorem_label))

            # Create points on the circle
        point_A = circle.point_at_angle(PI/4)
        point_B = circle.point_at_angle(3*PI/4)
        point_C = circle.point_at_angle(5*PI/4)
        point_D = circle.point_at_angle(7*PI/4)
        center = circle.get_center()

            # Draw the cyclic quadrilateral ABCD
        quad_ABCD = Polygon(point_A, point_B, point_C, point_D, color=GREEN)
        self.play(Create(quad_ABCD))

            # Draw the circle
        self.play(Create(circle))

            

            # Angle labels
        angle_text_A = Tex("A", color=ORANGE).scale(0.5).next_to(point_A, RIGHT)
        angle_text_B = Tex("B", color=ORANGE).scale(0.5).next_to(point_B, LEFT)
        angle_text_C = Tex("C", color=ORANGE).scale(0.5).next_to(point_C, LEFT)
        angle_text_D = Tex("D", color=ORANGE).scale(0.5).next_to(point_D, RIGHT)
        self.play(Write(angle_text_A), Write(angle_text_B), Write(angle_text_C), Write(angle_text_D))

        self.wait(2)

            # Fade out all elements
        self.play(FadeOut(circle), FadeOut(quad_ABCD), FadeOut(angle_text_A), FadeOut(angle_text_B), FadeOut(angle_text_C), FadeOut(angle_text_D), FadeOut(theorem_label))


        self.fadeOutCurrentScene()

        

    def Quad2(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Theorem", "If sum of any pair of opposite angles are supplementary, it is cyclic").setPosition([-3.5,2.5,0])
        self.setNumberOfCirclePositions(1)
        self.construct1(p10,p10)

        circle = Circle(radius=1.5, color=BLUE)
        circle.move_to(ORIGIN)
        self.play(Create(circle))

            # Label for the theorem
        theorem_label = Tex("", color=YELLOW).scale(0.7).next_to(circle, UP)
        self.play(Write(theorem_label))

            # Create points on the circle
        point_A = circle.point_at_angle(PI/4)
        point_B = circle.point_at_angle(3*PI/4)
        point_C = circle.point_at_angle(5*PI/4)
        point_D = circle.point_at_angle(7*PI/4)
        center = circle.get_center()

            # Draw the cyclic quadrilateral ABCD
        quad_ABCD = Polygon(point_A, point_B, point_C, point_D, color=GREEN)
        self.play(Create(quad_ABCD))

            # Draw the circle
        self.play(Create(circle))

            

            # Angle labels
        angle_text_A = Tex("A", color=ORANGE).scale(0.5).next_to(point_A, RIGHT)
        angle_text_B = Tex("B", color=ORANGE).scale(0.5).next_to(point_B, LEFT)
        angle_text_C = Tex("C", color=ORANGE).scale(0.5).next_to(point_C, LEFT)
        angle_text_D = Tex("D", color=ORANGE).scale(0.5).next_to(point_D, RIGHT)
        self.play(Write(angle_text_A), Write(angle_text_B), Write(angle_text_C), Write(angle_text_D))

        self.wait(2)

            # Fade out all elements
        self.play(FadeOut(circle), FadeOut(quad_ABCD), FadeOut(angle_text_A), FadeOut(angle_text_B), FadeOut(angle_text_C), FadeOut(angle_text_D), FadeOut(theorem_label))

        self.fadeOutCurrentScene()


    


if __name__ == "__main__":
    scene = CircleAnim()
    scene.render()