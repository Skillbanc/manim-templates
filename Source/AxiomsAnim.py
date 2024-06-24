<<<<<<< HEAD
=======
# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla
>>>>>>> 790924edeb67f3367e9dcfacd0ef999d6047a93b
import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class AxiomsAnim(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
<<<<<<< HEAD
        self.constructDataByCVO()
        self.RenderSkillbancLogo()
        
    # render using CVO data object
    def constructDataByCVO(self):
        p10=cvo.CVO().CreateCVO("mathematics","AXIOMS")
        p11=cvo.CVO().CreateCVO("","a+b=b+a")
        p12=cvo.CVO().CreateCVO("","a*b=b*a")
        p13=cvo.CVO().CreateCVO("","a+0=a")
        p14=cvo.CVO().CreateCVO("","a*1=a")
        p15=cvo.CVO().CreateCVO("","a*0=0")
=======
        self.RenderSkillbancLogo()
        self.constructDataByCVO()
        # self.fadeOut()
        # self.constructDataByJSON()
        # self.fadeOut()
        
    # render using CVO data object
    def constructDataByCVO(self):
        p10=cvo.CVO().CreateCVO("Mathematics Axioms","")
        p11=cvo.CVO().CreateCVO("Axiom", "a+b=b+a")
        p12=cvo.CVO().CreateCVO("Axiom", "a*b=b*a")
        p13=cvo.CVO().CreateCVO("Axiom", "a+0=a")
        p14=cvo.CVO().CreateCVO("Axiom", "a*1=a")
        p15=cvo.CVO().CreateCVO("Axiom", "a(b+c)=ab+ac")
        p16=cvo.CVO().CreateCVO("Axiom", "a+(b+c)=(a+b)+c")
        
>>>>>>> 790924edeb67f3367e9dcfacd0ef999d6047a93b
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
<<<<<<< HEAD


        self.construct1(p10,p10)
    
   


=======
        p10.cvolist.append(p16)
        self.setNumberOfCirclePositions(7)
        rectangle=Rectangle()
        self.add(rectangle)
        self.wait(1)
        self.remove(rectangle)
        self.wait(1)
        self.construct1(p10,p10)


        
      
>>>>>>> 790924edeb67f3367e9dcfacd0ef999d6047a93b
if __name__ == "__main__":
    scene = AxiomsAnim()
    scene.render()
    