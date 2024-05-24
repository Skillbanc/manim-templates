# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy

from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo


class C3Anim(AbstractAnim):
    
    
    def construct(self):
         self.isFadeOutAtTheEndOfThisScene = True 
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         
         p10=cvo.CVO().CreateCVO("Person","John Doe")#.setPosition([0,2.5,0])
         
         p11=cvo.CVO().CreateCVO("Age","36")#.setPosition([2,0,0])
         p12=cvo.CVO().CreateCVO("In Words","Thirty Six")#.setPosition([-2,0,0])
         p11.cvolist.append(p12)
         
         p10.cvolist.append(p11)
         
         self.setNumberOfCirclePositions(3)
         self.construct1(p10,p10)
         

      
if __name__ == "__main__":
    scene = C3Anim()
    scene.render()