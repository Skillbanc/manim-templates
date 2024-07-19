from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class NUM10to99(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.TenAnd99()
        self.create_number_representation()
        self.tento99()
        self.AscAndDescOrder()
        self.exercise()
        self.OneTo99()
        self.GithubSourceCodeReference()
        self.SubscribeYoutube()
        self.fadeOutCurrentScene()
        
    def TenAnd99(self):
        self.isRandom=False
        self.angleChoice=[TAU/5,TAU/5]
        p1=cvo.CVO().CreateCVO("Numbers 10 and 99","").setPosition([-5,0,0])
        p2=cvo.CVO().CreateCVO("10 is the smallest two digit number","").setPosition([3,2,0])
        p3=cvo.CVO().CreateCVO("99 is the largest two digit number","").setPosition([3,-2,0])
        p1.cvolist.append(p2)
        p1.cvolist.append(p3)
        self.construct1(p1,p1)
        self.wait(2)
        self.fadeOutCurrentScene()
        
    def create_number_representation(self):
        number_line = NumberLine(
            x_range=[0, 100, 10],
            length=10,
            color=BLUE,
            include_numbers=True,
            label_direction=UP
        )
        self.play(Create(number_line,run_time=3))
        self.wait(1)

        tens_label = Text("Tens", color=GREEN).to_edge(UP + LEFT)
        units_label = Text("Ones", color=YELLOW).to_edge(UP + RIGHT)
        self.play(Write(tens_label), Write(units_label))
        self.wait(1)

        def show_number(num, position):
            tens_digit = num // 10
            units_digit = num % 10

            number_group = VGroup(
                Text(str(tens_digit), color=GREEN).scale(2),
                Text(str(units_digit), color=YELLOW).scale(2)
            ).arrange(RIGHT).move_to(UP * 2)

            self.play(Write(number_group))
            tens_arrow = Arrow(start=Text("Tens").to_edge(UP + LEFT).get_bottom(), end=number_group[0].get_top(), color=GREEN)
            ones_arrow = Arrow(start=Text("Ones").to_edge(UP + RIGHT).get_bottom(), end=number_group[1].get_top(), color=YELLOW)
            self.play(Create(tens_arrow), Create(ones_arrow))

            self.wait(2)
            self.play(FadeOut(number_group), FadeOut(tens_arrow), FadeOut(ones_arrow))

        def mark_number_on_line(num):
            dot = Dot(number_line.n2p(num), color=RED)
            number_text = Text(str(num), color=RED).next_to(dot, DOWN)
            self.play(Create(dot), Write(number_text))
            self.wait(0.5)

        key_numbers = [10, 23, 45, 67, 89]
        for i, number in enumerate(key_numbers):
            position = DOWN + i * 0.5 * DOWN
            mark_number_on_line(number)
            show_number(number, position)

        self.wait(1)
        self.fadeOutCurrentScene()

    def tento99(self):
        def create_bundle(x, y):
            bundle = VGroup(*[Line(ORIGIN, UP) for _ in range(10)])
            bundle.arrange(RIGHT, buff=0.1).scale(0.6)
            bundle.move_to([x, y, 0])
            return bundle

        row0_bundles=[create_bundle(-6.5,3)]
        row1_bundles = [create_bundle(-6.5, 2), create_bundle(-5, 2)]
        row2_bundles = [create_bundle(-6.5, 1), create_bundle(-5.5, 1), create_bundle(-4, 1)]
        row3_bundles = [create_bundle(-6.5, 0), create_bundle(-5.5, 0), create_bundle(-4.5, 0), create_bundle(-3, 0)]
        row4_bundles = [create_bundle(-6.5, -1), create_bundle(-5.5,-1),create_bundle(-4.5,-1),create_bundle(-3.5,-1),create_bundle(-2,-1)]
        row5_bundles = [create_bundle(-6.5, -2), create_bundle(-5.5,-2),create_bundle(-4.5,-2),create_bundle(-3.5,-2),create_bundle(-2.5,-2),create_bundle(-1,-2)]
        row6_bundles = [create_bundle(-6.5, -3), create_bundle(-5.5,-3),create_bundle(-4.5,-3),create_bundle(-3.5,-3),create_bundle(-2.5,-3),create_bundle(-1.5,-3),create_bundle(0,-3)]

        row0_equation = MathTex("10").move_to([4,3,0]).scale(0.7)
        row1_equation = MathTex("10", "+", "10", "=", "20").move_to([5, 2, 0]).scale(0.7)
        row2_equation = MathTex("20", "+", "10", "=", "30").move_to([5, 1, 0]).scale(0.7)
        row3_equation = MathTex("30", "+", "10", "=", "40").move_to([5, 0, 0]).scale(0.7)
        row4_equation = MathTex("40", "+", "10", "=", "50").move_to([5, -1, 0]).scale(0.7)
        row5_equation = MathTex("50", "+", "10", "=", "60").move_to([5, -2, 0]).scale(0.7)
        row6_equation = MathTex("60", "+", "10", "=", "70").move_to([5, -3, 0]).scale(0.7)

        for bundle in row0_bundles:
            self.play(FadeIn(bundle))
        self.play(Write(row0_equation))

        for bundle in row1_bundles:
            self.play(FadeIn(bundle))
        self.play(Write(row1_equation))

        for bundle in row2_bundles:
            self.play(FadeIn(bundle))
        self.play(Write(row2_equation))

        for bundle in row3_bundles:
            self.play(FadeIn(bundle))
        self.play(Write(row3_equation))

        for bundle in row4_bundles:
            self.play(FadeIn(bundle))
        self.play(Write(row4_equation))

        for bundle in row5_bundles:
            self.play(FadeIn(bundle))
        self.play(Write(row5_equation))

        for bundle in row6_bundles:
            self.play(FadeIn(bundle))
        self.play(Write(row6_equation))
        self.wait(2)
        self.fadeOutCurrentScene()

        row7_bundles = [create_bundle(-6.5, 3), create_bundle(-5.5,3),create_bundle(-4.5,3),create_bundle(-3.5,3),create_bundle(-2.5,3),create_bundle(-1.5,3),create_bundle(-0.5,3),create_bundle(1,3)]
        row8_bundles = [create_bundle(-6.5, 2), create_bundle(-5.5,2),create_bundle(-4.5,2),create_bundle(-3.5,2),create_bundle(-2.5,2),create_bundle(-1.5,2),create_bundle(-0.5,2),create_bundle(0.5,2),create_bundle(2,2)]
        row9_bundles = [create_bundle(-6.5, 1), create_bundle(-5.5,1),create_bundle(-4.5,1),create_bundle(-3.5,1),create_bundle(-2.5,1),create_bundle(-1.5,1),create_bundle(-0.5,1),create_bundle(0.5,1),create_bundle(1.5,1),create_bundle(2.5,1)]



        row7_equation = MathTex("70", "+", "10", "=", "80").move_to([5, 3, 0]).scale(0.7)
        row8_equation = MathTex("80", "+", "10", "=", "90").move_to([5, 2, 0]).scale(0.7)
        row9_equation = MathTex("90", "+", "10", "=", "100").move_to([5, 1, 0]).scale(0.7)

        for bundle in row7_bundles:
            self.play(FadeIn(bundle))
        self.play(Write(row7_equation))

        for bundle in row8_bundles:
            self.play(FadeIn(bundle))
        self.play(Write(row8_equation))

        for bundle in row9_bundles:
            self.play(FadeIn(bundle))
        self.play(Write(row9_equation))
        self.wait(2)
        self.fadeOutCurrentScene()
        
    def AscAndDescOrder(self):
        title = Text("Ascending and Descending Order", font_size=50)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))
        asc_text = Text("Ascending Order", color=BLUE, font_size=50).to_edge(UP)
        self.play(Write(asc_text))
        text=Text("Arranging the numbers from the smallest to the biggest is known as \n\n ASCENDING  ORDER",font_size=30).shift(UP *2 )
        self.play(Write(text))
        asc_num=[25,49,92,85,79,12,68,56,37]
        asc1_group = VGroup().next_to(text,DOWN,buff=1)
        for i, num in enumerate(asc_num):
            num_text = Text(str(num), font_size=36)
            asc1_group.add(num_text)
        asc1_group.arrange(RIGHT, buff=0.5)
        self.play(Write(asc1_group))
        text1=Text("Sorted Numbers").next_to(asc1_group,DOWN,buff=0.5)
        self.play(Write(text1))
        ascending_numbers = [12, 25, 37, 49, 56, 68, 79, 85, 92]
        asc_group = VGroup()
        for i, num in enumerate(ascending_numbers):
            num_text = Text(str(num), font_size=36)
            asc_group.add(num_text)
        asc_group.arrange(RIGHT, buff=0.5)
        asc_group.shift(DOWN*2.3)
        self.play(FadeIn(asc_group))

        for i, num_text in enumerate(asc_group):
            if i > 0:
                self.play(
                    num_text.animate.shift(UP * 0.5),
                    asc_group[i - 1].animate.shift(DOWN * 0.5)
                )
                self.wait(0.5)
        self.fadeOutCurrentScene()

        desc_text = Text("Descending Order", color=GREEN, font_size=50).to_edge(UP)
        self.play(Write(desc_text))
        text=Text("Arranging the  numbers from the biggest to the smallest is known as \n\n DESCENDING  ORDER",font_size=30).shift(UP *2)
        self.play(Write(text))
        desc_num=[54,99,34,67,18,20,45,77]
        desc1_group = VGroup().next_to(text,DOWN,buff=1)
        for i, num in enumerate(desc_num):
            num_text = Text(str(num), font_size=36)
            desc1_group.add(num_text)
        desc1_group.arrange(RIGHT, buff=0.5)
        self.play(Write(desc1_group))
        text1=Text("Sorted Numbers").next_to(desc1_group,DOWN,buff=0.5)
        self.play(Write(text1))
        descending_numbers = [99, 77, 67, 54, 45, 34, 20, 18]
        desc_group = VGroup()
        for i, num in enumerate(descending_numbers):
            num_text = Text(str(num), font_size=36)
            desc_group.add(num_text)
        desc_group.arrange(RIGHT, buff=0.5)
        desc_group.shift(DOWN*2.3)
        self.play(FadeIn(desc_group))

        for i, num_text in enumerate(desc_group):
            if i > 0:
                self.play(
                    num_text.animate.shift(UP * 0.5),
                    desc_group[i - 1].animate.shift(DOWN * 0.5)
                )
                self.wait(0.5)
        self.fadeOutCurrentScene()

    def exercise(self):
        title = Text("Finding the Number of Tens", font_size=30).to_edge(UP)
        self.play(Write(title))
        part_a_title = Text("Look at the number. Write how many tens there are in it?", font_size=24).next_to(title, DOWN, buff=0.3)
        self.play(Write(part_a_title))

        example_table = [
            ("80", ""), 
            ("30", ""), 
            ("50", ""), 
            ("90", ""),
            ("20",""),
            ("70",""),
            ("10","")
        ]
        first_boxes = [VGroup(Square(0.5), Square(0.5)).arrange(RIGHT, buff=0.1) for _ in example_table]
        first_group = VGroup(*first_boxes).arrange(DOWN, buff=0.3).shift(DOWN * 2,RIGHT*1).next_to(part_a_title,DOWN)
        for box in first_boxes:
            self.play(Create(box,run_time=0.5))

        for i, (a, b) in enumerate(example_table):
            self.play(Write(Text(a).scale(0.5).move_to(first_boxes[i][0])))
            self.play(Write(Text(b).scale(0.5).move_to(first_boxes[i][1])))
        self.wait(4)
        example_table = [
            ("", "8"), 
            ("", "3"), 
            ("", "5"), 
            ("", "9"),
            ("","2"),
            ("","7"),
            ("","1")
        ]
        first_boxes = [VGroup(Square(0.5), Square(0.5)).arrange(RIGHT, buff=0.1) for _ in example_table]
        first_group = VGroup(*first_boxes).arrange(DOWN, buff=0.3).shift(DOWN * 2,RIGHT*1).next_to(part_a_title,DOWN)
        for box in first_boxes:
            self.play(Create(box,run_time=0.5))

        for i, (a, b) in enumerate(example_table):
            self.play(Write(Text(a).scale(0.5).move_to(first_boxes[i][0])))
            self.play(Write(Text(b).scale(0.5).move_to(first_boxes[i][1])))
        self.wait(2)
        self.fadeOutCurrentScene()

        part_b_title = Text("Fill in the blank boxes with the correct numbers", font_size=24).to_edge(UP)
        self.play(Write(part_b_title))

        fill_table = [
            ("50", ""), 
            ("", "6"), 
            ("", "7"), 
            ("40", ""),
            ("","2"),
            ("","3"),
            ("10","")
        ]
        second_boxes = [VGroup(Square(0.5), Square(0.5)).arrange(RIGHT, buff=0.1) for _ in fill_table]
        second_group = VGroup(*second_boxes).arrange(DOWN, buff=0.3).shift(DOWN * 2,RIGHT*1).next_to(part_b_title,DOWN)
        for box in second_boxes:
            self.play(Create(box,run_time=0.5))

        for i, (a, b) in enumerate(fill_table):
            self.play(Write(Text(a).scale(0.5).move_to(second_boxes[i][0])))
            self.play(Write(Text(b).scale(0.5).move_to(second_boxes[i][1])))
        self.wait(4)
        fill_table = [
            ("", "5"), 
            ("60", ""), 
            ("70", ""), 
            ("", "4"),
            ("20",""),
            ("30",""),
            ("","1")
        ]
        second_boxes = [VGroup(Square(0.5), Square(0.5)).arrange(RIGHT, buff=0.1) for _ in fill_table]
        second_group = VGroup(*second_boxes).arrange(DOWN, buff=0.3).shift(DOWN * 2,RIGHT*1).next_to(part_b_title,DOWN)
        for box in second_boxes:
            self.play(Create(box,run_time=0.5))

        for i, (a, b) in enumerate(fill_table):
            self.play(Write(Text(a).scale(0.5).move_to(second_boxes[i][0])))
            self.play(Write(Text(b).scale(0.5).move_to(second_boxes[i][1])))
        self.wait(2)
        self.fadeOutCurrentScene()

    def OneTo99(self):
        title = Text("Numbers from 1 to 99", font_size=36).to_edge(LEFT)
        self.play(Write(title))
        self.wait(1)
        number_grid = VGroup()
        for i in range(1, 100):
            num_text = Text(str(i), font_size=20)
            number_grid.add(num_text)
        number_grid.arrange_in_grid(rows=10, cols=10, buff=0.5).move_to(RIGHT * 3)
        self.play(Write(number_grid,run_time=10))
        self.wait(4)
        self.fadeOutCurrentScene()
    
    def SetDeveloperList(self):
        self.DeveloperList="Srujan"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade2Chapter2Numbers10to99.py"


if __name__ == "__main__":
    scene = NUM10to99()
    scene.render()