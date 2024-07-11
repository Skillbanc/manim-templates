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

class grade5(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.constructDataByCVO()
        self.fadeOutCurrentScene()
        self.perimeter()
        self.fadeOutCurrentScene()
        self.square()
        self.fadeOutCurrentScene()
        self.triangle()
        self.fadeOutCurrentScene()
        self.tri1()
        self.fadeOutCurrentScene
        self.trapezium()
        self.fadeOutCurrentScene()
        self.trap1()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

        



    # render using CVO data object
    def constructDataByCVO(self):
        p10=cvo.CVO().CreateCVO("Spaces and Boundaries","I")
        p11=cvo.CVO().CreateCVO("Perimeter", "Total length of the boundry")
        
       
        p10.cvolist.append(p11)
       
       
        self.setNumberOfCirclePositions(2) 

        self.construct1(p10,p10)

   

    def perimeter(self):
       
        p22=cvo.CVO().CreateCVO("calculating perimeter of a square"," length of each side = 3")
        p23=cvo.CVO().CreateCVO("perimeter", "Sum of all the sides")
        
       
        p22.cvolist.append(p23)
       
       
        self.setNumberOfCirclePositions(2) 

        self.construct1(p22,p22)
# To run the code, save it in a file named `perimeter_of_square.py` and run:
# manim -pql perimeter_of_square.py PerimeterOfSquare


    def square(self):
     
        # Title
        title = Text("Perimeter of Square").to_edge(UP)
        
        # Square with different colors
        square = Square(side_length=3, color=BLUE)
        square.shift(RIGHT * 3)
        
        # Labels for vertices
        labels = ["A", "B", "C", "D"]
        vertex_labels = VGroup(*[Text(label) for label in labels])
        vertex_positions = [UP + LEFT, UP + RIGHT, DOWN + RIGHT, DOWN + LEFT]
        for i, vertex_label in enumerate(vertex_labels):
            vertex_label.next_to(square.get_vertices()[i], vertex_positions[i], buff=0.1)
        
        # Labels for sides with different colors
        side_length = "3m"
        side_colors = [RED, GREEN, YELLOW, ORANGE]
        side_labels = VGroup(
            Text(side_length, color=side_colors[0]).next_to(square.get_center() + 1.5 * UP, UP, buff=0.1),
            Text(side_length, color=side_colors[1]).next_to(square.get_center() + 1.5 * RIGHT, RIGHT, buff=0.1),
            Text(side_length, color=side_colors[2]).next_to(square.get_center() + 1.5 * DOWN, DOWN, buff=0.1),
            Text(side_length, color=side_colors[3]).next_to(square.get_center() + 1.5 * LEFT, LEFT, buff=0.1),
        )
        
        # Calculation steps with reduced font size
        calc_steps = VGroup(
            Text("Perimeter = Sum of all sides", font_size=28).to_edge(LEFT).shift(UP*2),
            Text("= 3m + 3m + 3m + 3m", font_size=28).to_edge(LEFT).shift(UP*1),
            Text("= 4 * 3m", font_size=28).to_edge(LEFT),
            Text("= 12m", font_size=28).to_edge(LEFT).shift(DOWN*1),
            Text("The perimeter of square is 12m", font_size=28).to_edge(LEFT).shift(DOWN*2)  # Conclusion
        )
        
        # Drawing elements
        self.play(Write(title))
        self.play(Create(square))
        self.play(*[Write(vertex_label) for vertex_label in vertex_labels])
        self.play(*[Write(side_label) for side_label in side_labels])
        self.play(*[Write(step) for step in calc_steps])

        # Keeping the screen for a few seconds
        self.wait(3)

# To run the code, use:
# manim -pql perimeter_of_square.py PerimeterOfSquare


    def triangle(self):
        p10=cvo.CVO().CreateCVO("Calculating perimeter of a triangle"," Length of sides = 4m,3m,5m")
        p11=cvo.CVO().CreateCVO("Perimeter", "Sum of all sides")
        
       
        p10.cvolist.append(p11)
       
       
        self.setNumberOfCirclePositions(2) 

        self.construct1(p10,p10)

        self.fadeOutCurrentScene()


    def tri1(self):
    
     
        # Title
        title = Text("Perimeter of Triangle").to_edge(UP)
        
        # Triangle with different colors
        triangle = Polygon(
            [0, 0, 0],
            [2, 2, 0],
            [4, 0, 0],
            color=BLUE
        )
        triangle.shift(RIGHT * 1.5)
        
        # Labels for vertices
        labels = ["A", "B", "C"]
        vertex_labels = VGroup(*[Text(label) for label in labels])
        vertex_positions = [DOWN + LEFT, UP, DOWN + RIGHT]
        for i, vertex_label in enumerate(vertex_labels):
            vertex_label.next_to(triangle.get_vertices()[i], vertex_positions[i], buff=0.1)
        
        # Labels for sides with different colors
        side_lengths = ["3m", "4m", "5m"]
        side_colors = [RED, GREEN, ORANGE]
        side_labels = VGroup(
            Text(side_lengths[0], color=side_colors[0]).next_to(triangle.get_center() + 1.5 * LEFT, LEFT, buff=0.1),
            Text(side_lengths[1], color=side_colors[1]).next_to(triangle.get_center() + 1.5 * DOWN, DOWN, buff=0.1),
            Text(side_lengths[2], color=side_colors[2]).next_to(triangle.get_center() + 1.5 * RIGHT, RIGHT, buff=0.1),
        )
        
        # Calculation steps with reduced font size
        calc_steps = VGroup(
            Text("Perimeter = Sum of all sides", font_size=28).to_edge(LEFT).shift(UP*2),
            Text("= 3m + 4m + 5m", font_size=28).to_edge(LEFT).shift(UP*1),
            Text("= 12m", font_size=28).to_edge(LEFT),
            Text("The perimeter of triangle is 12m", font_size=28).to_edge(LEFT).shift(DOWN*1)  # Conclusion
        )
        
        # Drawing elements
        self.play(Write(title))
        self.play(Create(triangle))
        self.play(*[Write(vertex_label) for vertex_label in vertex_labels])
        self.play(*[Write(side_label) for side_label in side_labels])
        self.play(*[Write(step) for step in calc_steps])

        # Keeping the screen for a few seconds
        self.wait(3)
        self.fadeOutCurrentScene()
# To run the code, use:
# manim -pql perimeter_of_triangle.py PerimeterOfTriangle


    def trapezium(self):
        p10=cvo.CVO().CreateCVO("calculating perimeter of a trapezium"," length of each side = 5cm")
        p11=cvo.CVO().CreateCVO("perimeter", "sum of all the sides")
        
       
        p10.cvolist.append(p11)
       
       
        self.setNumberOfCirclePositions(2) 

        self.construct1(p10,p10)

      
    def trap1(self):
        # Title
        title = Text("Perimeter of Trapezium").to_edge(UP, buff=0.5)
        
        # Trapezium with different colors
        trapezium = Polygon(
            [-2, 0, 0],  # A
            [-1, 2, 0],  # B
            [1, 2, 0],   # C
            [2, 0, 0],   # D
            color=BLUE,
            stroke_width=2,
        )
        trapezium.scale(1.5)
        
        # Shift the trapezium to the right and slightly down
        trapezium.shift(RIGHT * 3 + DOWN * 0.5)

        # Labels for vertices
        labels = ["A", "B", "C", "D"]
        vertex_labels = VGroup(*[Text(label) for label in labels])
        vertex_positions = [DOWN + LEFT, UP + LEFT, UP + RIGHT, DOWN + RIGHT]
        for i, vertex_label in enumerate(vertex_labels):
            vertex_label.next_to(trapezium.get_vertices()[i], vertex_positions[i], buff=0.2)
        
        # Labels for sides with different colors
        side_lengths = ["4m", "4m", "5m", "6m"]  # Updated lengths
        side_colors = [RED, GREEN, ORANGE, PURPLE]
        side_label_positions = [
            trapezium.get_vertices()[0] + (trapezium.get_vertices()[1] - trapezium.get_vertices()[0]) * 0.5 + UP * 0.5,   # AB midpoint
            trapezium.get_vertices()[1] + (trapezium.get_vertices()[2] - trapezium.get_vertices()[1]) * 0.5 + LEFT * 0.8,   # BC midpoint
            trapezium.get_vertices()[2] + (trapezium.get_vertices()[3] - trapezium.get_vertices()[2]) * 0.5 + UP * 0.5,   # CD midpoint
            trapezium.get_vertices()[3] + (trapezium.get_vertices()[0] - trapezium.get_vertices()[3]) * 0.5 + RIGHT * 0.8,   # DA midpoint
        ]
        side_labels = VGroup(
            Text(side_lengths[0], color=side_colors[0], stroke_width=0).move_to(side_label_positions[0] + LEFT * 0.8),  # Move "4m" outside AB to the left
            Text(side_lengths[1], color=side_colors[1], stroke_width=0).move_to(side_label_positions[1] + UP * 0.5),  # Move "4m" above BC
            Text(side_lengths[2], color=side_colors[2], stroke_width=0).move_to(side_label_positions[2] + RIGHT * 0.8),
            Text(side_lengths[3], color=side_colors[3], stroke_width=0).move_to(side_label_positions[3] + DOWN * 0.5)
        )
        
        # Calculation steps with reduced font size
        calc_steps = VGroup(
            Text("Perimeter = Sum of all sides", font_size=28).to_edge(LEFT).shift(UP*2),
            Text("= 4m + 4m + 5m + 6m", font_size=28).to_edge(LEFT).shift(UP*1),  # Adjusted for new side lengths
            Text("= 19m", font_size=28).to_edge(LEFT),  # Adjusted for new side lengths
            Text("The perimeter of trapezium is 19m", font_size=28).to_edge(LEFT).shift(DOWN*1)  # Conclusion
        )
        
        # Animation sequence
        self.play(Write(title))
        self.play(Create(trapezium))
        self.play(*[Write(vertex_label) for vertex_label in vertex_labels])
        self.play(*[Write(side_label) for side_label in side_labels])
        self.play(*[Write(step) for step in calc_steps])

        # Keeping the screen for a few seconds
        self.wait(3)

# To run the code, use:
# manim -pql perimeter_of_trapezium.py PerimeterOfTrapezium



    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Surfaces And Boundraies.py"

        
    def SetDeveloperList(self):  
        self.DeveloperList= "Habeeb unissa"

if __name__ == "__main__":
    scene = grade5()
    scene.render()
        