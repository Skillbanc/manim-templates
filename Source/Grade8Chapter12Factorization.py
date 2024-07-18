from manim import *
from AbstractAnim import AbstractAnim
import cvo

class Grade8Chapter12Factorization(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.factorization_Example()
        self.fadeOutCurrentScene()
        self.factorsofalgebraicexpression()
        self.fadeOutCurrentScene()
        self.Types_of_Factorization()
        self.fadeOutCurrentScene()
        self.PrimeandComplexfactorization()
        self.fadeOutCurrentScene()
        self.MethodofCommonfactors()
        self.fadeOutCurrentScene()
        self.Factorisation_by_grouping_the_terms()
        self.fadeOutCurrentScene()
        self.Factorization_Identies()
        self.fadeOutCurrentScene()
        self.Factorisationusingidenties()
        self.fadeOutCurrentScene()
        self.divisionofalgebraicexpression()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        
    def Introduction(self):

        self.isRandom=False
        p10=cvo.CVO().CreateCVO("Factorization","").setPosition([-4.5,-1.5,0])
        p11=cvo.CVO().CreateCVO("definition","The process of breaking down an expression into a product of simpler factors.").setPosition([0.5,0.5,0]).setangle(-TAU/4)

        p10.cvolist.append(p11)

        p11.setcircleradius(1.25)
        self.construct1(p10,p10)


    def factorization_Example(self):
        # Title
        sub_title1 = Text("Let us Try to write ‘42’ as product of any two numbers",font_size=29).to_edge(UP*2.75+LEFT*1)

        sub_title2 = Text("42  =  1 × 42 ",font_size=27).to_edge(UP* 4.5+LEFT* 7)
        sub_title3 = Text("=  2 × 21",font_size=29).to_edge(UP* 6 +LEFT*8.25)
        sub_title4 = Text("=  3 × 14",font_size=29).to_edge(UP*7.5+LEFT*8.15)
        sub_title5 = Text("=  6 × 7",font_size=29).to_edge(UP*9+LEFT*8.2)
        sub_title6 = Text("Thus 1, 2, 3, 6, 7, 14, 21 and 42 are the factors of 42.",font_size=29).to_edge(UP*10.5)
        sub_title7 = Text("The form of factorisation where all factors are ",font_size=29).to_edge(UP*12)
        sub_title8 = MarkupText("primes is called product of <span foreground='YELLOW'>prime factor form</span>.",font_size=29).to_edge(UP*13.25)




        self.play(Write(sub_title1))
        self.wait(2)
        self.play(Write(sub_title2))
        self.wait(2)
        self.play(Write(sub_title3))
        self.wait(2)
        self.play(Write(sub_title4))
        self.wait(2)
        self.play(Write(sub_title5))
        self.wait(2)
        self.play(Write(sub_title6))
        self.wait(2)
        self.play(Write(sub_title7))
        self.wait(2)
        self.play(Write(sub_title8))
        
        elements_to_fade = VGroup(sub_title1, sub_title2, sub_title3, sub_title4, sub_title5, sub_title6, sub_title7, sub_title8)
        self.play(FadeOut(elements_to_fade))
        self.wait(1)


    def factorsofalgebraicexpression(self):
        self.setNumberOfCirclePositions(5)
        #self.angleChoice = [0,0,0]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("algebraic expression","7yz").setPosition([-4,-2.5,0])
        p11=cvo.CVO().CreateCVO("Factors","").setPosition([4.5,-1.75,0])
        p11.extendOname(["7","yz"])
        p12=cvo.CVO().CreateCVO("Factors","").setPosition([4,1,0])
        p12.extendOname(["7y","z"])
        p13=cvo.CVO().CreateCVO("Factors","7z and y are factors").setPosition([1.25,2,0])
        p13.extendOname(["7z","y"])
        p14=cvo.CVO().CreateCVO("Factors","7,y and z are factors").setPosition([-2.25,1.75,0])
        p14.extendOname(["7","y","z"])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.setcircleradius(1.1)
        p11.setcircleradius(1.25)
        p12.setcircleradius(1.25)
        p13.setcircleradius(1.25)
        p14.setcircleradius(1.25)
        self.construct1(p10,p10)
        #self.play()




    def Types_of_Factorization(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Factorization","").setPosition([-2,0,0])
        p11=cvo.CVO().CreateCVO("Prime Factorization", "").setPosition([2.5,2,0])
        p12=cvo.CVO().CreateCVO("Complex Factorization", "").setPosition([2.5,-2,0])
        
        
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)



    def PrimeandComplexfactorization(self):  

        heading = Text("Prime Factorization :",color=DARK_BROWN,font_size=37).to_edge(UP*1.25+LEFT * 1)
        sub_title1 = Text("The process of expressing a composite number as a product of its prime numbers.",font_size=26).to_edge(UP*3+LEFT*1.15)
        sub_title2 = Text("example: find the prime factorization of 60. ",font_size=29).to_edge(UP*4.75+LEFT*2.5)
        sub_title2[0:8].set_color(BLUE)
        sub_title3 = Text("the prime factorization of 60 is: 60 = 2×2×3×5  or  2²×3×5",font_size=29).to_edge(UP*6.6+LEFT*5.65)
        heading2 = Text("Complex Factorization: ",color=PINK,font_size=37).to_edge(UP*9+LEFT * 1)
        sub_title5 = Text("Breaking down a polynomial into simpler factors those with complex numbers.",font_size=26).to_edge(UP*10.5+LEFT*1.15)
        sub_title6 = Text("example: find the complex factorization of x²+1",font_size=29).to_edge(UP*12+LEFT*2.5)
        sub_title6[0:8].set_color(BLUE)
        sub_title7 = Text("the complex factorization of x²+1 = (x+i) (x-i) ",font_size=29).to_edge(UP*13.5+LEFT*5.65)
        
        self.play(Write(heading))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)
        self.play(Write(sub_title3))
        self.wait(1)
        self.play(Write(heading2))
        self.wait(1)
        self.play(Write(sub_title5))
        self.wait(1)
        self.play(Write(sub_title6))
        self.wait(1)
        self.play(Write(sub_title7))
        self.fadeOutCurrentScene()



        # Subtitle
        sub_title1 = Text("Example: (4x² - 1) ÷ (2x - 1)", font_size=27).to_edge(UP*1.5 + LEFT*1)
        sub_title1[0:8].set_color(PURPLE)
        self.play(Write(sub_title1))
        self.wait(2)

        # Step 1: Write the initial expression
        initial_expression = MathTex(r"\frac{4x^2 - 1}{2x - 1}").to_edge(UP*3)
        self.play(Write(initial_expression))
        self.wait(1)

        # Step 2: Show the expression as a difference of squares
        step_1 = MathTex(r"= \frac{(2x)^2 - 1^2}{2x - 1}").to_edge(UP*5.5)
        self.play(Transform(initial_expression.copy(), step_1))
        self.wait(1)

        # Step 3: Introduce the difference of squares formula
        diff_squares = Text(r"a² - b² = (a+b) (a-b)", font_size=24).next_to(step_1, DOWN*2.5)
        self.play(Write(diff_squares))
        self.wait(1)

        # Step 4: Factor the numerator using the difference of squares formula
        step_2 = MathTex(r"= \frac{(2x + 1)(2x - 1)}{2x - 1}").to_edge(UP*10.7)
        self.play(Transform(step_1.copy(), step_2))
        self.wait(1)

        # Step 5: Fade out the common term (2x - 1) in the numerator and denominator
        numerator_term = step_2[0][11:19]  # (2x - 1) in the numerator
        denominator_term = step_2[0][20:28]  # (2x - 1) in the denominator

        self.play(FadeOut(numerator_term), FadeOut(denominator_term))
        self.wait(1)

        # Step 6: Write the simplified final step
        final_step = MathTex(r"= 2x + 1").to_edge(UP*13.5)
        self.play(Transform(step_2.copy(), final_step))
        self.wait(1)

        # Optional wait at the end
        self.wait(2)

        # Add the final expressions to the scene
        self.add(final_step)




        

        # # Subtitle
        # sub_title1 = Text("Example:         (4x²-1) ÷ (2x-1)", font_size=27).to_edge(UP*1.5 + LEFT*1)
        # sub_title1[0:8].set_color(PURPLE)
        # self.play(Write(sub_title1))
        # self.wait(2)

        # # Step 1: Write the initial expression
        # initial_expression = MathTex(r"\frac{4x^2 - 1}{2x - 1}").to_edge(UP*3)
        # step_1 = MathTex(r"= \frac{(2x)^2 - 1^2}{2x - 1}").to_edge(UP*5)
        # step_2 = MathTex(r"= \frac{(2x + 1)(2x - 1)}{2x - 1}").to_edge(UP*7)
        # final_step = MathTex(r"= 2x + 1").to_edge(UP*9)  # Simplified final step

        # # Arrange them
        # step_1.next_to(initial_expression, DOWN*0.75, buff=1)
        # step_2.next_to(step_1, DOWN*0.75, buff=1)
        # final_step.next_to(step_3, DOWN*0.75, buff=1)

        # # Animation sequence
        # self.play(Write(initial_expression))
        # self.wait(1)
        # self.play(Transform(initial_expression.copy(), step_1))
        # self.wait(1)
        # self.play(Transform(step_1.copy(), step_2))
        # self.wait(1)
        # self.play(Transform(step_2.copy(), final_step))
        # self.wait(1)

        # self.wait(2)  # Optional wait at the end

        # # Add the final expressions to the scene
        # self.add(final_step)


    def MethodofCommonfactors(self):
        # Title
        sub_title1 = Text("Method of common factors :",font_size=29,color=BLUE).to_edge(UP*1.75)
        sub_title2 = Text("Example :",font_size=29,color=PINK).to_edge(UP*4.25+LEFT*1)
        sub_title3 = Text("25 a²b +35 ab² = (5× 5 × a × a × b) +(5× 7 × a × b× b)",font_size=27).next_to(sub_title2,RIGHT*1)
        sub_title4 = Text("=  5 × a × b ×[ (5 × a) + (7 × b)]",font_size=29).to_edge(UP* 6.5+LEFT*10.5)
        sub_title5 = Text("= 5ab (5a + 7b)",font_size=29).to_edge(UP*8.75+LEFT*10.5)
        sub_title6 = Text("∴ 25 a²b +35ab² = 5ab (5a + 7b)",font_size=29).to_edge(UP*11+LEFT*4.5)



        self.play(Write(sub_title1))
        self.wait(2)
        self.play(Write(sub_title2))
        self.wait(2)
        self.play(Write(sub_title3))
        self.wait(2)
        self.play(Write(sub_title4))
        self.wait(2)
        self.play(Write(sub_title5))
        self.wait(2)
        self.play(Write(sub_title6))
        self.wait(2)

        elements_to_fade = VGroup(sub_title1, sub_title2, sub_title3, sub_title4, sub_title5, sub_title6)
        self.play(FadeOut(elements_to_fade))
        self.wait(1)

        

    def Factorisation_by_grouping_the_terms(self):

        # Subtitles
        sub_title1 = Text("Example:", font_size=29, color=PINK).to_edge(UP + LEFT)
        sub_title2 = Text("Factorise 6ab - b² - 2bc + 12ac", font_size=27).next_to(sub_title1, RIGHT)
        sub_title3 = Text("Step 1: Check whether there are any common factors for all terms. Obviously none.", font_size=26).to_edge(UP*3 + LEFT)
        sub_title4 = Text("Step 2: On regrouping the first two terms we have", font_size=26).to_edge(UP*4.5 + LEFT)
        sub_title5 = Text("6ab - b² = b(6a - b) ....................I", font_size=26).to_edge(UP*6 )
        sub_title6 = Text("We need to change the order of the last two terms in the expression", font_size=26).to_edge(UP*7.5 + LEFT*4)
        sub_title7 = Text("12ac - 2bc = 2c(6a - b) ...................II", font_size=26).to_edge(UP*9)
        sub_title8 = Text("Step 3: Combining I and II together", font_size=26).to_edge(UP*10.5 + LEFT)
        sub_title9 = Text("6ab - b² - 2bc + 12ac = b(6a - b) + 2c(6a - b)", font_size=26).to_edge(UP*12 )
        sub_title10 = Text("(6a - b)(b + 2c)", font_size=26).to_edge(UP*13.5)
        sub_title11 = Text("Hence the factors of 6ab - b² - 2bc + 12ac are (6a - b) and (b + 2c)", font_size=26).to_edge(UP*14.8)

        # Set color for step numbers
        sub_title3[0:6].set_color(GREEN)  # Color "Step 1:" in green
        sub_title4[0:6].set_color(GREEN)  # Color "Step 2:" in green
        sub_title8[0:6].set_color(GREEN)  # Color "Step 3:" in green

        # Animation sequence

        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)
        self.play(Write(sub_title3))
        self.wait(1)
        self.play(Write(sub_title4))
        self.wait(1)
        self.play(Write(sub_title5))
        self.wait(1)
        self.play(Write(sub_title6))
        self.wait(1)
        self.play(Write(sub_title7))
        self.wait(1)
        self.play(Write(sub_title8))
        self.wait(1)
        self.play(Write(sub_title9))
        self.wait(1)
        self.play(Write(sub_title10))
        self.wait(1)
        self.play(Write(sub_title11))
        self.wait(2)

        # Fade out all elements
        elements_to_fade = VGroup(sub_title1, sub_title2, sub_title3, sub_title4, sub_title5, sub_title6, sub_title7, sub_title8, sub_title9, sub_title10, sub_title11)
        self.play(FadeOut(elements_to_fade))
        self.wait(1)


    def Factorization_Identies(self):

        union = Text("Factorisation using identities:",color=DARK_BROWN).to_edge(UP*1.25)
        sub_title1 = Text("(a+b)² = a² + b² + 2ab",font_size=30).to_edge(UP*4.5)
        sub_title2 = Text("(a-b)² = a² + b² - 2ab",font_size=30).to_edge(UP*7.5)
        sub_title3 = Text("(a+b) (a-b) = a² - b²",font_size=30).to_edge(UP*10)
        sub_title4 = Text("We can use these identities for factorisation, if the given",font_size=30).to_edge(UP*12.75)
        sub_title5 = Text("given is in the form of RHS (RightHand Side) of the particular identity.",font_size=30).to_edge(UP*14.5+LEFT*1.25)

        # Create a surrounding rectangle for the subtitle and formula
        rect = SurroundingRectangle(VGroup(sub_title1, sub_title2,sub_title3), color=BLUE, buff=0.3)
        

        self.play(Write(union))
        self.wait(2)
        self.play(Write(sub_title1))
        self.wait(2)
        self.play(Write(sub_title2))
        self.wait(2)
        self.play(Write(sub_title3))
        self.wait(2)  
        self.play(Create(rect))
        self.wait(1)
        self.play(Write(sub_title4))
        self.wait(2)
        self.play(Write(sub_title5))
        self.wait(2)

        elements_to_fade = VGroup(sub_title1, sub_title2, sub_title3, rect, sub_title4, sub_title5)
        self.play(FadeOut(elements_to_fade))
        self.wait(1)

    def Factorisationusingidenties(self):
        # Title
        sub_title1 = Text("Example :",font_size=29,color=PINK).to_edge(UP*1+LEFT*1)
        sub_title2 = Text("Factorise x² + 10x + 25",font_size=27).next_to(sub_title1,RIGHT*1)
        sub_title3 = Text("the first and third terms are perfect squares",font_size=29).to_edge(UP* 3+LEFT*4)
        sub_title4 = Text("That is x² and 25(5²) ",font_size=29).to_edge(UP*4.5+LEFT*4)
        sub_title5 = Text("x² + 10x + 25 = (x)²+ 2(x)(5) + (5)²",font_size=29).to_edge(UP*6+LEFT*4)
        sub_title6 = Text("We can compare it with a²+ 2ab + b²",font_size=29).to_edge(UP*7.5+LEFT*4)
        sub_title7 = Text("i.e. (a + b)². Here a = x and b = 5",font_size=29).to_edge(UP*9+LEFT*4)
        sub_title8 = Text("We have x² + 10x + 25 = (x+5)² = (x+5) (x+5)",font_size=29).to_edge(UP*10.5+LEFT*4)



        self.play(Write(sub_title1))
        self.wait(2)
        self.play(Write(sub_title2))
        self.wait(2)
        self.play(Write(sub_title3))
        self.wait(2)
        self.play(Write(sub_title4))
        self.wait(2)
        self.play(Write(sub_title5))
        self.wait(2)
        self.play(Write(sub_title6))
        self.wait(2)
        self.play(Write(sub_title7))
        self.wait(2)
        self.play(Write(sub_title8))
        self.wait(2)

        elements_to_fade = VGroup(sub_title1, sub_title2, sub_title3, sub_title4, sub_title5, sub_title6,sub_title7,sub_title8)
        self.play(FadeOut(elements_to_fade))
        self.wait(1)

    def divisionofalgebraicexpression(self):

        sub_title2 = Text("Division of Algebraic Expression",font_size=30,color=YELLOW).to_edge(UP*1+LEFT*1)
        sub_title3 = Text("Example 1. Let us consider 3x × 5³ = 15x⁴ ",font_size=29).to_edge(UP* 3+LEFT*4)
        sub_title4 = Text("Then 15x⁴ ÷ 5x³ = 3x and 15x⁴ ÷ 3x = 5x³",font_size=29).to_edge(UP*4.5+LEFT*4)
        sub_title5 = Text("Example 2.Let us consider 6a(a+5) = 6a² + 30a",font_size=29).to_edge(UP*6.5+LEFT*4)
        sub_title6 = Text("(6a² + 30a) ÷ 6a = a + 5",font_size=29).to_edge(UP*7.5+LEFT*4)
        sub_title7 = Text("(6a² + 30a) + (a+5) = 6a",font_size=29).to_edge(UP*9+LEFT*4)
       
        self.play(Write(sub_title2))
        self.wait(2)
        self.play(Write(sub_title3))
        self.wait(2)
        self.play(Write(sub_title4))
        self.wait(2)
        self.play(Write(sub_title5))
        self.wait(2)
        self.play(Write(sub_title6))
        self.wait(2)
        self.play(Write(sub_title7))
        self.wait(2)

        elements_to_fade = VGroup(sub_title2, sub_title3, sub_title4, sub_title5, sub_title6,sub_title7)
        self.play(FadeOut(elements_to_fade))
        self.wait(1)


    def SetDeveloperList(self):
        self.DeveloperList="Bommi Yaswanth"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade8Chapter12Factoeization.py"


if __name__ == "__main__":
    scene = Grade8Chapter12Factorization()
    scene.render()