
from manim import *
from AbstractAnim import AbstractAnim
import cvo

class Grade8Chapter15PlayingWithNumbersTopic6(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.DivisibilityRule10()
        self.fadeOutCurrentScene()
        self.DivisibilityRule11()
        self.fadeOutCurrentScene()
        self.DivisibilityRule12()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        

   
    def Introduction(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [-TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Playing With Numbers","")
        p11=cvo.CVO().CreateCVO("Divisibility Rules", "")
        p11.extendOname(["10","11","12"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)


    def DivisibilityRule10(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Divisibility Rule 10","units place- 0 ")
        p11=cvo.CVO().CreateCVO("example","50")
        p12=cvo.CVO().CreateCVO("units digit ","0")
        p13=cvo.CVO().CreateCVO("Divisibility Rule of 10", "satisfied")
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        self.construct1(p10,p10)
        #self.construct1(p13,p13)
        #self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play() 

    

    def DivisibilityRule11(self):
        self.setNumberOfCirclePositions(5)
        #self.angleChoice = [0,0,0]
        #self.isRandom = False

        p10=cvo.CVO().CreateCVO("Divisibility Rule 11","$sum of odd place-sum of even place =divisible by 11$")
        p11=cvo.CVO().CreateCVO("example","11")
        p12=cvo.CVO().CreateCVO("$sum of odd place-sum of even place$","$1-1=0$")
        p13=cvo.CVO().CreateCVO("Divisibile by 11", "0 is divisble by 11")
        p14=cvo.CVO().CreateCVO("Divisibility Rule of 11", "satisfied")
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        p13.cvolist.append(p14)
        self.construct1(p10,p10)
        #self.construct1(p13,p13)
        #self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()

    def DivisibilityRule12(self):
        self.setNumberOfCirclePositions(7)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Divisibility Rule 12","both by 4 and 3").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("example","24").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("last 2 digits","24(divisible)").setPosition([4,0,0]).setangle(-TAU/4)
        p13=cvo.CVO().CreateCVO("Divisibility Rule of 4", "satisfied").setPosition([4,-2,0]).setangle(-TAU/4)
        p14=cvo.CVO().CreateCVO("sum of digits ","2+4=6").setPosition([-4,2,0]).setangle(-TAU/4)
        p15=cvo.CVO().CreateCVO("Divisibility Rule of 3", "satisfied").setPosition([-4,-2,0]).setangle(-TAU/4)
        p16=cvo.CVO().CreateCVO("Divisibility Rule of 12", "satisfied").setPosition([0,-2.5,0])
        p10.cvolist.append(p11)
        p11.cvolist.append(p14)
        p14.cvolist.append(p15)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        self.construct1(p10,p10)
        self.construct1(p16,p16)
        self.play(Create(CurvedArrow(p13.pos,p16.pos)),Create(CurvedArrow(p15.pos,p16.pos)))
        #self.play()

    def SetDeveloperList(self): 
       self.DeveloperList="Medha Masanam" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade8Chapter15PlayingWithNumbersTopic6.py"

 


if __name__ == "__main__":
    scene = Grade8Chapter15PlayingWithNumbersTopic6()
    scene.render()