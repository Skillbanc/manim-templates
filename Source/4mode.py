from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo


class mode(AbstractAnim):
    
    
    def construct(self):
        self.constructDataByCVO()
        self.fadeOutCurrentScene()
    def constructDataByCVO(self):
        self.isRandom=False
         
        p1=cvo.CVO().CreateCVO("Mode","").setPosition([0,2,0])
        p2=cvo.CVO().CreateCVO("Definition","The most frequently occurring value").setPosition([-3,0,0])  
        p3=cvo.CVO().CreateCVO("note:","There may be 2 or 3 or many modes for the same data.").setPosition([3,-1.5,0])
    
        p1.cvolist.append(p2)
        p1.cvolist.append(p3)
        self.construct1(p1,p1)
         
if __name__ == "__main__":
    scene = mode()
    scene.render()