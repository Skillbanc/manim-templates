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
         p10=cvo.CVO().CreateCVO("Integration of AWS Redshift with AWS Ecosystem",".").setPosition([0,2.5,0])
         p11=cvo.CVO().CreateCVO("Amazon S3",".").setPosition([4,2,0])
         p12=cvo.CVO().CreateCVO("AWS Glue",".").setPosition([5,-2,0])
         p13=cvo.CVO().CreateCVO("Amazon Quicksight",".").setPosition([-4,2,0]).setangle(-TAU/4)
         p14=cvo.CVO().CreateCVO("AWS Data Pipeline and AWS Batch",".").setPosition([-4,0,0]).setangle(-TAU/4)
         
         
         p10.cvolist.append(p11)
         p10.cvolist.append(p12)
         p10.cvolist.append(p13)
         p10.cvolist.append(p14)
         
         self.construct1(p10,p10)
         

      
if __name__ == "__main__":
    scene = C5Anim()
    scene.render()