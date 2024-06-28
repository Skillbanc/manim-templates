# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla
import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class Chap8G1_SubUptoNine(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.Anim()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        
    def SetDeveloperList(self):  
        self.DeveloperList="Prithiv Shiv M V"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade1Chapter8SubtractionUptoNine.py"

    def Introduction(self):
        self.isRandom=False
        self.setNumberOfCirclePositions(4)
        title=Text("Subraction of Numbers upto 9").to_edge(UP)
        Numbers=Text("Numbers: 1 2 3 4 5 6 7 8 9").next_to(title,DOWN)
        self.play(Write(title))
        self.play(Write(Numbers))
        self.wait(1)

        p11=cvo.CVO().CreateCVO("Subtraction","Process of taking\\\\1 number from another")
        p13=cvo.CVO().CreateCVO("Notation","x-y")
        p11.cvolist.append(p13)
        self.construct1(p11,p11)

    def Anim(self):
        title = Text("Subtraction Examples", font_size=72)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        problems = [
            (9, 1, 8),
            (8, 2, 6),
            (6, 3, 3),
            (7, 5, 2),
            (3, 2, 1),
            (9, 7, 2),
            (8, 4, 4),
            (9, 4, 5),
            (5, 5, 0),
        ]
        
        def create_fruit(fruit, row, col):
            fruit_text = Text(fruit, font_size=72)
            x_pos = -6.2 + col * 1.2  # Adjust horizontal spacing (1.2 is an example)
            y_pos = 1 - row * 1.5   # Adjust vertical spacing (1.5 is an example)
            fruit_text.move_to(np.array([x_pos, y_pos, 0]))
            return fruit_text
        
        fruit_emoji = "🍎"

        for total, subtrahend, result in problems:
            problem_text = Text(f"{total} - {subtrahend} = {result}", font_size=72, color=BLUE)
            self.play(Write(problem_text))
            self.wait(1)
            self.play(problem_text.animate.shift(UP * 3.3))
            self.wait(1)
            
            # Create fruits for total
            total_fruits = VGroup()
            for i in range(total):
                col = i % 3  # Adjust columns as needed
                row = i // 3  # Adjust rows as needed
                fruit = create_fruit(fruit_emoji, row, col)
                total_fruits.add(fruit)
            
            total_label = Text(f"{total}", font_size=24)
            total_label.next_to(total_fruits, DOWN)
            
            self.play(
                FadeIn(total_fruits),
                Write(total_label)
            )
            self.wait(1)

            # Animate subtraction
            minus_text = Text("-", font_size=144, color=BLUE)
            minus_text.next_to(total_fruits, RIGHT)
            self.play(Write(minus_text))
            self.wait(1)

            # Create fruits for subtrahend
            subtrahend_fruits = VGroup()
            for i in range(subtrahend):
                col = i % 3  # Adjust columns as needed
                row = i // 3  # Adjust rows as needed
                fruit = create_fruit(fruit_emoji, row, col)
                subtrahend_fruits.add(fruit)

            subtrahend_fruits.next_to(minus_text, RIGHT)
            
            subtrahend_label = Text(f"{subtrahend}", font_size=24)
            subtrahend_label.next_to(subtrahend_fruits, DOWN)
            
            self.play(
                FadeIn(subtrahend_fruits),
                Write(subtrahend_label)
            )
            self.wait(1)

            # Animate equals sign
            equal_text = Text("=", font_size=144, color=BLUE)
            equal_text.next_to(subtrahend_fruits, RIGHT)
            self.play(Write(equal_text))
            self.wait(1)

            # Create fruits for result
            result_fruits = VGroup()
            for i in range(result):
                col = i % 3  # Adjust columns as needed
                row = i // 3  # Adjust rows as needed
                fruit = create_fruit(fruit_emoji, row, col)
                result_fruits.add(fruit)

            result_fruits.next_to(equal_text, RIGHT)
            
            result_label = Text(f"{result}", font_size=24)
            result_label.next_to(result_fruits, DOWN)
            
            self.play(
                FadeIn(result_fruits),
                Write(result_label)
            )
            self.wait(1)
            
            # Fade out all elements for the current problem
            self.play(
                FadeOut(problem_text),
                FadeOut(total_fruits),
                FadeOut(subtrahend_fruits),
                FadeOut(result_fruits),
                FadeOut(total_label),
                FadeOut(subtrahend_label),
                FadeOut(result_label),
                FadeOut(minus_text),
                FadeOut(equal_text)
            )
        
        self.wait(2)


if __name__ == "__main__":
    scene = Chap8G1_SubUptoNine()
    scene.render()
    