from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class Addition(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.Add()
        self.NUM()
        self.vertical_addition_exercise_1()
        self.GithubSourceCodeReference()

    def Add(self):

        self.isRandom=False

        augend = MathTex("7").scale(3).move_to(LEFT)
        plus = MathTex("+").scale(3).next_to(augend, RIGHT)
        addend = MathTex("5").scale(3).next_to(plus, RIGHT)
        equals = MathTex("=").scale(3).next_to(addend, RIGHT)
        sum_result = MathTex("12").scale(3).next_to(equals, RIGHT)

        augend_label = Text("Augend", color=WHITE).scale(0.7).next_to(augend, LEFT)
        addend_label = Text("Addend", color=WHITE).scale(0.7).next_to(addend, DOWN)
        sum_label = Text("Sum", color=WHITE).scale(0.7).next_to(sum_result, RIGHT)
        plus_label = Text("Plus", color=WHITE).scale(0.7).next_to(plus, UP)


        self.play(Write(augend), Write(plus), Write(addend), Write(equals), Write(sum_result))
        self.play(Write(augend_label), Write(addend_label), Write(sum_label), Write(plus_label))        
        self.wait(2)
        self.fadeOutCurrentScene()

    def NUM(self):

        self.isRandom=False

        Title=Text("Addition").to_corner(UP)

        p1=cvo.CVO().CreateCVO("n1 + n2","33 + 44").setPosition([-4,0,0])

        p2=cvo.CVO().CreateCVO("n1","33").setPosition([3,2,0])

        p3=cvo.CVO().CreateCVO("n2","44").setPosition([3,-1,0])

        p4=cvo.CVO().CreateCVO("Result","77").setPosition([3,-3,0])

        self.play(Write(Title))
        self.construct1(p1,p1)
        self.construct1(p2,p2)
        self.play(Create(CurvedArrow(p1.pos,p2.pos)))
        self.construct1(p3,p3)
        self.play(Create(CurvedArrow(p1.pos,p3.pos)))
        self.construct1(p4,p4)
        self.play(Create(CurvedArrow(p1.pos,p4.pos)))
        self.fadeOutCurrentScene()

    def vertical_addition_exercise_1(self):
        # Title
        title = Tex("Solving the following additions:", color=PURPLE).to_edge(UP*1.5+LEFT*1)
        self.play(Write(title))
        
        # Addition 2 + 5 = 7
        addition1 = self.vertical_addition("2", "5", "7")
        addition1.move_to([-5.5, 1, 0])

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
        title = Text("Calculations:", font_size=31, color=DARK_BROWN).to_edge(UP*5 + RIGHT*3.25)
        
        # Create an underline for the word "Calculations"
        underline = Line(start=title.get_left() + LEFT*0.4, end=title.get_left() + RIGHT*1.79, color=GOLD, stroke_width=2)
        underline.next_to(title, DOWN, buff=0.1)
        
    
        sub_title1 = Text("2 + 5 = 7",font_size=32,color=YELLOW).to_edge(UP*6.65+RIGHT*4)

        # Split the result into tens and units
        result_units = Tex("7",color=BLUE).scale(1.1)
        result_units.next_to(addition1[2], DOWN).shift(RIGHT * 0.2)
        
        # Add the title and underline to the scene
        self.add(title, underline)
        self.wait(0.3)
        self.play(Write(sub_title1))
        self.wait(0.5)
        self.play(Write(result_units))  # Write the units place first
        self.wait(1)

        self.play(FadeOut(sub_title1), FadeOut(title), FadeOut(underline))

        # Addition 8 + 5 = 13
        addition6 = self.vertical_addition("8", "5", "13")
        addition6.move_to([-2.5, 1, 0])

        # Animate addition6
        self.play(Write(addition6[0]))  # Top number
        self.wait(0.5)
        self.play(Write(addition6[1]))  # Bottom number
        self.wait(0.5)
        self.play(Write(addition6[5]))  # Plus symbol
        self.wait(0.5)
        self.play(Write(addition6[2]))  # First underline
        self.wait(0.5)
        self.play(Write(addition6[4]))  # Second underline
        self.wait(0.5)

        # Create the title text
        title = Text("Calculations:", font_size=31, color=DARK_BROWN).to_edge(UP*5 + RIGHT*3.25)
        
        # Create an underline for the word "Calculations"
        underline = Line(start=title.get_left() + LEFT*0.4, end=title.get_left() + RIGHT*1.79, color=GOLD, stroke_width=2)
        underline.next_to(title, DOWN, buff=0.1)
        

        sub_title11 = Text("8 + 5 = 13",font_size=32,color=YELLOW).to_edge(UP*6.65+RIGHT*4)

        # Split the result of addition6 into tens and units
        result_tens_6 = Tex("1",color=BLUE).scale(1.1)
        result_units_6 = Tex("3",color=BLUE).scale(1.1)
        result_units_6.next_to(addition6[2], DOWN).shift(RIGHT * 0.2)
        result_tens_6.next_to(result_units_6, LEFT*0.4)
        

        self.add(title, underline)
        self.wait(0.5)
        self.play(Write(sub_title11))
        self.wait(0.5)
        self.play(Write(result_units_6))  # Write the units place first
        self.wait(1)
        self.play(Write(result_tens_6))  # Write the tens place
        self.wait(1)

        self.play(FadeOut(sub_title11), FadeOut(title), FadeOut(underline))

        # Addition 34 + 43 = 77
        addition6 = self.vertical_addition("34", "43", "77")
        addition6.move_to([-5.5, -2, 0])

        # Animate addition6
        self.play(Write(addition6[0]))  # Top number
        self.wait(0.5)
        self.play(Write(addition6[1]))  # Bottom number
        self.wait(0.5)
        self.play(Write(addition6[5]))  # Plus symbol
        self.wait(0.5)
        self.play(Write(addition6[2]))  # First underline
        self.wait(0.5)
        self.play(Write(addition6[4]))  # Second underline
        self.wait(0.5)

        # Create the title text
        title = Text("Calculations:", font_size=31, color=DARK_BROWN).to_edge(UP*5 + RIGHT*3.25)
        
        # Create an underline for the word "Calculations"
        underline = Line(start=title.get_left() + LEFT*0.4, end=title.get_left() + RIGHT*1.79, color=GOLD, stroke_width=2)
        underline.next_to(title, DOWN, buff=0.1)
        

        sub_title11 = Text("4 + 3 = 7",font_size=32,color=YELLOW).to_edge(UP*6.65+RIGHT*4)
        sub_title12 = Text("3 + 4 = 7",font_size=32,color=YELLOW).to_edge(UP*8.3+RIGHT*4)

        # Split the result of addition6 into tens and units
        result_tens_6 = Tex("7",color=BLUE).scale(1.1)
        result_units_6 = Tex("7",color=BLUE).scale(1.1)
        result_units_6.next_to(addition6[2], DOWN).shift(RIGHT * 0.2)
        result_tens_6.next_to(result_units_6, LEFT*0.4)
        

        self.add(title, underline)
        self.wait(0.5)
        self.play(Write(sub_title11))
        self.wait(0.5)
        self.play(Write(result_units_6))  # Write the units place first
        self.wait(1)
        self.play(Write(sub_title12))
        self.wait(0.5)
        self.play(Write(result_tens_6))  # Write the tens place
        self.wait(1)

        self.play(FadeOut(sub_title11), FadeOut(sub_title12), FadeOut(title), FadeOut(underline))



        
        # Addition 13 + 9 = 22
        addition5 = self.vertical_addition("13", "9", "22")
        addition5.move_to([-2.5, -2, 0])

        # Animate addition5
        self.play(Write(addition5[0]))  # Top number
        self.wait(0.5)
        self.play(Write(addition5[1]))  # Bottom number
        self.wait(0.5)
        self.play(Write(addition5[5]))  # Plus symbol
        self.wait(0.5)
        self.play(Write(addition5[2]))  # First underline
        self.wait(0.5)
        self.play(Write(addition5[4]))  # Second underline
        self.wait(0.5)

        # Create the title text
        title = Text("Calculations:", font_size=31, color=DARK_BROWN).to_edge(UP*5 + RIGHT*3.25)
        
        # Create an underline for the word "Calculations"
        underline = Line(start=title.get_left() + LEFT*0.4, end=title.get_left() + RIGHT*1.79, color=GOLD, stroke_width=2)
        underline.next_to(title, DOWN, buff=0.1)

        sub_title9 = Text("3 + 9 = 12",font_size=32,color=YELLOW).to_edge(UP*6.65+RIGHT*4)
        sub_title10 = Text("1 + 1 = 2",font_size=32,color=YELLOW).to_edge(UP*8.3+RIGHT*4)

        # Split the result of addition5 into tens and units
        result_tens_5 = Tex("2",color=BLUE).scale(1.1)
        result_units_5 = Tex("2",color=BLUE).scale(1.1)
        result_units_5.next_to(addition5[2], DOWN).shift(RIGHT * 0.2)
        result_tens_5.next_to(result_units_5, LEFT*0.4)
        
        self.add(title, underline)
        self.wait(0.5)
        self.play(Write(sub_title9))
        self.wait(0.5)
        self.play(Write(result_units_5))  # Write the units place first
        self.wait(1)
        self.play(Write(sub_title10))
        self.wait(0.5)
        self.play(Write(result_tens_5))  # Write the tens place
        self.wait(1)

        self.play(FadeOut(sub_title9), FadeOut(sub_title10), FadeOut(title), FadeOut(underline))





    def vertical_addition(self, top_number, bottom_number, result):
        numbers = VGroup(
            Tex(top_number).scale(1.1),
            Tex(bottom_number).scale(1.1),
            Tex("\\underline{\\phantom{0000}}").scale(2),
            Tex(result).scale(1.1),
            Tex("\\underline{\\phantom{0000}}").scale(2),
            Tex("+").scale(1.1)
        ).arrange(DOWN, buff=0.2)

        numbers.move_to(ORIGIN)

        numbers[1].next_to(numbers[0], DOWN)
        numbers[5].next_to(numbers[1], LEFT)

        return numbers


        

    def SetDeveloperList(self):
        self.DeveloperList="Bhaskar"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade3Chapter3Addition.py"

if __name__ == "__main__":
    scene = Addition()
    scene.render()
