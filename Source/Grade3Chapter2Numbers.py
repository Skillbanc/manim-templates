import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class numbers(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.Hundred_intro()
        self.fadeOutCurrentScene()
        self.Placevalue()
        self.fadeOutCurrentScene()
        self.PlacevalueofZero()
        self.fadeOutCurrentScene()
        # self.Identifying_numbers()
        # self.fadeOutCurrentScene()
        self.UnderstandingDigits()
        self.fadeOutCurrentScene()
        self.ComparingNumbers()
        self.fadeOutCurrentScene()
        self.AscendingandDescending()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

    def Introduction(self):
        self.angleChoice=[TAU/4,TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Three-digit Number","").setPosition([-3,0,0])
        p11=cvo.CVO().CreateCVO("Ones","1").setPosition([0,2,0])
        p12=cvo.CVO().CreateCVO("Tens","10").setPosition([3,1,0])
        p13=cvo.CVO().CreateCVO("Hundereds","100").setPosition([3,-2,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
    
    def Hundred_intro(self):
        twodigit = Text("9 tens + 9 ones = 99").shift(UP*2)
        self.play(Write(twodigit))
        self.wait(2)
        text = Text("99 is the largest 2 digit number").next_to(twodigit,DOWN,buff=1).set_color(YELLOW)
        self.play(FadeIn(text))
        self.wait(2)
        self.play(FadeOut(twodigit,text))
        
        # Transform to the next equation
        threedigit = Text("9 tens ").shift(UP*2,LEFT*2)
        threedigit1 = Text("+ 9 ones + 1").next_to(threedigit,RIGHT,buff=0.3)
        self.play(Write(threedigit),Write(threedigit1))
        self.wait(2)
        transform_twodigit = Text("+ 1 ten").next_to(threedigit,RIGHT,buff=0.3)
        self.play(Transform(threedigit1, transform_twodigit))
        self.wait(2)
        threedigit2 = Text("= 10 tens").next_to(transform_twodigit,RIGHT,buff=0.3)
        self.play(Write(threedigit2))
        self.wait(1)
        transform_threedigit = Text("= 100").next_to(transform_twodigit,RIGHT,buff=0.3)
        self.play(Transform(threedigit2, transform_threedigit))
        self.wait(2)

        text = Text("100 is the smallest 3 digit number").set_color(YELLOW)
        self.play(FadeIn(text))
        self.wait(2)
        self.play(FadeOut(threedigit,threedigit1,threedigit2,text))
    
    def Placevalue(self):
        title = Text("Place Value", font_size=48)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        # Number 349 with closer spacing
        digits_close = VGroup(
            Tex("3", font_size=72, color=BLUE),
            Tex("4", font_size=72, color=GREEN),
            Tex("9", font_size=72, color=RED)
        ).arrange(RIGHT, buff=0.2)
        digits_close.move_to(UP*2)
        self.play(Write(digits_close))

        # Move digits to original position with larger spacing
        digits_original = VGroup(
            Tex("3", font_size=72, color=BLUE),
            Tex("4", font_size=72, color=GREEN),
            Tex("9", font_size=72, color=RED)
        ).arrange(RIGHT, buff=1.0)
        digits_original.move_to(UP*2)
        self.play(Transform(digits_close, digits_original))

        # Explanation boxes
        explanations = VGroup(
            Tex(
                r"Ones place \\ 9 ones \\ Place value = 9 x 1 = 9",
                font_size=36, color=YELLOW
            ).scale(0.8),
            Tex(
                r"Tens place \\ 4 tens \\ Place value = 4 x 10 = 40",
                font_size=36, color=YELLOW
            ).scale(0.8),
            Tex(
                r"Hundreds place \\ 3 hundreds \\ Place value = 3 x 100 = 300",
                font_size=36, color=YELLOW
            ).scale(0.8)
        )

        explanations[0].to_edge(RIGHT).shift(DOWN*1)
        explanations[1]
        explanations[2].to_edge(LEFT).shift(DOWN*1)

        # Arrows
        arrows = VGroup(
            Arrow(digits_original[2].get_bottom(), explanations[0].get_top(), buff=0.1),
            Arrow(digits_original[1].get_bottom(), explanations[1].get_top(), buff=0.1),
            Arrow(digits_original[0].get_bottom(), explanations[2].get_top(), buff=0.1)
        )

        for exp, arr in zip(explanations, arrows):
            self.play(GrowArrow(arr))
            self.play(Write(exp))
            self.wait(2)
        
    def Identifying_numbers(self):
        text = Text("Identify the Number using hundereds, tens and ones",font_size=40).set_color(BLUE).to_edge(UP)
        self.play(Write(text))
        self.wait(2)
        table_data = [
            ["100", "10", "1", "Number"],
            ["2", "5", "3", ""],
            ["9", "1", "-", ""],
            ["7", "-", "4", ""],
        ]
        
        # Create the table
        table = Table(
            table_data,
            include_outer_lines=True,
        )
        # Add different colors to each column
        colors = [BLUE, GREEN, RED, YELLOW]
        for i, color in enumerate(colors):
            for j in range(4):
                cell = table.get_cell((j+1, i+1))
                cell.set_fill(color, opacity=0.5)
        table.scale(0.75)

        # Add the table to the scene
        self.play(FadeIn(table))
        self.wait(2)

        number1=Text("253",font_size=35).shift(RIGHT*2,UP*0.5).set_color(YELLOW)
        self.play(FadeIn(number1))
        self.wait(2)

        number2=Text("910",font_size=35).next_to(number1,DOWN,buff=0.75).set_color(YELLOW)
        self.play(FadeIn(number2))
        self.wait(2)

        number3=Text("704",font_size=35).next_to(number2,DOWN,buff=0.5).set_color(YELLOW)
        self.play(FadeIn(number3))
        self.wait(2)

    def UnderstandingDigits(self):
        title = Text("Understanding 1-digit, 2-digit, and 3-digit Numbers", font_size=40)
        self.play(Write(title))
        self.play(FadeOut(title))

        # Example of a 1-digit number
        one_digit_number = Tex("7", font_size=72, color=RED)
        ones_7 = Text("ones", font_size=36, color=YELLOW).next_to(one_digit_number,DOWN,buff=0.5)
        one_digit_text = Text("1-digit number", font_size=40)
        one_digit_text.to_edge(UP)
        self.play(Write(one_digit_text), Write(one_digit_number))
        self.play(Write(ones_7))

        self.wait(2)
        self.play(FadeOut(one_digit_number), FadeOut(one_digit_text,ones_7))

        # Example of a 2-digit number
        two_digit_number = Tex("42", font_size=72, color=BLUE)
        two_digit_number.move_to(UP*2)
        two_digit_text = Text("2-digit number", font_size=40)
        two_digit_text.to_edge(UP)
        self.play(Write(two_digit_text),Write(two_digit_number))

        digits_42 = VGroup(
            Tex("4", font_size=72, color=GREEN),
            Tex("2", font_size=72, color=GREEN)
        ).arrange(RIGHT, buff=2)
        digits_42.next_to(two_digit_number, DOWN, buff=0.5)

        tens_ones_42 = VGroup(
            Text("tens", font_size=36, color=YELLOW),
            Text("ones", font_size=36, color=YELLOW)
        ).arrange(RIGHT, buff=1.5)
        tens_ones_42.next_to(digits_42, DOWN, buff=0.75)

        digits_42_text = Text("4 and 2 are the digits", font_size=36, color=YELLOW)
        digits_42_text.next_to(tens_ones_42, DOWN,buff = 1)

        self.play(Transform(two_digit_number, digits_42),Write(tens_ones_42))
        self.wait(1)

        self.play(Write(digits_42_text))
        self.wait(2)

        self.play(FadeOut(two_digit_number), FadeOut(digits_42_text), FadeOut(tens_ones_42),FadeOut(two_digit_text))

        # Example of a 3-digit number
        three_digit_number = Tex("349", font_size=72, color=PURPLE)
        three_digit_number.move_to(UP*2)
        three_digit_text = Text("3-digit number", font_size=40)
        three_digit_text.to_edge(UP)
        self.play(Write(three_digit_number), Write(three_digit_text))

        digits_349 = VGroup(
            Tex("3", font_size=72, color=GREEN),
            Tex("4", font_size=72, color=GREEN),
            Tex("9", font_size=72, color=GREEN)
        ).arrange(RIGHT, buff=2)
        digits_349.next_to(three_digit_number, DOWN, buff=1.0)

        hundreds_tens_ones_349 = VGroup(
            Text("hundreds", font_size=36, color=YELLOW),
            Text("tens", font_size=36, color=YELLOW),
            Text("ones", font_size=36, color=YELLOW)
        ).arrange(RIGHT, buff=1)
        hundreds_tens_ones_349.next_to(digits_349, DOWN, buff=1.0)
      
        digits_349_text = Text("3, 4, and 9 are the digits", font_size=36, color=YELLOW)
        digits_349_text.next_to(hundreds_tens_ones_349, DOWN,buff = 1)

        self.play(Transform(three_digit_number, digits_349),Write(hundreds_tens_ones_349))
        self.wait(1)
        
        self.play(Write(digits_349_text))
        self.wait(2)

        # Ending the scene
        self.play(FadeOut(three_digit_number,digits_349_text,three_digit_text,hundreds_tens_ones_349))

    def ComparingNumbers(self):
        title = Text("Comparing numbers", font_size=40)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        comparisons = [
            (r"<", "Less Than", r"3<5", [(3, BLUE), (5, GREEN)], LEFT*3 + DOWN*1.65, LEFT*2 + DOWN*1, (DOWN*2.75, RIGHT*1)),
            (r">", "Greater Than", r"5>3", [(5, BLUE), (3, GREEN)], LEFT*4.25 + DOWN*1, LEFT*3 + DOWN*1.65, (DOWN*2.75, RIGHT*1)),
            (r"=", "Equals To", r"5=5", [(5, BLUE), (5, GREEN)], LEFT*3 + DOWN*1, LEFT*2 + DOWN*1, (UP*0.75, RIGHT*1.5))
        ]

        for symbol, text, example, stacks, left_pos, right_pos, line_shift in comparisons:
            math_symbol = MathTex(symbol, font_size=72, color=RED)
            math_symbol.move_to(RIGHT*2 + UP*1)
            text_obj = Text(text, font_size=36, color=YELLOW)
            text_obj.next_to(math_symbol, DOWN)
            example_text = MathTex(example, font_size=72, color=YELLOW).next_to(text_obj, DOWN, buff=1)

            self.play(Write(math_symbol), Write(text_obj))

            left_stack = VGroup(*[Square(side_length=0.5, fill_color=stacks[0][1], fill_opacity=1) for _ in range(stacks[0][0])]).arrange(UP, buff=0.1)
            right_stack = VGroup(*[Square(side_length=0.5, fill_color=stacks[1][1], fill_opacity=1) for _ in range(stacks[1][0])]).arrange(UP, buff=0.1)

            left_stack.move_to(left_pos)
            right_stack.move_to(right_pos)

            if symbol == r"<":         
                line1=Line(LEFT*6,LEFT*2).shift(DOWN*2.75,RIGHT*1).set_color(YELLOW)
                line2=Line(line1.get_left(),line1.get_right()+UP*5).set_color(YELLOW)

            elif symbol == r">":
                line1=Line(LEFT*6,LEFT*2).shift(DOWN*2.75,RIGHT*1).set_color(YELLOW)
                line2=Line(line1.get_right(),line1.get_left()+UP*5).set_color(YELLOW)

            else :
                line1=Line(LEFT*6,LEFT*2).set_color(YELLOW).shift(UP*0.75,RIGHT*1.5)
                line2=Line(line1.get_left()+DOWN*3.5,line1.get_right()+DOWN*3.5).set_color(YELLOW)              

            self.play(Write(left_stack), Write(right_stack))
            self.play(Write(line1), Write(line2))
            self.wait(2)
            self.play(Write(example_text))

            self.play(FadeOut(math_symbol), FadeOut(text_obj, example_text), FadeOut(left_stack), FadeOut(right_stack), FadeOut(line1, line2))

        self.play(FadeOut(title))
    
    def AscendingandDescending(self):
        # Title
        title = Text("Ascending and Descending Order", font_size=40)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        # Define random numbers
        random_numbers = [3, 1, 4, 5, 2]
        initial_numbers = random_numbers.copy()  # To keep track of initial positions

        asc_desc = [
            ("Ascending Order", sorted(random_numbers), BLUE, DOWN*1),
            ("Descending Order", sorted(random_numbers, reverse=True), RED, DOWN*1)
        ]
        for desc, sorted_numbers, color, position in asc_desc:
            # Display initial random sequence
            initial_sequence = VGroup(*[MathTex(str(num), font_size=48) for num in random_numbers])
            initial_sequence.arrange(RIGHT, buff=1)
            initial_sequence.move_to(UP*2)

            self.play(Write(initial_sequence))
            self.wait(1)

            desc_text = Text(desc, font_size=36, color=color)
            desc_text.move_to(position + UP)
            self.play(Write(desc_text))

            if desc == "Ascending Order":
                explanation_text = Text("Arranging numbers from smallest to biggest", font_size=30)
            else:
                explanation_text = Text("Arranging numbers from biggest to smallest", font_size=30)
            
            explanation_text.shift(DOWN*1.5)
            self.play(Write(explanation_text))
            self.wait(1)
            self.play(FadeOut(explanation_text))               
            
            sorted_objects = VGroup(*[MathTex(str(num), font_size=48, color=color) for num in sorted_numbers])
            sorted_objects.arrange(RIGHT, buff=1)
            sorted_objects.next_to(desc_text, DOWN, buff=1)

            # Animate the sorting process
            initial_positions = initial_sequence.copy()
            sorted_indices = set()
            for i, num in enumerate(sorted_numbers):
                index = initial_numbers.index(num)
                # Ensure we get the next unsorted index
                while index in sorted_indices:
                    index = initial_numbers.index(num, index + 1)
                sorted_indices.add(index)
                self.play(initial_positions[index].animate.move_to(sorted_objects[i].get_center()).set_color(color),
                          run_time=0.5)
            
            self.wait(1)
            self.play(FadeOut(desc_text), FadeOut(initial_positions))

    def PlacevalueofZero(self):
        # Title
        title = MathTex("\\text{Place Value of 0 in Numbers}").scale(0.75)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        examples = [
            ("205", "no tens", 1),
            ("340", "no ones", 2)
        ]
        positions = [UP*2, UP*2]

        for (num, explanation, zero_index), position in zip(examples, positions):
            num_text = VGroup(*[MathTex(digit, font_size=72) for digit in num])
            num_text.arrange(RIGHT, buff=0.5).shift(UP*2)

            self.play(Write(num_text))

            # Extract digits
            hundreds = num[0] if len(num) == 3 else "0"
            tens = num[1] if len(num) >= 2 else "0"
            ones = num[2] if len(num) >= 3 else num[1] if len(num) == 2 else num[0]

            # Labels for hundreds, tens, ones
            labels = VGroup(
                VGroup(Text("Hundreds", font_size=24), MathTex(hundreds, font_size=48)).arrange(DOWN, buff=0.5).move_to(position + LEFT*3 + DOWN*3),
                VGroup(Text("Tens", font_size=24), MathTex(tens, font_size=48)).arrange(DOWN, buff=0.5).move_to(position + DOWN*3),
                VGroup(Text("Ones", font_size=24), MathTex(ones, font_size=48)).arrange(DOWN, buff=0.5).move_to(position + RIGHT*3 + DOWN*3)
            )

            self.play(Write(labels))

            # Add arrow and explanation for 0
            zero_digit = num_text[zero_index]
            arrow = Arrow(start=zero_digit.get_bottom(), end=zero_digit.get_bottom() + DOWN*1, buff=0.1, color=YELLOW)
            explanation_text = Text(explanation, font_size=24, color=YELLOW)
            explanation_text.next_to(arrow.get_end(), DOWN)

            self.play(Write(arrow), Write(explanation_text))
            self.wait(2)

            self.play(FadeOut(num_text), FadeOut(labels), FadeOut(arrow), FadeOut(explanation_text))

        self.play(FadeOut(title))

    def SetDeveloperList(self):
        self.DeveloperList="A.Sindhu sri"
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade3Chapter2Numbers.py"

              
if __name__ == "__main__":
    scene = numbers()
    scene.render()