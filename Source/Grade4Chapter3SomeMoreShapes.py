from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class Shapes(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.first()
        self.shape()

    def first(self):
        self.isRandom=False

        p1=cvo.CVO().CreateCVO("some common Shapes","").setPosition([0,2.5,0])
        p2=cvo.CVO().CreateCVO("Circle","").setPosition([-4,0,0])
        p3=cvo.CVO().CreateCVO("Square","").setPosition([-1,0,0])
        p4=cvo.CVO().CreateCVO("Rectangle","").setPosition([2,0,0])
        p5=cvo.CVO().CreateCVO("Triangle","").setPosition([4,0,0])

        self.construct1(p1,p1)
        self.construct1(p2,p2)
        self.play(Create(CurvedArrow(p1.pos,p2.pos)))
        self.construct1(p3,p3)
        self.play(Create(CurvedArrow(p1.pos,p3.pos)))
        self.construct1(p4,p4)
        self.play(Create(CurvedArrow(p1.pos,p4.pos)))
        self.construct1(p5,p5)
        self.play(Create(CurvedArrow(p1.pos,p5.pos)))
        self.fadeOutCurrentScene()


    def shape(self):
        self.isRandom=False

        sub_Title = Text("Circle").scale(0.8).to_corner(UP)
        c = Circle(1.5)
        self.play(Create(c),Write(sub_Title))
        self.wait(2)
        self.fadeOutCurrentScene()

        sub_Title = Text("Square").scale(0.8).to_edge(UP)
        s=Square(2)
        self.play(Create(s),Write(sub_Title))
        self.wait(2)
        self.fadeOutCurrentScene()

        sub_Title = Text("Rectangle").scale(0.8).to_edge(UP)
        s=Rectangle()
        self.play(Create(s),Write(sub_Title))
        self.wait(2)
        self.fadeOutCurrentScene()

        sub_Title = Text("Triangle").scale(0.8).to_edge(UP)
        s=Triangle().scale(2)
        self.play(Create(s),Write(sub_Title))
        self.wait(2)
        self.fadeOutCurrentScene()

if __name__ == "__main__":
    scene = Shapes()
    scene.render()
