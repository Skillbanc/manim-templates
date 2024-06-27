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

class DivAnim(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.Division()
        self.Example()
        
        self.GithubSourceCodeReference()

        
        # self.fadeOut()
        # self.constructDataByJSON()
        # self.fadeOut()
        
    def SetDeveloperList(self):  
        self.DeveloperList="Hriday Bhushan"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade2Chapter12DivisionOfOneNumberByAnother.py"
    
    # render using CVO data object
    def Division(self):
        title = Text("Division of One Number by Another", font_size=32).to_edge(UP)
        self.play(Create(title))
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Division","")
        p11=cvo.CVO().CreateCVO("Definition","Sharing a collection of items into equal parts")
        p12=cvo.CVO().CreateCVO("Symbol","÷")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Example(self):
       # Set up the scene for 1080p resolution
        self.camera.frame_width = 16
        self.camera.frame_height = 9
        

        # Title
        title = Text("Distribute 18 marbles among 3 people equally.", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        # Texts and positions
        labels = [
            "Total number of marbles",
            "Marbles distributed for the first time",
            "Remaining marbles",
            "Marbles distributed for the second time",
            "Remaining marbles",
            "Marbles distributed for the third time",
            "Remaining marbles",
            "By distributing equally, each one gets",
            "The Division form"
        ]

        equal_signs = [Text("=", font_size=24) for _ in labels]

        # Positioning the labels
        left_column_x = -5
        middle_column_x = 0
        right_column_x = 5
        y_start = 2

        label_positions = [UP * (y_start - i * 0.75) + LEFT * 5 for i in range(len(labels))]
        equal_sign_positions = [UP * (y_start - i * 0.75) for i in range(len(labels))]
        value_positions = [UP * (y_start - i * 0.75) + RIGHT * 5 for i in range(len(labels))]

        labels_mobjects = [Text(label, font_size=24).move_to(pos) for label, pos in zip(labels, label_positions)]

        # Writing labels and equal signs
        for label, equal_sign in zip(labels_mobjects, equal_signs):
            self.play(Write(label))
            equal_sign.move_to(equal_sign_positions[labels_mobjects.index(label)])
            self.play(Write(equal_sign))

        # Initial numbers
        total_marbles = 18
        people = 3
        marbles_each_round = total_marbles // people

        total_text = Text(str(total_marbles), font_size=24).move_to(value_positions[0])
        self.play(Write(total_text))

        # Distribute marbles
        for i in range(3):
            distributed_text = Text(str(marbles_each_round), font_size=24).move_to(value_positions[1 + i*2])
            self.play(Write(distributed_text))

            remaining_marbles = total_marbles - (i + 1) * marbles_each_round
            remaining_text = Text(str(remaining_marbles), font_size=24).move_to(value_positions[2 + i*2])
            self.play(Write(remaining_text))

        # Final results
        result_text = Text(str(marbles_each_round), font_size=24).move_to(value_positions[7])
        self.play(Write(result_text))

        division_text = Text(f"{total_marbles} ÷ {people} = {marbles_each_round}", font_size=24).move_to(value_positions[8])
        self.play(Write(division_text))

        self.wait(2)
        self.fadeOutCurrentScene()

    
    

    
if __name__ == "__main__":
    scene = DivAnim()
    scene.render()