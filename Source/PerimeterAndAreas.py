# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla
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

# Configure Manim to allow more cached files
config.max_files_cached = 800  # Change this number to your desired value


class PerimeterAndAreas(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.introduction()
        self.fadeOutCurrentScene()
        self.shapes()
        self.fadeOutCurrentScene()
        self.perimeter()
        self.fadeOutCurrentScene()
        self.perimeteroftriangle()
        self.fadeOutCurrentScene()
        self.perimeterofsquare()
        self.fadeOutCurrentScene()
        self.perimeterofrectangle()
        self.fadeOutCurrentScene()
        self.perimeterofpentagon()
        self.fadeOutCurrentScene()
        self.perimeterofhexagon()
        self.fadeOutCurrentScene()
        self.perimeterofoctagon()
        self.fadeOutCurrentScene()
        self.areas()
        self.fadeOutCurrentScene()
        self.areaoftriangle()
        self.fadeOutCurrentScene()
        self.areaofsquare()
        self.fadeOutCurrentScene()
        self.areaofrectangle()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
    
    def RenderSkillbancLogo(self):
        
        self.orange = "#D76800"
        self.blue = "#3F64A7"
        self.green = "#96D24D"
        self.circles = VGroup(
            Circle(radius=1).rotate(PI/2).set_fill(self.orange, opacity=1).set_stroke(self.orange, opacity=1).shift(LEFT*3),
            Circle(radius=1).rotate(PI/2).set_fill(self.blue, opacity=1).set_stroke(self.blue, opacity=1),
            Circle(radius=1).rotate(PI/2).set_fill(self.green, opacity=1).set_stroke(self.green, opacity=1).shift(RIGHT*3)
        )
        circle1, circle2, circle3 = self.circles
        
        lines = VGroup(
            Arrow(circle1.get_right(), circle2.get_left(), max_tip_length_to_length_ratio=2),
            Arrow(circle2.get_right(), circle3.get_left(), max_tip_length_to_length_ratio=2),
            CurvedArrow(circle1.get_top(), circle3.get_top(), angle=-TAU/4),
            CurvedArrow(circle1.get_bottom(), circle3.get_bottom(), angle=TAU/4)
        )

        # Adjust the starting points of the straight arrows to touch the circumference
        lines[0].put_start_and_end_on(circle1.get_right(), circle2.get_left())
        lines[1].put_start_and_end_on(circle2.get_right(), circle3.get_left())

        # Add the text "skillbanc" below the curved arrows
        self.play(Create(circle1), Create(circle2), Create(circle3), rate_func=smooth, run_time=1)
        self.play(Create(lines), rate_func=smooth, run_time=1)
        text = Text("Skillbanc.com, Inc.").next_to(lines[3], DOWN)
        self.play(Create(text), rate_func=smooth, run_time=0.75)
        
        self.logoGroup = VGroup().add(self.circles).add(lines).add(text)
        self.play(self.logoGroup.animate.scale(0),run_time=1)
        # self.play(self.circles.animate.scale(0),lines.animate.scale(0),text.animate.scale(0),run_time=3)
    
        
    def introduction(self):
        
        self.setNumberOfCirclePositions(3)
        self.isRandom = False
        p10 = cvo.CVO().CreateCVO("perimeter and Area", "")
        p12 = cvo.CVO().CreateCVO("perimeter", "Perimeter is the distance around the outside of a shape.")
        p13 = cvo.CVO().CreateCVO("area", "Area is the amount of space inside a shape.")

        p10.cvolist.append(p12)
        p10.cvolist.append(p13)

        self.construct1(p10, p10)

    def shapes(self):
        self.setNumberOfCirclePositions(2)
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("parimeter and area","")
        p11=cvo.CVO().CreateCVO("shapes","").setPosition([2,0,0])
        p11onnamelist=["triangle","square","rectangle","pentagon","hexagon","octagon"]
        p11.extendOname(p11onnamelist)
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        # self.SetNumberOfClasses(2)
        self.angleChoice = [TAU/4]
        self.colorChoice=[ORANGE,YELLOW]
    
        self.construct1(p10,p10)
        
    def perimeter(self): 
        heading = Text("Perimeter of different shapes")
        heading.to_edge(UP) 
        
        self.play(Write(heading)) 
 
    def perimeteroftriangle(self):
         # Create a heading
        heading = Text("Perimeter of a Triangle")
        heading.to_edge(UP)

        # Create a triangle
        triangle = Polygon(
            ORIGIN, 3 * RIGHT, 3 * RIGHT + 3 * UP,
            stroke_color=BLUE,
            stroke_width=2,
            fill_color=BLUE,
            fill_opacity=0.3
        )
        triangle.move_to(LEFT * 3)  # Move the triangle to the left side

        # Get vertices of the triangle
        v0, v1, v2 = triangle.get_vertices()

        # Create two-sided arrows with length labels below each side
        arrow_1 = DoubleArrow(start=v0 + DOWN * 0.5, end=v1 + DOWN * 0.5, buff=0.1)
        length_label_1 = MathTex("a").next_to(arrow_1, DOWN)
        
        arrow_2 = DoubleArrow(start=v1 + RIGHT * 0.5, end=v2 + RIGHT * 0.5, buff=0.1)
        length_label_2 = MathTex("b").next_to(arrow_2, RIGHT)

        arrow_3 = DoubleArrow(start=v2 + UP * 0.5, end=v0 + UP * 0.5, buff=0.1)
        length_label_3 = MathTex("c").next_to(arrow_3, UP)

        # Calculate perimeter and create the formula
        perimeter_formula = MathTex("P = a + b + c")
        perimeter_formula.to_corner(DR)

        # Add heading, triangle, arrows, and labels to the scene
        self.play(Write(heading))
        self.play(Create(triangle))
        self.play(Create(arrow_1), Write(length_label_1))
        self.play(Create(arrow_2), Write(length_label_2))
        self.play(Create(arrow_3), Write(length_label_3))
        self.play(Write(perimeter_formula))

        # Hold the final frame for a few seconds
        self.wait(2)
        
        p10=cvo.CVO().CreateCVO("formula","a + b + c").setPosition([2,1,0])
        p11=cvo.CVO().CreateCVO("example","a=4,b=3,c=5").setPosition([4,1,0])
        p12=cvo.CVO().CreateCVO("perimeter","4+3+5 = 12").setPosition([3,-2,0]).setangle(-TAU/4)
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
         
        self.construct1(p10,p10)
 
    def perimeterofsquare(self):
            
        # Create a heading
        heading = Text("Perimeter of a Square")
        heading.to_edge(UP)

        # Create a square
        square = Square(side_length=2)
        square.move_to(LEFT * 3)
        square.set_color(BLUE)

        # Add side labels
        side_label_1 = MathTex("a")
        side_label_2 = side_label_1.copy()
        side_label_3 = side_label_1.copy()
        side_label_4 = side_label_1.copy()

        # Position side labels
        side_label_1.next_to(square.get_top(), UP)
        side_label_2.next_to(square.get_bottom(), DOWN)
        side_label_3.next_to(square.get_left(), LEFT)
        side_label_4.next_to(square.get_right(), RIGHT)

        # Create the perimeter formula
        perimeter_formula = MathTex("P = 4a")
        perimeter_formula.to_corner(DR)

        # Add heading, square, and labels to the scene
        self.play(Write(heading))
        self.play(Create(square))
        self.play(Write(side_label_1), Write(side_label_2), Write(side_label_3), Write(side_label_4))
        self.play(Write(perimeter_formula))

        # Hold the final frame for a few seconds
        self.wait(2)
        
        p10=cvo.CVO().CreateCVO("formula","4*length of a side(a)").setPosition([2,1,0])
        p11=cvo.CVO().CreateCVO("example","a=4").setPosition([4,1,0])
        p12=cvo.CVO().CreateCVO("perimeter","4*4 = 16").setPosition([3,-2,0]).setangle(-TAU/4)
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        
         
        self.construct1(p10,p10)
         
    def perimeterofrectangle(self):
        # Create a heading
        heading = Text("Perimeter of a Rectangle")
        heading.to_edge(UP)

        # Create a rectangle
        rectangle = Rectangle(width=3, height=2)
        rectangle.move_to(LEFT * 3)
        rectangle.set_color(BLUE)

        # Get vertices of the rectangle
        v0, v1, v2, v3 = rectangle.get_vertices()

        # Create arrows for width (l) and height (b)
        arrow_width = DoubleArrow(start=v0 + DOWN * 1.5, end=v1 + DOWN * 1.5, buff=0.1)
        width_label = MathTex("l").next_to(arrow_width, DOWN)
        
        arrow_height = DoubleArrow(start=v1 + RIGHT * 1.5, end=v2 + RIGHT * 1.5, buff=0.1)
        height_label = MathTex("b").next_to(arrow_height, RIGHT)

        # Calculate perimeter and create the formula
        perimeter_formula = MathTex("P = 2l + 2b")
        perimeter_formula.to_corner(DR)

        # Add heading, rectangle, arrows, and labels to the scene
        self.play(Write(heading))
        self.play(Create(rectangle))
        self.play(Create(arrow_width), Write(width_label))
        self.play(Create(arrow_height), Write(height_label))
        self.play(Write(perimeter_formula))

        # Hold the final frame for a few seconds
        self.wait(2)

        p10=cvo.CVO().CreateCVO("formula","2(l+b)").setPosition([2,1,0])
        p11=cvo.CVO().CreateCVO("example","l=2,b=3,c=5").setPosition([4,1,0])
        p12=cvo.CVO().CreateCVO("perimeter","2(2+3) = 10").setPosition([3,-2,0]).setangle(-TAU/4)
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
         
        self.construct1(p10,p10)    

    def perimeterofpentagon(self):
        # Create a heading
        heading = Text("Perimeter of a Regular Polygon(Pentagon)")
        heading.to_edge(UP)

        # Define side length of the pentagon
        side_length = 2

        # Create a pentagon
        pentagon = RegularPolygon(n=5, start_angle=0, color=BLUE)
        pentagon.set_width(side_length)
        pentagon.move_to(LEFT * 3)

        # Get vertices of the pentagon
        vertices = pentagon.get_vertices()

        # Calculate center point and perpendicular vector for the bottom side (index 2 in this case)
        side_index = 2
        side_vector = vertices[(side_index + 1) % 5] - vertices[side_index]
        center_point = (vertices[side_index] + vertices[(side_index + 1) % 5]) / 2

        # Calculate perpendicular vector (pointing downwards)
        perpendicular_vector = np.array([-side_vector[1], side_vector[0], 0])  # Perpendicular vector
        perpendicular_vector /= np.linalg.norm(perpendicular_vector)  # Normalize

        # Adjust positions for arrow and label
        arrow_start = vertices[side_index] + perpendicular_vector * 0.1
        arrow_end = vertices[(side_index + 1) % 5] + perpendicular_vector * 0.1
        arrow = DoubleArrow(start=arrow_start, end=arrow_end, buff=0.2, stroke_width=8)
        label = MathTex("a").next_to(arrow, perpendicular_vector, buff=0.2)

        # Calculate perimeter formula
        perimeter_formula = MathTex("P = 5 \\times a")
        perimeter_formula.to_corner(DR)

        # Add heading, pentagon, arrow, label, and formula to the scene
        self.play(Write(heading))
        self.play(Create(pentagon))
        self.play(Create(arrow), Write(label))
        self.play(Write(perimeter_formula))

        # Hold the final frame for a few seconds
        self.wait(2)
        
        p10=cvo.CVO().CreateCVO("pentagon","5-sided polygon(all sides are equal)").setPosition([2,1,0])
        p11=cvo.CVO().CreateCVO("formula","5 x length of any side(a)").setPosition([5,1,0])
        p12=cvo.CVO().CreateCVO("example","a=3").setPosition([2,-2,0]).setangle(-TAU/4)
        p13=cvo.CVO().CreateCVO("perimeter","5*3 = 15").setPosition([5,-2,0]).setangle(-TAU/4)
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
         
        self.construct1(p10,p10)  
    
    def perimeterofhexagon(self):
         # Create a heading
        heading = Text("Perimeter of Regular Polygon(Hexagon)")
        heading.to_edge(UP)

        # Define side length of the hexagon
        side_length = 2

        # Create a hexagon
        hexagon = RegularPolygon(n=6, start_angle=0, color=BLUE)
        hexagon.set_width(side_length)
        hexagon.move_to(LEFT * 3)

        # Get vertices of the hexagon
        vertices = hexagon.get_vertices()

        # Calculate center point and perpendicular vector for the bottom side (index 2 in this case)
        side_index = 2
        side_vector = vertices[(side_index + 1) % 6] - vertices[side_index]
        center_point = (vertices[side_index] + vertices[(side_index + 1) % 6]) / 2

        # Calculate perpendicular vector (pointing outwards from the hexagon)
        perpendicular_vector = np.array([-side_vector[1], side_vector[0], 0])  # Perpendicular vector
        perpendicular_vector /= np.linalg.norm(perpendicular_vector)  # Normalize

        # Adjust positions for arrow and label outside the hexagon
        arrow_start = vertices[side_index] + perpendicular_vector * 0.1
        arrow_end = vertices[(side_index + 1) % 6] + perpendicular_vector * 0.5  # Increase length for larger arrow
        arrow = DoubleArrow(start=arrow_start, end=arrow_end, buff=0.2, stroke_width=8)
        label = MathTex("a").next_to(arrow, perpendicular_vector, buff=0.2)

        # Calculate perimeter formula
        perimeter_formula = MathTex("P = 6 \\times a")
        perimeter_formula.to_corner(DR)

        # Add heading, hexagon, arrow, label, and formula to the scene
        self.play(Write(heading))
        self.play(Create(hexagon))
        self.play(Create(arrow), Write(label))
        self.play(Write(perimeter_formula))

        # Hold the final frame for a few seconds
        self.wait(2)
        
        p10=cvo.CVO().CreateCVO("pentagon","6-sided polygon(all sides are equal)").setPosition([2,1,0])
        p11=cvo.CVO().CreateCVO("formula","6 x length of any side(a)").setPosition([5,1,0])
        p12=cvo.CVO().CreateCVO("example","a=3").setPosition([2,-2,0]).setangle(-TAU/4)
        p13=cvo.CVO().CreateCVO("perimeter","6*3 = 18").setPosition([5,-2,0]).setangle(-TAU/4)
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
         
        self.construct1(p10,p10)
          
    def perimeterofoctagon(self):
        # Create a heading
        heading = Text("Perimeter of regular polygon(Octagon)")
        heading.to_edge(UP)

        # Define side length of the octagon
        side_length = 2

        # Create an octagon
        octagon = RegularPolygon(n=8, start_angle=0, color=BLUE)
        octagon.set_width(side_length)
        octagon.move_to(LEFT * 3)

        # Get vertices of the octagon
        vertices = octagon.get_vertices()

        # Calculate center point and perpendicular vector for the bottom side (index 3 in this case)
        side_index = 3
        side_vector = vertices[(side_index + 1) % 8] - vertices[side_index]
        center_point = (vertices[side_index] + vertices[(side_index + 1) % 8]) / 2

        # Calculate perpendicular vector (pointing upwards)
        perpendicular_vector = np.array([side_vector[1], -side_vector[0], 0])  # Perpendicular vector
        perpendicular_vector /= np.linalg.norm(perpendicular_vector)  # Normalize

        # Adjust positions for two-sided arrow and label beside the octagon
        arrow_start = vertices[side_index] + perpendicular_vector * 0.2
        arrow_end = vertices[(side_index + 1) % 8] + perpendicular_vector * 0.2
        arrow = DoubleArrow(start=arrow_start, end=arrow_end, buff=0.1, stroke_width=6)
        label = MathTex("a").next_to(arrow, perpendicular_vector, buff=0.1)

        # Calculate perimeter formula
        perimeter_formula = MathTex("P = 8 \\times a")
        perimeter_formula.to_corner(DR)

        # Add heading, octagon, arrow, label, and formula to the scene
        self.play(Write(heading))
        self.play(Create(octagon))
        self.play(Create(arrow), Write(label))
        self.play(Write(perimeter_formula))

        # Hold the final frame for a few seconds
        self.wait(2)
        
        p10=cvo.CVO().CreateCVO("octagon","8-sided polygon(all sides are equal)").setPosition([2,1,0])
        p11=cvo.CVO().CreateCVO("formula","8 x length of any side(a)").setPosition([5,1,0])
        p12=cvo.CVO().CreateCVO("example","a=2").setPosition([2,-2,0]).setangle(-TAU/4)
        p13=cvo.CVO().CreateCVO("area","8*3 = 16").setPosition([5,-2,0]).setangle(-TAU/4)
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
         
        self.construct1(p10,p10)
    
    def areas(self):
        heading = Text("area of different shapes")
        heading.to_edge(UP) 
        
        self.play(Write(heading)) 
    
    def areaoftriangle(self):
        
        # Create a heading
        heading = Text("Area of triangle")
        heading.to_edge(UP)
         # Add heading at the end
        self.play(Write(heading))
        self.wait(2)
       
        # Define the vertices of the triangle
        A = np.array([-4, -2, 0])
        B = np.array([-1, -2, 0])
        C = np.array([-2, 2, 0])

        # Create the triangle
        triangle = Polygon(A, B, C, fill_color=BLUE, fill_opacity=0.5)

        # Create the labels for the vertices
        label_A = MathTex("A").next_to(A, LEFT)
        label_B = MathTex("B").next_to(B, DOWN)
        label_C = MathTex("C").next_to(C, RIGHT)

        # Create the double-sided arrows for the base (from A to B)
        arrow_base = DoubleArrow(A, B, buff=0.1, stroke_width=5)
        label_base = MathTex("base").next_to(arrow_base, DOWN, buff=0.1)

        # Create the double-sided arrows for the height (from C to the perpendicular point on AB)
        height_point_on_AB = np.array([C[0], A[1], 0])  # Point on AB directly above C
        arrow_height = DoubleArrow(C, height_point_on_AB, buff=0.1, stroke_width=5)
        label_height = MathTex("height").next_to(arrow_height, RIGHT, buff=0.1)

        # Add all objects to the scene
        self.add(triangle, label_A, label_B, label_C)

        # Animate the triangle creation
        self.play(Create(triangle))
        self.wait(0.5)

        # Add labels and arrows
        self.play(Write(label_A), Write(label_B), Write(label_C))
        self.wait(0.5)
        self.play(GrowArrow(arrow_base), Write(label_base))
        self.play(GrowArrow(arrow_height), Write(label_height))
        self.wait(1)
       
        p10=cvo.CVO().CreateCVO("formula","1/2(b*h)").setPosition([2,1,0])
        p11=cvo.CVO().CreateCVO("example","b=2,h=3").setPosition([4,1,0])
        p12=cvo.CVO().CreateCVO("area","1/2(2*3) = 3").setPosition([3,-2,0]).setangle(-TAU/4)
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
         
        self.construct1(p10,p10) 
        
    def areaofsquare(self):
         # Create heading for square area
        heading = Text("Area of a Square").to_edge(UP)

        # Define side length of the square
        side_length = 3

        # Create square
        square = Square(side_length=side_length, color=BLUE, fill_opacity=0.3)
        square.move_to(LEFT * 3)  # Move the square to the left side

        # Create two-sided arrow with label for side length of square
        arrow_start = square.get_bottom() + LEFT * 0.5
        arrow_end = square.get_top() + LEFT * 0.5
        arrow_square = DoubleArrow(arrow_start, arrow_end, buff=0.1)
        length_label_square = MathTex("s").next_to(arrow_square, LEFT)

        # Add all elements to the scene
        self.play(Write(heading))
        self.play(Create(square))
        self.play(Create(arrow_square), Write(length_label_square))

        self.wait(2)

        self.wait(1)
        p10=cvo.CVO().CreateCVO("formula","side x side").setPosition([2,1,0])
        p11=cvo.CVO().CreateCVO("example","s=3").setPosition([4,1,0])
        p12=cvo.CVO().CreateCVO("area","3*3 = 9").setPosition([3,-2,0]).setangle(-TAU/4)
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
         
        self.construct1(p10,p10) 
        
    def areaofrectangle(self):
         # Define dimensions
        width = 4
        height = 3

        # Create the rectangle and move it to the left
        rect = Rectangle(width=width, height=height, color=BLUE)
        rect.set_fill(BLUE, opacity=0.5)
        rect.shift(LEFT * 3)

        # Add labels for length and breadth, moving them slightly further away
        length_label = Tex("l").next_to(rect, DOWN, buff=0.7)
        breadth_label = Tex("b").next_to(rect, LEFT, buff=0.7)

        # Create a VGroup for the labels to manage them together
        labels = VGroup(length_label, breadth_label)

        # Title
        title = Text("Area of a Rectangle")
        title.to_edge(UP)

        # Create double-sided arrows, significantly shorter than the sides
        length_arrow = DoubleArrow(
            start=rect.get_corner(DL) + LEFT * 0.5 + RIGHT * 1,
            end=rect.get_corner(DR) + RIGHT * 0.5 - RIGHT * 1,
            buff=0
        ).next_to(length_label, UP, buff=0.2)
        
        breadth_arrow = DoubleArrow(
            start=rect.get_corner(UL) + UP * 0.5 + DOWN * 1,
            end=rect.get_corner(DL) + DOWN * 0.5 - DOWN * 1,
            buff=0
        ).next_to(breadth_label, RIGHT, buff=0.2)

        # Animate the rectangle, labels, and arrows
        self.play(Create(rect))
        self.play(Write(labels))
        self.play(Create(length_arrow), Create(breadth_arrow))
        self.wait(1)

        # Animate the title
        self.play(Write(title))
        self.wait(2)
             
        p10=cvo.CVO().CreateCVO("formula","length(l) x breadth(b)").setPosition([2,1,0])
        p11=cvo.CVO().CreateCVO("example","l=3,b=4").setPosition([4,1,0])
        p12=cvo.CVO().CreateCVO("area","3*4= 12").setPosition([3,-2,0]).setangle(-TAU/4)
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
         
        self.construct1(p10,p10) 
        
if __name__ == "__main__":
    scene = PerimeterAndAreas()
    scene.render()
