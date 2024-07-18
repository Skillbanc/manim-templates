from manim import *
from AbstractAnim import AbstractAnim
import cvo


class AdditionofNumbers(AbstractAnim):
    def construct(self):
        # self.RenderSkillbancLogo()
        # self.fadeOutCurrentScene()
        # self.Extra_text()
        # self.fadeOutCurrentScene()
        self.addition()
        # self.fadeOutCurrentScene()
        # self.vertical_addition_exercise_1()
        # self.fadeOutCurrentScene()
        # self.horizontal_additionExercise()
        # self.fadeOutCurrentScene()
        # self.GithubSourceCodeReference()


    def Extra_text(self):
        title = Text("Chapter 5 : Addition of Numbers", font_size=44)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))


    def addition(self):

        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        # p1=cvo.CVO().CreateCVO("cname","oname")
        self.angleChoice = [TAU/4,TAU/4,TAU/4]
        self.isRandom=False
        
        p1=cvo.CVO().CreateCVO("Addition","").setPosition([-4.5,1,0])
        p2=cvo.CVO().CreateCVO("definition","Addition is the process of combining numbers to find their total.").setPosition([1.5,2,0])
        p3=cvo.CVO().CreateCVO("Symbol","+").setPosition([3.5,0,0])
        p4=cvo.CVO().CreateCVO("Example","35+15=50").setPosition([-2,-2.5,0])
        p1.cvolist.append(p2)
        p1.cvolist.append(p2)
        p1.cvolist.append(p3)

        p1.setcircleradius(1.25)
        self.construct1(p1,p1)


    





    def vertical_addition_exercise_1(self):
        # Title
        title = Tex("Solving the following additions:", color=PURPLE).to_edge(UP*1.5+LEFT*1)
        self.play(Write(title))
        
        # Addition 52 + 21 = 73
        addition1 = self.vertical_addition("52", "21", "73")
        addition1.move_to([-5.5, 1, 0])

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
        title = Text("Calculations:", font_size=31, color=DARK_BROWN).to_edge(UP*5 + RIGHT*3.25)
        
        # Create an underline for the word "Calculations"
        underline = Line(start=title.get_left() + LEFT*0.4, end=title.get_left() + RIGHT*1.79, color=GOLD, stroke_width=2)
        underline.next_to(title, DOWN, buff=0.1)
        
    
        sub_title1 = Text("2 + 1 = 3",font_size=32,color=YELLOW).to_edge(UP*6.65+RIGHT*4)
        sub_title2 = Text("5 + 2 = 7",font_size=32,color=YELLOW).to_edge(UP*8.3+RIGHT*4)

        # Split the result into tens and units
        result_tens = Tex("7",color=BLUE).scale(1.1)
        result_units = Tex("3",color=BLUE).scale(1.1)
        result_units.next_to(addition1[2], DOWN).shift(RIGHT * 0.2)
        result_tens.next_to(result_units, LEFT*0.4)
        
        # Add the title and underline to the scene
        self.add(title, underline)
        self.wait(0.3)
        self.play(Write(sub_title1))
        self.wait(0.5)
        self.play(Write(result_units))  # Write the units place first
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(0.5)
        self.play(Write(result_tens))  # Write the tens place
        self.wait(1)

        self.play(FadeOut(sub_title1), FadeOut(sub_title2), FadeOut(title), FadeOut(underline))

        



        # Addition 24 + 22 = 46
        addition2 = self.vertical_addition("24", "22", "46")
        addition2.move_to([-2.5, 1, 0])

        # Animate the creation of addition2
        self.play(Write(addition2[0]))  # Top number
        self.wait(0.5)
        self.play(Write(addition2[1]))  # Bottom number
        self.wait(0.5)
        self.play(Write(addition2[5]))  # Plus symbol
        self.wait(0.5)
        self.play(Write(addition2[2]))  # First underline
        self.wait(0.5)
        self.play(Write(addition2[4]))  # Second underline
        self.wait(0.5)

        # Create the title text
        title = Text("Calculations:", font_size=31, color=DARK_BROWN).to_edge(UP*5 + RIGHT*3.25)
        
        # Create an underline for the word "Calculations"
        underline = Line(start=title.get_left() + LEFT*0.4, end=title.get_left() + RIGHT*1.79, color=GOLD, stroke_width=2)
        underline.next_to(title, DOWN, buff=0.1)

        sub_title3 = Text("4 + 2 = 6",font_size=32,color=YELLOW).to_edge(UP*6.65+RIGHT*4)
        sub_title4 = Text("2 + 2 = 4",font_size=32,color=YELLOW).to_edge(UP*8.3+RIGHT*4)


        # Split the result of addition2 into tens and units
        result_tens_2 = Tex("4",color=BLUE).scale(1.1)
        result_units_2 = Tex("6",color=BLUE).scale(1.1)
        result_units_2.next_to(addition2[2], DOWN).shift(RIGHT * 0.2)
        result_tens_2.next_to(result_units_2, LEFT*0.4)
        
        self.add(title, underline)
        self.wait(0.3)
        self.play(Write(sub_title3))
        self.wait(0.5)
        self.play(Write(result_units_2))  # Write the units place first
        self.wait(1)
        self.play(Write(sub_title4))
        self.wait(0.5)
        self.play(Write(result_tens_2))  # Write the tens place
        self.wait(1)

        self.play(FadeOut(sub_title3), FadeOut(sub_title4), FadeOut(title), FadeOut(underline))




        


        # Addition 33 + 45 = 78
        addition3 = self.vertical_addition("33", "45", "78")
        addition3.move_to([0.5, 1, 0])

        # Animate addition3
        self.play(Write(addition3[0]))  # Top number
        self.wait(0.5)
        self.play(Write(addition3[1]))  # Bottom number
        self.wait(0.5)
        self.play(Write(addition3[5]))  # Plus symbol
        self.wait(0.5)
        self.play(Write(addition3[2]))  # First underline
        self.wait(0.5)
        self.play(Write(addition3[4]))  # Second underline
        self.wait(0.5)


        # Create the title text
        title = Text("Calculations:", font_size=31, color=DARK_BROWN).to_edge(UP*5 + RIGHT*3.25)
        
        # Create an underline for the word "Calculations"
        underline = Line(start=title.get_left() + LEFT*0.4, end=title.get_left() + RIGHT*1.79, color=GOLD, stroke_width=2)
        underline.next_to(title, DOWN, buff=0.1)


        sub_title5 = Text("3 + 5 = 8",font_size=32,color=YELLOW).to_edge(UP*6.65+RIGHT*4)
        sub_title6 = Text("3 + 4 = 7",font_size=32,color=YELLOW).to_edge(UP*8.3+RIGHT*4)

        # Split the result of addition3 into tens and units
        result_tens_3 = Tex("7",color=BLUE).scale(1.1)
        result_units_3 = Tex("8",color=BLUE).scale(1.1)
        result_units_3.next_to(addition3[2], DOWN).shift(RIGHT * 0.2)
        result_tens_3.next_to(result_units_3, LEFT*0.4)
        
        self.add(title, underline)
        self.wait(0.5)
        self.play(Write(sub_title5))
        self.wait(0.5)
        self.play(Write(result_units_3))  # Write the units place first
        self.wait(1)
        self.play(Write(sub_title6))
        self.wait(0.5)
        self.play(Write(result_tens_3))  # Write the tens place
        self.wait(1)

        self.play(FadeOut(sub_title5), FadeOut(sub_title6), FadeOut(title), FadeOut(underline))


        

        # Addition 12 + 53 = 65
        addition4 = self.vertical_addition("12", "53", "65")
        addition4.move_to([-5.5, -2, 0])

        # Animate addition4
        self.play(Write(addition4[0]))  # Top number
        self.wait(0.5)
        self.play(Write(addition4[1]))  # Bottom number
        self.wait(0.5)
        self.play(Write(addition4[5]))  # Plus symbol
        self.wait(0.5)
        self.play(Write(addition4[2]))  # First underline
        self.wait(0.5)
        self.play(Write(addition4[4]))  # Second underline
        self.wait(0.5)

        # Create the title text
        title = Text("Calculations:", font_size=31, color=DARK_BROWN).to_edge(UP*5 + RIGHT*3.25)
        
        # Create an underline for the word "Calculations"
        underline = Line(start=title.get_left() + LEFT*0.4, end=title.get_left() + RIGHT*1.79, color=GOLD, stroke_width=2)
        underline.next_to(title, DOWN, buff=0.1)

        sub_title7 = Text("2 + 3 = 5",font_size=32,color=YELLOW).to_edge(UP*6.65+RIGHT*4)
        sub_title8 = Text("1 + 5 = 6",font_size=32,color=YELLOW).to_edge(UP*8.3+RIGHT*4)

        # Split the result of addition4 into tens and units
        result_tens_4 = Tex("6",color=BLUE).scale(1.1)
        result_units_4 = Tex("5",color=BLUE).scale(1.1)
        result_units_4.next_to(addition4[2], DOWN).shift(RIGHT * 0.2)
        result_tens_4.next_to(result_units_4, LEFT*0.4)
        
        self.add(title, underline)
        self.wait(0.5)
        self.play(Write(sub_title7))
        self.wait(0.5)
        self.play(Write(result_units_4))  # Write the units place first
        self.wait(1)
        self.play(Write(sub_title8))
        self.wait(0.5)
        self.play(Write(result_tens_4))  # Write the tens place
        self.wait(1)

        self.play(FadeOut(sub_title7), FadeOut(sub_title8), FadeOut(title), FadeOut(underline))



        # Addition 66 + 23 = 89
        addition5 = self.vertical_addition("66", "23", "89")
        addition5.move_to([-2.5, -2, 0])

        # Animate addition5
        self.play(Write(addition5[0]))  # Top number
        self.wait(0.5)
        self.play(Write(addition5[1]))  # Bottom number
        self.wait(0.5)
        self.play(Write(addition5[5]))  # Plus symbol
        self.wait(0.5)
        self.play(Write(addition5[2]))  # First underline
        self.wait(0.5)
        self.play(Write(addition5[4]))  # Second underline
        self.wait(0.5)

        # Create the title text
        title = Text("Calculations:", font_size=31, color=DARK_BROWN).to_edge(UP*5 + RIGHT*3.25)
        
        # Create an underline for the word "Calculations"
        underline = Line(start=title.get_left() + LEFT*0.4, end=title.get_left() + RIGHT*1.79, color=GOLD, stroke_width=2)
        underline.next_to(title, DOWN, buff=0.1)

        sub_title9 = Text("6 + 3 = 9",font_size=32,color=YELLOW).to_edge(UP*6.65+RIGHT*4)
        sub_title10 = Text("6 + 2 = 8",font_size=32,color=YELLOW).to_edge(UP*8.3+RIGHT*4)

        # Split the result of addition5 into tens and units
        result_tens_5 = Tex("8",color=BLUE).scale(1.1)
        result_units_5 = Tex("9",color=BLUE).scale(1.1)
        result_units_5.next_to(addition5[2], DOWN).shift(RIGHT * 0.2)
        result_tens_5.next_to(result_units_5, LEFT*0.4)
        
        self.add(title, underline)
        self.wait(0.5)
        self.play(Write(sub_title9))
        self.wait(0.5)
        self.play(Write(result_units_5))  # Write the units place first
        self.wait(1)
        self.play(Write(sub_title10))
        self.wait(0.5)
        self.play(Write(result_tens_5))  # Write the tens place
        self.wait(1)

        self.play(FadeOut(sub_title9), FadeOut(sub_title10), FadeOut(title), FadeOut(underline))





        # Addition 34 + 43 = 77
        addition6 = self.vertical_addition("34", "43", "77")
        addition6.move_to([0.5, -2, 0])

        # Animate addition6
        self.play(Write(addition6[0]))  # Top number
        self.wait(0.5)
        self.play(Write(addition6[1]))  # Bottom number
        self.wait(0.5)
        self.play(Write(addition6[5]))  # Plus symbol
        self.wait(0.5)
        self.play(Write(addition6[2]))  # First underline
        self.wait(0.5)
        self.play(Write(addition6[4]))  # Second underline
        self.wait(0.5)

        # Create the title text
        title = Text("Calculations:", font_size=31, color=DARK_BROWN).to_edge(UP*5 + RIGHT*3.25)
        
        # Create an underline for the word "Calculations"
        underline = Line(start=title.get_left() + LEFT*0.4, end=title.get_left() + RIGHT*1.79, color=GOLD, stroke_width=2)
        underline.next_to(title, DOWN, buff=0.1)
        

        sub_title11 = Text("4 + 3 = 7",font_size=32,color=YELLOW).to_edge(UP*6.65+RIGHT*4)
        sub_title12 = Text("3 + 4 = 7",font_size=32,color=YELLOW).to_edge(UP*8.3+RIGHT*4)

        # Split the result of addition6 into tens and units
        result_tens_6 = Tex("7",color=BLUE).scale(1.1)
        result_units_6 = Tex("7",color=BLUE).scale(1.1)
        result_units_6.next_to(addition6[2], DOWN).shift(RIGHT * 0.2)
        result_tens_6.next_to(result_units_6, LEFT*0.4)
        

        self.add(title, underline)
        self.wait(0.5)
        self.play(Write(sub_title11))
        self.wait(0.5)
        self.play(Write(result_units_6))  # Write the units place first
        self.wait(1)
        self.play(Write(sub_title12))
        self.wait(0.5)
        self.play(Write(result_tens_6))  # Write the tens place
        self.wait(1)

        self.play(FadeOut(sub_title11), FadeOut(sub_title12), FadeOut(title), FadeOut(underline))


        
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

        numbers[1].next_to(numbers[0], DOWN)
        numbers[5].next_to(numbers[1], LEFT)

        return numbers





    def horizontal_additionExercise(self):
        # Create and display the initial text
        t1 = Text("Add the numbers given. Write your answer in the box", font_size=35).to_edge(UP + LEFT * 1)
        self.play(Write(t1))
        

        # Define and display the first addition expression (s1)
        s1 = Text("23 + 14 = ", color=PINK, font_size=33).to_edge(LEFT * 3.5 + UP * 3.5)
        ss1 = Square(side_length=0.8).next_to(s1, RIGHT)
        self.play(Write(s1, run_time=2))
        self.play(Write(ss1, run_time=2))

        # Highlight unit's place digits 3 (in 23) and 4 (in 14)
        s1_unit_highlighted = Text("23 + 14 = ", t2c={'3': YELLOW, '+': PURE_GREEN, '4': YELLOW}, font_size=33).to_edge(LEFT * 3.5 + UP * 3.5)
        self.play(Transform(s1, s1_unit_highlighted))
        self.wait(1)

        # Write the intermediate result for the unit place in the square
        intermediate_result_1 = Text("7", color=BLUE, font_size=33).move_to(ss1.get_center() + RIGHT * 0.12)
        self.play(Write(intermediate_result_1))
        self.wait(1)

        # Fade out the highlighted text and return to the original color
        s1_original = Text("23 + 14 = ", color=PINK, font_size=33).to_edge(LEFT * 3.5 + UP * 3.5)
        self.play(Transform(s1, s1_original))
        self.wait(1)

        # Highlight tens place digits 2 (in 23) and 1 (in 14)
        s1_tens_highlighted = Text("23 + 14 = ", t2c={'2': YELLOW, '+': PURE_GREEN, '1': YELLOW}, font_size=33).to_edge(LEFT * 3.5 + UP * 3.5)
        self.play(Transform(s1, s1_tens_highlighted))
        self.wait(1)

        # Write the intermediate result for the tens place in the square, before the previous result
        intermediate_result_2 = Text("3", color=BLUE, font_size=33).move_to(ss1.get_center() + LEFT * 0.12)
        self.play(Write(intermediate_result_2))
        self.wait(1)

        # Fade out the highlighted text and return to the original color
        self.play(Transform(s1, s1_original))
        self.wait(1)

        # Remove intermediate digits
        self.play(FadeOut(intermediate_result_2), FadeOut(intermediate_result_1))

        # Final result
        s12 = Text("37", color=BLUE, font_size=33).move_to(ss1.get_center())
        self.play(Write(s12))
        self.wait(1)






        # Define and display the second addition expression (s2)
        s2 = Text("75 + 24 = ", color=PINK, font_size=33).next_to(s1, DOWN * 3.5)
        ss2 = Square(side_length=0.8).next_to(s2, RIGHT)
        self.play(Write(s2, run_time=2))
        self.play(Write(ss2, run_time=2))

        # Highlight unit's place digits 5 (in 75) and 4 (in 24)
        s2_unit_highlighted = Text("75 + 24 = ", t2c={'5': YELLOW, '+': PURE_GREEN, '4': YELLOW}, font_size=33).next_to(s1, DOWN * 3.5)
        self.play(Transform(s2, s2_unit_highlighted))
        self.wait(1)

        # Write the intermediate result for the unit place in the square
        intermediate_result_1 = Text("9", color=BLUE, font_size=33).move_to(ss2.get_center() + RIGHT * 0.12)
        self.play(Write(intermediate_result_1))
        self.wait(1)

        # Fade out the highlighted text and return to the original color
        s2_original = Text("75 + 24 = ", color=PINK, font_size=33).next_to(s1, DOWN * 3.5)
        self.play(Transform(s2, s2_original))
        self.wait(1)

        # Highlight tens place digits 7 (in 75) and 2 (in 24)
        s2_tens_highlighted = Text("75 + 24 = ", t2c={'7': YELLOW, '+': PURE_GREEN, '2': YELLOW}, font_size=33).next_to(s1, DOWN * 3.5)
        self.play(Transform(s2, s2_tens_highlighted))
        self.wait(1)

        # Write the intermediate result for the tens place in the square, before the previous result
        intermediate_result_2 = Text("9", color=BLUE, font_size=33).move_to(ss2.get_center() + LEFT * 0.12)
        self.play(Write(intermediate_result_2))
        self.wait(1)

        # Fade out the highlighted text and return to the original color
        self.play(Transform(s2, s2_original))
        self.wait(1)

        # Remove intermediate digits
        self.play(FadeOut(intermediate_result_2), FadeOut(intermediate_result_1))

        # Final result
        s22 = Text("99", color=BLUE, font_size=33).move_to(ss2.get_center())
        self.play(Write(s22))
        self.wait(1)





        # Define and display the third addition expression (s3)
        s3 = Text("63 + 23 = ", color=PINK, font_size=33).next_to(s2, DOWN * 3.5)
        ss3 = Square(side_length=0.8).next_to(s3, RIGHT)
        self.play(Write(s3, run_time=2))
        self.play(Write(ss3, run_time=2))

        # Highlight unit's place digits 3 (in 63) and 3 (in 23)
        s3_unit_highlighted = Text("63 + 23 = ", t2c={'3': YELLOW, '+': PURE_GREEN, '3': YELLOW}, font_size=33).next_to(s2, DOWN * 3.5)
        self.play(Transform(s3, s3_unit_highlighted))
        self.wait(1)

        # Write the intermediate result for the unit place in the square
        intermediate_result_1 = Text("6", color=BLUE, font_size=33).move_to(ss3.get_center() + RIGHT * 0.12)
        self.play(Write(intermediate_result_1))
        self.wait(1)

        # Fade out the highlighted text and return to the original color
        s3_original = Text("63 + 23 = ", color=PINK, font_size=33).next_to(s2, DOWN * 3.5)
        self.play(Transform(s3, s3_original))
        self.wait(1)

        # Highlight tens place digits 6 (in 63) and 2 (in 23)
        s3_tens_highlighted = Text("63 + 23 = ", t2c={'6': YELLOW, '+': PURE_GREEN, '2': YELLOW}, font_size=33).next_to(s2, DOWN * 3.5)
        self.play(Transform(s3, s3_tens_highlighted))
        self.wait(1)

        # Write the intermediate result for the tens place in the square, before the previous result
        intermediate_result_2 = Text("8", color=BLUE, font_size=33).move_to(ss3.get_center() + LEFT * 0.12)
        self.play(Write(intermediate_result_2))
        self.wait(1)

        # Fade out the highlighted text and return to the original color
        self.play(Transform(s3, s3_original))
        self.wait(1)

        # Remove intermediate digits
        self.play(FadeOut(intermediate_result_2), FadeOut(intermediate_result_1))

        # Final result
        s32 = Text("86", color=BLUE, font_size=33).move_to(ss3.get_center())
        self.play(Write(s32))
        self.wait(1)




        # Define and display the fourth addition expression (s4)
        s4 = Text("21 + 50 = ", color=PINK, font_size=33).next_to(s3, DOWN * 3.5)
        ss4 = Square(side_length=0.8).next_to(s4, RIGHT)
        self.play(Write(s4, run_time=2))
        self.play(Write(ss4, run_time=2))

        # Highlight unit's place digits 1 (in 21) and 0 (in 50)
        s4_unit_highlighted = Text("21 + 50 = ", t2c={'1': YELLOW, '+': PURE_GREEN, '0': YELLOW}, font_size=33).next_to(s3, DOWN * 3.5)
        self.play(Transform(s4, s4_unit_highlighted))
        self.wait(1)

        # Write the intermediate result for the unit place in the square
        intermediate_result_1 = Text("1", color=BLUE, font_size=33).move_to(ss4.get_center() + RIGHT * 0.12)
        self.play(Write(intermediate_result_1))
        self.wait(1)

        # Fade out the highlighted text and return to the original color
        s4_original = Text("21 + 50 = ", color=PINK, font_size=33).next_to(s3, DOWN * 3.5)
        self.play(Transform(s4, s4_original))
        self.wait(1)

        # Highlight tens place digits 2 (in 21) and 5 (in 50)
        s4_tens_highlighted = Text("21 + 50 = ", t2c={'2': YELLOW, '+': PURE_GREEN, '5': YELLOW}, font_size=33).next_to(s3, DOWN * 3.5)
        self.play(Transform(s4, s4_tens_highlighted))
        self.wait(1)

        # Write the intermediate result for the tens place in the square, before the previous result
        intermediate_result_2 = Text("7", color=BLUE, font_size=33).move_to(ss4.get_center() + LEFT * 0.12)
        self.play(Write(intermediate_result_2))
        self.wait(1)

        # Fade out the highlighted text and return to the original color
        self.play(Transform(s4, s4_original))
        self.wait(1)

        




        # Define and display the fifth addition expression (s5)
        s5 = Text("84 + 12 = ", color=PINK, font_size=33).next_to(s4, DOWN * 3.5)
        ss5 = Square(side_length=0.8).next_to(s5, RIGHT)
        self.play(Write(s5, run_time=2))
        self.play(Write(ss5, run_time=2))

        # Highlight unit's place digits 4 (in 84) and 2 (in 12)
        s5_unit_highlighted = Text("84 + 12 = ", t2c={'4': YELLOW, '+': PURE_GREEN, '2': YELLOW}, font_size=33).next_to(s4, DOWN * 3.5)
        self.play(Transform(s5, s5_unit_highlighted))
        self.wait(1)

        # Write the intermediate result for the unit place in the square
        intermediate_result_1 = Text("6", color=BLUE, font_size=33).move_to(ss5.get_center() + RIGHT * 0.12)
        self.play(Write(intermediate_result_1))
        self.wait(1)

        # Fade out the highlighted text and return to the original color
        s5_original = Text("84 + 12 = ", color=PINK, font_size=33).next_to(s4, DOWN * 3.5)
        self.play(Transform(s5, s5_original))
        self.wait(1)

        # Highlight tens place digits 8 (in 84) and 1 (in 12)
        s5_tens_highlighted = Text("84 + 12 = ", t2c={'8': YELLOW, '+': PURE_GREEN, '1': YELLOW}, font_size=33).next_to(s4, DOWN * 3.5)
        self.play(Transform(s5, s5_tens_highlighted))
        self.wait(1)

        # Write the intermediate result for the tens place in the square, before the previous result
        intermediate_result_2 = Text("9", color=BLUE, font_size=33).move_to(ss5.get_center() + LEFT * 0.12)
        self.play(Write(intermediate_result_2))
        self.wait(1)

        # Fade out the highlighted text and return to the original color
        self.play(Transform(s5, s5_original))
        self.wait(1)






        # Define and display the sixth addition expression (s6)
        s6 = Text("37 + 52 = ", color=PINK, font_size=33).next_to(s1, RIGHT * 20.5)
        ss6 = Square(side_length=0.8).next_to(s6, RIGHT)
        self.play(Write(s6, run_time=2))
        self.play(Write(ss6, run_time=2))

        # Highlight unit's place digits 7 (in 37) and 2 (in 52)
        s6_unit_highlighted = Text("37 + 52 = ", t2c={'7': YELLOW, '+': PURE_GREEN, '2': YELLOW}, font_size=33).next_to(s1, RIGHT * 20.5)
        self.play(Transform(s6, s6_unit_highlighted))
        self.wait(1)

        # Write the intermediate result for the unit place in the square
        intermediate_result_1 = Text("9", color=BLUE, font_size=33).move_to(ss6.get_center() + RIGHT * 0.12)
        self.play(Write(intermediate_result_1))
        self.wait(1)

        # Fade out the highlighted text and return to the original color
        s6_original = Text("37 + 52 = ", color=PINK, font_size=33).next_to(s1, RIGHT * 20.5)
        self.play(Transform(s6, s6_original))
        self.wait(1)

        # Highlight tens place digits 3 (in 37) and 5 (in 52)
        s6_tens_highlighted = Text("37 + 52 = ", t2c={'3': YELLOW, '+': PURE_GREEN, '5': YELLOW}, font_size=33).next_to(s1, RIGHT * 20.5)
        self.play(Transform(s6, s6_tens_highlighted))
        self.wait(1)

        # Write the intermediate result for the tens place in the square, before the previous result
        intermediate_result_2 = Text("8", color=BLUE, font_size=33).move_to(ss6.get_center() + LEFT * 0.12)
        self.play(Write(intermediate_result_2))
        self.wait(1)

        # Fade out the highlighted text and return to the original color
        self.play(Transform(s6, s6_original))
        self.wait(1)





        # Define and display the seventh addition expression (s7)
        s7 = Text("43 + 21 = ", color=PINK, font_size=33).next_to(s6, DOWN * 3.5)
        ss7 = Square(side_length=0.8).next_to(s7, RIGHT)
        self.play(Write(s7, run_time=2))
        self.play(Write(ss7, run_time=2))

        # Highlight unit's place digits 3 (in 43) and 1 (in 21)
        s7_unit_highlighted = Text("43 + 21 = ", t2c={'3': YELLOW, '+': PURE_GREEN, '1': YELLOW}, font_size=33).next_to(s6, DOWN * 3.5)
        self.play(Transform(s7, s7_unit_highlighted))
        self.wait(1)

        # Write the intermediate result for the unit place in the square
        intermediate_result_1 = Text("4", color=BLUE, font_size=33).move_to(ss7.get_center() + RIGHT * 0.12)
        self.play(Write(intermediate_result_1))
        self.wait(1)

        # Fade out the highlighted text and return to the original color
        s7_original = Text("43 + 21 = ", color=PINK, font_size=33).next_to(s6, DOWN * 3.5)
        self.play(Transform(s7, s7_original))
        self.wait(1)

        # Highlight tens place digits 4 (in 43) and 2 (in 21)
        s7_tens_highlighted = Text("43 + 21 = ", t2c={'4': YELLOW, '+': PURE_GREEN, '2': YELLOW}, font_size=33).next_to(s6, DOWN * 3.5)
        self.play(Transform(s7, s7_tens_highlighted))
        self.wait(1)

        # Write the intermediate result for the tens place in the square, before the previous result
        intermediate_result_2 = Text("6", color=BLUE, font_size=33).move_to(ss7.get_center() + LEFT * 0.12)
        self.play(Write(intermediate_result_2))
        self.wait(1)

        # Fade out the highlighted text and return to the original color
        self.play(Transform(s7, s7_original))
        self.wait(1)





        # Define and display the eighth addition expression (s8)
        s8 = Text("72 + 10 = ", color=PINK, font_size=33).next_to(s7, DOWN * 3.5)
        ss8 = Square(side_length=0.8).next_to(s8, RIGHT)
        self.play(Write(s8, run_time=2))
        self.play(Write(ss8, run_time=2))

        # Highlight unit's place digits 2 (in 72) and 0 (in 10)
        s8_unit_highlighted = Text("72 + 10 = ", t2c={'2': YELLOW, '+': PURE_GREEN, '0': YELLOW}, font_size=33).next_to(s7, DOWN * 3.5)
        self.play(Transform(s8, s8_unit_highlighted))
        self.wait(1)

        # Write the intermediate result for the unit place in the square
        intermediate_result_1 = Text("2", color=BLUE, font_size=33).move_to(ss8.get_center() + RIGHT * 0.12)
        self.play(Write(intermediate_result_1))
        self.wait(1)

        # Fade out the highlighted text and return to the original color
        s8_original = Text("72 + 10 = ", color=PINK, font_size=33).next_to(s7, DOWN * 3.5)
        self.play(Transform(s8, s8_original))
        self.wait(1)

        # Highlight tens place digits 7 (in 72) and 1 (in 10)
        s8_tens_highlighted = Text("72 + 10 = ", t2c={'7': YELLOW, '+': PURE_GREEN, '1': YELLOW}, font_size=33).next_to(s7, DOWN * 3.5)
        self.play(Transform(s8, s8_tens_highlighted))
        self.wait(1)

        # Write the intermediate result for the tens place in the square, before the previous result
        intermediate_result_2 = Text("8", color=BLUE, font_size=33).move_to(ss8.get_center() + LEFT * 0.12)
        self.play(Write(intermediate_result_2))
        self.wait(1)

        # Fade out the highlighted text and return to the original color
        self.play(Transform(s8, s8_original))
        self.wait(1)

        # Remove intermediate digits
        self.play(FadeOut(intermediate_result_2), FadeOut(intermediate_result_1))

        # Final result
        s82 = Text("82", color=BLUE, font_size=33).move_to(ss8.get_center())
        self.play(Write(s82))
        self.wait(1)






        # Define and display the ninth addition expression (s9)
        s9 = Text("46 + 23 = ", color=PINK, font_size=33).next_to(s8, DOWN * 3.5)
        ss9 = Square(side_length=0.8).next_to(s9, RIGHT)
        self.play(Write(s9, run_time=2))
        self.play(Write(ss9, run_time=2))

        # Highlight unit's place digits 6 (in 46) and 3 (in 23)
        s9_unit_highlighted = Text("46 + 23 = ", t2c={'6': YELLOW, '+': PURE_GREEN, '3': YELLOW}, font_size=33).next_to(s8, DOWN * 3.5)
        self.play(Transform(s9, s9_unit_highlighted))
        self.wait(1)

        # Write the intermediate result for the unit place in the square
        intermediate_result_1 = Text("9", color=BLUE, font_size=33).move_to(ss9.get_center() + RIGHT * 0.12)
        self.play(Write(intermediate_result_1))
        self.wait(1)

        # Fade out the highlighted text and return to the original color
        s9_original = Text("46 + 23 = ", color=PINK, font_size=33).next_to(s8, DOWN * 3.5)
        self.play(Transform(s9, s9_original))
        self.wait(1)

        # Highlight tens place digits 4 (in 46) and 2 (in 23)
        s9_tens_highlighted = Text("46 + 23 = ", t2c={'4': YELLOW, '+': PURE_GREEN, '2': YELLOW}, font_size=33).next_to(s8, DOWN * 3.5)
        self.play(Transform(s9, s9_tens_highlighted))
        self.wait(1)

        # Write the intermediate result for the tens place in the square, before the previous result
        intermediate_result_2 = Text("6", color=BLUE, font_size=33).move_to(ss9.get_center() + LEFT * 0.12)
        self.play(Write(intermediate_result_2))
        self.wait(1)

        # Fade out the highlighted text and return to the original color
        self.play(Transform(s9, s9_original))
        self.wait(1)





        # Define and display the tenth addition expression (s10)
        s10 = Text("30 + 24 = ", color=PINK, font_size=33).next_to(s9, DOWN * 3.5)
        ss10 = Square(side_length=0.8).next_to(s10, RIGHT)
        self.play(Write(s10, run_time=2))
        self.play(Write(ss10, run_time=2))

        # Highlight unit's place digits 0 (in 30) and 4 (in 24)
        s10_unit_highlighted = Text("30 + 24 = ", t2c={'0': YELLOW, '+': PURE_GREEN, '4': YELLOW}, font_size=33).next_to(s9, DOWN * 3.5)
        self.play(Transform(s10, s10_unit_highlighted))
        self.wait(1)

        # Write the intermediate result for the unit place in the square
        intermediate_result_1 = Text("4", color=BLUE, font_size=33).move_to(ss10.get_center() + RIGHT * 0.12)
        self.play(Write(intermediate_result_1))
        self.wait(1)

        # Fade out the highlighted text and return to the original color
        s10_original = Text("30 + 24 = ", color=PINK, font_size=33).next_to(s9, DOWN * 3.5)
        self.play(Transform(s10, s10_original))
        self.wait(1)

        # Highlight tens place digits 3 (in 30) and 2 (in 24)
        s10_tens_highlighted = Text("30 + 24 = ", t2c={'3': YELLOW, '+': PURE_GREEN, '2': YELLOW}, font_size=33).next_to(s9, DOWN * 3.5)
        self.play(Transform(s10, s10_tens_highlighted))
        self.wait(1)

        # Write the intermediate result for the tens place in the square, before the previous result
        intermediate_result_2 = Text("5", color=BLUE, font_size=33).move_to(ss10.get_center() + LEFT * 0.12)
        self.play(Write(intermediate_result_2))
        self.wait(1)

        # Fade out the highlighted text and return to the original color
        self.play(Transform(s10, s10_original))
        self.wait(1)

        # Remove intermediate digits
        self.play(FadeOut(intermediate_result_2), FadeOut(intermediate_result_1))

        # Final result
        s102 = Text("54", color=BLUE, font_size=33).move_to(ss10.get_center())
        self.play(Write(s102))
        self.wait(1)




    
    def SetDeveloperList(self):  
        self.DeveloperList="Raghu"

        
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Addition of Numbers.py"


if __name__ == "__main__":
    scene = AdditionofNumbers()
    scene.render()
