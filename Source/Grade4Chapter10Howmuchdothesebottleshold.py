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

class Howmuchdothesebottleshold(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.Litre()
        self.fadeOutCurrentScene()
        self.Exercise1()
        self.fadeOutCurrentScene()
        self.Exercise2()
        self.fadeOutCurrentScene()
        self.fillbottle()
        self.fadeOutCurrentScene()
        self.Example3()
        self.fadeOutCurrentScene()
        self.answer()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()        

    def Litre(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Litre","")
        p11=cvo.CVO().CreateCVO("1 litre", "1000 ml")
        p12=cvo.CVO().CreateCVO("Written as", "L or l")
        p13=cvo.CVO().CreateCVO("Millilitre written as", "ml or mL")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.setNumberOfCirclePositions(4)
        self.construct1(p10,p10)
  
    def Exercise1(self):
        # Define the colors for the title and blanks
        title_color = RED
        blank_color = YELLOW
        
        # Title text
        title = Text("Q. Fill in the blanks given below:", font_size=48, weight=BOLD, color=title_color)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Define the texts with placeholders for blanks
        text_a = Text("(a) 500 ml + _________ = 1 litre.", font_size=36)
        text_b = Text("(b) _________ + 750 ml = 1 litre.", font_size=36)
        text_c = Text("(c) 3 litres  = ____________ ml", font_size=36)
        text_d = Text("(d) 7 litres = ____________ ml", font_size=36)
        text_e = Text("(e) 8500 ml = ____l _______ ml", font_size=36)
        
        # Position the texts
        text_a.next_to(title, DOWN, buff=1)
        text_b.next_to(text_a, DOWN, buff=0.5)
        text_c.next_to(text_b, DOWN, buff=0.5)
        text_d.next_to(text_c, DOWN, buff=0.5)
        text_e.next_to(text_d, DOWN, buff=0.5)
        
        # Define the answers
        answer_a = Text("500 ml", color=blank_color, font_size=36)
        answer_b = Text("250 ml", color=blank_color, font_size=36)
        answer_c = Text("3000 ", color=blank_color, font_size=36)
        answer_d = Text("7000 ", color=blank_color, font_size=36)
        answer_e1 = Text("8 ", color=blank_color, font_size=36)
        answer_e2 = Text("500 ", color=blank_color, font_size=36)
        
        # Manually position the answers above the blanks
        answer_a.next_to(text_a[12], UP, buff=0.1)  # Position above the blank in text_a
        answer_b.next_to(text_b[6], UP, buff=0.1)   # Position above the blank in text_b
        answer_c.next_to(text_c[15], UP, buff=0.1)  # Position above the blank in text_c
        answer_d.next_to(text_d[15], UP, buff=0.1)  # Position above the blank in text_d
        answer_e1.next_to(text_e[12], UP, buff=0.1) # Position above the first blank in text_e
        answer_e2.next_to(text_e[19], UP, buff=0.1) # Position above the second blank in text_e
        
        # Animate the texts and answers
        self.play(Write(text_a))
        self.play(Write(answer_a))
        self.play(Write(text_b))
        self.play(Write(answer_b))
        self.play(Write(text_c))
        self.play(Write(answer_c))
        self.play(Write(text_d))
        self.play(Write(answer_d))
        self.play(Write(text_e))
        self.play(Write(answer_e1), Write(answer_e2))
        self.wait(5)

    def Exercise2(self):
        # Define the colors for the headers and answers
        header_color = BLUE
        answer_color = YELLOW
        
        # Title text
        title = Text("Q. Which of the following things do you take in millilitres \n""and which in litres?", font_size=30, weight=BOLD,color=RED)
        title.shift(UP* 3)
        # Define the table data
        table_content = [
            ["Item", "Millilitres/ Litres"],
            ["Milk", "Litres"],
            ["Coconut oil", "Millilitres"],
            ["Cool drink", "Millilitres/Litres"],
            ["Shampoo", "Millilitres"],
            ["Medicine syrup", "Millilitres"]
        ]
        
        # Define cell dimensions
        cell_height = 1
        cell_width = 4
        
        # Calculate start position
        start_position = ORIGIN + UP * (len(table_content) * cell_height / 2)
        
        # Create the table with colored headers and answers
        table = VGroup(*[
            VGroup(*[
                Tex(content, color=header_color if j == 0 else answer_color if (i == 1 and j != 0) else WHITE).move_to(
                    start_position + np.array([i * cell_width, -j * cell_height, 0])
                )
                for i, content in enumerate(row)
            ])
            for j, row in enumerate(table_content)
        ])
        
        # Create horizontal lines
        h_lines = VGroup(*[
            Line(
                start=start_position + np.array([-cell_width / 2, -j * cell_height - cell_height / 2, 0]),
                end=start_position + np.array([(len(table_content[0])) * cell_width - cell_width / 2, -j * cell_height - cell_height / 2, 0])
            )
            for j in range(len(table_content) + 1)
        ])
        
        # Additional top horizontal line
        extra_h_line_top = Line(
            start=start_position + np.array([-cell_width / 2, cell_height / 2, 0]),
            end=start_position + np.array([(len(table_content[0])) * cell_width - cell_width / 2, cell_height / 2, 0])
        )
        
        # Create vertical lines
        v_lines = VGroup(*[
            Line(
                start=start_position + np.array([i * cell_width - cell_width / 2, cell_height / 2, 0]),
                end=start_position + np.array([i * cell_width - cell_width / 2, -(len(table_content)) * cell_height + cell_height / 2, 0])
            )
            for i in range(len(table_content[0]) + 1)
        ])
        
        # Combine table and lines
        table_with_lines = VGroup(table, h_lines, v_lines, extra_h_line_top)
        
        # Position adjustments
        table_with_lines.shift(LEFT * 2)
        table_with_lines.shift(DOWN * 1.5)
        
        # Animate the title and table
        self.play(Write(title))
        self.play(Create(table_with_lines))
        self.wait(5)

    def fillbottle(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("4 glasses of water","")
        p11=cvo.CVO().CreateCVO("To fill", "1 liter water bottle")
        p10.cvolist.append(p11)
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)

    def Example3(self):
        # Define the text
        question_text = (
            "Q. Dolly uses a bucket of water for having bath. She drinks\n"" about 8 glasses of water and uses 3 buckets of water for other\n"" purposes in a day. How many litres of water does Dolly\n"" need for the following:(1 liter is equal to 4 glasses of water.\n\n"
            "(a) having bath ________\n\n"
            "(b) drinking ________\n\n"
            "(c) for other purposes ________\n\n"
            "(d) How many litres of water does dolly need in a day? _____"
        )
        
        # Create the text object with red color
        question = Text(question_text, color=RED,font_size=35)
        
        # Display the text on the screen
        question.to_edge(UP)
        self.play(Write(question))
        self.wait(5)

    def answer(self):
        titles = [
            "(a) having bath:",
            "(b) drinking:",
            "(c) for other purposes:",
            "(d) How many litres of water does Dolly need in a day?"
        ]
        
        info_texts = [
            "Given:\n"
            "For bathing = 1 bucket\n"
            "So, 1 bucket = 10 litres\n\n"
            "Therefore, Dolly requires 10 litres of water to have bath.",
            
            "Given:\n"
            "For drinking = 8 glasses\n"
            "(1 litre is equal to 4 glasses of water)\n\n"
            "4 glasses of water = 1 litre\n"
            "8 glasses of water = 4 glasses of water + 4 glasses of water\n"
            "= 1 litre + 1 litre\n"
            "= 2 litres\n\n"
            "Therefore, Dolly requires 2 litres of water for drinking.",

            "Given:\n"
            "For other purposes = 3 buckets\n\n"
            "One bucket holds 10 litres of water.\n\n"
            "3 buckets = 10 x 3 = 30 litres\n\n"
            "Therefore, Dolly requires 30 litres of water for other purposes.",

            "So, from the above assumptions,\n"
            "Water used for bathing = 10 litres,\n"
            "water used for drinking = 2 litres and\n"
            "for other purposes = 30 litres\n\n"
            "Thus, the total amount of water she used in a day is\n"
            "10 litres + 2 litres + 30 litres = 42 litres\n\n"
            "Therefore, Dolly needs 42 litres of water in a day."
        ]

        # Create the text objects
        titles_text = [Text(title, color=RED).scale(0.8) for title in titles]
        infos_text = [Text(info).scale(0.6) for info in info_texts]
        
        # Position and display the titles and information on the screen
        for title, info in zip(titles_text, infos_text):
            title.move_to(UP * 3)
            info.move_to(DOWN * 0)

            self.play(Write(title))
            self.wait(1)
            self.play(Write(info))
            self.wait(2)
            
            # Fade out the title and info after displaying
            self.play(FadeOut(title), FadeOut(info))
            self.wait(1)
        
        # End the scene
        self.wait(2)


    def SetDeveloperList(self): 
       self.DeveloperList="Potluri Divya Reddy" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade4Chapter10Howmuchdothesebottleshold.py"

if __name__ == "__main__":
    scene = Howmuchdothesebottleshold()
    scene.render()