from manim import *
from AbstractAnim import AbstractAnim
import cvo

class Grade6Chapter2WholenumbersTopic1(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.topic1()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        

   
    def Introduction(self):
        self.setNumberOfCirclePositions(3)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO(" Whole Numbers"," collection of positive numbers and zero")
        p11=cvo.CVO().CreateCVO("Denoted by","W")
        p12=cvo.CVO().CreateCVO("Representation", "W={0,1,2,3....}")
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        self.construct1(p10,p10)
        #self.construct1(p13,p13)
        #self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()

    
    
    def topic1(self):
        # Create a number line
        number_line = NumberLine(
            x_range=[-10, 10, 1],
            length=12,
            include_numbers=True,
            label_direction=DOWN,
        )
        self.play(Create(number_line))
        self.wait()

        # Addition
        self.perform_addition(number_line, 2, 3)
        self.wait()

        # Subtraction
        self.perform_subtraction(number_line, 5, 2)
        self.wait()

        # Multiplication
        self.perform_multiplication(number_line, 2, 3)
        self.wait()

        # Division
        self.perform_division(number_line, 6, 2)
        self.wait()

    def arc_jump(self, dot, start, end, direction=1):
        arc = ArcBetweenPoints(start, end, angle=direction * TAU/4)
        return MoveAlongPath(dot, arc)

    def perform_addition(self, number_line, a, b):
        dot = Dot(number_line.number_to_point(a), color=RED)
        self.play(FadeIn(dot))
        
        for i in range(b):
            start = number_line.number_to_point(a + i)
            end = number_line.number_to_point(a + i + 1)
            self.play(self.arc_jump(dot, start, end), run_time=0.5)
        
        result = MathTex(f"{a} + {b} = {a+b}")
        result.next_to(number_line, UP)
        self.play(Write(result))
        self.wait()
        self.play(FadeOut(dot), FadeOut(result))

    def perform_subtraction(self, number_line, a, b):
        dot = Dot(number_line.number_to_point(a), color=BLUE)
        self.play(FadeIn(dot))
        
        for i in range(b):
            start = number_line.number_to_point(a - i)
            end = number_line.number_to_point(a - i - 1)
            self.play(self.arc_jump(dot, start, end, direction=-1), run_time=0.5)
        
        result = MathTex(f"{a} - {b} = {a-b}")
        result.next_to(number_line, UP)
        self.play(Write(result))
        self.wait()
        self.play(FadeOut(dot), FadeOut(result))

    def perform_multiplication(self, number_line, a, b):
        dot = Dot(number_line.number_to_point(0), color=GREEN)
        self.play(FadeIn(dot))
        
        for i in range(b):
            start = number_line.number_to_point(i * a)
            end = number_line.number_to_point((i + 1) * a)
            self.play(self.arc_jump(dot, start, end), run_time=0.5)
        
        result = MathTex(f"{a} \\times {b} = {a*b}")
        result.next_to(number_line, UP)
        self.play(Write(result))
        self.wait()
        self.play(FadeOut(dot), FadeOut(result))

    def perform_division(self, number_line, a, b):
        dot = Dot(number_line.number_to_point(a), color=YELLOW)
        self.play(FadeIn(dot))
        
        jump_size = a / b
        for i in range(b):
            start = number_line.number_to_point(a - i * jump_size)
            end = number_line.number_to_point(a - (i + 1) * jump_size)
            self.play(self.arc_jump(dot, start, end, direction=-1), run_time=0.5)
        
        result = MathTex(f"{a} \\div {b} = {a/b}")
        result.next_to(number_line, UP)
        self.play(Write(result))
        self.wait()
        self.play(FadeOut(dot), FadeOut(result))

    """def topic1(self):
        # Create a number line
        number_line = NumberLine(
            x_range=[-10, 10, 1],
            length=10,
            include_numbers=True,
            label_direction=DOWN,
        )
        self.play(Create(number_line))
        self.wait()

        # Addition
        self.perform_addition(number_line, 3, 2)
        self.wait()

        # Subtraction
        self.perform_subtraction(number_line, 5, 2)
        self.wait()

        # Multiplication
        self.perform_multiplication(number_line, 2, 3)
        self.wait()

        # Division
        self.perform_division(number_line, 6, 2)
        self.wait()

    def perform_addition(self, number_line, a, b):
        # Addition: a + b
        dot = Dot(number_line.number_to_point(0), color=RED)
        self.play(FadeIn(dot))
        
        # First jump (a)
        self.play(dot.animate.move_to(number_line.number_to_point(a)))
        
        # Second jump (b)
        self.play(dot.animate.move_to(number_line.number_to_point(a + b)))
        
        result = MathTex(f"{a} + {b} = {a+b}")
        result.next_to(number_line, UP)
        self.play(Write(result))
        self.wait()
        self.play(FadeOut(dot), FadeOut(result))

    def perform_subtraction(self, number_line, a, b):
        # Subtraction: a - b
        dot = Dot(number_line.number_to_point(0), color=BLUE)
        self.play(FadeIn(dot))
        
        # First jump (a)
        self.play(dot.animate.move_to(number_line.number_to_point(a)))
        
        # Second jump (-b)
        self.play(dot.animate.move_to(number_line.number_to_point(a - b)))
        
        result = MathTex(f"{a} - {b} = {a-b}")
        result.next_to(number_line, UP)
        self.play(Write(result))
        self.wait()
        self.play(FadeOut(dot), FadeOut(result))

    def perform_multiplication(self, number_line, a, b):
        # Multiplication: a * b
        dot = Dot(number_line.number_to_point(0), color=GREEN)
        self.play(FadeIn(dot))
        
        for _ in range(b):
            self.play(dot.animate.move_to(number_line.number_to_point(((_ + 1) * a))))
        
        result = MathTex(f"{a} \\times {b} = {a*b}")
        result.next_to(number_line, UP)
        self.play(Write(result))
        self.wait()
        self.play(FadeOut(dot), FadeOut(result))

    def perform_division(self, number_line, a, b):
        # Division: a / b
        dot = Dot(number_line.number_to_point(a), color=YELLOW)
        self.play(FadeIn(dot))
        
        jump_size = a / b
        for i in range(b):
            self.play(dot.animate.move_to(number_line.number_to_point(a - i * jump_size)))
        
        result = MathTex(f"{a} \\div {b} = {a/b}")
        result.next_to(number_line, UP)
        self.play(Write(result))
        self.wait()
        self.play(FadeOut(dot), FadeOut(result))"""
    

    def SetDeveloperList(self): 
       self.DeveloperList="Medha Masanam" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade6Chapter2WholenumbersTopic1.py"

if __name__ == "__main__":
    scene = Grade6Chapter2WholenumbersTopic1()
    scene.render()