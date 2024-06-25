# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla
import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo
class grade6(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.introduction()
        self.fadeOutCurrentScene()
        self.pencil()
        self.fadeOutCurrentScene()
        self.pencil2()
        self.fadeOutCurrentScene()
        self.multiplycationofnumbers1()
        self.fadeOutCurrentScene()
        self.multiplycationofnumbers2()
        self.fadeOutCurrentScene()
    
    def RenderSkillbancLogo(self):
        
        self.orange = "#D76800"
        self.blue = "#3F64A7"
        self.green = "#96D24D"
        self.circles = VGroup(
            Circle(radius=1).rotate(PI/2).set_fill(self.orange, opacity=1).set_stroke(self.orange, opacity=1).shift(LEFT*3),
            Circle(radius=1).rotate(PI/2).set_fill(self.blue, opacity=1).set_stroke(self.blue, opacity=1),
            Circle(radius=1).rotate(PI/2).set_fill(self.green, opacity=1).set_stroke(self.green, opacity=1).shift(RIGHT*3)
        )
        circle1, circle2, circle3 = self.circles
        
        lines = VGroup(
            Arrow(circle1.get_right(), circle2.get_left(), max_tip_length_to_length_ratio=2),
            Arrow(circle2.get_right(), circle3.get_left(), max_tip_length_to_length_ratio=2),
            CurvedArrow(circle1.get_top(), circle3.get_top(), angle=-TAU/4),
            CurvedArrow(circle1.get_bottom(), circle3.get_bottom(), angle=TAU/4)
        )

        # Adjust the starting points of the straight arrows to touch the circumference
        lines[0].put_start_and_end_on(circle1.get_right(), circle2.get_left())
        lines[1].put_start_and_end_on(circle2.get_right(), circle3.get_left())

        # Add the text "skillbanc" below the curved arrows
        self.play(Create(circle1), Create(circle2), Create(circle3), rate_func=smooth, run_time=1)
        self.play(Create(lines), rate_func=smooth, run_time=1)
        text = Text("Skillbanc.com, Inc.").next_to(lines[3], DOWN)
        self.play(Create(text), rate_func=smooth, run_time=0.75)
        
        self.logoGroup = VGroup().add(self.circles).add(lines).add(text)
        self.play(self.logoGroup.animate.scale(0),run_time=1)
        # self.play(self.circles.animate.scale(0),lines.animate.scale(0),text.animate.scale(0),run_time=3)
    
    def introduction(self):
        heading = Text("Multiplication of Numbers - 2").scale(1.2)
        heading.move_to(ORIGIN)  # Center the heading
        self.play(Write(heading))
        self.wait(2)
        
    def pencil(self):
        # Initial statement
        initial_text = Text("Geeta said to Lata, 'There are 15 pencils in each packet.'").scale(0.75)
        initial_text2 = Text("How many pencils are there in 3 such packets?").scale(0.75)
        initial_text.to_edge(UP)
        initial_text2.next_to(initial_text, DOWN)
        
        self.play(Write(initial_text), Write(initial_text2))
        self.wait(2)

        # Calculation steps
        step1 = Text("15 * 3 = ?").scale(1.0)
        step2 = Text("= (10 + 5) * 3").scale(1.0)
        step3 = Text("= 30 + 15").scale(1.0)
        step4 = Text("= 30 + 10 + 5").scale(1.0)
        step5 = Text("= 40 + 5").scale(1.0)
        step6 = Text("= 45").scale(1.0)

        # Positioning the steps
        step1.move_to(2*UP)
        step2.next_to(step1, DOWN, buff=0.2)
        step3.next_to(step2, DOWN, buff=0.2)
        step4.next_to(step3, DOWN, buff=0.2)
        step5.next_to(step4, DOWN, buff=0.2)
        step6.next_to(step5, DOWN, buff=0.2)
        
        # Showing the steps with reduced space
        self.play(Write(step1))
        self.wait(1)
        self.play(Write(step2))
        self.wait(1)
        self.play(Write(step3))
        self.wait(1)
        self.play(Write(step4))
        self.wait(1)
        self.play(Write(step5))
        self.wait(1)
        self.play(Write(step6))
        self.wait(1)

        # Conclusion
        conclusion_text = Text("Therefore, there are 45 pencils in 3 packets.").scale(0.8)
        conclusion_text.next_to(step6, DOWN, buff=0.2)
        self.play(Write(conclusion_text))
        self.wait(2)
        
    def pencil2(self):
        heading = Text("Alternative").scale(1.0)
        heading.move_to(UP * 3 + LEFT * 4)  # Position on the top-left corner
        self.play(Write(heading))
        self.wait(2)
        
        # Calculation steps - Left side (for "If tens are multiplied")
        left_box_texts = [
            Text("If tens are multiplied.").scale(0.8),
            Text("3 x 1 = 3 tens").scale(0.8),
            Text("3 tens + 1 ten = 4 tens").scale(0.8),
        ]
        left_box = VGroup(*left_box_texts).arrange(DOWN, buff=0.2)
        left_box.move_to(LEFT * 4)

        # Create a box around left_box
        left_box_border = SurroundingRectangle(left_box, buff=0.1)

        # Calculation steps - Right side (for "If ones are multiplied")
        right_box_texts = [
            Text("If ones are multiplied.").scale(0.8),
            Text("5 x 3 = 15 ones").scale(0.8),
            Text("15 ones + 1 ten = 5 ones").scale(0.8),
        ]
        right_box = VGroup(*right_box_texts).arrange(DOWN, buff=0.2)
        right_box.move_to(RIGHT * 4)

        # Create a box around right_box
        right_box_border = SurroundingRectangle(right_box, buff=0.1)

        # Central box (for "T O 1 1 5 I 3 4 5")
        central_box_texts = [
            Text("T O").scale(1.0),
            VGroup(   # VGroup to include the circle around "1"
                Circle(radius=0.2, color=WHITE, stroke_width=2),
                Text("1").scale(0.8),  # Scale down the text to fit within the circle
            ),
            Text("1 5").scale(1.0),
           VGroup(   # VGroup for "* 3" and line underneath
                Text("* 3").scale(1.0),
                Line(color=WHITE).set_width(Text("* 3").get_width()).move_to(DOWN * 0.5),  # Line below "* 3"
            ),
            Text("4 5").scale(1.0),
        ]
        central_box = VGroup(*central_box_texts).arrange(DOWN, buff=0.2)
        central_box[0].set_color(YELLOW)  # Color T O in yellow

        # Calculate dimensions for the central box
        central_box_width = max([text.get_width() for text in central_box_texts])
        central_box_height = sum([text.get_height() for text in central_box_texts]) + (len(central_box_texts) - 1) * 0.2

        # Positioning the texts within the central box
        for text in central_box_texts:
            text.align_to(central_box[0], LEFT)

        # Create a bounding box around central_box_texts
        central_box_border = SurroundingRectangle(central_box, buff=0.1)

        # Positioning
        central_box.move_to(UP * 1.5)
        central_box_border.move_to(UP * 1.5)

        # Line from T O to the bottom of the last text
        line = Line(central_box_texts[0].get_bottom(), central_box_texts[-1].get_bottom(), color=WHITE)

        # Showing the boxes and line
        self.play(
            Write(central_box_border),
            Write(central_box),
            Write(line),
        )
        self.wait(1)

        # Showing left_box and right_box with their borders
        self.play(
            Write(left_box_border),
            Write(left_box),
        )
        self.wait(1)
        
        self.play(
            Write(right_box_border),
            Write(right_box),
        )
        self.wait(2)

    def multiplycationofnumbers1(self):
        heading = Text("multiplication of numbers").scale(1.0)
        heading.move_to(UP * 3 + LEFT * 3)  # Position on the top-left corner
        self.play(Write(heading))
        self.wait(2)
        # Creating the texts with reduced scale
        text_t_o = Text("T O", color=BLUE).scale(1.0)  # Set "T O" in blue
        text_3_6 = Text("3 6").scale(1.0)
        text_star_3 = Text("* 3").scale(1.0)

        # Arranging the texts vertically with reduced buffer and aligning to the left
        texts_group = VGroup(text_t_o, text_3_6, text_star_3).arrange(DOWN, buff=0.4, aligned_edge=LEFT)

        # Creating the lines with reduced spacing
        line1 = Line(color=WHITE).set_width(text_star_3.get_width()).next_to(text_star_3, DOWN, buff=0.3)
        line2 = Line(color=WHITE).set_width(text_star_3.get_width()).next_to(line1, DOWN, buff=0.3)

        # Combine texts and lines
        display_group = VGroup(texts_group, line1, line2)

        # Aligning everything to the left side
        display_group.move_to(LEFT * 4)

        # Displaying the texts and lines on the screen
        self.play(Write(display_group))
        self.wait(2)
        
         # Create all Text objects
        texts = [
            Text("= 30 + 6"),
            Text("= * 3"),
            Text("= 90 + 18"),
            Text("= 90 + 10 + 8"),
            Text("= 100 + 8"),
            Text("= 108"),
        ]

        # Additional text to be inserted between two lines
        additional_text = Text("30*3 + 6*3")
        additional_text.scale(0.8)  # Scale down the additional text

        # Scale down all texts uniformly
        for text in texts:
            text.scale(0.8)

        # Insert the additional text between the second and third lines
        texts.insert(2, additional_text)

        # Arrange texts vertically with a specific buffer
        texts_group = VGroup(*texts).arrange(DOWN, buff=0.5)

        # Move texts to the right side of the screen
        texts_group.move_to(RIGHT * 4)

        # Display the texts on the screen
        self.play(Write(texts_group))
        self.wait(2)
        
    def multiplycationofnumbers2(self):  
           
        heading = Text("multiplication of numbers").scale(1.0)
        heading.move_to(UP * 3 + LEFT * 3)  # Position on the top-left corner
        self.play(Write(heading))
        self.wait(2)
        # Creating the texts with reduced scale
        text_t_o = Text("T O", color=BLUE).scale(1.0)  # Set "T O" in blue
        text_3_6 = Text("3 6").scale(1.0)
        text_star_3 = Text("* 3").scale(1.0)

        # Arranging the texts vertically with reduced buffer and aligning to the left
        texts_group = VGroup(text_t_o, text_3_6, text_star_3).arrange(DOWN, buff=0.4, aligned_edge=LEFT)

        # Creating the lines with reduced spacing
        line1 = Line(color=WHITE).set_width(text_star_3.get_width()).next_to(text_star_3, DOWN, buff=0.3)
        line2 = Line(color=WHITE).set_width(text_star_3.get_width()).next_to(line1, DOWN, buff=0.3)

        # Combine texts and lines
        display_group = VGroup(texts_group, line1, line2)

        # Aligning everything to the left side
        display_group.move_to(LEFT * 4)

        # Displaying the texts and lines on the screen
        self.play(Write(display_group))
        self.wait(2)
        
         # Create all Text objects
        texts = [
            Text("= 6 ones x 3 = 18 ones = 1 ten + 8 ones"),
            Text("= 3 tens x 3           = 9 tens"),
            Text("= 10 tens + 8 ones"),
            Text("= 100 ones + 8 ones"),
            Text("= 108"),
        ]

        # Additional text to be inserted between two lines
        additional_text = Text("30*3 + 6*3")
        additional_text.scale(0.8)  # Scale down the additional text

        # Scale down all texts uniformly
        for text in texts:
            text.scale(0.8)

        # Insert the additional text between the second and third lines
        texts.insert(2, additional_text)

        # Arrange texts vertically with a specific buffer
        texts_group = VGroup(*texts).arrange(DOWN, buff=0.5)

        # Move texts to the right side of the screen
        texts_group.move_to(RIGHT * 2)

        # Display the texts on the screen
        self.play(Write(texts_group))
        self.wait(2)

if __name__ == "__main__":
    scene = grade6()
    scene.render()
