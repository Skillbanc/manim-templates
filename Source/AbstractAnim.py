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
# class that has all common methods that can be used by subclasses
class AbstractAnim(Scene):
    colorChoice=[RED,BLUE,GREEN,PURPLE,ORANGE,YELLOW]
    shapeChoice=[Circle,Triangle,Square,Rectangle]
    positionChoice = [[-6,-2,0],[4,-2,0],[2,0,0],[-6,2,0],[-4,-2,0],[-4,2,0],[-2,-2,0],[4,0,0],[-4,0,0],[-2,2,0],[2,-2,0],[-6,0,0],[2,2,0],[6,0,0],[4,2,0],[6,-2,0],[-2,0,0],[6,2,0]]

    angleChoice = [TAU/5,TAU/4,TAU/3,TAU/2,-TAU/5,-TAU/4,-TAU/3,-TAU/2]
    def construct(self):
        pass
    # # def setup(self):
        
    # #     self.buildPositionChoiceArray()
        
    # def buildPositionChoiceArray(self):
        
    #     xrange = [-6,-4,-2,0,2,4,6]
    #     yrange = [-2,0,2]
    #     for i in xrange:
    #         for j in yrange:
    #             if not (i == 0 & j ==0):
    #                 print("[" + str(i) +"," + str(j) + ",0]" + ",")
    #                 self.positionChoice.append([i,j,0])
        
        
            
    #     return self
    
    # get the random position of the circle
    def get_random_position(self):
        positionChoiceIndex = 1
        if (len(self.positionChoice) > 2):
            positionChoiceIndex = random.randint(1, len(self.positionChoice) - 1)
        if (len(self.positionChoice) == 1):
            positionChoiceIndex = 0;
        return positionChoiceIndex
    # current object and the parent object to render 2 circles 2 class names 2 object names  and one arrow
    def construct1(self,cvo,cvoParent):
        angleChoiceIndex = random.randint(0,len(self.angleChoice) - 1)
        cvo.angle = self.angleChoice[angleChoiceIndex]
        colorChoiceIndex = random.randint(0, len(self.colorChoice) - 1)
        positionChoiceIndex = self.get_random_position()
        
        if (cvo.pos == None):
            cvo.pos=self.positionChoice[positionChoiceIndex]
        
        self.positionChoice.remove(cvo.pos)
            
        shapeChoiceIndex = 0 # random.randint(0,3)
        # Circle to contain objects
        cir1 = Circle(radius=cvo.circle_radius,color=self.colorChoice[colorChoiceIndex])
        star = Star(outer_radius=0.1, inner_radius=0.05,color=self.colorChoice[colorChoiceIndex]).move_to(cir1.get_center())
        
        c1nameposition = cvo.c1nameposition
        if( c1nameposition == None):
            c1nameposition = cir1.get_top()
        cname = Tex(cvo.cname,color=self.colorChoice[colorChoiceIndex]).move_to(c1nameposition).shift(UP * 0.25)
        
        o1nameposition = cvo.o1nameposition
        if( o1nameposition == None):
            o1nameposition = star.get_top()
        oname = Tex(cvo.oname,color=self.colorChoice[colorChoiceIndex]).move_to(o1nameposition).scale(0.5).shift(UP * 0.15)
        
        self.play(Create(cir1,run_time=cvo.duration),Create(cname,run_time=cvo.duration))
        
        if len(cvo.onameList) == 0:
            self.play(Create(oname),Create(star))
            grp1=VGroup(cir1,star,cname,oname)
        else: 
            grp1=VGroup(cir1,cname)
        
        self.play(grp1.animate.move_to(cvo.pos).scale(0.75))
        
        arrow1 = CurvedArrow(cvoParent.pos,cvo.pos,angle=cvo.angle)
        arrow1.tip.scale(0.75)
        if len(cvo.onameList) == 0:
            self.play(Create(arrow1),run_time=cvo.duration)
        # cname.remove()
        # oname.remove()
        # self.play(Create(cname),Create(oname))
        #self.bring_to_back(arrow1)
       
        if (len(cvo.onameList) > 0 and len(cvo.onameList) < 5):
            for index in range(len(cvo.onameList)):
                # starLocal = Star(outer_radius=0.15, inner_radius=0.1,color=self.colorChoice[colorChoiceIndex]).move_to(cir1.get_center())
                starLocal = Star(outer_radius=0.1, inner_radius=0.05,color=self.colorChoice[colorChoiceIndex]).move_to(cir1.get_top()).shift(LEFT * .35, DOWN * .25*(index+1)).scale(0.5)
                onameLocalText = Tex(cvo.onameList[index],color=self.colorChoice[colorChoiceIndex]).scale(0.35).next_to(starLocal).shift(LEFT * .20)
                arrow2 = CurvedArrow(cvoParent.pos,starLocal.get_center(),angle=cvo.angle)
                self.play(Create(starLocal),Create(onameLocalText))#grpLocal.animate.move_to(cir1.get_center()).scale(0.5).shift(DOWN * 2))#scale(0.25))
                self.play(Create(arrow2))
        else:
            self.play(grp1.animate.scale(1+0.1*len(cvo.onameList)))
            for index in range(len(cvo.onameList)):
                # starLocal = Star(outer_radius=0.15, inner_radius=0.1,color=self.colorChoice[colorChoiceIndex]).move_to(cir1.get_center())
                starLocal = Star(outer_radius=0.1, inner_radius=0.05,color=self.colorChoice[colorChoiceIndex]).move_to(cir1.get_top()).shift(LEFT * .35, DOWN * .25*(index+1)).scale(0.6)
                onameLocalText = Tex(cvo.onameList[index],color=self.colorChoice[colorChoiceIndex]).scale(0.45).next_to(starLocal).shift(LEFT * .20)
                arrow2 = CurvedArrow(cvoParent.pos,starLocal.get_center(),angle=cvo.angle)
                self.play(Create(starLocal),Create(onameLocalText))#grpLocal.animate.move_to(cir1.get_center()).scale(0.5).shift(DOWN * 2))#scale(0.25))
                self.play(Create(arrow2))
                          
        cvo.cnameMObject = cname
        cvo.onameMObject = oname
        
        self.wait()
        
        if (len(cvo.cvolist) > 0):
            for idx in range(0,len(cvo.cvolist)):
                self.construct1(cvo.cvolist[idx],cvo)
                
        

    # pass the json object and the top level data object
    def parsejson(self,json_data,cvo10):
        
        for key, value in json_data.items():
            if isinstance(value, dict):
                pass
                # p10=cvo.CVO().CreateCVO(key,"")
                # cvo10.cvolist.append(p10)
                   
                # self.parsejson(value,cvo10)                

            if isinstance(value, list):
                for item in value:
                    p10=cvo.CVO().CreateCVO(key,item)
                    cvo10.cvolist.append(p10)
            
            if isinstance(value,str):
                p10=cvo.CVO().CreateCVO(key,value)
                cvo10.cvolist.append(p10)
                
        
    def fadeOut(scene: Scene):
        animations = []
        for mobject in scene.mobjects:
            animations.append(FadeOut(mobject))
        if (len(animations) > 0):
            scene.play(*animations)
        
    