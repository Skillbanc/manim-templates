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

class C2Anim(AbstractAnim):
    
    def construct(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("Person","John Doe")
         
         p11=cvo.CVO().CreateCVO("Age","36")
                 
         p10.cvolist.append(p11)
         
         self.construct1(p10,p10)
  
            
if __name__ == "__main__":
    scene = C2Anim()
    scene.render()