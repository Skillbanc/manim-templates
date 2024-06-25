import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo

class MixedFractions(AbstractAnim):
    def construct(self):
        self.Example()
    def Example(self):
        p10=cvo.CVO().CreateCVO("Mixed Fractions ","").setPosition([-2,2.5,0])
        #p11=cvo.CVO().CreateCVO("Defination  ", "A fraction that has both a whole number and a fractional part").setPosition([0,1,0])
        p12=cvo.CVO().CreateCVO("Example",r"$(2\frac{3}{4})$").setPosition([0,1,0])
        p13=cvo.CVO().CreateCVO("Whole Number ", "$2$").setPosition([3,0,0])
        p14=cvo.CVO().CreateCVO("Fraction Part  ", r"$\frac{3}{4}$").setPosition([-3,-1.5,0])

       
        #p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p12.cvolist.append(p13)
        p12.cvolist.append(p14)
        self.construct1(p10,p10)

if __name__ == "__main__":
    scene = MixedFractions()
    scene.render()
