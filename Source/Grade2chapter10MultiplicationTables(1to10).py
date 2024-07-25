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


class Grade2chapter10MultiplicationTables1to10(AbstractAnim):
    
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.Title()
        self.fadeOutCurrentScene()
        self.t1()
        self.fadeOutCurrentScene()
        self.Fivetable()
        self.fadeOutCurrentScene()
        self.Two()
        self.fadeOutCurrentScene()
        self.Three()
        self.fadeOutCurrentScene()
        self.FOUR()
        self.fadeOutCurrentScene()
        self.SIX()
        self.fadeOutCurrentScene()
        self.SEVEN()
        self.fadeOutCurrentScene()
        self.eight()
        self.fadeOutCurrentScene()
        self.NINE()
        self.fadeOutCurrentScene()
        self.Flower()
        self.fadeOutCurrentScene()
        self.multizero()
        self.fadeOutCurrentScene()
        self.ENTIRETABLES()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

    def Title(self):
        # Title
        title = Text("Multiplication Tables (1 to 10) ", font_size=70)
        self.play(Write(title))
        self.wait(4)
        self.play(Unwrite(title))
        self.wait(2)



    def  t1(self):
         # Table data for the repeated addition and multiplication table of 5
        title_text = "Look at the repeated addition of 10 and the Multiplication Table of 10."
         # Title text
        title = Text(title_text, color=BLUE,fill_opacity=7).scale(0.6).to_edge(UP*0.4)
        # Add title to scene
        self.play(Write(title))
        self.wait(3)

        background = Rectangle(height=6.5, width=12.8)
        background.set_fill(opacity=.45)
        background.set_color([TEAL, RED, YELLOW])
        self.add(background)

        title = Text("10", color=WHITE,fill_opacity=0.3).scale(6)
        # Add title to scene
        self.play(Write(title))
        self.wait(2)


        table_data = [
         #  ["Number of chains", "A person counted the beads in the chains and \nwrote the numbers as shown below."],
            ["1", "10", "1 ten", "1 x 10 = 10"],
            ["2", "10 + 10", "2 tens", "2 x 10 = 20"],
            ["3", "10 + 10 + 10", "3 tens", "3 x 10 = 30"],
            ["4", "10 + 10 + 10 + 10", "4 tens", "4 x 10 = 40"],
            ["5", "10 + 10 + 10 + 10 + 10", "5 tens", "5 x 10 = 50"],
            ["6", "10 + 10 + 10 + 10 + 10 + 10", "6 tens", "6 x 10 = 60"],
            ["7", "10 + 10 + 10 + 10 + 10 + 10 + 10", "7 tens", "7 x 10 = 70"],
            ["8", "10 + 10 + 10 + 10 + 10 + 10 + 10 + 10", "8 tens", "8 x 10 = 80"],
            ["9", "10 + 10 + 10 + 10 + 10 + 10 + 10 + 10 + 10", "9 tens", "9 x 10 = 90"],
            ["10", "10 + 10 + 10 + 10 + 10 + 10 + 10 + 10 + 10 + 10", "10 tens", "10 x 10 = 100"]
        ]
        

        # Create table with custom column widths
        table = Table(
            table_data,
          #  col_labels=[Text("Number of chains"), Text("A person counted the beads in the chains \nand wrote the numbers as shown below.")],
            include_outer_lines=True,
            line_config={"stroke_width": 3, "color": RED},
        ).scale(0.5).set_opacity(20).stretch_to_fit_depth(4)

        # Add table to scene
        self.play(Create(table))
        self.wait(12)




    def Fivetable(self):
        # Table data for the repeated addition and multiplication table of 5
        title_text = "Look at the repeated addition of 5 and the Multiplication Table of 5."
         # Title text
        title = Text(title_text, color=YELLOW).scale(0.6).to_edge(UP*0.4)
        # Add title to scene
        self.play(Write(title))
        self.wait(4)



        background = Rectangle(height=6.6, width=10.23)
        background.set_fill(opacity=.45)
        background.set_color([TEAL, RED, YELLOW,GREEN])
        self.add(background)
        title = Text("5", color=WHITE,fill_opacity=0.4).scale(6)
        # Add title to scene
        self.play(Write(title))
        self.wait(2)


        table_data = [
           # ["", "Look at the repeated addition of 5. Write the Multiplication Table of 5.", "", ""],
            ["One five", "5", "1 x 5 = 5"],
            ["Two fives", "5 + 5", "2 x 5 = 10"],
            ["Three fives", "5 + 5 + 5", "3 x 5 = 15"],
            ["Four fives", "5 + 5 + 5 + 5", "4 x 5 = 20"],
            ["Five fives", "5 + 5 + 5 + 5 + 5", "5 x 5 = 25"],
            ["Six fives", "5 + 5 + 5 + 5 + 5 + 5", "6 x 5 = 30"],
            ["Seven fives", "5 + 5 + 5 + 5 + 5 + 5 + 5", "7 x 5 = 35"],
            ["Eight fives", "5 + 5 + 5 + 5 + 5 + 5 + 5 + 5", "8 x 5 = 40"],
            ["Nine fives", "5 + 5 + 5 + 5 + 5 + 5 + 5 + 5 + 5", "9 x 5 = 45"],
            ["Ten fives", "5 + 5 + 5 + 5 + 5 + 5 + 5 + 5 + 5 + 5", "10 x 5 = 50"]
        ]

        # Create table with custom column widths
      #  col_widths = [3, 10, 1, 5]

        table = Table(
            table_data,
           
         #   col_widths=col_widths,
            include_outer_lines=True,
            line_config={"stroke_width": 3.2, "color": BLUE},
        ).scale(0.5).set_opacity(20)

        
        self.play(Create(table))
        self.wait(3)
        self.play(FadeIn(table),running_start=0.5)
        self.wait(12)


    def Two(self):

        title = Text("Multiplication Table of 2", color=BLUE).scale(0.6).to_edge(UP*0.4)
        # Add title to scene
        self.play(Write(title))
        self.wait(3)


        title = Text("2", color=WHITE,fill_opacity=0.28).scale(6)
        # Add title to scene
        self.play(Write(title))
        self.wait(2)

        table_data = [
         #  ["Number of chains", "A person counted the beads in the chains and \nwrote the numbers as shown below."],
            ["2 x 1", "2", "2"],
            ["2 x 2", "2 + 2", "4"],
            ["2 x 3 ", "2 + 2 + 2", "6"],
            ["2 x 4", "2 + 2 + 2 + 2", "8"],
            ["2 x 5", "2 + 2 + 2 + 2 + 2", "10"],
            ["2 x 6", "2 + 2 + 2 + 2 + 2 + 2", "12"],
            ["2 x 7", "2 + 2 + 2 + 2 + 2 + 2 + 2", "14"],
            ["2 x 8", "2 + 2 + 2 + 2 + 2 + 2 + 2 + 2", "16"],
            [" 2 x 9 ", "2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2", "18"],
            [" 2 x 10", "2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2", "20"]
        ]
        

        # Create table with custom column widths
        table = Table(
            table_data,
          #  col_labels=[Text("Number of chains"), Text("A person counted the beads in the chains \nand wrote the numbers as shown below.")],
            include_outer_lines=True,
            line_config={"stroke_width": 3, "color": RED},
        ).scale(0.5).set_opacity(20).stretch_to_fit_depth(4).shift(LEFT*2.5)

        # Add table to scene
        self.play(Create(table))
        self.wait(5)

# Create equations for the multiplication table
        equations = VGroup(
            *[MathTex(f"2 \\times {i} =", 2 * i) for i in range(1, 11)]
        ).arrange(DOWN, buff=0.3).shift(RIGHT*5).set_color(YELLOW)

        # Display equations one by one
        for equation in equations:
            self.play(Write(equation))
            self.wait(0.5)

        # Fade out equations
        self.wait(5)
        self.play(FadeOut(equations))
        self.wait()



    def two1(self):
    
        # Create title
        title = Text("Multiplication Tables OF 2", font_size=36,color=YELLOW).to_edge(UP*0.75)
        self.play(Write(title))
        self.wait(3)


        equations = VGroup(
            *[MathTex(f"2 \\times {i} =", 2 * i) for i in range(1, 11)]
        ).arrange(DOWN, buff=0.3).shift(RIGHT*5).set_color(BLUE)


        # Create grid
        grid = VGroup()
        for i in range(10):
            for j in range(10):
                cell = Square(side_length=0.6, stroke_width=1.1)
                cell.set_stroke(color=PINK,opacity=20,width=2)
                if j < 2:
                    cell.set_fill(PINK, opacity=0.8)
                grid.add(cell)
        grid.arrange_in_grid(rows=10, cols=10, buff=0)
     
        # Anim
        self.play(Create(grid))
        self.wai(4)
   
        for equation in equations:
            self.play(Write(equation))
            self.wait(0.5)

        self.wait(6)
        # Fade out equations
        self.play(FadeOut(equations))
        self.wait()
       # self.play(Write(table3), Write(table3_label))


    def Three(self):
    
        # Create title
        title = Text("Multiplication Tables OF 3", font_size=36,color=BLUE).to_edge(UP*0.75)
        self.play(Write(title))
        self.wait(3)

        tit = Text("3", color=WHITE,fill_opacity=0.3).scale(6)
        # Add title to scene
        self.play(Write(tit))
        self.wait(2)

         # Create a grid of squares
        grid = VGroup(*[
            VGroup(*[
                Square(side_length=0.6).set_stroke(width=3)
                for _ in range(10)
            ]).arrange(RIGHT, buff=0)
            for _ in range(10)
        ]).arrange(DOWN, buff=0)

        grid.move_to(ORIGIN)

        # Add the grid to the scene
        self.add(grid)

        # Loop to animate each multiplication step
        for i in range(1, 11):
            rows = i
            cols = 3
            text = f"3 x {i} = {3*i}"
            highlight_squares = VGroup(*[
                grid[row][col].copy().set_fill(PINK, opacity=0.7).set_stroke(width=0.5)
                for row in range(rows)
                for col in range(cols)
            ])
            self.play(FadeIn(highlight_squares))

            multiplication_text = Text(text)
            multiplication_text.next_to(highlight_squares, RIGHT*4.65, buff=1)
            self.play(Write(multiplication_text))

            self.wait(3)
            self.play(FadeOut(multiplication_text), FadeOut(highlight_squares))

        self.wait()
 
    def FOUR(self):
    
  
        # Create title
        title = Text("Multiplication Tables OF 4", font_size=36,color=WHITE).to_edge(UP*0.75)
        self.play(Write(title))
        self.wait(3)


        tit = Text("4", color=WHITE,fill_opacity=0.3).scale(6)
        # Add title to scene
        self.play(Write(tit))
        self.wait(2)   
  

         # Create a grid of squares
        grid = VGroup(*[
            VGroup(*[
                Square(side_length=0.6).set_stroke(width=3)
                for _ in range(10)
            ]).arrange(RIGHT, buff=0)
            for _ in range(10)
        ]).arrange(DOWN, buff=0)

        grid.move_to(ORIGIN)

        # Add the grid to the scene
        self.add(grid)

        # Loop to animate each multiplication step
        for i in range(1, 11):
            rows = i
            cols = 4
            text = f"4 x {i} = {4*i}"
            highlight_squares = VGroup(*[
                grid[row][col].copy().set_fill(BLUE, opacity=0.7).set_stroke(width=0.5)
                for row in range(rows)
                for col in range(cols)
            ])
            self.play(FadeIn(highlight_squares))

            multiplication_text = Text(text)
            multiplication_text.next_to(highlight_squares, RIGHT*4.3, buff=1)
            self.play(Write(multiplication_text))

            self.wait(3)
            self.play(FadeOut(multiplication_text), FadeOut(highlight_squares))

        self.wait()
        
    def SIX(self):
    
  
        # Create title
        title = Text("Multiplication Tables OF 6", font_size=36,color=LIGHT_PINK).to_edge(UP*0.75)
        self.play(Write(title))
        self.wait(3)

        # table2.to_edge(RIGHT*1.2).shift(DOWN*0.1)
        tit = Text("6", color=WHITE,fill_opacity=0.3).scale(6)
        # Add title to scene
        self.play(Write(tit))
        self.wait(2)

         # Create a grid of squares
        grid = VGroup(*[
            VGroup(*[
                Square(side_length=0.6).set_stroke(width=3)
                for _ in range(10)
            ]).arrange(RIGHT, buff=0)
            for _ in range(10)
        ]).arrange(DOWN, buff=0)

        grid.move_to(ORIGIN)

        # Add the grid to the scene
        self.add(grid)

        # Loop to animate each multiplication step
        for i in range(1, 11):
            rows = i
            cols = 6
            text = f"6 x {i} = {6*i}"
            highlight_squares = VGroup(*[
                grid[row][col].copy().set_fill(YELLOW, opacity=0.7).set_stroke(width=0.5)
                for row in range(rows)
                for col in range(cols)
            ])
            self.play(FadeIn(highlight_squares))

            multiplication_text = Text(text)
            multiplication_text.next_to(highlight_squares, RIGHT*3, buff=1)
            self.play(Write(multiplication_text))

            self.wait(3)
            self.play(FadeOut(multiplication_text), FadeOut(highlight_squares))

        self.wait()
      
    def SEVEN(self):
    
        # Create title
        title = Text("Multiplication Tables OF 7", font_size=36,color=ORANGE).to_edge(UP*0.75)
        self.play(Write(title))
        self.wait(3)

        tit = Text("7", color=WHITE,fill_opacity=0.3).scale(6)
        # Add title to scene
        self.play(Write(tit))
        self.wait(2) 

      # Create a grid of squares
        grid = VGroup(*[
            VGroup(*[
                Square(side_length=0.6).set_stroke(width=3,color=YELLOW)
                for _ in range(10)
            ]).arrange(RIGHT, buff=0)
            for _ in range(10)
        ]).arrange(DOWN, buff=0)

        grid.move_to(ORIGIN)

        # Add the grid to the scene
        self.add(grid)

        # Loop to animate each multiplication step
        for i in range(1, 11):
            rows = i
            cols = 7
            text = f"7 x {i} = {7*i}"
            highlight_squares = VGroup(*[
                grid[row][col].copy().set_fill(WHITE, opacity=0.7).set_stroke(width=0.5)
                for row in range(rows)
                for col in range(cols)
            ])
            self.play(FadeIn(highlight_squares))

            multiplication_text = Text(text)
            multiplication_text.next_to(highlight_squares, RIGHT*2.3, buff=1)
            self.play(Write(multiplication_text))

            self.wait(3)
            self.play(FadeOut(multiplication_text), FadeOut(highlight_squares))

        self.wait()

    def NINE(self):
    
        # Create title
        title = Text("Multiplication Tables OF 9", font_size=36,color=WHITE).to_edge(UP*0.75)
        self.play(Write(title))
        self.wait(3)

        tit = Text("9", color=WHITE,fill_opacity=0.45).scale(6)
        # Add title to scene
        self.play(Write(tit))
        self.wait(2)
  # Create a grid of squares
        grid = VGroup(*[
            VGroup(*[
                Square(side_length=0.6).set_stroke(width=3,color=PINK)
                for _ in range(10)
            ]).arrange(RIGHT, buff=0)
            for _ in range(10)
        ]).arrange(DOWN, buff=0)

        grid.move_to(ORIGIN)

        # Add the grid to the scene
        self.add(grid)

        # Loop to animate each multiplication step
        for i in range(1, 11):
            rows = i
            cols = 9
            text = f"9 x {i} = {9*i}"
            highlight_squares = VGroup(*[
                grid[row][col].copy().set_fill(BLUE, opacity=0.7).set_stroke(width=0.5)
                for row in range(rows)
                for col in range(cols)
            ])
            self.play(FadeIn(highlight_squares))

            multiplication_text = Text(text)
            multiplication_text.next_to(highlight_squares, RIGHT*1.2, buff=1)
            self.play(Write(multiplication_text))

            self.wait()
            self.play(FadeOut(multiplication_text), FadeOut(highlight_squares))

        self.wait()




           
    def Flower(self):
    
  
        # Title
        title = Text("Count the flowers shown below in each flower-pot.", color=BLUE).scale(0.7)
        title.to_edge(UP)
        
        # Create flower pots
        pots = [
            self.create_pot_with_flowers(4),
            self.create_pot_with_flowers(3),
            self.create_pot_with_flowers(2),
            self.create_pot_with_flowers(1),
            self.create_pot_with_flowers(0)
        ]
        
        # Arrange pots
        pot_group = VGroup(*pots).arrange(RIGHT, buff=0.5)
        pot_group.next_to(title, DOWN, buff=0.5)
        
        # Create answer boxes
        boxes = VGroup(*[Square(side_length=1, color=PINK, fill_opacity=0) for _ in range(5)])
        boxes.arrange(RIGHT, buff=pot_group.get_width()/5 - boxes[4].get_width())
        boxes.next_to(pot_group, DOWN, buff=0.3)
        
        # Add number to first box
        number5 = Text("4", color=WHITE).scale(0.9)
        number5.move_to(boxes[0])
        number4 = Text("3", color=WHITE).scale(0.9)
        number4.move_to(boxes[1])
        number3 = Text("2", color=WHITE).scale(0.9)
        number3.move_to(boxes[2])
        number2 = Text("1", color=WHITE).scale(0.9)
        number2.move_to(boxes[3])
        number1 = Text("0", color=WHITE).scale(0.9)
        number1.move_to(boxes[4])
        
        # Animations
        self.play(Write(title))
        self.wait(3)
        self.play(Create(pot_group))
        self.wait(2)
        self.play(Create(boxes))
        self.wait(7.2)
        self.play(Write(number1),Write(number2),Write(number3),Write(number4),Write(number5))
        self.wait(4)

    def create_pot_with_flowers(self, num_flowers):
        pot = Triangle(color=ORANGE, fill_color=ORANGE, fill_opacity=1).scale(0.7)
        pot.rotate(PI)  # Flip the triangle upside down
        
        flowers = VGroup()
        for i in range(num_flowers):
            flower = self.create_flower()
            flower.next_to(pot, UP, buff=0.5)
            flower.shift(RIGHT * (i - (num_flowers-1)/2) * 0.2)
            flowers.add(flower)
        
        return VGroup(pot, flowers)

    def create_flower(self):
        petals = VGroup(*[Ellipse(width=0.5, height=0.1, color=YELLOW, fill_opacity=2) for _ in range(5)])
        for i, petal in enumerate(petals):
            petal.rotate(i * 1*PI/5)
        center = Circle(radius=0.09, color=RED, fill_opacity=2)
        return VGroup(petals, center)


    def ENTIRETABLES(self):
  
        # Title
        title = Text("Entire Multiplication tables in a single grid", 
                     color=BLUE).scale(1)
        title.to_edge(UP)

        # Create grid
        grid = Table(
            [
                ["x", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
                ["1", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
                ["2", "2", "4", "6", "8", "10", "12", "14", "16", "18", "20"],
                ["3", "3", "6", "9", "12", "15", "18", "21", "24", "27", "30"],
                ["4", "4", "8", "12", "16", "20", "24", "28", "32", "36", "40"],
                ["5", "5", "10", "15", "20", "25", "30", "35", "40", "45", "50"],
                ["6", "6", "12", "18", "24", "30", "36", "42", "48", "54", "60"],
                ["7", "7", "14", "21", "28", "35", "42", "49", "56", "63", "70"],
                ["8", "8", "16", "24", "32", "40", "48", "56", "64", "72", "80"],
                ["9", "9", "18", "27", "36", "45", "54", "63", "72", "81", "90"],
                ["10", "10", "20", "30", "40", "50", "60", "70", "80", "90", "100"]
            ],
            include_outer_lines=True
        )
        
        # Style the grid
        grid.scale(0.4)

        grid.set_color(WHITE)
        grid.set_column_colors(YELLOW,YELLOW,YELLOW,YELLOW,YELLOW,YELLOW,YELLOW,YELLOW,YELLOW,YELLOW,YELLOW)
        
        
        # Position the grid
        grid.next_to(title, DOWN, buff=0.7)

        # Animations
        self.play(Write(title))
        self.wait(3)
        self.play(Create(grid))
        self.wait(15)



    def multizero(self):
        # Create title
        title = Text("Multiplication Table of 0", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(3)
        
     # Create title
        pot1 = Triangle(color=ORANGE, fill_color=ORANGE, fill_opacity=1).scale(0.4)
        pot1.rotate(PI).to_edge(LEFT*3)
        self.play(Create(pot1))  # Flip the triangle upside down
        
        title1 = Text("empty pot with zero\n\n flowers ", font_size=25,color=BLUE)
        title1.next_to(pot1,DOWN)
        self.play(Write(title1))
        self.wait(3)

        # Create rows
        rows = VGroup()
        for i in range(1, 11):
            # Left side: number and cups
            number = Text(f"{i}", font_size=24)
            cups = VGroup(*[self.create_cup() for _ in range(i)])
            cups.arrange(RIGHT, buff=0.1)
            left = VGroup(number, cups).arrange(RIGHT, buff=0.5)

        

            # Combine left and right
            row = VGroup(left)
            rows.add(row)

        rows.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        rows.next_to(title, DOWN, buff=0.5)


        equations = VGroup(
            *[MathTex(f"0 \\times {i} =", 0 * i) for i in range(1, 11)]
        ).arrange(DOWN*6, buff=0.06).shift(RIGHT*5).set_color(YELLOW)
       

        # Animate each row
        for row in rows:
            self.play(FadeIn(row[0]))  # Animate left side
        
            self.wait(0.5)
           
        self.wait(4)
        for equation in equations:
            self.play(Write(equation))
            self.wait(0.5)
        self.wait(4)


    

    def create_cup(self):
        # Create a simple cup shape using basic geometries
        cup_color = "#8B4513"  # Brown color
        # base = Rectangle(width=0.2, height=0.05, fill_opacity=1, color=cup_color)
        # body = Rectangle(width=0.15, height=0.2, fill_opacity=1, color=cup_color)
        pot = Triangle(color=ORANGE, fill_color=ORANGE, fill_opacity=1).scale(0.48)
        pot.rotate(PI)  # Flip the triangle upside down
        
       
        
        cup = VGroup(pot)
        cup.scale(0.48)  # Adjust size as needed
        return cup
    

    
 
    def eight(self):
    
        # Create title
        title = Text("Multiplication Tables OF 8", font_size=36,color=WHITE).to_edge(UP*0.75)
        self.play(Write(title))
        self.wait(3)

        tit = Text("8", color=WHITE,fill_opacity=0.45).scale(6)
        # Add title to scene
        self.play(Write(tit))
        self.wait(2)
  # Create a grid of squares
        grid = VGroup(*[
            VGroup(*[
                Square(side_length=0.6).set_stroke(width=3,color=BLUE)
                for _ in range(10)
            ]).arrange(RIGHT, buff=0)
            for _ in range(10)
        ]).arrange(DOWN, buff=0)

        grid.move_to(ORIGIN)

        # Add the grid to the scene
        self.add(grid)

        # Loop to animate each multiplication step
        for i in range(1, 11):
            rows = i
            cols = 8
            text = f"8 x {i} = {8*i}"
            highlight_squares = VGroup(*[
                grid[row][col].copy().set_fill(PINK, opacity=0.7).set_stroke(width=0.5)
                for row in range(rows)
                for col in range(cols)
            ])
            self.play(FadeIn(highlight_squares))

            multiplication_text = Text(text)
            multiplication_text.next_to(highlight_squares, RIGHT*2.2, buff=1)
            self.play(Write(multiplication_text))

            self.wait()
            self.play(FadeOut(multiplication_text), FadeOut(highlight_squares))

        self.wait()




    def SetDeveloperList(self):
        self.DeveloperList = "Uday Kiran"   

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade2chapter10MultiplicationTables(1to10).py"      




# Run the scene
if __name__ == "__main__":
    from manim import config
    config.background_color = BLACK
    Grade2chapter10MultiplicationTables1to10().render()