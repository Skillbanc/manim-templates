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
        self.Example1()
        self.Example2()
        
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

    def Example1(self):

        # Title
        title = Text("Distribute 18 marbles among 3 people equally.", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        # Texts and positions
        text1=Tex("Total number of marbles = 18",font_size=30).next_to(title, DOWN*2)
        self.play(Write(text1))
        text2=Tex("Marbles distributed for the first time = 6",font_size=30).next_to(text1, DOWN*1.5)
        self.play(Write(text2))
        text3=Tex("Remaining marbles = 12",font_size=30).next_to(text2, DOWN*1.5)
        self.play(Write(text3))
        text4=Tex("Marbles distributed for the second time = 6",font_size=30).next_to(text3, DOWN*1.5)
        self.play(Write(text4))
        text5=Tex("Remaining marbles = 6",font_size=30).next_to(text4, DOWN*1.5)
        self.play(Write(text5))
        text6=Tex("Marbles distributed for the third time = 6",font_size=30).next_to(text5, DOWN*1.5)
        self.play(Write(text6))
        text7=Tex("Remaining marbles = 0",font_size=30).next_to(text6, DOWN*1.5)
        self.play(Write(text7))
        text8=Tex("By distributing equally, each one gets 6 marbles",font_size=30).next_to(text7, DOWN*1.5)
        self.play(Write(text8))
        text9=Tex("The Division form = 18/3",font_size=30).next_to(text8, DOWN*1.5)
        self.play(Write(text9))

        self.wait(2)
        self.fadeOutCurrentScene()

    def Example2(self):
        # Title
        title1 = Text("3 students can sit on a bench.", font_size=36)
        title2 = Text("How many benches are required for 21 students", font_size=36)
        title1.to_edge(UP)
        title2.next_to(title1, DOWN)
        self.play(Write(title1))
        self.play(Write(title2))

        # Texts and positions
        text1=Tex("Total number of students = 21",font_size=32).next_to(title2, DOWN*2)
        self.play(Write(text1))
        text2=Tex("Each bench can sit = 3",font_size=32).next_to(text1, DOWN*1.5)
        self.play(Write(text2))
        text3=Tex("Number of benches needed = 21/3",font_size=32).next_to(text2, DOWN*1.5)
        self.play(Write(text3))
        text4=Tex("Required Benches = 7",font_size=32).next_to(text3, DOWN*1.5)
        self.play(Write(text4))

        self.wait(2)
        self.fadeOutCurrentScene()
    
    

    
if __name__ == "__main__":
    scene = DivAnim()
    scene.render()