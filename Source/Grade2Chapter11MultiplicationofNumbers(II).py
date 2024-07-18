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

config.max_files_cached = 800  # Change this number to your desired value

class grade2(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.introduction()
        self.fadeOutCurrentScene()
        self.intro()
        self.fadeOutCurrentScene()
        self.pencil()
        self.fadeOutCurrentScene()
        self.pencil2()
        self.fadeOutCurrentScene()
        self.multiplycationofnumbers1()
        self.fadeOutCurrentScene()
        self.multiplycationofnumbers2()
        self.fadeOutCurrentScene()
        self.box()
        self.fadeOutCurrentScene()
        self.seriesofnumbers()
        self.fadeOutCurrentScene()
        self.pyramid()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        
    def SetDeveloperList(self):  
        self.DeveloperList="Vasudha"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade2Chapter11MultiplicationofNumbers(II).py"
    
    def introduction(self):
        heading = Text("Multiplication of Numbers - II").scale(1.2)
        heading.move_to(ORIGIN)  # Center the heading
        self.play(Write(heading))
        self.wait(2)
        
    def intro(self):
        self.setNumberOfCirclePositions(3)
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Multiplication ","").setPosition([-3.5,1,0]).setangle(-TAU/4)
        p11=cvo.CVO().CreateCVO("Definition"," the process of calculating the product of two or more numbers.").setPosition([0,-2,0]).setangle(-TAU/4)
        p11.setcircleradius(1.5)
        p12=cvo.CVO().CreateCVO("Symbol","x").setPosition([3,1,0]).setangle(-TAU/4)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        
        self.construct1(p10,p10)
        
    def pencil(self):
        # Initial statement
        initial_text = Text("Geeta said to Lata, 'There are 15 pencils in each packet.'").scale(0.75)
        initial_text2 = Text("How many pencils are there in 3 such packets?").scale(0.75)
        initial_text.to_edge(UP)
        initial_text2.next_to(initial_text, DOWN)
        
        self.play(Write(initial_text), Write(initial_text2))
        self.wait(2)

        # Calculation steps
        step1 = Text("15 * 3 = ?").scale(0.5)
        step2 = Text("= (10 + 5) * 3").scale(0.5)
        step3 = Text("= 30 + 15").scale(0.5)
        step4 = Text("= 30 + 10 + 5").scale(0.5)
        step5 = Text("= 40 + 5").scale(0.5)
        step6 = Text("= 45").scale(0.5)

        # Positioning the steps
        step1.move_to(2*UP)
        step2.next_to(step1, DOWN, buff=0.5)
        step3.next_to(step2, DOWN, buff=0.5)
        step4.next_to(step3, DOWN, buff=0.5)
        step5.next_to(step4, DOWN, buff=0.5)
        step6.next_to(step5, DOWN, buff=0.5)
        
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

        # New: Add T = tens, O = ones box at top right
        to_explanation = VGroup(
            Text("T = tens", font_size=24),
            Text("O = ones", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT)
        to_box = SurroundingRectangle(to_explanation, buff=0.1)
        to_group = VGroup(to_explanation, to_box).move_to(UP * 3 + RIGHT * 4)
    
        self.play(Write(to_group))
        self.wait(1)

        # Rest of the code remains the same
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
            Text("5 ones + 1 ten = 15 ones").scale(0.8),
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
                Text("x 3").scale(1.0),
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
        # line = Line(central_box_texts[0].get_bottom(), central_box_texts[-1].get_bottom(), color=WHITE)

        # Showing the boxes and line
        self.play(
            Write(central_box_border),
            Write(central_box),
            # Write(line),
        )
        self.wait(2)
        right_arrow = Arrow(
            start=right_box_border.get_left(), 
            end=central_box[4].get_right() + RIGHT * 0.2,
            buff=0.1,
            color=PINK
        )

        # Showing right_box with its border and then displaying the circle around "1" and "5"
        self.play(
            Write(right_box_border),
            Write(right_box),
        )
        self.play(
            Create(right_arrow),
        )
        
        self.wait(2)
        # self.play(
        #     central_box[1].animate.set_color(YELLOW),  # Highlight the circle around "1"
        #     central_box[4].animate.set_color(YELLOW),  # Highlight "1 5"
        # )
        # self.wait(2)
        left_arrow = Arrow(
            start=left_box_border.get_right(), 
            end=central_box[4].get_left() + LEFT * 0.2,
            buff=0.1,
            color=YELLOW
        )

        # Showing left_box with its border and then displaying "4" in the central box
        self.play(
            Write(left_box_border),
            Write(left_box),
        )
        
        self.play(
            Create(left_arrow),
        )
        self.wait(2)
        # self.play(
        #     central_box[4].animate.set_color(YELLOW),  # Highlight "4"
        # )
        self.wait(2)
        
        self.wait(2)

    def multiplycationofnumbers1(self):
       # Heading
        heading = Text("Multiplication of Numbers").scale(1.0)
        heading.move_to(UP * 3 + LEFT * 3)  # Position on the top-left corner
        self.play(Write(heading))
        self.wait(2)
        
        # Creating the texts with reduced scale
        text_t_o = Text("T O", color=BLUE).scale(1.0)  # Set "T O" in blue
        text_3_6 = Text("3 6").scale(1.0)
        text_star_3 = Text("x 3").scale(1.0)

        # Arranging the texts vertically with reduced buffer and aligning to the left
        texts_group = VGroup(text_t_o, text_3_6, text_star_3).arrange(DOWN, buff=0.4, aligned_edge=LEFT)

        # Creating the lines with reduced spacing
        line1 = Line(color=WHITE).set_width(text_star_3.get_width()).next_to(text_star_3, DOWN, buff=0.3)
        line2 = Line(color=WHITE).set_width(text_star_3.get_width()).next_to(line1, DOWN * 2, buff=0.3)

        # Combine texts and lines
        display_group = VGroup(texts_group, line1, line2)

        # Aligning everything to the left side
        display_group.move_to(LEFT * 4)

        # Displaying the texts and lines on the screen
        self.play(Write(display_group))
        self.wait(2)

        # # Create the "108" text
        # text_108 = Text("108").scale(0.7)
        # text_108.move_to((line1.get_center() + line2.get_center()) / 2)
        # self.play(Write(text_108))
        # self.wait(2)

        # Create all Text objects
        texts = [
            Text("= (30 + 6) * 3"),
            Text("= 90 + 18"),
            Text("= 90 + 10 + 8"),
            Text("= 100 + 8"),
            Text("= 108"),
        ]

        # Additional text to be inserted between two lines
        additional_text = Text("30 * 3 + 6 * 3")
        additional_text.scale(0.8)  # Scale down the additional text

        # Scale down all texts uniformly
        for text in texts:
            text.scale(0.8)

        # Insert the additional text between the second and third lines
        texts.insert(1, additional_text)

        # Arrange texts vertically with a specific buffer
        texts_group = VGroup(*texts).arrange(DOWN, buff=0.5)

        # Move texts to the right side of the screen
        texts_group.move_to(RIGHT * 4)

        # Display the texts one by one on the screen
        for text in texts_group:
            self.play(Write(text))
            self.wait(2)

        self.wait(2)
        
        # Create the "108" text
        text_108 = Text("108").scale(0.7)
        text_108.move_to((line1.get_center() + line2.get_center()) / 2)
        self.play(Write(text_108))
        self.wait(2)

        
    def multiplycationofnumbers2(self):  
           
        heading = Text("multiplication of numbers(alternative)").scale(1.0)
        heading.move_to(UP * 3 )  # Position on the top-left corner
        self.play(Write(heading))
        self.wait(2)

        # Creating the texts with reduced scale
        text_t_o = Text("T O", color=BLUE).scale(1.0)  # Set "T O" in blue
        text_3_6 = Text("3 6").scale(1.0)
        text_star_3 = Text("x 3").scale(1.0)

        # Arranging the texts vertically with reduced buffer and aligning to the left
        texts_group = VGroup(text_t_o, text_3_6, text_star_3).arrange(DOWN, buff=0.4, aligned_edge=LEFT)

        # Creating the lines with reduced spacing
        line1 = Line(color=WHITE).set_width(text_star_3.get_width()).next_to(text_star_3, DOWN, buff=0.3)
        line2 = Line(color=WHITE).set_width(text_star_3.get_width()).next_to(line1, DOWN*2, buff=0.3)

        # Combine texts and lines
        display_group = VGroup(texts_group, line1, line2)

        # Aligning everything to the left side
        display_group.move_to(LEFT * 4)

        # Displaying the texts and lines on the screen
        self.play(Write(display_group))
        self.wait(2)

        
         # Create all Text objects
        texts = [
            Text("=> 6 ones x 3 = 18 ones = 1 ten + 8 ones"),
            Text("=> 3 tens x 3           = 9 tens"),
            Text("                        = 10 tens + 8 ones"),
            Text("                        = 100 ones + 8 ones"),
            Text("                        = 108"),
        ]

        # Scale down all texts uniformly
        for text in texts:
            text.scale(0.8)
        # Arrange texts vertically with a specific buffer
        texts_group = VGroup(*texts).arrange(DOWN, buff=0.5)

        # Move texts to the right side of the screen
        texts_group.move_to(RIGHT * 2)
        
        # Display the texts one by one on the screen
        for text in texts_group:
            self.play(Write(text))
            self.wait(2)

        
        # Create the "108" text
        text_108 = Text("108").scale(0.7)
        text_108.move_to((line1.get_center() + line2.get_center()) / 2)
        self.play(Write(text_108))
        self.wait(2)
        
    def box(self):
        # Create the table with reduced size
        table = Table(
            [["x", "5", "6", "7", "8", "12"],
             ["12", "60", "72", "84", "96", "144"],
             ["14", "70", "84", "98", "112", "168"],
             ["16", "80", "96", "112", "128", "192"],
             ["18", "90", "108", "126", "144", "216"]],
            include_outer_lines=True,
            line_config={"color": WHITE}
        ).scale(0.6)  # Scale down the table
    
        # Add a smaller rectangle around the table
        rect = SurroundingRectangle(table, buff=0.05, color=WHITE)
    
        # Group the table and rectangle
        table_group = VGroup(table, rect).move_to(LEFT * 3)
    
        # Highlight the first row and first column
        first_row = table.get_rows()[0]
        first_column = table.get_columns()[0]
        first_row.set_color(YELLOW)
        first_column.set_color(BLUE)
    
        # Create explanation text with smaller font size
        explanation = VGroup(
            Text("Multiplication Table:", font_size=24),
            Text("Each row shows the product of", font_size=20),
            Text("the first number multiplied by", font_size=20),
            Text("the numbers in the top row.", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(table_group, RIGHT, buff=0.3)
    
        # Animation
        self.play(Create(rect))
        self.play(Write(first_row), Write(first_column))
        self.wait(2)
        self.play(Write(explanation))
        self.wait(2)

        # Show the remaining rows one by one
        for row in table.get_rows()[1:]:
            self.play(Write(VGroup(*row[1:])))
            self.wait(1)

        self.wait(2)


    def seriesofnumbers(self):
        heading = Text("Series of Numbers", font_size=48)
        heading.to_edge(UP)
        self.play(Write(heading))
        self.wait(1)

        series = [
            ("(a) 2, 4, 6, ", [8, 10, 12], "Add 2 each time"),
            ("(b) 5, 10, 15, ", [20, 25, 30], "Add 5 each time"),
            ("(c) 7, 14, 21, ", [28, 35, 42], "Add 7 each time"),
            ("(d) 9, 18, 27, ", [36, 45, 54], "Add 9 each time")
        ]

        for i, (start, continuation, explanation) in enumerate(series):
            # Create the initial series text
            text = Text(start, font_size=36)
            text.to_edge(LEFT).shift(UP * (1 - i * 1.2))  # Adjusted vertical spacing

            # Create explanation text box
            explain_box = Text(explanation, font_size=24, color=BLUE)
            explain_box.to_edge(RIGHT).align_to(text, UP)

            # Add the initial text and explanation
            self.play(Write(text))
            self.wait(1)
            self.play(Write(explain_box))
            self.wait(1)

            # Create placeholders and underlines for new numbers
            new_nums = []
            underlines = []
            for j, num in enumerate(continuation):
                new_num = Text(str(num) + (", " if j < 2 else ""), font_size=36)
                new_num.next_to(text, RIGHT, buff=0.8)  # Adjusted horizontal spacing
                underline = Underline(new_num, color=YELLOW).shift(DOWN * 0.1)  # Shifted underline down
                new_nums.append(new_num)
                underlines.append(underline)

                # Update text to include new_num for positioning the next number
                text = VGroup(text, new_num)

            # Show all underlines first
            self.play(*[Create(underline) for underline in underlines])

            # Show the explanation after underlines
            # explanation_text = Text(explanation, font_size=24, color=BLUE)
            # explanation_text.next_to(underlines[-1], RIGHT*2, buff=1)
            # self.play(Write(explanation_text))
            
            # Then reveal each new number
            for new_num in new_nums:
                self.play(Write(new_num))

            self.wait(0.5)

        self.wait(2)
        
    def pyramid(self): 
        # Title
        title = Text("Multiplication Pyramid", font_size=36)
        title.to_edge(UP + LEFT)
        self.play(Write(title))

        # Create the pyramid structure
        circles = []
        numbers = [2, 1, 4, None, None, None, None, None, None]
        positions = [
            (-2, -2, 0), (0, -2, 0), (2, -2, 0),
            (-1, 0, 0), (1, 0, 0),
            (0, 2, 0)
        ]

        for i, pos in enumerate(positions):
            circle = Circle(radius=0.3, color=BLUE)
            circle.move_to(pos)
            if i < len(numbers) and numbers[i] is not None:
                number = Text(str(numbers[i]), font_size=20)
                number.move_to(circle.get_center())
                circle.add(number)
            circles.append(circle)

        # Draw the pyramid
        for circle in circles:
            self.play(Create(circle))

        # Draw arrows
        arrows = []
        arrow_positions = [
            (circles[0], circles[3]), (circles[1], circles[3]), (circles[1], circles[4]), 
            (circles[2], circles[4]), (circles[3], circles[5]), (circles[4], circles[5])
        ]

        for start, end in arrow_positions:
            arrow = Arrow(start.get_top(), end.get_bottom(), buff=0.05, color=YELLOW)
            arrows.append(arrow)
            self.play(GrowArrow(arrow))

        # Perform multiplications
        multiplications = [
            (0, 1, 3), (1, 2, 4), 
            (3, 4, 5)
        ]

        for i, j, k in multiplications:
            self.play(circles[i].animate.set_color(RED), circles[j].animate.set_color(RED))
            if i < len(circles) and j < len(circles) and i < 5:  # Only the bottom row has initial numbers
                product = int(circles[i].submobjects[0].text) * int(circles[j].submobjects[0].text)
                result = Text(str(product), font_size=24, color=WHITE)
                result.move_to(circles[k].get_center())
                self.play(Write(result))
                circles[k].add(result)
            self.play(circles[i].animate.set_color(BLUE), circles[j].animate.set_color(BLUE))

        self.wait(2)

if __name__ == "__main__":
    scene = grade2()
    scene.render()
