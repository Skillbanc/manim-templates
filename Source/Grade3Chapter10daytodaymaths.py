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

class daytodaymaths(AbstractAnim,ThreeDScene):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.intro()
        self.fadeOutCurrentScene()
        self.Example0()
        self.fadeOutCurrentScene()
        self.Example2()
        self.fadeOutCurrentScene()
        self.Example4()
        self.fadeOutCurrentScene()
        self.Example5()
        self.fadeOutCurrentScene()
        self.Example6()
        self.fadeOutCurrentScene()
        self.Example7()
        self.fadeOutCurrentScene()
        self.Example8()
        self.fadeOutCurrentScene()
        self.Example9()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        
    def intro(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("DAY-TO-DAY MATHS","")
        p11=cvo.CVO().CreateCVO("Addition","")
        p12=cvo.CVO().CreateCVO("Subtraction","")
        p13=cvo.CVO().CreateCVO("Multiplication","")
        p14=cvo.CVO().CreateCVO("Division","")
        p14.setcircleradius(1.25)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        self.setNumberOfCirclePositions(5)
        self.construct1(p10,p10)
    def Example0(self):
        title = Text("Math in daily life", font_size=36, weight=BOLD, color=YELLOW).to_edge(UP)
        self.play(Write(title))

        # Problem (A)
        problem_a = Text(
            "Q. (A) Prashant gets up at 7 AM. It takes him 5 minutes to\n"
            "walk to the bus stop. The school bus arrives at 7:50 AM.\n"
            " How much time does he have to get ready for school?\n",
            
            font_size=35,
            color=GREEN
        ).scale(0.8).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(problem_a, shift=DOWN))

        # Answer to Problem (A)
        wake_up_time = Text("Given,\n""Prashant gets up at 7 AM.", font_size=24, color=WHITE).next_to(problem_a, DOWN, aligned_edge=LEFT, buff=0.5)
        walk_to_bus_stop = Text("Time taken by Prashant to walk to the bus stop is 5 minutes.", font_size=24, color=WHITE).next_to(wake_up_time, DOWN, aligned_edge=LEFT)
        bus_arrival_time = Text("The time of arrival of school bus is 7:50 AM.", font_size=24, color=WHITE).next_to(walk_to_bus_stop, DOWN, aligned_edge=LEFT)
        time_to_get_ready = Text(
            "7 hours 50 minutes - 5 minutes = 7 hours 45 minutes.\n\n"
            "Since Prashant gets up at 7 AM, he needs 45 minutes to get ready for school.\n\n"
            "Hence, Prashant has 45 minutes to get ready for school.",
            font_size=24, color=WHITE
        ).next_to(bus_arrival_time, DOWN, aligned_edge=LEFT)

        self.play(Write(wake_up_time))
        self.wait(1)
        self.play(Write(walk_to_bus_stop))
        self.wait(1)
        self.play(Write(bus_arrival_time))
        self.wait(1)
        self.play(Write(time_to_get_ready))
        self.wait(3)

        self.play(FadeOut(problem_a), FadeOut(wake_up_time), FadeOut(walk_to_bus_stop), FadeOut(bus_arrival_time), FadeOut(time_to_get_ready))

        # Problem (B)
        problem_b = Text(
            "(B) Richa notices that there are equal number of seats\n"
            "on each side of the bus. She also notices that there are \n"
            "4 seats in each row.Richa counts 12 seats on each side.\n"
            "How many seats are there in each row? How many seats\n"
            "are there in all?",
            font_size=35,
            color=GREEN
        ).scale(0.8).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(problem_b, shift=DOWN))

        # Answer to Problem (B)
        seats_per_side = Text(" Given,\n""There are 4 seats in each row.", font_size=24, color=WHITE).next_to(problem_b, DOWN, aligned_edge=LEFT, buff=0.5)
        total_seats_per_side = Text("The number of seats on each side is 12.There are two sides inside the bus.\n\n", font_size=24, color=WHITE).next_to(seats_per_side, DOWN, aligned_edge=LEFT)
        total_seats = Text(
                           "So, the total number of seats is,\n\n"
                           "12 + 12 = 24.\n\n"
                           "Hence, there are 4 seats in each row and 24 seats inside the bus.", font_size=24, color=WHITE).next_to(total_seats_per_side, DOWN, aligned_edge=LEFT, buff=0.5)

        self.play(Write(seats_per_side))
        self.wait(1)
        self.play(Write(total_seats_per_side))
        self.wait(1)
        self.play(Write(total_seats))
        self.wait(3)

        self.play(FadeOut(problem_b), FadeOut(seats_per_side), FadeOut(total_seats_per_side), FadeOut(total_seats))

        # Problem (C)
        problem_c = Text(
            "(C) Ramesh has been selling bananas since morning.\n"
            "He had 320 bananas. By evening he has 54 left\n"
            "with him. How many bananas did Ramesh sell?",
            font_size=35,
            color=GREEN
        ).scale(0.8).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(problem_c, shift=DOWN))

        # Answer to Problem (C)
        bananas_in_morning = Text("Given,\n""The number of bananas with Ramesh in the morning = 320", font_size=24, color=WHITE).next_to(problem_c, DOWN, aligned_edge=LEFT, buff=0.5)
        bananas_left_evening = Text("The number of bananas left with him by evening = 54", font_size=24, color=WHITE).next_to(bananas_in_morning, DOWN, aligned_edge=LEFT)
        bananas_sold = Text(
            " 320 - 54 = 266 bananas were sold.\n\n"
            "Therefore, Ramesh sold 266 bananas.",
            font_size=24, color=WHITE
        ).next_to(bananas_left_evening, DOWN, aligned_edge=LEFT, buff=0.5)

        self.play(Write(bananas_in_morning))
        self.wait(1)
        self.play(Write(bananas_left_evening))
        self.wait(1)
        self.play(Write(bananas_sold))
        self.wait(3)

        self.play(FadeOut(problem_c), FadeOut(bananas_in_morning), FadeOut(bananas_left_evening), FadeOut(bananas_sold))

        # Problem (D)
        problem_d = Text(
            "(D) Sarojini takes 25 minutes for cooking rice, 20 minutes\n"
            "for cooking curry and 15 minutes for rasam. If she has\n"
            "to serve food at 8:00 o'clock, at what time should she\n"
            "enter the kitchen?",
            font_size=35,
            color=GREEN
        ).scale(0.8).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(problem_d, shift=DOWN))

        # Answer to Problem (D)
        time_to_cook_rice = Text("Given,\n""The time taken to cook rice = 25 minutes", font_size=24, color=WHITE).next_to(problem_d, DOWN, aligned_edge=LEFT, buff=0.5)
        time_to_cook_curry = Text("The time taken to cook curry = 20 minutes", font_size=24, color=WHITE).next_to(time_to_cook_rice, DOWN, aligned_edge=LEFT)
        time_to_cook_rasam = Text("The time taken to cook rasam = 15 minutes", font_size=24, color=WHITE).next_to(time_to_cook_curry, DOWN, aligned_edge=LEFT)
        total_cooking_time = Text(
            "The total time taken to cook = 25 minutes + 20 minutes + 15 minutes\n\n"
            "= 60 minutes = 1 hour\n\n"
            "She has to serve food at 8:00 o'clock.So,should enter the kitchen 1 hour i.e.\n\n"

            "8:00 - 1:00 = 7:00."
            "Hence, she should enter the kitchen at 7:00 o'clock.",
            font_size=24, color=WHITE
        ).next_to(time_to_cook_rasam, DOWN, aligned_edge=LEFT, buff=0.4)

        self.play(Write(time_to_cook_rice))
        self.wait(1)
        self.play(Write(time_to_cook_curry))
        self.wait(1)
        self.play(Write(time_to_cook_rasam))
        self.wait(1)
        self.play(Write(total_cooking_time))
        self.wait(3)

        self.play(FadeOut(problem_d), FadeOut(time_to_cook_rice), FadeOut(time_to_cook_curry), FadeOut(time_to_cook_rasam), FadeOut(total_cooking_time))

        self.wait(2)


    def Example2(self):
        # Given information
        clay_elephant = 5  # kg
        clay_cat = 3       # kg
        clay_rat = 1       # kg

        # Step-by-step calculations
        total_clay = clay_elephant + clay_cat + clay_rat

        # Create the text objects
        title_text = Text(
            "Making toys with clay",
            font_size=36,
            color=YELLOW  # Set the color of the title to yellow
        )

        question_text = Text(
            "Q. Sudheer wants to make a toy elephant, a toy cat, and a toy rat with clay.\n "
            "The elephant needs 5 kg clay, the cat needs 3 kg, and the rat needs 1 kg.\n "
            "How much clay is needed to make all the toys?\n",
            font_size=24,
            color=GREEN  # Set the color of the question to green
        )

        elephant_clay_text = Text(
            f"The amount of clay needed for elephant = {clay_elephant} kg",
            font_size=24
        )

        cat_clay_text = Text(
            f"The amount of clay needed for cat = {clay_cat} kg",
            font_size=24
        )

        rat_clay_text = Text(
            f"The amount of clay needed for rat = {clay_rat} kg",
            font_size=24
        )

        total_clay_breakdown_text = Text(
            f"The total amount of clay needed to make all the toys \n"
            f"{clay_elephant} kg + {clay_cat} kg + {clay_rat} kg = {total_clay} kg",
            font_size=24
        )

        # Position the text objects
        title_text.to_edge(UP)
        question_text.next_to(title_text, DOWN,buff=1)
        elephant_clay_text.next_to(question_text, DOWN,buff=0.5)
        cat_clay_text.next_to(elephant_clay_text, DOWN)
        rat_clay_text.next_to(cat_clay_text, DOWN)
        total_clay_breakdown_text.next_to(rat_clay_text, DOWN,buff=1)

        # Show the text sequentially
        self.play(Write(title_text))
        self.wait(1)
        self.play(Write(question_text))
        self.wait(2)
        self.play(Write(elephant_clay_text))
        self.wait(2)
        self.play(Write(cat_clay_text))
        self.wait(2)
        self.play(Write(rat_clay_text))
        self.wait(2)
        self.play(Write(total_clay_breakdown_text))
        self.wait(3)

    def Example4(self):
        # Title text
        title_text = Text(
            "Santosh's Classroom",
            font_size=36,
            color=YELLOW  # Set the color of the title to yellow
        )
        title_text.to_edge(UP)  # Position title at the top of the screen
        
        # Question text
        question_text = Text(
            "Q. Santosh is looking at the floor of his classroom. He is counting the number\n"
            "of tiles used for flooring. Can you help Santosh in counting the tiles?",
            font_size=24,
            color=GREEN  # Set the color of the question to green
        )
        question_text.next_to(title_text, DOWN, buff=0.5)  # Position question below title
        
        # Show the text sequentially
        self.play(Write(title_text))
        self.wait(1)
        self.play(Write(question_text))
        self.wait(1)

        # Define the grid dimensions and square size
        rows = 5
        cols = 5
        square_size = 0.9 # Smaller square size for a smaller grid
        
        # Define the specific colors for each position
        pattern = [
            [BLUE, RED, BLUE, RED, BLUE],
            [RED, BLUE, RED, BLUE, RED],
            [BLUE, RED, BLUE, RED, BLUE],
            [RED, BLUE, RED, BLUE, RED],
            [BLUE, RED, BLUE, RED, BLUE]
        ]
        
        # Loop to create the grid based on the defined pattern
        grid_group = VGroup()
        for i in range(rows):
            for j in range(cols):
                color = pattern[i][j]
                square = Square(side_length=square_size, fill_color=color, fill_opacity=1)
                square.move_to(np.array([j - cols / 2, rows / 2 - i, 0]) * square_size)
                grid_group.add(square)
        
        # Position the grid below the question text
        grid_group.next_to(question_text, DOWN, buff=0.5)

        # Row labels
        row_labels = VGroup()
        for i in range(rows):
            row_label = Text(f"{i+1}{'st' if i == 0 else 'nd' if i == 1 else 'rd' if i == 2 else 'th'} Row ->", font_size=24)
            row_label.next_to(grid_group, LEFT, buff=0.5).shift(UP * (rows/2 - i - 0.5) * square_size)
            row_labels.add(row_label)

        # Add the grid and row labels to the scene
        self.play(FadeIn(grid_group))
        self.play(FadeIn(row_labels))
        self.wait(3)

        # Fade out the current screen
        self.play(FadeOut(grid_group), FadeOut(row_labels), FadeOut(question_text), FadeOut(title_text))
        self.wait(1)

        # Questions and answers
        questions_and_answers = VGroup(
            VGroup(Text("(A) How many tiles are there in each row?", font_size=24, color=GREEN), Text("Each row has 5 tiles.", font_size=24, color=WHITE)).arrange(DOWN),
            VGroup(Text("(B) How many rows are there?", font_size=24, color=GREEN), Text("There are 5 rows.", font_size=24, color=WHITE)).arrange(DOWN),
            VGroup(Text("(C) What is the total number of tiles?", font_size=24, color=GREEN), Text("The total number of tiles is 25.", font_size=24, color=WHITE)).arrange(DOWN),
            VGroup(Text("(D) How many blue tiles are there?", font_size=24, color=GREEN), Text("There are 13 blue tiles.", font_size=24, color=WHITE)).arrange(DOWN),
            VGroup(Text("(E) How many red tiles are there?", font_size=24, color=GREEN), Text("There are 12 red tiles.", font_size=24, color=WHITE)).arrange(DOWN)
        ).arrange(DOWN, buff=0.5).to_edge(LEFT)
        
        # Display questions and answers
        self.play(Write(questions_and_answers))
        self.wait(3)

    def Example5(self):
        title = Text("Surya went to Village", font_size=36, weight=BOLD, color=YELLOW).to_edge(UP)
        self.play(Write(title))
        
        problem_statement = Text(
            "Q. Surya went to his grand father's village on bicycle.It took him 1 hour \n"
            "to reach the village.On return, he walked for 3 hours and reached home.\n "
            "What is the total time spent by Surya on travelling?",
            font_size=45,
            color=GREEN
        ).scale(0.6).next_to(title, DOWN, buff=0.5)
        
        self.play(FadeIn(problem_statement, shift=DOWN))
        
        table_header = Text("Distance", font_size=35, weight=BOLD).scale(0.7).to_edge(LEFT)
        table_header_time = Text("Time taken", font_size=35, weight=BOLD).scale(0.7).next_to(table_header, RIGHT*4, buff=2)
        
        self.play(Write(table_header), Write(table_header_time))
        
        distance_home_to_village = Text("Home to grand father's village:", font_size=35, color=GREEN).scale(0.6).next_to(table_header, DOWN, buff=0.5).align_to(table_header, LEFT)
        distance_return_home = Text("Return to home:", font_size=35, color=GREEN).scale(0.6).next_to(distance_home_to_village, DOWN, buff=0.5).align_to(distance_home_to_village, LEFT)
        distance_total_time = Text("Total time taken:", font_size=35, color=GREEN).scale(0.6).next_to(distance_return_home, DOWN, buff=0.5).align_to(distance_home_to_village, LEFT)
        extra_question = Text("If Surya walks on both sides then how \nmuch time will he take?", font_size=25, color=GREEN).next_to(distance_total_time, DOWN, buff=0.5).align_to(distance_total_time, LEFT)
        
        self.play(
            Write(distance_home_to_village),
            Write(distance_return_home),
            Write(distance_total_time),
            Write(extra_question)
        )
        
        time_home_to_village = Text("1 hour", font_size=35, color=YELLOW).scale(0.6).next_to(distance_home_to_village, RIGHT*2.3, buff=2.5)
        time_return_home = Text("3 hours", font_size=35, color=YELLOW).scale(0.6).next_to(distance_return_home, RIGHT*3, buff=2.5)
        time_total_time = Text("4 hours", font_size=35, color=YELLOW).scale(0.6).next_to(distance_total_time, RIGHT*3, buff=2.5)
        extra_answer = Text("6 hours (3 hours each way)", font_size=35, color=YELLOW).scale(0.6).next_to(extra_question, RIGHT*5.2, buff=0.5)
        
        self.play(
            Write(time_home_to_village),
            Write(time_return_home),
            Write(time_total_time),
            Write(extra_answer)
        )

    def Example6(self):
        title = Text("Shikha goes to her grandmother's village", font_size=36, weight=BOLD, color=YELLOW).to_edge(UP)
        self.play(Write(title))

        # Problem (A)
        problem_a = Text(
            "Q. (A) Shikha has to go to her grandmother's village. Her bus will leave at 9 AM. \n"
            "It will take 3 hours to reach the village. At what time will Shikha reach \n"
            "the village?",
            font_size=40,
            color=GREEN
        ).scale(0.6).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(problem_a, shift=DOWN))

        # Answer to Problem (A)
        answer_a_1 = Text("The leaving time of the bus = 9 AM", font_size=24, color=WHITE).next_to(problem_a, DOWN, buff=1)
        answer_a_2 = Text("The time taken to reach the village = 3 hours", font_size=24, color=WHITE).next_to(answer_a_1, DOWN, buff=0.3)
        answer_a_3 = Text("Now, Shikha will reach the village at", font_size=24, color=WHITE).next_to(answer_a_2, DOWN, buff=0.3)
        answer_a_4 = Text("9:00 + 3:00 = 12:00", font_size=24, color=WHITE).next_to(answer_a_3, DOWN, buff=0.3)
        self.play(Write(answer_a_1), Write(answer_a_2), Write(answer_a_3), Write(answer_a_4))
        self.wait(2)
        self.play(FadeOut(problem_a), FadeOut(answer_a_1), FadeOut(answer_a_2), FadeOut(answer_a_3), FadeOut(answer_a_4))

        # Problem (B)
        problem_b = Text(
            "(B) When Shikha reached the bus stand, she came to know that her \n""bus had been delayed by 2 hours.Now at what time will she reach the village?\n",
            font_size=40,
            color=GREEN
        ).scale(0.6).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(problem_b, shift=DOWN))

        # Answer to Problem (B)
        answer_b_1 = Text("Again, when Shikha reached the bus stand, she came to know", font_size=24, color=WHITE).next_to(problem_b, DOWN, buff=1)
        answer_b_2 = Text("that her bus had been delayed by 2 hours.", font_size=24, color=WHITE).next_to(answer_b_1, DOWN, buff=0.3)
        answer_b_3 = Text("Now, the time of Shikha to the village will be ", font_size=24, color=WHITE).next_to(answer_b_2, DOWN, buff=0.3)
        answer_b_4 = Text("12:00 + 2:00 = 2:00 = 2 hours = 2 PM", font_size=24, color=WHITE).next_to(answer_b_3, DOWN, buff=0.3)
        answer_b_5 = Text("Hence, the time taken to reach the village without any delay is 12:00", font_size=24, color=WHITE).next_to(answer_b_4, DOWN, buff=1)
        answer_b_6 = Text("and with delay of 2 hours is 2 PM.", font_size=24, color=WHITE).next_to(answer_b_5, DOWN, buff=0.3)
        self.play(Write(answer_b_1), Write(answer_b_2), Write(answer_b_3), Write(answer_b_4), Write(answer_b_5), Write(answer_b_6))
        self.wait(2)

    def Example7(self):
        title = Text("Seema prepares tea ", font_size=36, weight=BOLD, color=YELLOW).to_edge(UP)
        self.play(Write(title))

        # Problem statement
        problem_statement = Text(
            "Q. Seema prepares very good tea. She uses 2 spoons of sugar \n"
            "for a cup of tea. Today, four guests have come to her house. \n"
            "She had to prepare tea for her mother, father and the guests.",
            font_size=35,
            color=GREEN
        ).scale(0.8).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(problem_statement, shift=DOWN))

        # Answer to Problem (A)
        answer_a_title = Text("(A) How many cups of tea need to be prepared?", font_size=24, color=GREEN).next_to(problem_statement, DOWN, buff=1)
        answer_a_1 = MathTex(
            r"\text{The total number of people, for whom she needs to prepare the tea} \\",
            r"= \text{father + mother + 4 guests} = 6\\",
            
        ).scale(0.8).next_to(answer_a_title, DOWN)
        answer_a_2 = Text("So, she needs to prepare 6 cups of tea.", font_size=24, color=WHITE).next_to(answer_a_1, DOWN, buff=0.5)
        self.play(Write(answer_a_title), Write(answer_a_1))
        self.wait(2)
        self.play(Write(answer_a_2))
        self.wait(2)
        self.play(FadeOut(answer_a_title), FadeOut(answer_a_1), FadeOut(answer_a_2))

        # Problem (B)
        problem_b = Text(
            "(B) How many spoons of sugar would be needed?",
            font_size=24,
            color=GREEN
        ).next_to(problem_statement, DOWN, buff=1)
        self.play(FadeIn(problem_b, shift=DOWN))

        # Answer to Problem (B)
        answer_b_1 = Text("Seema uses 2 spoons of sugar for a cup of tea.", font_size=24, color=WHITE).next_to(problem_b, DOWN, buff=0.5)
        answer_b_2 = Text("The amount of sugar needed for 6 cups of tea ", font_size=24, color=WHITE).next_to(answer_b_1, DOWN, buff=0.5)
        answer_b_3 = MathTex(
            r"=2 \times 6 = 12 \text{ spoons}"
        ).scale(0.8).next_to(answer_b_2, DOWN, aligned_edge=LEFT)
        answer_b_4 = Text("Seema needs to prepare 6 cups of tea and she needs 12 spoons of sugar.", font_size=24, color=WHITE).next_to(answer_b_3, DOWN, buff=0.5)
        self.play(Write(answer_b_1))
        self.wait(1)
        self.play(Write(answer_b_2))
        self.wait(1)
        self.play(Write(answer_b_3))
        self.wait(2)
        self.play(Write(answer_b_4))
        self.wait(2)

        self.play(FadeOut(problem_statement), FadeOut(problem_b), FadeOut(answer_b_1), FadeOut(answer_b_2), FadeOut(answer_b_3), FadeOut(answer_b_4))

        self.wait(2)

    def Example8(self):
        title = Text("Riya washes clothes", font_size=36, weight=BOLD, color=YELLOW).to_edge(UP)
        self.play(Write(title))

        # Problem (A)
        problem_a = Text(
            "Q. (A) Harish and Kavita filled a tank with water in their house.\n"
            "Harish brought 27 litres\n"
            "Kavita brought 23 litres\n"
            "Capacity of the tank = ?",
            font_size=35,
            color=GREEN
        ).scale(0.8).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(problem_a, shift=DOWN))

        # Answer to Problem (A)
        answer_a_1 = MathTex(r"\text{Total water in the tank}: \text{Harish's water + Kavita's water} \\").scale(0.8).next_to(problem_a, DOWN, buff=1)
        answer_a_2 = MathTex(r"= 27 + 23 = 50 \text{ litres}").scale(0.8).next_to(answer_a_1,DOWN)
        answer_a_3 = Text("Therefore, the total capacity of the tank is 50 litres.", font_size=24, color=WHITE).next_to(answer_a_2, DOWN, buff=1)
        self.play(Write(answer_a_1))
        self.wait(1)
        self.play(Write(answer_a_2))
        self.wait(2)
        self.play(Write(answer_a_3))
        self.wait(2)
        self.play(FadeOut(problem_a), FadeOut(answer_a_1), FadeOut(answer_a_2), FadeOut(answer_a_3))

        # Problem (B)
        problem_b = Text(
            "(B) Riya used water from the tank to wash clothes.\n"
            "There is 37 litres of water remaining in the tank.\n"
            "How much water did she use?",
            font_size=35,
            color=GREEN
        ).scale(0.8).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(problem_b, shift=DOWN))

        # Answer to Problem (B)
        answer_b_1 = MathTex(
            r"\text{Total water initially} - \text{Water remaining} \\").scale(0.8).next_to(problem_b, DOWN, buff=1)
        answer_b_2 = MathTex(r"= 50 - 37 = 13 \text{ litres}").scale(0.8).next_to(answer_b_1,DOWN)
        answer_b_3 = Text("Therefore, Riya used 13 litres of water.", font_size=24, color=WHITE).next_to(answer_b_2, DOWN, buff=1)
        self.play(Write(answer_b_1))
        self.wait(1)
        self.play(Write(answer_b_2))
        self.wait(2)
        self.play(Write(answer_b_3))
        self.wait(2)

    def Example9(self):
        title = Text("Milk consumed in the hostel", font_size=36, weight=BOLD, color=YELLOW).to_edge(UP)
        self.play(Write(title))

        # Problem (A)
        problem_a = Text(
            "Q. (A) Students in a hostel consume 24 litres of milk daily.\n"
            "How much milk is consumed in the hostel in a week?",
            font_size=35,
            color=GREEN
        ).scale(0.8).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(problem_a, shift=DOWN))

        # Answer to Problem (A)
        daily_milk_consumption = 24  # litres
        days_in_week = 7
        milk_consumed_weekly = daily_milk_consumption * days_in_week

        answer_a_1 = MathTex(
            r"\text{Daily milk consumption}= 24 \text{ litres} \\",
            
        ).scale(0.8).next_to(problem_a, DOWN,buff=1)
        answer_a_2 = MathTex(
            r"\text{Weekly milk consumption} = 24 \times 7 = 168 \text{ litres} \\"
            
        ).scale(0.8).next_to(answer_a_1, DOWN,buff=1)
        self.play(Write(answer_a_1))
        self.wait(1)
        self.play(Write(answer_a_2))
        self.wait(2)
        self.play(FadeOut(problem_a), FadeOut(answer_a_1), FadeOut(answer_a_2))

        # Problem (B)
        problem_b = Text(
            "(B) If each student consumes 2 litres of milk in a week,\n"
            "how many students are there in the hostel?",
            font_size=35,
            color=GREEN
        ).scale(0.8).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(problem_b, shift=DOWN))

        # Answer to Problem (B)
        weekly_milk_per_student = 2  # litres
        total_weekly_milk_consumption = 168  # litres from part A
        number_of_students = total_weekly_milk_consumption / weekly_milk_per_student

        answer_b_1 = MathTex(
            r"\text{Weekly milk consumption per student} = 2 \text{ litres}\\",
            
        ).scale(0.8).next_to(problem_b, DOWN,buff=1)
        answer_b_2 = MathTex(
            r"\text{Number of students} = \frac{168}{2} = 84\\",
            
        ).scale(0.8).next_to(answer_b_1, DOWN,buff=1)
        self.play(Write(answer_b_1))
        self.wait(1)
        self.play(Write(answer_b_2))
        self.wait(2)

        self.play(FadeOut(problem_b), FadeOut(answer_b_1), FadeOut(answer_b_2))

        self.wait(2)

    def SetDeveloperList(self): 
       self.DeveloperList="Potluri Divya Reddy" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade3Chapter10daytodaymaths.py"      
        
if __name__ == "__main__":
    scene = daytodaymaths()
    scene.render()