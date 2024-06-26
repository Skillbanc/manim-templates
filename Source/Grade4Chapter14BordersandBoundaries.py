import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class FactorsAnim(AbstractAnim):

    
    def construct(self):
        self.RenderSkillbancLogo()
        self.Borders()
        self.Border1()
        self.GithubSourceCodeReference()
    
    def Borders(self):

        p10=cvo.CVO().CreateCVO("Borders and Boundaries", "").setPosition([-3,0,0]).setangle(-TAU/6)
        p11=cvo.CVO().CreateCVO("Perimeter", "").setPosition([-1,0,0]).setangle(-TAU/6)
        p12=cvo.CVO().CreateCVO("Definition", "Total length of the shape or and area").setPosition([2,2,0]).setangle(-TAU/6)
        
       
        
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)

        p11.setcircleradius(1.5)
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
        rect = Polygon(A, B, C, D, color=BLUE)
        self.play(Create(rect))
        
        # Label the points
        point_labels = ["A", "B", "C", "D"]
        points = [A, B, C, D]
        for i, point in enumerate(points):
            label = Text(point_labels[i]).scale(0.7).next_to(point, direction=UR)
            self.play(Write(label))
        
        # Highlight the sides with lengths
        side_labels = [
            ("8 cm", (A+B)/2 + DOWN * 0.3),
            ("3 cm", (B+C)/2 + RIGHT * 0.3),
            ("8 cm", (C+D)/2 + UP * 0.3),
            ("3 cm", (D+A)/2 + LEFT * 0.3)
        ]
        
        for text, position in side_labels:
            label = Text(text).scale(0.7).move_to(position)
            self.play(Write(label))
        
        # Adding the lengths
        add_lengths = Text("8 cm + 3 cm + 8 cm + 3 cm").scale(0.5).next_to(rect, DOWN*3)
        self.play(Write(add_lengths))
        
        # Show the perimeter result
        perimeter_result = Text("Perimeter = 22 cm").scale(0.6).next_to(add_lengths, DOWN)
        self.play(Write(perimeter_result))
        
        self.wait(2)
        self.fadeOutCurrentScene()
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade4Chapter14BordersandBoundaries.py"

    def SetDeveloperList(self):  
        self.DeveloperList="Lagichetty Kushal"
    
if __name__ == "__main__":
    scene = FactorsAnim()
    scene.render()