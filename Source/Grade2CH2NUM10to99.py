from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class NUM10to99(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.TenAnd99()
        self.create_number_representation()
        self.AscAndDescOrder()
        self.OneTo99()
        self.GithubSourceCodeReference()
        
    def TenAnd99(self):
        text = Text("Number 10", font_size=60,color=LOGO_BLUE)
        self.play(Write(text))
        self.play(text.animate.shift(UP * 3))

        text = Text("10 is the smallest two digit number")
        self.play(Write(text))
        self.fadeOutCurrentScene()

        text = Text("Number 99", font_size=60,color=LOGO_BLUE)
        self.play(Write(text))
        self.play(text.animate.shift(UP * 3))

        text = Text("99 is the largest two digit number")
        self.play(Write(text))
        self.fadeOutCurrentScene()

    def create_number_representation(self):
        number_line = NumberLine(
            x_range=[0, 100, 10],
            length=10,
            color=BLUE,
            include_numbers=True,
            label_direction=UP
        )
        self.play(Create(number_line))
        self.wait(1)

        tens_label = Text("Tens", color=GREEN).to_edge(UP + LEFT)
        units_label = Text("Units", color=YELLOW).to_edge(UP + RIGHT)
        self.play(Write(tens_label), Write(units_label))
        self.wait(1)

        def show_number(num, position):
            tens_digit = num // 10
            units_digit = num % 10
            number_group = VGroup(
                Text(str(tens_digit), color=GREEN).scale(2),
                Text(str(units_digit), color=YELLOW).scale(2)
            ).arrange(RIGHT).move_to(position)
            self.play(Write(number_group))
            self.wait(0.5)
            self.play(FadeOut(number_group))

        def mark_number_on_line(num):
            dot = Dot(number_line.n2p(num), color=RED)
            number_text = Text(str(num), color=RED).next_to(dot, DOWN)
            self.play(Create(dot), Write(number_text))
            self.wait(0.5)
            self.play(FadeOut(dot), FadeOut(number_text))

        key_numbers = [10, 23, 45, 67, 89]
        for i, number in enumerate(key_numbers):
            position = DOWN + i * 0.5 * DOWN 
            mark_number_on_line(number)
            show_number(number, position)

        self.wait(1)
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
        ascending_numbers = [12, 25, 37, 49, 56, 68, 79, 85, 92]
        asc_group = VGroup()
        for i, num in enumerate(ascending_numbers):
            num_text = Text(str(num), font_size=36)
            asc_group.add(num_text)
        asc_group.arrange(RIGHT, buff=0.5)

        self.play(FadeIn(asc_group))

        for i, num_text in enumerate(asc_group):
            if i > 0:
                self.play(
                    num_text.animate.shift(UP * 0.5),
                    asc_group[i - 1].animate.shift(DOWN * 0.5)
                )
                self.wait(0.5)

        self.play(FadeOut(asc_group), FadeOut(asc_text))
        self.fadeOutCurrentScene()

        desc_text = Text("Descending Order", color=GREEN, font_size=50).to_edge(UP)
        self.play(Write(desc_text))
        text=Text("Arranging the  numbers from the biggest to the smallest is known as \n\n DESCENDING  ORDER",font_size=30).shift(UP *2)
        self.play(Write(text))
        descending_numbers = [92, 85, 79, 68, 56, 49, 37, 25, 12]
        desc_group = VGroup()
        for i, num in enumerate(descending_numbers):
            num_text = Text(str(num), font_size=36)
            desc_group.add(num_text)
        desc_group.arrange(RIGHT, buff=0.5)

        self.play(FadeIn(desc_group))

        for i, num_text in enumerate(desc_group):
            if i > 0:
                self.play(
                    num_text.animate.shift(UP * 0.5),
                    desc_group[i - 1].animate.shift(DOWN * 0.5)
                )
                self.wait(0.5)

        self.play(FadeOut(desc_group), FadeOut(desc_text))
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
        self.play(FadeIn(number_grid))
        

        self.wait(2)
        self.play(FadeOut(number_grid), FadeOut(title))   

        



    
    def SetDeveloperList(self):
        self.DeveloperList="Srujan"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade2CH2NumbersFrom10to99.py"


if __name__ == "__main__":
    scene = NUM10to99()
    scene.render()