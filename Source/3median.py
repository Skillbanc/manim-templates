# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy

from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo


class median(AbstractAnim):
    
    
    def construct(self):
        self.constructDataByCVO()
        self.fadeOutCurrentScene()
    def constructDataByCVO(self):
        self.isRandom=False
         
        p1=cvo.CVO().CreateCVO("Median","").setPosition([0,2,0])
        p2=cvo.CVO().CreateCVO("case 1: odd no.of observations(n)","median=((n+1)/2)th ").setPosition([-3,0,0])
        p3=cvo.CVO().CreateCVO("case 2: even no.of observations(n)","((n/2)th +((n+1)/2)th )/2 value").setPosition([3,0,0])
          
        p1.cvolist.append(p2)
        p1.cvolist.append(p3)
         
        p2.SetIsMathText(True)
        p3.SetIsMathText(True)
         
        self.construct1(p1,p1)
            
if __name__ == "__main__":
    scene = median()
    scene.render()