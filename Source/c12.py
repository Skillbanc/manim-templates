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

class C12Anim(AbstractAnim):
    
    def construct(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("repository","manimtemplates")
         #p11onamelist=["git pull","git push","git commit","git merge"]
         p11 = cvo.CVO().CreateCVO("commands","xys")
         p10.cvolist.append(p11)
         #p11.extendOname(p11onamelist)
         
         self.construct1(p10,p10)
  
            
if __name__ == "__main__":
    scene = C12Anim()
    scene.render()