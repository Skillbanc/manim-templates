from manim import*
import json
import cvo
from AbstractAnim import AbstractAnim

class SubtractionofNumbersupto9(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.Extra_text()
        self.fadeOutCurrentScene()
        self.Subtraction()
        self.fadeOutCurrentScene()
        self.CirleExamples()
        self.fadeOutCurrentScene()
        self.Square_Example()
        self.fadeOutCurrentScene()
        self.ExampleExercise_1()
        self.fadeOutCurrentScene()
        self.ExampleExercise_2()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()


    def Extra_text(self):
        title = Text("Chapter8 : Subtraction of Numbers upto 9", font_size=48)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))
        

    def Subtraction(self):
        self.isRandom=False
        self.setNumberOfCirclePositions(2)
        p10=cvo.CVO().CreateCVO("Subtraction","").setPosition([-4.5,1,0])
        p11=cvo.CVO().CreateCVO("definition","Subtraction is finding the difference between numbers").setPosition([1.5,2,0]).setangle(-TAU/4)
        p12=cvo.CVO().CreateCVO("Symbol","-").setPosition([3.5,-1,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)

        p11.setcircleradius(1.25)
        self.construct1(p10,p10)



    def CirleExamples(self):
        example = Text("Find the remaining things:", font_size=34).to_edge(UP*1+LEFT*1)

        # Subtraction Example: 5 - 2 = 3

        # Circles for the number 5
        c1 = Circle(radius=0.3, color=BLUE).to_edge(LEFT * 3 + UP * 3.5).set_fill(opacity=0.4)
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

        # Subtraction Example: 6 - 4 = 2
        # Circles for the number 6
        c1 = Circle(radius=0.3, color=GRAY).to_edge(LEFT * 1.5 + UP * 7.25).set_fill(opacity=0.4)
        c2 = Circle(radius=0.3, color=GRAY).next_to(c1, RIGHT * 1.2).set_fill(opacity=0.4)
        c3 = Circle(radius=0.3, color=GRAY).next_to(c2, RIGHT * 1.2).set_fill(opacity=0.4)
        c4 = Circle(radius=0.3, color=GRAY).next_to(c3, RIGHT * 1.2).set_fill(opacity=0.4)
        c5 = Circle(radius=0.3, color=GRAY).next_to(c4, RIGHT * 1.2).set_fill(opacity=0.4)
        c6 = Circle(radius=0.3, color=GRAY).next_to(c5, RIGHT * 1.2).set_fill(opacity=0.4)
        six = Text("6").next_to(c3, DOWN).shift(RIGHT * 0.5)

        minus2 = Text("-").next_to(c6, RIGHT * 1.2)

        # Circles for the number 4
        s1 = Circle(radius=0.3, color=GRAY).next_to(minus2, RIGHT * 1.2).set_fill(opacity=0.4)
        s2 = Circle(radius=0.3, color=GRAY).next_to(s1, RIGHT * 1.2).set_fill(opacity=0.4)
        s3 = Circle(radius=0.3, color=GRAY).next_to(s2, RIGHT * 1.2).set_fill(opacity=0.4)
        s4 = Circle(radius=0.3, color=GRAY).next_to(s3, RIGHT * 1.2).set_fill(opacity=0.4)

        four = Text("4").next_to(s2, DOWN).shift(RIGHT * 0.5)

        equal2 = Text("=").next_to(s4, RIGHT * 1.2)

        # Circles for the result 2
        result_c1 = Circle(radius=0.3, color=GRAY).next_to(equal2, RIGHT * 1.2).set_fill(opacity=0.4)
        result_c2 = Circle(radius=0.3, color=GRAY).next_to(result_c1, RIGHT * 1.2).set_fill(opacity=0.4)

        two = Text("2").next_to(result_c1, DOWN).shift(RIGHT * 0.5)

        # Animation for the second example
        self.play(Write(c1), Write(c2), Write(c3), Write(c4), Write(c5), Write(c6))
        self.play(Write(six))
        self.play(Write(minus2))
        self.play(Write(s1), Write(s2), Write(s3), Write(s4))
        self.play(Write(four))
        self.play(Write(equal2))
        self.play(Write(result_c1), Write(result_c2))
        self.play(Write(two))

        # Subtraction Example: 7 - 3 = 4

        # Circles for the number 7
        c1 = Circle(radius=0.3, color=DARK_BROWN).to_edge(LEFT * 1 + UP * 11.75).set_fill(opacity=0.4)
        c2 = Circle(radius=0.3, color=DARK_BROWN).next_to(c1, RIGHT * 1.2).set_fill(opacity=0.4)
        c3 = Circle(radius=0.3, color=DARK_BROWN).next_to(c2, RIGHT * 1.2).set_fill(opacity=0.4)
        c4 = Circle(radius=0.3, color=DARK_BROWN).next_to(c3, RIGHT * 1.2).set_fill(opacity=0.4)
        c5 = Circle(radius=0.3, color=DARK_BROWN).next_to(c4, RIGHT * 1.2).set_fill(opacity=0.4)
        c6 = Circle(radius=0.3, color=DARK_BROWN).next_to(c5, RIGHT * 1.2).set_fill(opacity=0.4)
        c7 = Circle(radius=0.3, color=DARK_BROWN).next_to(c6, RIGHT * 1.2).set_fill(opacity=0.4)
        seven = Text("7").next_to(c4, DOWN)

        minus3 = Text("-").next_to(c7, RIGHT * 1.2)

        # Circles for the number 3
        s1 = Circle(radius=0.3, color=DARK_BROWN).next_to(minus3, RIGHT * 1.2).set_fill(opacity=0.4)
        s2 = Circle(radius=0.3, color=DARK_BROWN).next_to(s1, RIGHT * 1.2).set_fill(opacity=0.4)
        s3 = Circle(radius=0.3, color=DARK_BROWN).next_to(s2, RIGHT * 1.2).set_fill(opacity=0.4)

        three = Text("3").next_to(s2, DOWN)

        equal3 = Text("=").next_to(s3, RIGHT * 1.2)

        # Circles for the result 4
        result_c1 = Circle(radius=0.3, color=DARK_BROWN).next_to(equal3, RIGHT * 1.2).set_fill(opacity=0.4)
        result_c2 = Circle(radius=0.3, color=DARK_BROWN).next_to(result_c1, RIGHT * 1.2).set_fill(opacity=0.4)
        result_c3 = Circle(radius=0.3, color=DARK_BROWN).next_to(result_c2, RIGHT * 1.2).set_fill(opacity=0.4)
        result_c4 = Circle(radius=0.3, color=DARK_BROWN).next_to(result_c3, RIGHT * 1.2).set_fill(opacity=0.4)

        four = Text("4").next_to(result_c2, DOWN).shift(RIGHT * 0.5)

        # Animation for the third example
        self.play(Write(c1), Write(c2), Write(c3), Write(c4), Write(c5), Write(c6), Write(c7))
        self.play(Write(seven))
        self.play(Write(minus3))
        self.play(Write(s1), Write(s2), Write(s3))
        self.play(Write(three))
        self.play(Write(equal3))
        self.play(Write(result_c1), Write(result_c2), Write(result_c3), Write(result_c4))
        self.play(Write(four))


        




    def Square_Example(self):
        example = Text("Examples:").to_edge(UP*1)

        # Subtraction Example: 3 - 2 = 1
        
        # Squares for the number 3
        box1 = Square(side_length=1, color=BLUE).to_edge(LEFT * 2 + UP * 3)
        box2 = Square(side_length=1, color=BLUE).next_to(box1, RIGHT * 1.2)
        box3 = Square(side_length=1, color=BLUE).next_to(box2, RIGHT * 1.2)
        three = Text("3").next_to(box2, DOWN).shift(RIGHT * 0.25)
        
        minus = Text("-").next_to(box3, RIGHT * 1.2)
        
        # Squares for the number 2
        box4 = Square(side_length=1, color=BLUE).next_to(minus, RIGHT * 1.2)
        box5 = Square(side_length=1, color=BLUE).next_to(box4, RIGHT * 1.2)
        two = Text("2").next_to(box4, DOWN).shift(RIGHT * 0.75)
        
        equal = Text("=").next_to(box5, RIGHT * 1.2)
        
        # Squares for the result 1
        box6 = Square(side_length=1, color=BLUE).next_to(equal, RIGHT * 1.2)
        result = Text("1").next_to(box6, DOWN)
        
        # Animation
        self.play(Write(example))
        self.play(Write(box1, run_time=2), Write(box2, run_time=2), Write(box3, run_time=2))
        self.play(Write(three))
        self.play(Write(minus))
        self.play(Write(box4, run_time=2), Write(box5, run_time=2))
        self.play(Write(two))
        self.play(Write(equal))
        self.play(Write(box6, run_time=2))
        self.play(Write(result))

        self.wait(3)
        
       

        #Example 4 - 2 = 2
        # Circles for the number 4
        box1 = Square(side_length=1, color=GREY).to_edge(LEFT * 2+UP*7.2)
        box2 = Square(side_length=1, color=GREY).next_to(box1, RIGHT * 1.2)
        box3 = Square(side_length=1, color=GREY).next_to(box2, RIGHT * 1.2)
        box4 = Square(side_length=1, color=GREY).next_to(box3, RIGHT * 1.2)
        four = Text("4").next_to(box3, DOWN).shift(LEFT * 0.75)
        
        minus = Text("-").next_to(box4, RIGHT * 1.2)
        
        # Circles for the number 2
        box5 = Square(side_length=1, color=GREY).next_to(minus, RIGHT * 1.2)
        box6 = Square(side_length=1, color=GREY).next_to(box5, RIGHT * 1.2)
        two = Text("2").next_to(box5, DOWN).shift(RIGHT * 0.75)
        
        equal = Text("=").next_to(box6, RIGHT * 1.2)
        
        # Circles for the result 2
        box7 = Square(side_length=1, color=GREY).next_to(equal, RIGHT * 1.2)
        box8 = Square(side_length=1, color=GREY).next_to(box7, RIGHT * 1.2)
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





    
        # Circles for the number 5 -1 = 4 
        box1 = Square(side_length=1, color=PURPLE).to_edge(LEFT * 1+UP*11.2)
        box2 = Square(side_length=1, color=PURPLE).next_to(box1, RIGHT * 1.2)
        box3 = Square(side_length=1, color=PURPLE).next_to(box2, RIGHT * 1.2)
        box4 = Square(side_length=1, color=PURPLE).next_to(box3, RIGHT * 1.2)
        box5 = Square(side_length=1, color=PURPLE).next_to(box4, RIGHT * 1.2)
        five = Text("5").next_to(box3, DOWN)
        
        minus = Text("-").next_to(box5, RIGHT * 1.2)
        
        # Circles for the number 1
        box6 = Square(side_length=1, color=PURPLE).next_to(minus, RIGHT * 1.2)
        one = Text("1").next_to(box6, DOWN)
        
        equal = Text("=").next_to(box6, RIGHT * 1.2)
        
        # Circles for the result 4
        box7 = Square(side_length=1, color=PURPLE).next_to(equal, RIGHT * 1.2)
        box8 = Square(side_length=1, color=PURPLE).next_to(box7, RIGHT * 0.5)
        box9 = Square(side_length=1, color=PURPLE).next_to(box8, RIGHT * 0.5)
        box10 = Square(side_length=1, color=PURPLE).next_to(box9, RIGHT * 0.5)
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




    def ExampleExercise_1(self):
        # Create and display the initial text
        t1 = Text("Calculate the differences for the following pairs of numbers:", font_size=35).to_edge(UP + LEFT * 1)
        self.play(Write(t1))
        
        # Define and display the subtractions
        s1 = Text("6 - 4 = ", color=PINK, font_size=30).to_edge(LEFT * 4.5 + UP * 3.5)
        ss1 = Square(side_length=0.7).next_to(s1, RIGHT)
        s12 = Text("2", color=BLUE, font_size=30).move_to(ss1.get_center())
        self.play(Write(s1, run_time=3))
        self.play(Write(ss1, run_time=2))
        self.play(Write(s12))
        
        s2 = Text("9 - 2 = ", color=PINK, font_size=30).next_to(s1, DOWN * 3)
        ss2 = Square(side_length=0.7).next_to(s2, RIGHT)
        s22 = Text("7", color=BLUE, font_size=30).move_to(ss2.get_center())
        self.play(Write(s2, run_time=3))
        self.play(Write(ss2, run_time=2))
        self.play(Write(s22))

        s3 = Text("7 - 4 = ", color=PINK, font_size=30).next_to(s2, DOWN * 3)
        ss3 = Square(side_length=0.7).next_to(s3, RIGHT)
        s32 = Text("3", color=BLUE, font_size=30).move_to(ss3.get_center())
        self.play(Write(s3, run_time=3))
        self.play(Write(ss3, run_time=2))
        self.play(Write(s32))

        s4 = Text("4 - 0 = ", color=PINK, font_size=30).next_to(s3, DOWN * 3)
        ss4 = Square(side_length=0.7).next_to(s4, RIGHT)
        s42 = Text("4", color=BLUE, font_size=30).move_to(ss4.get_center())
        self.play(Write(s4, run_time=3))
        self.play(Write(ss4, run_time=2))
        self.play(Write(s42))

        s5 = Text("8 - 2 = ", color=PINK, font_size=30).next_to(s4, DOWN * 3)
        ss5 = Square(side_length=0.7).next_to(s5, RIGHT)
        s52 = Text("6", color=BLUE, font_size=30).move_to(ss5.get_center())
        self.play(Write(s5, run_time=3))
        self.play(Write(ss5, run_time=2))
        self.play(Write(s52))

        s7 = Text("5 - 1 = ", color=PINK, font_size=30).next_to(s1, RIGHT * 20.5)
        ss7 = Square(side_length=0.7).next_to(s7, RIGHT)
        s72 = Text("4", color=BLUE, font_size=30).move_to(ss7.get_center())
        self.play(Write(s7, run_time=3))
        self.play(Write(ss7, run_time=2))
        self.play(Write(s72))
        
        s8 = Text("3 - 3 = ", color=PINK, font_size=30).next_to(s7, DOWN * 3)
        ss8 = Square(side_length=0.7).next_to(s8, RIGHT)
        s82 = Text("0", color=BLUE, font_size=30).move_to(ss8.get_center())
        self.play(Write(s8, run_time=3))
        self.play(Write(ss8, run_time=2))
        self.play(Write(s82))

        s9 = Text("7 - 5 = ", color=PINK, font_size=30).next_to(s8, DOWN * 3)
        ss9 = Square(side_length=0.7).next_to(s9, RIGHT)
        s92 = Text("2", color=BLUE, font_size=30).move_to(ss9.get_center())
        self.play(Write(s9, run_time=3))
        self.play(Write(ss9, run_time=2))
        self.play(Write(s92))

        s10 = Text("8 - 4 = ", color=PINK, font_size=30).next_to(s9, DOWN * 3)
        ss10 = Square(side_length=0.7).next_to(s10, RIGHT)
        s102 = Text("4", color=BLUE, font_size=30).move_to(ss10.get_center())
        self.play(Write(s10, run_time=3))
        self.play(Write(ss10, run_time=2))
        self.play(Write(s102))

        s11 = Text("9 - 4 = ", color=PINK, font_size=30).next_to(s10, DOWN * 3)
        ss11 = Square(side_length=0.7).next_to(s11, RIGHT)
        s112 = Text("5", color=BLUE, font_size=30).move_to(ss11.get_center())
        self.play(Write(s11, run_time=3))
        self.play(Write(ss11, run_time=2))
        self.play(Write(s112))

        # Fade out all elements
        self.play(
            FadeOut(s1), FadeOut(ss1), FadeOut(s12),
            FadeOut(s2), FadeOut(ss2), FadeOut(s22),
            FadeOut(s3), FadeOut(ss3), FadeOut(s32),
            FadeOut(s4), FadeOut(ss4), FadeOut(s42),
            FadeOut(s5), FadeOut(ss5), FadeOut(s52),
            FadeOut(s7), FadeOut(ss7), FadeOut(s72),
            FadeOut(s8), FadeOut(ss8), FadeOut(s82),
            FadeOut(s9), FadeOut(ss9), FadeOut(s92),
            FadeOut(s10), FadeOut(ss10), FadeOut(s102),
            FadeOut(s11), FadeOut(ss11), FadeOut(s112),
            FadeOut(t1)
        )


    def ExampleExercise_2(self):
        # Title
        title = Tex("Solving the following subtractions :",color=BLUE).to_edge(UP*1.5+LEFT*1)
        self.play(Write(title))
        
        # Subtraction 9 - 6
        subtraction1 = self.vertical_subtraction("9", "6", "3")
        subtraction1.move_to([-5,0,0])

        # Subtraction 6 - 5
        subtraction2 = self.vertical_subtraction("6", "5", "1")
        subtraction2.move_to([-2.5,0,0])

        # Subtraction 5 - 3
        subtraction3 = self.vertical_subtraction("5", "3", "2")
        subtraction3.move_to([0,0,0])

        # Subtraction 6 - 6
        subtraction4 = self.vertical_subtraction("6", "6", "0")
        subtraction4.move_to([2.5,0,0])

        # Subtraction 7 - 2
        subtraction5 = self.vertical_subtraction("7", "2", "5")
        subtraction5.move_to([5,0,0])

        # Animate sequentially
        self.play(Create(subtraction1))
        self.wait(1)
        self.play(Create(subtraction2))
        self.wait(1)
        self.play(Create(subtraction3))
        self.wait(2)
        self.play(Create(subtraction4))
        self.wait(2)
        self.play(Create(subtraction5))
        self.wait(2)


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




    def SetDeveloperList(self):  
        self.DeveloperList="Raghu"

        
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="SubtractionofNumbersupto9.py"




if __name__=="__main__":
    Scene=SubtractionofNumbersupto9()
    Scene.render()