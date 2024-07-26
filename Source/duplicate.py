from manim import *
import cvo
from AbstractAnim import AbstractAnim

class TableScene(AbstractAnim):
    def construct(self):
        self.CirleExamples()
        #self.ExampleExercise_1()
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


    






if __name__ == "__main__":
    scene = TableScene()
    scene.render()
