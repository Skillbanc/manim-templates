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


class C7Anim(AbstractAnim):
    
    
    def construct(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("Security in AWS Redshift","*").setPosition([0,2.5,0])
         p11=cvo.CVO().CreateCVO("Network Isolation",".").setPosition([4,2,0])
         p12=cvo.CVO().CreateCVO("Encryption",".").setPosition([5,-2,0])
         p13=cvo.CVO().CreateCVO("Access Control",".").setPosition([-4,3,0]).setangle(-TAU/4)
         p14=cvo.CVO().CreateCVO("Monitoring and Auditing",".").setPosition([-4,1,0]).setangle(-TAU/4)
         p15=cvo.CVO().CreateCVO("Compliance and Certification",".").setPosition([-4,-1,0]).setangle(-TAU/4)
         #p16=cvo.CVO().CreateCVO("",".").setPosition([-4,-3,0]).setangle(-TAU/4)
         p11.cvolist.append(p12)
         
         p10.cvolist.append(p11)
         p12.cvolist.append(p13)
         p13.cvolist.append(p14)
         p14.cvolist.append(p15)
         #p10.cvolist.append(p16)
         
         self.construct1(p10,p10)
         

      
if __name__ == "__main__":
    scene = C7Anim()
    scene.render()