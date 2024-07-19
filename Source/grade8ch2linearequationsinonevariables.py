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
        self.SolvingLinearEquation()
        self.fadeOutCurrentScene()
        self.Equationthathasvariablesonbothsides()
        self.fadeOutCurrentScene()
        self.Reducingequationstosimplerform()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

             
    def introduction(self):
        # p1=cvo.CVO().CreateCVO("cname","oname")
        
        p10=cvo.CVO().CreateCVO("Linear Equation", "").setPosition([0,2,0])
        p11=cvo.CVO().CreateCVO("General Form","ax = b").setPosition([-3,0,0])
        p12=cvo.CVO().CreateCVO("Degree of linear Equation","1").setPosition([0,-2,0])
        p13=cvo.CVO().CreateCVO("Example of linear Equation","2x = 6").setPosition([3,0,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
         
        self.construct1(p10,p10)


    def SolvingLinearEquation(self):
        # Create CVO object with mathematical text
        p10 = cvo.CVO().CreateCVO("Solve the linear equation 3y+39=8", "").SetIsMathText(True)
        # Append onameList with properly formatted LaTeX strings
        p10.onameList.append("Solve the linear equation 3y+39=8")
        p10.onameList.append("Given linear equation : 3y+39=8")
        p10.onameList.append(r"step1 : 3y = 8 - 39 (Transposing 39 to RHS)")
        p10.onameList.append(r"7 (7x + 10) = 9 (5x + 10)")
        p10.onameList.append(r"3y = -31")
        p10.onameList.append(r"step2 : y = -31/3 (Transposing 3 to RHS)")
        p10.onameList.append(r"y\ =\-31/3")
       
        # Render the CVO object
        self.construct2(p10, p10)


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


     
    def SetDeveloperList(self):  
        self.DeveloperList="Akshitha"

         
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="linearequations.py"

    

           
if __name__ == "__main__":
    scene = LinearEquation()
    scene.render()