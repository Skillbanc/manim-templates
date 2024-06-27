from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class simpleEquation(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.gen()
        self.Equ()
        self.ADD()
        self.SUB()
        self.MUL()
        self.DIV()

    def gen(self):
        self.isRandom=False

        p1=cvo.CVO().CreateCVO("Simple Equations","X=15").setPosition([0,3,0])

        p2=cvo.CVO().CreateCVO("Variable term","X").setPosition([-2,0,0])

        p3=cvo.CVO().CreateCVO("constant term","15").setPosition([2,0,0])

        p4=cvo.CVO().CreateCVO("Related by","=").setPosition([0,-2,0])

        self.construct1(p1,p1)
        self.construct1(p2,p2)
        self.play(Create(CurvedArrow(p1.pos,p2.pos)))
        self.construct1(p3,p3)
        self.play(Create(CurvedArrow(p1.pos,p3.pos)))
        self.construct1(p4,p4)
        self.play(Create(CurvedArrow(p2.pos,p4.pos)),Create(CurvedArrow(p3.pos,p4.pos)))
        self.fadeOutCurrentScene()

    def Equ(self):
        self.isRandom=False

        p1=cvo.CVO().CreateCVO("Equation","$ 12 + X = 20 $").setPosition([0,2.5,0])

        p2=cvo.CVO().CreateCVO("variable","X").setPosition([-2,1,0])
        p1.cvolist.append(p2)

        p3=cvo.CVO().CreateCVO("Constant","20, 12").setPosition([1,1,0])
        p1.cvolist.append(p3)

        p4=cvo.CVO().CreateCVO("LHS","$ 12 + X $").setPosition([-3,-1,0])
        p1.cvolist.append(p4)

        p5=cvo.CVO().CreateCVO("RHS","20").setPosition([0,-1,0])
        p1.cvolist.append(p5)

        p6=cvo.CVO().CreateCVO("Co efficient of variable","1").setPosition([3,-1,0])
        p1.cvolist.append(p6)

        self.construct1(p1,p1)
        self.fadeOutCurrentScene()


    def ADD(self):
        self.isRandom=False

        title1=Text("Solving equations using addtions").scale(0.8).to_edge(UP)
        self.play(Write(title1))

        p1=cvo.CVO().CreateCVO("Variable term (X)","8").setPosition([-3,1,0])

        p2=cvo.CVO().CreateCVO("Constant term (K)","3").setPosition([-3,-1,0])

        p3=cvo.CVO().CreateCVO("$ X+K=N $","$ 8+3=11 $").setPosition([0,0,0])

        p4=cvo.CVO().CreateCVO("N","11").setPosition([3,0,0])

        self.construct1(p1,p1)
        self.construct1(p2,p2)
        self.construct1(p3,p3)
        self.play(Create(CurvedArrow(p1.pos,p3.pos)),Create(CurvedArrow(p2.pos,p3.pos)))
        self.construct1(p4,p4)
        self.play(Create(CurvedArrow(p3.pos,p4.pos)))
        self.fadeOutCurrentScene()

    def SUB(self):
        self.isRandom=False

        title1=Text("Solving equations using subtractions").scale(0.8).to_edge(UP)
        self.play(Write(title1))

        p1=cvo.CVO().CreateCVO("Variable term: X","8").setPosition([-3,1,0])

        p2=cvo.CVO().CreateCVO("Constant term: K","3").setPosition([-3,-1,0])

        p3=cvo.CVO().CreateCVO("$ X - K = N $","$ 8-3=5 $").setPosition([0,0,0])
    
        p4=cvo.CVO().CreateCVO("N","5").setPosition([3,0,0])

        self.construct1(p1,p1)
        self.construct1(p2,p2)
        self.construct1(p3,p3)
        self.play(Create(CurvedArrow(p1.pos,p3.pos)),Create(CurvedArrow(p2.pos,p3.pos)))
        self.construct1(p4,p4)
        self.play(Create(CurvedArrow(p3.pos,p4.pos)))
       
        self.fadeOutCurrentScene()

    def MUL(self):
        self.isRandom=False

        title1=Text("Solving equations using Multiplication").scale(0.8).to_edge(UP)
        self.play(Write(title1))

        p1=cvo.CVO().CreateCVO("Variable term: X","8").setPosition([-3,1,0])

        p2=cvo.CVO().CreateCVO("Constant term: K","3").setPosition([-3,-1,0])

        p3=cvo.CVO().CreateCVO("$ X * K=N $","$ 8 * 3=24 $").setPosition([0,0,0])

        p4=cvo.CVO().CreateCVO("N","24").setPosition([3,0,0])

        self.construct1(p1,p1)
        self.construct1(p2,p2)
        self.construct1(p3,p3)
        self.play(Create(CurvedArrow(p1.pos,p3.pos)),Create(CurvedArrow(p2.pos,p3.pos)))
        self.construct1(p4,p4)
        self.play(Create(CurvedArrow(p3.pos,p4.pos)))
       
        self.fadeOutCurrentScene()

    def DIV(self):
        self.isRandom=False

        title1=Text("Solving equations using Division").scale(0.8).to_edge(UP)
        self.play(Write(title1))

        p1=cvo.CVO().CreateCVO("Variable term: X","8").setPosition([-3,1,0])

        p2=cvo.CVO().CreateCVO("Constant term: K","2").setPosition([-3,-1,0])

        p3=cvo.CVO().CreateCVO("$ X/K=N $","$ 8/2=4 $").setPosition([0,0,0])
        
        p4=cvo.CVO().CreateCVO("N","4").setPosition([3,0,0])

        self.construct1(p1,p1)
        self.construct1(p2,p2)
        self.construct1(p3,p3)
        self.play(Create(CurvedArrow(p1.pos,p3.pos)),Create(CurvedArrow(p2.pos,p3.pos)))
        self.construct1(p4,p4)
        self.play(Create(CurvedArrow(p3.pos,p4.pos)))
       
        self.fadeOutCurrentScene()

if __name__ == "__main__":
    scene = simpleEquation()
    scene.render()



