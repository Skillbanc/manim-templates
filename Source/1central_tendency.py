from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class central_tendency(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.constructDataByCVO()
        self.fadeOutCurrentScene()
    def constructDataByCVO(self):
        self.isRandom=False
        p1=cvo.CVO().CreateCVO("Basic Measures Of Central Tendency","").setPosition([0,2.5,0])
        p2=cvo.CVO().CreateCVO("Measure 1","Arithmetic Mean").setPosition([-5,0,0])
        p3=cvo.CVO().CreateCVO("Measure 2","Median").setPosition([0,-2,0])
        p4=cvo.CVO().CreateCVO("Measure 3","Mode").setPosition([5,0,0])

        p1.cvolist.append(p2)
        p1.cvolist.append(p3)
        p1.cvolist.append(p4)        

        self.construct1(p1,p1)
         
if __name__ == "__main__":
    scene = central_tendency()
    scene.render()