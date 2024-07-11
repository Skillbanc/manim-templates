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
        #self.RenderSkillbancLogo()
        #self.Division()
        self.Example()
        
        #self.GithubSourceCodeReference()

        
        # self.fadeOut()
        # self.constructDataByJSON()
        # self.fadeOut()
        
    def SetDeveloperList(self):  
        self.DeveloperList="Hriday Bhushan"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Chap12Class2.py"
    
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

        # Title
        title = Text("Distribute 18 marbles among 3 people equally.", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))

        # Texts and positions
        symbol = Text("")
        text1=Tex("Total number of marbles = 18").next_to(title, DOWN*2)
        self.play(Write(text1))
        text2=Tex("Marbles distributed for the first time = 6").next_to(text1, DOWN*1.5)
        self.play(Write(text2))
        text3=Tex("Remaining marbles = 12").next_to(text2, DOWN*1.5)
        self.play(Write(text3))
        text4=Tex("Marbles distributed for the second time = 6").next_to(text3, DOWN*1.5)
        self.play(Write(text4))
        text5=Tex("Remaining marbles = 6").next_to(text4, DOWN*1.5)
        self.play(Write(text5))
        text6=Tex("Marbles distributed for the third time = 6").next_to(text5, DOWN*1.5)
        self.play(Write(text6))
        text7=Tex("Remaining marbles = 0").next_to(text6, DOWN*1.5)
        self.play(Write(text7))
        text8=Tex("By distributing equally, each one gets 6 marbles").next_to(text7, DOWN*1.5)
        self.play(Write(text8))
        text9=Tex("The Division form = 18/3").next_to(text8, DOWN*1.5)
        self.play(Write(text9))
        #self.play(FadeIn(symbol))

        

        self.wait(2)
        self.fadeOutCurrentScene()

    
    

    
if __name__ == "__main__":
    scene = DivAnim()
    scene.render()