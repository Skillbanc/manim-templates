import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class numbers(AbstractAnim):
    def construct(self):
        # self.Introduction()
        self.test()

    def Introduction(self):
        self.angleChoice=[TAU/4,TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Three-digit Number","").setPosition([-3,0,0])
        p11=cvo.CVO().CreateCVO("Ones","1").setPosition([0,2,0])
        p12=cvo.CVO().CreateCVO("Tens","10").setPosition([3,0,0])
        p13=cvo.CVO().CreateCVO("Hundereds","100").setPosition([0,-2,0])
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

        # hundered1 = Text("1 hundred + 1 one = 101").shift(UP*2).set_color(YELLOW)
        # self.play(Write(hundered1))
        # self.wait(2)

        # hundered10 = Text("1 hundred + 1 ten = 110").next_to(hundered1,DOWN,buff=1).set_color(YELLOW)
        # self.play(Write(hundered10))
        # self.wait(2)

        # hundered11 = Text("1 hundred + 1 ten + 1 one = 111").next_to(hundered10,DOWN,buff=1).set_color(YELLOW)
        # self.play(Write(hundered11))
        # self.wait(2)
    
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
        ).arrange(RIGHT, buff=0.5)
        hundreds_tens_ones_349.next_to(digits_349, DOWN, buff=1.0)
      
        digits_349_text = Text("3, 4, and 9 are the digits", font_size=36, color=YELLOW)
        digits_349_text.next_to(hundreds_tens_ones_349, DOWN,buff = 1)

        self.play(Transform(three_digit_number, digits_349),Write(hundreds_tens_ones_349))
        self.wait(1)
        
        self.play(Write(digits_349_text))
        self.wait(2)

        # Ending the scene
        self.play(FadeOut(three_digit_number,digits_349_text,three_digit_text,hundreds_tens_ones_349))

    def testt(self):
        # title = Text("Comparing numbers", font_size=40)
        # self.play(Write(title))
        # self.play(title.animate.to_edge(UP))

        # # Explain Less Than (<)
        # less_than = MathTex(r"<", font_size=72, color=RED)
        # less_than.move_to(UP*2)
        # less_than_text = Text("Less Than", font_size=36, color=YELLOW)
        # less_than_text.next_to(less_than, DOWN)

        # self.play(Write(less_than), Write(less_than_text))
        
        # # Demonstrate with stacked objects
        # left_stack_lt = VGroup(*[Square(side_length=0.5, fill_color=BLUE, fill_opacity=1) for _ in range(3)]).arrange(UP, buff=0.1)
        # right_stack_lt = VGroup(*[Square(side_length=0.5, fill_color=GREEN, fill_opacity=1) for _ in range(5)]).arrange(UP, buff=0.1)
        
        # left_stack_lt.move_to(LEFT*3 + DOWN*1)
        # right_stack_lt.move_to(RIGHT*3 + DOWN*1)
        
        # self.play(Write(left_stack_lt), Write(right_stack_lt))
        
        # self.wait(2)
        # self.play(FadeOut(less_than), FadeOut(less_than_text), FadeOut(left_stack_lt), FadeOut(right_stack_lt))

        # # Explain Greater Than (>)
        # greater_than = MathTex(r">", font_size=72, color=RED)
        # greater_than.move_to(UP*2)
        # greater_than_text = Text("Greater Than", font_size=36, color=YELLOW)
        # greater_than_text.next_to(greater_than, DOWN)

        # self.play(Write(greater_than), Write(greater_than_text))
        
        # # Demonstrate with stacked objects
        # left_stack_gt = VGroup(*[Square(side_length=0.5, fill_color=BLUE, fill_opacity=1) for _ in range(6)]).arrange(UP, buff=0.1)
        # right_stack_gt = VGroup(*[Square(side_length=0.5, fill_color=GREEN, fill_opacity=1) for _ in range(4)]).arrange(UP, buff=0.1)
        
        # left_stack_gt.move_to(LEFT*3 + DOWN*1)
        # right_stack_gt.move_to(RIGHT*3 + DOWN*1)
        
        # self.play(Write(left_stack_gt), Write(right_stack_gt))
        
        # self.wait(2)
        # self.play(FadeOut(greater_than), FadeOut(greater_than_text), FadeOut(left_stack_gt), FadeOut(right_stack_gt))

        # # Explain Equals To (=)
        # equals_to = Tex(r"=", font_size=72, color=RED)
        # equals_to.move_to(UP*2)
        # equals_to_text = Text("Equals To", font_size=36, color=YELLOW)
        # equals_to_text.next_to(equals_to, DOWN)

        # self.play(Write(equals_to), Write(equals_to_text))
        
        # # Demonstrate with stacked objects
        # left_stack_eq = VGroup(*[Square(side_length=0.5, fill_color=BLUE, fill_opacity=1) for _ in range(5)]).arrange(UP, buff=0.1)
        # right_stack_eq = VGroup(*[Square(side_length=0.5, fill_color=GREEN, fill_opacity=1) for _ in range(5)]).arrange(UP, buff=0.1)
        
        # left_stack_eq.move_to(LEFT*3 + DOWN*1)
        # right_stack_eq.move_to(RIGHT*3 + DOWN*1)
        
        # self.play(Write(left_stack_eq), Write(right_stack_eq))

        # self.wait(2)

        # # Ending the scene
        # self.play(
        #     FadeOut(equals_to), FadeOut(equals_to_text),
        #     FadeOut(left_stack_eq), FadeOut(right_stack_eq),
        #     FadeOut(title)
        # )

        # self.wait(2)






        title = Text("Comparing numbers", font_size=40)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        # Explain Less Than (<)
        less_than = MathTex(r"<", font_size=72, color=RED)
        less_than.move_to(RIGHT*2+UP*1)
        less_than_text = Text("Less Than", font_size=36, color=YELLOW)
        less_than_text.next_to(less_than, DOWN)
        example_text = MathTex(r"3<5",font_size=72,color = YELLOW).next_to(less_than_text,DOWN,buff=1)

        self.play(Write(less_than), Write(less_than_text))
        
        # Demonstrate with stacked objects
        left_stack_lt = VGroup(*[Square(side_length=0.5, fill_color=BLUE, fill_opacity=1) for _ in range(3)]).arrange(UP, buff=0.1)
        right_stack_lt = VGroup(*[Square(side_length=0.5, fill_color=GREEN, fill_opacity=1) for _ in range(5)]).arrange(UP, buff=0.1)
        
        left_stack_lt.move_to(LEFT*3 + DOWN*1.65)
        right_stack_lt.move_to(LEFT*2 + DOWN*1)
        line1=Line(LEFT*6,LEFT*2).shift(DOWN*2.75,RIGHT*1).set_color(YELLOW)
        line2=Line(line1.get_left(),line1.get_right()+UP*5).set_color(YELLOW)
        self.play(Write(left_stack_lt), Write(right_stack_lt))
        self.play(Write(line1),Write(line2))
        self.wait(2)
        self.play(Write(example_text))
        self.play(FadeOut(less_than), FadeOut(less_than_text,example_text), FadeOut(left_stack_lt), FadeOut(right_stack_lt),FadeOut(line1,line2))

        # Explain Greater Than (>)
        greater_than = MathTex(r">", font_size=72, color=RED)
        greater_than.move_to(RIGHT*2+UP*1)
        greater_than_text = Text("Greater Than", font_size=36, color=YELLOW)
        greater_than_text.next_to(greater_than, DOWN)
        example_text = MathTex(r"5>3",font_size=72,color = YELLOW).next_to(greater_than_text,DOWN,buff=1)
        self.play(Write(greater_than), Write(greater_than_text))
        
        # Demonstrate with stacked objects
        left_stack_gt = VGroup(*[Square(side_length=0.5, fill_color=BLUE, fill_opacity=1) for _ in range(5)]).arrange(UP, buff=0.1)
        right_stack_gt = VGroup(*[Square(side_length=0.5, fill_color=GREEN, fill_opacity=1) for _ in range(3)]).arrange(UP, buff=0.1)
        
        left_stack_gt.move_to(LEFT*4.25 + DOWN*1)
        right_stack_gt.move_to(LEFT*3 + DOWN*1.65)
        line1=Line(LEFT*6,LEFT*2).shift(DOWN*2.75,RIGHT*1).set_color(YELLOW)
        line2=Line(line1.get_right(),line1.get_left()+UP*5).set_color(YELLOW)
        self.play(Write(left_stack_gt), Write(right_stack_gt))
        self.play(Write(line1),Write(line2))
        self.wait(2)
        self.play(Write(example_text))
        self.play(FadeOut(greater_than), FadeOut(greater_than_text,example_text), FadeOut(left_stack_gt), FadeOut(right_stack_gt),FadeOut(line1,line2))

        # Explain Equals To (=)
        equals_to = Tex(r"=", font_size=72, color=RED)
        equals_to.move_to(RIGHT*2+UP*1)
        equals_to_text = Text("Equals To", font_size=36, color=YELLOW)
        equals_to_text.next_to(equals_to, DOWN)
        example_text=MathTex(r"5=5",font_size=72,color = YELLOW).next_to(greater_than_text,DOWN,buff=1)
        self.play(Write(equals_to), Write(equals_to_text))
        
        # # Demonstrate with stacked objects
        left_stack_eq = VGroup(*[Square(side_length=0.5, fill_color=BLUE, fill_opacity=1) for _ in range(5)]).arrange(UP, buff=0.1)
        right_stack_eq = VGroup(*[Square(side_length=0.5, fill_color=GREEN, fill_opacity=1) for _ in range(5)]).arrange(UP, buff=0.1)
        
        left_stack_eq.move_to(LEFT*3 + DOWN*1)
        right_stack_eq.move_to(LEFT*2 + DOWN*1)
        line1=Line(LEFT*6,LEFT*2).set_color(YELLOW).shift(UP*0.75,RIGHT*1.5)
        line2=Line(line1.get_left()+DOWN*3.25,line1.get_right()+DOWN*3.25).set_color(YELLOW)
        self.play(Write(left_stack_eq), Write(right_stack_eq))
        self.play(Write(line1),Write(line2))
        self.wait(2)
        self.play(Write(example_text))
        # # Ending the scene
        self.play(
            FadeOut(equals_to), FadeOut(equals_to_text),
            FadeOut(left_stack_eq), FadeOut(right_stack_eq),
            FadeOut(title)
        )

        self.wait(2)


    def test(self):
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
        self.wait(2)




        











    def SetDeveloperList(self):
        self.DeveloperList="Sindhu"
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="MultiplyandDivide.py"

              
if __name__ == "__main__":
    scene = numbers()
    scene.render()