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


class Grade8Chapter15PlayingWithNumbersTopic3(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.create_animation()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        
    
    def create_animation(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("Factors","every number has factors").setPosition([0,2.5,0])
         p11=cvo.CVO().CreateCVO("Type-1","Prime Numbers").setPosition([4,2,0])
         p12=cvo.CVO().CreateCVO("Type-2","Composite Numbers").setPosition([5,-2,0])
        
         p13=cvo.CVO().CreateCVO("Example","2,3,5,7").setPosition([-4,3,0]).setangle(-TAU/4)
         p14=cvo.CVO().CreateCVO("Example","4,6,8,9").setPosition([-2,0,0]).setangle(-TAU/4)
         p15=cvo.CVO().CreateCVO("Defination","having 1 and itself as factors").setPosition([-4,-1,0]).setangle(-TAU/4)
         p16=cvo.CVO().CreateCVO("Defination","having factors other than 1 or itself").setPosition([-4,-3,0]).setangle(-TAU/4)
         p10.cvolist.append(p11)
         
         p10.cvolist.append(p12)
        
         p11.cvolist.append(p15)
         p15.cvolist.append(p13)
         p12.cvolist.append(p16)
         p16.cvolist.append(p14)
         self.construct1(p10,p10)
    def SetDeveloperList(self): 
       self.DeveloperList="Medha Masanam" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade8Chapter15PlayingWithNumbersTopic3.py"
      

      
if __name__ == "__main__":
    scene = Grade8Chapter15PlayingWithNumbersTopic3()
    scene.render()