from manim import *
from AbstractAnim import AbstractAnim
import cvo

class add(AbstractAnim):

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
        # self.ending()

    def Introduction(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [-TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Rational Numbers","")
        p11=cvo.CVO().CreateCVO("Operations", "")
        p11.extendOname(["Addition","Subtraction","Multiplication","Division"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def Addition(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Addition of RationalNumbers","X+Y")
        p11=cvo.CVO().CreateCVO("X variable","2/3")
        p12=cvo.CVO().CreateCVO("Y variable","3/4")
        p13=cvo.CVO().CreateCVO("Sum", "(2*4)/3+(3*3)/4 = 17/12")
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

        p10=cvo.CVO().CreateCVO("Subtraction of Rational Numbers","x-y")
        p11=cvo.CVO().CreateCVO("Variable x","4/3")
        p12=cvo.CVO().CreateCVO("Variable y","3/3")
        p13=cvo.CVO().CreateCVO("Difference", "(4-3)/3 = 1/3")
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

        p10=cvo.CVO().CreateCVO("Multiplication of Rational Numbers","X*Y")
        p11=cvo.CVO().CreateCVO("X variable","2/3")
        p12=cvo.CVO().CreateCVO("Y variable","3/4")
        p13=cvo.CVO().CreateCVO("Product", "2*3/3*4 = 6/12")
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

        p10=cvo.CVO().CreateCVO("Division of Rational numbers","X / Y")
        p11=cvo.CVO().CreateCVO("x","(1/2)")
        p12=cvo.CVO().CreateCVO("Y","(5/2)")
        p13=cvo.CVO().CreateCVO("Answer", "1*5/2*2 = 5/4")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
       
    def ending(self):
        self.setNumberOfCirclePositions(3)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p8=cvo.CVO().CreateCVO("GITHUB SOURCECODE LINK","")
        p9=cvo.CVO().CreateCVO("File name","add.py")
        p7=cvo.CVO().CreateCVO("Github Url","https://github.com/Skillbanc")
       
        p8.cvolist.append(p9)
        p8.cvolist.append(p7)
        self.construct1(p8,p8)

        #self.play()

if __name__ == "__main__":
    scene =add()
    scene.render()