
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class RDSServiceAnimation(AbstractAnim):
    
    def construct(self):
        #  p1=cvo.CVO().CreateCVO("cname","oname")
        
         p10=cvo.CVO().CreateCVO("AWS Service","RDS Service")
         
         
         self.construct1(p10,p10)
      
if __name__ == "__main__":
    
    scene = RDSServiceAnimation()
    scene.render()
    