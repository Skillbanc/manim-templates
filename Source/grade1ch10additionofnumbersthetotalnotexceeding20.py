from manim import *
from AbstractAnim import AbstractAnim
import cvo

class additionofnumbers(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.Add()
        self.fadeOutCurrentScene()
        self.Anim()  # Call the Anim method after Add
        self.fadeOutCurrentScene()
        self.add2()  # Call the Anim method after Add
        self.fadeOutCurrentScene()
        self.add1()  # Call the Anim method after Add
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
    
    def Add(self):
        self.isRandom = False
        t1 = Text("Chapter 10 : Addition of Numbers not Exceeding 20", font_size=35)
        t1.move_to([0, 0, 0])
        # Write the text and the underline
        self.play(Write(t1))
        self.wait(2)
        self.play(FadeOut(t1))
        
        p10 = cvo.CVO().CreateCVO("Addition", "")
        p12 = cvo.CVO().CreateCVO("Definition", "sum of two numbers")
        p11 = cvo.CVO().CreateCVO("Symbol", "+")
        p10.cvolist.append(p12)
        p10.cvolist.append(p11)
        self.setNumberOfCirclePositions(3)
        self.construct1(p10, p10)
        self.wait(2)


    def Anim(self):
        ex = Text("Example:", font_size=35)
        ex.move_to([-5, 3.3, 0])
        self.play(Write(ex))
        self.wait(1)

        problems = [
            (6, 6, 12),
            (6, 4, 10),
            (4, 4, 8)
        ]
    
        def create_chick(chick, row, col):
            chick_text = Text(chick, font_size=30, color=YELLOW)
            x_pos = -6 + col * 1  # Adjust horizontal spacing (1 is an example)
            y_pos = 1 - row * 1   # Adjust vertical spacing (1 is an example)
            chick_text.move_to(np.array([x_pos, y_pos, 0]))
            return chick_text
        
        chick_emoji = "🌻"

        for first_addend, second_addend, result in problems:
            problem_text = Text(f"{first_addend} + {second_addend} = {result}", font_size=40, color=BLUE)
            self.play(Write(problem_text))
            self.wait(1)
            self.play(problem_text.animate.shift(UP * 3.3))
            self.wait(1)
            
            # Create emojis for first addend
            first_addend_chick = VGroup()
            for i in range(first_addend):
                col = i % 5  # Adjust columns as needed
                row = i // 5  # Adjust rows as needed
                chick = create_chick(chick_emoji, row, col)
                first_addend_chick.add(chick)
            
            first_addend_label = Text(f"{first_addend}", font_size=24)
            first_addend_label.next_to(first_addend_chick, DOWN)
            
            self.play(
                FadeIn(first_addend_chick),
                Write(first_addend_label)
            )
            self.wait(2)

            # Animate addition
            plus_text = Text("+", font_size=125, color=BLUE)
            plus_text.next_to(first_addend_chick, RIGHT)
            self.play(Write(plus_text))
            self.wait(1)

            # Create emojis for second addend
            second_addend_chick = VGroup()
            for i in range(second_addend):
                col = i % 4  # Adjust columns as needed
                row = i // 4  # Adjust rows as needed
                chick = create_chick(chick_emoji, row, col)
                second_addend_chick.add(chick)

            second_addend_chick.next_to(plus_text, RIGHT)
            
            second_addend_label = Text(f"{second_addend}", font_size=24)
            second_addend_label.next_to(second_addend_chick, DOWN)
            
            self.play(
                FadeIn(second_addend_chick),
                Write(second_addend_label)
            )
            self.wait(2)

            # Animate equals sign
            equal_text = Text("=", font_size=125, color=BLUE)
            equal_text.next_to(second_addend_chick, RIGHT)
            self.play(Write(equal_text))
            self.wait(1)

            # Create emojis for result
            result_chick = VGroup()
            for i in range(result):
                col = i % 3  # Adjust columns as needed
                row = i // 3  # Adjust rows as needed
                chick = create_chick(chick_emoji, row, col)
                result_chick.add(chick)

            result_chick.next_to(equal_text, RIGHT)
            
            result_label = Text(f"{result}", font_size=24)
            result_label.next_to(result_chick, DOWN)
            
            self.play(
                FadeIn(result_chick),
                Write(result_label)
            )
            self.wait(2)
            
            # Fade out all elements for the current problem
            self.play(
                FadeOut(problem_text),
                FadeOut(first_addend_chick),
                FadeOut(second_addend_chick),
                FadeOut(result_chick),
                FadeOut(first_addend_label),
                FadeOut(second_addend_label),
                FadeOut(result_label),
                FadeOut(plus_text),
                FadeOut(equal_text)
            )
        
        self.wait(0)

    def add1(self):
        # Create and display the initial text
        t1 = Text("Calculate the sum for the following pairs of numbers:", font_size=35).to_edge(UP + LEFT * 1)
        self.play(Write(t1))
        
        # # Define and display the first addition expression (s1)
        s1 = Text("14 + 3 = ", color=PINK, font_size=33).to_edge(LEFT * 3.5 + UP * 3.5)
        ss1 = Square(side_length=0.8).next_to(s1, RIGHT)
        self.play(Write(s1, run_time=2))
        self.play(Write(ss1, run_time=2))

        # # Highlight unit's place digits 3 (in 23) and 4 (in 14)
        s1_unit_highlighted = Text("14 + 3 = ", t2c={'4': YELLOW, '+': PURE_GREEN, '3': YELLOW}, font_size=33).to_edge(LEFT * 3.5 + UP * 3.5)
        self.play(Transform(s1, s1_unit_highlighted))
        self.wait(1)

        # # Write the intermediate result for the unit place in the square
        intermediate_result_1 = Text("7", color=BLUE, font_size=33).move_to(ss1.get_center() + RIGHT * 0.12)
        self.play(Write(intermediate_result_1))
        self.wait(1)

        # # Fade out the highlighted text and return to the original color
        s1_original = Text("14 + 3 = ", color=PINK, font_size=33).to_edge(LEFT * 3.5 + UP * 3.5)
        self.play(Transform(s1, s1_original))
        self.wait(1)

        # # Highlight tens place digits 2 (in 23) and 1 (in 14)
        s1_tens_highlighted = Text("14 + 3 = ", t2c={'1': YELLOW}, font_size=33).to_edge(LEFT * 3.5 + UP * 3.5)
        self.play(Transform(s1, s1_tens_highlighted))
        self.wait(1)

        # # Write the intermediate result for the tens place in the square, before the previous result
        intermediate_result_2 = Text("1", color=BLUE, font_size=33).move_to(ss1.get_center() + LEFT * 0.12)
        self.play(Write(intermediate_result_2))
        self.wait(1)

        # # Fade out the highlighted text and return to the original color
        self.play(Transform(s1, s1_original))
        self.wait(1)




        # # Define and display the second addition expression (s2)
        s2 = Text("13 + 5 = ", color=PINK, font_size=33).next_to(s1, DOWN * 3.5)
        ss2 = Square(side_length=0.8).next_to(s2, RIGHT)
        self.play(Write(s2, run_time=2))
        self.play(Write(ss2, run_time=2))

        # # Highlight unit's place digits 5 (in 75) and 4 (in 24)
        s2_unit_highlighted = Text("13 + 5 = ", t2c={'3': YELLOW, '+': PURE_GREEN, '5': YELLOW}, font_size=33).next_to(s1, DOWN * 3.5)
        self.play(Transform(s2, s2_unit_highlighted))
        self.wait(1)

        # # Write the intermediate result for the unit place in the square
        intermediate_result_1 = Text("8", color=BLUE, font_size=33).move_to(ss2.get_center() + RIGHT * 0.12)
        self.play(Write(intermediate_result_1))
        self.wait(1)

        # # Fade out the highlighted text and return to the original color
        s2_original = Text("13 + 5 = ", color=PINK, font_size=33).next_to(s1, DOWN * 3.5)
        self.play(Transform(s2, s2_original))
        self.wait(1)

        # # Highlight tens place digits 7 (in 75) and 2 (in 24)
        s2_tens_highlighted = Text("13 + 5 = ", t2c={'1': YELLOW}, font_size=33).next_to(s1, DOWN * 3.5)
        self.play(Transform(s2, s2_tens_highlighted))
        self.wait(1)

        # # Write the intermediate result for the tens place in the square, before the previous result
        intermediate_result_2 = Text("1", color=BLUE, font_size=33).move_to(ss2.get_center() + LEFT * 0.12)
        self.play(Write(intermediate_result_2))
        self.wait(1)

        # # Fade out the highlighted text and return to the original color
        self.play(Transform(s2, s2_original))
        self.wait(1)




        # # Define and display the third addition expression (s3)
        s3 = Text("8 + 6 = ", color=PINK, font_size=33).next_to(s2, DOWN * 3.5)
        ss3 = Square(side_length=0.8).next_to(s3, RIGHT)
        self.play(Write(s3, run_time=2))
        self.play(Write(ss3, run_time=2))


        # # Write the intermediate result for the unit place in the square
        intermediate_result_1 = Text("14", color=BLUE, font_size=33).move_to(ss3.get_center() + RIGHT * 0.12)
        self.play(Write(intermediate_result_1))
        self.wait(1)

        



        # # Define and display the fourth addition expression (s4)
        s4 = Text("12 + 7 = ", color=PINK, font_size=33).next_to(s3, DOWN * 3.5)
        ss4 = Square(side_length=0.8).next_to(s4, RIGHT)
        self.play(Write(s4, run_time=2))
        self.play(Write(ss4, run_time=2))

        # # Highlight unit's place digits 1 (in 21) and 0 (in 50)
        s4_unit_highlighted = Text("12 + 7 = ", t2c={'2': YELLOW, '+': PURE_GREEN, '7': YELLOW}, font_size=33).next_to(s3, DOWN * 3.5)
        self.play(Transform(s4, s4_unit_highlighted))
        self.wait(1)

        # # Write the intermediate result for the unit place in the square
        intermediate_result_1 = Text("9", color=BLUE, font_size=33).move_to(ss4.get_center() + RIGHT * 0.12)
        self.play(Write(intermediate_result_1))
        self.wait(1)

        # # Fade out the highlighted text and return to the original color
        s4_original = Text("12 + 7 = ", color=PINK, font_size=33).next_to(s3, DOWN * 3.5)
        self.play(Transform(s4, s4_original))
        self.wait(1)

        # # Highlight tens place digits 2 (in 21) and 5 (in 50)
        s4_tens_highlighted = Text("12 + 7 = ", t2c={'1': YELLOW}, font_size=33).next_to(s3, DOWN * 3.5)
        self.play(Transform(s4, s4_tens_highlighted))
        self.wait(1)

        # # Write the intermediate result for the tens place in the square, before the previous result
        intermediate_result_2 = Text("1", color=BLUE, font_size=33).move_to(ss4.get_center() + LEFT * 0.12)
        self.play(Write(intermediate_result_2))
        self.wait(1)

        # # Fade out the highlighted text and return to the original color
        self.play(Transform(s4, s4_original))
        self.wait(1)




        # # Define and display the third addition expression (s3)
        s5 = Text("9 + 5 = ", color=PINK, font_size=33).next_to(s4, DOWN * 3.5)
        ss5 = Square(side_length=0.8).next_to(s5, RIGHT)
        self.play(Write(s5, run_time=2))
        self.play(Write(ss5, run_time=2))


        # # Write the intermediate result for the unit place in the square
        intermediate_result_1 = Text("14", color=BLUE, font_size=33).move_to(ss5.get_center() + RIGHT * 0.12)
        self.play(Write(intermediate_result_1))
        self.wait(1)
        



        # # Define and display the second addition expression (s2)
        s6 = Text("17 + 2 = ", color=PINK, font_size=33).next_to(s1,  RIGHT * 20.5)
        ss6 = Square(side_length=0.8).next_to(s6, RIGHT)
        self.play(Write(s6, run_time=2))
        self.play(Write(ss6, run_time=2))

        # # Highlight unit's place digits 5 (in 75) and 4 (in 24)
        s6_unit_highlighted = Text("17 + 2 = ", t2c={'7': YELLOW, '+': PURE_GREEN, '2': YELLOW}, font_size=33).next_to(s1, RIGHT * 20.5)
        self.play(Transform(s6, s6_unit_highlighted))
        self.wait(1)

        # # Write the intermediate result for the unit place in the square
        intermediate_result_1 = Text("9", color=BLUE, font_size=33).move_to(ss6.get_center() + RIGHT * 0.12)
        self.play(Write(intermediate_result_1))
        self.wait(1)

        # # Fade out the highlighted text and return to the original color
        s6_original = Text("17 + 2 = ", color=PINK, font_size=33).next_to(s1, RIGHT * 20.5)
        self.play(Transform(s6, s6_original))
        self.wait(1)

        # # Highlight tens place digits 7 (in 75) and 2 (in 24)
        s6_tens_highlighted = Text("17 + 2 = ", t2c={'1': YELLOW}, font_size=33).next_to(s1, RIGHT * 20.5)
        self.play(Transform(s6, s6_tens_highlighted))
        self.wait(1)

        # # Write the intermediate result for the tens place in the square, before the previous result
        intermediate_result_2 = Text("1", color=BLUE, font_size=33).move_to(ss6.get_center() + LEFT * 0.12)
        self.play(Write(intermediate_result_2))
        self.wait(1)

        # # Fade out the highlighted text and return to the original color
        self.play(Transform(s6, s6_original))
        self.wait(1)





        # # Define and display the second addition expression (s2)
        s7 = Text("10 + 5 = ", color=PINK, font_size=33).next_to(s6, DOWN * 3.5)
        ss7 = Square(side_length=0.8).next_to(s7, RIGHT)
        self.play(Write(s7, run_time=2))
        self.play(Write(ss7, run_time=2))

        # # Highlight unit's place digits 5 (in 75) and 4 (in 24)
        s7_unit_highlighted = Text("10 + 5 = ", t2c={'0': YELLOW, '+': PURE_GREEN, '5': YELLOW}, font_size=33).next_to(s6, DOWN * 3.5)
        self.play(Transform(s7, s7_unit_highlighted))
        self.wait(1)

        # # Write the intermediate result for the unit place in the square
        intermediate_result_1 = Text("5", color=BLUE, font_size=33).move_to(ss7.get_center() + RIGHT * 0.12)
        self.play(Write(intermediate_result_1))
        self.wait(1)

        # # Fade out the highlighted text and return to the original color
        s7_original = Text("10 + 5 = ", color=PINK, font_size=33).next_to(s6, DOWN * 3.5)
        self.play(Transform(s7, s7_original))
        self.wait(1)

        # # Highlight tens place digits 7 (in 75) and 2 (in 24)
        s7_tens_highlighted = Text("10 + 5 = ", t2c={'1': YELLOW}, font_size=33).next_to(s6, DOWN * 3.5)
        self.play(Transform(s7, s7_tens_highlighted))
        self.wait(1)

        # # Write the intermediate result for the tens place in the square, before the previous result
        intermediate_result_2 = Text("1", color=BLUE, font_size=33).move_to(ss7.get_center() + LEFT * 0.12)
        self.play(Write(intermediate_result_2))
        self.wait(1)

        # # Fade out the highlighted text and return to the original color
        self.play(Transform(s7, s7_original))
        self.wait(1)




        # # Define and display the second addition expression (s2)
        s8 = Text("13 + 3 = ", color=PINK, font_size=33).next_to(s7, DOWN * 3.5)
        ss8 = Square(side_length=0.8).next_to(s8, RIGHT)
        self.play(Write(s8, run_time=2))
        self.play(Write(ss8, run_time=2))

        # # Highlight unit's place digits 5 (in 75) and 4 (in 24)
        s8_unit_highlighted = Text("13 + 3 = ", t2c={'3': YELLOW, '+': PURE_GREEN, '3': YELLOW}, font_size=33).next_to(s7, DOWN * 3.5)
        self.play(Transform(s8, s8_unit_highlighted))
        self.wait(1)

        # # Write the intermediate result for the unit place in the square
        intermediate_result_1 = Text("6", color=BLUE, font_size=33).move_to(ss8.get_center() + RIGHT * 0.12)
        self.play(Write(intermediate_result_1))
        self.wait(1)

        # # Fade out the highlighted text and return to the original color
        s8_original = Text("13 + 3 = ", color=PINK, font_size=33).next_to(s7, DOWN * 3.5)
        self.play(Transform(s8, s8_original))
        self.wait(1)

        # # Highlight tens place digits 7 (in 75) and 2 (in 24)
        s8_tens_highlighted = Text("13 + 3 = ", t2c={'1': YELLOW}, font_size=33).next_to(s7, DOWN * 3.5)
        self.play(Transform(s8, s8_tens_highlighted))
        self.wait(1)

        # # Write the intermediate result for the tens place in the square, before the previous result
        intermediate_result_2 = Text("1", color=BLUE, font_size=33).move_to(ss8.get_center() + LEFT * 0.12)
        self.play(Write(intermediate_result_2))
        self.wait(1)

        # # Fade out the highlighted text and return to the original color
        self.play(Transform(s8, s8_original))
        self.wait(1)




        # # Define and display the third addition expression (s3)
        s9 = Text("9 + 6 = ", color=PINK, font_size=33).next_to(s8, DOWN * 3.5)
        ss9 = Square(side_length=0.8).next_to(s9, RIGHT)
        self.play(Write(s9, run_time=2))
        self.play(Write(ss9, run_time=2))


        # # Write the intermediate result for the unit place in the square
        intermediate_result_1 = Text("15", color=BLUE, font_size=33).move_to(ss9.get_center() + RIGHT * 0.12)
        self.play(Write(intermediate_result_1))
        self.wait(1)




        # # Define and display the third addition expression (s3)
        s10 = Text("8 + 1 = ", color=PINK, font_size=33).next_to(s9, DOWN * 3.5)
        ss10 = Square(side_length=0.8).next_to(s10, RIGHT)
        self.play(Write(s10, run_time=2))
        self.play(Write(ss10, run_time=2))


        # # Write the intermediate result for the unit place in the square
        intermediate_result_1 = Text("9", color=BLUE, font_size=33).move_to(ss10.get_center() + RIGHT * 0.12)
        self.play(Write(intermediate_result_1))
        self.wait(1)
    

    def add2(self):
        # Title
        title = Tex("Solving the following additions:", color=PURPLE).to_edge(UP*1.5 + LEFT*1)
        self.play(Write(title))

        # Addition 15 + 3 = 18
        addition1 = self.vertical_addition("15", "3", "18")
        addition1.move_to([-1, 0.5, 0])

        # Animate the creation of each part sequentially
        self.play(Write(addition1[0]))  # Top number
        self.wait(0.5)
        self.play(Write(addition1[1]))  # Bottom number
        self.wait(0.5)
        self.play(Write(addition1[5]))  # Plus symbol
        self.wait(0.5)
        self.play(Write(addition1[2]))  # First underline
        self.wait(0.5)
        self.play(Write(addition1[4]))  # Second underline
        self.wait(0.5)

        # Create the title text
        title_1 = Text("Calculations:", font_size=31, color=DARK_BROWN).to_edge(UP*5 + RIGHT*3.25)
        
        # Create an underline for the word "Calculations"
        underline = Line(start=title_1.get_left() + LEFT*0.4, end=title_1.get_left() + RIGHT*1.79, color=GOLD, stroke_width=2)
        underline.next_to(title_1, DOWN, buff=0.1)       
    
        sub_title1 = Text("5 + 3 = 8", font_size=32, color=YELLOW).to_edge(UP*6.65 + RIGHT*4)
        sub_title2 = Text("1 + 0 = 1", font_size=32, color=YELLOW).to_edge(UP*6.65 + RIGHT*4)        

        # Split the result into tens and units
        result_tens = Tex("1", color=BLUE).scale(1.1)
        result_units = Tex("8", color=BLUE).scale(1.1)
        result_units.next_to(addition1[2], DOWN).shift(RIGHT * 0.2)
        result_tens.next_to(result_units, LEFT*0.4)        
      
        # Add the title and underline to the scene
        self.add(title_1, underline)
        self.wait(0.3)
        self.play(Write(sub_title1))
        self.wait(0.5)
        self.play(FadeOut(sub_title1))
        self.wait(0.5)
        self.play(Write(result_units))  # Write the units place first
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(0.5)
        self.play(FadeOut(sub_title2))
        self.wait(0.5)
        self.play(Write(result_tens))  # Write the tens place
        self.wait(1)

        # Fade out all elements
        self.play(
            FadeOut(title_1), 
            FadeOut(underline), 
            FadeOut(addition1[5]), 
            FadeOut(addition1[4]), 
            FadeOut(addition1[2]), 
            FadeOut(addition1[1]), 
            FadeOut(addition1[0]), 
            FadeOut(result_units), 
            FadeOut(result_tens)
        )


        # Addition 12 + 3 = 15
        addition1 = self.vertical_addition("12", "3", "15")
        addition1.move_to([-1, 0.5, 0])

        # Animate the creation of each part sequentially
        self.play(Write(addition1[0]))  # Top number
        self.wait(0.5)
        self.play(Write(addition1[1]))  # Bottom number
        self.wait(0.5)
        self.play(Write(addition1[5]))  # Plus symbol
        self.wait(0.5)
        self.play(Write(addition1[2]))  # First underline
        self.wait(0.5)
        self.play(Write(addition1[4]))  # Second underline
        self.wait(0.5)

        # Create the title text
        title_1 = Text("Calculations:", font_size=31, color=DARK_BROWN).to_edge(UP*5 + RIGHT*3.25)
        
        # Create an underline for the word "Calculations"
        underline = Line(start=title_1.get_left() + LEFT*0.4, end=title_1.get_left() + RIGHT*1.79, color=GOLD, stroke_width=2)
        underline.next_to(title_1, DOWN, buff=0.1)       
    
        sub_title1 = Text("2 + 3 = 5", font_size=32, color=YELLOW).to_edge(UP*6.65 + RIGHT*4)
        sub_title2 = Text("1 + 0 = 1", font_size=32, color=YELLOW).to_edge(UP*6.65 + RIGHT*4)        

        # Split the result into tens and units
        result_tens = Tex("1", color=BLUE).scale(1.1)
        result_units = Tex("5", color=BLUE).scale(1.1)
        result_units.next_to(addition1[2], DOWN).shift(RIGHT * 0.2)
        result_tens.next_to(result_units, LEFT*0.4)        
      
        # Add the title and underline to the scene
        self.add(title_1, underline)
        self.wait(0.3)
        self.play(Write(sub_title1))
        self.wait(0.5)
        self.play(FadeOut(sub_title1))
        self.wait(0.5)
        self.play(Write(result_units))  # Write the units place first
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(0.5)
        self.play(FadeOut(sub_title2))
        self.wait(0.5)
        self.play(Write(result_tens))  # Write the tens place
        self.wait(1)

        # Fade out all elements
        self.play(
            FadeOut(title_1), 
            FadeOut(underline), 
            FadeOut(addition1[5]), 
            FadeOut(addition1[4]), 
            FadeOut(addition1[2]), 
            FadeOut(addition1[1]), 
            FadeOut(addition1[0]), 
            FadeOut(result_units), 
            FadeOut(result_tens)
        )


        # Addition 14 + 5 = 19
        addition1 = self.vertical_addition("14", "5", "19")
        addition1.move_to([-1, 0.5, 0])

        # Animate the creation of each part sequentially
        self.play(Write(addition1[0]))  # Top number
        self.wait(0.5)
        self.play(Write(addition1[1]))  # Bottom number
        self.wait(0.5)
        self.play(Write(addition1[5]))  # Plus symbol
        self.wait(0.5)
        self.play(Write(addition1[2]))  # First underline
        self.wait(0.5)
        self.play(Write(addition1[4]))  # Second underline
        self.wait(0.5)

        # Create the title text
        title_1 = Text("Calculations:", font_size=31, color=DARK_BROWN).to_edge(UP*5 + RIGHT*3.25)
        
        # Create an underline for the word "Calculations"
        underline = Line(start=title_1.get_left() + LEFT*0.4, end=title_1.get_left() + RIGHT*1.79, color=GOLD, stroke_width=2)
        underline.next_to(title_1, DOWN, buff=0.1)       
    
        sub_title1 = Text("4 + 5 = 9", font_size=32, color=YELLOW).to_edge(UP*6.65 + RIGHT*4)
        sub_title2 = Text("1 + 0 = 1", font_size=32, color=YELLOW).to_edge(UP*6.65 + RIGHT*4)        

        # Split the result into tens and units
        result_tens = Tex("1", color=BLUE).scale(1.1)
        result_units = Tex("9", color=BLUE).scale(1.1)
        result_units.next_to(addition1[2], DOWN).shift(RIGHT * 0.2)
        result_tens.next_to(result_units, LEFT*0.4)        
      
        # Add the title and underline to the scene
        self.add(title_1, underline)
        self.wait(0.3)
        self.play(Write(sub_title1))
        self.wait(0.5)
        self.play(FadeOut(sub_title1))
        self.wait(0.5)
        self.play(Write(result_units))  # Write the units place first
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(0.5)
        self.play(FadeOut(sub_title2))
        self.wait(0.5)
        self.play(Write(result_tens))  # Write the tens place
        self.wait(1)

        # Fade out all elements
        self.play(
            FadeOut(title_1), 
            FadeOut(underline), 
            FadeOut(addition1[5]), 
            FadeOut(addition1[4]), 
            FadeOut(addition1[2]), 
            FadeOut(addition1[1]), 
            FadeOut(addition1[0]), 
            FadeOut(result_units), 
            FadeOut(result_tens)
        )

        # Addition 12 + 5 = 17
        addition1 = self.vertical_addition("12", "5", "17")
        addition1.move_to([-1, 0.5, 0])

        # Animate the creation of each part sequentially
        self.play(Write(addition1[0]))  # Top number
        self.wait(0.5)
        self.play(Write(addition1[1]))  # Bottom number
        self.wait(0.5)
        self.play(Write(addition1[5]))  # Plus symbol
        self.wait(0.5)
        self.play(Write(addition1[2]))  # First underline
        self.wait(0.5)
        self.play(Write(addition1[4]))  # Second underline
        self.wait(0.5)

        # Create the title text
        title_1 = Text("Calculations:", font_size=31, color=DARK_BROWN).to_edge(UP*5 + RIGHT*3.25)
        
        # Create an underline for the word "Calculations"
        underline = Line(start=title_1.get_left() + LEFT*0.4, end=title_1.get_left() + RIGHT*1.79, color=GOLD, stroke_width=2)
        underline.next_to(title_1, DOWN, buff=0.1)       
    
        sub_title1 = Text("2 + 5 = 7", font_size=32, color=YELLOW).to_edge(UP*6.65 + RIGHT*4)
        sub_title2 = Text("1 + 0 = 1", font_size=32, color=YELLOW).to_edge(UP*6.65 + RIGHT*4)        

        # Split the result into tens and units
        result_tens = Tex("1", color=BLUE).scale(1.1)
        result_units = Tex("7", color=BLUE).scale(1.1)
        result_units.next_to(addition1[2], DOWN).shift(RIGHT * 0.2)
        result_tens.next_to(result_units, LEFT*0.4)        
      
        # Add the title and underline to the scene
        self.add(title_1, underline)
        self.wait(0.3)
        self.play(Write(sub_title1))
        self.wait(0.5)
        self.play(FadeOut(sub_title1))
        self.wait(0.5)
        self.play(Write(result_units))  # Write the units place first
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(0.5)
        self.play(FadeOut(sub_title2))
        self.wait(0.5)
        self.play(Write(result_tens))  # Write the tens place
        self.wait(1)

        # Fade out all elements
        self.play(
            FadeOut(title_1), 
            FadeOut(underline), 
            FadeOut(addition1[5]), 
            FadeOut(addition1[4]), 
            FadeOut(addition1[2]), 
            FadeOut(addition1[1]), 
            FadeOut(addition1[0]), 
            FadeOut(result_units), 
            FadeOut(result_tens)
        )

        
    def vertical_addition(self, top_number, bottom_number, result):
        numbers = VGroup(
            Tex(top_number).scale(1.1),
            Tex(bottom_number).scale(1.1),
            Tex("\\underline{\\phantom{0000}}").scale(2),
            Tex(result).scale(1.1),
            Tex("\\underline{\\phantom{0000}}").scale(2),
            Tex("+").scale(1.1)
        ).arrange(DOWN, buff=0.2)

        numbers.move_to(ORIGIN)

        numbers[1].next_to(numbers[0], DOWN).shift(RIGHT * 0.15) 
        numbers[5].next_to(numbers[1], LEFT*1.4)

        return numbers
    
    
    def SetDeveloperList(self):  
        self.DeveloperList="Akshitha"

        
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="additionofnumbers.py"

        

# To run the scene
if __name__ == "__main__":
    scene = additionofnumbers()
    scene.render()