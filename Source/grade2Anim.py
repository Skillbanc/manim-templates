from manim import *
from AbstractAnim import AbstractAnim

import cvo

class comparingthreedigitnumbers(AbstractAnim):
    def construct(self):
        # p1=cvo.CVO().CreateCVO("cname","oname")
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.Addition()
        self.fadeOutCurrentScene()
        self.comparing()
        self.fadeOutCurrentScene()

    def Addition(self):
        polygon = Text("Comparing Three-Digit Numbers",font_size=40).to_edge(UP*1)
        sub_title1 = Text("For comparing three digit numbers there are three conditions",font_size=29).to_edge(UP*4.0 + LEFT * 1)       
        sub_title2 = Text("condition-1: In 3-digit numbers, if the hundreds are not equal,",font_size=29).to_edge(UP*5.5 + LEFT * 1)
        sub_title3 = Text("the one with more hundreds is bigger"'.',font_size=29).to_edge(UP*6.5 + LEFT * 5.5)
        sub_title4 = Text("condition-2: In 3-digit numbers, if the hundreds are equal,",font_size=29).to_edge(UP*8 + LEFT * 1)
        sub_title5 = Text("the one with more tens is bigger"'.',font_size=29).to_edge(UP*9 + LEFT * 5.5)
        sub_title6 = Text("condition-3: In 3-digit numbers, if the hundreds and tens are equal,",font_size=29).to_edge(UP*10.5 + LEFT * 1)
        sub_title7 = Text("the one with more ones is bigger"'.',font_size=29).to_edge(UP*11.5 + LEFT * 5.5)

        self.play(Write(polygon))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)
        self.play(Write(sub_title3))
        self.wait(1)
        self.play(Write(sub_title4))
        self.wait(1)
        self.play(Write(sub_title5))
        self.wait(1)
        self.play(Write(sub_title6))
        self.wait(1)
        self.play(Write(sub_title7)) 
    

    def comparing(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("One day two friends sold vegetables at the weekly market.","").setPosition([0,2.5,0])
         p11=cvo.CVO().CreateCVO("Rangamma","").setPosition([-4,1.5,0])
         p12=cvo.CVO().CreateCVO("Sitamma","").setPosition([4,1.5,0])
         p10.cvolist.append(p11)
         p10.cvolist.append(p12)

         self.construct1(p10,p10)

         Rangama = Text("Rangama Earned 452",font_size=30).to_edge(UP*7 + LEFT * 1)
         Sitamma = Text("Sitamma earned 381",font_size=30).to_edge(UP*7 + RIGHT * 4)       
         sub_title2 = Text("In 452, there are 4 hundreds"'.',font_size=29).to_edge(UP*8.5 + LEFT * 1)
         sub_title3 = Text("In 381, there are 3 hundreds"'.',font_size=29).to_edge(UP*8.5 + RIGHT * 1)
         sub_title4 = Text("Rs.300 is less than Rs.400, It means Rangamma earned more",font_size=29).to_edge(UP*10)
         sub_title5 = Text("Rs.381 is less than Rs.452, that is 381 < 452",font_size=29).to_edge(UP*11.5)
         sub_title6 = Text("or",font_size=29).to_edge(UP*13)
         sub_title7 = Text("Rs.381 is less than Rs.452, that is 452 > 381",font_size=29).to_edge(UP*14.5)
        

         
         self.play(Write(Rangama))
         self.play(Write(Sitamma))
         self.wait(1)
         self.play(Write(sub_title2))
         self.wait(1)
         self.play(Write(sub_title3))
         self.wait(1)
         self.play(Write(sub_title4))
         self.wait(1)
         self.play(Write(sub_title5))
         self.wait(1)
         self.play(Write(sub_title6))
         self.wait(1)
         self.play(Write(sub_title7))
         self.wait(1)

        
if __name__ == "__main__":
    scene = comparingthreedigitnumbers()
    scene.render()