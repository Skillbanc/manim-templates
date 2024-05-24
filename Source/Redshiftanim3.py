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


class Redshiftanim3(AbstractAnim):
    
    
    def construct(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("Components of RedshiftCluster","").setPosition([0,2.5,0])
         p11=cvo.CVO().CreateCVO("LeaderNode","").setPosition([4,2.5,0]).setangle(TAU/4)
         p12=cvo.CVO().CreateCVO("ComputeNode","").setPosition([4,0,0]).setangle(TAU/3)
         p13=cvo.CVO().CreateCVO("NodeSlices","").setPosition([4,-2.5,0]).setangle(-TAU/4)
         p14=cvo.CVO().CreateCVO("ClusterStorage","").setPosition([-4,2.5,0]).setangle(-TAU/4)
         p15=cvo.CVO().CreateCVO("SystemTables","").setPosition([-4,0,0]).setangle(-TAU/4)
         p16=cvo.CVO().CreateCVO("WorkLoadManagement","").setPosition([-4,-2.5,0]).setangle(-TAU/4)
         p10.cvolist.append(p11)
         
         p10.cvolist.append(p12)
         p10.cvolist.append(p13)
         p10.cvolist.append(p14)
         p10.cvolist.append(p15)
         p10.cvolist.append(p16)
         
         self.construct1(p10,p10)
         

      
if __name__ == "__main__":
    scene = Redshiftanim3()
    scene.render()