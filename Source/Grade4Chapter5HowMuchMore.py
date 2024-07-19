import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class Grade4Ch5(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.Numline()
        self.fadeOutCurrentScene()
        self.Numline2()
        self.fadeOutCurrentScene()
        self.Numline3()
        self.fadeOutCurrentScene()
        self.Numline4()
        self.fadeOutCurrentScene()
        self.Numline5()
        self.fadeOutCurrentScene()
        self.Numline6()
        self.fadeOutCurrentScene()
        self.Add()  
        self.fadeOutCurrentScene()
        self.Sub()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
       
    

    def Numline(self):
        text1=Text("Addition Using Number Line", color=RED)
        text1.center()
        text1.shift(UP * 3)
        self.play(Write(text1))
        text=Text("Question :  12 + 28", color= GREEN).scale(0.7)
        text.center()
        text.shift(UP * 2, LEFT * 4.5)
        self.play(Write(text))
        text2=Text("Expansion : 12 + 10 + 10 +8", color= PURPLE).scale(0.7)
        text2.center()
        text2.shift(UP * 1.2,LEFT * 3)
        self.play(Write(text2))
        text3=Text("Answer : 40", color= PURPLE).scale(0.7)
        text3.center()
        text3.shift(LEFT * 4.5, UP * 0.6)
        self.play(Write(text3))

        number_line = NumberLine(
            x_range=[0, 50, 5],
            length=10,
            color=BLUE,
            include_numbers=True,
            label_direction=DOWN,
            decimal_number_config={"num_decimal_places": 0}
        )
        number_line.center()
        number_line.shift(DOWN * 2)
        self.play(Create(number_line))

        start_point = 12
        dot_start = Dot(point=number_line.n2p(start_point), color=RED)
        label_start = Tex("12").next_to(dot_start, DOWN * 2)
        self.play(Create(dot_start), Write(label_start))

        increments = [10, 10, 8]
        current_value = start_point

        for increment in increments:
            next_value = current_value + increment
            arrow = CurvedArrow(
                start_point=number_line.n2p(current_value),
                end_point=number_line.n2p(next_value),
                color=YELLOW,
                angle=-PI,
                tip_length=0.2
            )
            label = Tex(f"+{increment}").next_to(arrow, UP)
            self.play(Create(arrow), Write(label))
            current_value = next_value

        dot_end = Dot(point=number_line.n2p(current_value), color=GREEN)
        label_end = Tex(str(current_value)).next_to(dot_end, DOWN * 2)
        self.play(Create(dot_end), Write(label_end))
        self.wait(4)

    def Numline2(self):
        text1=Text("Addition Using Number Line", color=RED)
        text1.center()
        text1.shift(UP * 3)
        self.play(Write(text1))
        text=Text("Question : 25 + 23", color= GREEN).scale(0.7)
        text.center()
        text.shift(UP * 2, LEFT * 4.5)
        self.play(Write(text))
        text2=Text("Expansion : 25 + 10 + 10 + 3", color= PURPLE).scale(0.7)
        text2.center()
        text2.shift(UP * 1.2,LEFT * 3)
        self.play(Write(text2))
        text3=Text("Answer : 48", color= PURPLE).scale(0.7)
        text3.center()
        text3.shift(LEFT * 4.5, UP *0.6)
        self.play(Write(text3))
        number_line = NumberLine(
            x_range=[0, 50, 5],  
            length=10,           
            color=BLUE,
            include_numbers=True,  
            label_direction=DOWN,  
            decimal_number_config={"num_decimal_places": 0}  
        )

        number_line.center()
        number_line.shift(DOWN *2)
        self.play(Create(number_line))
        
        start_point = 25
        dot_start = Dot(point=number_line.n2p(start_point), color=RED)
        label_start = Tex("25").next_to(dot_start, DOWN *2)

        self.play(Create(dot_start), Write(label_start))

        increments = [10, 10, 3]
        current_value = start_point
        
       
        for increment in increments:
            next_value = current_value + increment
            arrow = CurvedArrow(
                start_point=number_line.n2p(current_value) , 
                end_point=number_line.n2p(next_value) , 
                color=YELLOW,
                angle= -PI,
                tip_length=0.2
            )
            label = Tex(f"+{increment}").next_to(arrow,UP)
            self.play(Create(arrow), Write(label))
            current_value = next_value

        dot_end = Dot(point=number_line.n2p(current_value), color=GREEN)
        label_end = Tex(str(current_value)).next_to(dot_end, DOWN * 2)
        self.play(Create(dot_end), Write(label_end))
        self.wait(2)

    def Numline3(self):
        text1=Text("Addition Using Number Line", color=RED)
        text1.center()
        text1.shift(UP * 3)
        self.play(Write(text1))
        text=Text("Question : 8 + 33", color= GREEN).scale(0.7)
        text.center()
        text.shift(UP * 2, LEFT * 4.5)
        self.play(Write(text))
        text2=Text("Expansion : 8 + 10 + 10 + 10 + 3", color= PURPLE).scale(0.7)
        text2.center()
        text2.shift(UP * 1.2,LEFT * 3)
        self.play(Write(text2))
        text3=Text("Answer : 41", color= PURPLE).scale(0.7)
        text3.center()
        text3.shift(LEFT * 4.5, UP *0.6)
        self.play(Write(text3))
        number_line = NumberLine(
            x_range=[0, 50, 5],  
            length=10,           
            color=BLUE,
            include_numbers=True,  
            label_direction=DOWN,  
            decimal_number_config={"num_decimal_places": 0}  
        )

        number_line.center()
        number_line.shift(DOWN *2)
        self.play(Create(number_line))
        
        start_point = 8
        dot_start = Dot(point=number_line.n2p(start_point), color=RED)
        label_start = Tex("8").next_to(dot_start, DOWN *2)

        self.play(Create(dot_start), Write(label_start))

        increments = [10, 10,10 , 3]
        current_value = start_point
        
        for increment in increments:
            next_value = current_value + increment
            arrow = CurvedArrow(
                start_point=number_line.n2p(current_value) , 
                end_point=number_line.n2p(next_value) , 
                color=YELLOW,
                angle= -PI,
                tip_length=0.2
            )
            label = Tex(f"+{increment}").next_to(arrow,UP)
            self.play(Create(arrow), Write(label))
            current_value = next_value

        dot_end = Dot(point=number_line.n2p(current_value), color=GREEN)
        label_end = Tex(str(current_value)).next_to(dot_end, DOWN * 2)
        self.play(Create(dot_end), Write(label_end))
        self.wait(2)
        
    def Numline4(self):
        text1=Text("Subtraction Using Number Line", color=RED)
        text1.center()
        text1.shift(UP * 3)
        self.play(Write(text1))
        text=Text("Question : 45 - 33", color= GREEN).scale(0.7)
        text.center()
        text.shift(UP * 2, LEFT * 4.5)
        self.play(Write(text))
        text2=Text("Expansion : 45 - 10 - 10 - 10 - 3", color= PURPLE).scale(0.7)
        text2.center()
        text2.shift(UP * 1.2,LEFT * 3)
        self.play(Write(text2))
        text3=Text("Answer : 12", color= PURPLE).scale(0.7)
        text3.center()
        text3.shift(LEFT * 4.5, UP *0.6)
        self.play(Write(text3))
        number_line = NumberLine(
            x_range=[0, 50, 5],  
            length=10,           
            color=BLUE,
            include_numbers=True,  
            label_direction=DOWN,  
            decimal_number_config={"num_decimal_places": 0}  
        )

        number_line.center()
        number_line.shift(DOWN *2)
        self.play(Create(number_line))
        
        start_point = 45
        dot_start = Dot(point=number_line.n2p(start_point), color=RED)
        label_start = Tex("45").next_to(dot_start, DOWN *2)

        self.play(Create(dot_start), Write(label_start))

        decrements = [10, 10, 10 , 3]
        current_value = start_point
       
        for decrement in decrements:
            next_value = current_value - decrement
            arrow = CurvedArrow(
                start_point=number_line.n2p(current_value) , 
                end_point=number_line.n2p(next_value) , 
                color=YELLOW,
                angle= PI,
                tip_length=0.2
            )
            label = Tex(f"-{decrement}").next_to(arrow,UP)
            self.play(Create(arrow), Write(label))
            current_value = next_value

        dot_end = Dot(point=number_line.n2p(current_value), color=GREEN)
        label_end = Tex(str(current_value)).next_to(dot_end, DOWN * 2)
        self.play(Create(dot_end), Write(label_end))
        self.wait(2)

    def Numline5(self):
        text1=Text("Subtraction Using Number Line", color=RED)
        text1.center()
        text1.shift(UP * 3)
        self.play(Write(text1))
        text=Text("Question : 37 - 19", color= GREEN).scale(0.7)
        text.center()
        text.shift(UP * 2, LEFT * 4.5)
        self.play(Write(text))
        text2=Text("Expansion : 37 - 10 - 9", color= PURPLE).scale(0.7)
        text2.center()
        text2.shift(UP * 1.2,LEFT * 4)
        self.play(Write(text2))
        text3=Text("Answer : 18", color= PURPLE).scale(0.7)
        text3.center()
        text3.shift(LEFT * 4.5, UP *0.6)
        self.play(Write(text3))
        number_line = NumberLine(
            x_range=[0, 50, 5],  
            length=10,           
            color=BLUE,
            include_numbers=True,  
            label_direction=DOWN,  
            decimal_number_config={"num_decimal_places": 0}  
        )

        number_line.center()
        number_line.shift(DOWN *2)
        self.play(Create(number_line))
        
        start_point = 37
        dot_start = Dot(point=number_line.n2p(start_point), color=RED)
        label_start = Tex("37").next_to(dot_start, DOWN *2)

        self.play(Create(dot_start), Write(label_start))

        decrements = [10, 9]
        current_value = start_point
       
        for decrement in decrements:
            next_value = current_value - decrement
            arrow = CurvedArrow(
                start_point=number_line.n2p(current_value) , 
                end_point=number_line.n2p(next_value) , 
                color=YELLOW,
                angle= PI,
                tip_length=0.2
            )
            label = Tex(f"-{decrement}").next_to(arrow,UP)
            self.play(Create(arrow), Write(label))
            current_value = next_value

        dot_end = Dot(point=number_line.n2p(current_value), color=GREEN)
        label_end = Tex(str(current_value)).next_to(dot_end, DOWN * 2)
        self.play(Create(dot_end), Write(label_end))
        self.wait(2)

    def Numline6(self):
        text1=Text("Subtraction Using Number Line", color=RED)
        text1.center()
        text1.shift(UP * 3)
        self.play(Write(text1))
        text=Text("Question : 43 - 39", color= GREEN).scale(0.7)
        text.center()
        text.shift(UP * 2, LEFT * 4.5)
        self.play(Write(text))
        text2=Text("Expansion : 43 - 10 - 10 - 10 - 9", color= PURPLE).scale(0.7)
        text2.center()
        text2.shift(UP * 1.2,LEFT * 3)
        self.play(Write(text2))
        text3=Text("Answer : 4", color= PURPLE).scale(0.7)
        text3.center()
        text3.shift(LEFT * 4.5, UP *0.6)
        self.play(Write(text3))
        number_line = NumberLine(
            x_range=[0, 50, 5],  
            length=10,           
            color=BLUE,
            include_numbers=True,  
            label_direction=DOWN,  
            decimal_number_config={"num_decimal_places": 0}  
        )

        number_line.center()
        number_line.shift(DOWN *2)
        self.play(Create(number_line))
        
        start_point = 43
        dot_start = Dot(point=number_line.n2p(start_point), color=RED)
        label_start = Tex("43").next_to(dot_start, DOWN *2)

        self.play(Create(dot_start), Write(label_start))

        decrements = [10, 10, 10 , 9]
        current_value = start_point
       
        for decrement in decrements:
            next_value = current_value - decrement
            arrow = CurvedArrow(
                start_point=number_line.n2p(current_value) , 
                end_point=number_line.n2p(next_value) , 
                color=YELLOW,
                angle= PI,
                tip_length=0.2
            )
            label = Tex(f"-{decrement}").next_to(arrow,UP)
            self.play(Create(arrow), Write(label))
            current_value = next_value

        dot_end = Dot(point=number_line.n2p(current_value), color=GREEN)
        label_end = Tex(str(current_value)).next_to(dot_end, DOWN * 2)
        self.play(Create(dot_end), Write(label_end))
        self.wait(2)
     
    def Add(self):
        text1=Text("Addition With Bigger Numbers", color=RED)
        text1.center()
        text1.shift(UP * 3)
        self.play(Write(text1))
        text=Text("Question : 156 + 127", color= GREEN).scale(0.7)
        text.center()
        text.shift(UP * 2, LEFT * 3)
        self.play(Write(text))
        text7=Text("156").scale(0.7)
        text7.center()
        text7.shift(UP ,LEFT * 3)
        self.play(Write(text7))
        text2=Text("156 = 100 + 50 + 6", color= PURPLE).scale(0.7)
        text2.center()
        text2.shift(UP * 1.2,RIGHT )
        self.play(Write(text2))
        text8=Text("+  127").scale(0.7)
        text8.center()
        text8.shift(LEFT * 3.2)
        self.play(Write(text8))
        text3=Text("+  127 = 100 + 20 + 7", color= PURPLE).scale(0.7)
        text3.center()
        text3.shift(RIGHT , UP *0.5)
        self.play(Write(text3))
        line = Line(start=LEFT * 4 , end=LEFT * 2)
        self.add(line)
        line.shift(DOWN * 0.4)
        line2 = Line(start=LEFT * 2 , end=RIGHT * 3)
        line2.shift(RIGHT)
        self.add(line2)
        text9=Text("283").scale(0.7)
        text9.center()
        text9.shift(LEFT* 3, DOWN)
        text4=Text("   = 200 + 70 + 13", color= PURPLE).scale(0.7)
        text4.center()
        text4.shift(RIGHT * 1.3, DOWN * 0.4)
        self.play(Write(text4))
        text5=Text("   = 200 + 70 + 10 + 3", color= PURPLE).scale(0.7)
        text5.center()
        text5.shift(DOWN * 1.1 ,RIGHT * 1.8)
        self.play(Write(text5))
        text6=Text("   = 200 + 80 + 3", color= PURPLE).scale(0.7)
        text6.center()
        text6.shift(DOWN * 1.7,RIGHT * 1.3)
        self.play(Write(text6))
        texta=Text("= 283",color = PURPLE).scale(0.7)
        texta.center()
        texta.shift( RIGHT * 0.5, DOWN * 2.4) 
        self.play(Write(texta))
        self.play(Write(text9))
        self.wait(5)

    def Sub(self):
        text1=Text("Subtraction With Bigger Numbers", color=RED)
        text1.center()
        text1.shift(UP * 3)
        self.play(Write(text1))
        text=Text("Q. - 279 - 146", color= GREEN).scale(0.7)
        text.center()
        text.shift(UP * 2, LEFT * 3)
        self.play(Write(text))
        text7=Text("279").scale(0.7)
        text7.center()
        text7.shift(UP ,LEFT * 3)
        self.play(Write(text7))
        text2=Text("279 = 200 + 70 + 9", color= PURPLE).scale(0.7)
        text2.center()
        text2.shift(UP ,RIGHT *1.4 )
        self.play(Write(text2))
        text8=Text("-     146").scale(0.7)
        text8.center()
        text8.shift(LEFT * 3.5)
        self.play(Write(text8))
        text3=Text("-  146 = 100 + 40 + 6", color= PURPLE).scale(0.7)
        text3.center()
        text3.shift(RIGHT * 1.4)
        self.play(Write(text3))
        line = Line(start=LEFT * 4 , end=LEFT * 2)
        self.add(line)
        line.shift(DOWN * 0.4)
        text9=Text("133").scale(0.7)
        text9.center()
        text9.shift(LEFT* 3, DOWN )
        
        line2 = Line(start=LEFT * 1.5 , end=RIGHT *3.5)
        self.add(line2)
        line2.shift(DOWN * 0.5, RIGHT *0.5)
        text4=Text("    = 100 + 30 + 3", color= PURPLE).scale(0.7)
        text4.center()
        text4.shift(RIGHT *1.4, DOWN * 1.1)
        self.play(Write(text4))
        text5=Text("    = 133", color= PURPLE).scale(0.7)
        text5.center()
        text5.shift(RIGHT * 0.5, DOWN * 1.7)

        self.play(Write(text5))
        self.play(Write(text9))
        self.wait(4)

    def SetDeveloperList(self): 
       self.DeveloperList="Khanak Gupta" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade4Chapter5HowMuchMore.py"

if __name__ == "__main__":
    scene = Grade4Ch5()
    scene.render()