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
config.max_files_cached = 1000  # Change this number to your desired value


class Grade6Chapter10PerimeterAndAreas(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.Intro()
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
    
    def SetDeveloperList(self):
        self.DeveloperList="Vasudha"
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade6CH10PerimeterAndArea"
        
    def Intro(self): 
        heading = Text("CHAPTER-10:Perimeter and Areas",color=PURPLE)
        heading.to_edge(ORIGIN + UP) 
        self.play(Write(heading))
        self.wait(2)
        self.play(heading.animate.to_edge(UP))
        
    def introduction(self):
        
        self.setNumberOfCirclePositions(3)
        self.isRandom = False
        p10 = cvo.CVO().CreateCVO("Perimeter and Area", "").setPosition([-3,0,0])
        p12 = cvo.CVO().CreateCVO("Perimeter", "the perimeter of a shape is defined as the total length of its boundary.").setPosition([1,2,0])
        p13 = cvo.CVO().CreateCVO("Area", "Area is the amount of space inside a shape.").setPosition([1,-2,0])

        p10.cvolist.append(p12)
        p10.cvolist.append(p13)

        self.construct1(p10, p10)

    def shapes(self):
        self.setNumberOfCirclePositions(2)
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Perimeter and Area","")
        p11=cvo.CVO().CreateCVO("Shapes","").setPosition([2,0,0])
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
        triangle = Polygon(A, B, C, color=WHITE, fill_opacity=0).shift(LEFT*4)
        
        # Labels for the vertices
        label_a = MathTex("A", color=WHITE).next_to(A + LEFT*4, UP)
        label_b = MathTex("B", color=WHITE).next_to(B + LEFT*4, DOWN + LEFT*0.2)
        label_c = MathTex("C", color=WHITE).next_to(C + LEFT*4, DOWN + RIGHT*0.2)
        
        # Create double-sided arrows and labels for the sides
        side_ab = DoubleArrow(A, B, buff=0, color=WHITE).shift(UP*0.2 + LEFT*4)
        side_bc = DoubleArrow(B, C, buff=0, color=WHITE).shift(DOWN*0.2 + LEFT*4)
        side_ca = DoubleArrow(C, A, buff=0, color=WHITE).shift(RIGHT*0.2 + LEFT*4)
        
        label_ab = MathTex("a", color=WHITE).next_to(side_ab, LEFT)
        label_bc = MathTex("b", color=WHITE).next_to(side_bc, DOWN)
        label_ca = MathTex("c", color=WHITE).next_to(side_ca, RIGHT)
        
        # Create perimeter calculation text
        perimeter_text = MathTex(
            r"Perimeter = (a + b + c)", color=WHITE
        ).to_corner(DL*3, buff=0.3)
        
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
        
        self.isRandom = False
        self.angleChoice = [TAU/2,-TAU/2]
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
        square = Polygon(A, B, C, D, color=WHITE, fill_opacity=0).scale(0.8).shift(LEFT*4)
        
        # Labels for the vertices
        label_a = MathTex("A", color=WHITE).next_to(A + LEFT*4, UP)
        label_b = MathTex("B", color=WHITE).next_to(B + LEFT*4, UP)
        label_c = MathTex("C", color=WHITE).next_to(C + LEFT*4, DOWN)
        label_d = MathTex("D", color=WHITE).next_to(D + LEFT*4, DOWN)
        
        # Create double-sided arrows and labels for the sides
        side_ab = DoubleArrow(A, B, buff=0, color=WHITE).shift(UP*0.1 + LEFT*4)
        side_bc = DoubleArrow(B, C, buff=0, color=WHITE).shift(RIGHT*0.1 + LEFT*4)
        side_cd = DoubleArrow(C, D, buff=0, color=WHITE).shift(DOWN*0.1 + LEFT*4)
        side_da = DoubleArrow(D, A, buff=0, color=WHITE).shift(LEFT*0.1 + LEFT*4)
        
        label_ab = MathTex("s", color=WHITE).next_to(side_ab, UP)
        label_bc = MathTex("s", color=WHITE).next_to(side_bc, RIGHT)
        label_cd = MathTex("s", color=WHITE).next_to(side_cd, DOWN)
        label_da = MathTex("s", color=WHITE).next_to(side_da, LEFT)
        
        perimeter_text = MathTex(
            r"Perimeter = 4*length of a side", color=WHITE
        ).to_corner(DL*3, buff=0.3)
        
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
        
        self.play(Write(perimeter_text))
        
        # Keep the animation on screen for a few seconds
        self.wait(2)
        
        self.isRandom = False
        self.angleChoice = [TAU/2,-TAU/2]
        p10=cvo.CVO().CreateCVO("formula","4*length of a side(s)").setPosition([2,1,0])
        p11=cvo.CVO().CreateCVO("example","s=4").setPosition([4,1,0])
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
        rectangle = Polygon(A, B, C, D, color=WHITE, fill_opacity=0).shift(LEFT*4)
        
        # Labels for the vertices
        label_a = MathTex("A", color=WHITE).next_to(A + LEFT*4, UP)
        label_b = MathTex("B", color=WHITE).next_to(B + LEFT*4, UP)
        label_c = MathTex("C", color=WHITE).next_to(C + LEFT*4, DOWN)
        label_d = MathTex("D", color=WHITE).next_to(D + LEFT*4, DOWN)
        
        # Create double-sided arrows and labels for the sides
        side_ab = DoubleArrow(A, B, buff=0, color=WHITE).shift(UP*0.1 + LEFT*4)
        side_bc = DoubleArrow(B, C, buff=0, color=WHITE).shift(RIGHT*0.1 + LEFT*4)
        side_cd = DoubleArrow(C, D, buff=0, color=WHITE).shift(DOWN*0.1 + LEFT*4)
        side_da = DoubleArrow(D, A, buff=0, color=WHITE).shift(LEFT*0.1 + LEFT*4)
        
        label_ab = MathTex("l", color=WHITE).next_to(side_ab, UP)
        label_bc = MathTex("b", color=WHITE).next_to(side_bc, RIGHT)
        label_cd = MathTex("l", color=WHITE).next_to(side_cd, DOWN)
        label_da = MathTex("b", color=WHITE).next_to(side_da, LEFT)
        
        perimeter_text = MathTex(
            r"Perimeter = 2(l + b)", color=WHITE
        ).to_corner(DL*3, buff=0.3)
        
        
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
        self.play(Write(perimeter_text))
        
        # Keep the animation on screen for a few seconds
        self.wait(2)
        
        self.isRandom = False
        self.angleChoice = [TAU/2,-TAU/2]
        p10=cvo.CVO().CreateCVO("formula","2(l+b)").setPosition([2,1,0])
        p11=cvo.CVO().CreateCVO("example","l=2,b=3").setPosition([4,1,0])
        p12=cvo.CVO().CreateCVO("perimeter","2(2+3) = 10").setPosition([3,-2,0]).setangle(-TAU/4)
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
         
        self.construct1(p10,p10)    

    def perimeterofpentagon(self):
        heading = Text("Perimeter of a Regular Polygon (Pentagon)")
        heading.to_edge(UP)

        # Define side length of the pentagon
        side_length = 2

        # Create a pentagon
        pentagon = RegularPolygon(n=5, start_angle=0, color=WHITE)
        pentagon.set_width(side_length)
        pentagon.move_to(LEFT * 4)

        # Get vertices of the pentagon
        vertices = pentagon.get_vertices()

        # Choose the top-right side of the pentagon
        side_index = 0  # Top-right side
        start_point = vertices[side_index]
        end_point = vertices[(side_index + 1) % 5]

        # Calculate direction vector and perpendicular vector
        direction_vector = (end_point - start_point) / np.linalg.norm(end_point - start_point)
        perpendicular_vector = np.array([-direction_vector[1], direction_vector[0], 0])

        # Position arrow and label above the side
        arrow_offset = -0.2  # Adjust this value to move the arrow further out
        arrow_start = start_point + perpendicular_vector * arrow_offset
        arrow_end = end_point + perpendicular_vector * arrow_offset
        arrow = DoubleArrow(arrow_start, arrow_end, buff=0.1, stroke_width=6, color=BLUE)
        label = MathTex("a", color=WHITE).next_to(arrow, UP + RIGHT, buff=0.05)
        self.wait(2)

        # Calculate perimeter formula
        perimeter_formula = MathTex("P = 5 \\times a")
        perimeter_formula.next_to(pentagon, DOWN, buff=1)

        # Add heading, pentagon, arrow, label, and formula to the scene
        self.play(Write(heading))
        self.play(Create(pentagon))
        self.play(Create(arrow), Write(label))
        self.play(Write(perimeter_formula))

        # Hold the final frame for a few seconds
        self.wait(2)
        
        self.isRandom = False
        self.angleChoice = [TAU/4,TAU/2,-TAU/4]
        p10=cvo.CVO().CreateCVO("pentagon","5-sided polygon(all sides are equal)").setPosition([2,1,0])
        p11=cvo.CVO().CreateCVO("formula","5 x length of any side(a)").setPosition([5,1,0])
        p12=cvo.CVO().CreateCVO("example","a=3").setPosition([5,-2,0])
        p13=cvo.CVO().CreateCVO("perimeter","5*3 = 15").setPosition([2,-2,0])
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
        hexagon.move_to(LEFT * 4)

        # Get vertices of the hexagon
        vertices = hexagon.get_vertices()

        # Animate the drawing of the hexagon
        hexagon_edges = VGroup()
        for i in range(6):
            edge = Line(vertices[i], vertices[(i + 1) % 6], color=WHITE)
            hexagon_edges.add(edge)

        # Create arrow and label for the top-right side
        side_label = "s"
        start_point = vertices[0]  # Top vertex
        end_point = vertices[1]    # Top-right vertex
        direction_vector = (end_point - start_point) / np.linalg.norm(end_point - start_point)
        perpendicular_vector = np.array([-direction_vector[1], direction_vector[0], 0])

        # Calculate arrow positions (outside the hexagon)
        arrow_offset = -0.2  # Adjust this value to move the arrow further out
        arrow_start = start_point + perpendicular_vector * arrow_offset
        arrow_end = end_point + perpendicular_vector * arrow_offset

        arrow = DoubleArrow(arrow_start, arrow_end, buff=0.2, stroke_width=8, color=BLUE)
        label = MathTex(side_label, color=WHITE).next_to(arrow, UP + RIGHT, buff=0.1)

        self.wait(2)

        # Calculate perimeter formula
        perimeter_formula = MathTex("P = 6 \\times s")
        perimeter_formula.next_to(hexagon, DOWN, buff=0.5)  # Position below the hexagon

        # Add heading, hexagon, arrow, label, and formula to the scene
        self.play(Write(heading))
        self.play(Create(hexagon_edges), run_time=3)
        self.play(Create(arrow), Write(label))
        self.play(Write(perimeter_formula))

        # Hold the final frame for a few seconds
        self.wait(2)
        self.isRandom = False
        self.angleChoice = [TAU/4,TAU/2,-TAU/4,]
        p10=cvo.CVO().CreateCVO("hexagon","6-sided polygon(all sides are equal)").setPosition([2,1,0])
        p11=cvo.CVO().CreateCVO("formula","6 x length of any side(s)").setPosition([5,1,0])
        p12=cvo.CVO().CreateCVO("example","s=3").setPosition([5,-2,0])
        p13=cvo.CVO().CreateCVO("perimeter","6*3 = 18").setPosition([2,-2,0])
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
        octagon.move_to(LEFT * 4)

        # Get vertices of the octagon
        vertices = octagon.get_vertices()

        # Animate the drawing of the octagon
        octagon_edges = VGroup()
        for i in range(8):
            edge = Line(vertices[i], vertices[(i + 1) % 8], color=WHITE)
            octagon_edges.add(edge)

        # Create double-sided arrow and label for the right side
        side_label = "s"
        start_point = vertices[2]  # Right-top vertex
        end_point = vertices[3]    # Right-bottom vertex
        direction_vector = (end_point - start_point) / np.linalg.norm(end_point - start_point)
        perpendicular_vector = np.array([-direction_vector[1], direction_vector[0], 0])

        # Calculate arrow positions (outside the octagon)
        arrow_offset = -0.2  # Adjust this value to move the arrow further out
        arrow_start = start_point + perpendicular_vector * arrow_offset
        arrow_end = end_point + perpendicular_vector * arrow_offset

        arrow = DoubleArrow(arrow_start, arrow_end, buff=0.1, stroke_width=8, color=BLUE)
        label = MathTex(side_label, color=WHITE).next_to(arrow, UP, buff=0.1)

        # Calculate perimeter formula
        perimeter_formula = MathTex("P = 8 \\times s")
        perimeter_formula.next_to(octagon, DOWN, buff=0.5)  # Position below the octagon

        # Add heading, octagon, arrow, label, and formula to the scene
        self.play(Write(heading))
        self.play(Create(octagon_edges), run_time=3)
        self.play(Create(arrow), Write(label))
        self.play(Write(perimeter_formula))

        # Hold the final frame for a few seconds
        self.wait(2)
        
        self.isRandom = False
        self.angleChoice = [TAU/4,TAU/2,-TAU/4]
        p10=cvo.CVO().CreateCVO("octagon","8-sided polygon(all sides are equal)").setPosition([2,1,0])
        p11=cvo.CVO().CreateCVO("formula","8 x length of any side(s)").setPosition([5,1,0])
        p12=cvo.CVO().CreateCVO("example","s=2").setPosition([5,-2,0])
        p13=cvo.CVO().CreateCVO("Perimeter","8*3 = 16").setPosition([2,-2,0])
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

        # Define the vertices of the triangle (moved further left)
        A = np.array([-6, -2, 0])  # Changed from -4 to -6
        B = np.array([-3, -2, 0])  # Changed from -1 to -3
        C = np.array([-4, 2, 0])   # Changed from -2 to -4

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
        label_base = MathTex("base(b)").next_to(arrow_base, DOWN, buff=0.1)

        # Create the double-sided arrows for the height (from C to the perpendicular point on AB)
        height_point_on_AB = np.array([C[0], A[1], 0])  # Point on AB directly above C
        arrow_height = DoubleArrow(C, height_point_on_AB, buff=0.1, stroke_width=5)
        label_height = MathTex("height(h)").next_to(arrow_height, RIGHT, buff=0.1)

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
        
        self.isRandom = False
        self.angleChoice = [TAU/2,-TAU/2]
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
        square = Polygon(A, B, C, D, color=BLUE, fill_opacity=0).scale(0.8).shift(LEFT*4)
        
        # Labels for the vertices
        label_a = MathTex("A", color=WHITE).next_to(A + LEFT*4, UP)
        label_b = MathTex("B", color=WHITE).next_to(B + LEFT*4, UP)
        label_c = MathTex("C", color=WHITE).next_to(C + LEFT*4, DOWN)
        label_d = MathTex("D", color=WHITE).next_to(D + LEFT*4, DOWN)
        
        # Create double-sided arrows and labels for the sides
        side_ab = DoubleArrow(A, B, buff=0, color=WHITE).shift(UP*0.1 + LEFT*4)
        side_bc = DoubleArrow(B, C, buff=0, color=WHITE).shift(RIGHT*0.1 + LEFT*4)
        side_cd = DoubleArrow(C, D, buff=0, color=WHITE).shift(DOWN*0.1 + LEFT*4)
        side_da = DoubleArrow(D, A, buff=0, color=WHITE).shift(LEFT*0.1 + LEFT*4)
        
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
        
        self.isRandom = False
        self.angleChoice = [TAU/2,-TAU/2]
        p10=cvo.CVO().CreateCVO("formula","side(s) x side(s)").setPosition([2,1,0])
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
        rectangle = Polygon(A, B, C, D, color=WHITE, fill_opacity=0).scale(0.8).shift(LEFT*4)
        
        # Labels for the vertices
        label_a = MathTex("A", color=WHITE).next_to(A + LEFT*4, UP)
        label_b = MathTex("B", color=WHITE).next_to(B + LEFT*4, UP)
        label_c = MathTex("C", color=WHITE).next_to(C + LEFT*4, DOWN)
        label_d = MathTex("D", color=WHITE).next_to(D + LEFT*4, DOWN)
        
        # Create double-sided arrows and labels for the sides
        side_ab = DoubleArrow(A, B, buff=0, color=WHITE).shift(UP*0.1 + LEFT*4)
        side_bc = DoubleArrow(B, C, buff=0, color=WHITE).shift(RIGHT*0.1 + LEFT*4)
        side_cd = DoubleArrow(C, D, buff=0, color=WHITE).shift(DOWN*0.1 + LEFT*4)
        side_da = DoubleArrow(D, A, buff=0, color=WHITE).shift(LEFT*0.1 + LEFT*4)
        
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
        
        self.isRandom = False
        self.angleChoice = [TAU/2,-TAU/2]
        p10=cvo.CVO().CreateCVO("formula","l x b").setPosition([2,1,0])
        p11=cvo.CVO().CreateCVO("example","l=3,b=4").setPosition([4,1,0])
        p12=cvo.CVO().CreateCVO("area","3*4= 12").setPosition([3,-2,0]).setangle(-TAU/4)
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
         
        self.construct1(p10,p10) 
    

if __name__ == "__main__":
    scene = Grade6Chapter10PerimeterAndAreas()
    scene.render()
