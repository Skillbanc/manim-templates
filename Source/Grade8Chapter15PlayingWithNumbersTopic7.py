from manim import *
from AbstractAnim import AbstractAnim
import cvo

class Grade8Chapter15PlayingWithNumbersTopic7(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.Example()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        
        
    def Introduction(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Playing With Numbers","Puzzles with Missing Digits")
        p11=cvo.CVO().CreateCVO("Step 1","Each letter of the puzzle must stand for just one digit")
        p12=cvo.CVO().CreateCVO("Step 2","The digit with highest place value of the number can not be zero")
        p13=cvo.CVO().CreateCVO("Step 3", "Only one solution")
        
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        self.construct1(p10,p10)
        #self.construct1(p13,p13)
        #self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()
    

    def Example(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Example","$17A + 2A4 = 407$")
        p11=cvo.CVO().CreateCVO("Step 1(units place)","$A + 4 = 7$")
        p12=cvo.CVO().CreateCVO("Step 2","$A = 7-4 = 3$")
        p13=cvo.CVO().CreateCVO("Solution", "$173 + 234 = 407$")
        p10.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        self.construct1(p10,p10)
        # self.construct1(p13,p13)
        #self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()
    def SetDeveloperList(self): 
       self.DeveloperList="Medha Masanam" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade8Chapter15PlayingWithNumbersTopic7.py"
  

if __name__== "__main__":
    scene = Grade8Chapter15PlayingWithNumbersTopic7()
    scene.render()