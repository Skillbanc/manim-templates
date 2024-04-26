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
    positionChoice=[[0,2.5,0],[4,2,0],[5,-2,0],[-4,3,0],[-4,1,0],[-4,-1,0]]
    def construct(self):
        pass
    
    def get_random_position(self):
        positionChoiceIndex = random.randint(0, 5)
        return positionChoiceIndex

    def construct1(self,cvo,cvoParent):
        colorChoiceIndex = random.randint(0, 5)
        positionChoiceIndex = self.get_random_position()
        cvo.pos=self.positionChoice[positionChoiceIndex]
        shapeChoiceIndex = 0 # random.randint(0,3)
        # Circle to contain objects
        cir1 = Circle(radius=cvo.circle_radius,color=self.colorChoice[colorChoiceIndex])
            
        star = Star(outer_radius=0.15, inner_radius=0.1,color=self.colorChoice[colorChoiceIndex]).move_to(cir1.get_center())
        c1nameposition = cvo.c1nameposition

        if( c1nameposition == None):
            c1nameposition = cir1.get_top()

        cname = Tex(cvo.cname,color=self.colorChoice[colorChoiceIndex]).move_to(c1nameposition).shift(UP * 0.25)
        o1nameposition = cvo.o1nameposition

        if( o1nameposition == None):
            o1nameposition = star.get_top()
        oname = Tex(cvo.oname,color=self.colorChoice[colorChoiceIndex]).move_to(o1nameposition).scale(0.5).shift(UP * 0.15)
        
        self.play(Create(cir1,run_time=cvo.duration),Create(cname,run_time=cvo.duration))
            
        self.play(Create(oname),Create(star))
       
        grp1=VGroup(cir1,star,cname,oname)
        
        self.play(grp1.animate.move_to(cvo.pos).scale(0.75))
        
        arrow1 = CurvedArrow(cvoParent.pos,cvo.pos,angle=cvo.angle,color=WHITE)
        
        self.play(Create(arrow1),run_time=cvo.duration)
        
        
        self.wait()
        
        if (len(cvo.cvolist) > 0):
            for idx in range(0,len(cvo.cvolist)):
                self.construct1(cvo.cvolist[idx],cvo)

    def construct2(self,cvo,cvoParent):
        colorChoiceIndex = random.randint(0, 5)
        shapeChoiceIndex = 0 #random.randint(0,3)
        # Circle to contain objects
        cir1 = Circle(radius=cvo.circle_radius,color=self.colorChoice[colorChoiceIndex])
        self.add(NumberPlane())
        self.play(Create(cir1,run_time=2))
            
        
       
        # grp1=VGroup(cir1,star,cname,oname)



        if cvo!=cvoParent:
            cir1.animate.move_to(cvo.pos)
        cname = Tex(cvo.cname,color=self.colorChoice[colorChoiceIndex]).move_to(cir1.get_top()).shift(UP * 0.25)
        star = Star(outer_radius=0.15, inner_radius=0.1,color=self.colorChoice[colorChoiceIndex]).move_to(cir1.get_center())
        oname = Tex(cvo.oname,color=self.colorChoice[colorChoiceIndex]).move_to(star.get_top()).scale(0.5).shift(UP * 0.15)
        self.play(Create(cname,run_time=cvo.duration))
        self.play(Create(oname),Create(star))

        
        arrow1 = CurvedArrow(cvoParent.pos,cvo.pos,angle=-TAU/3,color=WHITE)
        self.play(oname.animate.move_to(star.get_bottom()))
        
        self.play(Create(arrow1),run_time=cvo.duration)
        
        
        self.wait()
        
        if (len(cvo.cvolist) > 0):
            for idx in range(0,len(cvo.cvolist)):
                self.construct1(cvo.cvolist[idx],cvo)
                
        