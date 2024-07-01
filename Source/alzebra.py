# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla

from manim import *
from manim.constants import TAU
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class Alzebra(AbstractAnim):
    
    
    def construct(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
        
        self.setNumberOfCirclePositions(10)
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("algebra expression","5x+6y+3")
        p11=cvo.CVO().CreateCVO("like terms","3x+2x+3")
        p12=cvo.CVO().CreateCVO("unlike terms","2y-3x-3")
        p13=cvo.CVO().CreateCVO("addition","3x+7x=10x")
        p14=cvo.CVO().CreateCVO("substraction","7y-9y=-2y")
        p15=cvo.CVO().CreateCVO("multiplication","5x*4y=20xy")
        p16=cvo.CVO().CreateCVO("identities","a and b")
        p17=cvo.CVO().CreateCVO("(a+b)^2","(a^2)+(b^2)+(2ab)")
        p17.SetIsMathText(True)
        p18=cvo.CVO().CreateCVO("(a-b)^2","(a^2)+(b^2)-(2ab)")
        p18.SetIsMathText(True)
        p19=cvo.CVO().CreateCVO("(a+b)(a-b)","(a^2)-(b^2)")
        p19.SetIsMathText(True)
         
        p16.cvolist.append(p17)
        p16.cvolist.append(p18)
        p16.cvolist.append(p19)
         
         
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        p10.cvolist.append(p16)
        
        
        self.construct1(p10,p10)
        
         

      
if __name__ == "__main__":
    scene = Alzebra()
    scene.render()
    
    