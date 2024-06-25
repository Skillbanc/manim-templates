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

class coq4Amin(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.constructDataByCVO()
        # self.fadeOut()
        # self.constructDataByJSON()
        # self.fadeOut()
        
    # render using CVO data object
    def constructDataByCVO(self):
        p10=cvo.CVO().CreateCVO("Quadrilateral Meaurements","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("4S AND 1A", "S.S.S.S.A").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("4S AND 1Diag", "S.S.S.S.Diag").setPosition([5,-2,0])
        p13=cvo.CVO().CreateCVO("3S AND 2Diag", "S.S.S.Diag.Diag").setPosition([-4,3,0]).setangle(-TAU/4)
        p14=cvo.CVO().CreateCVO("2AdjS AND 3A", "S.A.S.A.A").setPosition([-4,1,0]).setangle(-TAU/4)
        p15=cvo.CVO().CreateCVO("3S AND 2A", "S.A.S.A.S").setPosition([-4,-1,0]).setangle(-TAU/4)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        self.construct1(p10,p10)


        
      
if __name__ == "__main__":
    scene = coq4Amin()
    scene.render()