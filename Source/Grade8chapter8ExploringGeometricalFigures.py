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


class Grade8chapter8ExploringGeometricalFigures(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Title()
        self.fadeOutCurrentScene()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.congruency()
        self.fadeOutCurrentScene()
        self.congruent()
        self.fadeOutCurrentScene()
        self.rotation()
        self.fadeOutCurrentScene()
        self.flipping()
        self.fadeOutCurrentScene()
        self.similaritycheck1()
        self.fadeOutCurrentScene()
        self.similaritycheck2()
        self.fadeOutCurrentScene()
        self.constructDataByCVO() #
        self.fadeOutCurrentScene()
        self.constdilation()
        self.fadeOutCurrentScene()
        self.symmetry()
        self.fadeOutCurrentScene()
        self.linesymmetry()
        self.fadeOutCurrentScene()
        self.rotationalsymmetry()
        self.fadeOutCurrentScene()
        self.pointsymmetry()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()



    def Title(self):
        # Title
        title = Text("Exploring Geometrical Figures ", font_size=70)
        self.play(Write(title))
        self.wait(3)
        self.play(Unwrite(title))
        self.wait(2)  






    def Introduction(self):

        # Create a title
        title = Text("Geometric Shapes").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Circle
        circle = Circle(radius=1.5, color=RED)
        circle_text = Text("Circle").next_to(circle, DOWN)
        self.play(Create(circle), Write(circle_text))
        self.wait(2)
        self.play(FadeOut(circle), FadeOut(circle_text))

        # Rectangle
        rectangle = Rectangle(width=3, height=2, color=BLUE)
        rectangle_text = Text("Rectangle").next_to(rectangle, DOWN)
        self.play(Create(rectangle), Write(rectangle_text))
        self.wait(2)
        self.play(FadeOut(rectangle), FadeOut(rectangle_text))

        # Square
        square = Square(side_length=2, color=GREEN)
        square_text = Text("Square").next_to(square, DOWN)
        self.play(Create(square), Write(square_text))
        self.wait(2)
        self.play(FadeOut(square), FadeOut(square_text))

        # Rhombus
        rhombus = Polygon([-1,0,0], [0,1,0], [1,0,0], [0,-1,0], color=YELLOW)
        rhombus_text = Text("Rhombus").next_to(rhombus, DOWN)
        self.play(Create(rhombus), Write(rhombus_text))
        self.wait(2)
        self.play(FadeOut(rhombus), FadeOut(rhombus_text))

        # Triangle
        triangle = Triangle(color=PURPLE)
        triangle_text = Text("Triangle").next_to(triangle, DOWN)
        self.play(Create(triangle), Write(triangle_text))
        self.wait(2)
        self.play(FadeOut(triangle), FadeOut(triangle_text))

        # Fade out title
        self.play(FadeOut(title))
        self.wait(1)



#Congruency
    def congruency(self):
        self.colorChoice = [WHITE,YELLOW,BLUE]
        self.isRandom= False
        p10=cvo.CVO().CreateCVO("congruency","").setPosition([-5,0,0])
        p11=cvo.CVO().CreateCVO("Equal sides", "").setPosition([1.5,2,0]).setangle(TAU/3)
        p12=cvo.CVO().CreateCVO("Equal angles", "").setPosition([1.5,-2,0]).setangle(TAU/4)
        p10.setcircleradius(1.5)
        p11.setcircleradius(1.5)
        p12.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
      
        self.construct1(p10,p10)
        self.wait(3.5)



#conguent
    def congruent(self):
        
        
        # Create the title\

    #("Hello,\\nWorld!"
     

        title = Text("               CONGRUENT   \n\n    Same Sides & Same Angles ", font_size=47)
        title.to_edge(UP)

        # Create the first square
        square1 = Square(side_length=2, fill_color=ORANGE, fill_opacity=10)
        square1.shift(2*LEFT)

        # Create the second square
        square2 = Square(side_length=2, fill_color=BLUE, fill_opacity=10)
        square2.shift(2*RIGHT)

        # Create the congruency marks
        mark1 = VGroup(*[Dot(square1.get_vertices()[i], color=YELLOW) for i in range(4)])
        mark2 = VGroup(*[Dot(square2.get_vertices()[i], color=YELLOW) for i in range(4)])

        # Create the congruency lines
        line1 = Line(square1.get_vertices()[0], square2.get_vertices()[0], color=YELLOW)
        line2 = Line(square1.get_vertices()[1], square2.get_vertices()[1], color=YELLOW)
        line3 = Line(square1.get_vertices()[2], square2.get_vertices()[2], color=YELLOW)
        line4 = Line(square1.get_vertices()[3], square2.get_vertices()[3], color=YELLOW)

        # Add the title, squares, congruency marks, and congruency lines to the scene
        self.add(title, square1, square2, mark1, mark2, line1, line2, line3, line4)

        # Wait for a few seconds
        self.wait(3)

        # Animate the transformation from one square to the other
        self.play(Transform(square1, square2), run_time=3)

        # Wait for a few seconds
        self.wait(4)


#rotation
    def rotation(self):
   
        # Create a grid
        grid = NumberPlane(
            x_range=(-7, 7),
            y_range=(-7, 7),
            axis_config={"color": WHITE},
        )
        self.add(grid)
     
    
        a = Text("Rotation ",color =ORANGE, font_size=48).to_edge(UP)
        self.play(Write(a))
        self.wait(1.9)


        # Create a square
        square = Square(side_length=2, color=YELLOW)

        # Create labels for vertices
        labels = VGroup(
            Text("A").scale(0.5).next_to(square.get_corner(UL), UL, buff=0.1),
            Text("B").scale(0.5).next_to(square.get_corner(UR), UR, buff=0.1),
            Text("C").scale(0.5).next_to(square.get_corner(DR), DR, buff=0.1),
            Text("D").scale(0.5).next_to(square.get_corner(DL), DL, buff=0.1)
        )

        # Group the square and labels together
        square_group = VGroup(square, labels)

        # Add the grid to the scene
        self.play(Create(grid))
        self.wait(1)

        # Add the square and labels to the scene
        self.play(Create(square), Write(labels))
        self.wait(2.2)

        # Rotate the square group
        self.play(Rotate(square_group, angle=PI, about_point=ORIGIN, rate_func=linear, run_time=4))
        self.wait(1)

        # Rotate back to original position
        self.play(Rotate(square_group, angle=-PI, about_point=ORIGIN, rate_func=linear, run_time=4))
        self.wait(3)
        




    def flipping(self):
  # Create a grid
        grid = NumberPlane(
            x_range=(0, 0),
            y_range=(-7, 7),
            axis_config={"color": WHITE},
        )
        self.add(grid)
        # Create title
        title = Text("Flipping of square", font_size=35)
        title.to_edge(UP)
        self.play(Write(title))

        # Create the initial square
        square = Square(side_length=2, color=BLUE)
        
        # Create vertex dots
        vertices = [Dot(point, color=YELLOW) for point in square.get_vertices()]
        
        # Create vertex labels
        labels = ['A', 'B', 'C', 'D']
        vertex_labels = VGroup(*[
            Text(label, font_size=24).next_to(vertex, direction=UP+LEFT, buff=0.1)
            for label, vertex in zip(labels, vertices)
        ])

        # Group square, vertices, and labels
        square_group = VGroup(square, *vertices, vertex_labels)
        square_group.move_to(LEFT * 3)

        # Add square group to the scene
        self.play(Create(square_group))
        self.wait(1)

        # Add "Before" label
        before_label = Text("Before", font_size=24).next_to(square_group, DOWN)
        self.play(Write(before_label))
        self.wait(1)

        # # Flip animation for initial square
        # self.play(Rotate(square_group, angle=PI, axis=RIGHT, run_time=2))
        # self.wait(1)

        # # Flip back
        # self.play(Rotate(square_group, angle=PI, axis=RIGHT, run_time=2))
        # self.wait(1)

        # Create arrow for transformation
        arrow = Arrow(square_group.get_right(), RIGHT * 2.5, buff=0.5)
        transform_label = Text("Flipping", font_size=30).next_to(arrow, UP, buff=0.1)
        self.play(Create(arrow), Write(transform_label))
        self.wait(1)
        self.play(Unwrite(before_label))

        # Transform the square
        transformed_square = square.copy().set_color(RED)
        transformed_vertices = [Dot(point, color=GREEN) for point in transformed_square.get_vertices()]
        transformed_labels = ['A', 'B', 'C', 'D']
        transformed_vertex_labels = VGroup(*[
            Text(label, font_size=24).next_to(vertex, direction=UP+LEFT, buff=0.1)
            for label, vertex in zip(transformed_labels, transformed_vertices)
        ])
        transformed_group = VGroup(transformed_square, *transformed_vertices, transformed_vertex_labels)
        transformed_group.move_to(RIGHT * 3)

        # Animate the transformation
        self.play(Transform(square_group, transformed_group))
      

        # Add "After" label
        after_label = Text("After", font_size=24).next_to(square_group, DOWN)
        self.play(Write(after_label))
      

        # Flip animation for transformed square
        self.play(Rotate(square_group, angle=PI, axis=RIGHT, run_time=2))
        self.wait(3.5)





#similarity  check

    def similaritycheck1(self):


    # Title
     title = Text("Checking Similarity", color=YELLOW).scale(1.2).to_edge(UP)
     self.play(Write(title))
     self.wait(2.3)

    # Create two squares
     square1 = Square(side_length=2, color=BLUE)
     square2 = Square(side_length=2.5, color=RED)

    # Position the squares
     square1.shift(LEFT * 2.5)
     square2.shift(RIGHT * 2.5)

    # Add labels
     label1 = Text("Square 1", font_size=27).next_to(square1, UP*2.1)
     label2 = Text("Square 2", font_size=27).next_to(square2, UP*2.33)

    # Create angle indicators (small squares)
     angle_indicators1 = self.create_angle_indicators1(square1, BLUE)
     angle_indicators2 = self.create_angle_indicators1(square2, RED)

    # Create side labels with lengths in cm
     side_labels1 = self.create_side_labels1(square1, "2 cm")
     side_labels2 = self.create_side_labels1(square2, "3 cm")

    # Create 90-degree labels
     degree_labels1 = self.create_degree_labels1(square1)
     degree_labels2 = self.create_degree_labels1(square2)

    # Animation
     self.play(Create(square1), Create(square2))
     self.play(Write(label1), Write(label2))
     self.wait(1)

     self.play(Create(VGroup(*angle_indicators1)), Create(VGroup(*angle_indicators2)))
     self.wait(1)
     self.play(Write(VGroup(*degree_labels1)), Write(VGroup(*degree_labels2)))
     self.wait(3)
     self.play(Write(VGroup(*side_labels1)), Write(VGroup(*side_labels2)))
     self.wait(3)



    # Show angle equality
     angle_text = Text("All angles = 90°", font_size=26).to_edge(DOWN*2.5)
     self.play(Write(angle_text))
     self.wait(2.2)

    # Show similarity conclusion
     similarity_text = Text("Squares are similar!", font_size=30).next_to(angle_text, DOWN)
     self.play(Write(similarity_text))
     self.wait(3)

    def create_angle_indicators1(self, square, color):
     indicators = []
     for i in range(4):
        indicator = Square(side_length=0.2, color=color)
        indicator.move_to(square.get_vertices()[i])
        indicator.shift((square.get_center() - square.get_vertices()[i]) * 0.09)
        indicators.append(indicator)
     return indicators

    def create_side_labels1(self, square, label):
     labels = []
     for i in range(4):
        mid_point = (square.get_vertices()[i] + square.get_vertices()[(i+1) % 4]) / 2
        direction = mid_point - square.get_center()
        side_label = Text(label).scale(0.4).move_to(mid_point + direction * 0.4)
        labels.append(side_label)
     return labels

    def create_degree_labels1(self, square):
     labels1 = []
     for i in range(4):
        vertex = square.get_vertices()[i]
        direction = vertex - square.get_center()
        degree_label = Text("90°", font_size=20).move_to(vertex + direction * -0.32)
        labels1.append(degree_label)
     return labels1



    
    def similaritycheck2(self):
        # Title
        title = Text("Checking Similarity", color=YELLOW).scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2.3)

        # Create two triangles
        triangle1 = Triangle(color=BLUE).scale(1.5)
        triangle2 = Triangle(color=RED).scale(2)

        # Position the triangles
        triangle1.shift(LEFT * 3)
        triangle2.shift(RIGHT * 3)

        # Add labels
        label1 = Text("Triangle 1", font_size=27).next_to(triangle1, UP*2.1)
        label2 = Text("Triangle 2", font_size=27).next_to(triangle2, UP*2.33)

        # Create angle indicators (small triangles)
        angle_indicators1 = self.create_angle_indicators(triangle1, BLUE)
        angle_indicators2 = self.create_angle_indicators(triangle2, RED)

        # Create side labels with lengths
        side_labels1 = self.create_side_labels(triangle1, ["3 cm", " 3 cm", "3 cm"])
        side_labels2 = self.create_side_labels(triangle2, ["5 cm", "5 cm", "5 cm"])

        # Create degree labels
        degree_labels1 = self.create_degree_labels(triangle1, ["60°", "60°", "60°"])
        degree_labels2 = self.create_degree_labels(triangle2, ["60°", "60°", "60°"])

        # Animation
        self.play(Create(triangle1), Create(triangle2))
        self.play(Write(label1), Write(label2))
        self.wait(1)

        self.play(Create(VGroup(*angle_indicators1)), Create(VGroup(*angle_indicators2)))
        self.wait(1)
        self.play(Write(VGroup(*degree_labels1)), Write(VGroup(*degree_labels2)))
        self.wait(3)
        self.play(Write(VGroup(*side_labels1)), Write(VGroup(*side_labels2)))
        self.wait(3)

        # Show angle equality
        angle_text = Text("All angles = 60°", font_size=27).to_edge(DOWN*2.5)
        self.play(Write(angle_text))
        self.wait(2.2)

        # Show similarity conclusion
        similarity_text = Text("Triangles are similar!", font_size=30).next_to(angle_text, DOWN)
        self.play(Write(similarity_text))
        self.wait(3)

    def create_angle_indicators(self, triangle, color):
        indicators = []
        for i in range(3):
            indicator = Triangle(color=color).scale(0.1)
            indicator.move_to(triangle.get_vertices()[i])
            indicator.shift((triangle.get_center() - triangle.get_vertices()[i]) * 0.05)
            indicators.append(indicator)
        return indicators

    def create_side_labels(self, triangle, labels):
        side_labels = []
        for i in range(3):
            mid_point = (triangle.get_vertices()[i] + triangle.get_vertices()[(i+1) % 3]) / 2
            direction = mid_point - triangle.get_center()
            side_label = Text(labels[i], font_size=20).move_to(mid_point + direction * 0.5)
            side_labels.append(side_label)
        return side_labels

    def create_degree_labels(self, triangle, angles):
        labels = []
        for i in range(3):
            vertex = triangle.get_vertices()[i]
            direction = vertex - triangle.get_center()
            degree_label = Text(angles[i], font_size=20).move_to(vertex + direction * -0.3)
            labels.append(degree_label)
        return labels

        
#linesymmetry
 #rotationalsymmetry
    # render using CVO data object
    def constructDataByCVO(self):
        self.colorChoice = [WHITE,YELLOW,BLUE]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Dilation","").setPosition([-5,0,0])
        p11=cvo.CVO().CreateCVO("Definition", "Dilation is a transformation that changes the size\n\n of a figure without changing its shape.").setPosition([1.5,2,0]).setangle(TAU/3)
        p12=cvo.CVO().CreateCVO("scale factor", "proportion that changes the size of a shape after transformation").setPosition([1.5,-2,0]).setangle(TAU/4)
        p11.setcircleradius(1.75)
        p12.setcircleradius(1.75)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
      
 
        
        self.construct1(p10,p10)
        self.wait(7)

        

   
    def constdilation(self):
        a = Text("Dialtion Construction ",font_size=37,color=PINK).to_edge(UP)
        self.play(Write(a))
        self.wait(1.8)
   

        # Create the original triangle
        triangle = Polygon([-3, -2, 0], [1, -2, 0], [-1, 1, 0], color=BLUE)
        
        # Create the center of dilation
        center = Dot([4, -1, 0], color=RED)
        center_label = Text("C", font_size=28,color = ORANGE).next_to(center, DOWN)
        
        # Create labels for the original triangle
        labels = VGroup(
            Text("P", font_size=24,color = BLUE).next_to(triangle.get_vertices()[0], DOWN+LEFT),
            Text("Q", font_size=24,color = BLUE).next_to(triangle.get_vertices()[1], DOWN+RIGHT),
            Text("R", font_size=24,color = BLUE).next_to(triangle.get_vertices()[2], UP),
        )
        lab = VGroup(
            Dot(color = BLUE).move_to(triangle.get_vertices()[0]),
            Dot(color = BLUE).move_to(triangle.get_vertices()[1]),
            Dot(color = BLUE).move_to(triangle.get_vertices()[2]),

        )

        # Create a text box for step descriptions
        description = Text("", font_size=24).to_edge(UP)

        # Step 1: Draw the original triangle and center
        self.play(

         
            Write(description.become(Text("Step 1: Draw a  triangle PQR and choose the center of dilation C \nwhich is not on the triangle. ", font_size=29,color = YELLOW).to_edge(DOWN))),
                   
        )
        self.wait(5)
        self.play( Create(triangle), Create(center),Create(lab), Write(center_label), Write(labels))
        self.wait(3)

        # Step 2: Draw lines from center to vertices
        lines = VGroup(*[DashedLine(center.get_center(), vertex) for vertex in triangle.get_vertices()])
        self.play(
            
            description.animate.become(Text("Step 2: Draw lines from C to P, Q, and R", font_size=29,color = YELLOW).to_edge(DOWN))
        )
        self.wait(3)
        self.play(Create(lines))
        self.wait(2)

        # Step 3: Extend the lines
        extended_lines = VGroup(*[
            DashedLine(center.get_center(), vertex + 1.5*(vertex - center.get_center()))
            for vertex in triangle.get_vertices()
        ])
        self.play(
            
            description.animate.become(Text("Step 3: Extend the lines from C", font_size=29,color = YELLOW).to_edge(DOWN))
        )
        self.wait(2.1)
        self.play(Transform(lines, extended_lines))
        self.wait(3)

        # Step 4: Create the dilated triangle
        scale_factor = 1.5
        dilated_triangle = Polygon(
            *[center.get_center() + scale_factor * (vertex - center.get_center())
              for vertex in triangle.get_vertices()],
            color=GREEN
        )
        
        # Create labels for the dilated triangle
        dilated_labels = VGroup(
            Text("P'", font_size=24,color=GREEN).next_to(dilated_triangle.get_vertices()[0], UP+LEFT),
            Text("Q'", font_size=24,color=GREEN).next_to(dilated_triangle.get_vertices()[1], UP+RIGHT),
            Text("R'", font_size=24,color=GREEN).next_to(dilated_triangle.get_vertices()[2], UP),
        )

        dot = VGroup(
            Dot(color=GREEN).move_to(dilated_triangle.get_vertices()[0]),
            Dot(color=GREEN).move_to(dilated_triangle.get_vertices()[1]),
            Dot(color=GREEN).move_to(dilated_triangle.get_vertices()[2]),
            
        )

        

        self.play(
            
            description.animate.become(Text("Step 4: By using compasses, Mark\n\n three points P' , Q' and R' \n\non the projections'", font_size=26,color = YELLOW).to_edge(DOWN*9+RIGHT))
        )
        self.wait(4)
        self.play(Create(dot))
        self.wait(2)
        
        self.play(Write(dilated_labels))
        self.wait(3)
        b = Text("K = Scale factor",font_size=29,color=PINK).to_edge(RIGHT+DOWN*4)
        self.play(Write(b))
        self.wait(2)

        a = description.animate.become(Text("CP'= k (CP) ",font_size=30,color=YELLOW).to_edge(DOWN+RIGHT*3.5))
        self.play(a)
        self.wait(4)

        # Final step: Show the complete construction
        self.play(
            description.animate.become(Text("Step 5: Join P'Q', Q'R' and R'P'. So that  P'Q' R' ~  PQR", font_size=29,color = YELLOW).to_edge(DOWN))
        )
        self.wait(3)
        self.play(Create(dilated_triangle))
        self.wait(4)



#symmetry
    def symmetry(self):
        # Create the grid
    

        # Create titles
        title = Text(" Symmetry", font_size=46).shift(UP * 3.5)
    

        # Create a group
        group = VGroup( title)
    

        self.add(group)
        self.wait(2)
         # Create a square
        square = Text("B",font_size=240,color=BLUE)

        # Create axes
        axes = DashedLine(ORIGIN).set_length(7).shift(UP*0)
           
        

        # Rotate the square to demonstrate rotational symmetry
        # self.play(Rotate(square, angle=PI/2, about_point=ORIGIN), run_time=2)
        # self.play(Rotate(square, angle=PI/2, about_point=ORIGIN), run_time=2)
        # self.play(Rotate(square, angle=PI/2, about_point=ORIGIN), run_time=2)
        # self.play(Rotate(square, angle=PI/2, about_point=ORIGIN), run_time=2)

        # Pause to show the square back in its original position
        
        squar = Text("Symmetry is a property where an object remains unchanged after a specific \n\ntransformation is applied to it.",font_size=30,color=YELLOW)
        self.play(Write(squar))
        self.wait(6)
        self.play(squar.animate.to_edge(DOWN*2.5 ))
        self.wait(1.4)
        
        self.play(Create(axes), Create(square))
        self.wait(3)

    
       
    def linesymmetry(self):
        # Title
 
        # Title
        a = Text("Line Symmetry", font_size=37.8, color=YELLOW).to_edge(UP)
        self.play(Write(a))
        self.wait(2)

        # Create a square
        square = Square(side_length=4, color=BLUE)

        # Add vertex labels
        vertices = square.get_vertices()
        vertex_labels = VGroup(*[
            Text(label, font_size=24).next_to(vertex, direction)
            for label, vertex, direction in zip(
                ['B', 'A', 'C', 'D'],
                vertices,
                [UL, UR, DR, DL]
            )
        ])

        # Create symmetry lines
        diag1 = DashedLine(square.get_corner(UL), square.get_corner(DR), color=RED)
        diag2 = DashedLine(square.get_corner(UR), square.get_corner(DL), color=RED)
        vert = DashedLine(square.get_top(), square.get_bottom(), color=GREEN)
        horiz = DashedLine(square.get_left(), square.get_right(), color=GREEN)

        # Create labels
        diag_label = Text("", font_size=24, color=RED).next_to(square, UP, buff=0.5)
        axis_label = Text("", font_size=24, color=GREEN).next_to(diag_label, DOWN)

        # Add square and vertex labels to the scene
        self.play(Create(square), Write(vertex_labels))
        self.wait(1)

        # Show diagonal symmetry lines
        self.play(Create(diag1), Create(diag2), Write(diag_label))
        self.wait(2.3)

     


        # Show axis symmetry lines
        self.play(Create(vert), Create(horiz), Write(axis_label))
        self.wait(2.6)

        

        # Final message
        final_text = Text("A square has four lines of symmetry.Because it consists of\n 2 diagonals , 1 x-axis and 1 y-axis.", font_size=32).next_to(square, DOWN, buff=0.5)
        self.play(Write(final_text))
        self.wait(6.5)


    def rotationalsymmetry(self):
         
        a = Text("Rotational Symmetry", font_size=40, color=YELLOW).to_edge(UP)
        self.play(Write(a))
        self.wait(2)


        specific_condition = Text("Rotational symmetry is a geometric property where an object looks the\n\n same after being rotated by a certain angle around a fixed point.", font_size=30,color=BLUE).to_edge(DOWN*7.5)
        self.play( Write(specific_condition))
        self.wait(6.7)
        self.play(
        
        FadeOut(specific_condition),
        FadeOut(a)
        )
    
        self.wait(1)

        shapes = [
        (Circle(radius=2, color=BLUE), "Circle", "Infinite"),
        (Square(side_length=4, color=GREEN), "Square", 4),
        (Triangle(color=RED).scale(2), "Triangle", 3),
        (Rectangle(width=4, height=2, color=YELLOW), "Rectangle", 2)
         ]

        for shape, name, symmetries in shapes:
           self.show_symmetry(shape, name, symmetries)
           self.wait(2)
           self.clear()
    def show_symmetry(self, shape, shape_name, symmetries):
        
       # Create the shape
     shape.move_to(ORIGIN)

    # Create a dot at the center
     center_dot = Dot(color=WHITE)

    # Create an arrow to show rotation
     arrow = Arrow(start=ORIGIN, end=shape.get_top(), color=ORANGE)

    # Group the shape and arrow
     group = VGroup(shape, arrow)

# Create and display the shape name
     name_text = Text(shape_name, font_size=36).to_edge(UP)
     self.play(Write(name_text))
     self.wait(2)
    # Add elements to the scene
     self.play(Create(group), Create(center_dot))
     self.wait(2)

    # # Create and display the shape name
    #  name_text = Text(shape_name, font_size=36).to_edge(UP)
    #  self.play(Write(name_text))


    # Rotate the shape
     if symmetries == "Infinite":
        self.play(Rotate(group, angle=2*PI, about_point=ORIGIN), run_time=5)
        check_text = Text(" A circle has infinite rotational symmetry around at any angle.", color=GREEN, font_size=28).to_edge(DOWN*1.6)
        self.play(Write(check_text))
        self.wait(2)
     else:
        for i in range(symmetries):
            self.play(
                Rotate(group, angle=2*PI/symmetries, about_point=ORIGIN),
                run_time=2
            )
            angle = 360 / symmetries * (i + 1)
            check_text = Text(f" It is similar at {angle}° with compare to original position.", color=WHITE, font_size=30).to_edge(DOWN*1.6)
            self.play(Write(check_text))
            self.wait(2)
            if i < symmetries - 1:
                self.play(FadeOut(check_text))

     self.wait(2)

    # Final message
     if symmetries == "Infinite":
        final_text = Text("Order of Rotation is Infinite. ", font_size=36).to_edge(DOWN)
     else:
        self.wait(1.5)
        final_text = Text(f"Order of Rotation is {symmetries}. ", font_size=36).to_edge(DOWN)
    
     self.play(
      
        FadeOut(check_text),
        Write(final_text)
    )
     self.wait(3)





#    
   
    def pointsymmetry(self):
        # Title
        title = Text("Point Symmetry").scale(0.9).to_edge(UP)
        self.play(Write(title))
        self.wait(2)

        a = Text("Point symmetry occurs when every part has a matching part exactly \nopposite the center point.",font_size=30,color=PINK)
        self.play(Write(a))
        self.wait(5)
        self.play(a.animate.to_edge(DOWN ))
        self.wait(1.5)
        # Create star
        star = Star(n=5, outer_radius=2, inner_radius=1, color=YELLOW)
        star_label = Text("Star").next_to(star, DOWN)
        self.wait(1.2)

        # Create hourglass
        hourglass = self.create_hourglass()
        hourglass_label = Text("Hourglass").next_to(hourglass, DOWN)
        self.wait(1)

        # Position shapes
        star.shift(LEFT * 3)
        star_label.shift(LEFT * 3)
        hourglass.shift(RIGHT * 3)
        hourglass_label.shift(RIGHT * 3)

        # Show shapes
        self.play(Create(star), Create(hourglass))
        self.wait(1.5)
        self.play(Write(star_label), Write(hourglass_label))
        self.wait(1.4)


        # Show center points
        star_center = Dot(star.get_center(), color=RED)
        hourglass_center = Dot(hourglass.get_center(), color=RED)
        self.play(Create(star_center), Create(hourglass_center))


        # Wait before finishing
        self.wait(4)
        

    def create_hourglass(self):
        # Create an hourglass shape using two triangles
        triangle1 = Triangle(color=BLUE).scale(1).shift(DOWN)
        triangle2 = Triangle(color=BLUE).scale(1).rotate(PI).next_to(triangle1,UP*0.2)
        hourglass = VGroup(triangle1, triangle2)
        return hourglass






        
    def SetDeveloperList(self):
        self.DeveloperList = "Uday Kiran"   

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade8chapter8ExploringGeometricalFigures.py"      
        
     
      
if __name__ == "__main__":
    scene = Grade8chapter8ExploringGeometricalFigures()
    scene.render()