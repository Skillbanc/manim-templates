
from manim import *
from AbstractAnim import AbstractAnim
import cvo

class Grade8Chapter15PlayingWithNumbersTopic5(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.DivisibilityRule6()
        self.fadeOutCurrentScene()
        self.DivisibilityRule7()
        self.fadeOutCurrentScene()
        self.DivisibilityRule8()
        self.fadeOutCurrentScene()
        self.DivisibilityRule9()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        

    def Introduction(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [-TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Playing With Numbers","")
        p11=cvo.CVO().CreateCVO("Divisibility Rules", "")
        p11.extendOname(["6","7","8","9"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def DivisibilityRule6(self):
        self.setNumberOfCirclePositions(7)
        #self.angleChoice = [0,0,0]
        #self.isRandom = False

        p10=cvo.CVO().CreateCVO("Divisibility Rule 6","divisible by both 2 and 3").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("example","30").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("units place","0").setPosition([4,0,0]).setangle(-TAU/4)
        p13=cvo.CVO().CreateCVO("Divisibility Rule of 2", "satisfied").setPosition([4,-2,0]).setangle(-TAU/4)
        p14=cvo.CVO().CreateCVO("sum of digits ","3+0=3(divisible)").setPosition([-4,2,0]).setangle(-TAU/4)
        p15=cvo.CVO().CreateCVO("Divisibility Rule of 3", "satisfied").setPosition([-4,-2,0]).setangle(-TAU/4)
        p16=cvo.CVO().CreateCVO("Divisibility Rule of 6", "satisfied").setPosition([0,-2.5,0])
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        p11.cvolist.append(p14)
        p14.cvolist.append(p15)
        self.construct1(p10,p10)
        self.construct1(p16,p16)
        self.play(Create(CurvedArrow(p13.pos,p16.pos)),Create(CurvedArrow(p15.pos,p16.pos)))
        #self.play()

    def DivisibilityRule7(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Divisibility Rule 7","$unit digit*2-given number,check if divisible by 7$")
        p11=cvo.CVO().CreateCVO("example","7")
        p12=cvo.CVO().CreateCVO("$unit digit*2-given number$","$7*2=14-7=7(divisible)$")
        p13=cvo.CVO().CreateCVO("Divisibility Rule of 7", "satisfied")
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        self.construct1(p10,p10)
        #self.construct1(p13,p13)
        #self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()

    

    def DivisibilityRule8(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Divisibility Rule 8","last 3 digits divisible by 8")
        p11=cvo.CVO().CreateCVO("example","328")
        p12=cvo.CVO().CreateCVO("last 3 digits ","328(divisble by 8)")
        p13=cvo.CVO().CreateCVO("Divisibility Rule of 8", "satisfied")
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        self.construct1(p10,p10)
        #self.construct1(p13,p13)
        #self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()

        
    def DivisibilityRule9(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Divisibility Rule 9","sum of digits divisible by 9")
        p11=cvo.CVO().CreateCVO("example","27")
        p12=cvo.CVO().CreateCVO("sum of digits","7+2=9(divisible by 9)")
        p13=cvo.CVO().CreateCVO("Divisibility Rule of 9", "satisfied")
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        self.construct1(p10,p10)
        #self.construct1(p13,p13)
        #self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()
    
    def SetDeveloperList(self): 
       self.DeveloperList="Medha Masanam" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade8Chapter15PlayingWithNumbersTopic5.py"



if __name__ == "__main__":
    scene = Grade8Chapter15PlayingWithNumbersTopic5()
    scene.render()