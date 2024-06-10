
from manim import *
from AbstractAnim import AbstractAnim
import cvo

class DivisibilityRules1(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.DivisibilityRule2()
        self.fadeOutCurrentScene()
        self.DivisibilityRule3()
        self.fadeOutCurrentScene()
        self.DivisibilityRule4()
        self.fadeOutCurrentScene()
        self.DivisibilityRule5()

    def Introduction(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [-TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Playing With Numbers","")
        p11=cvo.CVO().CreateCVO("Divisibility Rules", "")
        p11.extendOname(["2","3","4","5"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def DivisibilityRule2(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Divisibility Rule 2","Units Place-2,4,6,8,0")
        p11=cvo.CVO().CreateCVO("example","28")
        p12=cvo.CVO().CreateCVO("units place","8")
        p13=cvo.CVO().CreateCVO("Divisibility Rule of 2", "satisfied")
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        self.construct1(p10,p10)
        #self.construct1(p13,p13)
        #self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()

    def DivisibilityRule3(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Divisibility Rule 3","sum of digits divisible by 3")
        p11=cvo.CVO().CreateCVO("example","12")
        p12=cvo.CVO().CreateCVO("sum of digits","3")
        p13=cvo.CVO().CreateCVO("Divisibility Rule of 3", "satisfied")
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        self.construct1(p10,p10)
        #self.construct1(p13,p13)
        #self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()

    def DivisibilityRule4(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Divisibility Rule 4","last 2 digits divisible by 4")
        p11=cvo.CVO().CreateCVO("example","116")
        p12=cvo.CVO().CreateCVO("last 2 digits ","16")
        p13=cvo.CVO().CreateCVO("Divisibility Rule of 4", "satisfied")
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        self.construct1(p10,p10)
        #self.construct1(p13,p13)
        #self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()

    def DivisibilityRule5(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Divisibility Rule 5","units place- 0 or 5")
        p11=cvo.CVO().CreateCVO("example","45")
        p12=cvo.CVO().CreateCVO("units digit ","5")
        p13=cvo.CVO().CreateCVO("Divisibility Rule of 5", "satisfied")
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        self.construct1(p10,p10)
        #self.construct1(p13,p13)
        #self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()
        
    


if __name__ == "__main__":
    scene = DivisibilityRules1()
    scene.render()