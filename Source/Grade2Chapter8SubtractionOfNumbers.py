from manim import *
from AbstractAnim import AbstractAnim
import cvo

class Chap8G2_Subtraction(AbstractAnim):
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
        self.DeveloperList = "Prithiv Shiv"
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName = "Grade2Chapter8SubtractionOfNumbers.py"

    def Introduction(self):
        self.isRandom = False
        self.setNumberOfCirclePositions(4)
        title = Text("Subtraction of Numbers").to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        p11 = cvo.CVO().CreateCVO("Subtraction", "")
        p13 = cvo.CVO().CreateCVO("Definition", "Process of taking\\\\1 number from another")
        p11.cvolist.append(p13)
        self.construct1(p11, p11)

    def sub(self):
        self.isRandom = False
        self.setNumberOfCirclePositions(5)

        # Title
        title = Text("Subtraction Process", font_size=72).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Example numbers
        example = Text("Example: 15 - 7", font_size=48).to_edge(DOWN)
        self.play(Write(example))
        self.wait(1)

        # Step 1: Unit Digit Check
        step1 = Text("Step 1: Check the Unit Digits", font_size=48).to_edge(UP)
        self.play(Transform(title, step1))
        self.wait(1)
        
        explanation1 = Text("Look at the rightmost digits: 5 and 7.", font_size=36).next_to(step1, DOWN)
        self.play(Write(explanation1))
        self.wait(2)

        comparison = Text("Since 5 is smaller than 7, we need to borrow.", font_size=36).next_to(explanation1, DOWN)
        self.play(Write(comparison))
        self.wait(2)

        self.play(FadeOut(explanation1), FadeOut(comparison))

        # Step 2: Carry Over
        step2 = Text("Step 2: Carry Over", font_size=48).to_edge(UP)
        self.play(Transform(title, step2))
        self.wait(1)
        
        explanation2 = Text("Borrow 1 from the tens place.", font_size=36).next_to(step2, DOWN)
        self.play(Write(explanation2))
        self.wait(2)

        carry_over = Text("This makes 5 become 15.", font_size=36).next_to(explanation2, DOWN)
        self.play(Write(carry_over))
        self.wait(2)

        borrowed_example = Text("Now, it's 15 - 7.", font_size=36).next_to(carry_over, DOWN)
        self.play(Write(borrowed_example))
        self.wait(2)

        self.play(FadeOut(explanation2), FadeOut(carry_over), FadeOut(borrowed_example))

        # Step 3: Adjust the Tenth Digit
        step3 = Text("Step 3: Adjust the Tens Digit", font_size=48).to_edge(UP)
        self.play(Transform(title, step3))
        self.wait(1)
        
        explanation3 = Text("The tens digit becomes 0 because we borrowed 1.", font_size=36).next_to(step3, DOWN)
        self.play(Write(explanation3))
        self.wait(2)

        adjust_tenth = Text("Now, perform the subtraction.", font_size=36).next_to(explanation3, DOWN)
        self.play(Write(adjust_tenth))
        self.wait(2)

        self.play(FadeOut(explanation3), FadeOut(adjust_tenth))

        # Step 4: Perform Subtraction
        step4 = Text("Step 4: Subtract Each Digit", font_size=48).to_edge(UP)
        self.play(Transform(title, step4))
        self.wait(1)
        
        explanation4 = Text("15 - 7 = 8", font_size=36).next_to(step4, DOWN)
        self.play(Write(explanation4))
        self.wait(2)

        self.play(FadeOut(explanation4))

        self.play(FadeOut(step4), FadeOut(example))

        # Summary
        summary = Text("This is how we subtract numbers!", font_size=48).to_edge(DOWN)
        self.play(Write(summary))
        self.wait(2)


    def Heading(self):
        title = Text("Subtraction Examples", font_size=72).to_edge(UP)
        self.play(Write(title))
        self.wait(2)

        # Subtraction problems
        problems = [
            (20, 18),
            (31, 26), 
            (15, 11),
            (52, 18), 
            (45, 29)
        ]

        for minuend, subtrahend in problems:
            self.animate_subtraction(minuend, subtrahend)
            self.wait(2)
            self.clear_elements_except_heading(title)

    def clear_elements_except_heading(self, title):
        # Clear all elements except the title
        all_mobjects = self.mobjects.copy()
        all_mobjects.remove(title)
        self.play(*[FadeOut(mobj) for mobj in all_mobjects])

    def animate_subtraction(self, minuend, subtrahend):
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

        arrow = None
        explanation_texts = []

        # Animate the subtraction process
        for i in range(1, -1, -1):
            # Extract the digits
            minuend_digit = int(minuend_str[i])
            subtrahend_digit = int(subtrahend_str[i])

            # Explanation text position
            explanation_text_pos = 2 * UP if i == 1 else 2.5 * UP

            borrowed = False  # Flag to check if borrowing happened

            # Determine if we need to carry over
            if minuend_digit < subtrahend_digit:
                explanation_text = Tex(f"{minuend_digit} $<$ {subtrahend_digit}, borrowing from the tenths place", font_size=36).move_to(explanation_text_pos)
                self.play(Write(explanation_text))
                explanation_texts.append(explanation_text)
                self.wait(1)

                # Borrow from the next column
                minuend_digit += 10
                arrow = Arrow(start=minuend_digits[i-1].get_top(), end=minuend_digits[i].get_top(), buff=0.1, color=YELLOW)
                self.play(Write(arrow))
                self.wait(1)

                # Update the carry digit above
                new_carry = int(minuend_str[i-1]) - 1

                # Add slash to the original minuend digit before changing it
                slash = Line(start=minuend_digits[i-1].get_corner(UP + LEFT), end=minuend_digits[i-1].get_corner(DOWN + RIGHT), color=RED)
                self.play(Create(slash))
                self.wait(1)

                carry_digits[i-1].set_text("1")
                self.play(Transform(carry_digits[i-1], Tex("1", font_size=42, color=YELLOW).move_to(carry_digits[i-1]).next_to(arrow, 0.5 * DOWN)))

                # Update the minuend digit text without adding an extra Tex object
                minuend_str = minuend_str[:i-1] + str(new_carry) + minuend_str[i:]
                self.remove(minuend_digits[i-1])
                minuend_digits[i-1] = Tex(str(new_carry), font_size=72).move_to(UP + (i - 1 - 0.5) * RIGHT)
                self.play(Write(minuend_digits[i-1]))

                # Remove the slash after the new number pops
                self.play(FadeOut(slash))
                borrowed = True

            # Perform the subtraction
            result_digit = minuend_digit - subtrahend_digit
            self.remove(result_digits[i])
            result_digits[i] = Tex(str(result_digit), font_size=72).move_to(DOWN + (i - 0.5) * RIGHT)
            self.play(Write(result_digits[i]))
            self.wait(1)

            # Add the no borrowing needed explanation only if no borrowing happened
            # if not borrowed:
            #     explanation_text = Tex(f"{minuend_digit} $>=$ {subtrahend_digit}, no borrowing needed", font_size=36).move_to(explanation_text_pos)
            #     self.play(Write(explanation_text))
            #     explanation_texts.append(explanation_text)
            #     self.wait(1)

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
        all_mobjects = [*minuend_digits, *subtrahend_digits, *result_digits, *carry_digits, minus_sign, line, result_line, final_result_text] + explanation_texts
        if arrow is not None:
            all_mobjects.append(arrow)

        self.play(*[FadeOut(mobj) for mobj in all_mobjects])
        self.wait(1)

if __name__ == "__main__":
    scene = Chap8G2_Subtraction()
    scene.render()
