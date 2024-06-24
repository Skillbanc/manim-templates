import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo
class constoftri(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()  
        self.constructoftri()
        self.fadeOutCurrentScene()
        self.threes()
        self.fadeOutCurrentScene()
        self.twosonea()
        self.fadeOutCurrentScene()
        self.onestwoa()
        self.fadeOutCurrentScene()
        self.oneratwos()
    def constructoftri(self):
        self.isRandom = False
        self.positionChoice = [[0,0,0],[-4,2,0],[4,2,0],[-4,-2,0],[4,-2,0]]
        p10=cvo.CVO().CreateCVO("Mathematics","Construction of Triangle")
        p11=cvo.CVO().CreateCVO("Constructed using 3sides","s-s-s")
        p12=cvo.CVO().CreateCVO("Constructed using 2sides,1angle","s-a-s")
        p13=cvo.CVO().CreateCVO("Constructed using 1side,2angle","a-s-a")
        p14=cvo.CVO().CreateCVO("Constructed using 1right-angle,2sides","r-s-s")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        self.construct1(p10,p10)
        

    def threes(self):
        self.isRandom = False
        self.positionChoice = [[0,0,0],[-4,2,0],[4,2,0],[-4,-2,0],[4,-2,0]]
        a10=cvo.CVO().CreateCVO("Constructing a Traingle using 3sides","4cm,5cm,6cm")
        a11=cvo.CVO().CreateCVO("Select a Side","say 4cm")
        a12=cvo.CVO().CreateCVO("Draw an Arc from starting point","taking 5cm")
        a13=cvo.CVO().CreateCVO("Do the same thing from other end","taking 6cm")
        a14=cvo.CVO().CreateCVO("Combine all lines","Trinagle is formed")
        a10.cvolist.append(a11)
        a10.cvolist.append(a12)
        a10.cvolist.append(a13)
        a10.cvolist.append(a14)
        self.construct1(a10,a10) 

    def twosonea(self):
        self.isRandom = False
        self.positionChoice = [[0,0,0],[-4,2,0],[4,2,0],[-4,-2,0],[4,-2,0]]
        r10=cvo.CVO().CreateCVO("Constructing a Traingle using 2sides and 1angle","4cm,5cm,50")
        r11=cvo.CVO().CreateCVO("draw a lineseg","take 4cm")
        r12=cvo.CVO().CreateCVO("make a ray from the starting of the line","50")
        r13=cvo.CVO().CreateCVO("draw a line from other end to the ray","take 5cm")
        r14=cvo.CVO().CreateCVO("connect lines","traingle is formed")
        r10.cvolist.append(r11)
        r10.cvolist.append(r12)
        r10.cvolist.append(r13)
        r10.cvolist.append(r14)
        self.construct1(r10,r10) 

    def onestwoa(self):
        self.isRandom = False
        self.positionChoice = [[0,0,0],[-4,2,0],[4,2,0],[-4,-2,0],[4,-2,0]]
        m1=cvo.CVO().CreateCVO("Construction of Triangle with 1side and 2angles","4cm,50,110")
        m2=cvo.CVO().CreateCVO("draw a lineseg","of 4cm")
        m3=cvo.CVO().CreateCVO("make a ray from beginning of line","50")
        m4=cvo.CVO().CreateCVO("make a ray from end of line","110")
        m5=cvo.CVO().CreateCVO("connect lines","triangle is formed")
        m1.cvolist.append(m2)
        m1.cvolist.append(m3)
        m1.cvolist.append(m4)
        m1.cvolist.append(m5)
        self.construct1(m1,m1)

    def oneratwos(self):
        self.isRandom = False
        self.positionChoice = [[0,0,0],[-4,2,0],[4,2,0],[-4,-2,0],[4,-2,0]]
        a1=cvo.CVO().CreateCVO("Construction of Triangle using 1rightangle and hypotenuse sides","4cm,6cm,90")
        a2=cvo.CVO().CreateCVO("draw a lineseg","of 4cm")
        a3=cvo.CVO().CreateCVO("make a ray","90")
        a4=cvo.CVO().CreateCVO("draw a line from other end of lineseg","take 6cm")
        a5=cvo.CVO().CreateCVO("connect lines","triangle is formed")
        a1.cvolist.append(a2)
        a1.cvolist.append(a3)
        a1.cvolist.append(a4)
        a1.cvolist.append(a5)
        self.construct1(a1,a1)

if __name__ == "__main__":
    scene = constoftri()
    scene.render()
