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
        #self.constructDataByJSON()
        # self.fadeOut()
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
        p10=cvo.CVO().CreateCVO("spaces and boundries","I")
        p11=cvo.CVO().CreateCVO("perimeter", "total length of the boundry")
        
       
        p10.cvolist.append(p11)
       
       
        self.setNumberOfCirclePositions(2) 

        self.construct1(p10,p10)

   

    def perimeter(self):
       
       
        # Define the side length of the square in cm
        side_length = 3

        # Create a square with the specified side length
        square = Square(side_length=side_length, color=BLUE)

        # Create labels for the vertices
        A = Text("A").next_to(square.get_corner(UL), UP + LEFT)
        B = Text("B").next_to(square.get_corner(UR), UP + RIGHT)
        C = Text("C").next_to(square.get_corner(DR), DOWN + RIGHT)
        D = Text("D").next_to(square.get_corner(DL), DOWN + LEFT)

        # Calculate the perimeter
        perimeter = 4 * side_length

        # Create a text label to display the perimeter
        perimeter_text = Text(f"Perimeter = {perimeter} cm").to_edge(UP)

        # Display the square and labels
        self.play(Create(square))
        self.play(Write(A), Write(B), Write(C), Write(D))

        # Display the perimeter
        self.play(Write(perimeter_text))

        # Hold the final frame for a while
        self.wait(2)

# To run the code, save it in a file named `perimeter_of_square.py` and run:
# manim -pql perimeter_of_square.py PerimeterOfSquare


    def square(self):
    
        p10=cvo.CVO().CreateCVO("calculating perimeter of a square"," length of each side = 3")
        p11=cvo.CVO().CreateCVO("perimeter", "4*side")
        
       
        p10.cvolist.append(p11)
       
       
        self.setNumberOfCirclePositions(2) 

        self.construct1(p10,p10)





    def triangle(self):
        # Define the side length of the triangle in cm
        side_length = 4

        # Create an equilateral triangle with the specified side length
        triangle = RegularPolygon(n=3, color=BLUE)
        triangle.set_height(side_length * 2 / np.sqrt(3))  # Adjust the height to match side length

        # Create labels for the vertices
        A = Text("A").next_to(triangle.get_vertices()[0], UP)
        B = Text("B").next_to(triangle.get_vertices()[1], DOWN + RIGHT)
        C = Text("C").next_to(triangle.get_vertices()[2], DOWN + LEFT)

        # Calculate the perimeter
        perimeter = 3 * side_length

        # Create a text label to display the perimeter
        perimeter_text = Text(f"Perimeter = {perimeter} cm").to_edge(UP)

        # Display the triangle and labels
        self.play(Create(triangle))
        self.play(Write(A), Write(B), Write(C))

        # Display the perimeter
        self.play(Write(perimeter_text))

        # Hold the final frame for a while
        self.wait(2)

# To run the code, save it in a file named `perimeter_of_triangle.py` and run:
# manim -pql perimeter_of_triangle.py PerimeterOfTriangle

    def tri1(self):
    
        p10=cvo.CVO().CreateCVO("calculating perimeter of a triangle"," length of each side = 4cm")
        p11=cvo.CVO().CreateCVO("perimeter", "P=a+b+c")
        
       
        p10.cvolist.append(p11)
       
       
        self.setNumberOfCirclePositions(2) 

        self.construct1(p10,p10)

        self.fadeOutCurrentScene()

    def trapezium(self):
        # Define the side length of the trapezium in cm
        side_length = 5

        # Create points for the trapezium
        A = np.array([-3, 2, 0])
        B = np.array([3, 2, 0])
        C = np.array([2, -2, 0])
        D = np.array([-2, -2, 0])

        # Create the trapezium using the Polygon class
        trapezium = Polygon(A, B, C, D, color=BLUE)

        # Create labels for the vertices
        label_A = Text("A").next_to(A, UP + LEFT)
        label_B = Text("B").next_to(B, UP + RIGHT)
        label_C = Text("C").next_to(C, DOWN + RIGHT)
        label_D = Text("D").next_to(D, DOWN + LEFT)

        # Calculate the perimeter
        perimeter = 4 * side_length

        # Create a text label to display the perimeter
        perimeter_text = Text(f"Perimeter = {perimeter} cm").to_edge(UP)

        # Display the trapezium and labels
        self.play(Create(trapezium))
        self.play(Write(label_A), Write(label_B), Write(label_C), Write(label_D))

        # Display the perimeter
        self.play(Write(perimeter_text))

        # Hold the final frame for a while
        self.wait(2)

# To run the code, save it in a file named `perimeter_of_trapezium.py` and run:
# manim -pql perimeter_of_trapezium.py PerimeterOfTrapezium

    def trap1(self):
    
        p10=cvo.CVO().CreateCVO("calculating perimeter of a trapezium"," length of each side = 5cm")
        p11=cvo.CVO().CreateCVO("perimeter", "P=a+b+c+d")
        
       
        p10.cvolist.append(p11)
       
       
        self.setNumberOfCirclePositions(2) 

        self.construct1(p10,p10)



def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Surfaces And Boundries.py"

        
def SetDeveloperList(self):  
        self.DeveloperList="Habeeb unissa"

if __name__ == "__main__":
    scene = grade5()
    scene.render()
        