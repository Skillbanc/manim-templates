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


class Redshiftanim9(AbstractAnim):


     # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.RedshiftanimA()
        self.wait(2)
        self.clear()
        self.RedshiftanimB()
        self.wait(2)
        self.clear()
        self.RedshiftanimC()
        self.wait(2)
        self.clear()
        self.RedshiftanimD()
    
    
    def RedshiftanimA(self):
        self.isRandom=False
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
        p10=cvo.CVO().CreateCVO("AWS Services","").setPosition([0,2.5,0]).setangle(TAU/4)
        p11=cvo.CVO().CreateCVO("Compute Services","").setPosition([-5,-2,0]).setangle(TAU/4)
        p12=cvo.CVO().CreateCVO("Storage Services","").setPosition([0,-2,0]).setangle(TAU/4)
        p13=cvo.CVO().CreateCVO("Database Services","").setPosition([5,-2,0]).setangle(TAU/4)
        
        p10.cvolist.append(p11) 
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.colorChoice=[RED,BLUE,GREEN,PURPLE,ORANGE,YELLOW,LIGHT_PINK,WHITE,LIGHT_GRAY,LIGHT_BROWN,PINK,GRAY_BROWN,DARK_BROWN,MAROON,MAROON_A,MAROON_B,MAROON_C,MAROON_D,MAROON_E]
        self.construct1(p10,p10)
         
    def RedshiftanimB(self):
        self.isRandom=False
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
        p10=cvo.CVO().CreateCVO("Compute Services","").setPosition([0,2.5,0]).setangle(TAU/4)
        p11=cvo.CVO().CreateCVO("Amazon EC2","").setPosition([4,2,0]).setangle(TAU/4)
        p12=cvo.CVO().CreateCVO("AWS Lambda","").setPosition([5,-2,0]).setangle(TAU/4)
        p13=cvo.CVO().CreateCVO("Amazon ECS","").setPosition([-4,2,0]).setangle(TAU/4)
        p14=cvo.CVO().CreateCVO("AWS Batch","").setPosition([-5,-2,0]).setangle(TAU/4)
        
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
         
        self.construct1(p10,p10)

    def RedshiftanimC(self):
        self.isRandom=False
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
        p10=cvo.CVO().CreateCVO("Storage Services","").setPosition([0,2.5,0]).setangle(TAU/4)
        p11=cvo.CVO().CreateCVO("Amazon S3","").setPosition([2,0,0]).setangle(TAU/4)
        p12=cvo.CVO().CreateCVO("Amazon Glacier","").setPosition([-2,0,0]).setangle(TAU/4)
        p13=cvo.CVO().CreateCVO("Amazon EBS","").setPosition([0,-2.5,0]).setangle(TAU/4)

        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        
        self.construct1(p10,p10)

    def RedshiftanimD(self):
        self.isRandom=False
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
        p10=cvo.CVO().CreateCVO("Database Services","").setPosition([0,2.5,0]).setangle(TAU/4)
        p11=cvo.CVO().CreateCVO("Amazon RDS","").setPosition([2,0,0]).setangle(TAU/4)
        p12=cvo.CVO().CreateCVO("Amazon DyanamoDB","").setPosition([-2,0,0]).setangle(TAU/4)
        p13=cvo.CVO().CreateCVO("Amazon Redshift","").setPosition([0,-2.5,0]).setangle(TAU/4)
        
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        
        self.construct1(p10,p10)    
         

      
if __name__ == "__main__":
    scene = Redshiftanim9()
    scene.render()

    