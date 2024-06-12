# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla


from manim import *


import cvo
import random
# class that has all common methods that can be used by subclasses
class AbstractAnim(Scene):
    grpAll = VGroup()
    isFadeOutAtTheEndOfThisScene = False
    colorChoice=[RED,BLUE,GREEN,PURPLE,ORANGE,YELLOW,LIGHT_PINK,WHITE,LIGHT_GRAY,LIGHT_BROWN,PINK,GRAY_BROWN]
    shapeChoice=[Circle,Triangle,Square,Rectangle]
    positionChoice = [[-6,-2,0],[4,-2,0],[2,0,0],[-6,2,0],[-4,-2,0],[-4,2,0],[-2,-2,0],[4,0,0],[-4,0,0],[-2,2,0],[2,-2,0],[-6,0,0],[2,2,0],[6,0,0],[4,2,0],[6,-2,0],[-2,0,0],[6,2,0]]
    DeveloperList=""
    

    # angleChoice = [TAU/5,TAU/4,TAU/3,TAU/2,-TAU/5,-TAU/4,-TAU/3,-TAU/2]
    isRandom = True
   
    def initChoices(self):
        self.colorChoice=[RED,BLUE,GREEN,PURPLE,ORANGE,YELLOW,LIGHT_PINK,WHITE,LIGHT_GRAY,LIGHT_BROWN,PINK,GRAY_BROWN]
        self.shapeChoice=[Circle,Triangle,Square,Rectangle]
        self.positionChoice = [[0,0,0],[-6,-2,0],[4,-2,0],[2,0,0],[-6,2,0],[-4,-2,0],[-4,2,0],[-2,-2,0],[4,0,0],[-4,0,0],[-2,2,0],[2,-2,0],[-6,0,0],[2,2,0],[6,0,0],[4,2,0],[6,-2,0],[-2,0,0],[6,2,0]]
        self.angleChoice = [TAU/5,TAU/4,TAU/3,TAU/2,-TAU/5,-TAU/4,-TAU/3,-TAU/2]
    
    def setNumberOfCirclePositions(self,numberOfCircles : int):
        match numberOfCircles:
            case 1:
                self.positionChoice = [[0,0,0]]
            case 2:
                self.positionChoice = [[-4,0,0],[4,0,0]]
            case 3:
                self.positionChoice = [[-4,0,0],[4,2,0],[4,-2,0]]
            case 4:
                self.positionChoice = [[-4,-2,0],[4,-2,0],[-4,2,0],[4,2,0]]
            case 5:
                self.positionChoice = [[-4,-2,0],[4,-2,0],[-4,2,0],[4,2,0],[0,-2,0]]
            case 6:
                 self.positionChoice = [[-6,-2,0],[6,-2,0],[0,3,0],[-6,2,0],[6,2,0],[0,-3,0]]
        
    def setNumberOfAngleChoices(self,numberOfAngles : int):
        match numberOfAngles:
            case 9:
                self.angleChoice = [TAU/5,TAU/4,TAU/3,TAU/2,-TAU/5,-TAU/4,-TAU/3,-TAU/2,TAU/5,TAU/4]
    def construct(self):
        pass
    def setup(self):
        self.initChoices()
        
        # self.buildPositionChoiceArray()
        
    def buildPositionChoiceArray(self):
        pass    
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
            positionChoiceIndex = 0
        return positionChoiceIndex
    # current object and the parent object to render 2 circles 2 class names 2 object names  and one arrow
    def construct1(self,cvo,cvoParent):
        if (self.isRandom):
            colorChoiceIndex = random.randint(0, len(self.colorChoice) - 1)
        else:
            colorChoiceIndex = 0
        
        cvo.color = self.colorChoice[colorChoiceIndex]
        
       
            
        # if random ness position then use random
        if (self.isRandom):
            positionChoiceIndex = self.get_random_position()
        else:
            positionChoiceIndex = 0
            
        if (cvo.pos == None):
            cvo.pos=self.positionChoice[positionChoiceIndex]
        
       
            
        shapeChoiceIndex = 0 # random.randint(0,3)
        # Circle to contain objects
        cir1 = Circle(radius=cvo.circle_radius,color=self.colorChoice[colorChoiceIndex])
        star = Star(outer_radius=0.1, inner_radius=0.05,color=self.colorChoice[colorChoiceIndex]).move_to(cir1.get_center())
        
        c1nameposition = cvo.c1nameposition
        if( c1nameposition == None):
            c1nameposition = cir1.get_top()
        if (cvo.IsMathText):
            cname = MathTex(cvo.cname,color=self.colorChoice[colorChoiceIndex]).move_to(c1nameposition).shift(UP * 0.25)
        else:
            cname = Tex(cvo.cname,color=self.colorChoice[colorChoiceIndex]).move_to(c1nameposition).shift(UP * 0.25)
        
        o1nameposition = cvo.o1nameposition
        if( o1nameposition == None):
            o1nameposition = star.get_top()
        
        if (cvo.IsMathText):
            oname = MathTex(cvo.oname,color=self.colorChoice[colorChoiceIndex]).move_to(o1nameposition).shift(UP * 0.15)
        else:
            oname = Tex(cvo.oname,color=self.colorChoice[colorChoiceIndex]).move_to(o1nameposition).shift(UP * 0.15)
        
        
        self.play(Create(cir1,run_time=cvo.duration),Create(cname,run_time=cvo.duration))
            
        
        
        if len(cvo.onameList) == 0:
            self.play(Create(oname),Create(star))
            self.play(cname.animate.scale(2.0), oname.animate.scale(2.0),run_time=1)
            self.play(cname.animate.scale(0.5), oname.animate.scale(0.3),run_time=1)
            grp1=VGroup(cir1,star,cname,oname)
        else: 
            grp1=VGroup(cir1,cname)
        
        self.play(grp1.animate.scale(0.75).move_to(cvo.pos).shift(UP*0.16))
    
        
    
        if (cvo != cvoParent):
            if (self.isRandom):
                angleChoiceIndex = random.randint(0,len(self.angleChoice) - 1)
            else:
                angleChoiceIndex = 0
            
            cvo.angle = self.angleChoice[angleChoiceIndex]
            
            
            arrow1 = CurvedArrow(cvoParent.pos,cvo.pos,angle=cvo.angle,stroke_width=1.5)
            arrow1.tip.scale(0.75)
            if len(cvo.onameList) == 0:
                self.play(Create(arrow1),run_time=cvo.duration)
            #self.bring_to_back(arrow1)
            grp1.add(arrow1)
            
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
        
        #self.wait()
        
       
                
        if (self.positionChoice.__contains__(cvo.pos)):
            self.positionChoice.remove(cvo.pos)
            
        if (cvo != cvoParent):
            if (self.angleChoice.__contains__(cvo.angle)):
                self.angleChoice.remove(cvo.angle)
                
        if (self.colorChoice.__contains__(cvo.color)):
            self.colorChoice.remove(cvo.color)
        
        if (len(cvo.cvolist) > 0):
            for idx in range(0,len(cvo.cvolist)):
                self.construct1(cvo.cvolist[idx],cvo)
        
        self.grpAll.add(grp1)
        
        
        if (self.isFadeOutAtTheEndOfThisScene):
            self.play(self.grpAll.animate.scale(0))
            
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
                
        
    def fadeOutCurrentScene(self):
        animations = []
        for mobject in self.mobjects:
            animations.append(FadeOut(mobject))
        if (len(animations) > 0):
            self.play(*animations)
        
        self.initChoices()
        
    def RenderSkillbancLogo(self):
        
        self.orange = "#D76800"
        self.blue = "#3F64A7"
        self.green = "#96D24D"
        self.circles = VGroup(
            Circle(radius=1).rotate(PI/2).set_fill(self.orange, opacity=1).set_stroke(self.orange, opacity=1).shift(LEFT*3),
            Circle(radius=1).rotate(PI/2).set_fill(self.blue, opacity=1).set_stroke(self.blue, opacity=1),
            Circle(radius=1).rotate(PI/2).set_fill(self.green, opacity=1).set_stroke(self.green, opacity=1).shift(RIGHT*3)
        )
        circle1, circle2, circle3 = self.circles
        
        lines = VGroup(
            Arrow(circle1.get_right(), circle2.get_left(), max_tip_length_to_length_ratio=2),
            Arrow(circle2.get_right(), circle3.get_left(), max_tip_length_to_length_ratio=2),
            CurvedArrow(circle1.get_top(), circle3.get_top(), angle=-TAU/4),
            CurvedArrow(circle1.get_bottom(), circle3.get_bottom(), angle=TAU/4)
        )

        # Adjust the starting points of the straight arrows to touch the circumference
        lines[0].put_start_and_end_on(circle1.get_right(), circle2.get_left())
        lines[1].put_start_and_end_on(circle2.get_right(), circle3.get_left())

        # Add the text "skillbanc" below the curved arrows
        self.play(Create(circle1), Create(circle2), Create(circle3), rate_func=smooth, run_time=1)
        self.play(Create(lines), rate_func=smooth, run_time=1)
        text = Text("Skillbanc.com, Inc.").next_to(lines[3], DOWN)
        self.play(Create(text), rate_func=smooth, run_time=0.75)
        
        self.logoGroup = VGroup().add(self.circles).add(lines).add(text)
        self.play(self.logoGroup.animate.scale(0),run_time=1)
        # self.play(self.circles.animate.scale(0),lines.animate.scale(0),text.animate.scale(0),run_time=3)
        
    def GithubSourceCodeReference(self): 
        self.SetDeveloperList()
        self.colorChoice=[BLUE,ORANGE,PINK,ORANGE,PURPLE]
        p2 = cvo.CVO().CreateCVO("SOURCE CODE REFERENCE", "").setPosition([0,2.5,0])
        p4 = cvo.CVO().CreateCVO("Github URL", "https://github.com/Skillbanc/manim-templates").setPosition([-4,1,0]).setangle(TAU / 3)
        p5 = cvo.CVO().CreateCVO("File Name", "comparingquantities.py").setPosition([4,1,0]).setangle(TAU / 3)
        p6=cvo.CVO().CreateCVO("Architected By","Sudhakar Moparthy").setPosition([5,-2,0]).setangle(-TAU / 4)

        p7=cvo.CVO().CreateCVO("Developed By",self.GetDeveloperList()).setPosition([0,-2,0]).setangle(-TAU / 4)
        
        p2.cvolist.append(p4)
        p2.cvolist.append(p5)
        self.setNumberOfCirclePositions(5)
        p4.setcircleradius(3)
        p5.setcircleradius(2)
        p6.setcircleradius(1.5)
        p2.cvolist.append(p6)
        p2.cvolist.append(p7)
        self.construct1(p2,p2)
        
    def GetDeveloperList(self): 
        return self.DeveloperList
      
    def SetDeveloperList(self):  
        pass  
         
    def construct2(self,p10,cvoParent):  
        text0 = Tex(p10.onameList[0],color=BLUE)
        text01 = Tex(p10.onameList[0],color=BLUE)
        
        self.play(Create(text0))
        grp1 = VGroup(text01)
        
        for i in range(1,len(p10.onameList)):
                    
          
           if (p10.IsMathText):
            text1 = MathTex(p10.onameList[i],color=BLUE)
            text01 = MathTex(p10.onameList[i],color=BLUE)
           else:   
            text1 = Tex(p10.onameList[i],color=BLUE)
            text01 = MathTex(p10.onameList[i],color=BLUE)
            
           
           self.play(grp1.animate.shift(UP * 1))
           self.play(ReplacementTransform(text0,text1))
           
           grp1.add(text01)
           text0 = text1
           # self.wait(2)
         
           
           
        self.wait(2)