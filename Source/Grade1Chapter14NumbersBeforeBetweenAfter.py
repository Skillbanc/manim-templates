from manim import *
from AbstractAnim import AbstractAnim
import cvo

class Grade1Chapter14NumbersBeforeBetweenAfter(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.topic1()
        self.fadeOutCurrentScene()
        
        self.GithubSourceCodeReference()
        

    def Introduction(self):
        # Display the main title
        self.show_title("Let's Learn About Numbers!")
        p10=cvo.CVO().CreateCVO("Let us assume two numbers","5,7").setPosition([0,2.5,0])
        #p11=cvo.CVO().CreateCVO("Example Number 2","7").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("Number Before 5","4").setPosition([5,-2,0])
        p13=cvo.CVO().CreateCVO("Number After 5","6").setPosition([-4,2,0]).setangle(-TAU/4)
        p14=cvo.CVO().CreateCVO("Number Between 5 and 7","6").setPosition([4,2,0])
       # p11.cvolist.append(p12)
         
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
         
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

        # Set up the two numbers we'll be working with
        

    def topic1(self):
        num1, num2 = 5, 7

        self.show_title("Number Comparison")
        self.show_predecessor_successor(num1)
        self.show_middle_number(num1, num2)
        self.show_smallest_biggest(num1, num2)
        self.show_order(num1, num2)

    def show_title(self, title_text):
        title = Text(title_text, font_size=40)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

    def create_number_line(self):
        return NumberLine(
            x_range=[0, 10, 1],
            length=10,
            include_numbers=True,
            label_direction=DOWN
        )

    def show_predecessor_successor(self, num):
        pred_text = Text(f"The number before {num} is {num-1}", font_size=32).to_edge(UP)
        self.play(Write(pred_text))
        self.wait(1)

        number_line = self.create_number_line()
        self.play(Create(number_line))

        dot1 = Dot(number_line.number_to_point(num), color=RED)
        num1_label = Text(str(num), color=RED).next_to(dot1, UP)
        self.play(FadeIn(dot1), Write(num1_label))
        self.wait(1)

        pred_dot = Dot(number_line.number_to_point(num - 1), color=YELLOW)
        pred_label = Text(f"{num-1}", color=YELLOW, font_size=24).next_to(pred_dot, UP)
        self.play(FadeIn(pred_dot), Write(pred_label))
        self.wait(1)

        succ_text = Text(f"The number after {num} is {num+1}", font_size=32).to_edge(UP)
        self.play(Transform(pred_text, succ_text))
        self.wait(1)

        succ_dot = Dot(number_line.number_to_point(num + 1), color=YELLOW)
        succ_label = Text(f"{num+1}", color=YELLOW, font_size=24).next_to(succ_dot, UP)
        self.play(FadeOut(pred_dot), FadeOut(pred_label))
        self.play(FadeIn(succ_dot), Write(succ_label))
        self.wait(1)

        self.play(FadeOut(pred_text), FadeOut(succ_dot), FadeOut(succ_label), FadeOut(number_line), FadeOut(dot1), FadeOut(num1_label))

    def show_middle_number(self, num1, num2):
        middle = int((num1 + num2) / 2)
        
        middle_text = Text(f"The middle number between {num1} and {num2} is {middle}", font_size=32).to_edge(UP)
        self.play(Write(middle_text))
        self.wait(1)

        number_line = self.create_number_line()
        self.play(Create(number_line))

        dot1 = Dot(number_line.number_to_point(num1), color=RED)
        dot2 = Dot(number_line.number_to_point(num2), color=BLUE)
        num1_label = Text(str(num1), color=RED).next_to(dot1, UP)
        num2_label = Text(str(num2), color=BLUE).next_to(dot2, UP)

        self.play(
            FadeIn(dot1), Write(num1_label),
            FadeIn(dot2), Write(num2_label)
        )
        self.wait(1)

        middle_dot = Dot(number_line.number_to_point(middle), color=GREEN)
        middle_label = Text(f"{middle}", color=GREEN, font_size=24).next_to(middle_dot, UP)
        self.play(FadeIn(middle_dot), Write(middle_label))
        self.wait(1)

        self.play(FadeOut(middle_text), FadeOut(middle_dot), FadeOut(middle_label), FadeOut(number_line),FadeOut(dot1), FadeOut(num1_label),FadeOut(dot2), FadeOut(num2_label))

    def show_smallest_biggest(self, num1, num2):
        smallest = min(num1, num2)
        biggest = max(num1, num2)

        smallest_text = Text(f"The smallest number among {num1} and {num2} is {smallest}", font_size=32).to_edge(UP)
        self.play(Write(smallest_text))
        self.wait(1)

        number_line = self.create_number_line()
        self.play(Create(number_line))
        dot1 = Dot(number_line.number_to_point(num1), color=RED)
        dot2 = Dot(number_line.number_to_point(num2), color=BLUE)
        num1_label = Text(str(num1), color=RED).next_to(dot1, UP)
        num2_label = Text(str(num2), color=BLUE).next_to(dot2, UP)

        self.play(
            FadeIn(dot1), Write(num1_label),
            FadeIn(dot2), Write(num2_label)
        )
        self.wait(3)
        self.play(FadeOut(dot1), FadeOut(num1_label),FadeOut(dot2), FadeOut(num2_label))
        
        smallest_dot = Dot(number_line.number_to_point(smallest), color=RED)
        smallest_label = Text(f"{smallest}", color=RED, font_size=24).next_to(smallest_dot, UP)
        self.play(FadeIn(smallest_dot), Write(smallest_label))
        self.wait(1)
        self.play(FadeOut(smallest_dot), FadeOut(smallest_label))
        
        biggest_text = Text(f"The biggest number among {num1} and {num2} is {biggest}", font_size=32).to_edge(UP)
        self.play(Transform(smallest_text, biggest_text))
        self.wait(1)

        biggest_dot = Dot(number_line.number_to_point(biggest), color=BLUE)
        biggest_label = Text(f"{biggest}", color=BLUE, font_size=24).next_to(biggest_dot, UP)
        self.play(FadeIn(biggest_dot), Write(biggest_label))
        self.wait(1)
        self.play(FadeOut(smallest_text),FadeOut(biggest_dot), FadeOut(biggest_label), FadeOut(number_line))

    def show_order(self, num1, num2):
        ordered = sorted([num1, num2])

        order_text = Text(f"From smallest to biggest: {ordered[0]}, {ordered[1]}", font_size=32).to_edge(UP)
        self.play(Write(order_text))
        self.wait(1)

        number_line = self.create_number_line()
        self.play(Create(number_line))

        dot1 = Dot(number_line.number_to_point(num1), color=RED)
        dot2 = Dot(number_line.number_to_point(num2), color=BLUE)
        num1_label = Text(str(num1), color=RED).next_to(dot1, UP)
        num2_label = Text(str(num2), color=BLUE).next_to(dot2, UP)

        self.play(
            FadeIn(dot1), Write(num1_label),
            FadeIn(dot2), Write(num2_label)
        )
        self.wait(3)
        self.play(FadeOut(dot1), FadeOut(num1_label),FadeOut(dot2), FadeOut(num2_label))

        dots = [Dot(number_line.number_to_point(num), color=YELLOW) for num in ordered]
        labels = [Text(str(num), color=YELLOW, font_size=24).next_to(dot, UP) for num, dot in zip(ordered, dots)]

        self.play(*[FadeIn(dot) for dot in dots], *[Write(label) for label in labels])
        self.wait(1)

        self.play(FadeOut(order_text), *[FadeOut(dot) for dot in dots], 
                  *[FadeOut(label) for label in labels], FadeOut(number_line))
        
    def SetDeveloperList(self):
        self.DeveloperList = "Medha Masanam"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName = "Grade1Chapter14NumbersBeforeBetweenAfter.py"

if __name__ == "__main__":
    scene = Grade1Chapter14NumbersBeforeBetweenAfter()
    scene.render()