from manim import *
from AbstractAnim import AbstractAnim
import cvo

class snehithanim(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.Direct()
        self.fadeOutCurrentScene()
        

    def Introduction(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [-TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Proportions","")
        p11=cvo.CVO().CreateCVO("Types", "")
        p11.extendOname(["Direct","Inverse"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)
    
    def Direct(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Direct Propotion","")
        p11=cvo.CVO().CreateCVO("X variablea","x")
        p12=cvo.CVO().CreateCVO("Y variable","y")
        p13=cvo.CVO().CreateCVO("for direct proportion", "x=ky")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()

if __name__ == "__main__":
    scene = snehithanim()
scene.render()