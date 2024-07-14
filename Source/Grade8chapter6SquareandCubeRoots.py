from manim import *
from AbstractAnim import AbstractAnim
import cvo

class SquarecubeOperations(AbstractAnim):

    def construct(self):

        self.RenderSkillbancLogo()
        self.Extra_text()
        self.fadeOutCurrentScene()
        #self.introduction()
        #self.fadeOutCurrentScene()
        self.SquaringOfNumbers()
        self.fadeOutCurrentScene()
        self.PerfectSquareandSquareNumber()
        self.fadeOutCurrentScene()
        self.SubtopicsOfSquares()
        self.fadeOutCurrentScene()
        self.PropertiesofSquareNumbers()
        self.fadeOutCurrentScene()
        self.InterestingPatternsofSquare()
        self.fadeOutCurrentScene()
        self.pythagoreanTriplets()
        self.fadeOutCurrentScene()
        self.SquareRoot()
        self.fadeOutCurrentScene()
        self.SquareandSquareroot_table()
        self.fadeOutCurrentScene()
        self.PrimeFactorization2()
        self.fadeOutCurrentScene()
        self.Subtractionofsuccessiveoddnumbers()
        self.fadeOutCurrentScene()
        #self.intro_text()
        #self.fadeOutCurrentScene()
        #self.division_steps()
        #self.fadeOutCurrentScene()
        self.squarerootsofnonperfectsquarenumbers()
        self.fadeOutCurrentScene()
        self.Cube()
        self.fadeOutCurrentScene()
        self.Cube_Table()
        self.fadeOutCurrentScene()
        self.CubeRoot()
        self.fadeOutCurrentScene()
        self.CubeandCubeRoot_table()
        self.fadeOutCurrentScene()
        self.cuberootthroughPrimeFactorization2()
        self.fadeOutCurrentScene()
        self.Estimatingthecuberootofanumber()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()


    def Extra_text(self):
        title = Text("Chapter6 : Square Roots and Cube Roots", font_size=48)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))
       

    def introduction(self):
        # p1=cvo.CVO().CreateCVO("cname","oname")

        p10=cvo.CVO().CreateCVO("Numbers","").setPosition([-5,0,0])
        p11=cvo.CVO().CreateCVO("Operations on Numbers","Squaring,Cubing").setPosition([-1,0,0])
        p12=cvo.CVO().CreateCVO("Squaring","$x^2$=x*x").setPosition([3.5,1,0])
        p13=cvo.CVO().CreateCVO("Cubing","$x^3$=x*x*x").setPosition([3.5,-2,0])
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)

        self.construct1(p10,p10)



    def SquaringOfNumbers(self):
        
        # self.angleChoice = [0,0,0]
        self.isRandom = False
    
        # Create CVO objects with their respective labels and positions
        p10 = cvo.CVO().CreateCVO("Squaring of Numbers", "").setPosition([-5, 1.25, 0])
        p11 = cvo.CVO().CreateCVO("Notation", "$x^2$").setPosition([-1, 1.25, 0])
        p12 = cvo.CVO().CreateCVO("Expansion", "$x^2 = x * x$").setPosition([3.5, 1.25, 0])
        p13 = cvo.CVO().CreateCVO("x variable", "3").setPosition([-1, -2, 0])
        p14 = cvo.CVO().CreateCVO("result", "9").setPosition([4, -2, 0])
    
        # Build the hierarchy of CVO objects
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
        p13.cvolist.append(p14)

        # Construct the animation from the root p10
        self.construct1(p10,p10)



    def PerfectSquareandSquareNumber(self):
        title = Text("Perfect Square and Square Number").to_edge(UP)
        self.play(Write(title))
        self.wait(0.7)

        # Perfect Square Section
        perfect_square_title = Text("Perfect Square", color=BLUE, font_size=39).shift(UP*2)
        perfect_square_def = Text("A rational number that is equal to the square of another rational number.", font_size=30).next_to(perfect_square_title, DOWN*1.25)
        self.play(Write(perfect_square_title))
        self.wait(0.8)
        self.play(Write(perfect_square_def))
        self.wait(1)

        # Example 1
        example1 = MarkupText(
            "<span foreground='PURPLE'>Example 1:</span>",
            font_size=34
        ).next_to(perfect_square_def, DOWN*2.75).to_edge(LEFT*5.5)
        perfect_square_ex1 = MathTex(r"\left(\frac{3}{2}\right)^2 = \frac{9}{4}", font_size=35).next_to(example1, RIGHT*2.25)
        explanation_ex1 = MathTex(r"\frac{9}{4} \text{ is a perfect square.}", font_size=34).next_to(perfect_square_ex1, DOWN*1.8).to_edge(LEFT*11.5)

        self.play(Write(example1))
        self.play(Write(perfect_square_ex1))
        self.wait(1)
        self.play(Write(explanation_ex1))
        self.wait(2)
        self.play(FadeOut(example1), FadeOut(perfect_square_ex1), FadeOut(explanation_ex1))

        # Example 2
        example2 = MarkupText(
            "<span foreground='PURPLE'>Example 2:</span>",
            font_size=34
        ).next_to(perfect_square_def, DOWN*2.75).to_edge(LEFT*5.5)
        perfect_square_ex2 = MathTex(r"4^2 = 16", font_size=35).next_to(example2, RIGHT*2.25)
        explanation_ex2 = Text("16 is a perfect square.", font_size=30).next_to(perfect_square_ex1, DOWN*1.8).to_edge(LEFT*11.5)

        self.play(Write(example2))
        self.play(Write(perfect_square_ex2))
        self.wait(1)
        self.play(Write(explanation_ex2))
        self.wait(2)
        self.play(FadeOut(example2), FadeOut(perfect_square_ex2), FadeOut(explanation_ex2))

        # Fade out the Perfect Square section
        self.play(FadeOut(perfect_square_title), FadeOut(perfect_square_def))

        # Square Number Section
        square_number_title = Text("Square Number", color=GREEN, font_size=39).shift(UP*2)
        square_number_def = Text("A number that is the product of an integer with itself.", font_size=30).next_to(square_number_title, DOWN*1.25)
        self.play(Write(square_number_title))
        self.wait(0.8)
        self.play(Write(square_number_def))
        self.wait(1)

        # Example 1
        example_sn1 = MarkupText(
            "<span foreground='PURPLE'>Example 1:</span>",
            font_size=34
        ).next_to(square_number_def, DOWN*2.75).to_edge(LEFT*5.5)
        square_number_ex1 = MathTex(r"3^2 = 9", font_size=35).next_to(example_sn1, RIGHT*2.25)
        explanation_sn_ex1 = Text("9 is a square number.", font_size=30).next_to(square_number_ex1, DOWN*1.8).to_edge(LEFT*11.5)

        self.play(Write(example_sn1))
        self.play(Write(square_number_ex1))
        self.wait(1)
        self.play(Write(explanation_sn_ex1))
        self.wait(2)
        self.play(FadeOut(example_sn1), FadeOut(square_number_ex1), FadeOut(explanation_sn_ex1))

        # Example 2
        example_sn2 = MarkupText(
            "<span foreground='PURPLE'>Example 2:</span>",
            font_size=34
        ).next_to(square_number_def, DOWN*2.75).to_edge(LEFT*5.5)
        square_number_ex2 = MathTex(r"(-5)^2 = 25", font_size=35).next_to(example_sn2, RIGHT*2.25)
        explanation_sn_ex2 = Text("25 is a square number.", font_size=30).next_to(square_number_ex2, DOWN*1.8).to_edge(LEFT*11.5)

        self.play(Write(example_sn2))
        self.play(Write(square_number_ex2))
        self.wait(1)
        self.play(Write(explanation_sn_ex2))
        self.wait(2)
        self.play(FadeOut(example_sn2), FadeOut(square_number_ex2), FadeOut(explanation_sn_ex2))

        self.play(FadeOut(square_number_title), FadeOut(square_number_def), FadeOut(title))
        self.wait(2)



    def SubtopicsOfSquares(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("sub topics of Square and Square Roots","").setPosition([0,2.5,0])
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
         p13=cvo.CVO().CreateCVO("Finding units place","").setPosition([5,1,0]).setangle(-TAU/4)
         p14=cvo.CVO().CreateCVO("Example","2.25=$(1.5)^2$=1.5*1.5").setPosition([-3,-3,0])
         p15=cvo.CVO().CreateCVO("Example","36=$(6)^2$=6*6").setPosition([0,-3,0])
         p16=cvo.CVO().CreateCVO("Example","$7^2$=7*7=49=9").setPosition([3,-3,0])
         p10.cvolist.append(p11)
         p10.cvolist.append(p12)
         p10.cvolist.append(p13)
         p11.cvolist.append(p14)
         p12.cvolist.append(p15)
         p13.cvolist.append(p16)
 
         self.construct1(p10,p10)
         #self.play()
    

    def InterestingPatternsofSquare(self):

        self.setNumberOfCirclePositions(7)
        self.colorChoice=[RED,BLUE,PURPLE,YELLOW,GREEN,ORANGE,PINK]

        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
        p10=cvo.CVO().CreateCVO("Interesting patterns of Square","Chapter:6.2").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Sum of first n odd numbers = $n^2$","$\sum_{i=1}^{n} (2i-1) = n^2$").setPosition([-4.12,1,0]).setangle(TAU/3)
        p12=cvo.CVO().CreateCVO("Numeric Palindrome","$1111^2$=1234321").setPosition([0,0,0]).setangle(-TAU/4)
        p13=cvo.CVO().CreateCVO("Numbers between sucessive squares","2*Base of the first Number").setPosition([4,1,0]).setangle(-TAU/3)
        p14=cvo.CVO().CreateCVO("Example","1+3+5+7=16=$4^2$").setPosition([-2.25,-2,0])
        p15=cvo.CVO().CreateCVO("Example","$1001^2$=1002001").setPosition([0,-2,0])
        p16=cvo.CVO().CreateCVO("Example","$2^2$=4;$3^2$=9=2*2=4").setPosition([2.25,-2,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p11.cvolist.append(p14)
        p12.cvolist.append(p15)
        p13.cvolist.append(p16)
 
    
        p11.setcircleradius(1.25)
        p12.setcircleradius(1.05)
        p14.setcircleradius(1.25)
        p15.setcircleradius(1.1)
        p16.setcircleradius(1.25)

 
        self.construct1(p10,p10)
        #self.play()

    def pythagoreanTriplets(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("pythagorean Triplets","Chapter:6.3").setPosition([-5,2.5,0])
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

        p10=cvo.CVO().CreateCVO("Square Root of Number",r"$\sqrt{x}$").setPosition([-4.5,1,0])
        p11=cvo.CVO().CreateCVO("x variable","9").setPosition([-2,-2,0])
        p12=cvo.CVO().CreateCVO("Square root of x",r"$\sqrt{9}$=3*3").setPosition([2,-2,0])
        p13=cvo.CVO().CreateCVO("result","3").setPosition([5.7,-1,0])
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)

        p10.setcircleradius(1.25)
        p11.setcircleradius(1.25)
        p12.setcircleradius(1.25)
        p13.setcircleradius(1.25)
        

        self.construct1(p10,p10)
        #self.play()


    
    def SquareandSquareroot_table(self):

        table_data = [
            ["Square", "Square roots"],
            ["1² = 1", "√1 = 1"],
            ["2² = 4", "√4 = 2"],
            ["3² = 9", "√9 = 3"],
            ["4² = 16", "√16 = 4"],
            ["5² = 25", "√25 = 5"], 
            ["6² = 36", "√36 = 6"],
            ["7² = 49", "√49 = 7"],
            ["8² = 64", "√64 = 8"],
            ["9² = 81", "√81 = 9"],
            ["10² = 100", "√100 = 10"],
        ]

        # Create the table with the title
        table = Table(
            table_data,
            include_outer_lines=True,
            h_buff=1.5,
            v_buff=0.4
        )
        

        # Change the color of the table lines to blue
        table.get_horizontal_lines().set_color(BLUE)
        table.get_vertical_lines().set_color(BLUE)

        # Change the color of the headings to pink
        table.get_entries((1, 1)).set_color(PINK)
        table.get_entries((1, 2)).set_color(PINK)

        # Position the table at the center of the scene
        table.scale(0.6)
        table.move_to(ORIGIN)

        # Play the title and table together
        self.play(Create(table.get_horizontal_lines()), Create(table.get_vertical_lines()))
        self.wait(1)

        # Sequentially play each cell in the table
        for row in table.get_entries():
            for cell in row:
                self.play(FadeIn(cell))
                self.wait(0.5)

        self.wait(2)




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
    


    def Cube(self):
        # self.angleChoice = [0,0,0]
        self.isRandom = False
    
        # Create CVO objects with their respective labels and positions
        p10 = cvo.CVO().CreateCVO("Cubing of Numbers", "").setPosition([-5, 1.25, 0])
        p11 = cvo.CVO().CreateCVO("Notation", "$x^3$").setPosition([-1, 1.25, 0])
        p12 = cvo.CVO().CreateCVO("Expansion", "$x^3 = x * x * x$").setPosition([3.5, 1.25, 0])
        p13 = cvo.CVO().CreateCVO("x variable", "4").setPosition([-1, -2, 0])
        p14 = cvo.CVO().CreateCVO("result", "64").setPosition([4, -2, 0])
    
        # Build the hierarchy of CVO objects
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
        p13.cvolist.append(p14)

        # Construct the animation from the root p10
        self.construct1(p10,p10)



    def Cube_Table(self):

        table_data =[

            ["Number", "Cube"],
            ["1", "1³ = 1 * 1 * 1 = 1"],
            ["2", "2³ = 2 * 2 * 2 = 8"],
            ["3", "3³ = 3 * 3 * 3 = 27"],
            ["4", "4³ = 4 * 4 * 4 = 64"],
            ["5", "5³ = 5 * 5 * 5 = 125"],
            ["6", "6³ = 6 * 6 * 6 = 216"],
            ["7", "7³ = 7 * 7 * 7 = 343"],
            ["8", "8³ = 8 * 8 * 8 = 512"],
            ["9", "9³ = 9 * 9 * 9 = 729"],
            ["10", "10³ = 10 * 10 * 10 = 1000"],
        ]

        # Create the table with the title
        table = Table(
            table_data,
            include_outer_lines=True,
            h_buff=1.6,
            v_buff=0.45
        )
        
        # Change the color of the table lines to blue
        table.get_horizontal_lines().set_color(BLUE)
        table.get_vertical_lines().set_color(BLUE)

        # Change the color of the headings to pink
        table.get_entries((1, 1)).set_color(GOLD)
        table.get_entries((1, 2)).set_color(GOLD)


        # Position the table at the center of the scene
        table.scale(0.6)
        table.move_to(ORIGIN)


        # Play the title and table together
        self.play( Create(table.get_horizontal_lines()), Create(table.get_vertical_lines()))
        self.wait(1)

        # Sequentially play each cell in the table
        for row in table.get_entries():
            for cell in row:
                self.play(FadeIn(cell))
                self.wait(0.5)

        self.wait(2)



    def CubeRoot(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Cube root of Numbers",r"$\sqrt[3]{x}$").setPosition([-4.5,1,0])
        p11=cvo.CVO().CreateCVO("X variable","64").setPosition([-2,-2,0])
        p12=cvo.CVO().CreateCVO("Cuberoot of 64",r"$\sqrt[3]{64}$=$\sqrt[3]{4*4*4}$").setPosition([2,-2,0])
        p13=cvo.CVO().CreateCVO("result","4").setPosition([5.7,-1,0])
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)

        p10.setcircleradius(1.25)
        p11.setcircleradius(1.25)
        p12.setcircleradius(1.25)
        p13.setcircleradius(1.25)
        
        self.construct1(p10,p10)
        #self.play()


    def CubeandCubeRoot_table(self):

        table_data = [
            ["Cube",  "Cube roots"],
            ["1³ = 1", "∛1 = 1"],
            ["2³ = 8", "∛8 = 2"],
            ["3³ = 27", "∛27 = 3"],
            ["4³ = 64", "∛64 = 4"],
            ["5³ = 125", "∛125 = 5"],
            ["6³ = 216", "∛216 = 6"],
            ["7³ = 343", "∛343 = 7"],
            ["8³ = 512", "∛512 = 8"],
            ["9³ = 729", "∛729 = 9"],
            ["10³ = 1000", "∛1000 = 10"],
        ]
        
        # Create the table with the title
        table = Table(
            table_data,
            include_outer_lines=True,
            h_buff=1.7,
            v_buff=0.4
        )
        
        # Change the color of the table lines to blue
        table.get_horizontal_lines().set_color(BLUE)
        table.get_vertical_lines().set_color(BLUE)

        # Change the color of the headings to pink
        table.get_entries((1, 1)).set_color(PINK)
        table.get_entries((1, 2)).set_color(PINK)


        # Position the table at the center of the scene
        table.scale(0.6)
        table.move_to(ORIGIN)


        # Play the title and table together
        self.play(Create(table.get_horizontal_lines()), Create(table.get_vertical_lines()))
        self.wait(1)

        # Sequentially play each cell in the table
        for row in table.get_entries():
            for cell in row:
                self.play(FadeIn(cell))
                self.wait(0.5)

        self.wait(2)

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
        self.SourceCodeFileName="SquareRootsandCubeRoots.py"


if __name__ == "__main__":
    scene = SquarecubeOperations()
    scene.render()