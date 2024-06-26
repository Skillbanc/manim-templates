from manim import *
from AbstractAnim import AbstractAnim
import cvo

class ratio(AbstractAnim):

    def construct(self):
        #self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.formsofratio()
        self.fadeOutCurrentScene()
        self.proportions()
        self.fadeOutCurrentScene()
        self.percentage()
        self.fadeOutCurrentScene()
        self.usespercentage()
        self.fadeOutCurrentScene()
        self.profitandloss()
        self.fadeOutCurrentScene()
        self.discount()
        self.fadeOutCurrentScene()
        self.simpleinterest()
        

    def Introduction(self):
        
        self.israndom=False
        self.positionChoice = [[-4,-2,0],[4,-2,0],[-4,2,0],[4,2,0],[0,-2,0]]
        p10=cvo.CVO().CreateCVO("ratio","")
        p11=cvo.CVO().CreateCVO("notation","a:b")
        p12=cvo.CVO().CreateCVO("symbol",":")
        p13=cvo.CVO().CreateCVO("antecedent","a")
        p14=cvo.CVO().CreateCVO("consequent","b")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p11.cvolist.append(p13)
        p11.cvolist.append(p14)  
        
        self.construct1(p10,p10)
        


    def formsofratio(self):
        self.israndom=False
        #self.setNumberOfCirclePositions(3)
        #self.colorChoice=[RED,BLUE,GREEN,PURPLE,ORANGE,YELLOW,LIGHT_PINK,WHITE,LIGHT_GRAY,LIGHT_BROWN,PINK,GRAY_BROWN]
        self.positionChoice = [[-4,0,0],[4,2,0],[4,-2,0]]
        p10=cvo.CVO().CreateCVO("forms of ratio","")
        p11=cvo.CVO().CreateCVO("Proportions","")
        p12=cvo.CVO().CreateCVO("percentages","")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        
        self.construct1(p10,p10)

    def proportions(self):
        self.israndom=False
        self.positionChoice = [[-5,2,0],[6,-2,0],[0,3,0],[-6,2,0],[6,2,0],[0,-3,0]]
        #self.setNumberOfCirclePositions(6)

        #self.colorChoice=[RED,BLUE,GREEN,PURPLE,ORANGE,YELLOW,LIGHT_PINK,WHITE,LIGHT_GRAY,LIGHT_BROWN,PINK,GRAY_BROWN]

        p10=cvo.CVO().CreateCVO("Proportions","")
        p11=cvo.CVO().CreateCVO("Symbol","::")
        p12=cvo.CVO().CreateCVO("Law of proportion","a:b::c:d")
        p13=cvo.CVO().CreateCVO("Product of means","bc")
        p14=cvo.CVO().CreateCVO("Product of extremes","ad")
        p15=cvo.CVO().CreateCVO("Equation","bc=ad")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p12.cvolist.append(p13)
        p12.cvolist.append(p14)
        p13.cvolist.append(p15)
        p14.cvolist.append(p15)
       
        self.construct1(p10,p10)
        
    def percentage(self):
        self.israndom=False
        self.positionChoice = [[-4,0,0],[4,2,0],[4,-2,0]]
        #self.setNumberOfCirclePositions(3)
        # self.colorChoice=[RED,BLUE,GREEN,PURPLE,ORANGE,YELLOW,LIGHT_PINK,WHITE,LIGHT_GRAY,LIGHT_BROWN,PINK,GRAY_BROWN]
        p10=cvo.CVO().CreateCVO("Proportions","")
        p11=cvo.CVO().CreateCVO("symbol","%")
        p12=cvo.CVO().CreateCVO("example","65%=65/100")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
       
        self.construct1(p10,p10)

    def usespercentage(self):
        self.israndom=False
        self.positionChoice = [[-4,-2,0],[4,-2,0],[-4,2,0],[4,2,0]]
        #self.setNumberOfCirclePositions(4)
        

        # self.colorChoice=[RED,BLUE,GREEN,PURPLE,ORANGE,YELLOW,LIGHT_PINK,WHITE,LIGHT_GRAY,LIGHT_BROWN,PINK,GRAY_BROWN]
        p10=cvo.CVO().CreateCVO("Percentage uses","")
        p11=cvo.CVO().CreateCVO("profit and loss","")
        p12=cvo.CVO().CreateCVO("simple interest","")
        p13=cvo.CVO().CreateCVO("discount","")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        
        self.construct1(p10,p10)

    def profitandloss(self):
         self.israndom=False
         self.positionChoice = [[-4,-2,0],[4,-2,0],[-4,2,0],[4,2,0]]
         #self.setNumberOfCirclePositions(4)
        #  self.colorChoice=[RED,BLUE,GREEN,PURPLE,ORANGE,YELLOW,LIGHT_PINK,WHITE,LIGHT_GRAY,LIGHT_BROWN,PINK,GRAY_BROWN]
         p10=cvo.CVO().CreateCVO("Profit","selling price - cost price")
         p11=cvo.CVO().CreateCVO("Profit%","profit/cost price")
         p12=cvo.CVO().CreateCVO("loss","costprice-selling price")
         p13=cvo.CVO().CreateCVO("loss%","loss/cost price")
         p10.cvolist.append(p11)
         p12.cvolist.append(p13)
         
         self.construct1(p10,p10)
         
    
    def discount(self):
         self.israndom=False 
         self.positionChoice = [[-4,0,0],[4,0,0]]
         #self.setNumberOfCirclePositions(2)
         
        #  self.colorChoice=[RED,BLUE,GREEN,PURPLE,ORANGE,YELLOW,LIGHT_PINK,WHITE,LIGHT_GRAY,LIGHT_BROWN,PINK,GRAY_BROWN]
         p10=cvo.CVO().CreateCVO("discount","market price - selling price")
         p11=cvo.CVO().CreateCVO("discount%","discount/market price")
         p10.cvolist.append(p11)
        
         self.construct1(p10,p10)

    def simpleinterest(self):
        self.israndom=False
        self.positionChoice = [[-6,-2,0],[6,-2,0],[0,3,0],[-6,2,0],[6,2,0],[0,-3,0]]
        #self.setNumberOfCirclePositions(6)
        # self.colorChoice=[RED,BLUE,GREEN,PURPLE,ORANGE,YELLOW,LIGHT_PINK,WHITE,LIGHT_GRAY,LIGHT_BROWN,PINK,GRAY_BROWN]
        p10=cvo.CVO().CreateCVO("SimpleInterest","")
        p11=cvo.CVO().CreateCVO("principle","P")
        p12=cvo.CVO().CreateCVO("interest","R%")
        p13=cvo.CVO().CreateCVO("time","T")
        p14=cvo.CVO().CreateCVO("amount","P+R")
        p15=cvo.CVO().CreateCVO("SI","P*T*R")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p11.cvolist.append(p14)
        p12.cvolist.append(p14)
        p11.cvolist.append(p15)
        p12.cvolist.append(p15)
        p13.cvolist.append(p15)
        
        self.construct1(p10,p10)
        


if __name__== "__main__":
    scene=ratio()
    scene.render()
