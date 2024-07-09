from manim import *
from AbstractAnim import AbstractAnim
import cvo
from numpy import size
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
        self.fadeOutCurrentScene()
        self.prop()
        self.fadeOutCurrentScene()
        self.Rules()
        self.fadeOutCurrentScene()
        self.ending()

    def Introduction(self):
        count = 0
        # starting object
        p10=cvo.CVO().CreateCVO("Rational Numbers","The numbers which can be represented in P/Q").setPosition([0,2.5,0])
        count += 1

                # 2nd c2 object
        p12=cvo.CVO().CreateCVO("Examples","1/2,10,7/2,-3/2").setPosition([3,0,0])
        count += 1
        # Level 2
        # p13=cvo.CVO().CreateCVO("Project","Manim-Templates")
        # count += 1
        # p12.cvolist.append(p13)
        
        p10.cvolist.append(p12)
        
        # Level 1 First c2 object
        p11=cvo.CVO().CreateCVO("operations",".").setPosition([-3,0,0])
        count += 1
        # Level 2 
        p14=cvo.CVO().CreateCVO("Addition","+").setPosition([-4,-2,2])
        count += 1
        p11.cvolist.append(p14)

        p15=cvo.CVO().CreateCVO("Subtraction","-").setPosition([-5.5,-2,2])
        count += 1
        p11.cvolist.append(p15)

        p16=cvo.CVO().CreateCVO("multiplication","*").setPosition([-2,-2,2])
        count += 1
        p11.cvolist.append(p16)

        p17=cvo.CVO().CreateCVO("Division","/").setPosition([0,-2,2])
        count += 1
        p11.cvolist.append(p17)
        
        p10.cvolist.append(p11)
            


        # p13=cvo.CVO().CreateCVO("topics","role of 0,role of 1,\nclosure,\nassociative,\n distributive,\ncommutative")
        # count += 1
        # p10.cvolist.append(p13)
        
        self.setNumberOfCirclePositions(count)
       
       
        self.construct1(p10,p10)

    # def ending(self):
    #     self.setNumberOfCirclePositions(3)
    #     #self.angleChoice = [0,0,0]
    #     self.isRandom = False

    #     p8=cvo.CVO().CreateCVO("GITHUB SOURCECODE LINK","")
    #     p9=cvo.CVO().CreateCVO("File name","add.py")
    #     p7=cvo.CVO().CreateCVO("Github Url","https://github.com/Skillbanc")
       
    #     p8.cvolist.append(p9)
    #     p8.cvolist.append(p7)
    #     self.construct1(p8,p8)
   

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

    def prop(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("Properties","").setPosition([0,2.5,0])
         p11=cvo.CVO().CreateCVO("closure","Result of mathematical operation on operands\n belongs to the same group of operands").setPosition([3 ,1,0])
         p12=cvo.CVO().CreateCVO("Commutative ","a+b=b+a (or) a*b=b*a").setPosition([3,-2,0])
         p13=cvo.CVO().CreateCVO("Associative","a+(b+c)=(a+b)+c (or) a*(b*c)=(a*b)*c22").setPosition([-3,-2,0]).setangle(-TAU/4)
         p14=cvo.CVO().CreateCVO("Distributive","a*(b+c)=(a*b)+(a*c)").setPosition([-4,0,0]).setangle(-TAU/4)
         p10.cvolist.append(p12)
         p10.cvolist.append(p11)
         p10.cvolist.append(p13)
         p10.cvolist.append(p14)
         self.construct1(p10,p10)
         self.play     
         
    def Rules(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("Rules","").setPosition([0,2.5,0])
         p11=cvo.CVO().CreateCVO("Additive identity ","x+0 =x").setPosition([3 ,1,0])
         p12=cvo.CVO().CreateCVO("Multiplicative identity "," x*1 =x").setPosition([3,-2,0])
         p13=cvo.CVO().CreateCVO("Multiplicative Inverse","a/b = 1/(c/b) or vise versa").setPosition([-3,-2,0]).setangle(-TAU/4)
         p10.cvolist.append(p12)
         p10.cvolist.append(p11)
         p10.cvolist.append(p13)
         self.construct1(p10,p10)
       
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