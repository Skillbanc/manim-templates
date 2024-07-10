from manim import *
from AbstractAnim import AbstractAnim
import cvo


class AdditionofNumbers(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.Extra_text()
        self.fadeOutCurrentScene()
        self.addition()
        self.fadeOutCurrentScene()
        self.vertical_addition_Exercise_1()
        self.fadeOutCurrentScene()
        self.horizontal_additionExercise()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()


    def Extra_text(self):
        title = Text("Chapter 5 : Addition of Numbers", font_size=45)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))


    def addition(self):
        self.isRandom=False
        self.setNumberOfCirclePositions(2)
        p10=cvo.CVO().CreateCVO("Addition","").setPosition([-4,2,0])
        p11=cvo.CVO().CreateCVO("Symbol","+").setPosition([4,2,0]).setangle(-TAU/4)
        p12=cvo.CVO().CreateCVO("Example","35+15=50").setPosition([3.5,-1,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)

        p11.setcircleradius(1.25)
        self.construct1(p10,p10)





    def vertical_addition_Exercise_1(self):
        # Title
        title = Tex("Solving the following additions:", color=BLUE).to_edge(UP*1.5+LEFT*1)
        self.play(Write(title))
    
        # Addition 52 + 21 = 73
        addition1 = self.vertical_addition("52", "21", "73")
        addition1.move_to([-5,1,0])

        # Addition 24 + 22 = 46
        addition2 = self.vertical_addition("24", "22", "46")
        addition2.move_to([-1.5,1,0])

        # Addition 16 + 33 = 49
        addition3 = self.vertical_addition("16", "33", "49")
        addition3.move_to([1.5,1,0])

        # Addition 37 + 51 = 88
        addition4 = self.vertical_addition("37", "51", "88")
        addition4.move_to([5,1,0])

        # Addition 12 + 53 = 65
        addition5 = self.vertical_addition("12", "53", "65")
        addition5.move_to([-5,-2,0])

        # Addition 66 + 13 = 99
        addition6 = self.vertical_addition("66", "13", "79")
        addition6.move_to([-1.5,-2,0])

        # Addition 30 + 20 = 50
        addition7 = self.vertical_addition("30", "20", "50")
        addition7.move_to([1.5,-2,0])

        # Addition 60 + 23 = 83
        addition8 = self.vertical_addition("60", "23", "83")
        addition8.move_to([5,-2,0])


        
        self.play(Create(addition1))
        self.wait(1.5)
        self.play(Create(addition2))
        self.wait(1.5)
        self.play(Create(addition3))
        self.wait(2)
        self.play(Create(addition4))
        self.wait(2)
        self.play(Create(addition5))
        self.wait(2)
        self.play(Create(addition6))
        self.wait(2)
        self.play(Create(addition7))
        self.wait(2)
        self.play(Create(addition8))
        self.wait(2)


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

        numbers[1].next_to(numbers[0],DOWN)
        numbers[5].next_to(numbers[1],LEFT)

        return numbers




    def horizontal_additionExercise(self):
        # Create and display the initial text
        t1 = Text("Calculate the differences for the following pairs of numbers:", font_size=35).to_edge(UP + LEFT * 1)
        self.play(Write(t1))
        

        # Define and display the first addition expression (s1)
        s1 = Text("23 + 14 = ", color=PINK, font_size=33).to_edge(LEFT * 3.5 + UP * 3.5)
        ss1 = Square(side_length=0.8).next_to(s1, RIGHT)
        self.play(Write(s1, run_time=2))
        self.play(Write(ss1, run_time=2))

        # Highlight unit's place digits 3 (in 23) and 4 (in 14)
        s1_unit_highlighted = Text("23 + 14 = ", t2c={'3': GREEN, '+': RED, '4': GREEN}, font_size=33).to_edge(LEFT * 3.5 + UP * 3.5)
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
        s1_tens_highlighted = Text("23 + 14 = ", t2c={'2': GREEN, '+': RED, '1': GREEN}, font_size=33).to_edge(LEFT * 3.5 + UP * 3.5)
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
        s2_unit_highlighted = Text("75 + 24 = ", t2c={'5': GREEN, '+': RED, '4': GREEN}, font_size=33).next_to(s1, DOWN * 3.5)
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
        s2_tens_highlighted = Text("75 + 24 = ", t2c={'7': GREEN, '+': RED, '2': GREEN}, font_size=33).next_to(s1, DOWN * 3.5)
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
        s3_unit_highlighted = Text("63 + 23 = ", t2c={'3': GREEN, '+': RED, '3': GREEN}, font_size=33).next_to(s2, DOWN * 3.5)
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
        s3_tens_highlighted = Text("63 + 23 = ", t2c={'6': GREEN, '+': RED, '2': GREEN}, font_size=33).next_to(s2, DOWN * 3.5)
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
        s4_unit_highlighted = Text("21 + 50 = ", t2c={'1': GREEN, '+': RED, '0': GREEN}, font_size=33).next_to(s3, DOWN * 3.5)
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
        s4_tens_highlighted = Text("21 + 50 = ", t2c={'2': GREEN, '+': RED, '5': GREEN}, font_size=33).next_to(s3, DOWN * 3.5)
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
        s5_unit_highlighted = Text("84 + 12 = ", t2c={'4': GREEN, '+': RED, '2': GREEN}, font_size=33).next_to(s4, DOWN * 3.5)
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
        s5_tens_highlighted = Text("84 + 12 = ", t2c={'8': GREEN, '+': RED, '1': GREEN}, font_size=33).next_to(s4, DOWN * 3.5)
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
        s6_unit_highlighted = Text("37 + 52 = ", t2c={'7': GREEN, '+': RED, '2': GREEN}, font_size=33).next_to(s1, RIGHT * 20.5)
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
        s6_tens_highlighted = Text("37 + 52 = ", t2c={'3': GREEN, '+': RED, '5': GREEN}, font_size=33).next_to(s1, RIGHT * 20.5)
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
        s7_unit_highlighted = Text("43 + 21 = ", t2c={'3': GREEN, '+': RED, '1': GREEN}, font_size=33).next_to(s6, DOWN * 3.5)
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
        s7_tens_highlighted = Text("43 + 21 = ", t2c={'4': GREEN, '+': RED, '2': GREEN}, font_size=33).next_to(s6, DOWN * 3.5)
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
        s8_unit_highlighted = Text("72 + 10 = ", t2c={'2': GREEN, '+': RED, '0': GREEN}, font_size=33).next_to(s7, DOWN * 3.5)
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
        s8_tens_highlighted = Text("72 + 10 = ", t2c={'7': GREEN, '+': RED, '1': GREEN}, font_size=33).next_to(s7, DOWN * 3.5)
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
        s9_unit_highlighted = Text("46 + 23 = ", t2c={'6': GREEN, '+': RED, '3': GREEN}, font_size=33).next_to(s8, DOWN * 3.5)
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
        s9_tens_highlighted = Text("46 + 23 = ", t2c={'4': GREEN, '+': RED, '2': GREEN}, font_size=33).next_to(s8, DOWN * 3.5)
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
        s10_unit_highlighted = Text("30 + 24 = ", t2c={'0': GREEN, '+': RED, '4': GREEN}, font_size=33).next_to(s9, DOWN * 3.5)
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
        s10_tens_highlighted = Text("30 + 24 = ", t2c={'3': GREEN, '+': RED, '2': GREEN}, font_size=33).next_to(s9, DOWN * 3.5)
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
