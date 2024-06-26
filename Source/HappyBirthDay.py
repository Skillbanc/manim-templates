# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy

from manim import *
from AbstractAnim import AbstractAnim

import cvo


class HappyBirthDay(AbstractAnim):
    
    
    def construct(self):
        # p1=cvo.CVO().CreateCVO("cname","oname")
        
        toList = ["Arjun!","Arjun!"]
        
        # change the index to generate happy birthday greeting for the person in toList
        p10=cvo.CVO().CreateCVO("Happy Birthday", toList[0])
         
        p11=cvo.CVO().CreateCVO("Greetings","Have a great day")
         
        p10.cvolist.append(p11)
         
        self.construct1(p10,p10)
         

      
if __name__ == "__main__":
    scene = HappyBirthDay()
    scene.render()