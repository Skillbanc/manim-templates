

from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo


class properties(AbstractAnim):
    
    
    def construct(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("Properties","4types").setPosition([0,2.5,0])
         p11=cvo.CVO().CreateCVO("closure","Result of mathematical operation on operands\n belongs to the same group of operands").setPosition([3 ,1,0])
         p12=cvo.CVO().CreateCVO("Commutative ","It ststes that we can swap numbers over and still get the same answer").setPosition([3,-2,0])
         p13=cvo.CVO().CreateCVO("Associative","It states that the result remains the same regardless of how the numbers are grouped").setPosition([-3,-2,0]).setangle(-TAU/4)
         p14=cvo.CVO().CreateCVO("Distributive","a*(b+c)=(a*b)+(a*c)").setPosition([-4,0,0]).setangle(-TAU/4)
         p10.cvolist.append(p12)
         
         p10.cvolist.append(p11)
         p10.cvolist.append(p13)
         p10.cvolist.append(p14)
         
         self.construct1(p10,p10)
         

      
if __name__ == "__main__":
    scene = properties()
    scene.render()