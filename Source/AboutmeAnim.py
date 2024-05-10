# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License

import json
from manim import *

from AbstractAnim import AbstractAnim

import cvo

class AboutMe(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderAboutMe()
       
        
    # render using CVO data object
    def RenderAboutMe(self):
        count = 0
        # starting object
        p10=cvo.CVO().CreateCVO("My Name","Vailla Rohit")
        count += 1
        
        # Level 1 First c2 object
        p11=cvo.CVO().CreateCVO("College","IFHE")
        count += 1
        # Level 2 
        p14=cvo.CVO().CreateCVO("Location","Hyderabad")
        count += 1
        p11.cvolist.append(p14)
        
        p10.cvolist.append(p11)
            
        # 2nd c2 object
        p12=cvo.CVO().CreateCVO("Company","Skillbanc.com.Inc, USA")
        count += 1
        # Level 2
        p13=cvo.CVO().CreateCVO("Project","Manim-Templates")
        count += 1
        p12.cvolist.append(p13)
        
        p10.cvolist.append(p12)
        
        self.setNumberOfClasses(count)
       
       
        self.construct1(p10,p10)
   
if __name__ == "__main__":
    scene = AboutMe()
    scene.render()
    