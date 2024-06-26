from manim import *
from AbstractAnim import AbstractAnim
import cvo

class Subtraction(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.sub()
        self.fadeOutCurrentScene()
        self.SubAnim()
        self.fadeOutCurrentScene()
        self.Sub_3Anim()
        self.fadeOutCurrentScene()
        self.Borrow()
        self.fadeOutCurrentScene()
        self.BorrowAnim()
        self.fadeOutCurrentScene()
        self.Borrow_3Anim()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
  

    def sub(self):
        self.positionChoice=[[-4,0,0],[0,-2,0],[-2,0,0],[1,0,0],[3,0,0]]
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Subtraction", "")
        p11 = cvo.CVO().CreateCVO("Symbol", "minus (-)")
        p12 = cvo.CVO().CreateCVO("Numbers", "90,45")
        p13 = cvo.CVO().CreateCVO("Representation", "90 - 45")
        p14 = cvo.CVO().CreateCVO("Result", "45")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p12.cvolist.append(p13)
        p13.cvolist.append(p14)
        self.construct1(p10, p10)
        # self.construct1(p12, p12)
        self.fadeOutCurrentScene()

    def SubAnim(self):
        # Create title
        title = Text("Subtraction", font_size=40).to_edge(UP)
        
        # Example problem and answer
        example = Text("Example: 39 - 27 = ?", font_size=30).next_to(title, DOWN * 2, buff=0.5)

        self.play(Write(title))
        self.wait(1)
        self.play(Write(example))
        self.wait(1)

        # Numbers for the subtraction
        number1 = MathTex("3", "9", font_size=48)
        number2 = MathTex("2", "7", font_size=48)
        number1.arrange(RIGHT, buff=0.75)
        number2.arrange(RIGHT, buff=0.75)
        number1.next_to(example, DOWN, buff=1)
        number2.next_to(number1, DOWN, buff=0.5)

        # Borrowing annotations
        ten_in_box = MathTex("10", font_size=24, color=YELLOW).next_to(number1[0], UP * 1.5)
        one_in_box = MathTex("1", font_size=24, color=GREEN).next_to(number1[1], UP * 1.5)
        minus_sign = Tex("-").scale(1).next_to(number2, LEFT, buff=0.5)
        line = Line(number2.get_left(), number2.get_right()).next_to(number2, DOWN)
        equals_sign = Tex("=").scale(0.7).next_to(minus_sign,DOWN*3, buff=0.2)

        # Create the result digits manually to place them properly
        result_digit1 = MathTex("1", font_size=48)
        result_digit2 = MathTex("2", font_size=48)
        
        # Place the digits manually starting from the right side
        result_digit2.move_to(number1[1].get_center() + DOWN * 1.5)
        result_digit1.next_to(result_digit2, LEFT, buff=0.75)
        ans = Text("39 - 27 = 12", font_size=30).next_to(result_digit1,DOWN*2)

        # Display the numbers
        self.play(Write(number1))
        self.play(Write(number2))
        self.play(Write(one_in_box), Write(ten_in_box))
        self.wait(1)
        self.play(Write(minus_sign))
        self.play(Write(line))
        self.wait(1)
        self.play(Write(equals_sign))
        
        # Animate result digits from right to left
        self.play(Write(result_digit2))
        self.play(Write(result_digit1))
        
        self.wait(2)
        self.play(Write(ans))
        self.wait(2)

    def Sub_3Anim(self):
        title = Text("Three-Digit Subtraction", font_size=40).to_edge(UP)
        self.play(Write(title))
        
        # Subtraction example and answer
        example = Text("Example: 305 - 103 = ?", font_size=30).next_to(title, DOWN * 1, buff=0.5)
        self.play(Write(example))
        self.wait(1)
        # Breaking down the numbers for visualization with spacing
        number1 = MathTex("3", "0", "5", font_size=48)
        number2 = MathTex("1", "0", "3", font_size=48)
        result_digits = MathTex("2", "0", "2", font_size=48)
        
        number1.arrange(RIGHT, buff=0.75)
        number2.arrange(RIGHT, buff=0.75)
        result_digits.arrange(RIGHT, buff=0.75)
        
        number1.next_to(example, DOWN, buff=1)
        number2.next_to(number1, DOWN, buff=0.5)
        
        # Borrowing annotations
        hundred_in_box = MathTex("100", font_size=24, color=BLUE).next_to(number1[0], UP * 1.5)
        ten_in_box = MathTex("10", font_size=24, color=YELLOW).next_to(number1[1], UP * 1.5)
        one_in_box = MathTex("1", font_size=24, color=GREEN).next_to(number1[2], UP * 1.5)
        
        minus_sign = Tex("-").scale(1).next_to(number2, LEFT, buff=0.5)
        line = Line(number2.get_left(), number2.get_right()).next_to(number2, DOWN)
        
        # Positioning the result digits below the corresponding digits
        result_2_right = MathTex("2", font_size=48).next_to(number2[2], DOWN, buff=1)
        result_0_middle = MathTex("0", font_size=48).next_to(number2[1], DOWN, buff=1)
        result_2_left = MathTex("2", font_size=48).next_to(number2[0], DOWN, buff=1)
        
        equals_sign = Tex("=").scale(0.7).next_to(minus_sign,DOWN*6, buff=0.2)

        # Answer text
        ans = Text("305 - 103 = 202", font_size=30).next_to(result_2_left, DOWN * 2)

        # Centering all elements
        all_elements = VGroup(number1, number2, minus_sign, line, equals_sign, result_2_right, result_0_middle, result_2_left, hundred_in_box, ten_in_box, one_in_box)
        all_elements.move_to(ORIGIN)

        # Display the numbers
        self.play(Write(number1))
        self.play(Write(number2))
        self.play(Write(hundred_in_box), Write(ten_in_box), Write(one_in_box))
        self.wait(1)
        self.play(Write(minus_sign))
        self.play(Write(line))  # Adding the line after number2  
        self.wait(1)
        self.play(Write(equals_sign))
        
        # Display the result digits from right to left
        self.play(Write(result_2_right))
        self.wait(1)
        self.play(Write(result_0_middle))
        self.wait(1)
        self.play(Write(result_2_left))
        self.wait(2)
        
        # Transform the example to the final answer
        self.play(Write(ans))
        self.wait(2)


    def Borrow(self):
        self.positionChoice=[[-4,-2,0],[0,-2,0],[-3,2,0],[1,2,0],[3,0,0]]
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Subtraction", "Borrowing")
        p11 = cvo.CVO().CreateCVO("Borrowing Condition", "Samller digit - Bigger digit")
        p12 = cvo.CVO().CreateCVO("Numbers", "65,29")
        p13 = cvo.CVO().CreateCVO("Representation", "65 - 29")
        p14 = cvo.CVO().CreateCVO("Result", "36")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p12.cvolist.append(p13)
        p13.cvolist.append(p14)
        self.construct1(p10, p10)
        # self.construct1(p13, p13)
        self.fadeOutCurrentScene()

    def BorrowAnim(self):
         # Create title
        title = Text("Borrowing in Subtraction", font_size=48).to_edge(UP)
        
        # Subtraction problem
        problem_text = MathTex("Example: 53 - 27 = ?", font_size=48)
        problem_text.next_to(title, DOWN, buff=0.5)

        # Display the title and the problem
        self.play(Write(title))
        self.play(Write(problem_text))
        self.wait(1)

        # Breaking down the numbers for visualization
        fifty_three = MathTex("5", "3", font_size=54)
        twenty_seven = MathTex("2", "7", font_size=54)
        fifty_three.arrange(RIGHT, buff=0.75)
        twenty_seven.arrange(RIGHT, buff=0.75)
        fifty_three.next_to(problem_text, DOWN, buff=1.5)
        twenty_seven.next_to(fifty_three, DOWN, buff=0.5)
        
        # Borrowing annotations
        ten_in_box = MathTex("10", font_size=24, color=YELLOW).next_to(fifty_three[0], UP * 1.5)
        one_in_box = MathTex("1", font_size=24, color=GREEN).next_to(fifty_three[1], UP * 1.5)
        minus_sign = Tex("-").scale(1).next_to(twenty_seven, LEFT, buff=0.5)
        line = Line(twenty_seven.get_left(), twenty_seven.get_right()).next_to(twenty_seven, DOWN)
        equals_sign = Tex("=").scale(0.7).next_to(minus_sign, DOWN * 3, buff=0.2)

        # Display the numbers
        self.play(Write(fifty_three))
        self.play(Write(twenty_seven))
        self.play(Write(one_in_box), Write(ten_in_box))
        self.wait(1)
        self.play(Write(minus_sign))
        self.play(Write(line))
        self.wait(1)
        self.play(Write(equals_sign))

        # Highlight the need for borrowing
        borrow_text = Text("As 7 > 3, we need to borrow from 5", font_size=28)
        borrow_text.next_to(line, DOWN * 2.5)
        self.play(Write(borrow_text))
        self.wait(2)

        # Strike through the original digits
        strike_five = Line(fifty_three[0].get_top(), fifty_three[0].get_bottom(), stroke_width=5, color=RED)
        strike_three = Line(fifty_three[1].get_top(), fifty_three[1].get_bottom(), stroke_width=5, color=RED)

        self.play(Create(strike_five), Create(strike_three))
        self.wait(1)

        # Change 5 to 4 and 3 to 13 with borrowing
        borrowed_four = MathTex("4", font_size=48).move_to(fifty_three[0].get_center() + UP * 1.2 + LEFT * 0.2)
        borrowed_thirteen = MathTex("13", font_size=48).move_to(fifty_three[1].get_center() + UP * 1.2 + RIGHT * 0.2)

        self.play(Write(borrowed_four))
        self.play(Write(borrowed_thirteen))
        self.wait(1)

        # Result digits
        result_digit2 = MathTex("6", font_size=54)
        result_digit1 = MathTex("2", font_size=54)

        # Place the digits manually starting from the right side
        result_digit2.move_to(fifty_three[1].get_center() + DOWN * 1.5)
        result_digit1.next_to(result_digit2, LEFT, buff=0.75)

        # Display result digits from right to left
        self.play(Write(result_digit2))
        self.play(Write(result_digit1))
        self.wait(2)

        # Show final result
        final_result = MathTex("53 - 27 = 26", font_size=48)
        final_result.next_to(borrow_text, DOWN * 1)

        self.play(Write(final_result))
        self.wait(2)
        

    def Borrow_3Anim(self):

        title = Text("Three-digit Borrowing in Subtraction", font_size=48).to_edge(UP)
        
        # Subtraction problem
        problem_text = MathTex("Example: 205 - 137 = ?", font_size=35).next_to(title, DOWN, buff=0.5)

        # Display the title and the problem
        self.play(Write(title))
        self.play(Write(problem_text))
        self.wait(1)

        # Breaking down the numbers for visualization
        two_zero_five = MathTex("2", "0", "5", font_size=48)
        one_three_seven = MathTex("1", "3", "7", font_size=48)
        two_zero_five.arrange(RIGHT, buff=0.75)
        one_three_seven.arrange(RIGHT, buff=0.75)
        two_zero_five.next_to(problem_text, DOWN, buff=1)
        one_three_seven.next_to(two_zero_five, DOWN, buff=0.5)
        
        # Position labels for 1, 10, 100
        # Borrowing annotations
        hundred_in_box = MathTex("100", font_size=24, color=BLUE).next_to(two_zero_five[0], UP * 2.5 + RIGHT*1, buff=0.2)
        ten_in_box = MathTex("10", font_size=24, color=YELLOW).next_to(two_zero_five[1], UP * 2.5 +RIGHT*1, buff=0.2)
        one_in_box = MathTex("1", font_size=24, color=GREEN).next_to(two_zero_five[2], UP * 2.5+ RIGHT*1, buff=0.2)
        
        # Minus sign and line
        minus_sign = Tex("-").scale(1).next_to(one_three_seven, LEFT, buff=0.5)
        line = Line(one_three_seven.get_left(), one_three_seven.get_right()).next_to(one_three_seven, DOWN)
        equals_sign = Tex("=").scale(0.7).next_to(minus_sign, DOWN * 3, buff=0.2)

        # Centering all elements
        all_elements = VGroup(two_zero_five, one_three_seven, minus_sign, line, equals_sign)
        all_elements.move_to(ORIGIN)

        # Display the numbers and annotations
        self.play(Write(two_zero_five))
        self.play(Write(one_three_seven))
        self.play(Write(hundred_in_box), Write(ten_in_box), Write(one_in_box))
        self.wait(1)
        self.play(Write(minus_sign))
        self.play(Write(line))
        self.wait(1)
        self.play(Write(equals_sign))

        # Highlight the need for borrowing
        borrow_text = Text("As 7 > 5, we need to borrow from 0, which also borrows from 2", font_size=28)
        borrow_text.next_to(line, DOWN, buff=1.5)
        self.play(Write(borrow_text))
        self.wait(2)

        # Step-by-step borrowing
        # Borrow from the 2 to make the 0 a 10
        borrowed_one = MathTex("1", font_size=40).next_to(two_zero_five[0], UP, buff=0.2)
        ten_in_box = MathTex("10", font_size=40).next_to(two_zero_five[1], UP, buff=0.2)
        strike_two = Line(two_zero_five[0].get_top(), two_zero_five[0].get_bottom(), stroke_width=5, color=RED)

        self.play(Create(strike_two))
        self.play(Write(borrowed_one))
        self.wait(1)
        self.play(Write(ten_in_box))
        self.wait(2)

        # Borrow from the new 10 to make the 5 a 15
        borrowed_nine = MathTex("9", font_size=40).next_to(two_zero_five[1], UP, buff=0.2)
        fifteen_in_box = MathTex("15", font_size=40).next_to(two_zero_five[2], UP, buff=0.2)
        strike_zero = Line(two_zero_five[1].get_top(), two_zero_five[1].get_bottom(), stroke_width=5, color=RED)
        strike_five = Line(two_zero_five[2].get_top(), two_zero_five[2].get_bottom(), stroke_width=5, color=RED)

        self.play(Create(strike_zero))
        self.play(Transform(ten_in_box,borrowed_nine))
        self.wait(1)
        self.play(Create(strike_five))
        self.play(Write(fifteen_in_box))
        self.wait(1)

        # Perform the subtraction
        result_digits = MathTex("0", "6", "8", font_size=48)
        result_digits.arrange(RIGHT, buff=0.75)
        for i in range(2, -1, -1):
            self.play(Write(result_digits[i].move_to(two_zero_five[i].get_center() + DOWN * 1.5)))

        self.wait(2)

        # Show final result
        final_result = MathTex("205 - 137 = 68", font_size=48)
        final_result.next_to(borrow_text, DOWN * 1.5)
        self.play(Write(final_result))
        self.wait(2)



    def SetDeveloperList(self):  
        self.DeveloperList="Gayathri Veeramreddy"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Subtraction.py"

 

if __name__ == "__main__":
    scene = Subtraction()
    scene.render() 