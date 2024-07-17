# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License

import json
from manim import *

from AbstractAnim import AbstractAnim

import cvo

class int6(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.intro1()
        self.fadeOutCurrentScene()
        self.RenderAboutMe()
        self.fadeOutCurrentScene()
        self.Addition()
        self.fadeOutCurrentScene()
        self.addexample()
        self.fadeOutCurrentScene()
        self.Subtraction()
        self.fadeOutCurrentScene()
        self.subexample()
        self.fadeOutCurrentScene()  
        self.Multiplication()
        self.fadeOutCurrentScene()
        self.mulexample()
        self.fadeOutCurrentScene()
        self.Division()
        self.fadeOutCurrentScene()
        self.divexample()
        self.fadeOutCurrentScene()
        self.numberlineintro()
        self.fadeOutCurrentScene()
        self.addnumline()
        self.fadeOutCurrentScene()
        self.addnegitivenumline()
        self.fadeOutCurrentScene()
        self.addnegposinumline()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        
        
    def RenderSkillbancLogo(self):
        
        self.orange = "#D76800"
        self.blue = "#3F64A7"
        self.green = "#96D24D"
        self.circles = VGroup(
            Circle(radius=1).rotate(PI/2).set_fill(self.orange, opacity=1).set_stroke(self.orange, opacity=1).shift(LEFT*3),
            Circle(radius=1).rotate(PI/2).set_fill(self.blue, opacity=1).set_stroke(self.blue, opacity=1),
            Circle(radius=1).rotate(PI/2).set_fill(self.green, opacity=1).set_stroke(self.green, opacity=1).shift(RIGHT*3)
        )
        circle1, circle2, circle3 = self.circles
        
        lines = VGroup(
            Arrow(circle1.get_right(), circle2.get_left(), max_tip_length_to_length_ratio=2),
            Arrow(circle2.get_right(), circle3.get_left(), max_tip_length_to_length_ratio=2),
            CurvedArrow(circle1.get_top(), circle3.get_top(), angle=-TAU/4),
            CurvedArrow(circle1.get_bottom(), circle3.get_bottom(), angle=TAU/4)
        )

        # Adjust the starting points of the straight arrows to touch the circumference
        lines[0].put_start_and_end_on(circle1.get_right(), circle2.get_left())
        lines[1].put_start_and_end_on(circle2.get_right(), circle3.get_left())

        # Add the text "skillbanc" below the curved arrows
        self.play(Create(circle1), Create(circle2), Create(circle3), rate_func=smooth, run_time=1)
        self.play(Create(lines), rate_func=smooth, run_time=1)
        text = Text("Skillbanc.com, Inc.").next_to(lines[3], DOWN)
        self.play(Create(text), rate_func=smooth, run_time=0.75)
        
        self.logoGroup = VGroup().add(self.circles).add(lines).add(text)
        self.play(self.logoGroup.animate.scale(0),run_time=1)
        # self.play(self.circles.animate.scale(0),lines.animate.scale(0),text.animate.scale(0),run_time=3)
        
    def intro1(self):

        # Title
        title = Text("Understanding Integers",color=RED ,font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Definition of rational numbers
        definition = Text("Integers are whole numbers that can be positive, negative, or zero",color=RED_A, font_size=24)
        # fraction = MathTex(r"",color=BLUE, font_size=48)
        # condition = Text("where p and q are integers and q ≠ 0.", font_size=24)

        self.play(Write(definition.next_to(title,DOWN)))
        # self.play(Write(fraction.next_to(definition, DOWN, buff=0.5)))
        # self.play(Write(condition.next_to(fraction, DOWN, buff=0.5)))
        self.wait(1)

        # self.play(FadeOut(definition)),
                #    FadeOut(condition))
        # self.play(fraction.animate.to_edge(UP*2.2))

        # Examples of rational numbers
        # examples_title = Text("Integers",color=ORANGE ,font_size=36)
        # self.play(Write(examples_title.next_to(fraction, DOWN, buff=1)))
        # self.wait(1)

        examples = [
            ("", MathTex(r"Positive= 1", font_size=48)),
            ("", MathTex(r"Negative= -1", font_size=48)),
            # ("", MathTex(r"Integer={2}/{1}", font_size=48)),
            ("", MathTex(r"zero= 0", font_size=48))
        ]

        positions = [
            LEFT * 3 + UP * 0,
            RIGHT * 3 + UP * 0,
            LEFT * 3 + DOWN * 1.5,
            RIGHT * 3 + DOWN * 1.5,
        ]

        for (label, example), position in zip(examples, positions):
            label_text = Text(label, font_size=24).next_to(position, UP)
            example.move_to(position)
            self.play(Write(label_text), FadeIn(example))
            self.wait(1)

        # Concluding visualization
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # conclusion = Text("Rational numbers can be positive, negative, integers, or zero", font_size=30,color=GOLD)
        # self.play(Write(conclusion))
        # self.wait(2)
    # render using CVO data object
    def RenderAboutMe(self):
        count = 0
        # starting object
        p10=cvo.CVO().CreateCVO("Integers","").setPosition([-3,0,0])
        count += 1

        p12=cvo.CVO().CreateCVO("Positive Numbers","1,4,6").setPosition([2,1,2])
        count += 1

        p10.cvolist.append(p12)

        p20=cvo.CVO().CreateCVO("Zero","0").setPosition([2,-1,2])
        count += 1
        p10.cvolist.append(p20)

        p21=cvo.CVO().CreateCVO("Negitive Number","-1,-4").setPosition([2,-3,2])
        count += 1
        count += 1
        p10.cvolist.append(p21)

        self.setNumberOfCirclePositions(count)
       
       
        self.construct1(p10,p10)
      
    def Addition(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Addition of Integers","X+Y")
        p11=cvo.CVO().CreateCVO("X variable","2")
        p12=cvo.CVO().CreateCVO("Y variable","3")
        p13=cvo.CVO().CreateCVO("Sum", "5")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()

    def addexample(self):

        title = Text("Addition",color=PURPLE).to_edge(UP)
        self.play(Write(title))

        examples = [
            r"X + Y \quad \text{example:}\quad 2+3 =5",
            r"(-X) + Y \quad \text{example:} \quad -2 + 3 = 1",
            r"(-X) +(-Y) \quad \text{example:} \quad -2 + -3 = -5",
            r"X + (-Y) \quad \text{example:}\quad 2 + (-3) = -1"
        ]
        example1 = MathTex(examples[0]).scale(0.8).next_to(title, DOWN, buff=1)
        example2 = MathTex(examples[1]).scale(0.8).next_to(example1, DOWN, aligned_edge=LEFT, buff=0.5)
        example3 = MathTex(examples[2]).scale(0.8).next_to(example2, DOWN, aligned_edge=LEFT, buff=0.5)
        example4 = MathTex(examples[3]).scale(0.8).next_to(example3, DOWN, aligned_edge=LEFT, buff=0.5)

        self.play(Write(example1,color=ORANGE))
        self.wait(1)
        self.play(Write(example2))
        self.wait(1)
        self.play(Write(example3))
        self.wait(1)
        self.play(Write(example4))
        self.wait(1)

        self.wait(3)


    def Subtraction(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Subtraction of Integers","X-Y")
        p11=cvo.CVO().CreateCVO("X variable","2")
        p12=cvo.CVO().CreateCVO("Y variable","3")
        p13=cvo.CVO().CreateCVO("Difference", "-1")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()

    def subexample(self):
    
        title = Text("Subtraction",color=PURPLE).to_edge(UP)
        self.play(Write(title))

        examples = [
        r"X - Y \quad \text{example:} \quad 2 - 3 = -1",
        r"(-X) - Y \quad \text{example:} \quad -2 - 3 = -5",
        r"(-X) - (-Y) \quad \text{example:} \quad -2 - (-3) = 1",
        r"X - (-Y) \quad \text{example:} \quad 2 - (-3) = 5"
         ]
        example1 = MathTex(examples[0]).scale(0.8).next_to(title, DOWN, buff=1)
        example2 = MathTex(examples[1]).scale(0.8).next_to(example1, DOWN, aligned_edge=LEFT, buff=0.5)
        example3 = MathTex(examples[2]).scale(0.8).next_to(example2, DOWN, aligned_edge=LEFT, buff=0.5)
        example4 = MathTex(examples[3]).scale(0.8).next_to(example3, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(Write(example1))
        self.wait(1)
        self.play(Write(example2))
        self.wait(1)
        self.play(Write(example3))
        self.wait(1)
        self.play(Write(example4))
        self.wait(1)
 
        self.wait(3)


    def Multiplication(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Multiplication of Integers","X*Y")
        p11=cvo.CVO().CreateCVO("X variable","2")
        p12=cvo.CVO().CreateCVO("Y variable","3")
        p13=cvo.CVO().CreateCVO("Product", "6")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()


    def mulexample(self):
        title = Text("Multiplication",color=PURPLE).to_edge(UP)
        self.play(Write(title))

        examples = [
            r"X \times Y \quad \text{example:} \quad 2 \times 3 = 6",
            r"(-X) \times Y \quad \text{example:} \quad -2 \times 3 = -6",
            r"(-X) \times (-Y) \quad \text{example:} \quad -2 \times -3 = 6",
            r"X \times (-Y) \quad \text{example:} \quad 2 \times (-3) = -6"
        ]
        example1 = MathTex(examples[0]).scale(0.8).next_to(title, DOWN, buff=1)
        example2 = MathTex(examples[1]).scale(0.8).next_to(example1, DOWN, aligned_edge=LEFT, buff=0.5)
        example3 = MathTex(examples[2]).scale(0.8).next_to(example2, DOWN, aligned_edge=LEFT, buff=0.5)
        example4 = MathTex(examples[3]).scale(0.8).next_to(example3, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(Write(example1))
        self.wait(1)
        self.play(Write(example2))
        self.wait(1)
        self.play(Write(example3))
        self.wait(1)
        self.play(Write(example4))
        self.wait(1)
 
        self.wait(3)

    

    def Division(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Division of Integers","X/Y")
        p11=cvo.CVO().CreateCVO("X variable","8")
        p12=cvo.CVO().CreateCVO("Y variable","2")
        p13=cvo.CVO().CreateCVO("Quotient", "4")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()


    def divexample(self):
        title = Text("Division",color=PURPLE).to_edge(UP)
        self.play(Write(title))

        examples = [
        r"X \div Y \quad \text{example:} \quad 6 \div 3 = 2",
        r"(-X) \div Y \quad \text{example:} \quad -6 \div 3 = -2",
        r"(-X) \div (-Y) \quad \text{example:} \quad -6 \div -3 = 2",
        r"X \div (-Y) \quad \text{example:} \quad 6 \div (-3) = -2"
        ]
        example1 = MathTex(examples[0]).scale(0.8).next_to(title, DOWN, buff=1)
        example2 = MathTex(examples[1]).scale(0.8).next_to(example1, DOWN, aligned_edge=LEFT, buff=0.5)
        example3 = MathTex(examples[2]).scale(0.8).next_to(example2, DOWN, aligned_edge=LEFT, buff=0.5)
        example4 = MathTex(examples[3]).scale(0.8).next_to(example3, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(Write(example1))
        self.wait(1)
        self.play(Write(example2))
        self.wait(1)
        self.play(Write(example3))
        self.wait(1)
        self.play(Write(example4))
        self.wait(1)
 
        self.wait(3)

    def RenderNaturalNumbers(self):
        number_line = NumberLine(x_range=[-5,5,1],include_numbers=1)
        pointer = Vector(DOWN)
        label = MathTex("x").add_updater(lambda m: m.next_to(pointer, UP))

        tracker = ValueTracker(1)
        pointer.add_updater(
            lambda m: m.next_to(
                        number_line.n2p(tracker.get_value()),
                        UP
                    )
        )
        self.add(number_line, pointer,label)
        for i in range(-5,6):
            self.play(tracker.animate.set_value(i))

    def addnumline(self,):
        number_line = NumberLine(
            x_range=[-7, 8, 1],  # from -7 to 7 with step size 1
            length=14,  # length of the number line
            color=WHITE,
            include_numbers=True,
            label_direction=DOWN,
            include_tip=True,
            tip_width=0.2,
            tip_height=0.2,
        )
        number_line.add_numbers()

        # Define the numbers to add
        a = 2
        b = 3

        # Initial positions for the numbers
        start_a = number_line.n2p(0)
        end_a = number_line.n2p(a)
        end_b = number_line.n2p(a + b)

        # Create dots and labels for the numbers
        dot_a = Dot(start_a, color=BLUE)
        dot_b = Dot(end_a, color=RED)
        dot_c = Dot(end_b, color=GREEN)
        label_a = MathTex("0").next_to(dot_a, DOWN)
        label_b = MathTex(f"{a}").next_to(dot_b, DOWN)
        label_c = MathTex(f"{a + b}").next_to(dot_c, DOWN)

        # Create arrows showing the addition
        arrow_a = Arrow(start=start_a, end=end_a, buff=0, color=YELLOW)
        arrow_b = Arrow(start=end_a, end=end_b, buff=0, color=RED)

        # Create texts for the numbers added
        add_text_a = MathTex(f"{a}").next_to(arrow_a, UP)
        add_text_b = MathTex(f"{b}").next_to(arrow_b, UP)

        # Explanation texts
        explanation_text = Text("Let us add 2 and 3 on a number line.", font_size=24).to_edge(UP)
        step_text_a = Text("Starting at 0, move 2 units to the right.", font_size=20).next_to(explanation_text, DOWN)
        step_text_b = Text("Then move 3 more units to the right.", font_size=20).next_to(step_text_a, DOWN)
        result_text = Text("We reach 5, so 2 + 3 = 5.", font_size=24).to_edge(DOWN)

        # Animate the number line, dots, arrows, and text
        self.play(Write(explanation_text))
        self.play(Create(number_line))
        self.play(Create(dot_a),)
        self.play(Write(step_text_a))
        self.play(Create(arrow_a), Create(dot_b),)
        self.wait(1)
        self.play(Write(step_text_b))
        self.play(Create(arrow_b), Create(dot_c),)
        self.wait(1)
        self.play(Write(result_text))

        # Hold the final frame
        self.wait(2)

    def addnegitivenumline(self):
                 # Create the number line
        number_line = NumberLine(
            x_range=[-7, 8, 1],  # from -7 to 7 with step size 1
            length=14,  # length of the number line
            color=WHITE,
            include_numbers=True,
            label_direction=DOWN,
            include_tip=True,
            tip_width=0.2,
            tip_height=0.2,
        )
        number_line.add_numbers()

        # Define the numbers to add
        a = -2
        b = -3

        # Initial positions for the numbers
        start_a = number_line.n2p(0)
        end_a = number_line.n2p(a)
        end_b = number_line.n2p(a + b)

        # Create dots and labels for the numbers
        dot_a = Dot(start_a, color=BLUE)
        dot_b = Dot(end_a, color=RED)
        dot_c = Dot(end_b, color=GREEN)
        label_a = MathTex("0").next_to(dot_a, DOWN)
        label_b = MathTex(f"{a}").next_to(dot_b, DOWN)
        label_c = MathTex(f"{a + b}").next_to(dot_c, DOWN)

        # Create arrows showing the addition
        arrow_a = Arrow(start=start_a, end=end_a, buff=0, color=YELLOW)
        arrow_b = Arrow(start=end_a, end=end_b, buff=0, color=RED)

        # Create texts for the numbers added
        add_text_a = MathTex(f"{a}").next_to(arrow_a, UP)
        add_text_b = MathTex(f"{b}").next_to(arrow_b, UP)

        # Explanation texts
        explanation_text = Text("Let us add -2 and -3 on a number line.", font_size=24).to_edge(UP)
        step_text_a = Text("Starting at 0, move -2 units to the left.", font_size=20).next_to(explanation_text, DOWN)
        step_text_b = Text("Then move -3 more units to the left.", font_size=20).next_to(step_text_a, DOWN)
        result_text = Text("We reach -5, so -2 +-3 = -5.", font_size=24).to_edge(DOWN)

        # Animate the number line, dots, arrows, and text
        self.play(Write(explanation_text))
        self.play(Create(number_line))
        self.play(Create(dot_a),)
        self.play(Write(step_text_a))
        self.play(Create(arrow_a), Create(dot_b),)
        self.wait(1)
        self.play(Write(step_text_b))
        self.play(Create(arrow_b), Create(dot_c),)
        self.wait(1)
        self.play(Write(result_text))

        # Hold the final frame
        self.wait(2)

    def addnegposinumline(self):
        number_line = NumberLine(
            x_range=[-7, 8, 1],  # from -7 to 7 with step size 1
            length=14,  # length of the number line
            color=WHITE,
            include_numbers=True,
            label_direction=DOWN,
            include_tip=True,
            tip_width=0.2,
            tip_height=0.2,
        )
        number_line.add_numbers()

        # Define the numbers to add
        a = 6
        b = -3

        # Initial positions for the numbers
        start_a = number_line.n2p(0)
        end_a = number_line.n2p(a)
        end_b = number_line.n2p(a + b)

        # Create dots and labels for the numbers
        dot_a = Dot(start_a, color=BLUE)
        dot_b = Dot(end_a, color=RED)
        dot_c = Dot(end_b, color=GREEN)
        label_a = MathTex("0").next_to(dot_a, DOWN)
        label_b = MathTex(f"{a}").next_to(dot_b, DOWN)
        label_c = MathTex(f"{a + b}").next_to(dot_c, DOWN)

        # Create arrows showing the addition
        arrow_a = Arrow(start=start_a, end=end_a, buff=0, color=YELLOW)
        arrow_b = Arrow(start=end_a, end=end_b, buff=0, color=RED)

        # Create texts for the numbers added
        add_text_a = MathTex(f"{a}").next_to(arrow_a, UP)
        add_text_b = MathTex(f"{b}").next_to(arrow_b, UP)

        # Explanation texts
        explanation_text = Text("Let us add 6 and -3 on a number line.", font_size=24).to_edge(UP)
        step_text_a = Text("Starting at 0, move 6 units to the right.", font_size=20).next_to(explanation_text, DOWN)
        step_text_b = Text("Then move -3 more units to the left.", font_size=20).next_to(step_text_a, DOWN)
        result_text = Text("We reach 3, so 6 -3 = 3.", font_size=24).to_edge(DOWN)

        # Animate the number line, dots, arrows, and text
        self.play(Write(explanation_text))
        self.play(Create(number_line))
        self.play(Create(dot_a),)
        self.play(Write(step_text_a))
        self.play(Create(arrow_a), Create(dot_b), )
        self.wait(1)
        self.play(Write(step_text_b))
        self.play(Create(arrow_b), Create(dot_c),)
        self.wait(1)
        self.play(Write(result_text))

        # Hold the final frame
        self.wait(2)

    def SetDeveloperList(self):
        self.DeveloperList="Sai Krishna Bikkumalla"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade6Ch6Integers.py"
  

    def numberlineintro(self):

        # Create the text
        text = Text("NUMBER LINE",color=RED).scale(2)
        
        # Display the text on the screen
        self.play(Write(text))
        
        # Hold the text on the screen for 2 seconds
        self.wait(1)
if __name__ == "__main__":
    scene = int6()
    scene.render()
    