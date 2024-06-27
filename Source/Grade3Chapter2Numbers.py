import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class numbers(AbstractAnim):
    def construct(self):
        self.Introduction()

    def Introduction(self):
        self.angleChoice=[TAU/4,TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Three-digit Number","").setPosition([-3,0,0])
        p11=cvo.CVO().CreateCVO("Ones","1").setPosition([0,2,0])
        p12=cvo.CVO().CreateCVO("Tens","10").setPosition([3,0,0])
        p13=cvo.CVO().CreateCVO("Hundereds","100").setPosition([0,-2,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
    
    def hundred_intro(self):
        twodigit = Text("9 tens + 9 ones = 99").shift(UP*2)
        self.play(Write(twodigit))
        self.wait(2)
        text = Text("99 is the largest 2 digit number").next_to(twodigit,DOWN,buff=1).set_color(YELLOW)
        self.play(FadeIn(text))
        self.wait(2)
        self.play(FadeOut(twodigit,text))
        
        # Transform to the next equation
        threedigit = Text("9 tens ").shift(UP*2,LEFT*2)
        threedigit1 = Text("+ 9 ones + 1").next_to(threedigit,RIGHT,buff=0.3)
        self.play(Write(threedigit),Write(threedigit1))
        self.wait(2)
        transform_twodigit = Text("+ 1 ten").next_to(threedigit,RIGHT,buff=0.3)
        self.play(Transform(threedigit1, transform_twodigit))
        self.wait(2)
        threedigit2 = Text("= 10 tens").next_to(transform_twodigit,RIGHT,buff=0.3)
        self.play(Write(threedigit2))
        self.wait(1)
        transform_threedigit = Text("= 100").next_to(transform_twodigit,RIGHT,buff=0.3)
        self.play(Transform(threedigit2, transform_threedigit))
        self.wait(2)

        text = Text("100 is the smallest 3 digit number").set_color(YELLOW)
        self.play(FadeIn(text))
        self.wait(2)
        self.play(FadeOut(threedigit,threedigit1,threedigit2,text))

        hundered1 = Text("1 hundred + 1 one = 101").shift(UP*2).set_color(YELLOW)
        self.play(Write(hundered1))
        self.wait(2)

        hundered10 = Text("1 hundred + 1 ten = 110").next_to(hundered1,DOWN,buff=1).set_color(YELLOW)
        self.play(Write(hundered10))
        self.wait(2)

        hundered11 = Text("1 hundred + 1 ten + 1 one = 111").next_to(hundered10,DOWN,buff=1).set_color(YELLOW)
        self.play(Write(hundered11))
        self.wait(2)
    
    def Identifying_numbers(self):
        text = Text("Identify the Number using hundereds, tens and ones",font_size=40).set_color(BLUE).to_edge(UP)
        self.play(Write(text))
        self.wait(2)
        table_data = [
            ["100", "10", "1", "Number"],
            ["2", "5", "3", ""],
            ["9", "1", "-", ""],
            ["7", "-", "4", ""],
        ]
        
        # Create the table
        table = Table(
            table_data,
            include_outer_lines=True,
        )
        # Add different colors to each column
        colors = [BLUE, GREEN, RED, YELLOW]
        for i, color in enumerate(colors):
            for j in range(4):
                cell = table.get_cell((j+1, i+1))
                cell.set_fill(color, opacity=0.5)
        table.scale(0.75)

        # Add the table to the scene
        self.play(FadeIn(table))
        self.wait(2)

        number1=Text("253",font_size=35).shift(RIGHT*2,UP*0.5).set_color(YELLOW)
        self.play(FadeIn(number1))
        self.wait(2)

        number2=Text("910",font_size=35).next_to(number1,DOWN,buff=0.75).set_color(YELLOW)
        self.play(FadeIn(number2))
        self.wait(2)

        number3=Text("704",font_size=35).next_to(number2,DOWN,buff=0.5).set_color(YELLOW)
        self.play(FadeIn(number3))
        self.wait(2)
    
    # def Placevalue(self):
        











    def SetDeveloperList(self):
        self.DeveloperList="Sindhu"
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="MultiplyandDivide.py"

              
if __name__ == "__main__":
    scene = numbers()
    scene.render()