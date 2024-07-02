# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla

from manim import *
from AbstractAnim import AbstractAnim
import cvo 

class Chap8G2_Subtraction(AbstractAnim):
    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.sub()
        self.fadeOutCurrentScene()
        self.Heading()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

    def SetDeveloperList(self):
        self.DeveloperList="Prithiv Shiv"
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade2Chapter8SubtractionOfNumbers.py"


    def Introduction(self):
        self.isRandom=False
        self.setNumberOfCirclePositions(4)
        title=Text("Subraction of Numbers").to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        p11=cvo.CVO().CreateCVO("Subtraction","")
        p13=cvo.CVO().CreateCVO("Definition","Process of taking\\\\1 number from another")
        p14=cvo.CVO().CreateCVO("Notation","5-3")
        p11.cvolist.append(p13)
        p11.cvolist.append(p14)
        self.construct1(p11,p11)

    def sub(self):
        self.isRandom=False
        self.setNumberOfCirclePositions(5)
        p10 = cvo.CVO().CreateCVO("Subtraction ", "15 - 7")

        p11 = cvo.CVO().CreateCVO("Unit Digit Check", "$5 < 7$")

        p12 = cvo.CVO().CreateCVO("Carry Over", "Borrow from next digit(1)").setangle(-TAU/4)

        p13 = cvo.CVO().CreateCVO("Tenth Digit Adjustment", "1 becomes 0,\\\\5 becomes 15")

        p14 = cvo.CVO().CreateCVO("Perform Subtraction", "15 - 7 = 8")

        p13.setcircleradius(1.3)
        p12.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        p13.cvolist.append(p14)

        self.construct1(p10,p10)
        
    
    def Heading(self):
        title = Text("Subtraction Examples", font_size=72).to_edge(UP)
        self.play(Write(title))
        self.wait(2)

        # Subtraction problem
        problems = [(20,18),
                    (31,26), 
                    (15,11),
                    (52, 18), 
                    (45, 29)
                    ]

        for minuend, subtrahend in problems:
            self.animate_subtraction(minuend, subtrahend)
            self.wait(2)
            self.clear()

    def animate_subtraction(self,minuend, subtrahend):
        # Convert numbers to strings
        minuend_str = str(minuend)
        subtrahend_str = str(subtrahend)

        # Create Tex objects for each digit
        minuend_digits = VGroup(*[Tex(char, font_size=72) for char in minuend_str])
        subtrahend_digits = VGroup(*[Tex(char, font_size=72) for char in subtrahend_str])
        result_digits = VGroup(*[Tex('0', font_size=72) for _ in minuend_str])
        carry_digits = VGroup(*[Tex('', font_size=36, color=YELLOW) for _ in minuend_str])

        # Position the digits correctly
        for i, digit in enumerate(minuend_digits):
            digit.move_to(UP + (i - 0.5) * RIGHT)

        for i, digit in enumerate(subtrahend_digits):
            digit.move_to((i - 0.5) * RIGHT)

        for i, digit in enumerate(result_digits):
            digit.move_to(DOWN + (i - 0.5) * RIGHT)

        for i, digit in enumerate(carry_digits):
            digit.next_to(minuend_digits[i], UP)

        # Display the digits
        self.play(*[Write(digit) for digit in minuend_digits + subtrahend_digits])
        self.wait(1)

        # Create and display the minus sign
        minus_sign = Tex("-", font_size=72).next_to(subtrahend_digits, LEFT)
        self.play(Write(minus_sign))
        self.wait(1)

        # Create and display the line below the subtraction
        line = Line(start=minuend_digits.get_left() + LEFT, end=minuend_digits.get_right() + RIGHT)
        line.next_to(subtrahend_digits, DOWN)
        self.play(Create(line))
        self.wait(1)

        arrow=None
        # Animate the subtraction process
        for i in range(1, -1, -1):
            # Extract the digits
            minuend_digit = int(minuend_str[i])
            subtrahend_digit = int(subtrahend_str[i])

            # Determine if we need to carry over
            if minuend_digit < subtrahend_digit:
                # Borrow from the next column
                minuend_digit += 10
                arrow = Arrow(start=minuend_digits[i-1].get_top(), end=minuend_digits[i].get_top(), buff=0.1, color=YELLOW)
                self.play(Write(arrow))
                self.wait(1)

                # Update the carry digit above
                new_carry = int(minuend_str[i-1]) - 1
                carry_digits[i-1].set_text(str(new_carry))
                self.play(Transform(carry_digits[i-1], Tex(str("1"), font_size=42, color=YELLOW).move_to(carry_digits[i-1]).next_to(arrow,0.5*DOWN)))

                # Update the minuend digit text without adding an extra Tex object
                minuend_str = minuend_str[:i-1] + str(new_carry) + minuend_str[i:]
                self.remove(minuend_digits[i-1])
                minuend_digits[i-1] = Tex(str(new_carry), font_size=72).move_to(UP + (i - 1 - 0.5) * RIGHT)
                self.play(Write(minuend_digits[i-1]))

            # Perform the subtraction
            result_digit = minuend_digit - subtrahend_digit
            self.remove(result_digits[i])
            result_digits[i] = Tex(str(result_digit), font_size=72).move_to(DOWN + (i - 0.5) * RIGHT)
            self.play(Write(result_digits[i]))
            self.wait(1)

        # Create and display the final result line
        result_line = Line(start=minuend_digits.get_left() + LEFT, end=minuend_digits.get_right() + RIGHT)
        result_line.next_to(result_digits, DOWN)
        self.play(Create(result_line))
        self.wait(1)

        # Display the final result
        final_result_text = Tex(f"Result: {minuend - subtrahend}", font_size=72)
        final_result_text.move_to(3 * DOWN)
        self.play(Write(final_result_text))
        self.wait(2)

        # Fade out all elements
        all_mobjects = [*minuend_digits, *subtrahend_digits, *result_digits, *carry_digits, minus_sign, line,arrow, result_line, final_result_text]
        self.play(*[FadeOut(mobj) for mobj in all_mobjects])
        self.wait(1)
       
      
if __name__ == "__main__":
    scene = Chap8G2_Subtraction()
    scene.render()