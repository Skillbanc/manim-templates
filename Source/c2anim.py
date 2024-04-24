# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla

from manim import *
from numpy import size

import cvo

class C2Anim(Scene):
    
    def construct(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("Person","John Doe").setPosition([0,2.5,0])
         
         p11=cvo.CVO().CreateCVO("Age","36").setPosition([0,-2.5,0])
                 
         p10.cvolist.append(p11)
         
         self.construct1(p10,p10)

    def construct1(self,cvo,cvoParent):
        # c1o1
        cir1 = Circle(radius=cvo.circle_radius,color=cvo.circle_color)
            
        star = Star(outer_radius=0.15, inner_radius=0.1).move_to(cir1.get_center())
        cname = Tex(cvo.cname).move_to(cir1.get_top()).shift(UP * 0.25)
        oname = Tex(cvo.oname).move_to(star.get_top()).scale(0.5).shift(UP * 0.15)
        
        self.play(Create(cir1,run_time=2),Create(cname,run_time=2))
            
        self.play(Create(oname),Create(star))
       
        grp1=VGroup(cir1,star,cname,oname)
        self.play(grp1.animate.move_to(cvo.pos).scale(0.75))
        
        arrow1 = CurvedArrow(cvoParent.pos,cvo.pos,angle=-TAU/3)
        
        self.play(Create(arrow1),run_time=2)
        
        
        self.wait()
        
        if (len(cvo.cvolist) > 0):
            for idx in range(0,len(cvo.cvolist)):
                self.construct1(cvo.cvolist[idx],cvo)
           
        
            
if __name__ == "__main__":
    scene = C2Anim()
    scene.render()