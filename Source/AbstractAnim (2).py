# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla

from manim import *
from numpy import size

import cvo
import random

class AbstractAnim(Scene):
    
    colorChoice=[RED,BLUE,GREEN,PURPLE,ORANGE,YELLOW]
    shapeChoice=[Circle,Triangle,Square,Rectangle]
    def construct(self):
        pass

    def construct1(self,cvo,cvoParent):
        colorChoiceIndex = random.randint(0, 5)
        shapeChoiceIndex = 0 # random.randint(0,3)
        # Circle to contain objects
        cir1 = Circle(radius=cvo.circle_radius,color=self.colorChoice[colorChoiceIndex])
            
        star = Star(outer_radius=0.15, inner_radius=0.1,color=YELLOW).move_to(cir1.get_center())
        cname = Tex(cvo.cname,color=self.colorChoice[colorChoiceIndex]).move_to(cir1.get_top()).shift(UP * 0.25)
        oname = Tex(cvo.oname,color=self.colorChoice[colorChoiceIndex]).move_to(star.get_top()).scale(0.5).shift(UP * 0.15)
        
        self.play(Create(cir1,run_time=2),Create(cname,run_time=2))
            
        self.play(Create(oname),Create(star))
       
        grp1=VGroup(cir1,star,cname,oname)
        self.play(grp1.animate.move_to(cvo.pos).scale(0.75))
        if (cvo.pos != cvoParent.pos):
            arrow1 = CurvedArrow(cvoParent.pos,cvo.pos,angle=-TAU/3,color=WHITE)
            self.play(Create(arrow1),run_time=2)
        
        
        self.wait()
        
        if (len(cvo.cvolist) > 0):
            for idx in range(0,len(cvo.cvolist)):
                self.construct1(cvo.cvolist[idx],cvo)
                
    def construct2(self,cvo,cvoParent):
        colorChoiceIndex = random.randint(0, 5)
        shapeChoiceIndex = 0 # random.randint(0,3)
        # Circle to contain objects
        cir1 = Circle(radius=cvo.circle_radius,color=self.colorChoice[colorChoiceIndex])
        
        
        self.add(NumberPlane())
         
        
        
        self.play(Create(cir1,run_time=1))
        

        grp1=VGroup(cir1,star,cname,oname)
        
        
       
        if (cvo != cvoParent):
        
            self.play(grp1.animate.move_to(cvo.pos).scale(0.5))
            star = Star(outer_radius=0.15, inner_radius=0.1,color=YELLOW).move_to(cir1.get_center())
            cname = Tex(cvo.cname,color=self.colorChoice[colorChoiceIndex]).move_to(cir1.get_top()).shift(UP * 0.25)
            oname = Tex(cvo.oname,color=self.colorChoice[colorChoiceIndex]).move_to(star.get_top()).scale(0.5).shift(UP * 0.15)
        
            self.play(Create(cname,run_time=1))
        
            self.play(Create(oname),Create(star))
        
        if (cvo != cvoParent):
            arrow1 = CurvedArrow(cvoParent.pos,cvo.pos,angle=-TAU/3,color=WHITE)
            self.play(Create(arrow1),run_time=2)
        
        
        self.wait()
        
        if (len(cvo.cvolist) > 0):
            for idx in range(0,len(cvo.cvolist)):
                self.construct2(cvo.cvolist[idx],cvo)
                
           