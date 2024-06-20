import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class AxiomsAnim(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.constructDataByCVO()
        self.RenderSkillbancLogo()
        
    # render using CVO data object
    def constructDataByCVO(self):
        p10=cvo.CVO().CreateCVO("mathematics","AXIOMS")
        p11=cvo.CVO().CreateCVO("","a+b=b+a")
        p12=cvo.CVO().CreateCVO("","a*b=b*a")
        p13=cvo.CVO().CreateCVO("","a+0=a")
        p14=cvo.CVO().CreateCVO("","a*1=a")
        p15=cvo.CVO().CreateCVO("","a*0=0")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)


        self.construct1(p10,p10)
    
   


if __name__ == "__main__":
    scene = AxiomsAnim()
    scene.render()
    