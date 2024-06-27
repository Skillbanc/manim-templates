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

class PatternAnim(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.Pattern()
        self.Example()
        self.Example2()
        
        self.GithubSourceCodeReference()

        
        # self.fadeOut()
        # self.constructDataByJSON()
        # self.fadeOut()
        
    def SetDeveloperList(self):  
        self.DeveloperList="Hriday Bhushan"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade3Chap12Patterns.py"
    
    def Pattern(self):
        title = Text("Patterns", font_size=36).to_edge(UP)
        self.play(Create(title))
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Patterns","")
        p11=cvo.CVO().CreateCVO("Definition","Arrangement of lines, shapes, colours, etc. as a design")
        
        p10.setcircleradius(1.2)
        p11.setcircleradius(1.2)
        p10.cvolist.append(p11)
        
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Example(self): 
        # Create a rectangle
        rect = Rectangle(height=4, width=3)
        
        # Title
        title = Text("Symmetric Patterns").to_edge(UP)
        self.play(Write(title))
        
        # Display the original rectangle
        self.play(Create(rect))
        self.play(FadeOut(title))

        title1 = Text("Vertical Symmetry").to_edge(UP)
        self.play(Write(title1))
        # Vertical symmetry
        vertical_line = Line(start=rect.get_top(), end=rect.get_bottom())
        self.play(Create(vertical_line))
        self.wait(1)
        self.play(FadeOut(vertical_line))
        
        self.play(FadeOut(title1))

        title2 = Text("Horizontal Symmetry").to_edge(UP)
        self.play(Write(title2))
        # Horizontal symmetry
        horizontal_line = Line(start=rect.get_left(), end=rect.get_right())
        self.play(Create(horizontal_line))
        self.wait(1)
        self.play(FadeOut(horizontal_line))
        
        self.play(FadeOut(title2))

        title3 = Text("Diagonal Symmetry").to_edge(UP)
        self.play(Write(title3))
        # Diagonal symmetry (top-left to bottom-right)
        diagonal_line1 = Line(start=rect.get_corner(UL), end=rect.get_corner(DR))
        self.play(Create(diagonal_line1))
        self.wait(1)
        self.play(FadeOut(diagonal_line1))
        
        # Diagonal symmetry (top-right to bottom-left)
        diagonal_line2 = Line(start=rect.get_corner(UR), end=rect.get_corner(DL))
        self.play(Create(diagonal_line2))
        self.wait(1)
        self.play(FadeOut(diagonal_line2))
        
        self.wait(2)
        self.fadeOutCurrentScene()

    def Example2(self):
        # Title
        title = Text("Pattern Animation").to_edge(UP)
        self.play(Write(title))
        
        # Define pattern rows
        patterns = [
            [Text("A"), Text("B"), Text("A"), Text("B")],
            [Circle(), Square(), Circle(), Square()],
            [Triangle().rotate(PI), Triangle(), Triangle().rotate(PI), Triangle()],
            [Arrow(LEFT), Arrow(RIGHT), Arrow(LEFT), Arrow(RIGHT)]
        ]
        
        # Define spacing
        row_spacing = 1.5  # Increased row spacing
        initial_y_position = UP * 2  # Start position just below the title
        
        # Add each pattern row to the scene
        for i, pattern in enumerate(patterns):
            pattern_group = VGroup(*[self.create_pattern_item(item) for item in pattern])
            pattern_group.arrange(RIGHT, buff=1).shift(initial_y_position + DOWN * i * row_spacing)
            self.play(Create(pattern_group))
            self.wait(1)
        
        self.wait(2)
        self.fadeOutCurrentScene()
    
    def create_pattern_item(self, item):
        if isinstance(item, Text):
            return item
        elif isinstance(item, VMobject):
            item.set_height(1)
            return item
        else:
            raise ValueError("Unsupported pattern item type")
    

    
if __name__ == "__main__":
    scene = PatternAnim()
    scene.render()