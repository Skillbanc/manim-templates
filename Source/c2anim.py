from manim import *
from numpy import size

import cvo

class C2Anim(Scene):
    
    # cvolist=[0]
    def construct(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p1=cvo.CVO().CreateCVO("John","36","Person","Age")
         cvolist=[p1]
         self.construct1(cvolist)
    def construct1(self,cvolist):

            cir1 = Circle(radius=cvolist[0].circle_radius,color=cvolist[0].circle_color)
            
            star = Star(outer_radius=0.15, inner_radius=0.1).move_to(cir1.get_center())
            c1name = Tex(cvolist[0].c1name).move_to(cir1.get_top()+.5)
            o1name = Tex(cvolist[0].o1name).move_to(star.get_bottom()).scale(0.5)

            self.play(Create(cir1,run_time=2),Create(c1name,run_time=2))
            
            self.play(Create(o1name),Create(star))
            grp1=VGroup(cir1,star,c1name,o1name)
            self.play(grp1.animate.shift(LEFT * 2))
            self.wait(2)

            cir2 = Circle(radius=cvolist[0].circle_radius,color=cvolist[0].circle_color)
            
            star2 = Star(outer_radius=0.15, inner_radius=0.1).move_to(cir2.get_center())
            c2name = Tex(cvolist[0].c2name).move_to(cir2.get_top()+.5)
            o2name = Tex(cvolist[0].o2name).next_to(star2).scale(0.5)

            self.play(Create(cir2,run_time=2),Create(c2name,run_time=2))
            
            self.play(Create(o2name),Create(star2))
            grp1=VGroup(cir2,star2,c2name,o2name)
            self.play(grp1.animate.shift(RIGHT * 2))
            self.wait(2)

            self.play(Create(Arrow(star.get_center(),star2.get_center())),run_time=2)
        
# if __name__ == "__main__":
#     p1=cvo.CVO().CreateCVO("John","36","Person","Age")
#     cvolist=[p1]
#     scene = C1Anim()
#     scene.construct(cvolist)
#     # scene.construct(cvo=p1)
#     scene.render()