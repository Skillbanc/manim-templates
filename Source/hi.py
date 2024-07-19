from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo
class hi(AbstractAnim):

    def construct(self):
        self.DivisibilityRule7()
        self.fadeOutCurrentScene()


    def DivisibilityRule6(self):
        self.setNumberOfCirclePositions(8)
        self.angleChoice = [TAU/4,-TAU/4,-TAU/2,-TAU/2,-TAU/4,-TAU/4]
        self.isRandom = False

        #self.angleChoice = [0,0,0]
        #self.isRandom = False

        p10=cvo.CVO().CreateCVO("Divisibility Rule 6","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Condition","divisible by both 2 and 3").setPosition([-4,-2,0])
        p12=cvo.CVO().CreateCVO("example","30").setPosition([4,2,0])
        p13=cvo.CVO().CreateCVO("units place","0").setPosition([4,0,0])
        p14=cvo.CVO().CreateCVO("Divisibility Rule of 2?", "satisfied").setPosition([4,-2,0])
        p15=cvo.CVO().CreateCVO("sum of digits ","3+0=3(divisible)").setPosition([-4,0,0])
        p16=cvo.CVO().CreateCVO("Divisibility Rule of 3?", "satisfied").setPosition([-4,-2,0])
        p17=cvo.CVO().CreateCVO("Divisibility Rule of 6?", "satisfied").setPosition([0,-2.5,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p12.cvolist.append(p13)
        p13.cvolist.append(p14)
        p12.cvolist.append(p15)
        p12.cvolist.append(p16)
        
        self.construct1(p10,p10)
        self.construct1(p17,p17)
        self.play(Create(CurvedArrow(p14.pos,p17.pos)),Create(CurvedArrow(p16.pos,p17.pos)))


      
if __name__ == "__main__":
    scene = hi()
    scene.render()