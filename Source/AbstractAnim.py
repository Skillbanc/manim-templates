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
    positionChoice = [[0,0,0],[0,2.5,0],[4,2,0],[5,-2,0],[-4,3,0],[-4,1,0],[-4,-1,0]]
    angleChoice = [TAU/5,TAU/4,TAU/3,TAU/2,-TAU/5,-TAU/4,-TAU/3,-TAU/2]
    def construct(self):
        pass
    
    def get_random_position(self):
        positionChoiceIndex = random.randint(1, len(self.positionChoice) - 1)
        if (len(self.positionChoice) == 1):
            positionChoiceIndex = 0;
        return positionChoiceIndex

    def construct1(self,cvo,cvoParent):
        angleChoiceIndex = random.randint(0,len(self.angleChoice) - 1)
        cvo.angle = self.angleChoice[angleChoiceIndex]
        colorChoiceIndex = random.randint(0, len(self.colorChoice) - 1)
        
        positionChoiceIndex = self.get_random_position()
        cvo.pos=self.positionChoice[positionChoiceIndex]
        self.positionChoice.remove(self.positionChoice[positionChoiceIndex])
        
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
        
        arrow1 = CurvedArrow(cvoParent.pos,cvo.pos,angle=cvo.angle,stroke_width=2)
        arrow1.tip.scale(0.5)
        self.play(Create(arrow1),run_time=cvo.duration)
        # cname.remove()
        # oname.remove()
        # self.play(Create(cname),Create(oname))
        self.bring_to_back(arrow1)
       
        
        
        cvo.cnameMObject = cname
        cvo.onameMObject = oname
        
        self.wait()
        
        if (len(cvo.cvolist) > 0):
            for idx in range(0,len(cvo.cvolist)):
                self.construct1(cvo.cvolist[idx],cvo)

    
                
        