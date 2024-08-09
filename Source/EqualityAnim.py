# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License

import json
from os import remove
from manim import *
from scipy.spatial import transform
from AbstractAnim import AbstractAnim

import cvo

class EqualityAnim(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.RenderEqualityC1C2Diagram()
        self.RenderEquality1()
       
    def RenderEqualityC1C2Diagram(self):
        #self.positionChoice = [[0,0,0],[-6,-2,0],[4,-2,0],[2,0,0],[-6,2,0],[-4,-2,0],[-4,2,0],[-2,-2,0],[4,0,0],[-4,0,0],[-2,2,0],[2,-2,0],[-6,0,0],[2,2,0],[6,0,0],[4,2,0],[6,-2,0],[-2,0,0],[6,2,0]]
        self.setNumberOfCirclePositions(4)
        self.isRandom = False
        
        p10=cvo.CVO().CreateCVO("Equality","x=y")
        p11=cvo.CVO().CreateCVO("LHS","x")
        p12=cvo.CVO().CreateCVO("RHS","y")
        
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        
        self.construct1(p10,p10)
        
    # render using CVO data object
    def RenderEquality1(self):
        
        p10=cvo.CVO().CreateCVO("Equality","x=y")
        p10.SetIsMathText(True)
       
        p10.onameList.append("Equality")
        p10.onameList.append("1=1")
        p10.onameList.append("1+1=1+1")
        p10.onameList.append("1+1=2")
        p10.onameList.append("2=2")
        p10.onameList.append("2+1=2+1")
        p10.onameList.append("2+1=3")
        p10.onameList.append("3=3")
      
        p10.onameList.append("x=y")
        p10.onameList.append("x+1=y+1")
        p10.onameList.append("x+2=y+2")
        p10.onameList.append("x+K=y+K")
        p10.onameList.append("x-2=y-2")
        p10.onameList.append("x-K=y-K")
        p10.onameList.append("x*2=y*2")
        p10.onameList.append("x*3=y*3")
        p10.onameList.append("x*K=y*K")
        p10.onameList.append("x/2=y/2")
        p10.onameList.append("x/3=y/3")
        p10.onameList.append("x/K=y/K where K not equals 0")
        
        
        # self.construct1(p10,p10)
        
        self.construct2(p10,p10)
        
        
       
        
if __name__ == "__main__":
    scene = EqualityAnim()
    scene.render()
    