from manim import *
from numpy import size

import cvo

class C1Anim(Scene):
    
    # cvolist=[0]
    def construct(self):
         p1=cvo.CVO().CreateCVO("John","36")
         cvolist=[p1]
         self.construct1(cvolist)
    def construct1(self,cvolist):

            cir1 = Circle(radius=cvolist[0].circle_radius,color=cvolist[0].circle_color)
            
            star = Star(outer_radius=0.15, inner_radius=0.1)
            c1name = Tex(cvolist[0].c1name).move_to(cir1.get_top()+.5)
            o1name = Tex(cvolist[0].o1name).next_to(star).scale(0.5)

            self.play(Create(cir1,run_time=2),Create(c1name,run_time=2))
            
            self.play(Create(o1name),Create(star))
            self.wait(2)
        
# if __name__ == "__main__":
#     p1=cvo.CVO().CreateCVO("John","36","Person","Age")
#     cvolist=[p1]
#     scene = C1Anim()
#     scene.construct(cvolist)
#     # scene.construct(cvo=p1)
#     scene.render()