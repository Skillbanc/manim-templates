# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla

from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo


class C5Anim(AbstractAnim):
    
    
    def construct(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("Person","John Doe").setPosition([0,2.5,0])
         p11=cvo.CVO().CreateCVO("Age","36").setPosition([4,2,0])
         p12=cvo.CVO().CreateCVO("In Words","Thirty Six").setPosition([5,-2,0])
         p13=cvo.CVO().CreateCVO("Gender","Male").setPosition([-4,2,0]).setangle(-TAU/4)
         p14=cvo.CVO().CreateCVO("Height","5'9\"").setPosition([-4,0,0]).setangle(-TAU/4)
         p11.cvolist.append(p12)
         
         p10.cvolist.append(p11)
         p10.cvolist.append(p13)
         p10.cvolist.append(p14)
         
         self.construct1(p10,p10)
         

      
if __name__ == "__main__":
    scene = C5Anim()
    scene.render()