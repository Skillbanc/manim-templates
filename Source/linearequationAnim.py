from manim import *
from AbstractAnim import AbstractAnim

import cvo


class LinearEquation(AbstractAnim):



    def construct(self):
        # p1=cvo.CVO().CreateCVO("cname","oname")
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.introduction()
        self.fadeOutCurrentScene()
        self.Addition()
        self.fadeOutCurrentScene()
        self.SolvingLinearEquation()
        self.fadeOutCurrentScene()
        self.Equationthathasvariablesonbothsides()
        self.fadeOutCurrentScene()
        self.Reducingequationstosimplerform()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

            
    
    def introduction(self):
        # p1=cvo.CVO().CreateCVO("cname","oname")
        
        toList = ["ax+by=c","ax+by=c"]
        
        p10=cvo.CVO().CreateCVO("Linear Equation", toList[0]).setPosition([-4,0,0])
        p11=cvo.CVO().CreateCVO("Degree of linear Equation","Degree = 1").setPosition([2,1,0])
        p12=cvo.CVO().CreateCVO("Example of linear Equation","2x + 3y = 6").setPosition([2,-2,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
         
        self.construct1(p10,p10)

    

    def Addition(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("sub topics of Linear Equations","").setPosition([0,2.5,0])
         p11=cvo.CVO().CreateCVO("Linear Equations","Chapter:2.1").setPosition([-4.25,1.75,0])
         p12=cvo.CVO().CreateCVO("Linear equations in one variable","Chapter:2.2").setPosition([-4,0,0])
         p13=cvo.CVO().CreateCVO("Solving Simple equation having the variable on one side","Chapter:2.3").setPosition([-2,-3,0]).setangle(-TAU/4)
         p14=cvo.CVO().CreateCVO("Solving equation that has variables on two sides","Chapter:2.4").setPosition([3,-1.5,0]).setangle(-TAU/4)
         p15=cvo.CVO().CreateCVO("Reducing Equations to Simpler Form","Chapter:2.5").setPosition([3,1.5,0]).setangle(-TAU/4)
         p10.cvolist.append(p11)
         p10.cvolist.append(p12)
         p10.cvolist.append(p13)
         p10.cvolist.append(p14)
         p10.cvolist.append(p15)

         self.construct1(p10,p10)
         #self.play()


    

    def SolvingLinearEquation(self):
        # p1=cvo.CVO().CreateCVO("cname","oname")
        
        toList = ["3y+39=8","3y+39=8"]
        
        p10=cvo.CVO().CreateCVO("Linear Equation", toList[0]).setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("step1:","3y = 8 - 39 (Transposing 39 to RHS)").setPosition([-4,1,0])
        p12=cvo.CVO().CreateCVO("Answer","3y = -31").setPosition([-2,-2,0])
        p13=cvo.CVO().CreateCVO("step2:","y = -31/3 (Transposing 3 to RHS)").setPosition([2,-2,0])
        p14=cvo.CVO().CreateCVO("y value:","-31/3").setPosition([4,1,0])
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        p13.cvolist.append(p14)
         
        self.construct1(p10,p10)




    def Equationthathasvariablesonbothsides(self):
        # Create CVO object with mathematical text
        p10 = cvo.CVO().CreateCVO("Equation that has variables on both sides", "").SetIsMathText(True)
        # Append onameList with properly formatted LaTeX strings
        p10.onameList.append("Equation that has variables on both sides")
        p10.onameList.append(r"7x + 10 : 5x + 10 = 9 : 7")
        p10.onameList.append(r"7 (7x + 10) = 9 (5x + 10)")
        p10.onameList.append(r"49x + 70 = 45x + 90")
        p10.onameList.append(r"49x - 45x = 90 - 70")
        p10.onameList.append(r"4x = 20")
        p10.onameList.append(r"x\ =\ 5")
       
        
        # Render the CVO object
        self.construct2(p10, p10)




    def Reducingequationstosimplerform(self):
        # Create CVO object with mathematical text
        p10 = cvo.CVO().CreateCVO("Reducing equations to simpler form", "").SetIsMathText(True)
        # Append onameList with properly formatted LaTeX strings
        p10.onameList.append("Reducing equations to simpler form")
        p10.onameList.append(r"solve\ x/2 - 1/4 = x/3 + 1/2")
        p10.onameList.append(r"x/2 - 1/4 = x/3 + 1/2")
        p10.onameList.append(r"x/2 - x/3 = 1/2 + 1/4")
        p10.onameList.append(r"3x-2x/6 = 2+1/4")
        p10.onameList.append(r"x/6 = 3/4")
        p10.onameList.append(r"x = (3/4)*6")
        p10.onameList.append(r"x\ =\ 9/2")
        
        # Render the CVO object
        self.construct2(p10, p10)


    
    def GithubSourceCodeReference(self):
        self.colorChoice=[PINK,BLUE,LIGHT_GRAY]
        p2 = cvo.CVO().CreateCVO("SOURCE CODE REFERENCE", "").setPosition([0,2.5,0])
        p4 = cvo.CVO().CreateCVO("GITHUB URL", "https://github.com/Skillbanc/manim-templates").setPosition([-2,0,0])
        p5 = cvo.CVO().CreateCVO("File Name","linearequationAnim.py").setPosition([2,0,0])
        p2.cvolist.append(p4)
        p2.cvolist.append(p5)
        self.setNumberOfCirclePositions(3)
        p4.setcircleradius(1)
        p5.setcircleradius(1)
        self.construct1(p2, p2)

    

           
if __name__ == "__main__":
    scene = LinearEquation()
    scene.render()