# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy

from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo


class mean(AbstractAnim):
    
    
    def construct(self):
         self.constructDataByCVO()
         self.fadeOutCurrentScene()
    def constructDataByCVO(self):
        self.isRandom=False
         
        p1=cvo.CVO().CreateCVO("Arithmetic Mean","sum of observations divided by no.of observations").setPosition([-3,0,0])
        p2=cvo.CVO().CreateCVO("sum of observations","x_1+x_2+x_3+x_4........+x_n").setPosition([0,2,0])
        p3=cvo.CVO().CreateCVO("no.of observations","N(1 to n)").setPosition([0,-2,0])
        p4=cvo.CVO().CreateCVO("Mean","(x_1+x_2+x_3+x_4+........+x_n)/N").setPosition([5,0,0])
          
        p1.cvolist.append(p2)
         
        p1.cvolist.append(p3)
        p2.SetIsMathText(True)
        p4.SetIsMathText(True)
        self.construct1(p1,p1)
        
        self.construct1(p4,p4)
        self.play(Create(CurvedArrow(p2.pos,p4.pos)),Create(CurvedArrow(p3.pos,p4.pos)))
         
             
if __name__ == "__main__":
    scene = mean()
    scene.render()