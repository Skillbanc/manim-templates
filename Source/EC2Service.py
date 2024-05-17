from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo


class EC2Service(AbstractAnim):
    
    
    def construct(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("AWS Services","EC2").setPosition([0,2.5,0])
         p11=cvo.CVO().CreateCVO("EC2 Instances","WebServerInstance").setPosition([4,2,0])
         p12=cvo.CVO().CreateCVO("Security Groups","WebServerSecurityGroup").setPosition([5,-2,0])
         p13=cvo.CVO().CreateCVO("Storage","EBS").setPosition([-4,2,0]).setangle(-TAU/4)
         p14=cvo.CVO().CreateCVO("Elastic Ip","Standard Elastic IP Address:").setPosition([-4,0,0]).setangle(-TAU/4)
         
         
         
         p10.cvolist.append(p11)
         p10.cvolist.append(p12)
         p10.cvolist.append(p13)
         p10.cvolist.append(p14)
         
         
         self.construct1(p10,p10)
         

      
if __name__ == "__main__":
    scene = EC2Service()
    scene.render()