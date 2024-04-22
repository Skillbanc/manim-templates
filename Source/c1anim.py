from manim import *
from numpy import size

import cvo

class C1Anim(Scene):
    cvo = cvo.CVO()
    def construct(self):
        cir1 = Circle(radius=self.cvo.circle_radius,color=self.cvo.circle_color)
        
        star = Star(inner_radius=.05)
        c1name = Tex(self.cvo.c1name).move_to(cir1.get_top()+.5)
        o1name = Tex(self.cvo.o1name).next_to(star).scale(0.5)

        self.play(Create(cir1,run_time=2),Create(c1name,run_time=2))
        
        self.play(Create(o1name),Create(star))
        self.wait(2)
        
if __name__ == "__main__":
    p1=cvo.CVO()
    p1.CreateCVO("John","36","Person","Age")
        
    scene = C1Anim()
    scene.cvo = p1
    # scene.construct(cvo=p1)
    scene.render()