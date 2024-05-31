# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License

import json
from os import remove
from manim import *
from scipy.spatial import transform
from AbstractAnim import AbstractAnim

import cvo

class TrinomialFactorization(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        #self.RenderSkillbancLogo()
        #self.RenderTrinomialFactorizationC1C2Diagram()
        # self.RenderTrinomialFactorization1()
        self.RenderTrinomialFactorization2()
       
    def RenderTrinomialFactorizationC1C2Diagram(self):
        #self.positionChoice = [[0,0,0],[-6,-2,0],[4,-2,0],[2,0,0],[-6,2,0],[-4,-2,0],[-4,2,0],[-2,-2,0],[4,0,0],[-4,0,0],[-2,2,0],[2,-2,0],[-6,0,0],[2,2,0],[6,0,0],[4,2,0],[6,-2,0],[-2,0,0],[6,2,0]]
        self.setNumberOfCirclePositions(3)
        self.isRandom = False
        
        p10=cvo.CVO().CreateCVO("ax^2+bx+c","2x^2+5x+3").SetIsMathText(True)
        p11=cvo.CVO().CreateCVO("a * c","2 * 3")
        
        p12=cvo.CVO().CreateCVO("a+c","2 + 3")
        
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        
        self.construct1(p10,p10)
        
    # render using CVO data object
    def RenderTrinomialFactorization1(self):
        
        p10=cvo.CVO().CreateCVO("Trinomial Expresession","ax^2+bx+c").SetIsMathText(True)
        
       
        p10.onameList.append("Trinomial Expresession")
        p10.onameList.append("x^2+2x+1")
        p10.onameList.append("a=1,b=2,c=1")
        p10.onameList.append("ac= 1 * 1 = 1 , Factors Of ac = (1,1)")
        p10.onameList.append("x^2+x+x+1")
        p10.onameList.append("(x^2+x)+(x+1)")
        p10.onameList.append("x(x+1)+1(x+1)")
        p10.onameList.append("(x+1)(x+1)")
      
        
        # self.construct1(p10,p10)
        
        self.construct2(p10,p10)
        
    def RenderTrinomialFactorization2(self):
        
        p10=cvo.CVO().CreateCVO("Trinomial Expresession","2x^2+5x+3").SetIsMathText(True)
        
       
        p10.onameList.append("Trinomial Expresession")
        p10.onameList.append("2x^2+5x+3")
        p10.onameList.append("a=2,b=5,c=3")
        p10.onameList.append("ac= 2 * 3 = 6 , Factors of ac = (2,3)(6,1)")
        p10.onameList.append("2x^2+2x+3x+3")
        p10.onameList.append("(2x^2+2x)+(3x+3)")
        p10.onameList.append("2x(x+1)+3(x+1)")
        p10.onameList.append("(x+1)(2x+3)")
      
        
        # self.construct1(p10,p10)
        
        self.construct2(p10,p10)   
       
        
if __name__ == "__main__":
    scene = TrinomialFactorization()
    scene.render()
    