from manim import *
from AbstractAnim import AbstractAnim
import cvo
from numpy import size

class Grade1Ch3Numbersfrom1to5(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.show_intro()
        self.fadeOutCurrentScene()
        self.introc1()
        self.fadeOutCurrentScene()
        self.num1()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

    def show_intro(self):
        # Title for the scene
        intro_title = Text("Numbers from 1 to 5", font_size=72, color=BLUE)
        self.play(Write(intro_title))
        self.wait(2)
        self.play(FadeOut(intro_title)) 
        title = Text("Introduction to Numbers")
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))
        
        # Numbers 1 to 5

    def num1(self):
        # title = Text("Introduction to Numbers")
        # self.play(Write(title))
        # self.wait(2)
        # self.play(FadeOut(title))
        
        # Numbers 1 to 5 with names
        numbers_and_names = [
            (1, "One"),
            (2, "Two"),
            (3, "Three"),
            (4, "Four"),
            (5, "Five")
        ]
        
        for number, name in numbers_and_names:
            circle = Circle(radius=1, color=BLUE)
            number_text = Text(str(number), font_size=144).move_to(circle.get_center())
            name_text = Text(name, font_size=48)
            name_text.next_to(circle, DOWN)
            
            self.play(Create(circle), Write(number_text))
            self.wait(1)
            self.play(Write(name_text))
            self.wait(1)
            
                    #    FadeOut(number_text), FadeOut(name_text))

            squares = VGroup(*[
                Square(side_length=1).set_color(BLUE)
                for _ in range(number)
            ])
            squares.arrange(RIGHT, buff=0.5).next_to(name_text, UP*3, buff=1)
            
            self.play(Create(squares))
            self.wait(2)
            self.play(FadeOut(number_text), FadeOut(name_text), FadeOut(squares))
            self.play(FadeOut(circle))

        # End message
        end_message = Text("And that's numbers 1 to 5!", font_size=48)
        self.play(Write(end_message))
        self.wait(2)
        self.play(FadeOut(end_message))
        

    def introc1(self):
         
        self.setNumberOfCirclePositions(3)
        #self.angleChoice = [0,0,0]
        self.isRandom = False
        p8=cvo.CVO().CreateCVO("NUMBERS","")
        p9=cvo.CVO().CreateCVO("Definition","The term 'number' refers to a mathematical object\n used to count, measure, and label..").setPosition([2,0,2])
        # p7=cvo.CVO().CreateCVO("Symbol","'X'").setPosition([2,0,2])
        # p10=cvo.CVO().CreateCVO("Example","4 X 5=20").setPosition([2,-2.5,2])
        p8.cvolist.append(p9)
        # p8.cvolist.append(p7)
        # p8.cvolist.append(p10)
        self.construct1(p8,p8)
        self.wait(2)

    def SetDeveloperList(self):
        self.DeveloperList="Sai Krishna Bikkumalla"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade1Ch3Numbersfrom1to5.py"


if __name__ == "__main__":
    scene = Grade1Ch3Numbersfrom1to5()
    scene.render()
