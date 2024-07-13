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


class Grade8Chapter15PlayingWithNumbersTopic2(AbstractAnim):

   def construct(self):
        self.RenderSkillbancLogo()
        self.Expanded_Form()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        
    
   def Expanded_Form(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("Playing With Numbers","Expanded Form").setPosition([0,2.5,0])
         p11=cvo.CVO().CreateCVO("Example","64").setPosition([4,2,0])
         p12=cvo.CVO().CreateCVO("Expansion","$60+4$").setPosition([5,-2,0])
        
         p13=cvo.CVO().CreateCVO("Equal to","$(10*6)+(8)$").setPosition([-4,2,0]).setangle(-TAU/4)
         
         p11.cvolist.append(p12)
         
         p10.cvolist.append(p11)
        
         p12.cvolist.append(p13)
         
         self.construct1(p10,p10)


   def SetDeveloperList(self): 
       self.DeveloperList="Medha Masanam" 

   def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade8Chapter15PlayingWithNumbersTopic2.py"
   

      
if __name__ == "__main__":
    scene = Grade8Chapter15PlayingWithNumbersTopic2()
    scene.render()