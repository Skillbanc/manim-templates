from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class Addition(AbstractAnim):
    def construct(self):
        self.Add()
        self.NUM()

    def Add(self):

        self.isRandom=False

        augend = MathTex("7").scale(3).move_to(LEFT)
        plus = MathTex("+").scale(3).next_to(augend, RIGHT)
        addend = MathTex("5").scale(3).next_to(plus, RIGHT)
        equals = MathTex("=").scale(3).next_to(addend, RIGHT)
        sum_result = MathTex("12").scale(3).next_to(equals, RIGHT)

        augend_label = Text("Augend", color=WHITE).scale(0.7).next_to(augend, LEFT)
        addend_label = Text("Addend", color=WHITE).scale(0.7).next_to(addend, DOWN)
        sum_label = Text("Sum", color=WHITE).scale(0.7).next_to(sum_result, RIGHT)
        plus_label = Text("Plus", color=WHITE).scale(0.7).next_to(plus, UP)


        self.play(Write(augend), Write(plus), Write(addend), Write(equals), Write(sum_result))
        self.play(Write(augend_label), Write(addend_label), Write(sum_label), Write(plus_label))        
        self.wait(2)
        self.fadeOutCurrentScene()

    def NUM(self):

        self.isRandom=False

        Title=Text("Addition").to_corner(UP)

        p1=cvo.CVO().CreateCVO("n1 + n2","33 + 44").setPosition([0,1,0])

        p2=cvo.CVO().CreateCVO("n1","33").setPosition([-3,-1,0])

        p3=cvo.CVO().CreateCVO("n2","44").setPosition([3,-1,0])

        p4=cvo.CVO().CreateCVO("Result","77").setPosition([0,-3,0])

        self.play(Write(Title))
        self.construct1(p1,p1)
        self.construct1(p2,p2)
        self.play(Create(CurvedArrow(p1.pos,p2.pos)))
        self.construct1(p3,p3)
        self.play(Create(CurvedArrow(p1.pos,p3.pos)))
        self.construct1(p4,p4)
        self.play(Create(CurvedArrow(p1.pos,p4.pos)))

if __name__ == "__main__":
    scene = Addition()
    scene.render()
