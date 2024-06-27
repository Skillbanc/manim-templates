

from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo


class propexam(AbstractAnim):
    
    
    def construct(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("Properties","Examples").setPosition([0,2.5,0])
         p11=cvo.CVO().CreateCVO("closure","integer+integer=integer  :10+15=25").setPosition([4,2,0])
         p12=cvo.CVO().CreateCVO("Commutative ","a+b=b+a (or) a*b=b*a :2*3=3*2").setPosition([5,-2,0])
         p13=cvo.CVO().CreateCVO("Associative","a+(b+c)=(a+b)+c (or) a*(b*c)=(a*b)*c :2*(3*4)=(2*3)*4").setPosition([-4,2,0]).setangle(-TAU/4)
         p14=cvo.CVO().CreateCVO("Distributive","a*(b+c)=(a*b)+(a*c) (or) a*(b-c)=a*b-a*c").setPosition([-4,0,0]).setangle(-TAU/4)
         p10.cvolist.append(p12)
         
         p10.cvolist.append(p11)
         p10.cvolist.append(p13)
         p10.cvolist.append(p14)
         
         self.construct1(p10,p10)
         

      
if __name__ == "__main__":
    scene = propexam()
    scene.render()