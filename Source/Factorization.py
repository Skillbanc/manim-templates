from manim import *
from AbstractAnim import AbstractAnim
import cvo

class Factorization(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.PrimeFactorization()
        self.fadeOutCurrentScene()
        self.ComplexFactorization()
        self.fadeOutCurrentScene()
        self.factorsofalgebraicexpression()
        self.fadeOutCurrentScene()
        self.Factorisationusingidenties()
        self.fadeOutCurrentScene()
        self.factorsoftheform()
        self.fadeOutCurrentScene()
        self.divisionofalgebraicexpression()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
       

    def Introduction(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [-TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Factorization","")
        p11=cvo.CVO().CreateCVO("Types", "")
        p11.extendOname(["PrimeFactorization","ComplexFactorization"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def PrimeFactorization(self):
        self.setNumberOfCirclePositions(3)
        #self.angleChoice = [0,0,0]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("PrimeFactorization","X*1")
        p11=cvo.CVO().CreateCVO("X variable","3")
        p12=cvo.CVO().CreateCVO("factors of x","3*1")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.play(Create(CurvedArrow(p11.pos,p12.pos)))
        #self.play()

    def ComplexFactorization(self):
        self.setNumberOfCirclePositions(3)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("ComplexFactorization","X*1,X*2,....")
        p11=cvo.CVO().CreateCVO("X variable","")
        p12=cvo.CVO().CreateCVO("factors of x","1*6,2*3,3*2")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.play(Create(CurvedArrow(p11.pos,p12.pos)))
        #self.play()


    def factorsofalgebraicexpression(self):
        self.setNumberOfCirclePositions(5)
        #self.angleChoice = [0,0,0]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("factors of algebraic expression","7yz")
        p11=cvo.CVO().CreateCVO("7(yz)","7 and yz are factors")
        p12=cvo.CVO().CreateCVO("7y(z)","7y and z are factors")
        p13=cvo.CVO().CreateCVO("7z(y)","7z and y are factors")
        p14=cvo.CVO().CreateCVO("7xy","7,y and z are factors")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        self.construct1(p10,p10)
        #self.play()


    def Factorisationusingidenties(self):
        # Create CVO object with mathematical text
        p10 = cvo.CVO().CreateCVO("Factorisation using identies", "").SetIsMathText(True)
        # Append onameList with properly formatted LaTeX strings
        p10.onameList.append("Factorisation using identies")
        p10.onameList.append(r"(a+b)^2\ =\ a^2\ +\ 2ab\ +\ b^2")
        p10.onameList.append(r"(a-b)^2\ =\ a^2\ -\ 2ab\ +\ b^2")
        p10.onameList.append(r"(a-b)(a-b)\ =\ a^2\ -\ b^2\ are\ algebric\ identies.")
        p10.onameList.append(r"Example4:\  Factorise\ x^2\ +\ 10x\ +\ 25")
        p10.onameList.append(r"The\ first\ and\ third\ terms\ are\ perfect\ squares.")
        p10.onameList.append(r"(That\ is\ x^2\ and\ 25(5^2).")
        p10.onameList.append(r"so\ x^2\ +\ 10x\ 25\ =\ (x)^2\ 2(x)\ (5)\ +\ (5)^2")
        p10.onameList.append(r"we\ can\ comapare\ it\ with\ \ a^2\ +\ 2ab\ +\ b^2")
        p10.onameList.append(r"i.e.\ (a+b)^2.\ here\ a=x\ and\ b=5")
        p10.onameList.append(r"we\ have\ x^2\ +\ 10x\ +\ 25\ =\ (x+5)^2\ =\ (x+5)\ (x+5) ")
        
        # Render the CVO object
        self.construct2(p10, p10)
        

    def factorsoftheform(self):
        # Create CVO object with mathematical text
        p10 = cvo.CVO().CreateCVO("factors of the form", "").SetIsMathText(True)
        # Append onameList with properly formatted LaTeX strings
        p10.onameList.append("Factors of the form (x+a)(x+b)= $x^2$ +(a+b)x+ab")
        p10.onameList.append(r"Example1:\ consider\ x^2+12x+35\ ")
        p10.onameList.append(r"x^2\ (5+7)x\ +\ 35")
        p10.onameList.append(r"x^2\ +\ 5x\ +\ 7x\ +\ 35")
        p10.onameList.append(r"x(x+5)\ +\ 7(x+5)")
        p10.onameList.append(r"(x+5)\ (x+7)")
        p10.onameList.append(r"x^2\ +\ (a+b)x\ +\ ab\ can\ be\ factorised\ as\ (x+a)(x+b)")

        # Render the CVO object
        self.construct2(p10, p10)
        

    def divisionofalgebraicexpression(self):
        # Create CVO object with mathematical text
        p10 = cvo.CVO().CreateCVO("division of algebraic expression", "").SetIsMathText(True)
        # Append onameList with properly formatted LaTeX strings
        p10.onameList.append("Division of Algebraic Expression")
        p10.onameList.append(r"Let\ us\ consider\ 3x\ *\ 5x^3\ =\ 15x^4")
        p10.onameList.append(r"then\  15x^4\ +\ 5x^3\ = 3x\ and\ 15x^4\ +\ 3x\ =\ 5x^3")
        p10.onameList.append(r"consider\ 6a(a+5)\ =\ 6a^2\ +\ 30a")
        p10.onameList.append(r"(6a^2+30a)\ +\ 6a\ +\ a+5")
        p10.onameList.append(r"(6a^2+30a)\ +\ (a+5)\ =\ 6a")

        # Render the CVO object
        self.construct2(p10, p10)

    def GithubSourceCodeReference(self):
        self.colorChoice=[GREEN_C,BLUE_C,ORANGE]
        p2=cvo.CVO().CreateCVO("SOURCE CODE REFERENCE","").setPosition([0,2.5,0])
        p4=cvo.CVO().CreateCVO("Github URL","https://github.com/Skillbanc/manim-templates")
        p5=cvo.CVO().CreateCVO("File Name","Factorization.py")
        p2.cvolist.append(p4)
        p2.cvolist.append(p5)
        self.setNumberOfCirclePositions(3)
        p4.setcircleradius(3)
        p5.setcircleradius(2.5)
        self.construct1(p2,p2)


if __name__ == "__main__":
    scene = Factorization()
    scene.render()