from manim import *
from AbstractAnim import AbstractAnim
import cvo

class propanim(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.direct()
        self.fadeOutCurrentScene()
        self.inverse()
        self.SourceReference

        

    def Introduction(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [-TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("PROPORTIONS","")
        p11=cvo.CVO().CreateCVO("TYPES", "")
        p11.extendOname(["DIRECT","INVERSE"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def direct(self):
        self.setNumberOfCirclePositions(5)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("DIRECT PROPORTION","x/y=k \n and\n x=ky")
        p11=cvo.CVO().CreateCVO("X variable","4")
        p12=cvo.CVO().CreateCVO("Y variable","2")
        p14=cvo.CVO().CreateCVO("K variable","2")
        p13=cvo.CVO().CreateCVO("Proportion\n", "x=ky => 4=2(2)")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p14)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)),Create(CurvedArrow(p14.pos,p13.pos)))

    def inverse(self):
        self.setNumberOfCirclePositions(5)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("INVERSE PROPORTION","x=k/y\n and\n xy=k")
        p11=cvo.CVO().CreateCVO("X variable","2")
        p12=cvo.CVO().CreateCVO("Y variable","2")
        p14=cvo.CVO().CreateCVO("K variable","4")
        p13=cvo.CVO().CreateCVO("Proportion\n", "xy=k => 2(2)=4")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p14)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)),Create(CurvedArrow(p14.pos,p13.pos)))  
        
        
        
    def SourceReference(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("SOURCE CODE REFERENCE","").setPosition([0,3,0])
        p12=cvo.CVO().CreateCVO("GITHUB URL","https://github.com/Skillbanc/manim-templates.git").setPosition([4,0,0])
        p13=cvo.CVO().CreateCVO("FILE NAME", "propanim.py").setPosition([4,0,0])
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p12.setcircleradius(3)
        p13.setcircleradius(2)
        self.construct1(p10,p10)
        self.construct1(p13,p13)  


if __name__ == "__main__":
    scene = propanim()
    scene.render()