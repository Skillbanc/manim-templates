# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License

import json
from manim import *

from AbstractAnim import AbstractAnim

import cvo

class rational(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderAboutMe()
        # self.ending()
       
        
    # render using CVO data object
    def RenderAboutMe(self):
        count = 0
        # starting object
        p10=cvo.CVO().CreateCVO("Rational Numbers","The numbers which can be represented in P/Q").setPosition([0,2.5,0])
        count += 1

                # 2nd c2 object
        p12=cvo.CVO().CreateCVO("Examples","1/2,10,7/2,-3/2").setPosition([3,0,0])
        count += 1
        # Level 2
        # p13=cvo.CVO().CreateCVO("Project","Manim-Templates")
        # count += 1
        # p12.cvolist.append(p13)
        
        p10.cvolist.append(p12)
        
        # Level 1 First c2 object
        p11=cvo.CVO().CreateCVO("operations",".").setPosition([-3,0,0])
        count += 1
        # Level 2 
        p14=cvo.CVO().CreateCVO("Addition","+").setPosition([-4,-2,2])
        count += 1
        p11.cvolist.append(p14)

        p15=cvo.CVO().CreateCVO("Subtraction","-").setPosition([-5.5,-2,2])
        count += 1
        p11.cvolist.append(p15)

        p16=cvo.CVO().CreateCVO("multiplication","*").setPosition([-2,-2,2])
        count += 1
        p11.cvolist.append(p16)

        p17=cvo.CVO().CreateCVO("Division","/").setPosition([0,-2,2])
        count += 1
        p11.cvolist.append(p17)
        
        p10.cvolist.append(p11)
            


        # p13=cvo.CVO().CreateCVO("topics","role of 0,role of 1,\nclosure,\nassociative,\n distributive,\ncommutative")
        # count += 1
        # p10.cvolist.append(p13)
        
        self.setNumberOfCirclePositions(count)
       
       
        self.construct1(p10,p10)

    # def ending(self):
    #     self.setNumberOfCirclePositions(3)
    #     #self.angleChoice = [0,0,0]
    #     self.isRandom = False

    #     p8=cvo.CVO().CreateCVO("GITHUB SOURCECODE LINK","")
    #     p9=cvo.CVO().CreateCVO("File name","add.py")
    #     p7=cvo.CVO().CreateCVO("Github Url","https://github.com/Skillbanc")
       
    #     p8.cvolist.append(p9)
    #     p8.cvolist.append(p7)
    #     self.construct1(p8,p8)
   
if __name__ == "__main__":
    scene = rational()
    scene.render()
    