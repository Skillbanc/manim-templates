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

class HappyCelebrationDay(AbstractAnim):
    
    def construct(self):
         p10=cvo.CVO().CreateCVO("Celebration Day","International Labor Day")#.setPosition([0,0,0])
         
         p11=cvo.CVO().CreateCVO("Date","May 1st 2024")
         # p12=cvo.CVO().CreateCVO("In Words","Thirty Six").setPosition([-2,0,0])
         # p11.cvolist.append(p12)
         
         p10.cvolist.append(p11)
         
         self.construct1(p10,p10)
      
if __name__ == "__main__":
    scene = HappyCelebrationDay()
    scene.render()
    