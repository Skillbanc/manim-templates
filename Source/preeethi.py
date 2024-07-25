import random  # Import the random module
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo


class Sub(AbstractAnim):
    def construct(self):
        # self.RenderSkillbancLogo()
        # self.fadeOutCurrentScene()
        self.Time()
        # self.Hour()
        # self.Minutes()
        # self.fadeOutCurrentScene()
        # self.intro()
        # self.fadeOutCurrentScene()
        # self.intro1()
        # self.fadeOutCurrentScene()
        # self.GithubSourceCodeReference()
        # self.anim()
        # self.exercise()
    def SetDeveloperList(self):  
        self.DeveloperList="Vasudha"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade1Chapter16Time.py"   
        
    # render using CVO data object
    def Time(self):
        # self.play(Write(NumberPlane()))
        # p1 = cvo.CVO().CreateCVO("example", "build 8 square").setPosition([0,2.5,0])
        # p2 = cvo.CVO().CreateCVO("lines required", "for one square lines=4").setPosition([-4,2,0])
        # p3 = cvo.CVO().CreateCVO("for m sqaures", "4 * m").setPosition([-4,-2,0])
        # p4 = cvo.CVO().CreateCVO("m ", " no of squares").setPosition([-1,-3,0])
        # p5 = cvo.CVO().CreateCVO("lines for 8 sqaures", "4*8=32").setPosition([2,-1,0])
        # p1.cvolist.append(p2)
        # p2.cvolist.append(p3)
        # p3.cvolist.append(p4)
        # p3.cvolist.append(p5)
        # p2.setcircleradius(1.5)
        # self.setNumberOfCirclePositions(5)
        # self.construct1(p1, p1 )

        
        #self.angleChoice = [0,0,0]
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Addition of RationalNumbers","X+Y")
        p11=cvo.CVO().CreateCVO("X variable","2/3").setPosition([4.5,-2.7,0])
        p12=cvo.CVO().CreateCVO("Y variable","3/4").setPosition([-3,2,0])
        p13=cvo.CVO().CreateCVO("Sum", "(2/3)+(3/4)= ((2*4)+(3*3))/(3*4) = 17  /12").setPosition([4,1.2,0])
        p13.setcircleradius(2.8)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()
        
        # p7= cvo.CVO().CreateCVO("topics", "").setPosition([1,-3,0])
        # p7onamelist=["L.H.S and R.H.S of equation","Solutions of Equation"]
        
        # p1.cvolist.append(p7)
        # p7.extendOname(p7onamelist)
        # self.isRandom=False
        # self.colorChoice=[LIGHT_PINK,ORANGE,WHITE]
        # self.angleChoice = [TAU/4,TAU/4,TAU/4]
        # self.positionChoice = [[-4, -1, 0], [4, -1, 0], [0, 2, 0], [-4, 1, 0]] 
        # p3=cvo.CVO().CreateCVO("example","").setPosition([0,2.5,0])
        # p4=cvo.CVO().CreateCVO("","").setPosition([4,2,0])
        # p4onamelist=["Price=34000","price increased=20\%"]
        # p5=cvo.CVO().CreateCVO("answer using unitary","")
        # p5onamelist=["$20\% of 100=120$","$rs.1=120/100$","$rs.3400=(120/100)*3400=40,800$"]
        # p6=cvo.CVO().CreateCVO("answer using normal","")
        # p6onamelist=["$20\% of 34000=6800$","$increased price=34000+6800=40,800$"]
        # p3.cvolist.append(p4)
        # p4.extendOname(p4onamelist)
        # p4.cvolist.append(p5)
        # p5.extendOname(p5onamelist)
        # p4.cvolist.append(p6)
        # p6.extendOname(p6onamelist)
        # self.setNumberOfCirclePositions(4)
        # p4.setcircleradius(1.5)
        # p5.setcircleradius(2)
        # p6.setcircleradius(2)
       
       

        # p1 = cvo.CVO().CreateCVO("variable", "denoted by small letters").setPosition([-5,-3,0])
        # p2 = cvo.CVO().CreateCVO("letters", "a,b,c,d,......z").setPosition([-1,-3,0])
        # p1.cvolist.append(p2)
        # p1.setcircleradius(1.5)
        # self.setNumberOfCirclePositions(2)
        # self.construct1(p1, p1 )
        # p3 = cvo.CVO().CreateCVO("4 * no.of squares", "4 * m = 4m").setPosition([-1,-1,0])
        # p4 = cvo.CVO().CreateCVO("m ", "is a variable").setPosition([-3,-3,0])
        # p3.cvolist.append(p4)
        # p1.setcircleradius(1.5)
        # self.setNumberOfCirclePositions(2)
        # self.construct1(p3, p3 )
if __name__ == "__main__":
    scene = Sub()
    scene.render()