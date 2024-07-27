from manim import *
from AbstractAnim import AbstractAnim
import cvo
from numpy import size
class Grade8Ch1RationalNumbers(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.intro1()
        self.fadeOutCurrentScene()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.Addition()
        self.fadeOutCurrentScene()
        self.additionexample()
        self.fadeOutCurrentScene()
        self.Subtraction()
        self.fadeOutCurrentScene()
        self.subtractionexample()
        self.fadeOutCurrentScene()
        self.Multiplication()
        self.fadeOutCurrentScene()
        self.examplemul()
        self.fadeOutCurrentScene()
        self.Division()
        self.fadeOutCurrentScene()
        self.divisionexample1()
        self.fadeOutCurrentScene()
        self.divisionexample2()
        self.fadeOutCurrentScene()
        self.prop ()
        self.fadeOutCurrentScene()
        self.commutativepropexample()
        self.fadeOutCurrentScene()
        self.associativepropexample()
        self.fadeOutCurrentScene()
        self.distributivepropexample()
        self.fadeOutCurrentScene()
        self.Rules()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
       

    def Introduction(self):
        
        count = 0
        # starting object
        p10=cvo.CVO().CreateCVO("Rational Numbers","").setPosition([-5.5,0,0])
        count += 1

                # 2nd c2 object
        # p12=cvo.CVO().CreateCVO("Examples","1/2,10,7/2,-3/2").setPosition([3,0,0])
        # count += 1
        # # Level 2
        # p13=cvo.CVO().CreateCVO("Project","Manim-Templates")
        # count += 1
        # p12.cvolist.append(p13)
        
        # p10.cvolist.append(p12)
        
        # Level 1 First c2 object
        p11=cvo.CVO().CreateCVO("operations","").setPosition([-3,0,0])
        count += 1
        # Level 2 


        p15=cvo.CVO().CreateCVO("Addition","+").setPosition([4.5,2.6,0])
        count += 1
        p11.cvolist.append(p15)

        p16=cvo.CVO().CreateCVO("Subtraction","-").setPosition([5.5,0,0])
        count += 1
        p11.cvolist.append(p16)

        p17=cvo.CVO().CreateCVO("Multiplication","X").setPosition([4.5,-2.3,0])
        count += 1
        p11.cvolist.append(p17)

        p14=cvo.CVO().CreateCVO("Division","/").setPosition([2,-2.3,0])
        p11.cvolist.append(p14)
        
        p10.cvolist.append(p11)
        self.angleChoice = [TAU/4,-TAU/4,-TAU/4,-TAU/4,-TAU/4]
        self.isRandom = False
            


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
   
    def intro1(self):
        # Title
        title = Text("Understanding Rational Numbers",color=RED ,font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Definition of rational numbers
        definition = Text("A rational number is any number that can be written as",color=RED_A, font_size=24)
        fraction = MathTex(r"\frac{p}{q}",color=BLUE, font_size=48)
        condition = Text("where p and q are integers and q ≠ 0.", font_size=24)

        self.play(Write(definition))
        self.play(Write(fraction.next_to(definition, DOWN, buff=0.5)))
        self.play(Write(condition.next_to(fraction, DOWN, buff=0.5)))
        self.wait(2)

        self.play(FadeOut(definition), FadeOut(condition))
        self.play(fraction.animate.to_edge(UP*2.2))

        # Examples of rational numbers
        examples_title = Text("Examples of Rational Numbers",color=ORANGE ,font_size=36)
        self.play(Write(examples_title.next_to(fraction, DOWN, buff=1)))
        self.wait(1)

        examples = [
            ("", MathTex(r"Positive={3}/{4}", font_size=48)),
            ("", MathTex(r"Negative={-5}/{8}", font_size=48)),
            ("", MathTex(r"Integer={2}/{1}", font_size=48)),
            ("", MathTex(r"zero={0}/{1}", font_size=48))
        ]

        positions = [
            LEFT * 3 + UP * 0,
            RIGHT * 3 + UP * 0,
            LEFT * 3 + DOWN * 1.5,
            RIGHT * 3 + DOWN * 1.5,
        ]

        for (label, example), position in zip(examples, positions):
            label_text = Text(label, font_size=24).next_to(position, UP)
            example.move_to(position)
            self.play(Write(label_text), FadeIn(example))
            self.wait(1)

        # Concluding visualization
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        conclusion = Text("Rational numbers can be positive, negative, integers, or zero", font_size=30,color=GOLD)
        self.play(Write(conclusion))
        self.wait(2)

    def Addition(self):
        # self.setNumberOfCirclePositions(4)
        # #self.angleChoice = [0,0,0]
        # self.isRandom = False

        # p10=cvo.CVO().CreateCVO("Addition of RationalNumbers","X+Y")
        # p11=cvo.CVO().CreateCVO("X variable","2/3").setPosition([4.5,-2.7,0])
        # p12=cvo.CVO().CreateCVO("Y variable","3/4").setPosition([-3,2,0])
        # p13=cvo.CVO().CreateCVO("Sum", "(2/3)+(3/4)= ((2*4)+(3*3))/(3*4) = 17/12").setPosition([4,1.2,0])
        # p13.setcircleradius(2.8)
        # p10.cvolist.append(p11)
        # p10.cvolist.append(p12)
        # self.construct1(p10,p10)
        # self.construct1(p13,p13)
        # self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        
        self.isRandom = False
        self.angleChoice = [-TAU/2,TAU/5,TAU/5,-TAU/2,-TAU/2]
        p10=cvo.CVO().CreateCVO("Addition of Rational numbers","X + Y").setPosition([-4,-2.5,0])
        p7= cvo.CVO().CreateCVO("x,y values", "X=2/3,Y=3/4").setPosition([-4,2.5,0])
        # p7onamelist=["x=2/3","y=3/4"]
        p13=cvo.CVO().CreateCVO("Step 1", "(2/3)+(3/4)").setPosition([0,2.5,0])
        p14=cvo.CVO().CreateCVO("Step 2", "((2X4)+(3X3))/(3X4)").setPosition([5,2.5,0])
        p15=cvo.CVO().CreateCVO("Step 3", "(8+9)/12").setPosition([5,0,0])
        p16=cvo.CVO().CreateCVO("Answer", "17/12").setPosition([5,-2.5,0])
        
        p10.cvolist.append(p7)
        # p7.extendOname(p7onamelist)
        p7.cvolist.append(p13)
        p13.cvolist.append(p14)
        p14.setcircleradius(1.4)
        p14.cvolist.append(p15)
        p15.cvolist.append(p16)
        p15.setcircleradius(1.4)
        self.construct1(p10,p10)
        self.setNumberOfCirclePositions(6)

    def Subtraction(self):
        # self.setNumberOfCirclePositions(4)
        # #self.angleChoice = [0,0,0]
        # self.isRandom = False

        # p10=cvo.CVO().CreateCVO("Subtraction of Rational Numbers","x-y")
        # p11=cvo.CVO().CreateCVO("Variable x","4/3")
        # p12=cvo.CVO().CreateCVO("Variable y","3/3")
        # p13=cvo.CVO().CreateCVO("Difference", "(4/3)/(3/3)=(4-3)/3 = 1/3")
        # p13.setcircleradius(2)
        # p10.cvolist.append(p11)
        # p10.cvolist.append(p12)
        # self.construct1(p10,p10)
        # self.construct1(p13,p13)
        # self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        # #self.play()

        self.isRandom = False
        self.angleChoice = [-TAU/2,TAU/5,TAU/5,-TAU/2,-TAU/2]
        p10=cvo.CVO().CreateCVO("subtraction of Rational numbers","X - Y").setPosition([-4,-2.5,0])
        p7= cvo.CVO().CreateCVO("x,y values", "X=4/3,Y=3/3").setPosition([-4,2.5,0])
        # p7onamelist=["x=4/3","y=3/3"]
        p13=cvo.CVO().CreateCVO("Step 1", "(4/3)-(3/3)").setPosition([0,2.5,0])
        p14=cvo.CVO().CreateCVO("Step 2", "(4-3)/3").setPosition([5,2.5,0])
        p15=cvo.CVO().CreateCVO("Answer", "1/3").setPosition([5,0,0])
        # p16=cvo.CVO().CreateCVO("Answer", "1/5").setPosition([5,-2.5,0])
        
        p10.cvolist.append(p7)
        # p7.extendOname(p7onamelist)
        p7.cvolist.append(p13)
        p13.cvolist.append(p14)
        p14.cvolist.append(p15)
        # p15.cvolist.append(p16)
        p15.setcircleradius(1.4)
        self.construct1(p10,p10)
        self.setNumberOfCirclePositions(6)

    def Multiplication(self):
        # self.setNumberOfCirclePositions(4)
        # #self.angleChoice = [0,0,0]
        # self.isRandom = False

        # p10=cvo.CVO().CreateCVO("Multiplication of Rational Numbers","X*Y")
        # p11=cvo.CVO().CreateCVO("X variable","2/3")
        # p12=cvo.CVO().CreateCVO("Y variable","3/4")
        # p13=cvo.CVO().CreateCVO("Product", "(2/3)*(3/4)=(2*3)/(3*4) = 6/12")
        # p13.setcircleradius(2)
        # p10.cvolist.append(p11)
        # p10.cvolist.append(p12)
        # self.construct1(p10,p10)
        # self.construct1(p13,p13)
        # self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        # #self.play()

        self.isRandom = False
        self.angleChoice = [-TAU/2,TAU/5,TAU/5,-TAU/2,-TAU/2]
        p10=cvo.CVO().CreateCVO("Multiplication of Rational numbers","X * Y").setPosition([-4,-2.5,0])
        p7= cvo.CVO().CreateCVO("x,y values", "X=2/3,Y=3/4").setPosition([-4,2.5,0])
        # p7onamelist=["x=2/3","y=3/4"]
        p13=cvo.CVO().CreateCVO("Step 1", "(2/3) X (3/4)").setPosition([0,2.5,0])
        p14=cvo.CVO().CreateCVO("Step 2", "(2 x 3) / (3 x 4)").setPosition([5,2.5,0])
        p15=cvo.CVO().CreateCVO("Step 3", "6/12").setPosition([5,0,0])
        p16=cvo.CVO().CreateCVO("Answer", "1/2").setPosition([5,-2.5,0])
        
        p10.cvolist.append(p7)
        # p7.extendOname(p7onamelist)
        p7.cvolist.append(p13)
        p13.cvolist.append(p14)
        p14.setcircleradius(1.3)
        p14.cvolist.append(p15)
        p15.cvolist.append(p16)
        p15.setcircleradius(1.4)
        self.construct1(p10,p10)
        self.setNumberOfCirclePositions(6)

         

    def Division(self):
        self.isRandom = False
        self.angleChoice = [-TAU/2,TAU/5,TAU/5,-TAU/2,-TAU/2]
        p10=cvo.CVO().CreateCVO("Division of Rational numbers","X / Y").setPosition([-4,-2.5,0])
        p7= cvo.CVO().CreateCVO("x,y values", "X=1/2,Y=5/2").setPosition([-4,2.5,0])
        # p7onamelist=["x=1/2","y=5/2"]
        p13=cvo.CVO().CreateCVO("Step 1", "(1/2)/(5/2)").setPosition([0,2.5,0])
        p14=cvo.CVO().CreateCVO("Step 2", "(1/2)*(2/5)").setPosition([5,2.5,0])
        p15=cvo.CVO().CreateCVO("Step 3", "(1/2)*(2/5)=2/10").setPosition([5,0,0])
        p16=cvo.CVO().CreateCVO("Answer", "1/5").setPosition([5,-2.5,0])
        
        p10.cvolist.append(p7)
        # p7.extendOname(p7onamelist)
        p7.cvolist.append(p13)
        p13.cvolist.append(p14)
        p14.cvolist.append(p15)
        p15.cvolist.append(p16)
        p15.setcircleradius(1.4)
        self.construct1(p10,p10)
        self.setNumberOfCirclePositions(6)

    def prop(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("Properties","").setPosition([0,2.5,0])
         p11=cvo.CVO().CreateCVO("closure","Result of mathematical operation on operands\n belongs to the same group of operands").setPosition([3 ,1,0])
         p12=cvo.CVO().CreateCVO("Commutative ","a+b=b+a (or) a*b=b*a").setPosition([3,-2,0])
         p13=cvo.CVO().CreateCVO("Associative","a+(b+c)=(a+b)+c (or) a*(b*c)=(a*b)*c").setPosition([-3,-2,0]).setangle(-TAU/4)
         p14=cvo.CVO().CreateCVO("Distributive","a*(b+c)=(a*b)+(a*c)").setPosition([-4,2,0]).setangle(-TAU/4)
         p12.setcircleradius(2)
         p13.setcircleradius(2)
         p14.setcircleradius(2)
         p10.cvolist.append(p12)
         p10.cvolist.append(p11)
         p10.cvolist.append(p13)
         p10.cvolist.append(p14)
         self.construct1(p10,p10)
         self.play  

    def propexample(self):
        title = Text("Property Examples",color=PURPLE).to_edge(UP)
        self.play(Write(title))

        examples = [
        r"\text{associative property :} \quad 4+(3+2) = (4+3)+2 \quad\text{or}\quad 5\times(3\times2)=(5\times3)\times2",
        r"\text{commutative property :} \quad 6 \times 3 = 3 \times 6 \quad \text{or} \quad 6 + 3 =3 + 6",
        r"\text{distributive property:} \quad 3 \times (2+1) = 3\times2 +3\times 1",
        
        ]
        example1 = MathTex(examples[0]).scale(0.8).next_to(title, DOWN, buff=1)
        example2 = MathTex(examples[1]).scale(0.8).next_to(example1, DOWN, aligned_edge=LEFT, buff=0.5)
        example3 = MathTex(examples[2]).scale(0.8).next_to(example2, DOWN, aligned_edge=LEFT, buff=0.5)
        # example4 = MathTex(examples[3]).scale(0.8).next_to(example3, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(Write(example1))
        self.wait(1)
        self.play(Write(example2))
        self.wait(1)
        self.play(Write(example3))
        self.wait(1)
        # self.play(Write(example4))
        # self.wait(1)
 
        self.wait(3)   
         
    def Rules(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("Identities","").setPosition([0,2.5,0])
         p11=cvo.CVO().CreateCVO("Additive identity ","x+0 =x").setPosition([3 ,1,0])
         p12=cvo.CVO().CreateCVO("Multiplicative identity "," x*1 =x").setPosition([3,-2,0])
         p13=cvo.CVO().CreateCVO("Multiplicative Inverse","a/b X b/a = 1").setPosition([-3,-2,0]).setangle(-TAU/4)
         p10.cvolist.append(p12)
         p10.cvolist.append(p11)
         p10.cvolist.append(p13) 
         self.construct1(p10,p10)
       
  
    def examplemul(self):
        # Title
        title = Text("Multiplying Rational Numbers", font_size=36,color=RED)
        title.to_edge(UP)
        
        # Explanation text
        explanation_text = Text(
            "Now, we learn how to multiply the rational numbers. "
            "Consider the rational numbers ",color=BLUE
            ).scale(0.5).next_to(title, DOWN)
        
        # Rational numbers
        rational_numbers = MathTex(
            "\\frac{2}{3}", "\\text{ and }", "\\frac{5}{7}"
            ).scale(0.8).next_to(explanation_text, DOWN)
        
        # Multiplication statement
        multiply_statement = Text("We multiply").scale(0.5).next_to(rational_numbers, DOWN)
        
        # Equation
        equation = MathTex(
            "\\frac{2}{3}", "\\times", "\\frac{5}{7}", "=", "\\frac{2 \\times 5}{3 \\times 7}", "=", "\\frac{10}{21}"
            ).scale(0.8).next_to(multiply_statement, DOWN)
        
        # Explanation of steps
        # steps_explanation = Text(
        #     "(Product of numerator) \n\n(Product of denominator)"
        #     ).scale(0.5).next_to(equation, DOWN)
        
        # Add and animate
        self.play(Write(title))
        self.wait(1)
        
        self.play(Write(explanation_text))
        self.wait(2)
        
        self.play(Write(rational_numbers))
        self.wait(1)
        
        self.play(Write(multiply_statement))
        self.wait(1)
        
        self.play(Write(equation))
        self.wait(2)
        
        # self.play(Write(steps_explanation))
        self.wait(3)

    def divisionexample1(self):
    
        # Title
        title = Text("Division of Rational Numbers",color=RED, font_size=36)
        title.to_edge(UP)
        
        # Instruction text
        instruction_text = Text(
            "Observe the following",color=BLUE
        ).scale(0.5).next_to(title, DOWN)
        
        # Equations showing multiplicative inverse
        equation1 = MathTex(
            "\\frac{2}{5}", "\\times", "\\frac{5}{2}", "=", "1"
        ).scale(0.8).next_to(instruction_text, DOWN)
        
        equation2 = MathTex(
            "\\frac{-9}{11}", "\\times", "\\frac{11}{-9}", "=", "1"
        ).scale(0.8).next_to(equation1, DOWN)
        
        # Explanation text
        explanation_text = Text(
            "Here we notice that the product is '1'. If the product of any two \nrational numbers is '1' they are called"
            "the multiplicative inverse of each other. Here",color=BLUE_A
        ).scale(0.5).next_to(equation2, DOWN)
        
        explanation_text_2 = MathTex(
            "\\frac{2}{5}", "\\text{ and }", "\\frac{5}{2}", ";", "\\frac{-9}{11}", "\\text{ and }", "\\frac{11}{-9}"
        ).scale(0.8).next_to(explanation_text, DOWN)

        explanation_text_3 = Text(
            "are multiplicative inverses of each other."
        ).scale(0.5).next_to(explanation_text_2, DOWN)
        
        # Add and animate
        self.play(Write(title))
        self.wait(1)
        
        self.play(Write(instruction_text))
        self.wait(1)
        
        self.play(Write(equation1))
        self.wait(2)
        
        self.play(Write(equation2))
        self.wait(2)
        
        self.play(Write(explanation_text))
        self.wait(2)
        
        self.play(Write(explanation_text_2))
        self.wait(2)
        
        self.play(Write(explanation_text_3))
        self.wait(4)

    def associativepropexample(self):
        # Title
        title = Text("Associative Property Example", font_size=40,color=RED)
        title.to_edge(UP)
 
        # Rational numbers and equation setup
        intro_text = MathTex(r"\frac{2}{7},{5},\frac{1}{2}",font_size=35)
        intro_text.next_to(title, DOWN, buff=0.5)
        
        eq1 = MathTex(r"\frac{2}{7}", r"+", r"\left[ 5 + \left( \frac{1}{2} \right) \right]", r"=", r"\left[ \left( \frac{2}{7} + 5 \right) \right] + \left( \frac{1}{2} \right)",font_size=26)
        
        lhs_title = Text("L.H.S.", font_size=30)
        lhs1 = MathTex(r"=", r"\frac{2}{7}", r"+", r"\left[ 5 + \left( \frac{1}{2} \right) \right]",font_size=26)
        lhs2 = MathTex(r"=", r"\frac{2}{7}", r"+", r"\left[ \frac{10 + 1}{2} \right]",font_size=26)
        lhs3 = MathTex(r"=", r"\frac{2}{7}", r"+", r"\left[ \frac{11}{2} \right]",font_size=26)
        lhs4 = MathTex(r"=", r"\frac{4 + 77}{14}",font_size=26)
        lhs5 = MathTex(r"=", r"\frac{81}{14}",font_size=26)
        
        rhs_title = Text("R.H.S.", font_size=30)
        rhs1 = MathTex(r"=", r"\left[ \frac{2}{7} + 5 \right] + \frac{1}{2}",font_size=26)
        rhs2 = MathTex(r"=", r"\left[ \frac{2 + 35}{7} \right] + \frac{1}{2}",font_size=26)
        rhs3 = MathTex(r"=", r"\frac{37}{7} + \frac{1}{2}",font_size=26)
        rhs4 = MathTex(r"=", r"\frac{74 + 7}{14}",font_size=26)
        rhs5 = MathTex(r"=", r"\frac{81}{14}",font_size=26)
        
        # Position elements
        eq1.next_to(intro_text, DOWN, buff=0.5)
        
        lhs_title.next_to(eq1, DOWN,buff=1).to_edge(LEFT*3)
        lhs1.next_to(lhs_title, DOWN)
        lhs2.next_to(lhs1, DOWN)
        lhs3.next_to(lhs2, DOWN)
        lhs4.next_to(lhs3, RIGHT)
        lhs5.next_to(lhs4,RIGHT)
        
        rhs_title.next_to(lhs_title, RIGHT*5, buff=1)
        rhs1.next_to(rhs_title, DOWN)
        rhs2.next_to(rhs1, DOWN)
        rhs3.next_to(rhs2, DOWN)
        rhs4.next_to(rhs3, RIGHT)
        rhs5.next_to(rhs4, RIGHT)
        
        # Display equations
        self.play(Write(title))
        self.play(Write(intro_text))
        
        self.play(Write(eq1))
        self.wait(1)
        
        self.play(Write(lhs_title))
        self.play(Write(lhs1))
        self.wait(1)
        self.play(Write(lhs2))
        self.wait(1)
        self.play(Write(lhs3))
        self.wait(1)
        self.play(Write(lhs4))
        self.wait(1)
        self.play(Write(lhs5))
        self.wait(1)
        
        self.play(Write(rhs_title))
        self.play(Write(rhs1))
        self.wait(1)
        self.play(Write(rhs2))
        self.wait(1)
        self.play(Write(rhs3))
        self.wait(1)
        self.play(Write(rhs4))
        self.wait(1)
        self.play(Write(rhs5))
        self.wait(1)

        # Emphasize the final results
        box1 = SurroundingRectangle(lhs5, color=YELLOW, buff=0.1)
        box2 = SurroundingRectangle(rhs5, color=YELLOW, buff=0.1)
        
        self.play(Create(box1))
        self.wait(1)
        self.play(Create(box2))
        self.wait(1)

        self.play(Uncreate(box1), Uncreate(box2))
        self.wait(1)

        
    def distributivepropexample(self):
        # Title
        title = Text(" Distributive Property Example", font_size=36,color=RED)
        title.to_edge(UP)

        # Rational numbers and equation setup
        intro_text =  MathTex( r"\frac{2}{5},\frac{1}{2},\frac{3}{4}", font_size=36)
        intro_text.next_to(title, DOWN, buff=0.5)
        
        eq1 = MathTex(r"\frac{2}{5} \times \left( \frac{1}{2} + \frac{3}{4} \right) = \left( \frac{2}{5} \right) \times \left( \frac{1}{2} \right) + \left( \frac{2}{5} \right) \times \left( \frac{3}{4} \right)", font_size=26)
        
        lhs_title = Text("L.H.S.", font_size=30)
        lhs1 = MathTex(r"=", r"\frac{2}{5} \times \left( \frac{1}{2} + \frac{3}{4} \right)", font_size=26)
        lhs2 = MathTex(r"=", r"\frac{2}{5} \times \left( \frac{2 + 3}{4} \right)", font_size=26)
        lhs3 = MathTex(r"=", r"\frac{2}{5} \times \left( \frac{5}{4} \right)", font_size=26)
        lhs4 = MathTex(r"=", r"\frac{10}{20}", font_size=26)
        lhs5 = MathTex(r"=", r"\frac{1}{2}", font_size=26)
        
        rhs_title = Text("R.H.S.", font_size=30)
        rhs1 = MathTex(r"=", r"\frac{2}{5} \times \left( \frac{1}{2} \right) + \frac{2}{5} \times \left( \frac{3}{4} \right)", font_size=26)
        rhs2 = MathTex(r"=", r"\frac{2}{10} + \frac{6}{20}", font_size=26)
        rhs3 = MathTex(r"=", r"\frac{4}{20} + \frac{6}{20}", font_size=26)
        rhs4 = MathTex(r"=", r"\frac{10}{20}", font_size=26)
        rhs5 = MathTex(r"=", r"\frac{1}{2}", font_size=26)
        
        # Position elements
        eq1.next_to(intro_text, DOWN, buff=0.5)
        
        lhs_title.next_to(eq1, DOWN, buff=1).to_edge(LEFT*3)
        lhs1.next_to(lhs_title, DOWN)
        lhs2.next_to(lhs1, DOWN)
        lhs3.next_to(lhs2, DOWN)
        lhs4.next_to(lhs3, RIGHT)
        lhs5.next_to(lhs4, RIGHT)
        
        rhs_title.next_to(lhs_title, RIGHT*5, buff=1)
        rhs1.next_to(rhs_title, DOWN)
        rhs2.next_to(rhs1, DOWN)
        rhs3.next_to(rhs2, DOWN)
        rhs4.next_to(rhs3, RIGHT)
        rhs5.next_to(rhs4, RIGHT)
        
        # Display equations
        self.play(Write(title))
        self.play(Write(intro_text))
        
        self.play(Write(eq1))
        self.wait(1)
        
        self.play(Write(lhs_title))
        self.play(Write(lhs1))
        self.wait(1)
        self.play(Write(lhs2))
        self.wait(1)
        self.play(Write(lhs3))
        self.wait(1)
        self.play(Write(lhs4))
        self.wait(1)
        self.play(Write(lhs5))
        self.wait(1)
        
        self.play(Write(rhs_title))
        self.play(Write(rhs1))
        self.wait(1)
        self.play(Write(rhs2))
        self.wait(1)
        self.play(Write(rhs3))
        self.wait(1)
        self.play(Write(rhs4))
        self.wait(1)
        self.play(Write(rhs5))
        self.wait(1)

        # Emphasize the final results
        box1 = SurroundingRectangle(lhs5, color=YELLOW, buff=0.1)
        box2 = SurroundingRectangle(rhs5, color=YELLOW, buff=0.1)
        
        self.play(Create(box1))
        self.wait(1)
        self.play(Create(box2))
        self.wait(1)

        self.play(Uncreate(box1), Uncreate(box2))
        self.wait(1)

    def divisionexample2(self):
        # Title
        title = Text("Division of Rational Numbers", font_size=36,color=RED)
        title.to_edge(UP)
        
        # Explanation text
        explanation_text = Text(
            "Consider the rational number ",color=BLUE
        ).scale(0.5).next_to(title, DOWN)
        
        # Rational numbers
        rational_numbers = MathTex(
            "\\frac{3}{4}", "\\text{ and }", "\\frac{7}{11}",color=ORANGE
        ).scale(0.8).next_to(explanation_text, DOWN)
        
        # Division statement
        division_statement = Text("We divide ").scale(0.5).next_to(rational_numbers, DOWN*1)
        division_statement_2 = MathTex("\\frac{3}{4}", "\\text{ with }", "\\frac{7}{11}").scale(0.8).next_to(division_statement, RIGHT)
        
        # Equation steps
        equation1 = MathTex(
            "\\frac{3}{4}", "\\div", "\\frac{7}{11}", "=", "\\frac{3}{4}", "\\times", "\\frac{11}{7}",
        ).scale(0.8).next_to(explanation_text , DOWN*8)

        inverse1=MathTex("(\\frac{11}{7}\quad",color=RED_B).next_to(equation1, RIGHT)
        inverse_explanation = Text(" Is Multiplicative inverse of ", font_size=20).next_to(inverse1, RIGHT)
        inverse_number = MathTex("\\frac{7}{11})",color=RED_B).next_to(inverse_explanation, RIGHT)
        
        equation2 = MathTex(
            "=", "\\frac{3 \\times 11}{4 \\times 7}", "=", "\\frac{33}{28}"
        ).scale(0.8).next_to(equation1, DOWN)
        
        final_simplification = MathTex(
            "=", "\\frac{33}{28}"
        ).scale(0.8).next_to(equation2, DOWN)

        # Add and animate
        self.play(Write(title))
        self.wait(1)
        
        self.play(Write(explanation_text))
        self.wait(1)
        
        self.play(Write(rational_numbers))
        self.wait(1)
        
        self.play(Write(division_statement))
        self.wait(1)
        
        self.play(Write(division_statement_2))
        self.wait(1)
        
        self.play(Write(equation1))
        self.wait(2)

        self.play(Write(inverse1))
        self.play(Write(inverse_explanation))
        self.play(Write(inverse_number))
        self.wait(2)
        
        self.play(Write(equation2))
        self.wait(2)
        
        self.play(Write(final_simplification))
        self.wait(4)
    def additionexample(self):
         
        title = Text("ADDITION OF RATIONAL NUMBERS",color=RED)
        title.to_edge(UP)

        subtitle = Text("Consider the Rational Numbers",color=BLUE,font_size=25)
        subtitle.next_to(title, DOWN)

        self.play(Write(title))
        self.play(Write(subtitle))

        # Display the two rational numbers
        r1 = MathTex(r"\frac{2}{7}\quad\text{and}")
        r2 = MathTex(r"\frac{5}{8}")
        r1.next_to(subtitle, DOWN, buff=1)
        r2.next_to(r1, RIGHT, buff=1)

        self.play(Write(r1), Write(r2))

        # Show the addition process
        addition = MathTex(r"\frac{2}{7} + \frac{5}{8}")
        equals = MathTex("=")
        addition.next_to(r1, DOWN, buff=1)
        equals.next_to(addition, RIGHT, buff=1)
        self.play(Write(addition), Write(equals))

        # Show the intermediate step
        intermediate = MathTex(r"\frac{16 + 35}{56}")
        intermediate.next_to(equals, RIGHT, buff=1)
        self.play(Write(intermediate))

        # Show the final result
        result = MathTex(r"")
        result.next_to(intermediate, RIGHT, buff=1)
        self.play(Write(result))

        # Final display
        final_result = MathTex(r"\frac{16}{56} + \frac{35}{56} = \frac{51}{56}")
        final_result.next_to(equals, DOWN, buff=1)
        self.play(Write(final_result))

        # Highlight the closure property
        # closure_text = Text("Closure Property")
        # closure_text.next_to(final_result, DOWN, buff=1)
        # self.play(Write(closure_text))

        self.wait(4)

# To render the scene, run the following command in the terminal:
# manim -pql script_name.py RationalNumbersClosureProperty
        
    def commutativepropexample(self):
        # Title
        title = Text("Commutative Property Example", font_size=40,color=RED)
        title.to_edge(UP)

        # Rational numbers and equation setup
        eq1 = MathTex(r"\frac{5}{2}", r"+", r"\left(-\frac{3}{4}\right)", "=", r"\frac{2 \times 5 + 1 \times (-3)}{4}")
        eq2 = MathTex(r"=", r"\frac{10 - 3}{4}")
        eq3 = MathTex(r"=", r"\frac{7}{4}")
        
        eq4 = MathTex(r"\left(-\frac{3}{4}\right)", r"+", r"\frac{5}{2}", "=", r"\frac{1 \times (-3) + 2 \times 5}{4}")
        eq5 = MathTex(r"=", r"\frac{-3 + 10}{4}")
        eq6 = MathTex(r"=", r"\frac{7}{4}")
        
        # eq7 = MathTex(r"\frac{5}{2}", r"+", r"\left(-\frac{3}{4}\right)", r"=", r"\left(-\frac{3}{4}\right)", r"+", r"\frac{5}{2}")

        # Position equations
        eq1.next_to(title, DOWN, buff=1)
        eq2.next_to(eq1, RIGHT)
        eq3.next_to(eq2, RIGHT)
       
        eq4.next_to(eq1, DOWN, buff=1)
        eq5.next_to(eq4, RIGHT)
        eq6.next_to(eq5, DOWN)
        
        # eq7.next_to(eq6, DOWN, buff=1)

        # Display equations
        self.play(Write(title))
        
        self.play(Write(eq1))
        self.wait(1)
        self.play(Write(eq2))
        self.wait(1)
        self.play(Write(eq3))
        self.wait(1)
        
        self.play(Write(eq4))
        self.wait(1)
        self.play(Write(eq5))
        self.wait(1)
        self.play(Write(eq6))
        self.wait(1)
        
        # self.play(Write(eq7))
        # self.wait(1)

        # Emphasize the final results
        box1 = SurroundingRectangle(eq3, color=YELLOW, buff=0.1)
        box2 = SurroundingRectangle(eq6, color=YELLOW, buff=0.1)
        
        self.play(Create(box1))
        self.wait(1)
        self.play(Create(box2))
        self.wait(1)

        self.play(Uncreate(box1), Uncreate(box2))
        self.wait(1)


    def subtractionexample(self):
        title = Text("Subtraction of Rational numbers ",color=RED)
        title.to_edge(UP)

        subtitle = Text("Consider the Rational Numbers",color=BLUE,font_size=25)
        subtitle.next_to(title, DOWN)
 
        self.play(Write(title))
        self.play(Write(subtitle))

        # Display the two rational numbers
        r1 = MathTex(r"\frac{5}{9}\quad\text{and}")
        r2 = MathTex(r"\frac{3}{4}")
        r1.next_to(subtitle, DOWN, buff=1)
        r2.next_to(r1, RIGHT, buff=1)

        self.play(Write(r1), Write(r2))

        # Show the subtraction process
        subtraction = MathTex(r"\frac{5}{9} - \frac{3}{4}")
        equals = MathTex("=")
        subtraction.next_to(title , DOWN*3,buff=1 )
        equals.next_to(subtraction, RIGHT, buff=1)
        self.play(Write(subtraction), Write(equals))

        # Show the intermediate step 1
        intermediate1 = MathTex(r"\frac{5 \times 4 - 3 \times 9}{36}")
        intermediate1.next_to(equals, RIGHT, buff=1)
        self.play(Write(intermediate1))

        # Show the intermediate step 2
        intermediate2 = MathTex(r"\frac{20 - 27}{36}  = \frac{-7}{36}")
        intermediate2.next_to(intermediate1, DOWN, buff=0.5)
        self.play(Write(intermediate2))

        self.wait(4)

        # # Show the final result
        # result = MathTex(r"= \frac{-7}{36}")
        # result.next_to(intermediate2, DOWN, buff=1)
        # self.play(Write(result))

        # # Final display
        # final_result = MathTex(r"\frac{5}{9} - \frac{3}{4} = \frac{-7}{36}")
        # final_result.next_to(equals, DOWN, buff=1)
        # self.play(Write(final_result))


# To render the scene, run the following command in the terminal:
# manim -pql script_name.py RationalNumbersSubtraction

    def SetDeveloperList(self):
        self.DeveloperList="Sai Krishna Bikkumalla"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade8CH1RationalNumbers.py"
  

if __name__ == "__main__":
    scene =Grade8Ch1RationalNumbers()
    scene.render()
if __name__ == "__main__":
    scene =Grade8Ch1RationalNumbers()
    scene.render()