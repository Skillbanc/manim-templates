from manim import *
from AbstractAnim import AbstractAnim

import cvo


class basicgeometricalideas(AbstractAnim):

     def construct(self):
        # p1=cvo.CVO().CreateCVO("cname","oname")
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.Add()
        self.fadeOutCurrentScene()
        self.introduction()
        self.fadeOutCurrentScene()
        self.point1()
        self.fadeOutCurrentScene()
        self.linesegment1()
        self.fadeOutCurrentScene()
        self.line1()
        self.fadeOutCurrentScene()
        self.ray1()
        self.fadeOutCurrentScene()
        self.curve1()
        self.fadeOutCurrentScene()
        self.polygon1()
        self.fadeOutCurrentScene()
        self.angle1()
        self.fadeOutCurrentScene()
        self.triangle1()
        self.fadeOutCurrentScene()
        self.quadrilateral1()
        self.fadeOutCurrentScene()
        self.Circle1()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

      
     def Add(self):
        self.isRandom = False
        t1 = Text("Basic Geometrical Ideas", font_size=35)
        t1.move_to([0, 0, 0])
        # Write the text and the underline
        self.play(Write(t1))
        self.wait(2)

     def introduction(self):
        # p1=cvo.CVO().CreateCVO("cname","oname")
        self.angleChoice = [TAU/4,TAU/4,TAU/4,TAU/4,TAU/4]
        
        p10=cvo.CVO().CreateCVO("Basic Geometrical Shapes", "").setPosition([-4.5,-1,0])
        p11=cvo.CVO().CreateCVO("Point","").setPosition([-4,2,0])
        p12=cvo.CVO().CreateCVO("Line Segment","").setPosition([-1.25,2.25,0])
        p13=cvo.CVO().CreateCVO("Line","").setPosition([1.5,1.15,0])
        p14=cvo.CVO().CreateCVO("Ray","").setPosition([3.5,0,0])
        p15=cvo.CVO().CreateCVO("Curve","").setPosition([4.5,-2.5,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
         
        self.construct1(p10,p10)


     def point1(self):

        point = Text("Point").to_edge(UP*1)
        sub_title1 = Text("A point is a precise location in space with no size, length, width, or height,",font_size=29).to_edge(UP*3.0)
        sub_title2 = Text("usually represented by a dot and labeled with a letter"'.',font_size=29).to_edge(UP*4.5)

        self.play(Write(point))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))

        # Create a point
        point = Dot(point=ORIGIN, color=BLUE).shift(RIGHT * -1).to_edge(UP*6.5)
        point_label = Text("Point",font_size=30).next_to(point, RIGHT)

        # Display the point
        self.play(Write(point), Write(point_label))
        self.wait(1)

        properties = Text("Properties "':',font_size=35).shift(LEFT * 5.5 ).to_edge(UP*8)
        sub_title1 = Text('1. '"A point determines a location"'.',font_size=29).to_edge(UP*9.5).shift(LEFT * 3.8 )
        sub_title2 = Text('2. '"A point has no length, width, or height"'.',font_size=29).to_edge(UP*11).shift(LEFT * 3.0 )
        sub_title3 = Text('3. '"Points are usually denoted by a single capital letter"'.',font_size=29).to_edge(UP*12.5).shift(LEFT * 1.9)

        self.play(Write(properties))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)
        self.play(Write(sub_title3))

     def linesegment1(self):

        linesegment = Text("Line Segment").to_edge(UP*1)
        sub_title1 = Text("A line segment is a part of a line that has two endpoints and a definite length"'.',font_size=29).to_edge(UP*3.0)
        
        self.play(Write(linesegment))
        self.play(Write(sub_title1))

        A = Dot(point=LEFT, color=YELLOW).to_edge(UP*5.5)
        B = Dot(point=RIGHT, color=YELLOW).to_edge(UP*5.5)
        line_segment = Line(start=A.get_center(), end=B.get_center(), color=RED)
        A_label = Text("A",font_size=30).next_to(A, DOWN).to_edge(UP*5.5).shift(LEFT * 0.3)
        B_label = Text("B",font_size=30).next_to(B, DOWN).to_edge(UP*5.5).shift(RIGHT * 0.3 )

        # Display the line with arrows
        self.play(Write(A), Write(B), Write(line_segment),Write(A_label),Write(B_label))
        self.wait(1)
    
        properties = Text("Properties"':',font_size=35).shift(LEFT * 5.5 ).to_edge(UP*7.5)
        sub_title1 = Text('1. '"A line segment has a fixed length"'.',font_size=29).to_edge(UP*9).shift(LEFT * 3.5 )
        sub_title2 = Text('2. '"A line segment is straight with no curves"'.',font_size=29).to_edge(UP*10.5).shift(LEFT * 2.9 )
        sub_title3 = Text('3. '"A line segment has two distinct endpoints"'.',font_size=29).to_edge(UP*12).shift(LEFT * 2.75)
        
        self.play(Write(properties))
        self.play(Write(sub_title1))
        self.wait(0)
        self.play(Write(sub_title2))
        self.wait(0)
        self.play(Write(sub_title3))

     def line1(self):
        line = Text("Line").to_edge(UP*1)
        sub_title1 = Text("A line is a straight path that extends infinitely in both directions with",font_size=29).to_edge(UP*3.0)
        sub_title2 = Text("no thickness and is usually defined by two points"'.',font_size=29).to_edge(UP*4.5)

        self.play(Write(line))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))

        # Create a line with arrows   
        infinite_line = Line(start=LEFT*1, end=RIGHT*1, color=GREEN).to_edge(UP*7.0)
        left_arrow = Arrow(start=LEFT*0.5, end=LEFT*1, color=GREEN, buff=0).to_edge(UP*6.859)
        right_arrow = Arrow(start=RIGHT*0.5, end=RIGHT*1, color=GREEN, buff=0).to_edge(UP*6.859)
        line_label = Text("Line",font_size=35).next_to(infinite_line, UP)
  
        # Display the line with arrows
        self.play(Write(infinite_line), Write(left_arrow), Write(right_arrow), Write(line_label))
        self.wait(1)

        properties = Text("Properties"':',font_size=35).shift(LEFT * 5.5 ).to_edge(UP*8.5)
        sub_title1 = Text('1. '"A line has no width or thickness"'.',font_size=29).to_edge(UP*10).shift(LEFT * 3.7 )
        sub_title2 = Text('2. '"A line is perfectly straight with no curves"'.',font_size=29).to_edge(UP*11.5).shift(LEFT * 2.9 )
        sub_title3 = Text('3. '"A line extends infinitely in both directions"'.',font_size=29).to_edge(UP*13).shift(LEFT * 2.75)

        self.play(Write(properties))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)
        self.play(Write(sub_title3))

     def ray1(self):
        Ray = Text("Ray").to_edge(UP*1)
        sub_title1 = Text("A ray is a part of a line that starts at one point and extends infinitely",font_size=29).to_edge(UP*3.0)
        sub_title2 = Text("in one direction"'.',font_size=29).to_edge(UP*4.5)

        self.play(Write(Ray))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))

        # Create a ray starting from a point
        ray_start = Dot(point=ORIGIN, color=PURPLE)
        ray = Line(start=ray_start.get_center(), end=RIGHT*5.5, color=PURPLE)
        ray_arrow = Arrow(start=RIGHT*4.5, end=RIGHT*5.5, color=PURPLE, buff=0)
        ray_label = Text("Ray",font_size=30).next_to(ray, UP)

        # Display the ray with an arrow
        self.play(Write(ray_start), Write(ray), Write(ray_arrow), Write(ray_label))
        self.wait(0)

        properties = Text("Properties"':',font_size=30).to_edge(UP*8.0).shift(LEFT * 5.7 )
        sub_title1 = Text('1. '"A ray is straight with no curves"'.',font_size=29).to_edge(UP*9.5).shift(LEFT * 3.8 )
        sub_title2 = Text('2. '"A ray has one fixed endpoint where it begins"'.',font_size=29).to_edge(UP*11).shift(LEFT * 2.5)
        sub_title3 = Text('3. '"A ray extends infinitely in one direction from its starting point"'.',font_size=29).to_edge(UP*12.5).shift(LEFT * 1)

        self.play(Write(properties))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)
        self.play(Write(sub_title3))
  
     def curve1(self):
        curve = Text("Curve",font_size=40).to_edge(UP*1)
        sub_title1 = Text("A curve in mathematics is a one-dimensional continuous set of points"'.',font_size=29).to_edge(UP*3.0)
        
        self.play(Write(curve))
        self.play(Write(sub_title1))
        self.wait(1)


        # Define the cosine wave function
        cosine_wave = FunctionGraph(
            lambda x: np.cos(x),
            x_range=[-PI, PI],
            color=BLUE
        )
        
        # Add the cosine wave to the scene
        self.play(Create(cosine_wave))
        self.wait(0)
        self.play(FadeOut(curve))
        self.play(FadeOut(sub_title1))
        self.play(FadeOut(cosine_wave))


        opencurve = Text("Open Curve",font_size=40).to_edge(UP*1)
        sub_title1 = Text("An open curve is a curve that does not form a closed loop"'.',font_size=29).to_edge(UP*3.0)
        
        self.play(Write(opencurve))
        self.play(Write(sub_title1))
        self.wait(1)

        # Define the sine wave function
        sine_wave = FunctionGraph(
            lambda x: np.sin(x),
            x_range=[-PI, PI],
            color=BLUE
        )
        # Add the sine wave to the scene
        self.play(Create(sine_wave))
        self.wait(0)
        self.play(FadeOut(opencurve))
        self.play(FadeOut(sub_title1))
        self.play(FadeOut(sine_wave))
        
        closedcurve = Text("Closed Curve",font_size=40).to_edge(UP*1)
        sub_title1 = Text("A closed curve in mathematics is a curve that forms a loop,",font_size=29).to_edge(UP*3.0)
        sub_title2 = Text("meaning its endpoints meet"'.',font_size=29).to_edge(UP*4.5)

        self.play(Write(closedcurve))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))

        ellipse = Ellipse(width=4.0, height=2.0, color=BLUE).to_edge(UP*8)
        self.play(Create(ellipse))
        self.wait(0)
    
     def polygon1(self):
         # Define the titles and subtitles
        polygon_title = Text("Polygon", font_size=40).to_edge(UP*1)
        sub_title1 = Text("A polygon is a two-dimensional figure consisting of a finite number of straight", font_size=29).to_edge(UP*3.0)
        sub_title2 = Text("line segments connected end-to-end to form a closed loop or circuit.", font_size=29).to_edge(UP*4.5)

        # Display the titles and subtitles
        self.play(Write(polygon_title))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)

        # Create a regular pentagon centered on the screen
        pentagon = RegularPolygon(n=5, color=BLUE, fill_opacity=0.5)
        pentagon.set_fill(BLUE, opacity=0.5)
        pentagon.set_stroke(BLUE, width=2)
        pentagon.move_to(ORIGIN)

        # Add the pentagon to the scene
        self.play(Create(pentagon))
        self.wait(1)

        # Example subtitle should be below the figure
        example = Text("Example of Polygon with 5 Line Segments", font_size=30).next_to(ORIGIN, DOWN * 3).shift(LEFT * 0).to_edge(UP*11)
        self.play(Write(example))

        # Fade out everything
        self.play(FadeOut(polygon_title), FadeOut(sub_title1), FadeOut(sub_title2), FadeOut(example), FadeOut(pentagon))


     def angle1(self):
        point = Text("Angle").to_edge(UP*1)

        self.play(Write(point))
        # Define points
        vertex = ORIGIN
        pointA = [3, 2, 0]
        pointB = [3, -2, 0]

        # Create rays
        ray_OA = Line(vertex, pointA, color=BLUE).shift(RIGHT * 3 )
        ray_OB = Line(vertex, pointB, color=GREEN).shift(RIGHT * 3 )

        # Create labels for the rays
        label_OA = MathTex("OA").next_to(ray_OA, UP).shift(UP * -1)
        label_OB = MathTex("OB").next_to(ray_OB, DOWN).shift(DOWN * -1)
        label_O = MathTex("O").next_to(vertex, LEFT).shift(RIGHT * 3 )

        # Create the angle arc
        angle_arc = Arc(
            radius=1,
            start_angle=ray_OA.get_angle(),
            angle=ray_OB.get_angle() - ray_OA.get_angle(),
            color=YELLOW
        ).shift(RIGHT * 3)

        # Create the angle label
        angle_label = MathTex(r"\theta").move_to(angle_arc.point_from_proportion(0.5) + RIGHT * 0.5)

        # Add the rays, labels, and the angle arc to the scene
        self.play(Create(ray_OA), Write(label_OA))
        self.play(Create(ray_OB), Write(label_OB))
        self.play(Write(label_O))
        self.play(Create(angle_arc), Write(angle_label))
        self.wait(1)

        sub_title1 = Text("Angles are made when corners are formed"'.',font_size=29).to_edge(UP*3.0).shift(LEFT * 3)
        sub_title2 = Text("In the figure imagine two rays say OA and OB"'.',font_size=29).to_edge(UP*4.5).shift(LEFT * 2.7)
        sub_title3 = Text("These two rays have a common end point at O"'.',font_size=29).to_edge(UP*6).shift(LEFT * 2.7)
        sub_title4 = Text("The two rays here are said to form an angle"'.',font_size=29).to_edge(UP*7.5).shift(LEFT * 3)
        sub_title5 = Text("The two rays forming an angle are called the arms"'.',font_size=29).to_edge(UP*9).shift(LEFT * 2.5)
        sub_title6 = Text("Here the two rays OA and OB are two arms"'.',font_size=29).to_edge(UP*10.5).shift(LEFT * 3)
        sub_title7 = Text("O is the vertex of the angle"'.',font_size=29).to_edge(UP*12).shift(LEFT * 4.4)
        sub_title8 = Text("we read it as angle AOB or angle BOA"'.',font_size=29).to_edge(UP*13.5).shift(LEFT * 3.5)
        sub_title9 = Text("it is denoted by ∠AOB or ∠BOA or  simply ∠O"'.',font_size=29).to_edge(UP*15).shift(LEFT * 2.5)


        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)
        self.play(Write(sub_title3))
        self.wait(1)
        self.play(Write(sub_title4))
        self.wait(1)
        self.play(Write(sub_title5))
        self.wait(1)
        self.play(Write(sub_title6))
        self.wait(1)
        self.play(Write(sub_title7))
        self.wait(1)
        self.play(Write(sub_title8))
        self.wait(1)
        self.play(Write(sub_title9))


     def triangle1(self):
        # Define the titles and subtitles
        triangle_title = Text("Triangle", font_size=40).to_edge(UP*1)
        sub_title1 = Text("The simple closed figure formed by three line segments is a triangle.", font_size=29).to_edge(UP*3.0)
        sub_title2 = Text("The line segments are called sides.", font_size=29).to_edge(UP*4.5)
        
        # Display the titles and subtitles
        self.play(Write(triangle_title))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)
        
        # Create a triangle ABC centered on the screen
        A = np.array([-2, -1, 0])
        B = np.array([2, -1, 0])
        C = np.array([0, 1, 0])

        # Position the triangle exactly below sub_title2
        triangle_shape = Polygon(A, B, C, color=PINK, fill_opacity=0.3).next_to(sub_title2, DOWN, buff=0.5)
        label_A = MathTex("A", font_size=30, color=BLUE).next_to(triangle_shape.get_vertices()[0], LEFT)
        label_B = MathTex("B", font_size=30, color=BLUE).next_to(triangle_shape.get_vertices()[1], RIGHT)
        label_C = MathTex("C", font_size=30, color=BLUE).next_to(triangle_shape.get_vertices()[2], UP)

        self.play(Create(triangle_shape), Write(label_A), Write(label_B), Write(label_C))
        self.wait(1)
        
        # Example subtitle should be below the triangle and adjusted to avoid overlapping
        sub_title4 = Text("Example: The triangle formed by three line segments AB, BC, CA.", font_size=29).next_to(triangle_shape, DOWN * 2)
        sub_title3 = Text("Here A, B, C are called three vertices of the triangle ABC.", font_size=29).next_to(sub_title4, DOWN, buff=0.5)
        
        self.play(Write(sub_title4))
        self.wait(1)
        self.play(Write(sub_title3))
        self.wait(1)

        # Fade out everything
        self.play(FadeOut(triangle_title), FadeOut(sub_title1), FadeOut(sub_title2), FadeOut(sub_title3), FadeOut(sub_title4), FadeOut(triangle_shape), FadeOut(label_A), FadeOut(label_B), FadeOut(label_C))


     def quadrilateral1(self):
        # Define the titles and subtitles
        quadrilateral_title = Text("Quadrilateral", font_size=40).to_edge(UP * 1)
        sub_title1 = Text("Quadrilateral is a simple closed polygon with four line segments.", font_size=29).to_edge(UP * 3.5)
        sub_title2 = Text("Example: A Quadrilateral formed by four line segments AB, BC, CD, DA.", font_size=29).to_edge(UP * 6 + LEFT * 1)
        sub_title3 = Text("∠A, ∠B, ∠C and ∠D are its four angles.", font_size=29).to_edge(UP * 8 + LEFT * 1)
        sub_title4 = Text("Line segments joining opposite vertices A, C and B, D", font_size=29).to_edge(UP * 10 + LEFT * 1)
        sub_title5 = Text("namely AC and BD, are called its two diagonals.", font_size=29).to_edge(UP * 12 + LEFT * 1)

        self.play(Write(quadrilateral_title))
        self.wait(1)
        self.play(Write(sub_title1))
        self.wait(1)

        # Define points A, B, C, D
        A = np.array([2, -3, 0])
        B = np.array([6, -3, 0])
        C = np.array([5, 0, 0])
        D = np.array([3, -1, 0])

        # Create quadrilateral ABCD
        quadrilateral_shape = Polygon(A, B, C, D, color=BLUE)
        label_A = MathTex("A", color=BLUE).next_to(A, DOWN)
        label_B = MathTex("B", color=BLUE).next_to(B, DOWN)
        label_C = MathTex("C", color=BLUE).next_to(C, UP)
        label_D = MathTex("D", color=BLUE).next_to(D, UP)

        # Calculate and draw diagonals AC and BD
        diagonal_AC = Line(A, C, color=DARK_BROWN)
        diagonal_BD = Line(B, D, color=GREEN)

        # Create labels for diagonals
        label_AC = MathTex("AC", color=DARK_BROWN).move_to((A + C) / 2).shift(UP * 0.5)
        label_BD = MathTex("BD", color=GREEN).move_to((B + D) / 2).shift(DOWN * 0.5)

        # Display the quadrilateral and its labels
        self.play(Create(quadrilateral_shape),
                  Write(label_A), Write(label_B), Write(label_C), Write(label_D))
        self.wait(1)

        # Draw diagonals
        self.play(Create(diagonal_AC), Write(label_AC))
        self.play(Create(diagonal_BD), Write(label_BD))
        self.wait(2)

        # Display the subtitles
        self.play(Write(sub_title2))
        self.wait(1)
        self.play(Write(sub_title3))
        self.wait(1)
        self.play(Write(sub_title4))
        self.wait(1)
        self.play(Write(sub_title5))
        self.wait(2)

        # Fade out everything
        self.play(FadeOut(quadrilateral_title), FadeOut(sub_title1), FadeOut(sub_title2),
                  FadeOut(sub_title3), FadeOut(sub_title4), FadeOut(sub_title5),
                  FadeOut(quadrilateral_shape), FadeOut(label_A), FadeOut(label_B),
                  FadeOut(label_C), FadeOut(label_D), FadeOut(diagonal_AC), FadeOut(label_AC),
                  FadeOut(diagonal_BD), FadeOut(label_BD))

     def Circle1(self):
        circle1 = Text("Circle",font_size=40).to_edge(UP*1)
        sub_title1 = Text("A circle is a shape consisting of all points in a plane that are",font_size=29).to_edge(UP*3.0)
        sub_title2 = Text("equidistant from a fixed point called the center"'.',font_size=29).to_edge(UP*4.5)

        self.play(Write(circle1))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)
        self.play(FadeOut(circle1), FadeOut(sub_title1), FadeOut(sub_title2))

        # Draw the circle
        circle = Circle().to_edge(UP*6)
        self.play(Create(circle))
        self.wait(1)

        center = Text("Center",font_size=40).to_edge(UP*1)
        sub_title1 = Text("The center of a circle is a point that is equidistant from all points on the circle"'.',font_size=29).to_edge(UP*3.0)

        self.play(Write(center))
        self.play(Write(sub_title1))
        self.wait(1)

        # Show center
        center_dot = Dot(circle.get_center(), color=YELLOW)
        center_label = Text("Center",font_size=30).next_to(center_dot, DOWN)
        self.play(FadeIn(center_dot), Write(center_label))
        self.wait(1)
        self.play(FadeOut(center_dot), FadeOut(center_label))
        self.play(FadeOut(center), FadeOut(sub_title1))

        radius = Text("Radius",font_size=40).to_edge(UP*1)
        sub_title1 = Text("The distance from the center to any point on the circle is called the radius"'.',font_size=29).to_edge(UP*3.0)
        
        self.play(Write(radius))
        self.play(Write(sub_title1))
        self.wait(1)

        # Show radius
        radius_line = Line(circle.get_center(), circle.get_right(), color=BLUE)
        radius_label = Text("Radius",font_size=30).next_to(radius_line, UP)
        self.play(Create(radius_line), Write(radius_label))
        self.wait(1)
        self.play(FadeOut(radius_line), FadeOut(radius_label))
        self.play(FadeOut(radius), FadeOut(sub_title1))

        diameter = Text("Diameter",font_size=40).to_edge(UP*1)
        sub_title1 = Text("The diameter of a circle is the straight line distance that passes through",font_size=29).to_edge(UP*3.0)
        sub_title2 = Text("the center of the circle, connecting two points on its circumference"'.',font_size=29).to_edge(UP*4.5)
        
        self.play(Write(diameter))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)

        # Show diameter
        center_dot = Dot(circle.get_center(), color=YELLOW)
        diameter_line = Line(circle.get_left(), circle.get_right(), color=RED)
        diameter_label = Text("Diameter",font_size=30).next_to(diameter_line, DOWN)
        self.play(Create(diameter_line), Write(diameter_label), Create(center_dot))
        self.wait(1)
        self.play(FadeOut(diameter_line), FadeOut(diameter_label))
        self.play(FadeOut(diameter), FadeOut(sub_title1), FadeOut(sub_title2), FadeOut(center_dot))


        chord = Text("Chord",font_size=40).to_edge(UP*1)
        sub_title1 = Text("A chord of a circle is a straight line segment whose endpoints both lie",font_size=29).to_edge(UP*3.0)
        sub_title2 = Text("on the circumference of the circle"'.',font_size=29).to_edge(UP*4.5)
        
        self.play(Write(chord))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)

        # Show chord
        chord_line = Line(circle.point_at_angle(PI/4), circle.point_at_angle(3*PI/4), color=GREEN)
        chord_label = Text("Chord",font_size=30).next_to(chord_line, DOWN)
        self.play(Create(chord_line), Write(chord_label))
        self.wait(1)
        self.play(FadeOut(chord_line), FadeOut(chord_label))
        self.play(FadeOut(chord), FadeOut(sub_title1), FadeOut(sub_title2))

        sector1 = Text("Sector",font_size=40).to_edge(UP*1)
        sub_title1 = Text("A sector of a circle is a region bounded by two radii of the circle and",font_size=29).to_edge(UP*3.0)
        sub_title2 = Text("the arc between their endpoints"'.',font_size=29).to_edge(UP*4.5)
        
        self.play(Write(sector1))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)
 
        # Show sector
        sector = Sector(angle=PI/4, color=PURPLE, arc_center=circle.get_center())
        sector_label = Text("Sector",font_size=30).next_to(sector, DOWN)
        self.play(FadeIn(sector), Write(sector_label))
        self.wait(1)
        self.play(FadeOut(sector), FadeOut(sector_label))
        self.play(FadeOut(sector1), FadeOut(sub_title1), FadeOut(sub_title2))

        segment1 = Text("Segment",font_size=40).to_edge(UP*1)
        sub_title1 = Text("A segment of a circle is a region bounded by a chord and",font_size=29).to_edge(UP*3.0)
        sub_title2 = Text("the arc that the chord subtends"'.',font_size=29).to_edge(UP*4.5)
        
        self.play(Write(segment1))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)

        # Show segment
        segment = Polygon(circle.get_center(), circle.point_at_angle(PI/4), circle.point_at_angle(3*PI/4), color=ORANGE)
        segment_label = Text("Segment",font_size=30).next_to(segment, DOWN)
        self.play(Create(segment), Write(segment_label))
        self.wait(1)
        self.play(FadeOut(segment), FadeOut(segment_label))
        self.play(FadeOut(segment1), FadeOut(sub_title1), FadeOut(sub_title2))
  
        semicircularregion = Text("Semi-circular region", font_size=40).to_edge(UP*1)
        sub_title1 = Text("A semi-circular region is half of a circle, bounded by a diameter and the arc", font_size=29).to_edge(UP*3.0)
        sub_title2 = Text("connecting the endpoints of the diameter.", font_size=29).to_edge(UP*4.5)
        
        self.play(Write(semicircularregion))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)

        # Show semi-circular region
        semicircle = Arc(arc_center=ORIGIN, radius=1, start_angle=0, angle=PI, color=TEAL)
        semicircle.set_fill(TEAL, opacity=0.5)
        semicircle_label = Text("Semi-circular Region", font_size=30).next_to(semicircle, DOWN)
        self.play(Create(semicircle), Write(semicircle_label))
        self.wait(1)
        self.play(FadeOut(semicircle), FadeOut(semicircle_label))
        self.play(FadeOut(semicircularregion), FadeOut(sub_title1), FadeOut(sub_title2), FadeOut(circle))

        # Define and display the main title and subtitles
        circumference = Text("Circumference", font_size=40).to_edge(UP * 1)
        sub_title1 = Text("The circumference of a circle is the total distance around the circle.", font_size=29).to_edge(UP * 3.0)
        sub_title2 = Text("It is the circle's perimeter.", font_size=29).to_edge(UP * 4.5)
        
        self.play(Write(circumference))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)

        # Define the circle and move it to the center
        c = Circle(color=BLUE, radius=1)
        c.move_to(ORIGIN)

        # Display the circle
        self.play(Write(c))

        # Define and display the text "circumference" with increased font size to the right of the circle
        t6 = Text("circumference", font_size=30)
        t6.next_to(c, RIGHT, buff=1)
        self.play(Write(t6))
        self.wait(1)

        # Highlight the circumference text and the circle
        self.play(
            AnimationGroup(
                Indicate(c, color=YELLOW),
                Indicate(t6, color=YELLOW),
                lag_ratio=0  # Ensures both animations happen simultaneously
            )
        )



     def SetDeveloperList(self):  
        self.DeveloperList="Akshitha"

         
     def SetSourceCodeFileName(self):
        self.SourceCodeFileName="basicgeometricalideas.py"




if __name__ == "__main__":
    scene = basicgeometricalideas()
    scene.render()