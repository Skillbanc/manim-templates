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


class S3ServiceAnim(AbstractAnim):
    
    def construct(self):
        self.RenderS3Part1()
        # self.RenderS3FeaturesPart2()
    
    def RenderS3Part1(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("Amazon S3 Objects","*").setPosition([0,2.5,0])
         p11=cvo.CVO().CreateCVO("Key","*").setPosition([4,2,0])
         p12=cvo.CVO().CreateCVO("Version ID","*").setPosition([5,-2,0])
         p13=cvo.CVO().CreateCVO("Tags","*").setPosition([-4,3,0]).setangle(-TAU/4)
         p14=cvo.CVO().CreateCVO("Metadata","*").setPosition([-4,1,0]).setangle(-TAU/4)
         p15=cvo.CVO().CreateCVO("Sub Resources","*").setPosition([-4,-1,0]).setangle(-TAU/4)
         p16=cvo.CVO().CreateCVO("Value","*").setPosition([-4,-3,0]).setangle(-TAU/4)
         p10.cvolist.append(p12)
         
         p10.cvolist.append(p11)
         p10.cvolist.append(p13)
         p10.cvolist.append(p14)
         p10.cvolist.append(p15)
         p10.cvolist.append(p16)
         
         self.construct1(p10,p10)
         

    def RenderS3FeaturesPart2(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("Amazon Services","Amazon S3").setPosition([0,2.5,0])
         p11=cvo.CVO().CreateCVO("Features","S3").setPosition([4,2,0])
         p12=cvo.CVO().CreateCVO("Scalability","*").setPosition([5,-2,0])
         p13=cvo.CVO().CreateCVO("Cost Effective","*").setPosition([-4,3,0]).setangle(-TAU/4)
         p14=cvo.CVO().CreateCVO("Security","*").setPosition([-4,1,0]).setangle(-TAU/4)
         p15=cvo.CVO().CreateCVO("Availability","*").setPosition([-4,-1,0]).setangle(-TAU/4)
         p16=cvo.CVO().CreateCVO("Flexible Storage","*").setPosition([-4,-3,0]).setangle(-TAU/4)
         p17=cvo.CVO().CreateCVO("Data Management","*").setPosition([-2,-3,0]).setangle(-TAU/4)
         p11.cvolist.append(p12)

         p16.cvolist.append(p17)
         

         p10.cvolist.append(p11)
         p11.cvolist.append(p13)
         p11.cvolist.append(p14)
         p11.cvolist.append(p15)
         p11.cvolist.append(p17)
         
         self.construct1(p10,p10)

      
if __name__ == "__main__":
    scene = S3ServiceAnim()
    scene.render()