
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class graph_rep(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.constructDataByCVO()
    def constructDataByCVO(self):
        self.isRandom=False
        p1=cvo.CVO().CreateCVO("Graphical representation of Data","Bar Graphs").setPosition([0,2.5,0])
        p2=cvo.CVO().CreateCVO("Vertical Bars","Bars are parallel to y-axis").setPosition([-5,0,0])
        p3=cvo.CVO().CreateCVO("Horizontal Bars","Bars are parallel tp x-axis").setPosition([5,0,0])
        p1.cvolist.append(p2)
        p1.cvolist.append(p3)
       

        self.construct1(p1,p1)
        self.fadeOutCurrentScene()
      
if __name__ == "__main__":
    scene =graph_rep()
    scene.render()
