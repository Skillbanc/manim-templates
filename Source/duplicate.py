from manim import *
import cvo
from AbstractAnim import AbstractAnim

class TableScene(AbstractAnim):
    def construct(self):
        #self.CirleExamples()
        self.ExampleExercise_1()
        #self.vertical_Exercise()



    def CirleExamples(self):


        example = Text("Find the remaining things:", font_size=34).to_edge(UP*1.6+LEFT*1)

        # Subtraction Example: 5 - 2 = 3

        # Circles for the number 5
        c1 = Circle(radius=0.3, color=BLUE).to_edge(LEFT * 3 + UP * 7.25).set_fill(opacity=0.4)
        c2 = Circle(radius=0.3, color=BLUE).next_to(c1, RIGHT * 1.2).set_fill(opacity=0.4)
        c3 = Circle(radius=0.3, color=BLUE).next_to(c2, RIGHT * 1.2).set_fill(opacity=0.4)
        c4 = Circle(radius=0.3, color=BLUE).next_to(c3, RIGHT * 1.2).set_fill(opacity=0.4)
        c5 = Circle(radius=0.3, color=BLUE).next_to(c4, RIGHT * 1.2).set_fill(opacity=0.4)
        five = Text("5").next_to(c3, DOWN)

        minus1 = Text("-").next_to(c5, RIGHT * 1.2)

        # Circles for the number 2
        s1 = Circle(radius=0.3, color=BLUE).next_to(minus1, RIGHT * 1.2).set_fill(opacity=0.4)
        s2 = Circle(radius=0.3, color=BLUE).next_to(s1, RIGHT * 1.2).set_fill(opacity=0.4)

        two = Text("2").next_to(s1, DOWN).shift(RIGHT * 0.5)

        equal1 = Text("=").next_to(s2, RIGHT * 1.2)

        # Circles for the result 3
        result_c1 = Circle(radius=0.3, color=BLUE).next_to(equal1, RIGHT * 1.2).set_fill(opacity=0.4)
        result_c2 = Circle(radius=0.3, color=BLUE).next_to(result_c1, RIGHT * 1.2).set_fill(opacity=0.4)
        result_c3 = Circle(radius=0.3, color=BLUE).next_to(result_c2, RIGHT * 1.2).set_fill(opacity=0.4)

        three = Text("3").next_to(result_c2, DOWN)

        # Animation for the first example
        self.play(Write(example))
        self.play(Write(c1), Write(c2), Write(c3), Write(c4), Write(c5))
        self.play(Write(five))
        self.play(Write(minus1))
        self.play(Write(s1), Write(s2))
        self.play(Write(two))
        self.play(Write(equal1))
        self.play(Write(result_c1), Write(result_c2), Write(result_c3))
        self.play(Write(three))


        # Fade out all elements
        self.play(
            FadeOut(c1), FadeOut(c2), FadeOut(c3), FadeOut(c4), FadeOut(c5), 
            FadeOut(five), FadeOut(minus1), 
            FadeOut(s1), FadeOut(s2), FadeOut(two), 
            FadeOut(equal1), 
            FadeOut(result_c1), FadeOut(result_c2), FadeOut(result_c3), 
            FadeOut(three)
        )

        self.wait(1)


        # Subtraction Example: 6 - 4 = 2
        # # Circles for the number 6
        c1 = Circle(radius=0.3, color=GRAY).to_edge(LEFT * 3 + UP * 7.25).set_fill(opacity=0.4)
        c2 = Circle(radius=0.3, color=GRAY).next_to(c1, RIGHT * 1.2).set_fill(opacity=0.4)
        c3 = Circle(radius=0.3, color=GRAY).next_to(c2, RIGHT * 1.2).set_fill(opacity=0.4)
        c4 = Circle(radius=0.3, color=GRAY).next_to(c3, RIGHT * 1.2).set_fill(opacity=0.4)
        c5 = Circle(radius=0.3, color=GRAY).next_to(c4, RIGHT * 1.2).set_fill(opacity=0.4)
        c6 = Circle(radius=0.3, color=GRAY).next_to(c5, RIGHT * 1.2).set_fill(opacity=0.4)
        six = Text("6").next_to(c3, DOWN).shift(RIGHT * 0.5)

        minus2 = Text("-").next_to(c6, RIGHT * 1.2)

        # # Circles for the number 4
        s1 = Circle(radius=0.3, color=GRAY).next_to(minus2, RIGHT * 1.2).set_fill(opacity=0.4)
        s2 = Circle(radius=0.3, color=GRAY).next_to(s1, RIGHT * 1.2).set_fill(opacity=0.4)
        s3 = Circle(radius=0.3, color=GRAY).next_to(s2, RIGHT * 1.2).set_fill(opacity=0.4)
        s4 = Circle(radius=0.3, color=GRAY).next_to(s3, RIGHT * 1.2).set_fill(opacity=0.4)

        four = Text("4").next_to(s2, DOWN).shift(RIGHT * 0.5)

        equal2 = Text("=").next_to(s4, RIGHT * 1.2)

        # # Circles for the result 2
        result_c1 = Circle(radius=0.3, color=GRAY).next_to(equal2, RIGHT * 1.2).set_fill(opacity=0.4)
        result_c2 = Circle(radius=0.3, color=GRAY).next_to(result_c1, RIGHT * 1.2).set_fill(opacity=0.4)

        two = Text("2").next_to(result_c1, DOWN).shift(RIGHT * 0.5)

        # # Animation for the second example
        self.play(Write(c1), Write(c2), Write(c3), Write(c4), Write(c5), Write(c6))
        self.play(Write(six))
        self.play(Write(minus2))
        self.play(Write(s1), Write(s2), Write(s3), Write(s4))
        self.play(Write(four))
        self.play(Write(equal2))
        self.play(Write(result_c1), Write(result_c2))
        self.play(Write(two))



        # Fade out all elements
        self.play(
            FadeOut(c1), FadeOut(c2), FadeOut(c3), FadeOut(c4), FadeOut(c5), FadeOut(c6), 
            FadeOut(six), FadeOut(minus2), 
            FadeOut(s1), FadeOut(s2), FadeOut(s3), FadeOut(s4), 
            FadeOut(four), FadeOut(equal2), 
            FadeOut(result_c1), FadeOut(result_c2), 
            FadeOut(two)
        )

        self.wait(1)








        # # Subtraction Example: 7 - 3 = 4

        # # Circles for the number 7
        c1 = Circle(radius=0.3, color=DARK_BROWN).to_edge(LEFT * 1 + UP * 7.25).set_fill(opacity=0.4)
        c2 = Circle(radius=0.3, color=DARK_BROWN).next_to(c1, RIGHT * 1.2).set_fill(opacity=0.4)
        c3 = Circle(radius=0.3, color=DARK_BROWN).next_to(c2, RIGHT * 1.2).set_fill(opacity=0.4)
        c4 = Circle(radius=0.3, color=DARK_BROWN).next_to(c3, RIGHT * 1.2).set_fill(opacity=0.4)
        c5 = Circle(radius=0.3, color=DARK_BROWN).next_to(c4, RIGHT * 1.2).set_fill(opacity=0.4)
        c6 = Circle(radius=0.3, color=DARK_BROWN).next_to(c5, RIGHT * 1.2).set_fill(opacity=0.4)
        c7 = Circle(radius=0.3, color=DARK_BROWN).next_to(c6, RIGHT * 1.2).set_fill(opacity=0.4)
        seven = Text("7").next_to(c4, DOWN)

        minus3 = Text("-").next_to(c7, RIGHT * 1.2)

        # # Circles for the number 3
        s1 = Circle(radius=0.3, color=DARK_BROWN).next_to(minus3, RIGHT * 1.2).set_fill(opacity=0.4)
        s2 = Circle(radius=0.3, color=DARK_BROWN).next_to(s1, RIGHT * 1.2).set_fill(opacity=0.4)
        s3 = Circle(radius=0.3, color=DARK_BROWN).next_to(s2, RIGHT * 1.2).set_fill(opacity=0.4)

        three = Text("3").next_to(s2, DOWN)

        equal3 = Text("=").next_to(s3, RIGHT * 1.2)

        # # Circles for the result 4
        result_c1 = Circle(radius=0.3, color=DARK_BROWN).next_to(equal3, RIGHT * 1.2).set_fill(opacity=0.4)
        result_c2 = Circle(radius=0.3, color=DARK_BROWN).next_to(result_c1, RIGHT * 1.2).set_fill(opacity=0.4)
        result_c3 = Circle(radius=0.3, color=DARK_BROWN).next_to(result_c2, RIGHT * 1.2).set_fill(opacity=0.4)
        result_c4 = Circle(radius=0.3, color=DARK_BROWN).next_to(result_c3, RIGHT * 1.2).set_fill(opacity=0.4)

        four = Text("4").next_to(result_c2, DOWN).shift(RIGHT * 0.5)

        # # Animation for the third example
        self.play(Write(c1), Write(c2), Write(c3), Write(c4), Write(c5), Write(c6), Write(c7))
        self.play(Write(seven))
        self.play(Write(minus3))
        self.play(Write(s1), Write(s2), Write(s3))
        self.play(Write(three))
        self.play(Write(equal3))
        self.play(Write(result_c1), Write(result_c2), Write(result_c3), Write(result_c4))
        self.play(Write(four))

        # Fade out all elements
        self.play(
            FadeOut(c1), FadeOut(c2), FadeOut(c3), FadeOut(c4), FadeOut(c5), FadeOut(c6), FadeOut(c7),
            FadeOut(seven), FadeOut(minus3),
            FadeOut(s1), FadeOut(s2), FadeOut(s3),
            FadeOut(three), FadeOut(equal3),
            FadeOut(result_c1), FadeOut(result_c2), FadeOut(result_c3), FadeOut(result_c4),
            FadeOut(four)
        )

        self.wait(1)

        # Example 4 - 2 = 2

        # Squares for the number 4
        box1 = Square(side_length=1, color=BLUE).to_edge(LEFT * 2 + UP * 7.25).set_fill(color=BLUE, opacity=0.4)
        box2 = Square(side_length=1, color=BLUE).next_to(box1, RIGHT * 1.2).set_fill(color=BLUE, opacity=0.4)
        box3 = Square(side_length=1, color=BLUE).next_to(box2, RIGHT * 1.2).set_fill(color=BLUE, opacity=0.4)
        box4 = Square(side_length=1, color=BLUE).next_to(box3, RIGHT * 1.2).set_fill(color=BLUE, opacity=0.4)
        four = Text("4").next_to(box3, DOWN).shift(LEFT * 0.75)

        minus = Text("-").next_to(box4, RIGHT * 1.2)

        # Squares for the number 2
        box5 = Square(side_length=1, color=BLUE).next_to(minus, RIGHT * 1.2).set_fill(color=BLUE, opacity=0.4)
        box6 = Square(side_length=1, color=BLUE).next_to(box5, RIGHT * 1.2).set_fill(color=BLUE, opacity=0.4)
        two = Text("2").next_to(box5, DOWN).shift(RIGHT * 0.75)

        equal = Text("=").next_to(box6, RIGHT * 1.2)

        # Squares for the result 2
        box7 = Square(side_length=1, color=BLUE).next_to(equal, RIGHT * 1.2).set_fill(color=BLUE, opacity=0.4)
        box8 = Square(side_length=1, color=BLUE).next_to(box7, RIGHT * 1.2).set_fill(color=BLUE, opacity=0.4)
        result = Text("2").next_to(box7, DOWN).shift(RIGHT * 0.75)

        # Animation
        self.play(Write(box1, run_time=2), Write(box2, run_time=2), Write(box3, run_time=2), Write(box4, run_time=2))
        self.play(Write(four))
        self.play(Write(minus))
        self.play(Write(box5, run_time=2), Write(box6, run_time=2))
        self.play(Write(two))
        self.play(Write(equal))
        self.play(Write(box7, run_time=2), Write(box8, run_time=2))
        self.play(Write(result))

        # Fade out all elements
        self.play(
            FadeOut(box1), FadeOut(box2), FadeOut(box3), FadeOut(box4),
            FadeOut(four), FadeOut(minus),
            FadeOut(box5), FadeOut(box6),
            FadeOut(two), FadeOut(equal),
            FadeOut(box7), FadeOut(box8),
            FadeOut(result)
        )

        self.wait(2)



        # Circles for the number 5 - 1 = 4

        # Squares for the number 5
        box1 = Square(side_length=1, color=PURPLE).to_edge(LEFT * 1 + UP * 7.25).set_fill(color=PURPLE, opacity=0.3)
        box2 = Square(side_length=1, color=PURPLE).next_to(box1, RIGHT * 1.2).set_fill(color=PURPLE, opacity=0.3)
        box3 = Square(side_length=1, color=PURPLE).next_to(box2, RIGHT * 1.2).set_fill(color=PURPLE, opacity=0.3)
        box4 = Square(side_length=1, color=PURPLE).next_to(box3, RIGHT * 1.2).set_fill(color=PURPLE, opacity=0.3)
        box5 = Square(side_length=1, color=PURPLE).next_to(box4, RIGHT * 1.2).set_fill(color=PURPLE, opacity=0.3)
        five = Text("5").next_to(box3, DOWN)

        minus = Text("-").next_to(box5, RIGHT * 1.2)

        # Squares for the number 1
        box6 = Square(side_length=1, color=PURPLE).next_to(minus, RIGHT * 1.2).set_fill(color=PURPLE, opacity=0.3)
        one = Text("1").next_to(box6, DOWN)

        equal = Text("=").next_to(box6, RIGHT * 1.2)

        # Squares for the result 4
        box7 = Square(side_length=1, color=PURPLE).next_to(equal, RIGHT * 1.2).set_fill(color=PURPLE, opacity=0.3)
        box8 = Square(side_length=1, color=PURPLE).next_to(box7, RIGHT * 0.5).set_fill(color=PURPLE, opacity=0.3)
        box9 = Square(side_length=1, color=PURPLE).next_to(box8, RIGHT * 0.5).set_fill(color=PURPLE, opacity=0.3)
        box10 = Square(side_length=1, color=PURPLE).next_to(box9, RIGHT * 0.5).set_fill(color=PURPLE, opacity=0.3)
        four = Text("4").next_to(box9, DOWN).shift(LEFT * 0.75)

        # Animation
        self.play(Write(box1, run_time=2), Write(box2, run_time=2), Write(box3, run_time=2), Write(box4, run_time=2), Write(box5, run_time=2))
        self.play(Write(five))
        self.play(Write(minus))
        self.play(Write(box6, run_time=2))
        self.play(Write(one))
        self.play(Write(equal))
        self.play(Write(box7, run_time=2), Write(box8, run_time=2), Write(box9, run_time=2), Write(box10, run_time=2))
        self.play(Write(four))

        self.wait(3)

        # Fade out all elements
        self.play(
            FadeOut(box1), FadeOut(box2), FadeOut(box3), FadeOut(box4), FadeOut(box5),
            FadeOut(five), FadeOut(minus),
            FadeOut(box6), FadeOut(one), FadeOut(equal),
            FadeOut(box7), FadeOut(box8), FadeOut(box9), FadeOut(box10),
            FadeOut(four),FadeOut(example)
        )


    def ExampleExercise_1(self):
        # Create and display the initial text
        t1 = Text("Calculate the differences for the following pairs of numbers:", font_size=33).to_edge(UP*1.5 + LEFT * 1)
        self.play(Write(t1))
        
        # Define and display the subtractions
        s1 = Text("9 - 2 = ", color=PINK, font_size=30).to_edge(LEFT * 9.25 + UP * 4.5)
        ss1 = Square(side_length=0.7).next_to(s1, RIGHT)
        s12 = Text("7", color=BLUE, font_size=30).move_to(ss1.get_center())
        self.play(Write(s1, run_time=3))
        self.play(Write(ss1, run_time=2))
        self.play(Write(s12))
        
        s2 = Text("7 - 5 = ", color=PINK, font_size=30).next_to(s1, DOWN * 3)
        ss2 = Square(side_length=0.7).next_to(s2, RIGHT)
        s22 = Text("2", color=BLUE, font_size=30).move_to(ss2.get_center())
        self.play(Write(s2, run_time=3))
        self.play(Write(ss2, run_time=2))
        self.play(Write(s22))

        s3 = Text("4 - 4 = ", color=PINK, font_size=30).next_to(s2, DOWN * 3)
        ss3 = Square(side_length=0.7).next_to(s3, RIGHT)
        s32 = Text("0", color=BLUE, font_size=30).move_to(ss3.get_center())
        self.play(Write(s3, run_time=3))
        self.play(Write(ss3, run_time=2))
        self.play(Write(s32))

        s4 = Text("5 - 3 = ", color=PINK, font_size=30).next_to(s3, DOWN * 3)
        ss4 = Square(side_length=0.7).next_to(s4, RIGHT)
        s42 = Text("2", color=BLUE, font_size=30).move_to(ss4.get_center())
        self.play(Write(s4, run_time=3))
        self.play(Write(ss4, run_time=2))
        self.play(Write(s42))

        s5 = Text("8 - 5 = ", color=PINK, font_size=30).next_to(s4, DOWN * 3)
        ss5 = Square(side_length=0.7).next_to(s5, RIGHT)
        s52 = Text("3", color=BLUE, font_size=30).move_to(ss5.get_center())
        self.play(Write(s5, run_time=3))
        self.play(Write(ss5, run_time=2))
        self.play(Write(s52))



        # Fade out all elements
        self.play(
            FadeOut(s1), FadeOut(ss1), FadeOut(s12),
            FadeOut(s2), FadeOut(ss2), FadeOut(s22),
            FadeOut(s3), FadeOut(ss3), FadeOut(s32),
            FadeOut(s4), FadeOut(ss4), FadeOut(s42),
            FadeOut(s5), FadeOut(ss5), FadeOut(s52),
        )

    
    def vertical_Exercise(self):
        # Title
        title = Tex("Solving the following additions:", color=PURPLE).to_edge(UP*1.5 + LEFT*1)
        self.play(Write(title))

        # Addition 15 + 3 = 18
        addition1 = self.vertical_addition("15", "3", "18")
        addition1.move_to([-1, 0.5, 0])

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
        title_1 = Text("Calculations:", font_size=31, color=DARK_BROWN).to_edge(UP*5 + RIGHT*3.25)
        
        # Create an underline for the word "Calculations"
        underline = Line(start=title_1.get_left() + LEFT*0.4, end=title_1.get_left() + RIGHT*1.79, color=GOLD, stroke_width=2)
        underline.next_to(title_1, DOWN, buff=0.1)       
    
        sub_title1 = Text("5 + 3 = 8", font_size=32, color=YELLOW).to_edge(UP*6.65 + RIGHT*4)
        sub_title2 = Text("1 + 0 = 1", font_size=32, color=YELLOW).to_edge(UP*6.65 + RIGHT*4)        

        # Split the result into tens and units
        result_tens = Tex("1", color=BLUE).scale(1.1)
        result_units = Tex("8", color=BLUE).scale(1.1)
        result_units.next_to(addition1[2], DOWN).shift(RIGHT * 0.2)
        result_tens.next_to(result_units, LEFT*0.4)        
      
        # Add the title and underline to the scene
        self.add(title_1, underline)
        self.wait(0.3)
        self.play(Write(sub_title1))
        self.wait(0.5)
        self.play(FadeOut(sub_title1))
        self.wait(0.5)
        self.play(Write(result_units))  # Write the units place first
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(0.5)
        self.play(FadeOut(sub_title2))
        self.wait(0.5)
        self.play(Write(result_tens))  # Write the tens place
        self.wait(1)

        # Fade out all elements
        self.play(
            FadeOut(title_1), 
            FadeOut(underline), 
            FadeOut(addition1[5]), 
            FadeOut(addition1[4]), 
            FadeOut(addition1[2]), 
            FadeOut(addition1[1]), 
            FadeOut(addition1[0]), 
            FadeOut(result_units), 
            FadeOut(result_tens)
        )


        # Addition 12 + 3 = 15
        addition1 = self.vertical_addition("12", "3", "15")
        addition1.move_to([-1, 0.5, 0])

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
        title_1 = Text("Calculations:", font_size=31, color=DARK_BROWN).to_edge(UP*5 + RIGHT*3.25)
        
        # Create an underline for the word "Calculations"
        underline = Line(start=title_1.get_left() + LEFT*0.4, end=title_1.get_left() + RIGHT*1.79, color=GOLD, stroke_width=2)
        underline.next_to(title_1, DOWN, buff=0.1)       
    
        sub_title1 = Text("2 + 3 = 5", font_size=32, color=YELLOW).to_edge(UP*6.65 + RIGHT*4)
        sub_title2 = Text("1 + 0 = 1", font_size=32, color=YELLOW).to_edge(UP*6.65 + RIGHT*4)        

        # Split the result into tens and units
        result_tens = Tex("1", color=BLUE).scale(1.1)
        result_units = Tex("5", color=BLUE).scale(1.1)
        result_units.next_to(addition1[2], DOWN).shift(RIGHT * 0.2)
        result_tens.next_to(result_units, LEFT*0.4)        
      
        # Add the title and underline to the scene
        self.add(title_1, underline)
        self.wait(0.3)
        self.play(Write(sub_title1))
        self.wait(0.5)
        self.play(FadeOut(sub_title1))
        self.wait(0.5)
        self.play(Write(result_units))  # Write the units place first
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(0.5)
        self.play(FadeOut(sub_title2))
        self.wait(0.5)
        self.play(Write(result_tens))  # Write the tens place
        self.wait(1)

        # Fade out all elements
        self.play(
            FadeOut(title_1), 
            FadeOut(underline), 
            FadeOut(addition1[5]), 
            FadeOut(addition1[4]), 
            FadeOut(addition1[2]), 
            FadeOut(addition1[1]), 
            FadeOut(addition1[0]), 
            FadeOut(result_units), 
            FadeOut(result_tens)
        )


        # Addition 14 + 5 = 19
        addition1 = self.vertical_addition("14", "5", "19")
        addition1.move_to([-1, 0.5, 0])

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
        title_1 = Text("Calculations:", font_size=31, color=DARK_BROWN).to_edge(UP*5 + RIGHT*3.25)
        
        # Create an underline for the word "Calculations"
        underline = Line(start=title_1.get_left() + LEFT*0.4, end=title_1.get_left() + RIGHT*1.79, color=GOLD, stroke_width=2)
        underline.next_to(title_1, DOWN, buff=0.1)       
    
        sub_title1 = Text("4 + 5 = 9", font_size=32, color=YELLOW).to_edge(UP*6.65 + RIGHT*4)
        sub_title2 = Text("1 + 0 = 1", font_size=32, color=YELLOW).to_edge(UP*6.65 + RIGHT*4)        

        # Split the result into tens and units
        result_tens = Tex("1", color=BLUE).scale(1.1)
        result_units = Tex("9", color=BLUE).scale(1.1)
        result_units.next_to(addition1[2], DOWN).shift(RIGHT * 0.2)
        result_tens.next_to(result_units, LEFT*0.4)        
      
        # Add the title and underline to the scene
        self.add(title_1, underline)
        self.wait(0.3)
        self.play(Write(sub_title1))
        self.wait(0.5)
        self.play(FadeOut(sub_title1))
        self.wait(0.5)
        self.play(Write(result_units))  # Write the units place first
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(0.5)
        self.play(FadeOut(sub_title2))
        self.wait(0.5)
        self.play(Write(result_tens))  # Write the tens place
        self.wait(1)

        # Fade out all elements
        self.play(
            FadeOut(title_1), 
            FadeOut(underline), 
            FadeOut(addition1[5]), 
            FadeOut(addition1[4]), 
            FadeOut(addition1[2]), 
            FadeOut(addition1[1]), 
            FadeOut(addition1[0]), 
            FadeOut(result_units), 
            FadeOut(result_tens)
        )


    def vertical_subtraction(self, top_number, bottom_number, result):
        # Display the numbers vertically for subtraction
        numbers = VGroup(
            Tex(top_number).scale(1.1),       # Top number
            Tex("-" + bottom_number).scale(1.1),  # Bottom number
            Tex("\\underline{\\phantom{000}}").scale(2),  # Placeholder for upper underline
            Tex(result).scale(1.1),
            Tex("\\underline{\\phantom{000}}").scale(2)  # Placeholder for lower underline
        ).arrange(DOWN, buff=0.2)  # Vertical arrangement with buffer
        
        # Center the numbers on the screen
        numbers.move_to(ORIGIN)

        return numbers








if __name__ == "__main__":
    scene = TableScene()
    scene.render()
