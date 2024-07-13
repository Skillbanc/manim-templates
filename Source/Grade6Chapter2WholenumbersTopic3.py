from manim import *
from AbstractAnim import AbstractAnim
import cvo

class Grade6Chapter2WholenumbersTopic3(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.CommutativityofAddition()
        self.fadeOutCurrentScene()
        self.CommutativityofMultiplication()
       
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

    def Introduction(self):
        self.setNumberOfCirclePositions(3)
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Whole Numbers","Properties").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Commutative Property of Addition","").setPosition([2,0,0])
        p12=cvo.CVO().CreateCVO("Commutative Property of Multiplication","").setPosition([-2,-2,0])
        
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
     
        self.construct1(p10,p10)
        #self.construct1(p13,p13)
        #self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()


    def CommutativityofAddition(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Commutative Property of Addition","X+Y=Y+X")
        p11=cvo.CVO().CreateCVO("X variable","2")
        p12=cvo.CVO().CreateCVO("Y variable","3")
        p13=cvo.CVO().CreateCVO("Sum", "2+3=3+2==5")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()

    def CommutativityofMultiplication(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Commutative Property of Multiplication","X*Y=Y*X")
        p11=cvo.CVO().CreateCVO("X variable","2")
        p12=cvo.CVO().CreateCVO("Y variable","3")
        p13=cvo.CVO().CreateCVO("Product", "2*3=3*2==6")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()

        
    def SetDeveloperList(self): 
       self.DeveloperList="Medha Masanam" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade6Chapter2WholenumbersTopic3.py"
    


if __name__ == "__main__":
    scene = Grade6Chapter2WholenumbersTopic3()
    scene.render()