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

class coq1Amin(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.constructDataByCVO()
        # self.fadeOut()
        # self.constructDataByJSON()
        # self.fadeOut()
        
    # render using CVO data object
    def constructDataByCVO(self):
        p10=cvo.CVO().CreateCVO("Quadrilaterals","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("defination", " It consist of 4S,4A").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("ETI", "Latin words “quadri”=“four” and “latus”=“side”").setPosition([0,-2.5,0]).setangle(-TAU/3)
        p13=cvo.CVO().CreateCVO("keypoints", "Vertices\nSides\nDiagonals\nInterior Angles\n").setPosition([-4,3,0]).setangle(-TAU/4)

        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.construct1(p10,p10)


        
      
if __name__ == "__main__":
    scene = coq1Amin()
    scene.render()