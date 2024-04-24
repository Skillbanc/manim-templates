# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy

from manim import *
from numpy import size

import cvo

class C3Anim(Scene):
    
    
    def construct(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().setc1o1Name("Person","John Doe")
         p11=cvo.CVO().setc2o2Name("Age","36")
         p12=cvo.CVO().setc2o2Name("First Name","John")
         
         cvolist=[]
         cvolist.append(p10)
         cvolist.append(p11)
         cvolist.append(p12)
         
         self.construct1(cvolist)
    def construct1(self,cvolist):
            # c1o1
            cir1 = Circle(radius=cvolist[0].circle_radius,color=cvolist[0].circle_color)
            
            star = Star(outer_radius=0.15, inner_radius=0.1).move_to(cir1.get_center())
            c1name = Tex(cvolist[0].c1name).move_to(cir1.get_top()).shift(UP * 0.25)
            o1name = Tex(cvolist[0].o1name).move_to(star.get_top()).scale(0.5).shift(UP * 0.15)

            self.play(Create(cir1,run_time=2),Create(c1name,run_time=2))
            
            self.play(Create(o1name),Create(star))
            grp1=VGroup(cir1,star,c1name,o1name)
            self.play(grp1.animate.shift(UP * 2))
           

            # c2o2
            cir2 = Circle(radius=cvolist[1].circle_radius,color=cvolist[1].circle_color).shift(DOWN * 0.5)
            
            staro2name1 = Star(outer_radius=0.15, inner_radius=0.1).move_to(cir2.get_center())
            c2name1 = Tex(cvolist[1].c2name).move_to(cir2.get_top()).shift(UP * 0.25)
            o2name1 = Tex(cvolist[1].o2name).move_to(staro2name1.get_top()).scale(0.5).shift(DOWN * 0.5)

            self.play(Create(cir2,run_time=2),Create(c2name1,run_time=2))
            
            self.play(Create(o2name1),Create(staro2name1))
            grp2=VGroup(cir2,staro2name1,c2name1,o2name1)
            self.play(grp2.animate.shift(LEFT * 4))
           

            self.play(Create(CurvedArrow(star.get_center(),staro2name1.get_center())),run_time=2)
        
            # c2o2
            cir3 = Circle(radius=cvolist[2].circle_radius,color=cvolist[2].circle_color).shift(DOWN * 0.5)
            
            staro2name2 = Star(outer_radius=0.15, inner_radius=0.1).move_to(cir3.get_center())
            c2name2 = Tex(cvolist[2].c2name).move_to(cir3.get_top()).shift(UP * .25)
            o2name2 = Tex(cvolist[2].o2name).move_to(staro2name2.get_top()).scale(0.5).shift(DOWN * 0.5)
            
            self.play(Create(cir3,run_time=2),Create(c2name2,run_time=2))
            
            self.play(Create(o2name2),Create(staro2name2))
            grp3=VGroup(cir3,staro2name2,c2name2,o2name2)
            self.play(grp3.animate.shift(RIGHT * 4))
            self.wait(2)

            self.play(Create(CurvedArrow(star.get_center(),staro2name2.get_center())),run_time=2)
            
           
            self.wait(2)
            
if __name__ == "__main__":
    scene = C3Anim()
    scene.render()