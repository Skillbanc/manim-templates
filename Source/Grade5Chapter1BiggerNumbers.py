from manim import *
from AbstractAnim import AbstractAnim
import cvo

class BigNumbers(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.placeValue()
        self.fadeOutCurrentScene()
        self.expansion()
        self.fadeOutCurrentScene()
        self.addingBiggerNumbers()
        self.fadeOutCurrentScene()
        self.subtractingBiggerNumbers()
        self.fadeOutCurrentScene()
        self.comparingBiggerNumbers()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

    def placeValue(self):
        self.positionChoice = [[-4,0,0],[2,0,0]]
        self.angleChoice = [(TAU/5)]
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Place Value", "")
        p11 = cvo.CVO().CreateCVO("Understanding Place Value", "")
        p11.extendOname(["Units", "Tens", "Hundreds", "Thousands", "Ten Thousands", "Lakhs"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10, p10)
        self.fadeOutCurrentScene()

        title = Text("Place Value", font_size=30).to_edge(UP)
        explanation = Text("Understanding the value of digits based on their positions in a number.", font_size=24).next_to(title, DOWN, buff=0.5)
        example = MathTex("2345").scale(2).next_to(explanation, DOWN, buff=1)
        self.play(Write(title), Write(explanation), Write(example))
        self.wait(1)
        
        digits_texts = [
            "\\text{$ 2 \\Rightarrow \\text{Thousands place} $}",
            "\\text{$ 3 \\Rightarrow \\text{Hundreds place} $}",
            "\\text{$ 4 \\Rightarrow \\text{Tens place} $}",
            "\\text{$ 5 \\Rightarrow \\text{Units place} $}",
        ]
        
        digits = VGroup(*[MathTex(text, font_size=30) for text in digits_texts]).arrange(DOWN, aligned_edge=LEFT).next_to(example, DOWN, buff=1)

        self.play(Write(digits))
        self.wait(2)
        

    def expansion(self):
        self.positionChoice=[(-4.5,1.5,0),(3.5,1.5,0)]
        self.angleChoice=[(TAU/4)]
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Number Expansion", "")
        p11 = cvo.CVO().CreateCVO("Expanded Form", "")
        p11.extendOname(["Finding place values", "Adding all the digits"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10, p10)
        example = MathTex(
             "7890 &= \\text{Seven thousand eight hundred and ninety} \\\\",
            "&= 7 \\text{ thousand} + 8 \\text{ hundred} + 9 \\text{ ten} + 0 \\text{ ones} \\\\",
            "&= 7000 + 800 + 90 + 0\\\\",
            "&= 7890",
            font_size=30
        ).shift([0, -2, 0])
        self.play(Write(example))

        self.fadeOutCurrentScene()

        title = Text("Expansion", font_size=30).to_edge(UP)
        explanation = Text("Breaking down a number into its place value components.", font_size=24).next_to(title, DOWN, buff=0.5)
    
        example1 = MathTex(
            "4567 &= \\text{Four thousand five hundred and sixty-seven} \\\\",
            "&= 4 \\text{ thousand} + 5 \\text{ hundred} + 6 \\text{ ten} + 7 \\text{ ones} \\\\",
            "&= 4000 + 500 + 60 + 7",
            font_size=35
        ).next_to(explanation, DOWN, buff=1)
        example2 = MathTex(
            "1981 &= \\text{One thousand Nine hundred and eighty one} \\\\",
            "&= 1 \\text{ thousand} + 9 \\text{ hundred} + 8 \\text{ ten} + 1 \\text{ ones} \\\\",
            "&= 1000 + 900 + 80 + 1",
            font_size=35
        ).next_to(example1, DOWN, buff=1)

        self.play(Write(title))
        self.wait(1)
        self.play(Write(explanation))
        self.wait(1)
        self.play(Write(example1))
        self.play(Write(example2))
        self.wait(3)

    def addingBiggerNumbers(self):
        self.positionChoice=[[-4,0,0],[-1,2,0],[-1,-2,0],[2,0,0],[5,0,0]]
        self.isRandom = False
        self.angleChoice=[TAU/3,TAU/2,TAU/2,TAU/2,TAU/2]
        p10=cvo.CVO().CreateCVO("Bigger Numbers","")
        p11=cvo.CVO().CreateCVO("Number 1","12345")
        p12=cvo.CVO().CreateCVO("Number 2","67890")
        p13=cvo.CVO().CreateCVO("Addition","12345+67890")
        p14 = cvo.CVO().CreateCVO("Sum", "80235")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.construct1(p13, p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)))
        self.play(Create(CurvedArrow(p12.pos,p13.pos)))
        self.construct1(p14,p14)
        self.play(Create(CurvedArrow(p13.pos,p14.pos)))
        self.fadeOutCurrentScene()
        
        # Title and problem setup
        title = Text("Adding Bigger Numbers", font_size=30).to_edge(UP)
        problem_text = MathTex("Example: 3451 + 1987 =\\ ?", font_size=35).next_to(title, DOWN, buff=0.5)

        # Display the title and the problem
        self.play(Write(title))
        self.play(Write(problem_text))
        self.wait(1)

        # Display the numbers and the subtraction line
        three_four_five_one = MathTex("3", "4", "5", "1", font_size=48)
        one_nine_eight_seven = MathTex("1", "9", "8" , "7", font_size=48)
        three_four_five_one.arrange(RIGHT, buff=0.75)
        one_nine_eight_seven.arrange(RIGHT, buff=0.75)
        three_four_five_one.next_to(problem_text, DOWN, buff=1)
        one_nine_eight_seven.next_to(three_four_five_one, DOWN, buff=0.5)
        
        # Minus sign and line
        plus_sign = Tex("+").scale(1).next_to(one_nine_eight_seven, LEFT, buff=0.5)
        line = Line(one_nine_eight_seven.get_left(), one_nine_eight_seven.get_right()).next_to(one_nine_eight_seven, DOWN)
        equals_sign = Tex("=").scale(0.7).next_to(plus_sign, DOWN * 3, buff=0.2)

        self.play(Write(three_four_five_one))
        self.play(Write(one_nine_eight_seven))
        self.play(Write(plus_sign))
        self.play(Write(line))
        self.wait(1)
        self.play(Write(equals_sign))


        result_eight = MathTex("8").next_to(one_nine_eight_seven[3], DOWN, buff=0.5)  

        self.play(Write(result_eight))
        self.wait(1)


        carry_one = MathTex("1").next_to(three_four_five_one[1], UP, buff=0.2)
        result_three = MathTex("3").next_to(one_nine_eight_seven[2], DOWN, buff=0.5) 
        self.play(Write(carry_one))
        self.play(Write(result_three))

        self.wait(1)

        carry_one = MathTex("1").next_to(three_four_five_one[0], UP, buff=0.2)
        result_four = MathTex("4").next_to(one_nine_eight_seven[1], DOWN, buff=0.5) 
        self.play(Write(carry_one))
        self.play(Write(result_four))

        result_five = MathTex("5").next_to(one_nine_eight_seven[0], DOWN, buff=0.5)  
        self.play(Write(result_five))

        problem_ans = MathTex("Therefore\\ 3451 + 1987 = 5438", font_size=35).next_to(result_five, DOWN, buff=0.5)
        self.play(Write(problem_ans))

        self.wait(3)

    def subtractingBiggerNumbers(self):
        self.positionChoice=[[-4,0,0],[-1,2,0],[-1,-2,0],[2,0,0],[5,0,0]]
        self.isRandom = False
        self.angleChoice=[TAU/3,TAU/2,TAU/2,TAU/2,TAU/2]
        p10=cvo.CVO().CreateCVO("Bigger Numbers","")
        p11=cvo.CVO().CreateCVO("Number 1","67890")
        p12=cvo.CVO().CreateCVO("Number 2","12345")
        p13=cvo.CVO().CreateCVO("Subtraction","67890-12345")
        p14 = cvo.CVO().CreateCVO("Difference", "55545")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.construct1(p13, p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)))
        self.play(Create(CurvedArrow(p12.pos,p13.pos)))
        self.construct1(p14,p14)
        self.play(Create(CurvedArrow(p13.pos,p14.pos)))
        self.fadeOutCurrentScene()

        title = Text("Subtracting Bigger Numbers", font_size=30).to_edge(UP)
        problem_text = MathTex("Example: 3451 - 1987 = \\ ?", font_size=35).next_to(title, DOWN, buff=0.5)

        # Display the title and the problem
        self.play(Write(title))
        self.play(Write(problem_text))
        self.wait(1)

        # Display the numbers and the subtraction line
        three_four_five_one = MathTex("3", "4", "5", "1", font_size=48)
        one_nine_eight_seven = MathTex("1", "9", "8" , "7", font_size=48)
        three_four_five_one.arrange(RIGHT, buff=0.75)
        one_nine_eight_seven.arrange(RIGHT, buff=0.75)
        three_four_five_one.next_to(problem_text, DOWN, buff=1)
        one_nine_eight_seven.next_to(three_four_five_one, DOWN, buff=0.5)
        
        # Minus sign and line
        minus_sign = Tex("-").scale(1).next_to(one_nine_eight_seven, LEFT, buff=0.5)
        line = Line(one_nine_eight_seven.get_left(), one_nine_eight_seven.get_right()).next_to(one_nine_eight_seven, DOWN)
        equals_sign = Tex("=").scale(0.7).next_to(minus_sign, DOWN * 3, buff=0.2)

        self.play(Write(three_four_five_one))
        self.play(Write(one_nine_eight_seven))
        self.play(Write(minus_sign))
        self.play(Write(line))
        self.wait(1)
        self.play(Write(equals_sign))

        # Step-by-step borrowing
        borrowed_four = MathTex("4").next_to(three_four_five_one[2], UP, buff=0.2)
        eleven_in = MathTex("11").next_to(three_four_five_one[3], UP, buff=0.2)
        strike_five = Line(three_four_five_one[2].get_top(), three_four_five_one[2].get_bottom(), stroke_width=5, color=RED)
        result_four = MathTex("4").next_to(one_nine_eight_seven[3], DOWN, buff=0.5)  

        self.play(Create(strike_five))
        self.play(Write(borrowed_four))
        self.play(Write(eleven_in))
        self.play(Write(result_four))
        self.wait(1)


        borrowed_three = MathTex("3").next_to(three_four_five_one[1], UP, buff=0.2)
        fourteen = MathTex("14").next_to(three_four_five_one[2], UP, buff=0.2)
        strike_five = Line(three_four_five_one[1].get_top(), three_four_five_one[1].get_bottom(), stroke_width=5, color=RED)
        result_six = MathTex("6").next_to(one_nine_eight_seven[2], DOWN, buff=0.5) 

        self.play(Create(strike_five))
        self.play(Write(borrowed_three))
        self.play(FadeOut(borrowed_four))  # Fade out result_four
        self.play(Write(fourteen))
        self.play(Write(result_six))
        self.wait(1)

        borrowed_two = MathTex("2").next_to(three_four_five_one[0], UP, buff=0.2)
        Thirteen = MathTex("13").next_to(three_four_five_one[1], UP, buff=0.2)
        strike_five = Line(three_four_five_one[0].get_top(), three_four_five_one[0].get_bottom(), stroke_width=5, color=RED)
        result_four = MathTex("4").next_to(one_nine_eight_seven[1], DOWN, buff=0.5)  

        self.play(Create(strike_five))
        self.play(Write(borrowed_two))
        self.play(FadeOut(borrowed_three))  # Fade out result_four
        self.play(Write(Thirteen))
        self.play(Write(result_four))
        self.wait(1)

        result_one = MathTex("1").next_to(one_nine_eight_seven[0], DOWN, buff=0.5)  
        self.play(Write(result_one))

        problem_ans = MathTex("Therefore\\ 3451 - 1987 = 1464", font_size=35).next_to(result_one, DOWN, buff=0.5)
        self.play(Write(problem_ans))

        self.wait(3) 

    def comparingBiggerNumbers(self):
        self.positionChoice = [[-4, 0, 0], [0, 2, 0], [0, -2, 0]]
        self.angleChoice=[(TAU/3),(TAU/3)]
        self.isRandom = False
       

        p10 = cvo.CVO().CreateCVO("Compare Numbers", "")
        p11 = cvo.CVO().CreateCVO("Understanding Place Value", "")
        p12 = cvo.CVO().CreateCVO("Comparing Two Numbers", "")
        p12.extendOname(["Greater Than", "Less Than", "Equal To"])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10, p10)
        self.fadeOutCurrentScene()

        title = Text("Comparing Two Numbers", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Numbers to compare
        number1 = "4567"
        number2 = "4568"

        # Create the numbers
        num1_tex = MathTex(*number1, font_size=72)
        num2_tex = MathTex(*number2, font_size=72)

        # Arrange the numbers
        num1_tex.to_edge(LEFT, buff=2)
        num2_tex.to_edge(RIGHT, buff=2)

        # Create comparison symbols
        less_than = MathTex("<", font_size=72).move_to(ORIGIN)
        greater_than = MathTex(">", font_size=72).move_to(ORIGIN)
        equal_sign = MathTex("=", font_size=72).move_to(ORIGIN)

        # Highlight colors
        highlight_color = YELLOW
        default_color = WHITE

        # Animate the numbers
        self.play(Write(num1_tex), Write(num2_tex))
        self.wait(1)

        # Function to highlight digits and compare
        def compare_digits(index, color1, color2):
            self.play(
                num1_tex[index].animate.set_color(color1),
                num2_tex[index].animate.set_color(color2),
                run_time=0.5
            )
            self.wait(0.5)

        # Compare digits step by step
        comparison_made = False
        for i in range(4):
            if number1[i] < number2[i]:
                compare_digits(i, highlight_color, highlight_color)
                self.play(Write(less_than))
                comparison_made = True
                break
            elif number1[i] > number2[i]:
                compare_digits(i, highlight_color, highlight_color)
                self.play(Write(greater_than))
                comparison_made = True
                break
            else:
                compare_digits(i, highlight_color, highlight_color)
                self.play(Write(equal_sign))
                self.wait(1)
                move_next = Text(f"{number1[i]} = {number2[i]} so move to the next digit", font_size=24).next_to(equal_sign, DOWN, buff=1)
                self.play(Write(move_next))
                self.wait(1)
                self.play(FadeOut(equal_sign), FadeOut(move_next))
                compare_digits(i, default_color, default_color)

        # Final statement
        if comparison_made:
            final_statement = Text(f"{number1} is less than {number2}" if number1 < number2 else f"{number1} is greater than {number2}", font_size=30).next_to(less_than if number1 < number2 else greater_than, DOWN, buff=1)
        else:
            final_statement = Text(f"{number1} is equal to {number2}", font_size=30).next_to(equal_sign, DOWN, buff=1)

        self.play(Write(final_statement))
        self.wait(3)


    def SetDeveloperList(self):  
        self.DeveloperList="Shanmukha Priya"
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade5Chapter1BiggerNumbers.py"

if __name__ == "__main__":
     scene = BigNumbers()
     scene.render()