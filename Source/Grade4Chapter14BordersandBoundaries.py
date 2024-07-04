import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class BordersAnim(AbstractAnim):

    
    def construct(self):
        self.RenderSkillbancLogo()
        self.Borders()
        self.Border1()
        self.Example()
        self.GithubSourceCodeReference()
    
    def Borders(self):
        
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Borders and Boundaries", "").setPosition([-4,0,0])
        p11=cvo.CVO().CreateCVO("Perimeter", "").setPosition([-1,0,0]).setangle(-TAU/4)
        p12=cvo.CVO().CreateCVO("Definition", "Total length of the shape or and area").setPosition([2,1,0]).setangle(-TAU/4)
        
       
        
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)

        
        p12.setcircleradius(1.5)

        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Border1(self):

        # Title
        title = Text("Finding the Perimeter of a Fence").scale(0.9).to_edge(UP)
        self.play(Write(title))
        
        # Define points of the rectangle
        A = np.array([-4, -1, 0])
        B = np.array([4, -1, 0])
        C = np.array([4, 2, 0])
        D = np.array([-4, 2, 0])
        
        # Draw the rectangle
        rect = Polygon(A, B, C, D, color=BLUE, fill_color=GREEN, fill_opacity=0.5)
        self.play(Create(rect))
        
        point_labels = [
            ("A", A, DOWN + LEFT),
            ("B", B, DOWN + RIGHT),
            ("C", C, UP + RIGHT),
            ("D", D, UP + LEFT)
        ]
        
        for text, point, direction in point_labels:
            label = Text(text).scale(0.7).next_to(point, direction)
            self.play(Write(label))
        
        
        # Highlight the sides with lengths
        side_labels = [
            ("8 cm", (A+B)/2 + DOWN * 0.3),
            ("3 cm", (B+C)/2 + RIGHT * 0.6),
            ("8 cm", (C+D)/2 + UP * 0.3),
            ("3 cm", (D+A)/2 + LEFT * 0.6)
        ]
        
        for text, position in side_labels:
            label = Text(text).scale(0.7).move_to(position)
            self.play(Write(label))
        
        # Adding the lengths
        add_lengths = Text("8 cm + 3 cm + 8 cm + 3 cm = 22 cm").scale(0.5).next_to(rect, DOWN*4)
        self.play(Write(add_lengths))
        
        # Show the perimeter result
        perimeter_result = Text("Perimeter = 22 cm").scale(0.6).next_to(add_lengths, DOWN)
        self.play(Write(perimeter_result))
        
        self.wait(2)
        self.fadeOutCurrentScene()

    def Example(self):

        title = Text("Finding the Perimeter of a Garden",font_size=30,color=YELLOW).to_edge(UP)
        self.play(Write(title))
        
        # Subtitle
        title1 = Text("Ravi takes 3 rounds of this garden, every day in the morning. What is the total distance he walks each day?",font_size=28).scale(0.7).next_to(title, DOWN*2)
        self.play(Write(title1))
        
        # Create points for the trapezoid
        A = [-5, 1, 0]
        B = [5, 1, 0]
        C = [3.5, -1, 0]
        D = [-3.5, -1, 0]
        
        # Create the trapezoid
        trapezoid = Polygon(
            A, B, C, D,
            fill_color=GREEN, fill_opacity=0.5,
            stroke_color=WHITE
        ).scale(0.7).next_to(title1,DOWN*4)
        
        # Add the trapezoid to the scene
        self.play(Create(trapezoid))
        
        # Add labels for the sides
        labels = [
            Text("100 m").scale(0.5).next_to(trapezoid.get_top(), UP),
            Text("25 m").scale(0.5).next_to(trapezoid.get_right(), RIGHT),
            Text("70 m").scale(0.5).next_to(trapezoid.get_bottom(), DOWN),
            Text("25 m").scale(0.5).next_to(trapezoid.get_left(), LEFT)
        ]
        
        for label in labels:
            self.play(Write(label))

        # Display the total distance walked
        add_lengths = Text("Perimeter of Garden = 100 m + 25 m + 70 m + 25 m = 220 m",font_size= 26,color = GREEN).scale(0.7).next_to(trapezoid, DOWN*4)
        self.play(Write(add_lengths))
        length = Text("Ravi takes 3 rounds of the garden = 3 x 220m",font_size= 26,color = GREEN).scale(0.7).next_to(add_lengths, DOWN)
        self.play(Write(length))
        total_distance = Text("Total Distance = 660 m",font_size= 26,color = GREEN).scale(0.7).next_to(length,DOWN)
        self.play(Write(total_distance))

        self.fadeOutCurrentScene()

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade4Chapter14BordersandBoundaries.py"

    def SetDeveloperList(self):  
        self.DeveloperList="Lagichetty Kushal"
    
if __name__ == "__main__":
    scene = BordersAnim()
    scene.render()