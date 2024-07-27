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


class Grade6chapter13PracticalGeometry(AbstractAnim):

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
        self.wait(3.2)
        self.play(Unwrite(title))
        self.wait(2)
        
        #introduction
    def intro(self):    
        title = Text("Introduction ", font_size=40).shift(UP * 3.5)
      
        # Create a group
        group = VGroup( title)

        self.add(group)
        self.wait(2)


        # Right-angled diagram with vertex labels
        right_angle = Polygon(
          ORIGIN,
       [3, 0, 0],
    [3, 3, 0],
        color=BLUE,
        fill_opacity=0.2
   )

# Create vertex labels
        vertex_a = Tex("A", font_size=40)
        vertex_b = Tex("B", font_size=40)
        vertex_c = Tex("C", font_size=40)

# Position vertex labels
        vertex_a.next_to(ORIGIN, DOWN+LEFT)
        vertex_b.next_to([3, 0, 0], DOWN+RIGHT)
        vertex_c.next_to([3, 3, 0], UP+RIGHT)
 
        right_angle_label = MathTex(r"\angle ABC = 90^\circ", font_size=45)
        right_angle_label.next_to(right_angle, DOWN)

# Animate the creation of the triangle and labels
        self.play(
          DrawBorderThenFill(right_angle),
          Write(vertex_a),
           Write(vertex_b),
           Write(vertex_c),
           Write(right_angle_label)
         )
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
        p10=cvo.CVO().CreateCVO("Geometry Tools","").setPosition([0,2,0])
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
        self.wait(1)
    
        # Create a title
        title = Text("By Using Ruler")
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
      
        # Create a ruler
        s1 = Text("First take a ruler and place it on paper",font_size=35,color=PINK).to_edge(DOWN*2)
        self.play(Write(s1))
        self.wait(2.6)
        ruler = NumberLine(
            x_range=[0, 10, 1],
            length=10,
            include_numbers=True,
            include_tip=False,
        )
        self.play(Create(ruler))
        self.play(Unwrite(s1))
       
        # Create two points
        point_A = Dot(ruler.n2p(0), color=RED)
        point_B = Dot(ruler.n2p(6), color=BLUE)

        # Create labels for the points
        label_A = Text("A", color=RED).next_to(point_A, DOWN*1.8)
        label_B = Text("B", color=BLUE).next_to(point_B, DOWN*1.8)
        

           # Create a ruler
        s2 = Text("Marking two distinct points on  paper, labeling them point A\n and point B.",font_size=31,color=PINK).to_edge(DOWN*2)
        self.play(Write(s2))
        self.wait(3)
        # Add points and labels
        self.play(
            Create(point_A),
            Create(point_B),
            Write(label_A),
            Write(label_B)
        )
        self.play(Unwrite(s2))
        # Draw the line segment

        s3 = Text("Finally draw the line from the start point A to end point  B",font_size=35,color=PINK).to_edge(DOWN*1.6)
        self.play(Write(s3))
        self.wait(3)
        line_segment = Line(point_A.get_center(), point_B.get_center(), color=YELLOW)
        self.play(Create(line_segment))

        # Create and display measurement label
        measurement = Text("6 units", color=GREEN).next_to(line_segment, UP)
        self.play(Write(measurement))

        # Wait at the end
        self.wait(4)



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
       
        a = Dot(start_point)
        self.play(Create(a))
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
        b = Dot(end_point)
        self.play(Create(b))
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



    def ConstructCircleWithCompass(self):
        # Title
        title = Text("Construction of a Circle",color=PINK).to_edge(UP)
        self.play(Write(title))
        self.wait(3)
        
        # Step 1: Draw the center point
        step1_text = Text("Step 1: Mark the center point as O.",font_size= 40).next_to(title, DOWN).shift(DOWN * 5)
        center_point = Dot(point=ORIGIN, color=BLUE)
        
        self.play(Write(step1_text))
        self.play(Create(center_point))
        a = Text("O",color = ORANGE,font_size=24).next_to(center_point,DOWN)
        self.play(Write(a))
        self.wait(3)

        # Step 2: Set the compass radius
        step2_text = Text("Step 2: Set the compass required radius with the help \nof scale.",font_size=40).next_to(title, DOWN).shift(DOWN * 5)
        # radius_line = Line(ORIGIN, 2*RIGHT, color=YELLOW)
        
        
        self.play(Transform(step1_text, step2_text))
        # self.play(Create(radius_line))
        # b = Text("radius",font_size=24).next_to(radius_line,UP)
        # self.play(Write(b))
        self.wait(3.6)

        # Step 3: Draw the circle with the compass
        step3_text = Text("Step 3: Place your compass at O and draw the circle. ",font_size=40).next_to(title, DOWN).shift(DOWN * 5)
        circle = Circle(radius=2, color=GREEN)
        
        self.play(Transform(step1_text, step3_text))
        self.wait(2)
        
        self.play(Create(circle))
        self.wait(3)

        radius_line = Line(ORIGIN, 2*RIGHT, color=YELLOW)
        
        
        # self.play(Transform(step1_text, step2_text))
        self.play(Create(radius_line))
        b = Text("radius",font_size=24).next_to(radius_line,UP)
        self.play(Write(b))
        self.wait(3)

        # Final Diagram
        final_text = Text("Final Circle Diagram",font_size=40).next_to(title, DOWN).shift(DOWN * 5)
        final_diagram = VGroup(center_point, radius_line, circle)
        
        self.play(Transform(step1_text, final_text))
        self.play(final_diagram.animate.move_to(ORIGIN))
        self.wait(4)


##############perpendiculars
    def Perpendiculars(self):
  
        # Create title
        title = Text("Perpendicular Angle Forms a Square", color=YELLOW).to_edge(UP)
        self.play(Write(title))

        # Create two perpendicular lines
        line1 = Line(start=LEFT * 2, end=RIGHT * 2, color=BLUE)
        line2 = Line(start=DOWN * 2, end=UP * 2, color=GREEN)
        
        # Create the angle
        angle = RightAngle(line1, line2, length=0.4, color=RED)

        # Animation sequence for lines and angle
        self.play(Create(line1), Create(line2))
        self.play(Create(angle))
        self.wait(1)

        # Create the square
        square = Square(side_length=2.53, color=WHITE)
        square.move_to(ORIGIN)
        
        # Label the vertices
        labels = VGroup()
        vertices = ['A', 'B', 'C', 'D']
        positions = [UL, UR, DR, DL]
        
        for vertex, pos in zip(vertices, positions):
            label = Text(vertex, font_size=24).next_to(square.get_corner(pos), pos, buff=0.2)
            labels.add(label)

        # Animation sequence for square and labels
        self.play(Create(square))
        self.play(Write(labels))
        self.wait(1)

        # Highlight each corner of the square
        for i in range(4):
            dot = Dot(square.get_corner(positions[i]), color=YELLOW, radius=0.1)
            angle_label = MathTex("90°", color=ORANGE, font_size=27).next_to(dot, positions[i], buff=0.3)
            self.play(FadeIn(dot), Write(angle_label))
            self.wait(0.5)
            if i < 3:  # Don't fade out the last one
                self.play(FadeOut(dot), FadeOut(angle_label))

        # Final message
        final_message = Text("All four angles in a square are 90°", 
                             color=PINK, font_size=31).to_edge(DOWN*1.5)
        self.play(Write(final_message))
        self.wait(3.1)

        # Highlight perpendicular lines
        self.play(
            line1.animate.set_color(YELLOW),
            line2.animate.set_color(YELLOW),
            rate_func=there_and_back,
            run_time=2
        )

        # Final fade out
        self.play(
            FadeOut(square), FadeOut(labels), FadeOut(line1), FadeOut(line2),
            FadeOut(angle), FadeOut(title), FadeOut(final_message)
        )







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
        a = Dot(start_point,color=RED)
        b = Dot(end_point,color=RED)
        label_A = Text("A").next_to(start_point, LEFT)
        label_B = Text("B").next_to(end_point, RIGHT)
        
        self.play(Write(step1_text))
        self.play(Create(line_segment),Create(a),Create(b), Write(label_A), Write(label_B))
        self.wait(3)

        # Step 2: Draw arcs from both endpoints with radius greater than half the length of the segment
        step2_text = Text("Step 2: Draw arcs from both endpoints",font_size=40).next_to(title, DOWN).shift(DOWN*5.8)
        radius = line_segment.get_length() / 1.5
        arc1_top = Arc(radius=radius, start_angle=0, angle=PI, color=YELLOW).move_arc_center_to(start_point)
        arc1_bottom = Arc(radius=radius, start_angle=PI, angle=PI, color=YELLOW).move_arc_center_to(start_point)
        arc2_top = Arc(radius=radius, start_angle=PI, angle=PI, color=YELLOW).move_arc_center_to(end_point)
        arc2_bottom = Arc(radius=radius, start_angle=0, angle=PI, color=YELLOW).move_arc_center_to(end_point)

        self.play(Transform(step1_text, step2_text))
        self.play(Create(arc1_top), Create(arc1_bottom), Create(arc2_top), Create(arc2_bottom))
        self.wait(3)

        # Step 3: Mark the intersection points of the arcs
        step3_text = Text("Step 3: Mark the intersection points M and N",font_size=40).next_to(title, DOWN).shift(DOWN*5.8)
        intersection_top = Dot(arc1_top.point_from_proportion(0.238), color=RED)
        intersection_bottom = Dot(arc1_bottom.point_from_proportion(0.77), color=RED)
        label_M = Text("M").next_to(intersection_top, UP)
        label_N = Text("N").next_to(intersection_bottom, DOWN)

        self.play(Transform(step1_text, step3_text))
        self.play(Create(intersection_top), Create(intersection_bottom), Write(label_M), Write(label_N))
        self.wait(3)

        # Step 4: Draw the perpendicular bisector through the intersection points
        step4_text = Text("Step 4: Draw the perpendicular bisector",font_size=40).next_to(title, DOWN).shift(DOWN*5.8)
        perpendicular_bisector = DashedLine(intersection_top.get_center(), intersection_bottom.get_center(), color=GREEN)
        midpoint = Dot(line_segment.get_center(), color=RED)
        label_P = Text("P").next_to(midpoint, RIGHT)

        self.play(Transform(step1_text, step4_text))
        self.play(Create(perpendicular_bisector), Create(midpoint), Write(label_P))
        self.wait(3)

        # Final Diagram
        final_text = Text("Final Perpendicular Bisector Diagram",font_size=40).next_to(title, DOWN).shift(DOWN*5.8)
        final_diagram = VGroup(line_segment, arc1_top, arc1_bottom, arc2_top, arc2_bottom, intersection_top, intersection_bottom, perpendicular_bisector, midpoint, label_A, label_B, label_M, label_N, label_P)
        
        self.play(Transform(step1_text, final_text))
        self.play(final_diagram.animate.move_to(ORIGIN))
        self.wait(5)

    def Construct40DegreeAngle(self):
        # Title
   
        # Create title
        title = Text("Draw Angle Using Protractor", color=YELLOW).to_edge(UP)
        self.play(Write(title))

        # Step 1: Place the protractor
        step1 = Text("Step 1: Place the protractor having 180° ", color=WHITE, font_size=33).to_edge(DOWN)
        protractor = Arc(radius=2, angle=PI, color=BLUE)
        protractor_center = Dot(color=WHITE)

      # Add degree markings and labels
        degree_markings = VGroup()
        for degree in range(0, 181, 1):  # Changed to 181 to include 180 degrees
             angle = degree * DEGREES
             mark_length = 0.1 if degree % 10 == 0 else 0.05  # Longer marks for multiples of 10
             mark = Line(
             start=(2 - mark_length) * UP,
             end=2 * UP,
           ).rotate(angle, about_point=ORIGIN).set_color(GRAY)
        degree_markings.add(mark)
    
        if degree % 10 == 0:  # Labels for multiples of 10
         label = Text(str(degree), font_size=12).next_to(mark, UP, buff=0.1)
         label.rotate(angle - PI/2, about_point=ORIGIN)  # Rotate to align with the arc
        degree_markings.add(label) 

        self.play(Write(step1))
        self.play(Create(protractor), Create(protractor_center))
        self.wait(1)
        self.play(FadeOut(step1))

        # Step 2: Draw the base line
        step2 = Text("Step 2: Draw the base line with the help of  pencil.", color=WHITE, font_size=33).to_edge(DOWN)
        base_line = Line(ORIGIN, 3 * RIGHT, color=WHITE)
        
        self.play(Write(step2))
        self.play(Create(base_line))
        self.wait(1)
        self.play(FadeOut(step2))

        # Step 3: Locate the 40° mark
        step3 = Text("Step 3: Locate the 40° mark on protractor.", color=WHITE, font_size=33).to_edge(DOWN)
        a = Text("40°",font_size=20).shift(1.6 * UP+RIGHT*1.57)
        angle_40_mark = Dot(1.3 * UP+RIGHT*1.57).rotate(1 * DEGREES).set_color(RED)
        
        self.play(Write(step3))
        self.play(Write(a))
        self.play(Create(angle_40_mark))
        self.wait(1)
        self.play(FadeOut(step3))

        # Step 4: Draw the angle line
        step4 = Text("Step 4: Draw the angle line from centre to marked point.", color=WHITE, font_size=33).to_edge(DOWN)
        angle_line = Line(ORIGIN, 2.3 * (np.cos(40 * DEGREES) * RIGHT + np.sin(40 * DEGREES) * UP), color=RED)
        
        self.play(Write(step4))
        self.play(Create(angle_line))
        self.wait(1)
        self.play(FadeOut(step4))

        # Step 5: Label the angle
        step5 = Text("Step 5: Label the angle", color=WHITE, font_size=33).to_edge(DOWN)
        angle_arc = Arc(radius=0.5, angle=40*DEGREES, color=GREEN)
        angle_label = MathTex("40^\\circ", color=GREEN).next_to(angle_arc, RIGHT).shift(0.3 * UP)
        
        self.play(Write(step5))
        self.play(Create(angle_arc), Write(angle_label))
        self.wait(1)
        self.play(FadeOut(step5))

        # Final message
        final_message = Text("A   40° angle is drawn", color=WHITE, font_size=33).to_edge(DOWN)
        self.play(Write(final_message))
        self.wait(4)

        # Fade out everything
        self.play(
            FadeOut(protractor), FadeOut(protractor_center), FadeOut(degree_markings),
            FadeOut(base_line), FadeOut(angle_line), FadeOut(angle_arc),
            FadeOut(angle_label), FadeOut(title), FadeOut(final_message),
            FadeOut(angle_40_mark),FadeOut(a)
        )





######     CONSTRUCTING A COPY OF AN ANGLE OF UNKNOWN MEASURE




   
    def CopyAngleWithCompass(self):
           # Title for the scene
        title = Text("CONSTRUCTING A COPY OF AN ANGLE OF UNKNOWN MEASUREMENT",font_size= 27,color = YELLOW).to_edge(UP)
        self.play(Write(title))
        self.wait(3)
     
        # Step 1: Create the original angle
        point_A = Dot(ORIGIN, color=YELLOW)
        point_B = Dot(2*RIGHT, color=YELLOW)
        point_C = Dot(2*UP+RIGHT, color=YELLOW)
        
        line_AB = Line(point_A.get_center(), point_B.get_center())
        line_AC = Line(point_A.get_center(), point_C.get_center())
        
        original_angle = Angle(line_AB, line_AC, radius=0.5, color=BLUE)
        
        label_A = Text("A").next_to(point_A, DOWN+LEFT, buff=0.1).scale(0.7)
        label_B = Text("B").next_to(point_B, DOWN, buff=0.1).scale(0.7)
        label_C = Text("C").next_to(point_C, UP, buff=0.1).scale(0.7)

        step1_text = Text(" Unknown measurement angle diagram of ABC").scale(0.8).to_edge(DOWN)
        
        self.play(
            Create(VGroup(point_A, point_B, point_C, line_AB, line_AC, original_angle)),
            Write(VGroup(label_A, label_B, label_C)),
            Write(step1_text)
        )
        self.wait(2)

        # Step 2: Draw the base line for the new angle
        step2_text = Text("Step 1: Now draw base line PQ with pencil for coping \n angle of unknown measurement.").scale(0.65).to_edge(DOWN)
        point_D = Dot(3*LEFT + 2*DOWN, color=YELLOW)
        point_E = Dot(-1*RIGHT + 2*DOWN, color=YELLOW)
        base_line = Line(point_D.get_center(), point_E.get_center())
        
        label_D = Text("P").next_to(point_D, DOWN, buff=0.1).scale(0.7)
        label_E = Text("Q").next_to(point_E, DOWN, buff=0.1).scale(0.7)
        

        self.play(ReplacementTransform(step1_text, step2_text))
        self.wait(6)
        self.play(
            
            Create(VGroup(point_D, point_E, base_line)),
            Write(VGroup(label_D, label_E))
        )
        self.wait(3)

        # Step 3: Draw an arc with compass centered at the vertex of the original angle
        step3_text = Text("Step 2: Now setup the pencil with compass and place the compass\n at A and draw an arc to cut the lines AC and AB.").scale(0.65).to_edge(DOWN)
        arc1 = Arc(radius=2, angle=original_angle.get_value(), color=RED)
        arc1.shift(point_A.get_center())

        self.play(ReplacementTransform(step2_text, step3_text))
        self.wait(6)
        self.play(Create(arc1))
        self.wait(3)

        # Step 4: Draw an arc with the same radius centered at the start of the new base line
        step4_text = Text("Step 3: Use the same compasses setting to draw an arc with\n P as centre, cutting  at Q.").scale(0.7).to_edge(DOWN)
        arc2 = Arc(radius=2, angle=PI/2.9, color=RED)
        arc2.shift(point_D.get_center())
        
        self.play(ReplacementTransform(step3_text, step4_text))
        self.wait(4)
        self.play( Create(arc2))
        self.wait(2.5)

        # Step 5: Draw a line from the start of the base line to the intersection of the arcs
        step5_text = Text("Step 4:  Set your compasses with BC as the radius and Place the \ncompasses pointer at Q and draw an arc to cut the existing arc at R").scale(0.7).to_edge(DOWN)
        point_F = Dot(point_D.get_center() + 1.8*UP+RIGHT, color=YELLOW)
        new_line = Line(point_D.get_center(), point_F.get_center(), color=GREEN)
        
        label_F = Text("R").next_to(point_F, UP, buff=0.1).scale(0.7)
        
        self.play(ReplacementTransform(step4_text, step5_text))
        self.wait(6)
        self.play(
        
            Create(VGroup(point_F)),
            Write(label_F)
        )
        self.wait(2.5)
        

        # Step 6: Highlight the copied angle
        step6_text = Text("Step 5:  Join PR. This gives us ∠RPQ. It has the same \nmeasure as ∠CAB.").scale(0.7).to_edge(DOWN)
        copied_angle = Angle(base_line, new_line, radius=0.5, color=GREEN)
        
        self.play(ReplacementTransform(step5_text, step6_text))
       
        self.wait(6)
        self.play(Create(VGroup(new_line)))
        self.wait(1.5)
        self.play( Create(copied_angle))
        self.wait(3)

        # Add final labels
        original_label = Text("Original Angle of Unknown \nmeasurement ABC",color=BLUE).scale(0.6).next_to(original_angle, UP+LEFT)
        copied_label = Text("Copied Angle PQR",color=BLUE).scale(0.55).next_to(copied_angle, DOWN*-1+LEFT)
        
        self.play(Write(original_label), Write(copied_label))
        self.wait(3.7)

        # Optional: Clean up and show only the final result
        final_text = Text("Final Result: ∠ABC ≅ ∠PQR").scale(0.8).to_edge(DOWN)
        self.wait(3.2)
        self.play(
            FadeOut(arc1, arc2, step6_text),
            ReplacementTransform(VGroup(original_label, copied_label), final_text)
        )
        self.wait(3.5)


################################
         
        
    def Bisect(self):
      

      title = Text("CONSTRUCTION TO BISECT A GIVEN ANGLE",font_size= 36,color = ORANGE).to_edge(UP)
      self.play(Write(title))
      self.wait(3)
        # Step text configurations with smaller font size
      step1_text = Text("Step 1:  With O as centre and any convenient radius, draw\n\n an arc  PQ cutting OM and ON at P and Q respectively .",color = WHITE).scale(0.7).to_edge(DOWN*1.75)
      # self.play(Write(step1_text))
      # self.wait(5)
      


      line_l = Line(LEFT *0.38+DOWN*1 , RIGHT * 4+DOWN*1)
      self.play(Create(line_l))
      O = Dot(LEFT *0.38+DOWN*1)
      self.play(Create(O))
           
        # Label points
      O_label = MathTex("O",color = BLUE).next_to(LEFT *0.38+DOWN*1, DOWN)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
      self.play(Write(O_label))
      self.wait(0.3)

      N = Dot(LEFT *-2.5+DOWN*1)
      self.play(Create(N))
      self.wait(0.4)
           
        # Label points
      N_label = MathTex("N",color = BLUE).next_to(LEFT *-2.5+DOWN*1, DOWN)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
      self.play(Write(N_label))
      self.wait(0.3)

      angle_degrees = 60
      angle_radians = angle_degrees* DEGREES
      angle_line = Line( ORIGIN,2 * RIGHT).rotate(angle_radians).shift(DOWN*1+LEFT*0.47+UP*1.5).set_length(3.5)
      self.play(Create(angle_line))
      self.wait(0.3)


      M = Dot(DOWN*1+LEFT*-1.3+UP*2.8)
      self.play(Create(M))
      self.wait(0.3)
           
        # Label points
      M_label = MathTex("M",color = BLUE).next_to(DOWN*1+LEFT*-1.3+UP*2.8, UP)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
      self.play(Write(M_label))
      self.wait(1.1)
      # self.play(FadeOut(step1_text))



 # Compass arcs

      
      step2_text = Text("Step 2: With P as centre and any radius slightly more than half\n\n of the length of PQ, draw an arc in the interior of the given angle.",color = PINK).scale(0.7).to_edge(DOWN*1.75)
      self.play(Write(step1_text))
      self.wait(6)
      

  # Compass arcs
      arc1 = Arc(radius=3.7, angle=PI/4, arc_center=LEFT *2+DOWN*1)
        
      arc1.set_color(YELLOW)
    
        
      self.play(Create(arc1))
      self.wait(1)
        

      Q = Dot(LEFT *-1.7+DOWN*1)
      self.play(Create(Q))
      self.wait(0.5)
           
        # Label points
      Q_label = MathTex("Q",color = BLUE).next_to(LEFT *-1.7+DOWN*1, DOWN)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
      self.play(Write(Q_label))
      

      P = Dot(DOWN*1+LEFT*-0.94+UP*2.2)
      self.play(Create(P))
      self.wait(0.6)
           
        # Label points
      P_label = MathTex("P",color = BLUE).next_to(DOWN*1+LEFT*-0.94+UP*2.2, UP+LEFT)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
      self.play(Write(P_label))
      self.wait(1.7)
      self.play(FadeOut(step1_text))
      


      step3_text = Text("Step 3: With Q as centre and without altering radius \n\n (as in step 2) draw another arc in the interior of ∠MON.",color = WHITE).scale(0.7).to_edge(DOWN*1.75)
      self.play(Write(step2_text))
      self.wait(6)
      


  # Compass arcs
      arc2 = Arc(radius=3, angle=PI/7, arc_center=LEFT *0.5+DOWN*1+UP*1)
        
      arc2.set_color(YELLOW)
    
      self.play(Create(arc2))
      self.wait(1)
      self.play(FadeOut(step2_text))
        
    
      self.play(Write(step3_text))
      self.wait(4)
 # Compass arcs
      arc3 = Arc(radius=3, angle=PI/7, arc_center=LEFT *0.5+DOWN*1+UP*1).rotate(70)
        
      arc3.set_color(YELLOW)
    
      self.play(Create(arc3))
      self.wait(2.5)
      self.play(FadeOut(step3_text))
        


      he = Text("label the intersect point has Z.",color=PINK).to_edge(DOWN).scale(0.8)
      self.play(Write(he))
      self.wait(2.5)
      z = Dot(LEFT *-2.39+DOWN*1.05+UP*1.68)
      self.play(Create(z))
      
     
        # Label points
      z_label = MathTex("Z",color = BLUE).next_to(LEFT *-2.39+DOWN*1.05+UP*1.68, UP+RIGHT)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
      self.play(Write(z_label))
    #   he = Text("Let the two arcs intersect at Z.",color=PINK).to_edge(DOWN).scale(0.8)
    #   self.play(Write(he))
      self.play(Unwrite(arc1))
      self.wait(1.4)
      self.play(Unwrite(he))
      
      step4_text = Text("Step 4: Draw a line OZ. Then OZ is the desired bisector of ∠MON..\n\nObserve ∠MOZ = ∠ZON.",color = WHITE).scale(0.7).to_edge(DOWN*1.75)
      self.play(Write(step4_text))
      self.wait(3)
      

      angle_degrees = 30
      angle_radians = angle_degrees* DEGREES
      angle_line = DashedLine( ORIGIN,3.47 * RIGHT).rotate(angle_radians).shift(DOWN*1.55+LEFT*0.47+UP*1.5).set_length(3.7)
      self.play(Create(angle_line))
      self.wait(3)
      self.play(FadeOut(step4_text))
#self.play(Write(angle_label))



        ################################



    def Compass60degree(self):

         # Title for the scene
        title = Text("CONSTRUCTING ANGLES OF SPECIAL MEASURES \n                        Construction of 60° Angle",font_size= 32,color = WHITE).to_edge(UP)
        self.play(Write(title))
        self.wait(4)
        # Step text configurations with smaller font size
        step1_text = Tex("Step 1: Draw a line  and mark a point $O$ on it.",color = ORANGE).scale(0.98).to_edge(DOWN*2.5)
        step2_text = Tex("Step 2: Place the pointer of the compasses at $O$ and draw an arc of convenient radius which cuts the line  at a point, say $A$.",color = BLUE).scale(0.78).to_edge(DOWN*2.5)
        step3_text = Tex("Step 3: With the pointer at $A$ (as center) and the same radius as in step 2, draw an arc that passes through $O$.",color = ORANGE).scale(0.77).to_edge(DOWN*2.5)
        step4_text = Tex("Step 4: Let the two arcs intersect at $B$. Join $OB$. We get $\\angle AOB$ whose measure is $60^\\circ$.",color = BLUE).scale(0.79).to_edge(DOWN*2.5)

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
        self.wait(6)
        self.play(Create(line_l))
        self.play(Create(point_O), Write(label_O))
        self.wait(1.5)
        self.play(FadeOut(step1_text))

        # Step 2: Draw arc from O
        self.play(Write(step2_text))
        self.wait(6.5)
        self.play(Create(arc_OA))
        self.play(Create(point_A), Write(label_A))
        self.wait(2)
        self.play(FadeOut(step2_text))

        # Step 3: Draw arc from A


        self.play(Write(step3_text))
        self.wait(6)
        self.play(Create(arc_AB))
        self.wait(1.7)
        self.play(FadeOut(step3_text))

        # Step 4: Mark point B, join OB, and label the angle
        A = Dot(RIGHT*1+UP*1.71)
        
        self.play(Write(step4_text))
        self.wait(6.3)
        self.play(Create(A))
        step_text = Tex("B").shift(RIGHT*1+UP*1.97)
        self.play(Write(step_text))
        self.wait(1.1)
        self.play(Create(point_B), Write(label_B))
        self.play(Create(line_OB))
        # Draw the angle line
        angle_degrees = 60
        angle_radians = angle_degrees * DEGREES
        angle_line = Line(ORIGIN, 2 * RIGHT).rotate(angle_radians).shift(DOWN*-0.85+LEFT*0.47)
        self.play(Create(angle_line))
        self.play(Write(angle_label))
        self.wait(5)
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
        step1_title = Text("Step 1:  Draw a line OA.", font_size=32,color=BLUE).next_to(title, DOWN).shift(DOWN * 5.55)
        self.play(Write(step1_title))
        self.wait(2.5)
    

       
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
        self.wait(4.5)

        a = Dot().next_to(P, DOWN*0+RIGHT*7.5)
        self.play(Create(a))

        start_label = MathTex("M",color = BLUE).next_to(P, DOWN+RIGHT*7)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
        self.play(Write(start_label))


        arc2 = Arc(radius=arc_radius, angle=PI ).move_arc_center_to(P.get_center()).shift(LEFT)
        self.play(Create(arc2))
        
 # Step 5: Mark the intersections of the arc with the original angle
        step5_title = Text("Step 3: Now, taking M as center and with the same radius\n as before,draw an arc intersecting the previously drawn arc at point P.", font_size=26,color=BLUE).next_to(title, DOWN).shift(DOWN * 5.6)
        self.play(Transform(step1_title, step5_title))
        self.wait(5.5)

        arc6 = Arc(radius=3, angle=PI/6.2, arc_center=RIGHT*1.3+DOWN*1.6+UP*1).rotate(90)
        arc6.set_color(YELLOW)
        self.play(Create(arc6))
        
        z = Dot(RIGHT*4.088+DOWN*1.6+UP*1.8)
        self.play(Create(z))
           
        # Label points
        z_label = MathTex("P",color = BLUE).next_to(RIGHT*4.088+DOWN*1.6+UP*1.8, UP+RIGHT)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
        self.play(Write(z_label))


        # arc7 = Arc(radius=3, angle=PI/6.5, arc_center=LEFT *2+DOWN*1+UP*1).rotate(90)
        # arc7.set_color(YELLOW)
        # self.play(Create(arc7))

       
      #  self.play( Create(mark_B))
       # self.wait(1)

        # Step 6: Copy the distances of the intersections to the new arc
        step6_title = Text("Step 4: With P as center and the same radius, draw an arc cutting the arc at Q", font_size=26,color=PINK).next_to(title, DOWN).shift(DOWN * 5.7)
        self.play(Transform(step1_title, step6_title))
        self.wait(5)
        arc7 = Arc(radius=3, angle=PI/6.5, arc_center=LEFT *2+DOWN*1+UP*1).rotate(90)
        arc7.set_color(YELLOW)
        self.play(Create(arc7))

     #   distance_AB = Line(intersect_A, intersect_B)
 
        # Find the intersection on the new arc
        intersect_Q = arc2.point_from_proportion(0.6)
        mark_Q = Dot(intersect_Q)

        self.play(Create(mark_Q))
        Q_label = MathTex("Q",color = BLUE).next_to(mark_Q, UP+LEFT)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
        self.play(Write(Q_label))

    

        # Step 7: Draw the second ray of the copied angle
        step7_title = Text("Step 5: Draw the line OQ .Therefore, ∠AOQ= 120°. ", font_size=32,color=BLUE).next_to(title, DOWN).shift(DOWN * 5.6)
        self.play(Transform(step1_title, step7_title))
        self.wait(2.9)

        copied_angle_side = Line(P.get_center(), mark_Q.get_center()).set_length(4)
        self.play(Create(copied_angle_side))
        self.wait(3.5)






        
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

        a = Dot().next_to(P, DOWN*0+RIGHT*7.5)
        self.play(Create(a))

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
        self.wait(2.5)
        self.play(FadeOut(step20_title))

#self.play(Write(angle_label))
        copied_angle_side = DashedLine(P.get_center(), mark_Q.get_center()).set_length(4)
        self.play(Create(copied_angle_side))

           # Step 7: Draw the second ray of the copied angle
        step7_title = Text("∠POQ = 60° and ∠AOQ= 120°", font_size=32,color=ORANGE).next_to(title, DOWN).shift(DOWN * 5.6)
        self.play(Write( step7_title))
        self.wait(3)
        self.play(FadeOut(step7_title))

  
       # Step 7: Draw the second ray of the copied angle
        step21_title = Text("We know that 90° = 60° + 30° and also 90° = 120° - 30°", font_size=32,color=ORANGE).next_to(title, DOWN).shift(DOWN * 5.6)
        self.play(Write(step21_title))
        self.wait(4)
        self.play(FadeOut(step21_title))

##### # Step 7: Draw the second ray of the copied angle
        step23_title = Text("So, we need to bisect ∠POQ to get an angle of 30°.", font_size=32,color=ORANGE).next_to(title, DOWN).shift(DOWN * 5.6)
        self.play(Write( step23_title))
        self.wait(4.5)
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
        self.wait(4.5)
        self.play(FadeOut(step27_title))





    def SetDeveloperList(self):
        self.DeveloperList = "Uday Kiran"   

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade6chapter13PracticalGeometry.py"      
        





if __name__ == "__main__":
    scene = Grade6chapter13PracticalGeometry()
    scene.render()