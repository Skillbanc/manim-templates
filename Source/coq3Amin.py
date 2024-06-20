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

class coq3Amin(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.constructDataByCVO()
        # self.fadeOut()
        # self.constructDataByJSON()
        # self.fadeOut()
        
    # render using CVO data object
    def constructDataByCVO(self):
        p10=cvo.CVO().CreateCVO("Construction quadrilateral","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Materials needed", "Rulern\n,Pencil\n,Protractor\n,Compass\n").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("Step:1", "draw rough sketch").setPosition([5,-2,0])
        p13=cvo.CVO().CreateCVO("Step:2", "Analyse the fig and use spcl properties of it").setPosition([-4,3,0]).setangle(-TAU/4)
        p14=cvo.CVO().CreateCVO("Step:3", "use compass and protractor to obtain req fig").setPosition([-4,1,0]).setangle(-TAU/4)
        p15=cvo.CVO().CreateCVO("Step:4", "Join the pt's to complete").setPosition([-4,-1,0]).setangle(-TAU/4)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        self.construct1(p10,p10)


        
      
if __name__ == "__main__":
    scene = coq3Amin()
    scene.render()