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

        # Define vertices of the triangle
        A = np.array([0, 2, 0])
        B = np.array([-2, -1, 0])
        C = np.array([2, -1, 0])

        # Create the triangle with no fill
        triangle = Polygon(A, B, C, color=WHITE, fill_opacity=0).shift(LEFT*3)
        
        # Labels for the vertices
        label_a = MathTex("A", color=WHITE).next_to(A + LEFT*3, UP)
        label_b = MathTex("B", color=WHITE).next_to(B + LEFT*3, DOWN + LEFT*0.2)
        label_c = MathTex("C", color=WHITE).next_to(C + LEFT*3, DOWN + RIGHT*0.2)
        
        # Create double-sided arrows and labels for the sides
        side_ab = DoubleArrow(A, B, buff=0, color=WHITE).shift(UP*0.2 + LEFT*3)
        side_bc = DoubleArrow(B, C, buff=0, color=WHITE).shift(DOWN*0.2 + LEFT*3)
        side_ca = DoubleArrow(C, A, buff=0, color=WHITE).shift(RIGHT*0.2 + LEFT*3)
        
        label_ab = MathTex("a", color=WHITE).next_to(side_ab, LEFT)
        label_bc = MathTex("b", color=WHITE).next_to(side_bc, DOWN)
        label_ca = MathTex("c", color=WHITE).next_to(side_ca, RIGHT)
        
        # Create perimeter calculation text
        perimeter_text = MathTex(
            r"Perimeter = a + b + c", color=WHITE
        ).to_edge(DOWN)
        
        self.play(Write(heading))
        # Animate the drawing of the triangle
        self.play(Create(triangle))
        
        # Animate the drawing of the sides with labels
        self.play(GrowArrow(side_ab), Write(label_ab))
        self.play(GrowArrow(side_bc), Write(label_bc))
        self.play(GrowArrow(side_ca), Write(label_ca))
        
        # Show vertex labels
        self.play(Write(label_a), Write(label_b), Write(label_c))
        
        # Animate the appearance of the perimeter calculation
        self.play(Write(perimeter_text))
        
        # Keep the animation on screen for a few seconds
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

         # Define vertices of the square
        A = np.array([-1, 1, 0])
        B = np.array([1, 1, 0])
        C = np.array([1, -1, 0])
        D = np.array([-1, -1, 0])

        # Create the square with no fill
        square = Polygon(A, B, C, D, color=WHITE, fill_opacity=0).scale(0.8).shift(LEFT*3)
        
        # Labels for the vertices
        label_a = MathTex("A", color=WHITE).next_to(A + LEFT*3, UP)
        label_b = MathTex("B", color=WHITE).next_to(B + LEFT*3, UP)
        label_c = MathTex("C", color=WHITE).next_to(C + LEFT*3, DOWN)
        label_d = MathTex("D", color=WHITE).next_to(D + LEFT*3, DOWN)
        
        # Create double-sided arrows and labels for the sides
        side_ab = DoubleArrow(A, B, buff=0, color=WHITE).shift(UP*0.1 + LEFT*3)
        side_bc = DoubleArrow(B, C, buff=0, color=WHITE).shift(RIGHT*0.1 + LEFT*3)
        side_cd = DoubleArrow(C, D, buff=0, color=WHITE).shift(DOWN*0.1 + LEFT*3)
        side_da = DoubleArrow(D, A, buff=0, color=WHITE).shift(LEFT*0.1 + LEFT*3)
        
        label_ab = MathTex("s", color=WHITE).next_to(side_ab, UP)
        label_bc = MathTex("s", color=WHITE).next_to(side_bc, RIGHT)
        label_cd = MathTex("s", color=WHITE).next_to(side_cd, DOWN)
        label_da = MathTex("s", color=WHITE).next_to(side_da, LEFT)
        
        self.play(Write(heading))
        # Animate the drawing of the square
        self.play(Create(square))
        
        # Animate the drawing of the sides with labels
        self.play(GrowArrow(side_ab), Write(label_ab))
        self.play(GrowArrow(side_bc), Write(label_bc))
        self.play(GrowArrow(side_cd), Write(label_cd))
        self.play(GrowArrow(side_da), Write(label_da))
        
        # Show vertex labels
        self.play(Write(label_a), Write(label_b), Write(label_c), Write(label_d))
        
        # Keep the animation on screen for a few seconds
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

         # Define vertices of the rectangle
        A = np.array([-2, 1, 0])
        B = np.array([2, 1, 0])
        C = np.array([2, -1, 0])
        D = np.array([-2, -1, 0])

        # Create the rectangle with no fill
        rectangle = Polygon(A, B, C, D, color=WHITE, fill_opacity=0).shift(LEFT*3)
        
        # Labels for the vertices
        label_a = MathTex("A", color=WHITE).next_to(A + LEFT*3, UP)
        label_b = MathTex("B", color=WHITE).next_to(B + LEFT*3, UP)
        label_c = MathTex("C", color=WHITE).next_to(C + LEFT*3, DOWN)
        label_d = MathTex("D", color=WHITE).next_to(D + LEFT*3, DOWN)
        
        # Create double-sided arrows and labels for the sides
        side_ab = DoubleArrow(A, B, buff=0, color=WHITE).shift(UP*0.1 + LEFT*3)
        side_bc = DoubleArrow(B, C, buff=0, color=WHITE).shift(RIGHT*0.1 + LEFT*3)
        side_cd = DoubleArrow(C, D, buff=0, color=WHITE).shift(DOWN*0.1 + LEFT*3)
        side_da = DoubleArrow(D, A, buff=0, color=WHITE).shift(LEFT*0.1 + LEFT*3)
        
        label_ab = MathTex("l", color=WHITE).next_to(side_ab, UP)
        label_bc = MathTex("b", color=WHITE).next_to(side_bc, RIGHT)
        label_cd = MathTex("l", color=WHITE).next_to(side_cd, DOWN)
        label_da = MathTex("b", color=WHITE).next_to(side_da, LEFT)
        
        self.play(Write(heading))
        # Animate the drawing of the rectangle
        self.play(Create(rectangle))
        
        # Animate the drawing of the sides with labels
        self.play(GrowArrow(side_ab), Write(label_ab))
        self.play(GrowArrow(side_bc), Write(label_bc))
        self.play(GrowArrow(side_cd), Write(label_cd))
        self.play(GrowArrow(side_da), Write(label_da))
        
        # Show vertex labels
        self.play(Write(label_a), Write(label_b), Write(label_c), Write(label_d))
        
        # Keep the animation on screen for a few seconds
        self.wait(2)

        p10=cvo.CVO().CreateCVO("formula","2(l+b)").setPosition([2,1,0])
        p11=cvo.CVO().CreateCVO("example","l=2,b=3").setPosition([4,1,0])
        p12=cvo.CVO().CreateCVO("perimeter","2(2+3) = 10").setPosition([3,-2,0]).setangle(-TAU/4)
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
         
        self.construct1(p10,p10)    

    def perimeterofpentagon(self):
         # Create a heading
        heading = Text("Perimeter of a Regular Polygon (Pentagon)")
        heading.to_edge(UP)

        # Define side length of the pentagon
        side_length = 2

        # Create a pentagon
        pentagon = RegularPolygon(n=5, start_angle=0, color=WHITE)
        pentagon.set_width(side_length)
        pentagon.move_to(LEFT * 3)

        # Get vertices of the pentagon
        vertices = pentagon.get_vertices()

        # Choose one side of the pentagon (for example, the first side)
        side_index = 0
        start_point = vertices[side_index]
        end_point = vertices[(side_index + 1) % 5]

        # Calculate direction vector and perpendicular vector
        direction_vector = (end_point - start_point) / np.linalg.norm(end_point - start_point)
        perpendicular_vector = np.array([-direction_vector[1], direction_vector[0], 0])

        # Position arrow and label
        arrow_start = start_point + perpendicular_vector * 0.5
        arrow_end = end_point + perpendicular_vector * 0.5
        arrow = DoubleArrow(arrow_start, arrow_end, buff=0.2, stroke_width=8, color=BLUE)
        label = MathTex("a", color=WHITE).next_to((arrow_start + arrow_end) / 2, perpendicular_vector, buff=0.2)

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
        heading = Text("Perimeter of a Regular polygon(Hexagon)")
        heading.to_edge(UP)

        # Define side length of the hexagon
        side_length = 2

        # Create a hexagon
        hexagon = RegularPolygon(n=6, start_angle=0, color=WHITE)
        hexagon.set_width(side_length)
        hexagon.move_to(LEFT * 3)

        # Get vertices of the hexagon
        vertices = hexagon.get_vertices()

        # Animate the drawing of the hexagon
        hexagon_edges = VGroup()
        for i in range(6):
            edge = Line(vertices[i], vertices[(i + 1) % 6], color=WHITE)
            hexagon_edges.add(edge)

        # Create arrow and label for one side (e.g., side A)
        side_label = "s"
        start_point = vertices[0]
        end_point = vertices[1]
        direction_vector = (end_point - start_point) / np.linalg.norm(end_point - start_point)
        perpendicular_vector = np.array([-direction_vector[1], direction_vector[0], 0])

        # Calculate arrow positions
        arrow_start = start_point + perpendicular_vector * 0.5
        arrow_end = end_point + perpendicular_vector * 0.5

        arrow = DoubleArrow(arrow_start, arrow_end, buff=0.2, stroke_width=8, color=BLUE)
        label = MathTex(side_label, color=WHITE).next_to((start_point + end_point) / 2, perpendicular_vector, buff=0.2)

        # Calculate perimeter formula
        perimeter_formula = MathTex("P = 6 \\times s")
        perimeter_formula.to_corner(DR)

        # Add heading, hexagon, arrow, label, and formula to the scene
        self.play(Write(heading))
        self.play(Create(hexagon_edges), run_time=3)
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
        heading = Text("Perimeter of a Regular polygon(Octagon)")
        heading.to_edge(UP)

        # Define side length of the octagon
        side_length = 2

        # Create an octagon
        octagon = RegularPolygon(n=8, start_angle=0, color=WHITE)
        octagon.set_width(side_length)
        octagon.move_to(LEFT * 3)

        # Get vertices of the octagon
        vertices = octagon.get_vertices()

        # Animate the drawing of the octagon
        octagon_edges = VGroup()
        for i in range(8):
            edge = Line(vertices[i], vertices[(i + 1) % 8], color=WHITE)
            octagon_edges.add(edge)

        # Create double-sided arrow and label for one side (e.g., side A)
        side_label = "s"
        start_point = vertices[0]
        end_point = vertices[1]
        direction_vector = (end_point - start_point) / np.linalg.norm(end_point - start_point)
        perpendicular_vector = np.array([-direction_vector[1], direction_vector[0], 0])

        # Calculate arrow positions
        arrow_start = start_point + perpendicular_vector * 0.3 + UP * 0.15
        arrow_end = end_point + perpendicular_vector * 0.3 + UP * 0.15

        arrow = DoubleArrow(arrow_start, arrow_end, buff=0.2, stroke_width=8, color=BLUE)
        label = MathTex(side_label, color=WHITE).next_to(arrow_end, DOWN, buff=0.2)

        # Calculate perimeter formula
        perimeter_formula = MathTex("P = 8 \\times s")
        perimeter_formula.to_corner(DR)

        # Add heading, octagon, arrow, label, and formula to the scene
        self.play(Write(heading))
        self.play(Create(octagon_edges), run_time=3)
        self.play(Create(arrow), Write(label))
        self.play(Write(perimeter_formula))

        # Hold the final frame for a few seconds
        self.wait(2)

        
        p10=cvo.CVO().CreateCVO("octagon","8-sided polygon(all sides are equal)").setPosition([2,1,0])
        p11=cvo.CVO().CreateCVO("formula","8 x length of any side(a)").setPosition([5,1,0])
        p12=cvo.CVO().CreateCVO("example","a=2").setPosition([2,-2,0]).setangle(-TAU/4)
        p13=cvo.CVO().CreateCVO("Perimeter","8*3 = 16").setPosition([5,-2,0]).setangle(-TAU/4)
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
        heading = Text("Area of Triangle")
        heading.to_edge(UP)
        self.play(Write(heading))
        self.wait(1)

        # Define the vertices of the triangle
        A = np.array([-4, -2, 0])
        B = np.array([-1, -2, 0])
        C = np.array([-2, 2, 0])

        # Create the triangle outline
        triangle_outline = Polygon(A, B, C, stroke_color=WHITE, stroke_width=2, fill_opacity=0)
        
        # Create the triangle with shading
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

        # Add triangle outline to the scene
        self.play(Create(triangle_outline))
        self.wait(1)

        # Add triangle with shading and labels
        self.play(Transform(triangle_outline, triangle), Write(label_A), Write(label_B), Write(label_C))
        self.wait(1)

        # Add arrows and labels for base and height
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

        A = np.array([-1, 1, 0])
        B = np.array([1, 1, 0])
        C = np.array([1, -1, 0])
        D = np.array([-1, -1, 0])

        # Create the square with fill
        square = Polygon(A, B, C, D, color=BLUE, fill_opacity=0).scale(0.8).shift(LEFT*3)
        
        # Labels for the vertices
        label_a = MathTex("A", color=WHITE).next_to(A + LEFT*3, UP)
        label_b = MathTex("B", color=WHITE).next_to(B + LEFT*3, UP)
        label_c = MathTex("C", color=WHITE).next_to(C + LEFT*3, DOWN)
        label_d = MathTex("D", color=WHITE).next_to(D + LEFT*3, DOWN)
        
        # Create double-sided arrows and labels for the sides
        side_ab = DoubleArrow(A, B, buff=0, color=WHITE).shift(UP*0.1 + LEFT*3)
        side_bc = DoubleArrow(B, C, buff=0, color=WHITE).shift(RIGHT*0.1 + LEFT*3)
        side_cd = DoubleArrow(C, D, buff=0, color=WHITE).shift(DOWN*0.1 + LEFT*3)
        side_da = DoubleArrow(D, A, buff=0, color=WHITE).shift(LEFT*0.1 + LEFT*3)
        
        label_ab = MathTex("s", color=WHITE).next_to(side_ab, UP)
        label_bc = MathTex("s", color=WHITE).next_to(side_bc, RIGHT)
        label_cd = MathTex("s", color=WHITE).next_to(side_cd, DOWN)
        label_da = MathTex("s", color=WHITE).next_to(side_da, LEFT)
        
        self.play(Write(heading))
        # Animate the drawing and filling of the square
        self.play(Create(square))
        
        # Animate the drawing of the sides with labels
        self.play(GrowArrow(side_ab), Write(label_ab))
        self.play(GrowArrow(side_bc), Write(label_bc))
        self.play(GrowArrow(side_cd), Write(label_cd))
        self.play(GrowArrow(side_da), Write(label_da))
        
        # Show vertex labels
        self.play(Write(label_a), Write(label_b), Write(label_c), Write(label_d))
        
        # Fill the square
        square.set_fill(color=BLUE, opacity=0.5)
        self.wait(1)

        # Keep the animation on screen for a few seconds
        self.wait(2)

        p10=cvo.CVO().CreateCVO("formula","side x side").setPosition([2,1,0])
        p11=cvo.CVO().CreateCVO("example","s=3").setPosition([4,1,0])
        p12=cvo.CVO().CreateCVO("area","3*3 = 9").setPosition([3,-2,0]).setangle(-TAU/4)
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
         
        self.construct1(p10,p10) 
        
    def areaofrectangle(self):
        heading = Text("Area of a Rectangle").to_edge(UP)
        # Define vertices of the rectangle
        A = np.array([-2, 1, 0])
        B = np.array([2, 1, 0])
        C = np.array([2, -1, 0])
        D = np.array([-2, -1, 0])

        # Create the rectangle with no fill initially
        rectangle = Polygon(A, B, C, D, color=WHITE, fill_opacity=0).scale(0.8).shift(LEFT*3)
        
        # Labels for the vertices
        label_a = MathTex("A", color=WHITE).next_to(A + LEFT*3, UP)
        label_b = MathTex("B", color=WHITE).next_to(B + LEFT*3, UP)
        label_c = MathTex("C", color=WHITE).next_to(C + LEFT*3, DOWN)
        label_d = MathTex("D", color=WHITE).next_to(D + LEFT*3, DOWN)
        
        # Create double-sided arrows and labels for the sides
        side_ab = DoubleArrow(A, B, buff=0, color=WHITE).shift(UP*0.1 + LEFT*3)
        side_bc = DoubleArrow(B, C, buff=0, color=WHITE).shift(RIGHT*0.1 + LEFT*3)
        side_cd = DoubleArrow(C, D, buff=0, color=WHITE).shift(DOWN*0.1 + LEFT*3)
        side_da = DoubleArrow(D, A, buff=0, color=WHITE).shift(LEFT*0.1 + LEFT*3)
        
        label_ab = MathTex("l", color=WHITE).next_to(side_ab, UP)
        label_bc = MathTex("b", color=WHITE).next_to(side_bc, RIGHT)
        label_cd = MathTex("l", color=WHITE).next_to(side_cd, DOWN)
        label_da = MathTex("b", color=WHITE).next_to(side_da, LEFT)
        
        self.play(Write(heading))
        # Animate the drawing and filling of the rectangle
        self.play(Create(rectangle))
        
        # Animate the drawing of the sides with labels
        self.play(GrowArrow(side_ab), Write(label_ab))
        self.play(GrowArrow(side_bc), Write(label_bc))
        self.play(GrowArrow(side_cd), Write(label_cd))
        self.play(GrowArrow(side_da), Write(label_da))
        
        # Show vertex labels
        self.play(Write(label_a), Write(label_b), Write(label_c), Write(label_d))
        
        # Fill the rectangle
        rectangle.set_fill(color=BLUE, opacity=0.5)
        self.wait(1)

        # Keep the animation on screen for a few seconds
        self.wait(2)

        p10=cvo.CVO().CreateCVO("formula","length(l) x breadth(b)").setPosition([2,1,0])
        p11=cvo.CVO().CreateCVO("example","l=3,b=4").setPosition([4,1,0])
        p12=cvo.CVO().CreateCVO("area","3*4= 12").setPosition([3,-2,0]).setangle(-TAU/4)
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
         
        self.construct1(p10,p10) 
    
    def SetDeveloperList(self):
        self.developerlist="vasudha"  
        
if __name__ == "__main__":
    scene = PerimeterAndAreas()
    scene.render()
