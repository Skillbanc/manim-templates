from AbstractAnim import AbstractAnim
from manim import *

class ascen(AbstractAnim):
    def construct(self):  

        heading = Text("Ascending  order :",color=DARK_BROWN,font_size=37).to_edge(UP*1.25+LEFT * 1)
        sub_title1 = Text("Ascending order is the arrangement of elements from smallest to largest.",font_size=29).to_edge(UP*3)
        sub_title2 = Text("example:  58 , 95 , 96 , 44 ",font_size=29).to_edge(UP*4.75)
        sub_title3 = Text("Ascending  order is     44 , 58 , 95 , 96",font_size=29).to_edge(UP*6.6)
        heading2 = Text("Descending order :",color=PINK,font_size=37).to_edge(UP*9+LEFT * 1)
        sub_title5 = Text("Descending order is the arrangement of elements from largest to smallest.",font_size=29).to_edge(UP*10.5)
        sub_title6 = Text("example:   58 , 95 , 96 , 44 ",font_size=29).to_edge(UP*12)
        sub_title7 = Text("Descending order is     96 , 95 , 58 , 44",font_size=29).to_edge(UP*13.5)
        
        self.play(Write(heading))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)
        self.play(Write(sub_title3))
        self.wait(1)
        self.play(Write(heading2))
        self.wait(1)
        self.play(Write(sub_title5))
        self.wait(1)
        self.play(Write(sub_title6))
        self.wait(1)
        self.play(Write(sub_title7))

        

if __name__ == "__main__":
    from manim import *
    scene = ascen()
    scene.render()