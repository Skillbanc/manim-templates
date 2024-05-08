# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License

import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class MovieTitles(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.constructDataByCVO()
        self.fadeOut()
        
    # render using CVO data object
    def constructDataByCVO(self):
        self.positionChoice = [[0,0,0],[-6,-2,0],[6,-2,0],[0,3,0],[-6,2,0],[6,2,0],[0,-3,0]]
        self.angleChoice = [TAU/4,-TAU/4]
            
        p10=cvo.CVO().CreateCVO("Today's Topic","Git Version Control")
        p11=cvo.CVO().CreateCVO("Directed By","Sudhakar Moparthy")
        p12=cvo.CVO().CreateCVO("Production Company","Skillbanc.com, Inc.")
        p13=cvo.CVO().CreateCVO("Animated By","Rohit Vailla")
        p14=cvo.CVO().CreateCVO("Distributed By","Skillbanc YouTube Channel")
        p15=cvo.CVO().CreateCVO("Sponsered By", "Skillbanc.com, Inc.")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p14)
        p12.cvolist.append(p13)
        p12.cvolist.append(p15)
        
        self.construct1(p10,p10)
    
        
        
      
if __name__ == "__main__":
    scene = MovieTitles()
    scene.render()
    