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


class PracticalGeometryIntroduction(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.Title()
        self.fadeOutCurrentScene()
        self.intro()
        self.fadeOutCurrentScene()
        self.linesegment()
        self.fadeOutCurrentScene()
        self.RulerMethod()
        self.fadeOutCurrentScene()
        self.CompassMethod()
        self.fadeOutCurrentScene()
        self.ConstructCircleWithCompass()
        self.fadeOutCurrentScene()
        self.Perpendiculars()
        self.fadeOutCurrentScene()
        self.PerpendicularBisector()
        self.fadeOutCurrentScene()
        self.Construct40DegreeAngle()
        self.fadeOutCurrentScene()
        self.CopyAngleWithCompass()
        self.fadeOutCurrentScene()
        self.Bisect()
        self.fadeOutCurrentScene()
        self.Compass60degree()
        self.fadeOutCurrentScene()
        self.CON120deg()
        self.fadeOutCurrentScene()
        self.con90degree()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()





    def Title(self):
        # Title
        title = Text("Practical Geometry ", font_size=70)
        self.play(Write(title))
        self.wait(4)
        self.play(Unwrite(title))
        self.wait(2)
        
        #introduction
    def intro(self):    
        title = Text("Introduction ", font_size=40).shift(UP * 3.5)
      
        # Create a group
        group = VGroup( title)

        self.add(group)
        self.wait(2)


        # Right-angled diagram
        right_angle = Polygon(
            ORIGIN, 
            [3, 0, 0], 
            [3, 3, 0], 
            color=BLUE, 
            fill_opacity=2
        )
        right_angle_label = MathTex(r"\angle ABC = 90^\circ", font_size=45)
        right_angle_label.next_to(right_angle, DOWN)
        self.play(DrawBorderThenFill(right_angle), Write(right_angle_label))
        self.wait(3)


        # Circle at (1, 1)
        circle_diagonal = Circle(radius=1.6, color=YELLOW)
        circle_diagonal.move_to([-2, 1, 0])
        circle_diagonal_label = MathTex(r"circle", font_size=37)
        circle_diagonal_label.next_to(circle_diagonal, DOWN)
        self.play(DrawBorderThenFill(circle_diagonal), Write(circle_diagonal_label))
        self.wait(3)

          #line
         
        line1 = Line(start=DOWN* 2 + LEFT * 0, end=UP * 2 + LEFT * 0, color=PINK).shift(LEFT*4.6)
        self.add( line1)
        self.play(Write(line1))

        title = Text("Line", font_size=40,color =WHITE).shift(LEFT* 4.7 +DOWN*2.1)
        

        # Create a group
        group = VGroup( title)

        self.add(group)
        self.play(Write(title))
        self.wait(5)


        self.fadeOutCurrentScene()
        self.colorChoice = [BLUE,ORANGE,WHITE,YELLOW]
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
        p10=cvo.CVO().CreateCVO("Geometry Tools"," \n\n\n\n.  ").setPosition([0,2,0])
        # p11=cvo.CVO().CreateCVO("triangles","").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("Compass","").setPosition([5,-2.1,0])
        # p13=cvo.CVO().CreateCVO("rhombus","").setPosition([-4,2,0]).setangle(-TAU/4)
        p14=cvo.CVO().CreateCVO("Divider","").setPosition([-5,-2.2,0]).setangle(-TAU/4)
        p15=cvo.CVO().CreateCVO("Protractor","").setPosition([0,-2.2,0]).setangle(-TAU/6)

        p10.cvolist.append(p12)
       #  p10.cvolist.append(p11)
       #  p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        self.construct1(p10,p10)
        self.wait(2)

        p10.setcircleradius(3)
        self.wait(4)

      

################################################


#line segment
    def linesegment(self):



        # Create points A and B
        A = Dot(LEFT + DOWN, color=RED)
        B = Dot(RIGHT + UP, color=RED)
        
        # Create labels for points A and B
        label_A = Text("A", font_size=24).next_to(A, DOWN)
        label_B = Text("B", font_size=24).next_to(B, DOWN)
        
        # Create a line segment
        line = Line(A.get_center(), B.get_center(), color=BLUE)
        
        # Create a title
        title = Text("Line Segment ", font_size=40)
        
        # Add the title, points, labels, and line segment to the scene
        self.add(title.to_edge(UP), A, label_A, B, label_B, line)
        

        self.wait(3)

        title = Text("The distance between the points A and B is called the length of AB", font_size=30,color = YELLOW ).shift(DOWN * 2)
        
        # Create a group
        group = VGroup( title)

        self.add(group)

        # Wait for 2 seconds before closing the scene
        self.wait(5)



####Ruler methd 


    def RulerMethod(self):
 # Title
        title = Text("Construction of Line Segment", font_size=60,color = PINK)
        self.play(Write(title))
        self.wait(3)
        self.play(Unwrite(title))
        self.wait(2)
        

        # Create a title
        title = Text("By Using Ruler",color = BLUE)
        title.to_edge(UP)
        self.add(title)
        self.wait(3)

        # Create a ruler
        ruler = Line(LEFT * 10, RIGHT * 10)
        ruler.set_color(GRAY)
        self.add(ruler)

        # Create tick marks on the ruler
        for i in range(-10, 11):
            tick = Line(UP * 0.1, DOWN * 0.1)
            tick.move_to(i * RIGHT)
            self.add(tick)

        # Create two points
        A = Dot(LEFT * 4)
        A.set_color(RED)
        B = Dot(RIGHT * 4)
        B.set_color(BLUE)

        # Create labels for the points
        label_A = Text("A")
        label_A.next_to(A, DOWN)
        label_B = Text("B")
        label_B.next_to(B, DOWN)

        self.add(A, B, label_A, label_B)

        # Draw the line segment using the ruler method
        line_segment = Line(A.get_center(), B.get_center())
        line_segment.set_color(YELLOW)
        self.play(Create(line_segment), run_time=2)

        # Create measurement label
        measurement_label = Text("8cm", font_size=30)
        measurement_label.move_to((A.get_center() + B.get_center()) / 2 + UP * 0.5)
        self.add(measurement_label)

        # Wait for a few seconds
        self.wait(5)



######compasses method
  
    def CompassMethod(self):
        # Title
        title = Text("By Using Compasses",color = ORANGE).to_edge(UP)
        self.play(Write(title))
        self.wait(3)

    #line

        step1_text = Text("Step 1: Draw a line of any length.",font_size= 35).next_to(title, DOWN).shift(DOWN * 4.5)
      #  center_point = Dot(point=ORIGIN, color=BLUE)
        
        self.play(Write(step1_text))
      #  self.play(Create(center_point))
        self.wait(2)

        line2 = Line(start=RIGHT*3 + RIGHT * 3, end=LEFT*6 + RIGHT * 3, color=WHITE)
        self.add( line2)
         # Step 1: Draw the center point


        # Step 2: Set the compass radius
        step2_text = Text("Step 2: Mark the starting point A on the line segment.",font_size=35,color = GREEN).next_to(title, DOWN).shift(DOWN * 4.5)    
        self.play(Transform(step1_text, step2_text))
        self.wait(3)

        # Points
        start_point = LEFT * 3
        end_point = start_point + RIGHT * 5.3
       
        
        # Label points
        start_label = MathTex("A",color = BLUE).next_to(start_point, DOWN)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
        self.play(Write(start_label))


         # Step 2: Set the compass radius
        step3_text = Text("Step 3: Take a ruler and place the pointer\n of the compass, apart from the pencil's lead. ",font_size=35).next_to(title, DOWN).shift(DOWN * 4.5)    
        self.play(Transform(step1_text, step3_text))
        self.wait(4)

         # Step 2: Set the compass radius
        step4_text = Text("Step 4: Place the pointer of compass at the starting point \nand mark an arc on  line with the pencil point.",font_size=35,color = GREEN).next_to(title, DOWN).shift(DOWN * 4.5)    
        self.play(Transform(step1_text, step4_text))
        self.wait(4)
        
        # Compass arcs
        arc1 = Arc(radius=5.3, angle=PI/13, arc_center=start_point)
        arc2 = Arc(radius=5.3, angle=-PI/13, arc_center=start_point)
        arc1.set_color(YELLOW)
        arc2.set_color(YELLOW)
        
        self.play(Create(arc1), Create(arc2))
        
        self.wait(3)


        # Step 2: Set the compass radius
        step4_text = Text("Step 5 : Mark the arc point as B.",font_size=35).next_to(title, DOWN).shift(DOWN * 4.5)    
        self.play(Transform(step1_text, step4_text))
        self.wait(3)
        end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
        self.play(Write(end_label))
        self.wait(2)


            # Draw line segment
        line = Line(start_point, end_point,color = PINK)
        self.play(Create(line))

        # Indicate line segment length
        length_label = MathTex("Length \\text{ }",color = PINK).next_to(line, UP).scale(0.75)
        self.play(Write(length_label))
        
        self.wait(2)
        step5_text = Text("Final Line Segment",font_size=35,color = GREEN).next_to(title, DOWN).shift(DOWN * 4.5)    
        self.play(Transform(step1_text, step5_text))
        self.wait(5)


        ###construction of circle 
    def ConstructCircleWithCompass(self):
        # Title
        title = Text("Construction of a Circle",color=PINK).to_edge(UP)
        self.play(Write(title))
        self.wait(3)
        
        # Step 1: Draw the center point
        step1_text = Text("Step 1: Mark the center point",font_size= 40).next_to(title, DOWN).shift(DOWN * 5)
        center_point = Dot(point=ORIGIN, color=BLUE)
        
        self.play(Write(step1_text))
        self.play(Create(center_point))
        self.wait(3)

        # Step 2: Set the compass radius
        step2_text = Text("Step 2: Set the compass radius",font_size=40).next_to(title, DOWN).shift(DOWN * 5)
        radius_line = Line(ORIGIN, 2*RIGHT, color=YELLOW)
        
        
        self.play(Transform(step1_text, step2_text))
        self.play(Create(radius_line))
        self.wait(3)

        # Step 3: Draw the circle with the compass
        step3_text = Text("Step 3: Draw the circle with the compass",font_size=40).next_to(title, DOWN).shift(DOWN * 5)
        circle = Circle(radius=2, color=GREEN)
        
        self.play(Transform(step1_text, step3_text))
        self.play(Create(circle))
        self.wait(4)

        # Final Diagram
        final_text = Text("Step 4:Final Circle Diagram",font_size=40).next_to(title, DOWN).shift(DOWN * 5)
        final_diagram = VGroup(center_point, radius_line, circle)
        
        self.play(Transform(step1_text, final_text))
        self.play(final_diagram.animate.move_to(ORIGIN))
        self.wait(4)


##############perpendiculars
    def Perpendiculars(self):
        # Title
        title = Text("Perpendiculars").to_edge(UP)
        self.play(Write(title))
        self.wait(3)
        
        # Step 1: Draw the initial line
        step1_text = Text("Horizontal Line ",color = BLUE).next_to(title, DOWN).shift(DOWN * 5)
        initial_line = Line(4*LEFT, 4*RIGHT, color=BLUE)
        
        self.play(Write(step1_text))
        self.play(Create(initial_line))
        self.wait(3)

        # Step 2: Mark the point where perpendicular will be drawn
        step2_text = Text(" Intersection Point",color = RED).next_to(title, DOWN).shift(DOWN * 5)
        intersection_point = Dot(point=ORIGIN, color=RED)
        
        self.play(Transform(step1_text, step2_text))
        self.play(Create(intersection_point))
        self.wait(3)

        # Step 3: Draw the perpendicular line
        step3_text = Text("Perpendicular Line ",color =GREEN).next_to(title, DOWN).shift(DOWN * 5)
        perpendicular_line = Line(2*DOWN, 2*UP, color=GREEN)
        
        self.play(Transform(step1_text, step3_text))
        self.play(Create(perpendicular_line))
        self.wait(3)

        # Step 4: Indicate the 90-degree angle
        step4_text = Text(" ").next_to(title, DOWN).shift(DOWN * 5)
        right_angle = Arc(radius=0.5, start_angle=0, angle=PI/2, color=YELLOW).move_arc_center_to(intersection_point.get_center())
        
        self.play(Transform(step1_text, step4_text))
        self.play(Create(right_angle))
        self.wait(3)

        # Final Diagram
        final_text = Text("Perpendicular Lines with 90-Degree Angle",color = PINK).next_to(title, DOWN).shift(DOWN * 5)
        final_diagram = VGroup(initial_line, intersection_point, perpendicular_line, right_angle)
        
        self.play(Transform(step1_text, final_text))
        self.play(final_diagram.animate.move_to(ORIGIN))
        self.wait(5)

# To render the scene, save this script to a file (e.g., construct_perpendiculars.py) and run the following command in your terminal:
# manim -pql construct_perpendiculars.py ConstructPerpendiculars



#construction of perpendicular bisector
    def PerpendicularBisector(self):
        # Title
        title = Text("Perpendicular Bisector of a Line Segment",color=PINK).to_edge(UP)
        self.play(Write(title))
        self.wait(3)

        # Step 1: Draw the initial line segment
        step1_text = Text("Step 1: Draw the initial line segment AB",font_size=40).next_to(title, DOWN).shift(DOWN*5.8)
        start_point = 2*LEFT
        end_point = 2*RIGHT
        line_segment = Line(start_point, end_point, color=BLUE)
        label_A = Text("A").next_to(start_point, LEFT)
        label_B = Text("B").next_to(end_point, RIGHT)
        
        self.play(Write(step1_text))
        self.play(Create(line_segment), Write(label_A), Write(label_B))
        self.wait(4)

        # Step 2: Draw arcs from both endpoints with radius greater than half the length of the segment
        step2_text = Text("Step 2: Draw arcs from both endpoints",font_size=40).next_to(title, DOWN).shift(DOWN*5.8)
        radius = line_segment.get_length() / 1.5
        arc1_top = Arc(radius=radius, start_angle=0, angle=PI, color=YELLOW).move_arc_center_to(start_point)
        arc1_bottom = Arc(radius=radius, start_angle=PI, angle=PI, color=YELLOW).move_arc_center_to(start_point)
        arc2_top = Arc(radius=radius, start_angle=PI, angle=PI, color=YELLOW).move_arc_center_to(end_point)
        arc2_bottom = Arc(radius=radius, start_angle=0, angle=PI, color=YELLOW).move_arc_center_to(end_point)

        self.play(Transform(step1_text, step2_text))
        self.play(Create(arc1_top), Create(arc1_bottom), Create(arc2_top), Create(arc2_bottom))
        self.wait(4)

        # Step 3: Mark the intersection points of the arcs
        step3_text = Text("Step 3: Mark the intersection points M and N",font_size=40).next_to(title, DOWN).shift(DOWN*5.8)
        intersection_top = Dot(arc1_top.point_from_proportion(0.238), color=RED)
        intersection_bottom = Dot(arc1_bottom.point_from_proportion(0.77), color=RED)
        label_M = Text("M").next_to(intersection_top, UP)
        label_N = Text("N").next_to(intersection_bottom, DOWN)

        self.play(Transform(step1_text, step3_text))
        self.play(Create(intersection_top), Create(intersection_bottom), Write(label_M), Write(label_N))
        self.wait(4)

        # Step 4: Draw the perpendicular bisector through the intersection points
        step4_text = Text("Step 4: Draw the perpendicular bisector",font_size=40).next_to(title, DOWN).shift(DOWN*5.8)
        perpendicular_bisector = DashedLine(intersection_top.get_center(), intersection_bottom.get_center(), color=GREEN)
        midpoint = Dot(line_segment.get_center(), color=RED)
        label_P = Text("P").next_to(midpoint, RIGHT)

        self.play(Transform(step1_text, step4_text))
        self.play(Create(perpendicular_bisector), Create(midpoint), Write(label_P))
        self.wait(4)

        # Final Diagram
        final_text = Text("Final Perpendicular Bisector Diagram",font_size=40).next_to(title, DOWN).shift(DOWN*5.8)
        final_diagram = VGroup(line_segment, arc1_top, arc1_bottom, arc2_top, arc2_bottom, intersection_top, intersection_bottom, perpendicular_bisector, midpoint, label_A, label_B, label_M, label_N, label_P)
        
        self.play(Transform(step1_text, final_text))
        self.play(final_diagram.animate.move_to(ORIGIN))
        self.wait(5)

# To render the scene, save this script to a file (e.g., construct_perpendicular_bisector.py) and run the following command in your terminal:
# manim -pql construct_perpendicular_bisector.py ConstructPerpendicularBisector
#_bisector.py ConstructPerpendicularBisect  # Title
   



    def Construct40DegreeAngle(self):
        # Title
        title = Text("DRAWING ANGLES USING PROTRACTOR",color = BLUE).scale(0.75).to_edge(UP)
        self.play(Write(title))
        self.wait(3)

        # Protractor Diagram
        protractor_arc = Arc(radius=2, start_angle=0, angle=PI).shift(DOWN)
        protractor_lines = VGroup(*[
            Line(ORIGIN, 2 * UP).rotate(angle)
            for angle in np.linspace(0, PI, 13)
        ]).shift(DOWN)
        protractor = VGroup(protractor_arc, protractor_lines).shift(UP*0)

        # Add protractor to the scene
        self.play(Create(protractor))

        # Draw the base line
        base_line = Line( 5 * RIGHT).shift(DOWN +LEFT*3)
        self.play(Create(base_line))
        self.wait(2)

        # Draw the angle line
        angle_degrees = 40
        angle_radians = angle_degrees * DEGREES
        angle_line = Line(ORIGIN, 2 * RIGHT).rotate(angle_radians).shift(DOWN*0.3+LEFT*0.2)
        self.play(Create(angle_line))
        self.wait(2)

        # Angle label
        angle_label = MathTex(f"{angle_degrees}^\\circ",color = ORANGE).next_to(angle_line.get_end(), UP)
        self.play(Write(angle_label))
        self.wait(2)

        # Steps to construct the angle
        steps = [
            "1. Place the protractor's center at the vertex of the angle.",
            "2. Align the base line with the protractor's baseline.",
            "3. Mark the angle's degree on the protractor.",
            "4. Draw a line from the vertex through the marked point.",
        ]
        step_texts = VGroup(
            *[Text(step).scale(0.5).to_edge(DOWN) for step in steps]
        )

        for step_text in step_texts:
            self.play(Write(step_text))
            self.wait(4)
            self.play(FadeOut(step_text))

        # Wait before ending scene
        self.wait(5)





######     CONSTRUCTING A COPY OF AN ANGLE OF UNKNOWN MEASURE


    def CopyAngleWithCompass(self):
        # Title for the scene
        title = Text("CONSTRUCTING A COPY OF AN ANGLE OF UNKNOWN MEASURE",font_size= 32,color = YELLOW).to_edge(UP)
        self.play(Write(title))
        self.wait(3)

        # Step 1: Draw the original angle
        step1_title = Text("Step 1: Draw the original angle", font_size=32,color=BLUE).next_to(title, DOWN).shift(DOWN * 5.7)
        self.play(Write(step1_title))
        self.wait(3)

        O = Dot(ORIGIN)
        start_label = MathTex("O",color = ORANGE).next_to(O, DOWN)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
        self.play(Write(start_label))
        A = Dot(LEFT * 3 + DOWN * 2)
        B = Dot(RIGHT * 3 + UP * 2)
        original_angle = VGroup(Line(O.get_center(), A.get_center()), Line(O.get_center(), B.get_center()))

        self.play(Create(O), Create(A), Create(B), Create(original_angle))
        line2 = Line(start=RIGHT*3 + RIGHT * 3, end=LEFT*6 + RIGHT * 2, color=WHITE)
        self.add( line2)
         # Step 1: Draw the center point

        self.wait(3)

        # Step 2: Draw a ray from a new point
        step2_title = Text("Step 2: Draw a ray from a new point", font_size=32,color = PINK).next_to(title, DOWN).shift(DOWN * 5.7)
        self.play(Transform(step1_title, step2_title))
        self.wait(3)

        P = Dot(RIGHT * 3 + DOWN * 2)
        start_label = MathTex("O",color = ORANGE).next_to(P, DOWN)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
        self.play(Write(start_label))
        new_ray = Line(P.get_center(), P.get_center() + RIGHT * 3)
        self.play(Create(P), Create(new_ray))
        self.wait(3)

        # Step 3: Draw an arc on the original angle
        step3_title = Text("Step 3: Draw an arc on the original angle", font_size=32,color=BLUE).next_to(title, DOWN).shift(DOWN * 5.7)
        self.play(Transform(step1_title, step3_title))
        self.wait(3)

        arc_radius = 2.5
        arc1 = Arc(radius=arc_radius, angle=PI / 3).move_arc_center_to(O.get_center())
        self.play(Create(arc1))
        self.wait(3)

        # Step 4: Copy the arc to the new angle
        step4_title = Text("Step 4: Copy the arc to the new angle", font_size=32,color=PINK).next_to(title, DOWN).shift(DOWN * 5.7)
        self.play(Transform(step1_title, step4_title))
        self.wait(3)

        arc2 = Arc(radius=arc_radius, angle=PI / 3).move_arc_center_to(P.get_center())
        self.play(Create(arc2))
        self.wait(3)

        # Step 5: Mark the intersections of the arc with the original angle
        step5_title = Text("Step 5: Mark the intersections of the arc with the original angle", font_size=32,color=BLUE).next_to(title, DOWN).shift(DOWN * 5.7)
        self.play(Transform(step1_title, step5_title))
        self.wait(3)

        intersect_A = arc1.point_from_proportion(0.3)
        intersect_B = arc1.point_from_proportion(0.7)
        mark_A = Dot(intersect_A)
        mark_B = Dot(intersect_B)
        self.play(Create(mark_A), Create(mark_B))
        self.wait(3)

        # Step 6: Copy the distances of the intersections to the new arc
        step6_title = Text("Step 6: Copy the distances of the intersections to the new arc", font_size=32,color=PINK).next_to(title, DOWN).shift(DOWN * 5.7)
        self.play(Transform(step1_title, step6_title))
        self.wait(3)

        distance_AB = Line(intersect_A, intersect_B)
        self.play(Create(distance_AB))
        self.wait(2)

        # Use the compass to transfer the distance to the new arc
       # compass_arc = Arc(radius=distance_AB.get_length(), angle=PI / 6).move_arc_center_to(intersect_A)
       # self.play(Create(compass_arc))
       # self.wait(1)

        # Find the intersection on the new arc
        intersect_Q = arc2.point_from_proportion(0.3)
        mark_Q = Dot(intersect_Q)
        self.play(Create(mark_Q))
        self.wait(3)

        # Step 7: Draw the second ray of the copied angle
        step7_title = Text("Step 7: Draw the second ray of the copied angle", font_size=32,color=BLUE).next_to(title, DOWN).shift(DOWN * 5.7)
        self.play(Transform(step1_title, step7_title))
        self.wait(3)

        copied_angle_side = Line(P.get_center(), mark_Q.get_center())
        self.play(Create(copied_angle_side))
        self.wait(3)

        # Final title
        final_title = Text("Constructed Angle Copy", font_size=32,color = PINK).next_to(title, DOWN).shift(DOWN * 5.7)
        self.play(Transform(step1_title, final_title))
        self.play(Write(final_title))
        self.wait(5)

        # Clear the scene
        self.play(FadeOut(final_title), FadeOut(title), FadeOut(step1_title), *[FadeOut(mob) for mob in self.mobjects])


################################
         
        
    def Bisect(self):
      

      title = Text("CONSTRUCTION TO BISECT A GIVEN ANGLE",font_size= 36,color = ORANGE).to_edge(UP)
      self.play(Write(title))
      self.wait(3)
        # Step text configurations with smaller font size
      step1_text = Tex("Step 1: Draw the Given Angle .",color = WHITE).scale(1.2).to_edge(DOWN*2.5)
      self.play(Write(step1_text))
      self.wait(3)
      self.play(FadeOut(step1_text))


      line_l = Line(LEFT *0.38+DOWN*1 , RIGHT * 4+DOWN*1)
      self.play(Create(line_l))
      O = Dot(LEFT *0.38+DOWN*1)
      self.play(Create(O))
           
        # Label points
      O_label = MathTex("O",color = BLUE).next_to(LEFT *0.38+DOWN*1, DOWN)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
      self.play(Write(O_label))
      self.wait(2)

      N = Dot(LEFT *-2.5+DOWN*1)
      self.play(Create(N))
      self.wait(2)
           
        # Label points
      N_label = MathTex("N",color = BLUE).next_to(LEFT *-2.5+DOWN*1, DOWN)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
      self.play(Write(N_label))
      self.wait(2)

      angle_degrees = 60
      angle_radians = angle_degrees* DEGREES
      angle_line = Line( ORIGIN,2 * RIGHT).rotate(angle_radians).shift(DOWN*1+LEFT*0.47+UP*1.5).set_length(3.5)
      self.play(Create(angle_line))
      self.wait(3)


      M = Dot(DOWN*1+LEFT*-1.3+UP*2.8)
      self.play(Create(M))
      self.wait(2)
           
        # Label points
      M_label = MathTex("M",color = BLUE).next_to(DOWN*1+LEFT*-1.3+UP*2.8, UP)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
      self.play(Write(M_label))
      self.wait(2)



 # Compass arcs

      
      step2_text = Tex("Step 2: Draw an Arc Across Both Rays of the Angle.",color = PINK).scale(1.2).to_edge(DOWN*2.5)
      self.play(Write(step2_text))
      self.wait(3)
      self.play(FadeOut(step2_text))

  # Compass arcs
      arc1 = Arc(radius=3.7, angle=PI/4, arc_center=LEFT *2+DOWN*1)
        
      arc1.set_color(YELLOW)
    
        
      self.play(Create(arc1))
      self.wait(2)
        

      Q = Dot(LEFT *-1.7+DOWN*1)
      self.play(Create(Q))
      self.wait(2)
           
        # Label points
      Q_label = MathTex("Q",color = BLUE).next_to(LEFT *-1.7+DOWN*1, DOWN)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
      self.play(Write(Q_label))
      

      P = Dot(DOWN*1+LEFT*-0.94+UP*2.2)
      self.play(Create(P))
      self.wait(2)
           
        # Label points
      P_label = MathTex("P",color = BLUE).next_to(DOWN*1+LEFT*-0.94+UP*2.2, UP+LEFT)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
      self.play(Write(P_label))
      self.wait(2)
      


      step3_text = Tex("Step 3: Draw Arcs from the Points of Intersection.",color = WHITE).scale(1.2).to_edge(DOWN*2.5)
      self.play(Write(step3_text))
      self.wait(3)
      self.play(FadeOut(step3_text))


  # Compass arcs
      arc2 = Arc(radius=3, angle=PI/7, arc_center=LEFT *0.5+DOWN*1+UP*1)
        
      arc2.set_color(YELLOW)
    
      self.play(Create(arc2))
      self.wait(2)
        
    

 # Compass arcs
      arc3 = Arc(radius=3, angle=PI/7, arc_center=LEFT *0.5+DOWN*1+UP*1).rotate(70)
        
      arc3.set_color(YELLOW)
    
      self.play(Create(arc3))
      self.wait(2)
        

      z = Dot(LEFT *-2.39+DOWN*1.05+UP*1.68)
      self.play(Create(z))
           
        # Label points
      z_label = MathTex("Z",color = BLUE).next_to(LEFT *-2.39+DOWN*1.05+UP*1.68, UP+RIGHT)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
      self.play(Write(z_label))
      self.wait(2)
      
      step4_text = Tex("Step 4: Draw the Angle Bisector.",color = PINK).scale(1.2).to_edge(DOWN*2.5)
      self.play(Write(step4_text))
      self.wait(2)
      self.play(FadeOut(step4_text))

      angle_degrees = 30
      angle_radians = angle_degrees* DEGREES
      angle_line = DashedLine( ORIGIN,3.47 * RIGHT).rotate(angle_radians).shift(DOWN*1.55+LEFT*0.47+UP*1.5).set_length(3.7)
      self.play(Create(angle_line))
      self.wait(5)
#self.play(Write(angle_label))



        ################################



    def Compass60degree(self):

         # Title for the scene
        title = Text("CONSTRUCTING ANGLES OF SPECIAL MEASURES \n                        Construction of 60° Angle",font_size= 32,color = WHITE).to_edge(UP)
        self.play(Write(title))
        self.wait(4)
        # Step text configurations with smaller font size
        step1_text = Tex("Step 1: Draw a line $l$ and mark a point $O$ on it.",color = ORANGE).scale(0.76).to_edge(DOWN*2.5)
        step2_text = Tex("Step 2: Place the pointer of the compasses at $O$ and draw an arc of convenient radius which cuts the line $l$ at a point, say $A$.",color = BLUE).scale(0.77).to_edge(DOWN*2.5)
        step3_text = Tex("Step 3: With the pointer at $A$ (as center) and the same radius as in step 2, draw an arc that passes through $O$.",color = ORANGE).scale(0.77).to_edge(DOWN*2.5)
        step4_text = Tex("Step 4: Let the two arcs intersect at $B$. Join $OB$. We get $\\angle AOB$ whose measure is $60^\\circ$.",color = BLUE).scale(0.77).to_edge(DOWN*2.5)

        # Drawing configurations
        line_l = Line(LEFT * 3, RIGHT * 3)
        point_O = Dot(ORIGIN)
        label_O = MathTex("O").next_to(point_O, DOWN)
        
        radius = 2
        arc_OA = Arc(radius=radius, start_angle=0, angle=PI/2.5, color=YELLOW)
        point_A = Dot(arc_OA.get_start())
        label_A = MathTex("A").next_to(point_A, DOWN)


        
        
        arc_AB = Arc(radius=radius, start_angle=0, angle=PI, arc_center=point_A.get_center(), color=YELLOW)
        point_B = Dot(arc_AB.get_end())
        label_B = MathTex("O").next_to(point_B, DOWN)




        line_OB = Line(point_O.get_center(), point_B.get_center())


        angle_label = MathTex("60^\\circ").move_to(0.5 * (point_O.get_center() + point_B.get_center() + point_A.get_center())).shift(UP * 0.5)
        
        # Step 1: Draw line and point O
        self.play(Write(step1_text))
        self.play(Create(line_l))
        self.play(Create(point_O), Write(label_O))
        self.wait(4)
        self.play(FadeOut(step1_text))

        # Step 2: Draw arc from O
        self.play(Write(step2_text))
        self.play(Create(arc_OA))
        self.play(Create(point_A), Write(label_A))
        self.wait(4)
        self.play(FadeOut(step2_text))

        # Step 3: Draw arc from A


        self.play(Write(step3_text))
        self.play(Create(arc_AB))
        self.wait(4)
        self.play(FadeOut(step3_text))

        # Step 4: Mark point B, join OB, and label the angle
        A = Dot(RIGHT*1+UP*1.71)
        self.play(Create(A))
        self.play(Write(step4_text))
        step_text = Tex("B").shift(RIGHT*1+UP*1.97)
        self.play(Write(step_text))
        
        self.play(Create(point_B), Write(label_B))
        self.play(Create(line_OB))
        # Draw the angle line
        angle_degrees = 60
        angle_radians = angle_degrees * DEGREES
        angle_line = Line(ORIGIN, 2 * RIGHT).rotate(angle_radians).shift(DOWN*-0.85+LEFT*0.47)
        self.play(Create(angle_line))
        self.play(Write(angle_label))
        self.wait(4)
        self.play(FadeOut(step4_text))

# To render the scene, use:
# manim -pql construct_60_degree_angle.py Construct60DegreeAngle

# manim -pql construct_60_degree_angle.py Construct60DegreeAngle





#120 degree



    def CON120deg(self):
        title = Text("Construction of 120° Angle",font_size= 45,color = YELLOW).to_edge(UP)
        self.play(Write(title))
        self.wait(3)

        # Step 1: Draw the original angle
        step1_title = Text("Step 1:  Draw a ray OA.", font_size=32,color=BLUE).next_to(title, DOWN).shift(DOWN * 5.55)
        self.play(Write(step1_title))
        self.wait(3)
    

       
        P = Dot(RIGHT * 3 + DOWN * 2)
        start_label = MathTex("O",color = BLUE).next_to(P, DOWN)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
        self.play(Write(start_label))
        new_ray = Line(P.get_center(), P.get_center() + RIGHT * 3)
        self.play(Create(P), Create(new_ray))
      


        arc_radius = 3.076
      #  arc1 = Arc(radius=arc_radius, angle=PI ).move_arc_center_to(O.get_center())
      #  self.play(Create(arc1))
      #  self.wait(1)

        
    
        A = Dot( DOWN*2+RIGHT*5.82,color=WHITE)
        self.play(Create(A))
        start_ = MathTex("A",color = BLUE).next_to(P, DOWN+RIGHT*10.2)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
        self.play(Write(start_))



  # Step 1: Draw the original angle
        step9_title = Text("Step 2: Taking O as center and any radius, draw an arc cutting OA at M.", font_size=32,color=PINK).next_to(title, DOWN).shift(DOWN * 5.55)
        self.play(Transform(step1_title, step9_title))
        self.wait(4)



        start_label = MathTex("M",color = BLUE).next_to(P, DOWN+RIGHT*7)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
        self.play(Write(start_label))


        arc2 = Arc(radius=arc_radius, angle=PI ).move_arc_center_to(P.get_center()).shift(LEFT)
        self.play(Create(arc2))
        
 # Step 5: Mark the intersections of the arc with the original angle
        step5_title = Text("Step 3: Now, taking M as center and with the same radius\n as before,draw an arc intersecting the previously drawn arc at point P.", font_size=26,color=BLUE).next_to(title, DOWN).shift(DOWN * 5.6)
        self.play(Transform(step1_title, step5_title))
        self.wait(4)

        arc6 = Arc(radius=3, angle=PI/6.2, arc_center=RIGHT*1.3+DOWN*1.6+UP*1).rotate(90)
        arc6.set_color(YELLOW)
        self.play(Create(arc6))
        
        z = Dot(RIGHT*4.088+DOWN*1.6+UP*1.8)
        self.play(Create(z))
           
        # Label points
        z_label = MathTex("P",color = BLUE).next_to(RIGHT*4.088+DOWN*1.6+UP*1.8, UP+RIGHT)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
        self.play(Write(z_label))


        arc7 = Arc(radius=3, angle=PI/6.5, arc_center=LEFT *2+DOWN*1+UP*1).rotate(90)
        arc7.set_color(YELLOW)
        self.play(Create(arc7))

       
      #  self.play( Create(mark_B))
       # self.wait(1)

        # Step 6: Copy the distances of the intersections to the new arc
        step6_title = Text("Step 4: With P as center and the same radius, draw an arc cutting the arc at Q", font_size=26,color=PINK).next_to(title, DOWN).shift(DOWN * 5.7)
        self.play(Transform(step1_title, step6_title))
        self.wait(4)

     #   distance_AB = Line(intersect_A, intersect_B)
 
        # Find the intersection on the new arc
        intersect_Q = arc2.point_from_proportion(0.6)
        mark_Q = Dot(intersect_Q)

        self.play(Create(mark_Q))
        Q_label = MathTex("Q",color = BLUE).next_to(mark_Q, UP+LEFT)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
        self.play(Write(Q_label))

    

        # Step 7: Draw the second ray of the copied angle
        step7_title = Text("Step 5: Draw the line OQ", font_size=32,color=BLUE).next_to(title, DOWN).shift(DOWN * 5.6)
        self.play(Transform(step1_title, step7_title))

        copied_angle_side = Line(P.get_center(), mark_Q.get_center()).set_length(4)
        self.play(Create(copied_angle_side))
        self.wait(4)




        
    def con90degree(self):
    
        title = Text("Construction of 90° Angle",font_size= 45,color = LOGO_WHITE).to_edge(UP)
        self.play(Write(title))
        self.wait(3)

        # Step 1: Draw the original angle
        #step1_title = Text("Step 1:  Draw a ray OA.", font_size=32,color=BLUE).next_to(title, DOWN).shift(DOWN * 5.55)
       # self.play(Write(step1_title))

    
        P = Dot(RIGHT * 3 + DOWN * 2)
        start_label = MathTex("O",color = BLUE).next_to(P, DOWN)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
        self.play(Write(start_label))
        new_ray = Line(P.get_center(), P.get_center() + RIGHT * 3)
        self.play(Create(P), Create(new_ray))
      

        arc_radius = 3.076
      
        
        A = Dot( DOWN*2+RIGHT*5.82,color=WHITE)
        self.play(Create(A))
        start_ = MathTex("A",color = BLUE).next_to(P, DOWN+RIGHT*10.2)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
        self.play(Write(start_))


        start_label = MathTex("M",color = BLUE).next_to(P, DOWN+RIGHT*7)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
        self.play(Write(start_label))


        arc2 = Arc(radius=arc_radius, angle=PI ).move_arc_center_to(P.get_center()).shift(LEFT)
        self.play(Create(arc2))


        arc6 = Arc(radius=3, angle=PI/6.2, arc_center=RIGHT*1.3+DOWN*1.6+UP*1).rotate(90)
        arc6.set_color(YELLOW)
        self.play(Create(arc6))

        
        z = Dot(RIGHT*4.088+DOWN*1.6+UP*1.8)
        self.play(Create(z))
           
        # Label points
        z_label = MathTex("P",color = BLUE).next_to(RIGHT*4.088+DOWN*1.6+UP*1.8, UP+RIGHT)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
        self.play(Write(z_label))
         # Step 1: Draw the original angle
      

        arc7 = Arc(radius=3, angle=PI/6.5, arc_center=LEFT *2+DOWN*1+UP*1).rotate(90)
        arc7.set_color(YELLOW)
        self.play(Create(arc7))
     
 
        # Find the intersection on the new arc
        intersect_Q = arc2.point_from_proportion(0.6)
        mark_Q = Dot(intersect_Q)

        self.play(Create(mark_Q))
        Q_label = MathTex("Q",color = BLUE).next_to(mark_Q, UP+LEFT)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
        self.play(Write(Q_label))


        angle_degrees = 65
        angle_radians = angle_degrees* DEGREES
        angle_line = DashedLine( ORIGIN,3.47 * RIGHT).rotate(angle_radians).shift(DOWN*1.76+RIGHT*2.1+UP*1.5).set_length(3.7)
        self.play(Create(angle_line))


        step20_title = Text("∠AOP = 60°", font_size=32,color=ORANGE).next_to(title, DOWN).shift(DOWN * 5.55)
        self.play(Write(step20_title))
        self.wait(1.4)
        self.play(FadeOut(step20_title))

#self.play(Write(angle_label))
        copied_angle_side = DashedLine(P.get_center(), mark_Q.get_center()).set_length(4)
        self.play(Create(copied_angle_side))

           # Step 7: Draw the second ray of the copied angle
        step7_title = Text("∠POQ = 60° and ∠AOQ= 120°", font_size=32,color=ORANGE).next_to(title, DOWN).shift(DOWN * 5.6)
        self.play(Write( step7_title))
        self.wait(1.4)
        self.play(FadeOut(step7_title))

  
       # Step 7: Draw the second ray of the copied angle
        step21_title = Text("We know that 90° = 60° + 30° and also 90° = 120° - 30°", font_size=32,color=ORANGE).next_to(title, DOWN).shift(DOWN * 5.6)
        self.play(Write(step21_title))
        self.wait(1.4)
        self.play(FadeOut(step21_title))

##### # Step 7: Draw the second ray of the copied angle
        step23_title = Text("So, we need to bisect ∠POQ to get an angle of 30°.", font_size=32,color=ORANGE).next_to(title, DOWN).shift(DOWN * 5.6)
        self.play(Write( step23_title))
        self.wait(1.4)
        self.play(FadeOut(step23_title))


        arc10 = Arc(radius=3, angle=PI/8.2, arc_center=LEFT *0+DOWN*1+UP*1.7).rotate(90)
        arc10.set_color(YELLOW)
        self.play(Create(arc10))


        arc11 = Arc(radius=3, angle=PI/8.2, arc_center=LEFT *-0.2+DOWN*1+UP*1.7).rotate(95)
        arc11.set_color(YELLOW)
        self.play(Create(arc11))


        B = Dot( UP*1.43+RIGHT*3,color=WHITE)
        self.play(Create(B))
        start = MathTex("B",color = BLUE).next_to( UP*1.8+RIGHT*2.7)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
        self.play(Write(start))


        angle_degrees = 90
        angle_radians = angle_degrees* DEGREES
        angle_line = Line( ORIGIN,3.47 * RIGHT).rotate(angle_radians).shift(DOWN*1.6+RIGHT*1.25+UP*1.5).set_length(3.7)
        self.play(Create(angle_line))
#self.play(Write(angle_label))


#### # Step 7: Draw the second ray of the copied angle
        step27_title = Text("∠BOP = 30° and finally we got ∠AOB = 90°", font_size=32,color=ORANGE).next_to(title, DOWN).shift(DOWN * 5.6)
        self.play(Write(step27_title))
        self.wait(5)
        self.play(FadeOut(step27_title))





    def SetDeveloperList(self):
        self.DeveloperList = "Uday Kiran"   

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Practical Geometry.py"      
        





if __name__ == "__main__":
    scene = PracticalGeometryIntroduction()
    scene.render()