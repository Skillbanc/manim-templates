from manim import *
from AbstractAnim import AbstractAnim
import cvo

class Grade6Chapter2WholenumbersTopic2(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.Addition()
        self.fadeOutCurrentScene()
        self.Subtraction()
        self.fadeOutCurrentScene()
        self.Multiplication()
        self.fadeOutCurrentScene()
        self.Division()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

    def Introduction(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [-TAU/3]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Whole Numbers","")
        p11=cvo.CVO().CreateCVO("Operations", "")
        p11.extendOname([" Addition"," Subtraction"," Multiplication"," Division"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def Addition(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Addition of Whole Numbers","X+Y")
        p11=cvo.CVO().CreateCVO("X variable","2")
        p12=cvo.CVO().CreateCVO("Y variable","3")
        p13=cvo.CVO().CreateCVO("Sum", "5")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()

    def Subtraction(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Subtraction of Whole Numbers","X-Y")
        p11=cvo.CVO().CreateCVO("X variable","3")
        p12=cvo.CVO().CreateCVO("Y variable","2")
        p13=cvo.CVO().CreateCVO("Difference", "1")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()

    def Multiplication(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Multiplication of Whole Numbers","X*Y")
        p11=cvo.CVO().CreateCVO("X variable","2")
        p12=cvo.CVO().CreateCVO("Y variable","3")
        p13=cvo.CVO().CreateCVO("Product", "6")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()

    def Division(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Division of Whole Numbers","X/Y")
        p11=cvo.CVO().CreateCVO("X variable","8")
        p12=cvo.CVO().CreateCVO("Y variable","2")
        p13=cvo.CVO().CreateCVO("Quotient", "4")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()
        
    def SetDeveloperList(self): 
       self.DeveloperList="Medha Masanam" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade6Chapter2WholenumbersTopic2.py"
    


if __name__ == "__main__":
    scene = Grade6Chapter2WholenumbersTopic2()
    scene.render()