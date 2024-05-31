# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla

import json
from os import remove
from manim import *
from scipy.spatial import transform
from numpy import size
from AbstractAnim import AbstractAnim

import cvo


class Redshiftanim8(AbstractAnim):


     # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.Redshiftanim1()
        self.wait(2)
        self.clear()
        self.Redshiftanim2()
    
    
    def Redshiftanim1(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
        p10=cvo.CVO().CreateCVO("AWS Redshift Features","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Faster Performance","").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("Easy Integration","").setPosition([5,-2,0])
        p13=cvo.CVO().CreateCVO("Cost-Effective","").setPosition([-4,2,0]).setangle(-TAU/4)
        p14=cvo.CVO().CreateCVO("Safe and Secure","").setPosition([-5,-2,0]).setangle(-TAU/4)
        p10.cvolist.append(p12)
         
        p10.cvolist.append(p11)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
         
        self.construct1(p10,p10)
         
    def Redshiftanim2(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
        p10=cvo.CVO().CreateCVO("Nodes of Redshift","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("DenseCompute","").setPosition([2,0,0]).setangle(-TAU/3)
        p12=cvo.CVO().CreateCVO("DenseStorage","").setPosition([-2,0,0]).setangle(TAU/3)
        p13=cvo.CVO().CreateCVO("RA3","").setPosition([0,-2.5,0])
         
        p10.cvolist.append(p11)
         
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
         
        self.construct1(p10,p10)
         

      
if __name__ == "__main__":
    scene = Redshiftanim8()
    scene.render()

    