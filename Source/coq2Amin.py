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

class coq2Amin(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.constructDataByCVO()
        # self.fadeOut()
        # self.constructDataByJSON()
        # self.fadeOut()
        
    # render using CVO data object
    def constructDataByCVO(self):
        p10=cvo.CVO().CreateCVO("Types of quadrilateral","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Trapezium", " one pair of opp S are llel").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("parallelogram", "two pair opp S are equal and llel").setPosition([5,-2,0])
        p13=cvo.CVO().CreateCVO("Rhombus", "ADJs are equal").setPosition([-4,3,0]).setangle(-TAU/4)
        p14=cvo.CVO().CreateCVO("Kite", "2 pairs of AdjS equal  and diagonals intersect at 90 deg").setPosition([-4,1,0]).setangle(-TAU/4)
        p15=cvo.CVO().CreateCVO("Rectangle", "parallelogram with 4 right angles").setPosition([-4,-1,0]).setangle(-TAU/4)
        p16=cvo.CVO().CreateCVO("Square", "rhombus with 4 right angles").setPosition([-4,-3,0]).setangle(-TAU/4)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        p10.cvolist.append(p16)
        self.construct1(p10,p10)


        
      
if __name__ == "__main__":
    scene = coq2Amin()
    scene.render()