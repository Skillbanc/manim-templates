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

class TrigAnim(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.LoS()
        self.AoE()
        self.AoD()
        self.Requirements()
        # self.fadeOut()
        # self.constructDataByJSON()
        # self.fadeOut()
        
    # render using CVO data object
    def LoS(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Line of Sight","")
        p11=cvo.CVO().CreateCVO("Definition","a line from an observer's eye to a distant point").setPosition([2,0,0])
        
        p10.setcircleradius(1.5)
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
        Example= ImageMobject("/Users/hridaybhushan/Desktop/Screenshot 2024-06-11 at 17.27.53.png")
        Example.scale(1.7)
        self.add(Example)
        self.fadeOutCurrentScene()
    
    def AoE(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Angle of Elevation", "")
        p11=cvo.CVO().CreateCVO("Definition", " line of sight is above the horizontal line and angle between the line of sight and the horizontal line")
        p10.setcircleradius(1.5)
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
        Example= ImageMobject("/Users/hridaybhushan/Desktop/Screenshot 2024-06-11 at 19.14.16.png")
        Example.scale(1)
        self.add(Example)
        self.fadeOutCurrentScene()

    def AoD(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Angle of Depression", "")
        p11=cvo.CVO().CreateCVO("Definition", "Angle between the line of sight and the horizontal line")
        p10.cvolist.append(p11)
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
        Example= ImageMobject("/Users/hridaybhushan/Desktop/Screenshot 2024-06-11 at 19.14.11.png")
        Example.scale(1)
        self.add(Example)
        self.fadeOutCurrentScene()

    def Requirements(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Conditions for Diagram", "")
        p12=cvo.CVO().CreateCVO("Condition", "All objects should be considered linear")
        p11=cvo.CVO().CreateCVO("Condition", "Angle of elevation or depression is with reference to horizontal line").setPosition([2,-2,0])
        p13=cvo.CVO().CreateCVO("Condition", "Height of observer is neglected if not given")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p11.setcircleradius(1.5)
        p12.setcircleradius(1.5)
        p13.setcircleradius(1.5)
        self.setNumberOfCirclePositions(4)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
    
    
if __name__ == "__main__":
    scene = TrigAnim()
    scene.render()