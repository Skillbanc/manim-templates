from manim import *
from AbstractAnim import AbstractAnim
import cvo

class STA(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.mean()
        self.fadeOutCurrentScene()
        self.direct()


    def Introduction(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [-TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("STATISTICS","")
        p11=cvo.CVO().CreateCVO("MEASURES OF CENTRAL TENDENCY", "")
        p11.extendOname(["MEAN","MODE","MEDIAN"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def mean(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [-TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("MEAN","")
        p11=cvo.CVO().CreateCVO("METHODS OF MEAN", "")
        p11.extendOname(["DIRECT METHOD","ASSUMED MEAN METHOD","STEP-DEVIATON METHOD"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def direct(self):
        self.setNumberOfCirclePositions(3)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("DIRECT METHOD","\sum_ifixi /\n\sum_ifi").setPosition([0,2,0]).setcircleradius(1.5)
        p11=cvo.CVO().CreateCVO("\sum_ifixi","Sum of all the values\n of all the observations").setPosition([-5,-4,0]).setcircleradius(3)
        p12=cvo.CVO().CreateCVO("\sum_ifi","Number of observations").setPosition([5,-4,0]).setcircleradius(3)
        #p13=cvo.CVO().CreateCVO("LSA OF CUBE", "16").setPosition([4,0,0])
        p10.SetIsMathText(True)
        p11.SetIsMathText(True)
        p12.SetIsMathText(True)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        #self.construct1(p13,p13)
        #self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))

if __name__ == "__main__":
    scene = STA()
    scene.render()       