from manim import *
from AbstractAnim import AbstractAnim
import cvo


class RAT(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.ratio()
        self.fadeOutCurrentScene()
        self.proportion()
        self.fadeOutCurrentScene()
        self.law()
        self.fadeOutCurrentScene()
        self.percentage()
        self.fadeOutCurrentScene()
        self.profit
        self.fadeOutCurrentScene()
        self.loss()
        self.fadeOutCurrentScene()
        self.discount()
        self.fadeOutCurrentScene()
        self.Simpleinterest()

    def Introduction(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [-TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("RATIO-APPLICATIONS","")
        p11=cvo.CVO().CreateCVO("Aplications", "")
        p11.extendOname(["Ratio","Proportion","percentage","Profit and Loss","Discount","Simple Interest"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def ratio(self):
        self.setNumberOfCirclePositions(4)
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("RATIO","A:B")
        p11=cvo.CVO().CreateCVO("A variable","2")
        p12=cvo.CVO().CreateCVO("B variable","3")
        p13=cvo.CVO().CreateCVO("EQUATION", "2:3 OR 2/3")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))

    def proportion(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [-TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("PROPORTION","")
        p11=cvo.CVO().CreateCVO("Aplications", "")
        p11.extendOname(["SYMBOL ::","LAW OF PROPORTION"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def law(self):
        self.setNumberOfCirclePositions(5)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO(" LAW OF PROPORTION","A:B::C:D")
        p11=cvo.CVO().CreateCVO("PRODUCT OF MEANS ","BC")
        p12=cvo.CVO().CreateCVO("PRODUCT OF EXTREMES","AD")
        p13=cvo.CVO().CreateCVO("EQUATION", "BC=AD")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))

   
    def percentage(self):
        self.setNumberOfCirclePositions(4)
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("PERCENTAGE","X%")
        p11=cvo.CVO().CreateCVO("X variable","90")
        p12=cvo.CVO().CreateCVO("FORMULA ","(VALUE/TOTAL)*100")
        p13=cvo.CVO().CreateCVO("REPRESENTATION", "90% \nOR\n (90/100)*100")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))

    def profit(self):
        self.setNumberOfCirclePositions(3)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Profit","S.P-C.P")
        p11=cvo.CVO().CreateCVO("example ","50-40=10")
        p12=cvo.CVO().CreateCVO("Profit%","(P/C.P)*100=25%")
       
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
       
        self.construct1(p10,p10)
        #self.play(Create(CurvedArrow(p10.pos,p11.pos)),Create(CurvedArrow(p11.pos,p12.pos)))

    def loss(self):
        self.setNumberOfCirclePositions(3)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Loss","c.P-s.P")
        p11=cvo.CVO().CreateCVO("example ","60-50=10")
        p12=cvo.CVO().CreateCVO("Profit%","(L/C.P)*100=16%")
       
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
       
        self.construct1(p10,p10)
        #self.play(Create(CurvedArrow(p10.pos,p11.pos)),Create(CurvedArrow(p11.pos,p12.pos)))

    def discount(self):
        self.setNumberOfCirclePositions(3)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Discount"," MP-SP ")
        p11=cvo.CVO().CreateCVO(" Example ","100-60")
        p12=cvo.CVO().CreateCVO("Discount%","(D/MP)*100 =40%")
        
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
       
        self.construct1(p10,p10)
        
       
    def Simpleinterest(self):
        self.setNumberOfCirclePositions(5)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Simple Interest","P*T*R")
        p11=cvo.CVO().CreateCVO(" Principle ","P")
        p12=cvo.CVO().CreateCVO("Interest","R%")
        p13=cvo.CVO().CreateCVO("Time", "T")
       
        
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)

        self.construct1(p10,p10)
        
        #self.play(Create(CurvedArrow(p11.pos,p14.pos)),Create(CurvedArrow(p12.pos,p14.pos)),Create(CurvedArrow(p13.pos,p14.pos)))

if __name__ == "__main__":
    scene = RAT()
    scene.render()