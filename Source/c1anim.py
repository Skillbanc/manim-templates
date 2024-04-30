# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla

from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class C1Anim(AbstractAnim):
    
    def construct(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         #p10=cvo.CVO().CreateCVO("Person","John Doe").setPosition([0,2.5,0]).setangle(TAU/4)
         p10=cvo.CVO().CreateCVO("AWS Service","IAM Service")#.setPosition([0,2.5,0]).setangle(TAU/4)
         p10.appendOname("RDS Service")
         # p11=cvo.CVO().CreateCVO("Description","Identity Access Management")
         
         # p10.cvolist.append(p11)
         # # Users in IAM service
         # p12=cvo.CVO().CreateCVO("User","John Doe")
         # p10.cvolist.append(p12)
         # User group has users
         # p13=cvo.CVO().CreateCVO("User Group","Developer")
         # p15=cvo.CVO().CreateCVO("User","Jane Doe")
         # p15.appendOname("Jack Doe")
         
         # p13.cvolist.append(p15)
         # p10.cvolist.append(p13)
         
         # # Iam service has roles
         # p14=cvo.CVO().CreateCVO("Role","Developer")
         # p10.cvolist.append(p14)
         
         self.construct1(p10,p10)
      
if __name__ == "__main__":
    scene = C1Anim()
    scene.render()
    