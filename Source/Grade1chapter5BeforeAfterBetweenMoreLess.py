# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):
#   Sudhakar Moparthy
#   Rohit Vailla

from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo


class Grade1chapter5BeforeAfterBetweenMoreLess(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.Title()
        self.fadeOutCurrentScene()
        self.plant()
        self.fadeOutCurrentScene()
        self.cranes()
        self.fadeOutCurrentScene()
        self.balls()
        self.fadeOutCurrentScene()
        self.More()
        self.fadeOutCurrentScene()
        self.Less()
        self.fadeOutCurrentScene()
        self.counting()
        self.fadeOutCurrentScene()
        self.stob()
        self.fadeOutCurrentScene()
        self.btos()
        self.fadeOutCurrentScene()
        self.Next()
        self.fadeOutCurrentScene()
        self.middle()
        self.fadeOutCurrentScene()
        self.previous()
        self.fadeOutCurrentScene()
        self.Bigger()
        self.fadeOutCurrentScene()
        self.smaller()
        self.fadeOutCurrentScene()
        self.Biggeramoung3()
        self.fadeOutCurrentScene()
        self.G()
        self.fadeOutCurrentScene()
        self.s2b()
        self.fadeOutCurrentScene()
        self.b2s()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()







    def Title(self):
        # Title
        title = Tex("Before - After - Between - More - Less", font_size=70)
        self.play(Write(title))
        self.wait(4)
        self.play(Unwrite(title))
        self.wait(1.5)



    
    def plant(self):
    
        # Create flower pots
        # Create question text
        question = Text("Look at the pictures given below. How many flower pots are there?\n How many plants are there? Write your answer in the small blankboxes.", 
                        font_size=28, color=YELLOW).to_edge(UP*0.5)


        # Animations
        self.play(Write(question))
        self.wait(5)

        pots = VGroup(*[
            VGroup(
                Arc(angle=PI, start_angle=PI, radius=0.36, color=ORANGE, fill_opacity=1),
                Line([-0.3, 0, 0], [0.3, 0, 0], color=ORANGE)
            ).scale(0.9) for _ in range(5)
        ])
        pots.arrange(RIGHT, buff=0.2)
        pots.to_edge(UP*1.7 + LEFT, buff=1)

        # Create plants
        def create_plant():
            stem = Line(ORIGIN, UP * 0.8, color=GREEN)
            leaves = VGroup(
                Line(stem.get_top(), stem.get_top() + UP * 0.2 + LEFT * 0.2, color=GREEN),
                Line(stem.get_top(), stem.get_top() + UP * 0.2 + RIGHT * 0.2, color=GREEN)
            )
            return VGroup(stem, leaves)

        plants = VGroup(*[create_plant() for _ in range(3)])
        plants.arrange(RIGHT, buff=1.5)
        plants.next_to(pots, RIGHT, buff=1)

   

        # Create labels 
        pot_label = Text("5", font_size=29).next_to(pots, DOWN, buff=0.1)
        plant_label = Text("3", font_size=29).next_to(plants, DOWN, buff=0.1)

        # Create question text
        question_text = Text("As per the above picture, which are more and which are less - flower\npots or plants? Put for your answer.", 
                             font_size=28, color=BLUE).next_to(plants, DOWN *5.4, buff=0.1)

        # Create answer boxes
        answer_boxes = VGroup(*[Square(side_length=0.4, color=PURPLE) for _ in range(2)])
        answer_boxes[0:2].arrange(RIGHT, buff=2)
     
        answer_boxes.arrange(DOWN*4, buff=0.156)
        answer_boxes.next_to(question_text, DOWN, buff=1).to_edge(LEFT*5.9)

        # Create "more" and "less" labels above answer boxes
        more_less_labels = VGroup(
            Text("more", font_size=20),
            Text("less", font_size=20),
          
        )
        more_less_labels[0].next_to(answer_boxes[0], UP, buff=0.2)
        more_less_labels[1].next_to(answer_boxes[1], UP, buff=0.2)




          # Create answer boxes
        answer_boxes1 = VGroup(*[Square(side_length=0.4, color=PURPLE) for _ in range(2)])
        answer_boxes1[0:2].arrange(RIGHT, buff=2)
     
        answer_boxes1.arrange(DOWN*4, buff=0.156)
        answer_boxes1.next_to(question_text, DOWN, buff=1).to_edge(RIGHT*5.9)
        
        # Create "more" and "less" labels above answer boxes
        more_less_labels1 = VGroup(
            Text("more", font_size=20),
            Text("less", font_size=20),
          
        )
        more_less_labels1[0].next_to(answer_boxes1[0], UP, buff=0.2)
        more_less_labels1[1].next_to(answer_boxes1[1], UP, buff=0.2)
     
     

        # Create images
        pot_image = pots[0].copy().scale(2).next_to(answer_boxes[0], LEFT, buff=1)
        plant_image = create_plant().scale(1.5).next_to(answer_boxes1[0], LEFT, buff=1.5)

        # Create answer texts
        answer_texts = VGroup(
            Text("✓", font_size=30, color=GREEN),
            Text("", font_size=30),
            
        ).to_edge(LEFT*1)
        for text, box in zip(answer_texts, answer_boxes):
            text.move_to(box)

        answer_texts1 = VGroup(
            Text("", font_size=30, color=GREEN),
            Text("✓", font_size=30),
            
        ).to_edge(LEFT*1)
        for text1, box1 in zip(answer_texts1, answer_boxes1):
            text1.move_to(box1)

        # Animations
        self.play(Create(pots), Create(plants))
        self.play(Write(pot_label), Write(plant_label))
        self.play(Write(question_text))
        self.wait(4)
        self.play(Create(pot_image))        
        self.play(Create(answer_boxes), Write(more_less_labels))
        # self.play(Create(pot_image))
        self.play(Create(plant_image))
        self.play(Create(answer_boxes1), Write(more_less_labels1))        
        # self.play(Create(plant_image))
        self.wait(2)

        # Fill in the answer boxes and show answers
        self.play(
            answer_boxes[0].animate.set_fill(color=PURPLE, opacity=0.5),
           
            Write(answer_texts[0]),
           
        )

        self.wait(1.5)

        
        # Fill in the answer boxes and show answers
        self.play(
            answer_boxes1[1].animate.set_fill(color=PURPLE, opacity=0.5),
           
            Write(answer_texts1[1]),
           
        )

        self.wait(3.5)

    def cranes(self):
  
        # Create cranes
        def create_crane():
            
            smiley = Text("🦢", font_size=110)
            
           
            return VGroup(smiley)

        cranes = VGroup(*[create_crane() for _ in range(2)])
        cranes.arrange(DOWN, buff=0.5).scale(0.7).to_edge(LEFT, buff=2)

        # Create fish
        def create_fish():
            smile = Text("🐟", font_size=110,color=BLUE)
            
        
            return VGroup(smile)
        fish = VGroup(*[create_fish() for _ in range(2)])
        fish.arrange(DOWN, buff=0.5).scale(0.7).to_edge(RIGHT, buff=2)

        # Create arrows
        arrows = VGroup(*[DoubleArrow(start=cranes[i].get_right(), end=fish[i].get_left(), color=PINK) 
                          for i in range(2)])

        # Create answer boxes
        boxes = VGroup(*[Square(side_length=0.6, color=YELLOW) for _ in range(2)])
        boxes.arrange(RIGHT, buff=3).next_to(VGroup(cranes, fish), DOWN, buff=1)

        # Create question text
        question = Text("How many cranes are there and how many fishes are there? Are they\nin equal number?", 
                        font_size=33, color=ORANGE).to_edge(UP)


        # Animations
        self.play(Write(question))
        self.wait(5)
        self.play(Create(cranes), Create(fish))
        self.wait(2)
         # Add numbers
        crane_numbers = Text("Cranes", font_size=36,color=WHITE).next_to(boxes[0], DOWN*-0.9+LEFT*6.4)
        fish_numbers = Text("Fishes", font_size=36,color=BLUE).next_to(boxes[1], DOWN*-0.9+RIGHT*6.3)

        self.play(Write(crane_numbers), Write(fish_numbers))
        self.wait(3)
        self.play(Create(arrows))
        self.wait(2)
        self.play(Create(boxes))
        self.wait(2)





        # Add numbers
        crane_number = Text("2", font_size=39).next_to(boxes[0], DOWN*0)
        fish_number = Text("2", font_size=39).next_to(boxes[1], DOWN*0)

        self.play(Write(crane_number), Write(fish_number))
        self.wait(3)


        # Show equality
        equal_sign = Text("=", font_size=48).move_to((boxes[0].get_center() + boxes[1].get_center()) / 2)
        self.play(Write(equal_sign))

        self.wait(3)


    def balls(self):
             # Create question text
        question = Text("Look at the pictures given below. Count each set. Compare \nthe two sets, which has more or less or equal things.", font_size=32, color=WHITE).to_edge(UP*1)
        # Animations
        self.play(Write(question))
        self.wait(5)
        # Create the left set
        left_set = Circle(radius=1.8, color=WHITE)
        left_dots = VGroup(*[Sphere(color=ORANGE) for _ in range(3)]).scale(0.42)
        left_dots.arrange(DOWN, buff=0.5)
        left_group = VGroup(left_set, left_dots).shift(LEFT * 3)

        # Create the right set
        right_set = Circle(radius=1.8, color=WHITE)
        right_lines = VGroup(*[Line(start=ORIGIN, end=RIGHT, color=YELLOW) for _ in range(3)])
        right_lines.arrange(DOWN, buff=0.5).rotate(45 * DEGREES).scale(2)
        right_group = VGroup(right_set, right_lines).shift(RIGHT * 3)

        # Create arrows
        arrows = VGroup(*[
            Arrow(left_dots[i].get_center(), right_lines[i].get_start(), color=ORANGE)
            for i in range(3)
        ])

        # Create the "equal" text
        equal_text = Text("equal", color=WHITE).scale(0.8).next_to(arrows, DOWN)

        # Create a rectangle around everything
        surrounding_rect = SurroundingRectangle(VGroup(left_group, right_group, arrows, equal_text), color=PINK, buff=0.5)

        # Animations
        self.play(Create(surrounding_rect))
        self.play(Create(left_set), Create(right_set))
        self.play(Create(left_dots), Create(right_lines))
        # Add numbers
        crane_numbers = Text("Balls", font_size=36,color=BLUE).next_to(left_group, DOWN)
        fish_numbers = Text("Bats", font_size=36,color=YELLOW).next_to(right_group, DOWN)

        self.play(Write(crane_numbers), Write(fish_numbers))
        self.wait(3)

        self.play(Create(arrows))
        self.wait(3)
        self.play(Write(equal_text))
        self.wait(4)

    def Less(self):
             # Create question text
        question = Text("Look at the pictures given below. Count each set. Compare \nthe two sets, which has more or less or equal things.", font_size=32, color=WHITE).to_edge(UP*1)
        # Animations
        self.play(Write(question))
        self.wait(4)
        # Create the left set
        left_set = Circle(radius=1.8, color=WHITE)
        left_dots = VGroup(*[Sphere(color=ORANGE) for _ in range(3)]).scale(0.42)
        left_dots.arrange(DOWN, buff=0.5)
        left_group = VGroup(left_set, left_dots).shift(LEFT * 3)

        # Create the right set
        right_set = Circle(radius=1.8, color=WHITE)
        right_lines = VGroup(*[Line(start=ORIGIN, end=RIGHT, color=YELLOW) for _ in range(4)])
        right_lines.arrange(DOWN, buff=0.5).rotate(45 * DEGREES).scale(2)
        right_group = VGroup(right_set, right_lines).shift(RIGHT * 3)

        # Create arrows
        arrows = VGroup(*[
            Arrow(left_dots[i].get_center(), right_lines[i].get_start(), color=ORANGE)
            for i in range(3)
        ])

        # Create the "equal" text
        equal_text = Text("Less Balls", color=WHITE).scale(0.8).next_to(arrows, DOWN)

        # Create a rectangle around everything
        surrounding_rect = SurroundingRectangle(VGroup(left_group, right_group, arrows, equal_text), color=PINK, buff=0.5)

        # Animations
        self.play(Create(surrounding_rect))
        self.play(Create(left_set), Create(right_set))
        self.play(Create(left_dots), Create(right_lines))
        # Add numbers
        crane_numbers = Text("Balls", font_size=36,color=BLUE).next_to(left_group, DOWN)
        fish_numbers = Text("Bats", font_size=36,color=YELLOW).next_to(right_group, DOWN)

        self.play(Write(crane_numbers), Write(fish_numbers))
        self.wait(2)

        self.play(Create(arrows))
        self.wait(2)
        self.play(Write(equal_text))
        self.wait(4)







    def More(self):
             # Create question text
        question = Text("Look at the pictures given below. Count each set. Compare \nthe two sets, which has more or less or equal things.", font_size=32, color=WHITE).to_edge(UP*1)
        # Animations
        self.play(Write(question))
        self.wait(4)
        # Create the left set
        left_set = Circle(radius=1.8, color=WHITE)
        left_dots = VGroup(*[Sphere(color=ORANGE) for _ in range(4)]).scale(0.3)
        left_dots.arrange(DOWN, buff=0.3)
        left_group = VGroup(left_set, left_dots).shift(LEFT * 3)

        # Create the right set
        right_set = Circle(radius=1.8, color=WHITE)
        right_lines = VGroup(*[Line(start=ORIGIN, end=RIGHT, color=YELLOW) for _ in range(3)])
        right_lines.arrange(DOWN, buff=0.5).rotate(45 * DEGREES).scale(2)
        right_group = VGroup(right_set, right_lines).shift(RIGHT * 3)

        # Create arrows
        arrows = VGroup(*[
            Arrow(left_dots[i].get_center(), right_lines[i].get_start(), color=ORANGE)
            for i in range(3)
        ])

        # Create the "equal" text
        equal_text = Text("More Balls", color=WHITE).scale(0.7).next_to(arrows, DOWN)

        # Create a rectangle around everything
        surrounding_rect = SurroundingRectangle(VGroup(left_group, right_group, arrows, equal_text), color=PINK, buff=0.5)

        # Animations
        self.play(Create(surrounding_rect))
        self.play(Create(left_set), Create(right_set))
        self.play(Create(left_dots), Create(right_lines))
        # Add numbers
        crane_numbers = Text("Balls", font_size=36,color=BLUE).next_to(left_group, DOWN)
        fish_numbers = Text("Bats", font_size=36,color=YELLOW).next_to(right_group, DOWN)

        self.play(Write(crane_numbers), Write(fish_numbers))
        self.wait(3)

        self.play(Create(arrows))
        self.wait(2)
        self.play(Write(equal_text))
        self.wait(4)







    def stob(self):


         # Table data for the repeated addition and multiplication table of 5
        title_text = "From the small number to the big numbers"
         # Title text
        title = Text(title_text, color=YELLOW,fill_opacity=7).scale(1).to_edge(UP*1.5)
        # Add title to scene
        self.play(Write(title))
        self.wait(3)
        # Create the squares
        squares = VGroup(*[
            VGroup(*[Square(side_length=0.72, fill_opacity=2, fill_color=BLUE) for _ in range(i)])
            for i in range(1, 10)
        ])

        # Position the squares
        for i, row in enumerate(squares):
            row.arrange(RIGHT, buff=0)
            row.move_to(LEFT * 3 + DOWN * (4 - i * 0.5))
        squares.to_edge(LEFT* -7+DOWN*2)

        # Create the arrow
        arrow = Arrow(squares[0].get_center(), squares[-1].get_right(), color=PINK)

        # Create the numbers
        numbers = VGroup(*[
            Text(str(i), font_size=34).next_to(row, LEFT)
            for i, row in enumerate(squares, start=1)
        ])

        # Animation
        self.play(Create(squares[0]))
        self.play(Write(numbers[0]))

        for i in range(1, len(squares)):
            self.play(
                Transform(squares[i-1].copy(), squares[i]),
                Write(numbers[i])
            )
        self.wait(3)
        self.play(Create(arrow))

        self.wait(5)







    def btos(self):


# Table data for the repeated addition and multiplication table of 5
        title_text = "From the big number to the small numbers"
         # Title text
        title = Text(title_text, color=YELLOW,fill_opacity=7).scale(1).to_edge(UP*1.5)
        # Add title to scene
        self.play(Write(title))
        self.wait(3)


        # Create the squares
        squares = VGroup(*[
            VGroup(*[Square(side_length=0.74, fill_opacity=2, fill_color=BLUE) for _ in range(i)])
            for i in range(1, 10)
        ])

        # Position the squares
        for i, row in enumerate(squares):
            row.arrange(RIGHT, buff=0)
            row.move_to(LEFT * 3 + DOWN * (4 - i * 0.5))
        squares.to_edge(LEFT* -7+DOWN*2).rotate(160.19999)

        # Create the arrow
        arrow = Arrow(squares[-1].get_right(), squares[0].get_right(), color=PINK)

        # Create the numbers
        numbers = VGroup(*[
            Text(str(i), font_size=31).next_to(row, LEFT*0.7+UP*0.00001)
            for i, row in enumerate(squares, start=1)
        ])

        # # Animation
        # self.play(Create(squares[0]))
        # self.play(Write(numbers[9]))
        # self.play(Create(squares[8])) 
        for i in range(len(squares) - 1, 0, -1):
         self.play(
            Transform(squares[i], squares[i-1].copy()),
            Write(numbers[i])
        )
              
        self.play(Write(numbers[0]))         





        self.play(Create(arrow))

        self.wait(5)



###
    def G(self):


        title = Text("There are 3 numbers in each row, Circle the least number.", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(3)
        rows = [
            ["Example:", "2", "3", "4"],
            ["    (a)  \t   ", "7", "5", "2"],
            ["    (b)  \t   ", "9", "2", "7"],
            ["    (c)   \t  ", "6", "3", "5"],
            ["    (d)  \t   ", "4", "1", "8"],
            ["    (e)  \t   ", "3", "7", "5"]
        ]

        table = VGroup()
        for i, row in enumerate(rows):
            row_group = VGroup()
            for j, item in enumerate(row):
                if j == 0:
                    cell = Text(item, font_size=24)
                else:
                    cell = Square(side_length=0.6, color=PINK, fill_opacity=0.2)
                    number = Text(item, font_size=24)
                    cell.add(number)
                row_group.add(cell)
            row_group.arrange(RIGHT, buff=0.5)
            table.add(row_group)

        table.arrange(DOWN, buff=0.5)
        table.next_to(title, DOWN, buff=0.5)

        self.play(Create(table))
        self.wait(3)

        # Highlight the least numbers
        circles = []
        for i, row in enumerate(rows):
            if i == 0:  # Example row
                circle = Circle(radius=0.35, color=BLUE)
                circle.move_to(table[i][1])
                circles.append(circle)
            else:
                min_value = min(int(x) for x in row[1:])
                min_index = row.index(str(min_value))
                circle = Circle(radius=0.35, color=BLUE)
                circle.move_to(table[i][min_index])
                circles.append(circle)

        for circle in circles:
            self.play(Create(circle))

        self.wait(4)


    def s2b(self):
        title = Text("Observe the given numbers and write them from the \nsmallest to the biggest in the given boxes.", font_size=32, color=BLUE)
        title.to_edge(UP*0.3)
        self.play(Write(title))
        self.wait(4)

        rows = [
            ["Example:", "4", "6", "3", "3", "4", "6"],
            ["(a)", "5", "8", "6", "", "", ""],
            ["(b)", "3", "7", "4", "", "", ""],
            ["(c)", "6", "9", "7", "", "", ""],
            ["(d)", "2", "6", "4", "", "", ""],
            ["(e)", "2", "1", "3", "", "", ""],
            ["(f)", "7", "4", "9", "", "", ""]
        ]

        table = VGroup()
        for i, row in enumerate(rows):
            row_group = VGroup()
            for j, item in enumerate(row):
                if j == 0:
                    cell = Text(item, font_size=24)
                elif j < 4:
                    cell = Text(item, font_size=24)
                else:
                    cell = Square(side_length=0.6, color=YELLOW, fill_opacity=0.1)
                    if item:
                        number = Text(item, font_size=24)
                        cell.add(number)
                row_group.add(cell)
            row_group.arrange(RIGHT, buff=0.5)
            if i > 0:
                arrow = Arrow(LEFT, RIGHT, color=PURPLE)
                arrow.next_to(row_group[3], RIGHT, buff=0.2)
             #   row_group.add(arrow)
            table.add(row_group)

        table.arrange(DOWN, buff=0.3)
        table.next_to(title, DOWN, buff=0.5)

        self.play(Create(table))
        self.wait(3)

        # Animate sorting and filling the boxes
        for i, row in enumerate(rows[1:], start=1):
            numbers = [int(x) for x in row[1:4]]
            sorted_numbers = sorted(numbers)
            for j, num in enumerate(sorted_numbers):
                target_box = table[i][j+4]
                moving_number = Text(str(num), font_size=24, color=WHITE)
                moving_number.move_to(table[i][numbers.index(num)+1])
                self.play(
                #    TransformFromCopy(table[i][numbers.index(num)+1], moving_number),
                    moving_number.animate.move_to(target_box)
                )
                # self.remove(moving_number)
                #target_box.become(Square(side_length=0.6, color=BLUE, fill_opacity=0.1).add(Text(str(num), font_size=24)))

        self.wait(4)



    def b2s(self):
        title = Text("Observe the given numbers and write them from\n the biggest to the smallest",color=YELLOW).scale(0.7)
        title.to_edge(UP*0.3)
        self.add(title)

        examples = [
            ("Example:", [4, 6, 5]),
            ("(a)", [3, 5, 2]),
            ("(b)", [6, 8, 5]),
            ("(c)", [7, 9, 6]),
            ("(d)", [4, 8, 7]),
            ("(e)", [5, 6, 8]),
            ("(f)", [7, 8, 9])
        ]

        for i, (label, numbers) in enumerate(examples):
            self.show_example(label, numbers, i)
            self.wait(1)

        self.wait(2)

    def show_example(self, label, numbers, index):
        label_text = Text(label).scale(0.6).to_edge(LEFT*3+UP*1.8)
        label_text.shift(DOWN * (index * 0.8 + 1))
        self.play(Write(label_text))

        number_mobjects = [Text(str(n)).scale(0.6) for n in numbers]
        number_group = VGroup(*number_mobjects).arrange(RIGHT, buff=0.3)
        number_group.next_to(label_text, RIGHT, buff=0.5)

        self.play(Write(number_group))

        arrow = Arrow(LEFT, RIGHT, max_tip_length_to_length_ratio=0.1).scale(0.5)
        arrow.next_to(number_group, RIGHT)
        self.play(GrowArrow(arrow))

        sorted_numbers = sorted(numbers, reverse=True)
        boxes = VGroup(*[Square(side_length=0.6).set_stroke(BLUE) for _ in range(3)])
        boxes.arrange(RIGHT, buff=0.3)
        boxes.next_to(arrow, RIGHT)

        self.play(Create(boxes))

        for i, n in enumerate(sorted_numbers):
            sorted_num = Text(str(n)).scale(0.6).move_to(boxes[i].get_center())
            self.play(Write(sorted_num))
        self.wait(3)



    def Next(self):

        # Create title
        title = Text("Write the next number in the Box and circle it.", color=PINK).to_edge(UP)
        self.play(Write(title))
        self.wait(3)

        # Create example
        example_text = Text("Example:", color=RED).scale(0.7).next_to(title, DOWN).to_edge(LEFT)
        self.play(Write(example_text))

        # Function to create a row of squares with a circle
        def create_row(numbers, highlight_index=None):
            row = VGroup()
            for i, num in enumerate(numbers):
                square = Square(side_length=0.6)
                if i == highlight_index:
                    circle = Circle(radius=0.3, color=BLUE).move_to(square.get_center())
                    number = Text(str(num), color=BLACK).scale(0.6).move_to(circle.get_center())
                    row.add(VGroup(square, circle, number))
                else:
                    number = Text(str(num), color=BLACK).scale(0.6).move_to(square.get_center())
                    row.add(VGroup(square, number))
            row.arrange(RIGHT, buff=0.1)
            return row

        # Create example row
        example_row = create_row([])
        example_row.next_to(example_text, RIGHT)
        self.play(Create(example_row))

        # Create question rows
        questions = [[1,2],
            [3, 4],
            [5, 6],
            [7, 8],
            [9, 10],
            [11, 12],
            [13,14],
        ]

        rows = VGroup()
        for nums in questions:
            row = create_row(nums)
            rows.add(row)

        rows.arrange(DOWN, buff=0.3).next_to(title, DOWN, buff=0.5)
        self.play(Create(rows))
        self.wait(2.5)

                # Animate answers
        for i, row in enumerate(rows):
            circle = Circle(radius=0.2, color=BLACK).move_to(row[0].get_center())
            number = Text(str(questions[i][0]), color=WHITE).scale(0.6).move_to(circle.get_center())
            self.play(
                Create(circle),
                Write(number),
                run_time=0.1
            )

        # Final pause
        self.wait(3)

        # Animate answers
        for i, row in enumerate(rows):
            circle = Circle(radius=0.3, color=BLUE).move_to(row[1].get_center())
            number = Text(str(questions[i][1]), color=WHITE).scale(0.6).move_to(circle.get_center())
            self.play(
                Create(circle),
                Write(number),
                run_time=1.2
            )

        # Final pause
        self.wait(5)






    def middle(self):

        # Create title
        title = Text("Write the middle number in the Box and circle it.", color=BLUE,font_size=41).to_edge(UP)
        self.play(Write(title))
        self.wait(3)

        # Create example
        example_text = Text("Example:", color=BLACK).scale(0.7).next_to(title, DOWN).to_edge(LEFT)
        self.add(example_text)

        # Function to create a row of squares with a circle
        def create_row(numbers, highlight_index=None):
            row = VGroup()
            for i, num in enumerate(numbers):
                square = Square(side_length=0.6)
                if i == highlight_index:
                    circle = Circle(radius=0.3, color=YELLOW).move_to(square.get_center())
                    number = Text(str(num), color=BLACK).scale(0.6).move_to(circle.get_center())
                    row.add(VGroup(square, circle, number))
                else:
                    number = Text(str(num), color=BLACK).scale(0.6).move_to(square.get_center())
                    row.add(VGroup(square, number))
            row.arrange(RIGHT, buff=0.1)
            return row

        # Create example row
        example_row = create_row([])
        example_row.next_to(example_text, RIGHT)
        self.play(Create(example_row))

        # Create question rows
        questions = [[1,2,3],
            [4, 5, 6],
            [7, 8, 9],
            [10, 11, 12],
            [13, 14, 15],
            [16,17,18],
            [19,20,21] 
        ]

        rows = VGroup()
        for nums in questions:
            row = create_row(nums)
            rows.add(row)

        rows.arrange(DOWN, buff=0.3).next_to(title, DOWN, buff=0.5)
        self.play(Create(rows))
        self.wait(2)

        # Animate answers
        for i, row in enumerate(rows):
            circle = Circle(radius=0.2, color=BLACK).move_to(row[0].get_center())
            number = Text(str(questions[i][0]), color=WHITE).scale(0.6).move_to(circle.get_center())
            self.play(
                Create(circle),
                Write(number),
                run_time=0.1
            )


               # Animate answers
        for i, row in enumerate(rows):
            circle = Circle(radius=0.2, color=BLACK).move_to(row[2].get_center())
            number = Text(str(questions[i][2]), color=WHITE).scale(0.6).move_to(circle.get_center())
            self.play(
                Create(circle),
                Write(number),
                run_time=0.1
            )

        # Final pause
        self.wait(4)




        # Animate answers
        for i, row in enumerate(rows):
            circle = Circle(radius=0.3, color=YELLOW).move_to(row[1].get_center())
            number = Text(str(questions[i][1]), color=WHITE).scale(0.6).move_to(circle.get_center())
            self.play(
                Create(circle),
                Write(number),
                run_time=1.2
            )

        # Final pause
        self.wait(5)




    def previous(self):

        # Create title
        title = Text("Write the previous number in the Box and circle it.", color=BLUE,font_size=41).to_edge(UP)
        self.play(Write(title))
        self.wait(3)

        # Create example
        example_text = Text("Example:", color=RED).scale(0.7).next_to(title, DOWN).to_edge(LEFT)
        self.play(Write(example_text))

        # Function to create a row of squares with a circle
        def create_row(numbers, highlight_index=None):
            row = VGroup()
            for i, num in enumerate(numbers):
                square = Square(side_length=0.6)
                if i == highlight_index:
                    circle = Circle(radius=0.3, color=BLUE).move_to(square.get_center())
                    number = Text(str(num), color=BLACK).scale(0.6).move_to(circle.get_center())
                    row.add(VGroup(square, circle, number))
                else:
                    number = Text(str(num), color=BLACK).scale(0.6).move_to(square.get_center())
                    row.add(VGroup(square, number))
            row.arrange(RIGHT, buff=0.1)
            return row

        # Create example row
        example_row = create_row([])
        example_row.next_to(example_text, RIGHT)
        self.play(Create(example_row))

        # Create question rows
        questions = [[1,2],
            [3, 4],
            [5, 6],
            [7, 8],
            [9, 10],
            [11, 12],
            [13,14],
        ]

        rows = VGroup()
        for nums in questions:
            row = create_row(nums)
            rows.add(row)

        rows.arrange(DOWN, buff=0.3).next_to(title, DOWN, buff=0.5)
        self.play(Create(rows))
        self.wait(2)

       

        # Animate answers
        for i, row in enumerate(rows):
            circle = Circle(radius=0.2, color=BLACK).move_to(row[1].get_center())
            number = Text(str(questions[i][1]), color=WHITE).scale(0.6).move_to(circle.get_center())
            self.play(
                Create(circle),
                Write(number),
                run_time=0.1
            )

        # Final pause
        self.wait(4)

         # Animate answers
        for i, row in enumerate(rows):
            circle = Circle(radius=0.3, color=YELLOW).move_to(row[0].get_center())
            number = Text(str(questions[i][0]), color=WHITE).scale(0.6).move_to(circle.get_center())
            self.play(
                Create(circle),
                Write(number),
                run_time=1.2
            )

        # Final pause
        self.wait(6)

###

    def smaller(self):
        # Create title


        title = Text("Circle round the smaller of the two numbers given below", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(3)

        rows = [
            ["    (a)", "2", "3"],
            ["    (b)  \t   ", "7", "2"],
            ["    (c)  \t   ", "9", "7"],
            ["    (d)   \t  ", "6",  "5"],
            ["    (e)  \t   ",  "1", "8"],
            ["    (f)  \t   ", "3", "5"],
        

        ]

        table = VGroup()
        for i, row in enumerate(rows):
            row_group = VGroup()
            for j, item in enumerate(row):
                if j == 0:
                    cell = Text(item, font_size=24)
                else:
                    cell = Square(side_length=0.62, color=PINK, fill_opacity=0.2)
                    number = Text(item, font_size=24)
                    cell.add(number)
                row_group.add(cell)
            row_group.arrange(RIGHT, buff=0.5)
            table.add(row_group)

        table.arrange(DOWN, buff=0.4)
        table.next_to(title, DOWN, buff=0.5)

        self.play(Create(table))
        self.wait(4)

        # Highlight the least numbers
        circles = []
        for i, row in enumerate(rows):
            if i == 0:  # Example row
                circle = Circle(radius=0.36, color=YELLOW)
                circle.move_to(table[i][1])
                circles.append(circle)
            else:
                min_value = min(int(x) for x in row[1:])
                min_index = row.index(str(min_value))
                circle = Circle(radius=0.35, color=YELLOW)
                circle.move_to(table[i][min_index])
                circles.append(circle)

        for circle in circles:
            self.play(Create(circle))

        self.wait(5)


    def Bigger(self):
        # Create title


        title = Text("Circle the bigger of the two numbers given below.", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(3)

        rows = [
            ["    (a)", "3", "2"],
            ["    (b)  \t   ", "7", "2"],
            ["    (c)  \t   ", "9", "7"],
            ["    (d)   \t  ", "6",  "5"],
            ["    (e)  \t   ",  "1", "8"],
            ["    (f)  \t   ", "3", "5"],


        ]

        table = VGroup()
        for i, row in enumerate(rows):
            row_group = VGroup()
            for j, item in enumerate(row):
                if j == 0:
                    cell = Text(item, font_size=24)
                else:
                    cell = Square(side_length=0.7, color=YELLOW, fill_opacity=0.2)
                    number = Text(item, font_size=27)
                    cell.add(number)
                row_group.add(cell)
            row_group.arrange(RIGHT, buff=0.2)
            table.add(row_group)

        table.arrange(DOWN, buff=0.4)
        table.next_to(title, DOWN, buff=0.5)

        self.play(Create(table))
        self.wait(4)

        # Highlight the least numbers
        circles = []
        for i, row in enumerate(rows):
            if i == 0:  # Example row
                circle = Circle(radius=0.35, color=BLUE)
                circle.move_to(table[i][1])
                circles.append(circle)
            else:
                min_value = max(int(x) for x in row[1:])
                min_index = row.index(str(min_value))
                circle = Circle(radius=0.35, color=BLUE)
                circle.move_to(table[i][min_index])
                circles.append(circle)

        for circle in circles:
            self.play(Create(circle))

        self.wait(4)

    def Biggeramoung3(self):
        # Create title


        title = Text("Circle the biggest of the 3 numbers given below.", font_size=36,color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(3)

        rows = [
            ["    (a)", "6", "3","1"],
            ["    (b)  \t   ", "9", "2","5"],
            ["    (c)  \t   ", "9", "1","10"],
            ["    (d)   \t  ", "16",  "5","12"],
            ["    (e)  \t   ",  "19", "81","12"],
            ["    (f)  \t   ", "3", "5","25"],


        ]

        table = VGroup()
        for i, row in enumerate(rows):
            row_group = VGroup()
            for j, item in enumerate(row):
                if j == 0:
                    cell = Text(item, font_size=24)
                else:
                    cell = Square(side_length=0.7, color=BLUE, fill_opacity=0.2)
                    number = Text(item, font_size=27)
                    cell.add(number)
                row_group.add(cell)
            row_group.arrange(RIGHT, buff=0.2)
            table.add(row_group)

        table.arrange(DOWN, buff=0.4)
        table.next_to(title, DOWN, buff=0.5)

        self.play(Create(table))
        self.wait(4)

        # Highlight the least numbers
        circles = []
        for i, row in enumerate(rows):
            if i == 0:  # Example row
                circle = Circle(radius=0.35, color=ORANGE)
                circle.move_to(table[i][1])
                circles.append(circle)
            else:
                min_value = max(int(x) for x in row[1:])
                min_index = row.index(str(min_value))
                circle = Circle(radius=0.35, color=ORANGE)
                circle.move_to(table[i][min_index])
                circles.append(circle)

        for circle in circles:
            self.play(Create(circle))

        self.wait(5)

        
    def counting(self):
        self.camera.background_color = BLACK
        title = Text("Count the pictures", color=WHITE).scale(0.8).to_edge(UP)
        instruction = Text("Write their number in the blank box near the pictures.", color=WHITE, font_size=27).next_to(title, DOWN)
        
        self.play(Write(title), Write(instruction))
        self.wait(3)
        
        # Function to create a group of objects
        def create_group(shape, count, color, scale_factor=0.22):
            group = VGroup(*[shape(color=color, fill_opacity=1) for _ in range(count)])
            rows = (count + 2) // 3  # Calculate rows dynamically
            cols = min(count, 3)     # Max 3 columns
            group.arrange_in_grid(rows=rows, cols=cols, buff=0.5)
            return group.scale(scale_factor)
        
        # Function to create a row of the exercise
        def create_row(left_shape, left_count, right_shape, right_count, color, row_label):
            left_group = create_group(left_shape, left_count, color)
            right_group = create_group(right_shape, right_count, color)
            row = VGroup(left_group, right_group).arrange(RIGHT, buff=0.5)
            
            boxes = VGroup(Square(side_length=0.43, color=BLUE), Square(side_length=0.43, color=BLUE))
            boxes[0].next_to(left_group, DOWN)
            boxes[1].next_to(right_group, DOWN)
            
            label = Text(row_label, color=WHITE, font_size=24).next_to(row, LEFT)
            
            return VGroup(row, boxes, label)
        
        # Create rows
        biscuit_row = create_row(Rectangle, 5, Rectangle, 3, ORANGE, "EXAMPLE     (a)")
        cherry_row = create_row(Circle, 7, Circle, 8, RED, "(b)")
        mango_row = create_row(Triangle, 2, Triangle, 3, YELLOW, "(c)")
        
        
        # Arrange rows
        exercise = VGroup(biscuit_row, cherry_row, mango_row).arrange(DOWN, buff=0.7).scale(0.7).shift(DOWN*1)
        
        # Animate creation of rows
        for row in exercise:
            self.play(Create(row))
            self.wait(3)
        
        # Function to count and fill answer
        def fill_answer(row, left_count, right_count):
            left_box, right_box = row[1]  # Get the answer boxes
            left_answer = Text(str(left_count), color=WHITE).scale(0.5).move_to(left_box)
            right_answer = Text(str(right_count), color=WHITE).scale(0.5).move_to(right_box)
            
            self.play(
                Write(left_answer),
                Write(right_answer)
            )
        
        # Fill answers
        self.wait(3)
        fill_answer(biscuit_row, 5, 3)
        fill_answer(cherry_row, 7, 8)
        fill_answer(mango_row, 2, 3)
       
        
        self.wait(5)

        
    def SetDeveloperList(self):
        self.DeveloperList = "Uday Kiran"   

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade1chapter5Before-After-Between-More-Less.py"      




if __name__ == "__main__":
    scene = Grade1chapter5BeforeAfterBetweenMoreLess()
    scene.render()