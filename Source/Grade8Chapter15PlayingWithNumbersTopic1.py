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


class Grade8Chapter15PlayingWithNumbersTopic1(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Playing_numbers()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        
    
    
    def Playing_numbers(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("PlayingWithNumbers","Place Value").setPosition([0,2.5,0])
         p11=cvo.CVO().CreateCVO("Example","64").setPosition([4,2,0])
         p12=cvo.CVO().CreateCVO("Expansion","$60+4$").setPosition([5,-2,0])
        
         p13=cvo.CVO().CreateCVO("In words","sixty four").setPosition([-4,2,0]).setangle(-TAU/4)
         
         p11.cvolist.append(p12)
         
         p10.cvolist.append(p11)
        
         p11.cvolist.append(p13)
         
         self.construct1(p10,p10)
         
    def SetDeveloperList(self): 
       self.DeveloperList="Medha Masanam" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade8Chapter15PlayingWithNumbersTopic1.py"
  
      
if __name__ == "__main__":
    scene = Grade8Chapter15PlayingWithNumbersTopic1()
    scene.render()