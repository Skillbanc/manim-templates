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
        
        title = Text("cont....", font_size=48)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        self.wait(1)

        # Create larger packets
        packets = VGroup(*[Rectangle(height=3, width=2.5, fill_opacity=0.5, fill_color=BLUE) for _ in range(3)])
        packets.arrange(RIGHT, buff=0.8)
        packets.next_to(title, DOWN, buff=0.8)

        # Label packets
        labels = VGroup(*[Text(f"Packet {i+1}", font_size=28).next_to(packet, UP) for i, packet in enumerate(packets)])

        self.play(Create(packets), Write(labels))
        self.wait(1)

        # Create larger pencils
        pencil = Rectangle(height=0.5, width=0.1, fill_opacity=1, fill_color=YELLOW, stroke_color=DARK_BROWN)
        pencil_tip = Triangle(fill_color=DARK_BROWN, fill_opacity=1).scale(0.1).rotate(PI).next_to(pencil, DOWN, buff=0)
        pencil_group = VGroup(pencil, pencil_tip)

        # Function to create and arrange pencils in a packet
        def create_pencils_in_packet(packet):
            pencils = VGroup(*[pencil_group.copy() for _ in range(15)])
            
            # Calculate the available space in the packet
            packet_width = packet.width * 0.9
            packet_height = packet.height * 0.9
            
            # Arrange pencils in a 3x5 grid (3 rows, 5 columns)
            rows, cols = 3, 5
            x_spacing = packet_width / cols
            y_spacing = packet_height / rows
            
            for i, pencil in enumerate(pencils):
                row = i // cols
                col = i % cols
                x = packet.get_left()[0] + (col + 0.5) * x_spacing
                y = packet.get_bottom()[1] + (row + 0.5) * y_spacing
                pencil.move_to(np.array([x, y, 0]))
            
            return pencils

        # Show pencils in each packet
        all_pencils = VGroup()
        for i, packet in enumerate(packets):
            pencils = create_pencils_in_packet(packet)
            all_pencils.add(pencils)
            self.play(FadeIn(pencils), run_time=1)
            count = Text(f"15 pencils", font_size=24).next_to(packet, DOWN)
            self.play(Write(count))
            self.wait(2)

        # Show multiplication
        equation = MathTex("15 + 15 + 15", "=", "15 ","*"," 3 = 45") 
        equation.scale(1)
        equation.next_to(packets, DOWN, buff=1.2)
        self.play(Write(equation))
        self.wait(1)

        # Final answer
        answer = Text("There are 45 pencils in total!", font_size=30, color=YELLOW)
        answer.next_to(equation, DOWN, buff=0.7)
        self.play(Write(answer))
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
