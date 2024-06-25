import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo

class Exponents(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.ExpForm()
        self.fadeOutCurrentScene()
        self.ExpEx()
        self.fadeOutCurrentScene()
        self.ExpNegPower()
        self.fadeOutCurrentScene()
        self.Law1()
        self.fadeOutCurrentScene()
        self.Law2()
        self.fadeOutCurrentScene()
        self.Law3()
        self.fadeOutCurrentScene()
        self.Law4()
        self.fadeOutCurrentScene()
        self.Law5()
        self.fadeOutCurrentScene()
        self.ExpConversion()
        self.fadeOutCurrentScene()
        self.ExpComparison()
        self.fadeOutCurrentScene()

    def ExpForm(self):
        p10=cvo.CVO().CreateCVO("Mathematics Exponents","").setPosition([-2,2.5,0])
        p11=cvo.CVO().CreateCVO("Exponent Form ", "$a^n$").setPosition([0,1,0])
        p12=cvo.CVO().CreateCVO("Base", "a").setPosition([3,0,0])
        p13=cvo.CVO().CreateCVO("Power", "n").setPosition([-3,-1.5,0])

       # p14=cvo.CVO().CreateCVO("Result", "a*a*a*.....n times")
        
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
        #p11.cvolist.append(p14)
        self.construct1(p10,p10)
    def ExpEx(self):
        #p10=cvo.CVO().CreateCVO("Mathematics Exponents","") 
        p11=cvo.CVO().CreateCVO("Exponent Exp ", "$2^3$").setPosition([3, 1, 0]) 
        p12=cvo.CVO().CreateCVO("Base", "2").setPosition([3, -1, 0])
        p13=cvo.CVO().CreateCVO("Power", "3").setPosition([-3, 1, 0]).setangle(-TAU/4)

        p14=cvo.CVO().CreateCVO("Result", "2*2*2 = 8").setPosition([-3, -1, 0]).setangle(-TAU/4)
        
       # p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
        p11.cvolist.append(p14)
        self.construct1(p11,p11)
    def ExpNegPower(self):
        # Create content objects with positions
        #p10 = cvo.CVO().CreateCVO("Mathematics Exponents", "").setPosition([0, 3, 0])
        p11 = cvo.CVO().CreateCVO("Negative Power", "$a^{-n}$").setPosition([3, 1, 0])
        p12 = cvo.CVO().CreateCVO("Base", "a").setPosition([3, -1, 0])
        p13 = cvo.CVO().CreateCVO("Power", "-n").setPosition([-3, 1, 0]).setangle(-TAU/4)
        p14 = cvo.CVO().CreateCVO("Result", "$\\frac{1}{a^n} = \\frac{1}{a*a*..ntimes}$").setPosition([-3, -1, 0]).setangle(-TAU/4)
        p15 = cvo.CVO().CreateCVO("Example", "$2^{-3}$").setPosition([0, -2, 0])
        p16 = cvo.CVO().CreateCVO("Result", "$\\frac{1}{2^3} = \\frac{1}{8}$").setPosition([0,0,0])
        
        #p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
        p11.cvolist.append(p14)
        p11.cvolist.append(p15)
        p15.cvolist.append(p16)

        self.construct1(p11, p11)

    def Law1(self):
        #self.add(NumberPlane())
        self.positionChoice = [[0, 2.5, 0],[4, 2, 0],[5, -2, 0],[-4, 0, 0]]
        self.angleChoice = [TAU/4,TAU/4,TAU/4,TAU/4]
        self.colorChoice=[ORANGE,YELLOW,GREEN,WHITE]
        self.isRandom = False
        #p10 = cvo.CVO().CreateCVO("Mathematics Exponents", "").setPosition([0, 2.5, 0])
        p11 = cvo.CVO().CreateCVO("Laws of Exponents", "LAW 1").setPosition([4, 2, 0])
        p12 = cvo.CVO().CreateCVO("Product Rule ", "$(a^m*a^n = a^{m + n})$").setPosition([5, -2, 0])
        p13 = cvo.CVO().CreateCVO("Exp", "$(2^3*2^2 = 2^5)$").setPosition([-4, 0, 0])
        
        #p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        self.construct1(p11, p11)

    def Law2(self):
        #self.add(NumberPlane())
        self.positionChoice = [[0, 2.5, 0],[4, 2, 0],[5, -2, 0],[-4, 0, 0]]
        self.angleChoice = [TAU/4,TAU/4,TAU/4,TAU/4]
        self.colorChoice=[ORANGE,YELLOW,GREEN,WHITE]
        self.isRandom = False
        #p10 = cvo.CVO().CreateCVO("Mathematics Exponents", "").setPosition([0, 2.5, 0])
        p11 = cvo.CVO().CreateCVO("Laws of Exponents", "LAW 2 ").setPosition([4, 2, 0])
        p12 = cvo.CVO().CreateCVO("Quotient Rule", "$\\frac{a^m}{a^n} = a^{m - n}$").setPosition([5, -2, 0])
        p13 = cvo.CVO().CreateCVO("Exp", "$\\frac{3^4}{3^2} = 3^{2}$").setPosition([-4, 0, 0])
        
       # p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        self.construct1(p11, p11)

    def Law3(self):
        #self.add(NumberPlane())
        self.positionChoice = [[0, 2.5, 0],[4, 2, 0],[5, -2, 0],[-4, 0, 0]]
        self.angleChoice = [TAU/4,TAU/4,TAU/4,TAU/4]
        self.colorChoice=[ORANGE,YELLOW,GREEN,WHITE]
        self.isRandom = False
        #p10 = cvo.CVO().CreateCVO("Mathematics Exponents", "").setPosition([0, 2.5, 0])
        p11 = cvo.CVO().CreateCVO("Laws of Exponents", "LAW 3").setPosition([4, 2, 0])
        p12 = cvo.CVO().CreateCVO("Power Rule", "$((a^m)^n = a^{m*n})$").setPosition([5, -2, 0])
        p13 = cvo.CVO().CreateCVO("Exp", "$((5^3)^2 = 5^{6})$").setPosition([-4, 0, 0])
        
        #p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        self.construct1(p11, p11)

    def Law4(self):
        #self.add(NumberPlane())
        self.positionChoice = [[0, 3, 0],[0,1, 0],[3,-1,0],[-3,-1, 0]]
        self.angleChoice = [TAU/4,TAU/4,TAU/4,TAU/4]
        self.colorChoice=[ORANGE,YELLOW,GREEN,WHITE]
        self.isRandom = False
        #p10 = cvo.CVO().CreateCVO("Mathematics Exponents", "").setPosition([0, 3, 0])
        p11 = cvo.CVO().CreateCVO("Laws of Exponents", "LAW 4").setPosition([0, 1, 0])
        p12 = cvo.CVO().CreateCVO("Product of Powers", "$(a^m*b^m = (a*b)^m)$").setPosition([3, -1, 0])
        p13 = cvo.CVO().CreateCVO("Exp", "$(5^3*2^3 = (10)^3)$").setPosition([-3, -1, 0])
        
        #p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        self.construct1(p11, p11)

    def Law5(self):
        #self.add(NumberPlane())
        self.positionChoice = [[0, 3, 0],[0,1, 0],[3,-1, 0],[0, -2, 0]]
        self.angleChoice = [TAU/4,TAU/4,TAU/4,TAU/4]
        self.colorChoice=[ORANGE,YELLOW,GREEN,WHITE]
        self.isRandom = False
        #p10 = cvo.CVO().CreateCVO("Mathematics Exponents", "").setPosition([0, 3, 0])
        p11 = cvo.CVO().CreateCVO("Laws of Exponents", "LAW 5").setPosition([0, 1, 0])
        p12 = cvo.CVO().CreateCVO("Zero Exponent Rule", "$(a^0 = 1)$").setPosition([3, -1, 0])
        p13 = cvo.CVO().CreateCVO("Exp", "$(5^0 = 1)$").setPosition([0, -2, 0])
        
        #p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        self.construct1(p11, p11)


    def ExpConversion(self):
        p10 = cvo.CVO().CreateCVO("Application of Exponents", "Expressing Numbers in Standard Form").setPosition([3, 1, 0])
        p11 = cvo.CVO().CreateCVO("Exp 1", "$12345 = 1.2345*10^4$").setPosition([3, -1, 0])
        p12 = cvo.CVO().CreateCVO("Exp 2", "$0.00123 = 1.23*10^{-3}$").setPosition([-3, 1, 0]).setangle(-TAU/4)
        p13 = cvo.CVO().CreateCVO("Exp 3", "$987000 = 9.87*10^5$").setPosition([-3, -1, 0]).setangle(-TAU/4)
        p14 = cvo.CVO().CreateCVO("Exp 4", "$0.0000456 = 4.56*10^{-5}$").setPosition([0, -2, 0])
        
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        
        self.construct1(p10, p10)


    def ExpComparison(self):
        p10 = cvo.CVO().CreateCVO("Comparing Numbers with Exponents", "Very Large and Very Small Numbers").setPosition([3, 1, 0]) 
        p11 = cvo.CVO().CreateCVO("Large Num 1", "$5.97*10^{24}$ (Mass of Earth)").setPosition([3, -1, 0])
        p12 = cvo.CVO().CreateCVO("Large Num 2", "$1.99*10^{30}$ (Mass of Sun)").setPosition([-3, 1, 0]).setangle(-TAU/4)
        p13 = cvo.CVO().CreateCVO("Small Num 1", "$9.11*10^{-31}$ (Mass of Electron)").setPosition([-3, -1, 0]).setangle(-TAU/4)
        p14 = cvo.CVO().CreateCVO("Small Num 2", "$6.63*10^{-34}$ (Planck's Constant)").setPosition([0, -2, 0])
        
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        
        self.construct1(p10, p10)

    def SetDeveloperList(self):  
        self.DeveloperList = "Mukthanand Reddy"
         
if __name__ == "__main__":
    scene = Exponents()
    scene.render()
