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

class coq5Amin(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.constructDataByCVO()
        # self.fadeOut()
        # self.constructDataByJSON()
        # self.fadeOut()
        
    # render using CVO data object
    def constructDataByCVO(self):
        p10=cvo.CVO().CreateCVO("Spcl quadrilateral","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("rhombus", "").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("square", "").setPosition([5,-2,0])
        p13=cvo.CVO().CreateCVO("Unique quadrilateral", "5 independent measurements req").setPosition([-4,3,0]).setangle(-TAU/4)
        p14=cvo.CVO().CreateCVO("construction", "when 2Diag are given").setPosition([-4,1,0]).setangle(-TAU/4)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.construct1(p10,p10)
        self.construct1(p14,p14)
        self.play(Create(CurvedArrow(p11.pos,p14.pos)),Create(CurvedArrow(p12.pos,p14.pos)))
        #self.play()
        

        
      
if __name__ == "__main__":
    scene = coq5Amin()
    scene.render()