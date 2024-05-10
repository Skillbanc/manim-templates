# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License

import json
from manim import *

from AbstractAnim import AbstractAnim

import cvo

class MovieTitles(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderMovieTitles()
        
    # render using CVO data object
    def RenderMovieTitles(self):
        self.positionChoice = [[0,0,0],[-6,-2,0],[6,-2,0],[0,3,0],[-6,2,0],[6,2,0],[0,-3,0]]
        self.angleChoice = [TAU/4,-TAU/4]
        count = 0
        p10=cvo.CVO().CreateCVO("Today's Topic","Git Version Control")
        count += 1
        
        p11=cvo.CVO().CreateCVO("Directed By","Sudhakar Moparthy")
        count += 1
        p10.cvolist.append(p11)
        
        p12=cvo.CVO().CreateCVO("Produced By","Skillbanc.com, Inc.")
        count += 1
        p10.cvolist.append(p12)
        
        p13=cvo.CVO().CreateCVO("Animated By","Rohit Vailla")
        count += 1
        p10.cvolist.append(p13)
        
        p14=cvo.CVO().CreateCVO("Distributed By","Skillbanc YouTube Channel")
        count += 1
        p10.cvolist.append(p14)
        
        p15=cvo.CVO().CreateCVO("Sponsered By", "Skillbanc.com, Inc.")
        count += 1
        p10.cvolist.append(p15)
        

        self.construct1(p10,p10)
    
if __name__ == "__main__":
    scene = MovieTitles()
    scene.render()
    