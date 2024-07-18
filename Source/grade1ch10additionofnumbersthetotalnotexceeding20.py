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
        t1 = Text("Addition of Numbers not Exceeding 20", font_size=35)
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
        
        # Define and display the subtractions
        s1 = Text("14 + 3 = ", color=PINK, font_size=30).to_edge(LEFT * 4.5 + UP * 3.5)
        ss1 = Square(side_length=0.7).next_to(s1, RIGHT)
        s12 = Text("17", color=BLUE, font_size=30).move_to(ss1.get_center())
        self.play(Write(s1, run_time=3))
        self.play(Write(ss1, run_time=2))
        self.play(Write(s12))
        
        s2 = Text("13 + 5 = ", color=PINK, font_size=30).next_to(s1, DOWN * 3)
        ss2 = Square(side_length=0.7).next_to(s2, RIGHT)
        s22 = Text("18", color=BLUE, font_size=30).move_to(ss2.get_center())
        self.play(Write(s2, run_time=3))
        self.play(Write(ss2, run_time=2))
        self.play(Write(s22))

        s3 = Text("8 + 6 = ", color=PINK, font_size=30).next_to(s2, DOWN * 3)
        ss3 = Square(side_length=0.7).next_to(s3, RIGHT)
        s32 = Text("14", color=BLUE, font_size=30).move_to(ss3.get_center())
        self.play(Write(s3, run_time=3))
        self.play(Write(ss3, run_time=2))
        self.play(Write(s32))

        s4 = Text("12 + 7 = ", color=PINK, font_size=30).next_to(s3, DOWN * 3)
        ss4 = Square(side_length=0.7).next_to(s4, RIGHT)
        s42 = Text("19", color=BLUE, font_size=30).move_to(ss4.get_center())
        self.play(Write(s4, run_time=3))
        self.play(Write(ss4, run_time=2))
        self.play(Write(s42))
        
        s5 = Text("9 + 5 = ", color=PINK, font_size=30).next_to(s4, DOWN * 3)
        ss5 = Square(side_length=0.7).next_to(s5, RIGHT)
        s52 = Text("14", color=BLUE, font_size=30).move_to(ss5.get_center())
        self.play(Write(s5, run_time=3))
        self.play(Write(ss5, run_time=2))
        self.play(Write(s52))

        s7 = Text("11 + 8 = ", color=PINK, font_size=30).next_to(s1, RIGHT * 20.5)
        ss7 = Square(side_length=0.7).next_to(s7, RIGHT)
        s72 = Text("19", color=BLUE, font_size=30).move_to(ss7.get_center())
        self.play(Write(s7, run_time=3))
        self.play(Write(ss7, run_time=2))
        self.play(Write(s72))
        
        s8 = Text("10 + 5 = ", color=PINK, font_size=30).next_to(s7, DOWN * 3)
        ss8 = Square(side_length=0.7).next_to(s8, RIGHT)
        s82 = Text("15", color=BLUE, font_size=30).move_to(ss8.get_center())
        self.play(Write(s8, run_time=3))
        self.play(Write(ss8, run_time=2))
        self.play(Write(s82))
        
        s9 = Text("5 + 2 = ", color=PINK, font_size=30).next_to(s8, DOWN * 3)
        ss9 = Square(side_length=0.7).next_to(s9, RIGHT)
        s92 = Text("7", color=BLUE, font_size=30).move_to(ss9.get_center())
        self.play(Write(s9, run_time=3))
        self.play(Write(ss9, run_time=2))
        self.play(Write(s92))

        s10 = Text("8 + 1 = ", color=PINK, font_size=30).next_to(s9, DOWN * 3)
        ss10 = Square(side_length=0.7).next_to(s10, RIGHT)
        s102 = Text("9", color=BLUE, font_size=30).move_to(ss10.get_center())
        self.play(Write(s10, run_time=3))
        self.play(Write(ss10, run_time=2))
        self.play(Write(s102))

        s11 = Text("9 + 6 = ", color=PINK, font_size=30).next_to(s10, DOWN * 3)
        ss11 = Square(side_length=0.7).next_to(s11, RIGHT)
        s112 = Text("15", color=BLUE, font_size=30).move_to(ss11.get_center())
        self.play(Write(s11, run_time=3))
        self.play(Write(ss11, run_time=2))
        self.play(Write(s112))

         # Fade out all elements
        self.play(
            FadeOut(s1), FadeOut(ss1), FadeOut(s12),
            FadeOut(s2), FadeOut(ss2), FadeOut(s22),
            FadeOut(s3), FadeOut(ss3), FadeOut(s32),
            FadeOut(s4), FadeOut(ss4), FadeOut(s42),
            FadeOut(s5), FadeOut(ss5), FadeOut(s52),
            FadeOut(s7), FadeOut(ss7), FadeOut(s72),
            FadeOut(s8), FadeOut(ss8), FadeOut(s82),
            FadeOut(s9), FadeOut(ss9), FadeOut(s92),
            FadeOut(s10), FadeOut(ss10), FadeOut(s102),
            FadeOut(s11), FadeOut(ss11), FadeOut(s112),
            FadeOut(t1)
        )
    

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