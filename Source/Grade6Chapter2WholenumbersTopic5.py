from manim import *
from AbstractAnim import AbstractAnim
import cvo

class Grade6Chapter2WholenumbersTopic5(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.AdditiveIdentity()
        self.fadeOutCurrentScene()
        self.MultiplicativeIdentity()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

    def Introduction(self):
        self.setNumberOfCirclePositions(3)
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Whole Numbers","Properties")
        p11=cvo.CVO().CreateCVO("Additive Identity","")
        p12=cvo.CVO().CreateCVO("Multiplicative Identity","")
        
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        
        self.construct1(p10,p10)
        #self.construct1(p13,p13)
        #self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()

    def AdditiveIdentity(self):
        self.setNumberOfCirclePositions(5)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Additive Identity","Zero is called as the additive identity ")
        p11=cvo.CVO().CreateCVO("Means","Any whole number added to 0 gives the same whole number")
        p12=cvo.CVO().CreateCVO("Additive Identity of Whole Numbers","X+0=X")
        p13=cvo.CVO().CreateCVO("X variable","2")
        p14=cvo.CVO().CreateCVO("Sum", "2+0=2")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p12.cvolist.append(p13)
        p13.cvolist.append(p14)
        self.construct1(p10,p10)
        #self.construct1(p13,p13)
        #self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()

   
    def MultiplicativeIdentity(self):
        self.setNumberOfCirclePositions(5)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Multiplicative Identity","One is called as the Multiplicative identity ")
        p11=cvo.CVO().CreateCVO("Means","Any whole number multiplied with 1 gives the same whole number").setPosition([3,-2,0])
        p12=cvo.CVO().CreateCVO("Multiplicative Identity of Whole Numbers","X*1=X").setPosition([-3,2,0])
        p13=cvo.CVO().CreateCVO("X variable","2").setPosition([2,2,0])
        p14=cvo.CVO().CreateCVO("Product", "2*1=2").setPosition([4,2,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p12.cvolist.append(p13)
        p13.cvolist.append(p14)
        self.construct1(p10,p10)

     
    
        
    def SetDeveloperList(self): 
       self.DeveloperList="Medha Masanam" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade6Chapter2WholenumbersTopic5.py"
    


if __name__ == "__main__":
    scene = Grade6Chapter2WholenumbersTopic5()
    scene.render()