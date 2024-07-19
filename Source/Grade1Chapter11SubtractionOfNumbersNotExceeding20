# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
import random  # Import the random module
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo


class Grade1Ch11SubtractionOfNumbersNotExceeding20(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.Sub()
        self.fadeOutCurrentScene()
        self.Anim()
        self.fadeOutCurrentScene()
        self.example1()
        self.fadeOutCurrentScene()
        self.example2()
        self.fadeOutCurrentScene()
        self.example3()
        self.fadeOutCurrentScene()
        self.example4()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
      
    def SetDeveloperList(self):
        # return super().SetDeveloperList()
        self.DeveloperList="Bharathi Priyadarshini"
        
    def SetSourceCodeFileName(self):
        # return super().SetSourceCodeFileName()
        self.SourceCodeFileName="Grade1Chapter11SubtractionOfNumbersNotExceeding20"
  
    def Sub(self):
        self.isRandom = False
        t1 = Text("Subtraction of Numbers not Exceeding 20",font_size=30)
        t1.move_to([0,0, 0])
        # Write the text and the underline
        self.play(Write(t1))
        self.wait(2)
        self.play(FadeOut(t1))
        self.wait(1)
        p10=cvo.CVO().CreateCVO("Subtraction ","")
        p12=cvo.CVO().CreateCVO("Definition", "difference between two numbers")
        p11=cvo.CVO().CreateCVO("Symbol", "-")  
        p10.cvolist.append(p12)
        p10.cvolist.append(p11)
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)  
        self.wait(1)
      
    def Anim(self):
        ex=Text("Example",font_size=25)
        ex.move_to([-5,3, 0])
        self.play(Write(ex))
        self.wait(1)

        problems = [
            (15, 5, 10),
            (18, 12, 6),
            (16, 14, 2)
        ]
        
        def create_chick(chick, row, col):
            chick_text = Text(chick, font_size=30,color=YELLOW)
            x_pos = -6 + col * 1  # Adjust horizontal spacing (1.2 is an example)
            y_pos = 1 - row * 1   # Adjust vertical spacing (1.5 is an example)
            chick_text.move_to(np.array([x_pos, y_pos, 0]))
            return chick_text
        
        chick_emoji = "🐤"

        for total, subtrahend, result in problems:
            problem_text = Text(f"{total} - {subtrahend} = {result}", font_size=40, color=BLUE)
            self.play(Write(problem_text))
            self.wait(1)
            self.play(problem_text.animate.shift(UP * 3.3))
            self.wait(1)
           
            
            # Create fruits for total
            total_chick = VGroup()
            for i in range(total):
                col = i % 5 # Adjust columns as needed
                row = i // 5 # Adjust rows as needed
                chick = create_chick(chick_emoji, row, col)
                total_chick.add(chick)
            
            total_label = Text(f"{total}", font_size=24)
            total_label.next_to(total_chick, DOWN)
            
            self.play(
                FadeIn(total_chick),
                Write(total_label)
            )
            self.wait(2)

            # Animate subtraction
            minus_text = Text("-", font_size=125, color=BLUE)
            minus_text.next_to(total_chick, RIGHT)
            self.play(Write(minus_text))
            self.wait(1)

            # Create fruits for subtrahend
            subtrahend_chick = VGroup()
            for i in range(subtrahend):
                col = i % 4 # Adjust columns as needed
                row = i // 4  # Adjust rows as needed
                chick = create_chick(chick_emoji, row, col)
                subtrahend_chick.add(chick)

            subtrahend_chick.next_to(minus_text, RIGHT)
            
            subtrahend_label = Text(f"{subtrahend}", font_size=24)
            subtrahend_label.next_to(subtrahend_chick, DOWN)
            
            self.play(
                FadeIn(subtrahend_chick),
                Write(subtrahend_label)
            )
            self.wait(2)

            # Animate equals sign
            equal_text = Text("=", font_size=125, color=BLUE)
            equal_text.next_to(subtrahend_chick, RIGHT)
            self.play(Write(equal_text))
            self.wait(1)

            # Create fruits for result
            result_chick = VGroup()
            for i in range(result):
                col = i % 3  # Adjust columns as needed
                row = i // 3  # Adjust rows as needed
                chick = create_chick(chick_emoji, row, col)
                result_chick.add(chick)

            result_chick.next_to(equal_text, RIGHT)
            
            result_label = Text(f"{result}", font_size=24)
            result_label.next_to(result_chick, DOWN)
            
            self.play(
                FadeIn(result_chick),
                Write(result_label)
            )
            self.wait(2)
            
            # Fade out all elements for the current problem
            self.play(
                FadeOut(problem_text),
                FadeOut(total_chick),
                FadeOut(subtrahend_chick),
                FadeOut(result_chick),
                FadeOut(total_label),
                FadeOut(subtrahend_label),
                FadeOut(result_label),
                FadeOut(minus_text),
                FadeOut(equal_text)
            )
        
        self.wait(2)
    
    def example1(self):
        ex=Text("Subtract the numbers given below:",font_size=25)
        ex.move_to([-4.5,3.3, 0])
        self.play(Write(ex))
        self.wait(1)

        problems = [
            (12, 2, 10),
            (17, 15, 2),
            (16, 3, 13)
        ]
        
        def create_chick(chick, row, col):
            chick_text = Text(chick, font_size=30,color=LIGHT_BROWN)
            x_pos = -6 + col * 1  # Adjust horizontal spacing (1.2 is an example)
            y_pos = 1 - row * 1   # Adjust vertical spacing (1.5 is an example)
            chick_text.move_to(np.array([x_pos, y_pos, 0]))
            return chick_text
        
        chick_emoji = "🧸"

        for total, subtrahend, result in problems:
            problem_text = Text(f"{total} - {subtrahend} = ", font_size=30, color=BLUE)
            self.play(Write(problem_text))
            self.wait(1)
            self.play(problem_text.animate.shift(UP * 2.7))
            self.wait(1)
            # Create a rectangle box for the result
            box = Rectangle(height=0.5, width=1, color=WHITE)
            box.move_to(problem_text.get_right() + RIGHT * 0.75)  # Adjust the position as needed
            
            # Create the result text
            result_text = Text(f"{result}", font_size=30, color=BLUE)
            result_text.move_to(box.get_center())

            # Draw the box and write the result in it
            self.play(Create(box))
            self.wait(1)
            # self.play(Write(result_text))
            # self.wait(1)

            # Create fruits for total
            total_chick = VGroup()
            for i in range(total):
                col = i % 5 # Adjust columns as needed
                row = i // 5 # Adjust rows as needed
                chick = create_chick(chick_emoji, row, col)
                total_chick.add(chick)
            
            total_label = Text(f"{total}", font_size=24)
            total_label.next_to(total_chick, DOWN)
            
            self.play(
                FadeIn(total_chick),
                Write(total_label)
            )
            self.wait(2)

            # Animate subtraction
            minus_text = Text("-", font_size=125, color=BLUE)
            minus_text.next_to(total_chick, RIGHT)
            self.play(Write(minus_text))
            self.wait(1)

            # Create fruits for subtrahend
            subtrahend_chick = VGroup()
            for i in range(subtrahend):
                col = i % 4 # Adjust columns as needed
                row = i // 4  # Adjust rows as needed
                chick = create_chick(chick_emoji, row, col)
                subtrahend_chick.add(chick)

            subtrahend_chick.next_to(minus_text, RIGHT)
            
            subtrahend_label = Text(f"{subtrahend}", font_size=24)
            subtrahend_label.next_to(subtrahend_chick, DOWN)
            
            self.play(
                FadeIn(subtrahend_chick),
                Write(subtrahend_label)
            )
            self.wait(2)

            # Animate equals sign
            equal_text = Text("=", font_size=125, color=BLUE)
            equal_text.next_to(subtrahend_chick, RIGHT)
            self.play(Write(equal_text))
            self.wait(1)

            # Create fruits for result
            result_chick = VGroup()
            for i in range(result):
                col = i % 3  # Adjust columns as needed
                row = i // 3  # Adjust rows as needed
                chick = create_chick(chick_emoji, row, col)
                result_chick.add(chick)

            result_chick.next_to(equal_text, RIGHT)
            
            result_label = Text(f"{result}", font_size=24)
            result_label.next_to(result_chick, DOWN)
            
            self.play(
                FadeIn(result_chick),
                Write(result_label)
            )
            self.wait(1)
            self.play(Write(result_text))
            self.wait(2)
            
            # Fade out all elements for the current problem
            self.play(
                FadeOut(problem_text),
                FadeOut(result_text),
                FadeOut(box),
                FadeOut(total_chick),
                FadeOut(subtrahend_chick),
                FadeOut(result_chick),
                FadeOut(total_label),
                FadeOut(subtrahend_label),
                FadeOut(result_label),
                FadeOut(minus_text),
                FadeOut(equal_text)
            )
        
        self.wait(2)
    
    def example2(self):
        # self.play(Write(NumberPlane()))
        title = Text("Subtract the numbers given below:", font_size=25)
        title.move_to([-3, 3, 0])
        self.play(Write(title))
        self.wait(1)
        # First problem
        num = Text("1 5", font_size=40)
        num.move_to([0, 1.3, 0])
        self.play(Write(num))
        self.wait(1.5)

        # Minus sign
        minus = Text("-", font_size=60)
        minus.move_to([-0.8, 0.1, 0])
        self.play(Write(minus))

        # Second number
        num0 = Text(" 4", font_size=40)
        num0.move_to([0.2, 0.2, 0])
        self.play(Write(num0))
        self.wait(1)

        # Calculation details
        calculation = Text("Calculation:", font_size=30)
        calculation.move_to([4,2,0])
        t1 = Text("5 - 4 = 1", font_size=30)
        t1.move_to([4,1.1,0])
        t2 = Text("1 - 0 = 1", font_size=30)
        t2.move_to([4,0,0])
        
        # Result positions
        result1_position = [0.2, -0.7, 0]
        result2_position = [-0.2, -0.7, 0]

        # Line above and below result
        line_above = Line(start=[-0.8, 0, 0], end=[0.7, 0, 0], color=WHITE).move_to([result1_position[0], result1_position[1] + 0.4, 0])
        line_below = Line(start=[-0.8, 0, 0], end=[0.7, 0, 0], color=WHITE).move_to([result1_position[0], result1_position[1] - 0.4, 0])

        # Draw lines
        self.play(Create(line_above))
        self.play(Create(line_below))
        
        # Results
        result1 = Text(" 1", font_size=40)
        result1.move_to(result1_position)
        result2 = Text(" 1", font_size=40)
        result2.move_to(result2_position)
        
        self.play(Write(calculation))
        self.wait(1)
        self.play(Write(t1))
        self.wait(2)
        self.play(Write(result1))
        self.wait(1)
        self.play(Write(t2))
        self.wait(2)
        self.play(Write(result2))
        self.wait(3)
        self.play(FadeOut(num), FadeOut(minus),FadeOut(num0), FadeOut(line_above),FadeOut(line_below),FadeOut(calculation),FadeOut(t1), FadeOut(t2),FadeOut(result1),FadeOut(result2))
       
        num1 = Text("1 8", font_size=40)
        num1.move_to([0, 1.3, 0])
        self.play(Write(num1))
        self.wait(1.5)

        # Minus sign
        minus1 = Text("-", font_size=60)
        minus1.move_to([-0.8, 0.1, 0])
        self.play(Write(minus1))

        # Second number
        num2 = Text("  3", font_size=40)
        num2.move_to([0.2, 0.2, 0])
        self.play(Write(num2))
        self.wait(1)
         
        calculation1 = Text("Calculation:", font_size=30)
        calculation1.move_to([4,2,0])
        t11 = Text("8 - 3 = 5", font_size=30)
        t11.move_to([4,1.1,0])
        t12 = Text("1 - 0 = 1", font_size=30)
        t12.move_to([4,0,0])
        # Position for result
        result3_position = [0.2, -0.7, 0]
        result4_position = [-0.2, -0.7, 0]
        line_above = Line(start=[-0.8, 0, 0], end=[0.7, 0, 0], color=WHITE).move_to([result3_position[0], result3_position[1] + 0.4, 0])
        line_below = Line(start=[-0.8, 0, 0], end=[0.7, 0, 0], color=WHITE).move_to([result3_position[0], result3_position[1] - 0.4, 0])

        self.play(Create(line_above))
        self.play(Create(line_below))
        
        # Results
        result3 = Text(" 5", font_size=40)
        result3.move_to(result3_position)
        result4 = Text(" 1", font_size=40)
        result4.move_to(result4_position)
        self.play(Write(calculation1))
        self.wait(1)
        self.play(Write(t11))
        self.wait(2)
        self.play(Write(result3))
        self.wait(1)
        self.play(Write(t12))
        self.wait(2)
        self.play(Write(result4))
        self.wait(3)

    def example3(self):
        # self.play(Write(NumberPlane()))
        t1=Text("Subtract each pairs of numbers in each row .One of the answer is different.Tick the different one",font_size=23)
        t1.move_to([0,3,0])
        self.play(Write(t1))
        self.wait(2)
        # List of subtraction problems
        problems = ["14 - 2", "19 - 6", "17 - 5", "13 - 1"]
        
        # Create VGroup to hold all the problem boxes
        problem_boxes = VGroup()
        
        # Create boxes with problems
        for problem in problems:
            box = Rectangle(width=2, height=1, color=BLUE)
            text = Text(problem, font_size=24)
            text.move_to(box.get_center())
            problem_box = VGroup(box, text)
            problem_boxes.add(problem_box)
        
        # Arrange the boxes horizontally with some space between them
        problem_boxes.arrange(RIGHT, buff=1)
        
        # Create a surrounding rectangle
        surrounding_box = Rectangle(
            width=problem_boxes.get_width() + 1, 
            height=problem_boxes.get_height() + 1, 
            color=PURPLE
        )
        
        # Position the surrounding rectangle around the problem boxes
        surrounding_box.move_to(problem_boxes.get_center())
        
        # Add the surrounding box and the problem boxes to the scene
        self.play(Create(surrounding_box))
        self.play(FadeIn(problem_boxes))
        self.wait(2)
        t2=Text("14-2 = 12",font_size=25)
        t3=Text("19-6 = 13",font_size=25)
        t4=Text("17-5 = 12",font_size=25)
        t5=Text("13-1 = 12",font_size=25)
        t2.move_to([-4.5,-1.5,0])
        t3.move_to([-1.5,-1.5,0])
        t4.move_to([1.5,-1.5,0])
        t5.move_to([4.5,-1.5,0])
        self.play(Write(t2))
        self.wait(2)
        self.play(Write(t3))
        self.wait(2)
        self.play(Write(t4))
        self.wait(2)
        self.play(Write(t5))
        self.wait(2)
        t6=Text(" so,19-6 has different answer ",font_size=26)
        t6.move_to([0,-2.3,0])
        self.play(Write(t6))
        
        tick = VGroup(
            Line(ORIGIN, [0.2, -0.2, 0], color=GREEN),
            Line([0.2, -0.2, 0], [0.5, 0.3, 0], color=GREEN)
        )
        tick.scale(2)  # Scale the tick mark to an appropriate size
        tick.next_to(problem_boxes[1], UP)  # Position the tick mark above the second problem
        
        # Add the tick mark to the scene
        self.play(FadeIn(tick))
        self.wait(2.1)
         
    def example4(self):
        t0 = Text("Write the correct number that comes after subtracting",font_size=25)
        t0.move_to([-3,3.3, 0])
        self.play(Write(t0))
        self.wait(1.5)
        t1 = Text(" 19 ",font_size=25)
        t1.move_to([-6,1, 0])
        # self.play(Write(NumberPlane()))  
        t2 = Text(" -1 ",font_size=25)
        t2.move_to([-4.5,1.2, 0])
        t3 = Text(" 18 ",font_size=25)
        t3.move_to([-3,1, 0])
        t4 = Text(" -2 ",font_size=25)
        t4.move_to([-1.5,1.2, 0])
        t5 = Text(" 16 ",font_size=25)
        t5.move_to([0,1, 0])
        t6 = Text(" -3 ",font_size=25)
        t6.move_to([1.5,1.2, 0])
        t7 = Text(" 13 ",font_size=25)
        t7.move_to([3,1, 0])
        t8 = Text(" -3 ",font_size=25)
        t8.move_to([4.5,1.2, 0])
        t9 = Text(" 10 ",font_size=25)
        t9.move_to([6,1, 0])
           
        cir1=Circle(radius=0.5,color=PINK).move_to([-6, 1, 0])
        cir2=Circle(radius=0.5,color=PINK).move_to([-3, 1, 0])
        cir3=Circle(radius=0.5,color=PINK).move_to([0, 1, 0])
        cir4=Circle(radius=0.5,color=PINK).move_to([3, 1, 0]) 
        cir5=Circle(radius=0.5,color=PINK).move_to([6, 1, 0])
        line1 = Line(start=[-5.5,1,0],end=[-3.5,1,0],color=WHITE)
        line2 = Line(start=[-2.5,1,0],end=[-0.5,1,0],color=WHITE)
        line3 = Line(start=[0.5,1,0],end=[2.5,1,0],color=WHITE)
        line4 = Line(start=[3.5,1,0],end=[5.5,1,0], color=WHITE)
        self.play(Write(cir1))
        self.play(Write(t1))
        self.play(Create(line1))
        self.play(Write(t2))
        self.play(Write(cir2))
        self.play(Write(t3))
        self.play(Create(line2))
        self.play(Write(t4))
        self.play(Write(cir3))
        self.play(Create(line3))
        self.play(Write(t6))
        self.play(Write(cir4))
        self.play(Create(line4))
        self.play(Write(t8))
        self.play(Write(cir5))
        self.wait(2)
        self.play(Write(t5))
        self.wait(2)
        self.play(Write(t7))
        self.wait(2)
        self.play(Write(t9))
        t31 = Text("19 - 1 we get 18",font_size=28)
        t31.move_to([-5,0, 0])
        self.play(Write(t31))
        self.wait(3)
        t32 = Text("18 - 2 we get 16",font_size=28)
        t32.move_to([-5,-0.5, 0])
        self.play(Write(t32))
        self.wait(3)
        t33 = Text("16 - 3 we get 13",font_size=28)
        t33.move_to([-5,-1, 0])
        self.play(Write(t33))
        self.wait(3)
        t34 = Text("13 - 3 we get 10",font_size=28)
        t34.move_to([-5,-1.5, 0])
        self.play(Write(t34))
        self.wait(3)
        self.play(FadeOut(cir1),FadeOut(cir2),FadeOut(cir3),FadeOut(cir4),FadeOut(cir5),FadeOut(line1),FadeOut(line2),FadeOut(line3),FadeOut(line4),FadeOut(t1),FadeOut(t2),FadeOut(t3),FadeOut(t4),FadeOut(t5),FadeOut(t6),FadeOut(t7),FadeOut(t8),FadeOut(t9),FadeOut(t31),FadeOut(t32),FadeOut(t33),FadeOut(t34))
 
        t11 = Text(" 20 ",font_size=25)
        t11.move_to([-6,1, 0])
        # self.play(Write(NumberPlane()))  
        t12 = Text(" -1 ",font_size=25)
        t12.move_to([-5.3,1.6, 0])
        t13 = Text(" 19 ",font_size=25)
        t13.move_to([-4,2, 0])
        t14 = Text(" -2 ",font_size=25)
        t14.move_to([-2.7,1.6, 0])
        t15 = Text(" 17 ",font_size=25)
        t15.move_to([-2,1, 0])
        t16 = Text(" -3 ",font_size=25)
        t16.move_to([-0.8,1.4, 0])
        t17 = Text(" 14 ",font_size=25)
        t17.move_to([0,2, 0])
        t18 = Text(" -3 ",font_size=25)
        t18.move_to([1.5,1.6, 0])
        t19 = Text(" 11 ",font_size=25)
        t19.move_to([2,1, 0])
        t20 = Text(" -2 ",font_size=25)
        t20.move_to([3.3,1.4, 0])
        t21 = Text(" 9 ",font_size=25)
        t21.move_to([4,2, 0])
        t22 = Text(" -6 ",font_size=25)
        t22.move_to([5.3,1.6, 0])
        t23 = Text(" 3 ",font_size=25)
        t23.move_to([6,1, 0])   
        cir11=Circle(radius=0.5,color=PINK).move_to([-6, 1, 0])
        cir12=Circle(radius=0.5,color=PINK).move_to([-4, 2, 0])
        cir13=Circle(radius=0.5,color=PINK).move_to([-2, 1, 0])
        cir14=Circle(radius=0.5,color=PINK).move_to([0, 2, 0]) 
        cir15=Circle(radius=0.5,color=PINK).move_to([2, 1, 0])
        cir16=Circle(radius=0.5,color=PINK).move_to([4, 2, 0])
        cir17=Circle(radius=0.5,color=PINK).move_to([6, 1, 0])
        line11 = Line(start=[-5.5,1,0],end=[-4.5,2,0],color=WHITE)
        line12 = Line(start=[-3.5,2,0],end=[-2.5,1,0],color=WHITE)
        line13 = Line(start=[-1.5,1,0],end=[-0.5,2,0],color=WHITE)
        line14 = Line(start=[0.5,2,0],end=[1.5,1,0], color=WHITE)
        line15 = Line(start=[2.5,1,0],end=[3.5,2,0], color=WHITE)
        line16 = Line(start=[4.5,2,0],end=[5.5,1,0], color=WHITE)

        self.play(Write(cir11))
        self.play(Write(t11))
        self.play(Create(line11))
        self.play(Write(t12))
        self.play(Write(cir12))
        self.play(Write(t13))
        self.play(Create(line12))
        self.play(Write(t14))
        self.play(Write(cir13))
        self.play(Create(line13))
        self.play(Write(t16))
        self.play(Write(cir14))
        self.play(Create(line14))
        self.play(Write(t18))
        self.play(Write(cir15))
        self.play(Create(line15))
        self.play(Write(t20))
        self.play(Write(cir16))
        self.play(Create(line16))
        self.play(Write(t22))
        self.play(Write(cir17))
        self.wait(2)
        self.play(Write(t15))
        self.wait(2)
        self.play(Write(t17))
        self.wait(2)
        self.play(Write(t19))
        self.wait(2)
        self.play(Write(t21))
        self.wait(2)
        self.play(Write(t23))

        t20 = Text("20 - 1 we get 19",font_size=28)
        t20.move_to([-5,0, 0])
        self.play(Write(t20))
        self.wait(3)
        t21 = Text("19 - 2 we get 17",font_size=28)
        t21.move_to([-5,-0.5, 0])
        self.play(Write(t21))
        self.wait(3)
        t22 = Text("17 - 3 we get 14",font_size=28)
        t22.move_to([-5,-1, 0])
        self.play(Write(t22))
        self.wait(3)
        t23 = Text("14 - 3 we get 11",font_size=28)
        t23.move_to([-5,-1.5, 0])
        self.play(Write(t23))
        self.wait(3)
        t24 = Text("11 - 2 we get 9",font_size=28)
        t24.move_to([-5,-2, 0])
        self.play(Write(t24))
        self.wait(3)
        t25 = Text("9 - 6 we get 3",font_size=28)
        t25.move_to([-5,-2.5, 0])
        self.play(Write(t25))
        self.wait(3)
    
if __name__ == "__main__":
    scene = Grade1Ch11SubtractionOfNumbersNotExceeding20()
    scene.render()