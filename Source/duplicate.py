from AbstractAnim import AbstractAnim
from manim import *
import cvo


class duplicate(Scene):
    def construct(self):
        # # Create and display the initial text
        # t1 = Text("Add the numbers given. Write your answer in the box", font_size=35).to_edge(UP + LEFT * 1)
        # self.play(Write(t1))
        

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





        



if __name__ == "__main__":
    from manim import *
    scene = duplicate()
    scene.render()