
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class cumulative_frequency(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.constructDataByCVO()
        self.fadeOutCurrentScene()
    def constructDataByCVO(self):
        self.isRandom=False
        p1=cvo.CVO().CreateCVO("Cumulative Frequency","").setPosition([0,2.5,0])
        p2=cvo.CVO().CreateCVO("Lesser than C.F","Adding the frequencies from bottom").setPosition([-5,0,0])
        p3=cvo.CVO().CreateCVO("Greater than C.F","Adding the frequencies from the top").setPosition([5,0,0])
        p1.cvolist.append(p2)
        p1.cvolist.append(p3)
       

        self.construct1(p1,p1)
        self.fadeOutCurrentScene()
      
if __name__ == "__main__":
    scene =cumulative_frequency()
    scene.render()
