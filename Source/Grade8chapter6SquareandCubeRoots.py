from manim import *
from AbstractAnim import AbstractAnim
import cvo

class SquarecubeOperations(AbstractAnim):

    def construct(self):

        self.RenderSkillbancLogo()
        self.Extra_text()
        self.fadeOutCurrentScene()
        self.introduction()
        self.fadeOutCurrentScene()
        self.Square()
        self.fadeOutCurrentScene()
        self.Cube()
        self.fadeOutCurrentScene()
        self.Addition()
        self.fadeOutCurrentScene()
        self.PropertiesofSquareNumbers()
        self.fadeOutCurrentScene()
        self.InterestingPatternsofSquare()
        self.fadeOutCurrentScene()
        self.pythagoreanTriplets()
        self.fadeOutCurrentScene()
        self.SquareRoot()
        self.fadeOutCurrentScene()
        self.PrimeFactorization2()
        self.fadeOutCurrentScene()
        self.Subtractionofsuccessiveoddnumbers()
        self.fadeOutCurrentScene()
        self.intro_text()
        self.fadeOutCurrentScene()
        self.division_steps()
        self.fadeOutCurrentScene()
        self.squarerootsofnonperfectsquarenumbers()
        self.fadeOutCurrentScene()
        self.CubeRoot()
        self.fadeOutCurrentScene()
        self.cuberootthroughPrimeFactorization2()
        self.fadeOutCurrentScene()
        self.Estimatingthecuberootofanumber()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()


    def Extra_text(self):
        title = Text("Chapter : Square Roots and Cube Roots", font_size=48)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))
       

    def introduction(self):
        # p1=cvo.CVO().CreateCVO("cname","oname")

        p10=cvo.CVO().CreateCVO("Numbers","").setPosition([-5,0,0])
        p11=cvo.CVO().CreateCVO("Operations on Numbers","Squaring,Cubing").setPosition([-1,0,0])
        p12=cvo.CVO().CreateCVO("Squareing","$x^2$").setPosition([3.5,1,0])
        p13=cvo.CVO().CreateCVO("Cubeing","$x^3$").setPosition([3.5,-2,0])
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)

        self.construct1(p10,p10)


    def Square(self):
        self.setNumberOfCirclePositions(5)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Squring of Numbers","$x^2$").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("X variable","3").setPosition([-2.5,0,0])
        p12=cvo.CVO().CreateCVO("Squaring of x","$3^2$=3*3").setPosition([0,-2.5,0])
        p13=cvo.CVO().CreateCVO("Total","9").setPosition([2.5,0,0])
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()

    
    def Cube(self):
        self.setNumberOfCirclePositions(5)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Cubing of Numbers","$x^3$").setPosition([-2.5,2.5,0])
        p11=cvo.CVO().CreateCVO("X variable","2").setPosition([-2,-2,0])
        p12=cvo.CVO().CreateCVO("Cubeing of x","$2^3$=2*2*2").setPosition([2,-2,0])
        p13=cvo.CVO().CreateCVO("Total", "8").setPosition([2.5,2.5,0])
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()


    def Addition(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("sub topics of Square and Cube Roots","").setPosition([0,2.5,0])
         p11=cvo.CVO().CreateCVO("Properties of Square Numbers","Chapter:6.1").setPosition([-4,1,0])
         p12=cvo.CVO().CreateCVO("Interesting Patterns","Chapter:6.2").setPosition([-3,-2,0])
         p13=cvo.CVO().CreateCVO("Pythogorean Triplets","Chapter:6.3").setPosition([2.5,0,0]).setangle(-TAU/4)
         p14=cvo.CVO().CreateCVO("Methods for finding Squareroots","Chapter:6.4").setPosition([4,-2,0]).setangle(-TAU/4)
         p10.cvolist.append(p11)
         p10.cvolist.append(p12)
         p10.cvolist.append(p13)
         p10.cvolist.append(p14)
         self.construct1(p10,p10)
         #self.play()


    def PropertiesofSquareNumbers(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("Properties of SquareNumbers","Chapter:6.1").setPosition([0,2.5,0])
         p11=cvo.CVO().CreateCVO("Perfect Squares","RationalNum=$RationalNum^2$").setPosition([-5,1,0])
         p12=cvo.CVO().CreateCVO("Square Number","Integer=$Integer^2$").setPosition([0,0,0]).setangle(-TAU/4)
         p13=cvo.CVO().CreateCVO("Unit digit","").setPosition([5,1,0]).setangle(-TAU/4)
         p14=cvo.CVO().CreateCVO("Example","2.25=$(1.5)^2$=1.5*1.5").setPosition([-3,-3,0])
         p15=cvo.CVO().CreateCVO("Example","36=$(6)^2$=6*6").setPosition([0,-3,0])
         p16=cvo.CVO().CreateCVO("Example","$17^2$=7*7=49=9").setPosition([3,-3,0])
         p10.cvolist.append(p11)
         p10.cvolist.append(p12)
         p10.cvolist.append(p13)
         p11.cvolist.append(p14)
         p12.cvolist.append(p15)
         p13.cvolist.append(p16)
 
         self.construct1(p10,p10)
         #self.play()
    

    def InterestingPatternsofSquare(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("Interesting patterns of Square","Chapter:6.2").setPosition([0,2.5,0])
         p11=cvo.CVO().CreateCVO("Sum of first n odd numbers = $n^2$","$\sum_{i=1}^{n} (2i-1) = n^2$").setPosition([-4,1,0])
         p12=cvo.CVO().CreateCVO("Numeric Palindrome","$1111^2$=1234321").setPosition([0,0,0]).setangle(-TAU/4)
         p13=cvo.CVO().CreateCVO("Numbers between sucessive squares","2*Base of the first Number").setPosition([4,1,0]).setangle(-TAU/4)
         p14=cvo.CVO().CreateCVO("Example 1","1+3+5+7=16=$4^2$").setPosition([-2,-2,0])
         p15=cvo.CVO().CreateCVO("Example 2","$1001^2$=1002001").setPosition([0,-2,0])
         p16=cvo.CVO().CreateCVO("Example","$2^2$=4;$3^2$=9=2*2=4").setPosition([2,-2,0])
         p10.cvolist.append(p11)
         p10.cvolist.append(p12)
         p10.cvolist.append(p13)
         p11.cvolist.append(p14)
         p12.cvolist.append(p15)
         p13.cvolist.append(p16)
 
         self.construct1(p10,p10)
         #self.play()

    def pythagoreanTriplets(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("pythagorean Triplets","Chapter:6.3").setPosition([-4,2.5,0])
         p11=cvo.CVO().CreateCVO("If $a^2$+$b^2$=$c^2$","(a,b,c)are Pythagorean Triplts").setPosition([-3,-1,0])
         p12=cvo.CVO().CreateCVO("EX 1: $3^2$+$4^2$=25=$5^2$","(3,4,5)are Pythagorean Triplts").setPosition([3.5,1,0]).setangle(-TAU/4)
         p13=cvo.CVO().CreateCVO("EX 2: $5^2$+$12^2$=169=$13^2$","(5,12,13)are Pythagorean Triplts").setPosition([3.5,-2,0])
         p10.cvolist.append(p11)
         p11.cvolist.append(p12)
         p11.cvolist.append(p13)
         
         self.construct1(p10,p10)
         #self.play()
    

    
    def SquareRoot(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Square Root of Number",r"$\sqrt{x}$")
        p11=cvo.CVO().CreateCVO("X variable","9")
        p12=cvo.CVO().CreateCVO("Square root of 9",r"$\sqrt{9}$=3")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.play(Create(CurvedArrow(p11.pos,p12.pos)))
        #self.play()



    def PrimeFactorization2(self):
        # Create CVO object with mathematical text
        p10 = cvo.CVO().CreateCVO("Square root through Prime Factorization", "2x^2 + 5x + 3").SetIsMathText(True)

        # Append onameList with properly formatted LaTeX strings
        p10.onameList.append("Methods for finding square roots for perfect squares")
        p10.onameList.append("1. Prime Factorization method")
        p10.onameList.append(r"Let\ us\ find\ \sqrt{1296}\ by\ Prime\ Factorization\ method")
        p10.onameList.append(r"Step1:\ Resolving\ 1296\ into\ prime\ factors\ ,\ we\ get")
        p10.onameList.append("1296 = 2*2*2*2*3*3*3*3")
        p10.onameList.append("Step2:\ Make\ pairs\ of\ equal\ factors\ ,\ we\ get")
        p10.onameList.append(r"1296 = (2 \cdot 2) \cdot (2 \cdot 2) \cdot (3 \cdot 3) \cdot (3 \cdot 3)")
        p10.onameList.append("Step3:\ Choosing\ one\ factor\ out\ of\ every\ pair\ so\ ,\ we\ get")
        p10.onameList.append(r"\sqrt{1296} = 2*2*3*3=22")
        p10.onameList.append("Therefore\ ,\ the\ Square\ Root\ of\ 1296\ is\ 22")
 

        # Render the CVO object
        self.construct2(p10, p10)

    def Subtractionofsuccessiveoddnumbers(self):
        # Create CVO object with mathematical text
        p10 = cvo.CVO().CreateCVO("Square root through Subtraction of successive odd numbers","").SetIsMathText(True)

        # Append onameList with properly formatted LaTeX strings
        p10.onameList.append("2. Subtraction of successive odd numbers method")
        p10.onameList.append(r"we\ know\ that,\ sum\ of\ first\ \text{n}\ odd\ numbers\ is\ equal\ to\ n^2")
        p10.onameList.append(r"\sum_{i=1}^{n} (2i-1) = n^2")
        p10.onameList.append(r"1+3+5+7+9\ =\ 25\ =\ 5^2")
        p10.onameList.append(r"Finding\ Square\ root\ is\ the\ reverse\ order\ of\ this\ pattern")
        p10.onameList.append(r"For\ example,\ find\ \sqrt{49}")
        p10.onameList.append(r"Step\ 1:\ 49-1=48")
        p10.onameList.append(r"Step\ 2:\ 48-3=45")
        p10.onameList.append(r"Step\ 3:\ 45-5=40")
        p10.onameList.append(r"Step\ 4:\ 40-7=33")
        p10.onameList.append(r"Step\ 5:\ 33-9=24")
        p10.onameList.append(r"Step\ 6:\ 24-11=13")
        p10.onameList.append(r"Step\ 7:\ 13-13=0")
        p10.onameList.append(r"From\ 49,\ we\ have\ subtracted\ 7\ successive\ odd\ numbers,")
        p10.onameList.append(r"starting\ from\ 1\ and\ obtained\ zero\ (0)\ at\ the")
        p10.onameList.append(r"7^{\text{th}}\ step.")
        p10.onameList.append(r"Therefore,\ \sqrt{49}=7")

        # Render the CVO object
        self.construct2(p10, p10)

    def intro_text(self):
        title = Text("3. Finding Square Root using Division Method", font_size=48)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))
    
    def division_steps(self):
        step_title = Text("Finding √784 using Division Method", font_size=36)
        self.play(Write(step_title))
        self.wait(2)
        self.play(FadeOut(step_title))

        step1 = Text("Step 1: Group the digits in pairs from right to left.", font_size=24)
        self.play(Write(step1))
        self.wait(2)
        self.play(FadeOut(step1))

        grouped_digits = Text("784 -> 7 | 84", font_size=24)
        self.play(Write(grouped_digits))
        self.wait(2)
        self.play(FadeOut(grouped_digits))

        step2 = Text("Step 2: Find the largest number whose square is less than or equal to 7.", font_size=24)
        self.play(Write(step2))
        self.wait(2)
        self.play(FadeOut(step2))

        step2_result = MathTex("2^2 = 4")
        self.play(Write(step2_result))
        self.wait(2)
        self.play(FadeOut(step2_result))

        step3 = Text("Step 3: Subtract 4 from 7, get 3.", font_size=24)
        self.play(Write(step3))
        self.wait(2)
        self.play(FadeOut(step3))

        subtraction = MathTex("7 - 4 = 3")
        self.play(Write(subtraction))
        self.wait(2)
        self.play(FadeOut(subtraction))

        bring_down = Text("Step 4: Bring down the next pair of digits (84).", font_size=24)
        self.play(Write(bring_down))
        self.wait(2)
        self.play(FadeOut(bring_down))

        new_number = MathTex("384")
        self.play(Write(new_number))
        self.wait(2)
        self.play(FadeOut(new_number))

        step5 = Text("Step 5: Double the divisor (2 becomes 4). Find a digit (x) such that 4x * x <= 384.", font_size=24)
        self.play(Write(step5))
        self.wait(2)
        self.play(FadeOut(step5))

        calculation = MathTex("48 \\times 8 = 384")
        self.play(Write(calculation))
        self.wait(2)
        self.play(FadeOut(calculation))

        remainder = MathTex("384 - 384 = 0")
        self.play(Write(remainder))
        self.wait(2)
        self.play(FadeOut(remainder))

        final_step = Text("Step 6: Since the remainder is 0, the square root of 784 is 28.", font_size=24)
        self.play(Write(final_step))
        self.wait(2)
        self.play(FadeOut(final_step))

        conclusion = Text("Therefore, √784 = 28", font_size=36)
        self.play(Write(conclusion))
        self.wait(2)
        self.play(FadeOut(conclusion))


    def squarerootsofnonperfectsquarenumbers(self):
        # Create CVO object with mathematical text
        p10 = cvo.CVO().CreateCVO("Square roots of non-perfect square numbers", "").SetIsMathText(True)

        # Append onameList with properly formatted LaTeX strings
        p10.onameList.append("Square roots of non-perfect square numbers")
        p10.onameList.append(r"Let\ us\ estimate\ the\ value\ of\ \sqrt{300}")
        p10.onameList.append(r"300\ lies\ between\ two\ perfect\ square\ numbers\ 100\ and\ 400")
        p10.onameList.append(r"Therefore,\ 100\ <\ 300\ <\ 400")
        p10.onameList.append(r"10^2\ <\ 300\ <\ 20^2")
        p10.onameList.append(r"That\ is\ 10\ <\ \sqrt{300}\ <\ 20")
        p10.onameList.append(r"But\ still\ we\ are\ not\ close\ to\ a\ perfect\ square\ number")
        p10.onameList.append(r"We\ know\ that\ 17^2=289\ and,\ 18^2=324")
        p10.onameList.append(r"therefore\ 289\ <\ 300\ <\ 400")
        p10.onameList.append(r"17\ <\ \sqrt{300}\ <\ 18")
        p10.onameList.append(r"As\ 289\ is\ more\ closer\ to\ 300\ than\ 324.")
        p10.onameList.append(r"The\ approximate\ value\ of\ \sqrt{300}\ is\ 17.")
        
        # Render the CVO object
        self.construct2(p10, p10)

    def CubeRoot(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Cube root of Numbers",r"$\sqrt[3]{x}$")
        p11=cvo.CVO().CreateCVO("X variable","64")
        p12=cvo.CVO().CreateCVO("Cuberoot of 64",r"$\sqrt[3]{64}$=4")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.play(Create(CurvedArrow(p11.pos,p12.pos)))
        #self.play()
    

    def cuberootthroughPrimeFactorization2(self):
        # Create CVO object with mathematical text
        p10 = cvo.CVO().CreateCVO("Cube Root through Prime Factorization", "2x^2 + 5x + 3").SetIsMathText(True)

        # Append onameList with properly formatted LaTeX strings
        p10.onameList.append("Methods for finding cube roots")
        p10.onameList.append(r"1.\ Prime\ Factorization\ Method")
        p10.onameList.append(r"Let\ us\ find\ \sqrt[3]{1728}\ by\ Prime\ Factorization\ method")
        p10.onameList.append(r"Step\ 1:\ Resolving\ 1728\ into\ prime\ factors,\ we\ get")
        p10.onameList.append(r"1728 = 2 \times 2 \times 2 \times 2 \times 2 \times 2 \times 3 \times 3 \times 3")
        p10.onameList.append(r"Step\ 2:\ Make\ groups\ of\ three\ equal\ factors:")
        p10.onameList.append(r"1728 = (2 \times 2 \times 2) \times (2 \times 2 \times 2) \times (3 \times 3 \times 3)")
        p10.onameList.append(r"Step\ 3:\ Choose\ one\ factor\ from\ each\ group\ and\ multiply:")
        p10.onameList.append(r"\sqrt[3]{1728} = 2 \times 2 \times 3 = 12")
        p10.onameList.append(r"Therefore,\ \sqrt[3]{1728} = 12")
 
        # Render the CVO object
        self.construct2(p10, p10)

    def Estimatingthecuberootofanumber(self):
        # Create CVO object with mathematical text
        p10 = cvo.CVO().CreateCVO("Estimating the Cube Root of a Number", "").SetIsMathText(True)

        # Append onameList with properly formatted LaTeX strings
        p10.onameList.append("2. Estimating the Cube Root of a Number")
        p10.onameList.append(r"Let\ us\ find\ the\ cube\ root\ of\ 9261\ through\ estimation.")
        p10.onameList.append(r"Step\ 1:\ Start\ making\ groups\ of\ 3\ digits\ from\ the\ unit\ place.")
        p10.onameList.append(r"9\ (second\ group)\ \ \ 261\ (first\ group)")
        p10.onameList.append(r"Step\ 2:\ The\ first\ group,\ gives\ the\ units\ digit\ of\ cube\ number.")
        p10.onameList.append(r"As\ 261\ ends\ with\ 1,\ its\ cube\ root\ also\ ends\ with\ 1.")
        p10.onameList.append(r"So,\ the\ units\ place\ of\ the\ cube\ root\ will\ be\ 1.")
        p10.onameList.append(r"Step\ 3:\ Now,\ take\ the\ second\ group,\ 9.")
        p10.onameList.append(r"We\ know\ that\ 2^3\ <\ 9\ <\ 3^3.")
        p10.onameList.append(r"As\ the\ smallest\ number\ is\ 2,")
        p10.onameList.append(r"it\ becomes\ the\ tens\ place\ of\ the\ required\ cube\ root.")
        p10.onameList.append(r"Therefore,\ \sqrt[3]{9261} = 21")
        
        # Render the CVO object
        self.construct2(p10, p10)

    def SetDeveloperList(self):  
        self.DeveloperList="Raghu"

        
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="SquareandCubeRoots.py"


if _name_ == "_main_":
    scene = SquarecubeOperations()
    scene.render()