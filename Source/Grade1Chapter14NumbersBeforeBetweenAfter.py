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
        self.setNumberOfCirclePositions(4)
        self.isRandom=False
        self.angleChoice = [TAU/4,-TAU/4,-TAU/4]
        # Display the main title
        self.show_title("Let's Learn About Numbers!")
        p10=cvo.CVO().CreateCVO("Let us assume two numbers","5,7").setPosition([0,2.5,0])
        #.setPosition([0,2.5,0]).setPosition([5,-2,0]).setPosition([-4,2,0]).setPosition([-4,-2,0])
        p12=cvo.CVO().CreateCVO("Number Before 5","4").setPosition([5,-2,0])
        p13=cvo.CVO().CreateCVO("Number After 5","6").setPosition([-4,2,0])
        p14=cvo.CVO().CreateCVO("Number Between 5 and 7","6").setPosition([-4,-2,0])
       # p11.cvolist.append(p12)
         
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
         
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

        # Set up the two numbers we'll be working with
        

    def topic1(self):
        num1, num2 = 5, 7

        #self.show_title("Number Comparison")
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
        title = Text("Number Comparison", font_size=40).set_color(YELLOW).to_edge(UP)
        
        pred_text = Text(f"The number before {num} is ___", font_size=32).next_to(title, DOWN)
        
        self.play(Write(title))
        self.wait(1)
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
        
        # Create the text to appear above the blank
        fill_pred = Text(str(num-1), font_size=32, color=YELLOW).next_to(pred_text[-3:], UP, buff=0.1)
        
        self.play(
            FadeIn(pred_dot),
            Write(pred_label),
            Write(fill_pred)
        )
        self.wait(2)
        self.play(FadeOut(pred_dot), FadeOut(pred_label))

        succ_text = Text(f"The number after {num} is ___", font_size=32).next_to(title, DOWN)
        self.play(Transform(pred_text, succ_text), FadeOut(fill_pred))
        self.wait(1)

        succ_dot = Dot(number_line.number_to_point(num + 1), color=YELLOW)
        succ_label = Text(f"{num+1}", color=YELLOW, font_size=24).next_to(succ_dot, UP)
        
        # Create the text to appear above the blank
        fill_succ = Text(str(num+1), font_size=32, color=YELLOW).next_to(succ_text[-3:], UP, buff=0.1)
        
        self.play(
            FadeIn(succ_dot),
            Write(succ_label),
            Write(fill_succ)
        )
        self.wait(1)

        self.play(
            FadeOut(pred_text),
            FadeOut(succ_dot),
            FadeOut(succ_label),
            FadeOut(number_line),
            FadeOut(dot1),
            FadeOut(num1_label),
            FadeOut(title),
            FadeOut(fill_succ))
   
    def show_middle_number(self, num1, num2):
        middle = int((num1 + num2) / 2)
        title = Text("Number Comparison", font_size=40).set_color(YELLOW).to_edge(UP)

        
        middle_text = Text(f"The middle number between {num1} and {num2} is ___", font_size=32).next_to(title, DOWN)
        self.play(Write(title))
        self.wait(1)
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
        fill_middle = Text(str(middle), font_size=32, color=YELLOW).next_to(middle_text[-3:], UP, buff=0.1)

        self.play(FadeIn(middle_dot), Write(middle_label),Write(fill_middle))
        self.wait(1)

        self.play(FadeOut(middle_text), FadeOut(middle_dot), FadeOut(middle_label), FadeOut(number_line),FadeOut(dot1), FadeOut(num1_label),FadeOut(dot2), FadeOut(num2_label),FadeOut(title),FadeOut(fill_middle))

    def show_smallest_biggest(self, num1, num2):
        smallest = min(num1, num2)
        biggest = max(num1, num2)
        title = Text("Number Comparison", font_size=40).set_color(YELLOW).to_edge(UP)
        smallest_text = Text(f"The smallest number among {num1} and {num2} is ___", font_size=32).next_to(title, DOWN)
        self.play(Write(title))
        self.wait(1)
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
        
        
        
        fill_small = Text(str(smallest), font_size=32, color=RED).next_to(smallest_text[-3:], UP, buff=0.1)

        # Create a box around the smallest number on the number line
        smallest_box = SurroundingRectangle(num1_label, buff=0.1, color=YELLOW)
        
        self.play(
            FadeIn(dot1),
            Write(num1_label),
            Write(fill_small),
            Create(smallest_box)
        )
        self.wait(1)
        self.play(FadeOut(dot1), FadeOut(num1_label), FadeOut(dot2), FadeOut(num2_label), FadeOut(smallest_box))
        
        biggest_text = Text(f"The biggest number among {num1} and {num2} is ___", font_size=32).next_to(title, DOWN)
        self.play(Transform(smallest_text, biggest_text), FadeOut(fill_small))
        self.wait(1)
        
        dot1 = Dot(number_line.number_to_point(num1), color=RED)
        dot2 = Dot(number_line.number_to_point(num2), color=BLUE)
        num1_label = Text(str(num1), color=RED).next_to(dot1, UP)
        num2_label = Text(str(num2), color=BLUE).next_to(dot2, UP)

        self.play(
            FadeIn(dot1), Write(num1_label),
            FadeIn(dot2), Write(num2_label)
        )

        self.wait(3)
       
        
        
        fill_big = Text(str(biggest), font_size=32, color=BLUE).next_to(biggest_text[-3:], UP, buff=0.1)

        # Create a box around the biggest number on the number line
        biggest_box = SurroundingRectangle(num2_label, buff=0.1, color=YELLOW)

        self.play(
            FadeIn(dot2),
            Write(num2_label),
            Write(fill_big),
            Create(biggest_box)
        )
        self.wait(1)
        self.play(FadeOut(dot1), FadeOut(num1_label), FadeOut(dot2), FadeOut(num2_label),FadeOut(smallest_text),
            
            FadeOut(number_line),
            FadeOut(title),
            FadeOut(fill_big),
            FadeOut(biggest_box)
        )
    
    def show_order(self, num1, num2):
        ordered = sorted([num1, num2])
        title = Text("Number Comparison", font_size=40).set_color(YELLOW).to_edge(UP)

        order_text = Text(f"From smallest to biggest: {ordered[0]}, {ordered[1]}", font_size=32).next_to(title, DOWN)
        self.play(Write(title))
        self.wait(1)
        self.play(Write(order_text))
        self.wait(1)

        number_line = self.create_number_line()
        self.play(Create(number_line))

        # Create "smallest" and "biggest" labels
        smallest_label = Text("smallest", font_size=24).next_to(number_line.number_to_point(0), DOWN*3)
        biggest_label = Text("biggest", font_size=24).next_to(number_line.number_to_point(10), DOWN*3)

        # Create arrow
        arrow = Arrow(
            start=smallest_label.get_right(),
            end=biggest_label.get_left(),
            buff=0.4,
            color=YELLOW
        ).next_to(number_line, DOWN)

        # Add labels and arrow
        self.play(
            Write(smallest_label),
            Write(biggest_label),
            GrowArrow(arrow)
        )
        self.wait(1)

        dot1 = Dot(number_line.number_to_point(num1), color=RED)
        dot2 = Dot(number_line.number_to_point(num2), color=BLUE)
        num1_label = Text(str(num1), color=RED).next_to(dot1, UP)
        num2_label = Text(str(num2), color=BLUE).next_to(dot2, UP)

        self.play(
            FadeIn(dot1), Write(num1_label),
            FadeIn(dot2), Write(num2_label)
        )
        self.wait(3)
        self.play(
            FadeOut(dot1), FadeOut(num1_label),
            FadeOut(dot2), FadeOut(num2_label),
            FadeOut(number_line),
            FadeOut(smallest_label),
            FadeOut(biggest_label),
            FadeOut(arrow),
            FadeOut(order_text),FadeOut(title)
        )
        
    def SetDeveloperList(self):
        self.DeveloperList = "Medha Masanam"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName = "Grade1Chapter14NumbersBeforeBetweenAfter.py"

if __name__ == "__main__":
    scene = Grade1Chapter14NumbersBeforeBetweenAfter()
    scene.render()