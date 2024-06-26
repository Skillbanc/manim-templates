

from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo


class rules(AbstractAnim):
    
    
    def construct(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("Rules","").setPosition([0,2.5,0])
         p11=cvo.CVO().CreateCVO("Additive identity or zero rule","Any number+0 = 0+Any number").setPosition([3 ,1,0])
         p12=cvo.CVO().CreateCVO("Multiplicative identity (or) Rule of1"," Any number*1 = 1*Any number").setPosition([3,-2,0])
         p13=cvo.CVO().CreateCVO("Multiplicative Inverse (or Reciprocal)","a/b is multiplicative inverse of c/b or vise versa").setPosition([-3,-2,0]).setangle(-TAU/4)
         p10.cvolist.append(p12)
         
         p10.cvolist.append(p11)
         p10.cvolist.append(p13)
        
         
         self.construct1(p10,p10)
         

      
if __name__ == "__main__":
    scene = rules()
    scene.render()