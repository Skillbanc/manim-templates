from manim import *
from AbstractAnim import AbstractAnim
import cvo

class Integers(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction1()
        self.fadeOutCurrentScene()
        self.Addition()
        self.fadeOutCurrentScene()
        self.Subtraction()
        self.fadeOutCurrentScene()
        self.Multiplication()
        self.fadeOutCurrentScene()
        self.Division()
        self.fadeOutCurrentScene()
        self.Introduction2()
        self.fadeOutCurrentScene()
        self.Closureproperty()
        self.fadeOutCurrentScene()
        self.Commutativeproperty()
        self.fadeOutCurrentScene()
        self.Associativeproperty()
        self.fadeOutCurrentScene()
        self.Additiveidentity()
        self.fadeOutCurrentScene()
        self.Distributiveproperty()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

    def Introduction1(self):
        self.setNumberOfCirclePositions(2)
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Integers", "")
        p11 = cvo.CVO().CreateCVO("Operations", "")
        p11.extendOname(["Addition", "Subtraction", "Multiplication", "Division"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10, p10)

    def Addition(self):
        self.positionChoice=[[-4,0,0],[0,0,0],[4,0,0]]        
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Integers", "2,3")
        p11 = cvo.CVO().CreateCVO("Operation", "X+Y")
        p12 = cvo.CVO().CreateCVO("Sum", "5")
        

        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        self.construct1(p10, p10)
        self.fadeOutCurrentScene()

        title = Text("Addition").to_edge(UP)
        self.play(Write(title))

        examples = [
            r"X + Y \quad \text{example:} 2+3 =5",
            r"(-X) + Y \quad \text{example:} -2 + 3 = 1",
            r"(-X) +(-Y) \quad \text{example:} -2 + -3 = -5",
            r"X + (-Y) \quad \text{example:}2 + (-3) = -1"
        ]
        example1 = MathTex(examples[0]).scale(0.8).next_to(title, DOWN, buff=1)
        example2 = MathTex(examples[1]).scale(0.8).next_to(example1, DOWN, aligned_edge=LEFT, buff=0.5)
        example3 = MathTex(examples[2]).scale(0.8).next_to(example2, DOWN, aligned_edge=LEFT, buff=0.5)
        example4 = MathTex(examples[3]).scale(0.8).next_to(example3, DOWN, aligned_edge=LEFT, buff=0.5)


        self.play(Write(example1), Write(example2), Write(example3), Write(example4))

        self.wait(3)

    def Subtraction(self):
        self.positionChoice=[[-4,0,0],[0,0,0],[4,0,0]]        
        self.isRandom = False
        
        p10 = cvo.CVO().CreateCVO("Integers", "2,3")
        p11 = cvo.CVO().CreateCVO("Operation", "X-Y")
        p12 = cvo.CVO().CreateCVO("Difference", "-1")
    
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        self.construct1(p10, p10)
        self.fadeOutCurrentScene()

        title = Text("Subtraction").to_edge(UP)
        self.play(Write(title))

        examples = [
        r"X - Y \quad \text{example:} \quad 2 - 3 = -1",
        r"(-X) - Y \quad \text{example:} \quad -2 - 3 = -5",
        r"(-X) - (-Y) \quad \text{example:} \quad -2 - (-3) = 1",
        r"X - (-Y) \quad \text{example:} \quad 2 - (-3) = 5"
         ]
        example1 = MathTex(examples[0]).scale(0.8).next_to(title, DOWN, buff=1)
        example2 = MathTex(examples[1]).scale(0.8).next_to(example1, DOWN, aligned_edge=LEFT, buff=0.5)
        example3 = MathTex(examples[2]).scale(0.8).next_to(example2, DOWN, aligned_edge=LEFT, buff=0.5)
        example4 = MathTex(examples[3]).scale(0.8).next_to(example3, DOWN, aligned_edge=LEFT, buff=0.5)

        self.play(Write(example1), Write(example2), Write(example3), Write(example4))

        self.wait(3)

    def Multiplication(self):
        self.positionChoice=[[-4,0,0],[0,0,0],[4,0,0]]        
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Integers", "2,3")
        p11 = cvo.CVO().CreateCVO("Operation", "$ X \\times Y $")
        p12 = cvo.CVO().CreateCVO("Product", "6")
    
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        self.construct1(p10, p10)
        self.fadeOutCurrentScene()

        title = Text("Multiplication").to_edge(UP)
        self.play(Write(title))

        examples = [
            r"X \times Y \quad \text{example:} \quad 2 \times 3 = 6",
            r"(-X) \times Y \quad \text{example:} \quad -2 \times 3 = -6",
            r"(-X) \times (-Y) \quad \text{example:} \quad -2 \times -3 = 6",
            r"X \times (-Y) \quad \text{example:} \quad 2 \times (-3) = -6"
        ]
        example1 = MathTex(examples[0]).scale(0.8).next_to(title, DOWN, buff=1)
        example2 = MathTex(examples[1]).scale(0.8).next_to(example1, DOWN, aligned_edge=LEFT, buff=0.5)
        example3 = MathTex(examples[2]).scale(0.8).next_to(example2, DOWN, aligned_edge=LEFT, buff=0.5)
        example4 = MathTex(examples[3]).scale(0.8).next_to(example3, DOWN, aligned_edge=LEFT, buff=0.5)

        self.play(Write(example1), Write(example2), Write(example3), Write(example4))

        self.wait(3)


    def Division(self):
        self.positionChoice=[[-4,0,0],[0,0,0],[4,0,0]]        
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Integers", "6,3")
        p11 = cvo.CVO().CreateCVO("Operation", "$ X \\div Y $")
        p12 = cvo.CVO().CreateCVO("Quotient", "2")
    
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        self.construct1(p10, p10)
        self.fadeOutCurrentScene()

        title = Text("Division").to_edge(UP)
        self.play(Write(title))

        examples = [
        r"X \div Y \quad \text{example:} \quad 6 \div 3 = 2",
        r"(-X) \div Y \quad \text{example:} \quad -6 \div 3 = -2",
        r"(-X) \div (-Y) \quad \text{example:} \quad -6 \div -3 = 2",
        r"X \div (-Y) \quad \text{example:} \quad 6 \div (-3) = -2"
        ]
        example1 = MathTex(examples[0]).scale(0.8).next_to(title, DOWN, buff=1)
        example2 = MathTex(examples[1]).scale(0.8).next_to(example1, DOWN, aligned_edge=LEFT, buff=0.5)
        example3 = MathTex(examples[2]).scale(0.8).next_to(example2, DOWN, aligned_edge=LEFT, buff=0.5)
        example4 = MathTex(examples[3]).scale(0.8).next_to(example3, DOWN, aligned_edge=LEFT, buff=0.5)

        self.play(Write(example1), Write(example2), Write(example3), Write(example4))

        self.wait(3)

    def Introduction2(self):
        self.setNumberOfCirclePositions(2)
        self.isRandom = False


        p10 = cvo.CVO().CreateCVO("Integers", "")
        p11 = cvo.CVO().CreateCVO("Properties of integers", "")
        p11.extendOname(["Closure property", "Commutative property", "Associative property", "Additive identity", "Distributive Property"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10, p10)

    def Closureproperty(self):
        self.setNumberOfCirclePositions(5)
        self.isRandom = False

        p10 =cvo.CVO().CreateCVO("Closure Property","Closure of integer should be an integer")
        p11 = cvo.CVO().CreateCVO("Closure  of addition ","2+3=5")
        p12 = cvo.CVO().CreateCVO("Closure  of multiplication", "2 * 3 = 6")
        p13 = cvo.CVO().CreateCVO("Closure  of subtraction", "3 - 2 = 1")
        p14 = cvo.CVO().CreateCVO("Closure of division", " $\\frac{3}{2} \\not\\in \\text{integer}$ ")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        self.construct1(p10, p10)


    def Commutativeproperty(self):
        self.setNumberOfCirclePositions(5)
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Commutative for 2 integers", "2 , 3 ")
        p11 = cvo.CVO().CreateCVO("Commutative  of addition", "2 + 3 = 3 + 2 = 5")
        p12 = cvo.CVO().CreateCVO("Commutative  of multiplication", "2 * 3 = 3 * 2 = 6")
        p13 = cvo.CVO().CreateCVO("Commutative of subtraction", "$2 - 3 \\neq 3 - 2$")
        p14 = cvo.CVO().CreateCVO("Commutative of division", "$2 / 3 \\neq 3 / 2$")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        self.construct1(p10, p10)
    

    def Associativeproperty(self):
        self.setNumberOfCirclePositions(5)
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Associative for 3 integers", "2,3,4")
        p11 = cvo.CVO().CreateCVO("Associative for additiion", "(2 + 3) + 4 = 2 + (3 + 4) = 9")
        p12 = cvo.CVO().CreateCVO("Associative for subtraction", r"$(2 - 3) - 4 \neq 2 - (3 - 4)$")
        p13 = cvo.CVO().CreateCVO("Associative for multiplication", "(2 * 3) * 4 = 2 * (3 * 4) = 24")
        p14 = cvo.CVO().CreateCVO("Associative for division", r"$(2 / 3) / 4 \neq 2 / (3 / 4)$")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        self.construct1(p10, p10)


    def Additiveidentity(self):
        self.setNumberOfCirclePositions(5)
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Idedntity of integer", "2,a(identity element)")
        p11 = cvo.CVO().CreateCVO(" Identity of addition", "2 + 0 = 2")
        p12 = cvo.CVO().CreateCVO(" Identity of subtraction", "not applicable")
        p13 = cvo.CVO().CreateCVO(" Identity of multiplication", "2 * 0 = 0")
        p14 = cvo.CVO().CreateCVO(" Identity of division", "not applicable")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        self.construct1(p10, p10)
   


    def Distributiveproperty(self):
        self.setNumberOfCirclePositions(5)
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Distributive of integers", "2,3,5")
        p11 = cvo.CVO().CreateCVO("Distributive for addition", "2 * (3 + 5) = 2 * 3 + 2 * 5 = 16")
        p12 = cvo.CVO().CreateCVO("Distributive for Subtraction", "2 * (3 - 5) = 2 * 3 - 2 * 5 = -4")
        p13 = cvo.CVO().CreateCVO("Distributive for multiplication", "not applicable")
        p14 = cvo.CVO().CreateCVO("Distributive for division", "not applicable")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        self.construct1(p10, p10)
  
    def SetDeveloperList(self):  
        self.DeveloperList="Shanmukha Priya"
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade7CH1Integers.py"

if __name__ == "__main__":
        scene = Integers()
        scene.render()