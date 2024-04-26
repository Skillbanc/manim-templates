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


class C11Anim(AbstractAnim):
    
    
    def construct(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("Person","John Doe").setPosition([0,2.5,0])
         p11=cvo.CVO().CreateCVO("Age","36").setPosition([4,2,0])
         p12=cvo.CVO().CreateCVO("In Words","Thirty Six").setPosition([5,-2,0])
         p13=cvo.CVO().CreateCVO("Gender","Male").setPosition([-4,3,0]).setangle(-TAU/4)
         p14=cvo.CVO().CreateCVO("Height","5'9\"").setPosition([-4,1,0]).setangle(-TAU/4)
         p15=cvo.CVO().CreateCVO("Weight","155lb").setPosition([-4,-1,0]).setangle(-TAU/4)
         p16=cvo.CVO().CreateCVO("DOB","04/02/1988").setPosition([-4,-3,0]).setangle(-TAU/4)
         p17=cvo.CVO().CreateCVO("Date","04").setPosition([-2,-3,0])
         p18=cvo.CVO().CreateCVO("Year","1988").setPosition([-6,-3,0]).setangle(-TAU/4)
         p19=cvo.CVO().CreateCVO("Citizenship","USA").setPosition([0,-3,0]).setangle(-TAU/4)
         p20=cvo.CVO().CreateCVO("Phone no.","+1 555 555 555").setPosition([2,-3,0]).setangle(-TAU/4)
         p11.cvolist.append(p12)

         p16.cvolist.append(p17)
         p16.cvolist.append(p18)
         

         p10.cvolist.append(p11)
         p10.cvolist.append(p13)
         p10.cvolist.append(p14)
         p10.cvolist.append(p15)
         p10.cvolist.append(p16)
         p10.cvolist.append(p19)
         p10.cvolist.append(p20)
         
         self.construct1(p10,p10)
         

      
if __name__ == "__main__":
    scene = C11Anim()
    scene.render()