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

class TensAnim(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.Example()
        
        self.GithubSourceCodeReference()

        
        # self.fadeOut()
        # self.constructDataByJSON()
        # self.fadeOut()
        
    def SetDeveloperList(self):  
        self.DeveloperList="Hriday Bhushan"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade1Chap12TensAddition.py"
    
    # render using CVO data object
    def Introduction(self):
        title = Text("Introduction of Tens", font_size=36).to_edge(UP)
        self.play(Create(title))
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Tens","")
        p11=cvo.CVO().CreateCVO("Definition","Counting in steps of 10 for each unit")
        
        p10.setcircleradius(1.2)
        p11.setcircleradius(1.2)
        p10.cvolist.append(p11)
        
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Example(self):
         # Title
        title = Text("Count in tens. Write the numbers in the boxes.", font_size=24)
        title.to_edge(UP)
        self.play(Write(title))
        
        # List of numbers and their positions
        numbers = [10 * i for i in range(1, 6)]
        number_texts = [Text(str(num), font_size=24) for num in numbers]
        positions = [2*UP + i*DOWN for i in range(len(numbers))]

        # Drawing the tens and numbers
        for i, (num_text, pos) in enumerate(zip(number_texts, positions)):
            tens_group = VGroup()
            for j in range(i + 1):
                ten_circle = Circle(radius=0.2, fill_color=BLUE, fill_opacity=1)
                ten_circle.move_to(pos + LEFT * 3 + RIGHT * j * 0.7)
                tens_group.add(ten_circle)
            
            # Display tens
            self.play(FadeIn(tens_group))
            self.play(Write(num_text.move_to(pos + RIGHT * 3)))
            
            # Draw the box around the number
            box = SurroundingRectangle(num_text, buff=0.1)
            self.play(Create(box))
            self.wait(0.5)

        self.wait(2)
        self.fadeOutCurrentScene()

    
    

    
if __name__ == "__main__":
    scene = TensAnim()
    scene.render()