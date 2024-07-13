from manim import *
from AbstractAnim import AbstractAnim
import cvo

class Grade6Chapter2WholenumbersTopic4(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        
        self.fadeOutCurrentScene()
        self.AssociativityofAddition()
        self.fadeOutCurrentScene()
        self.AssociativityofMultiplication()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

    def Introduction(self):
        self.setNumberOfCirclePositions(5)
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Whole Numbers","Properties")
        
        p11=cvo.CVO().CreateCVO("Associative Property of Addition","")
        p12=cvo.CVO().CreateCVO("Associative Property of Multiplication","")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        """p10.cvolist.append(p13)
        p10.cvolist.append(p14)"""
        self.construct1(p10,p10)
        #self.construct1(p13,p13)
        #self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()


    def AssociativityofAddition(self):
        self.setNumberOfCirclePositions(6)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Associative Property of Addition","X+(Y+Z)=(X+Y)+Z").setPosition([-4,2,0])
        p11=cvo.CVO().CreateCVO("X variable","2").setPosition([5,2,0])
        p12=cvo.CVO().CreateCVO("Y variable","3").setPosition([-2,0,0])
        p13=cvo.CVO().CreateCVO("Z variable","1").setPosition([-3,-3,0])
        p14=cvo.CVO().CreateCVO("Sum", "2+(3+1)=(3+2)+1==6").setPosition([4,-2,0])
        #p15=cvo.CVO().CreateCVO("Solution", "6").setPosition([2,-2,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        #p14.cvolist.append(p15)
        self.construct1(p10,p10)
        self.construct1(p14,p14)
        self.play(Create(CurvedArrow(p11.pos,p14.pos)),Create(CurvedArrow(p12.pos,p14.pos)),Create(CurvedArrow(p13.pos,p14.pos)))
        
        #self.play()

    def AssociativityofMultiplication(self):
        self.setNumberOfCirclePositions(6)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Associative Property of Multiplication","X*(Y*Z)=(X*Y)*Z").setPosition([-4,2,0])
        p11=cvo.CVO().CreateCVO("X variable","2").setPosition([5,2,0])
        p12=cvo.CVO().CreateCVO("Y variable","3").setPosition([-2,0,0])
        p13=cvo.CVO().CreateCVO("Z variable","1").setPosition([-3,-3,0])
        p14=cvo.CVO().CreateCVO("Sum", "2*(3*1)=(3*2)*1==6").setPosition([4,-2,0])
        #p15=cvo.CVO().CreateCVO("Solution", "6")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.construct1(p10,p10)
        self.construct1(p14,p14)
        self.play(Create(CurvedArrow(p11.pos,p14.pos)),Create(CurvedArrow(p12.pos,p14.pos)),Create(CurvedArrow(p13.pos,p14.pos)))
        #   p14.cvolist.append(p15)
        
    def SetDeveloperList(self): 
       self.DeveloperList="Medha Masanam" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade6Chapter2WholenumbersTopic4.py"
    


if __name__ == "__main__":
    scene = Grade6Chapter2WholenumbersTopic4()
    scene.render()