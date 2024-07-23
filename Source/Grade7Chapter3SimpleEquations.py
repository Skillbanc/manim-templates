from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class simpleEquation(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.gen()
        self.Equ()
        self.solve()
        self.transpose1()
        self.ADD()
        self.SUB()
        self.MUL()
        self.DIV()
        self.GithubSourceCodeReference()

    def gen(self):
        self.isRandom=False

        p1=cvo.CVO().CreateCVO("Simple Equations","X=15").setPosition([0,2.5,0])

        p2=cvo.CVO().CreateCVO("Variable term","X").setPosition([-4,0,0]).setangle(TAU/3)

        p3=cvo.CVO().CreateCVO("constant term","15").setPosition([4,0,0])


        self.construct1(p1,p1)
        self.construct1(p2,p2)
        self.play(Create(CurvedArrow(p1.pos,p2.pos)))
        self.construct1(p3,p3)
        self.play(Create(CurvedArrow(p1.pos,p3.pos)))
        self.fadeOutCurrentScene()

    def Equ(self):
        self.isRandom=False

        p1=cvo.CVO().CreateCVO("Equation","$ 12 + X = 20 $").setPosition([0,2.5,0])

        p2=cvo.CVO().CreateCVO("variable term","X").setPosition([-4,1,0])
        p1.cvolist.append(p2)

        p3=cvo.CVO().CreateCVO("Constant term","20, 12").setPosition([4,1,0])
        p1.cvolist.append(p3)

        p4=cvo.CVO().CreateCVO("LHS","$ 12 + X $").setPosition([-3,-1,0])
        p1.cvolist.append(p4)

        p5=cvo.CVO().CreateCVO("RHS","20").setPosition([3,-1,0])
        p1.cvolist.append(p5)

        p6=cvo.CVO().CreateCVO("Co efficient of variable","1").setPosition([0,-2,0])
        p1.cvolist.append(p6)

        self.construct1(p1,p1)
        self.fadeOutCurrentScene()

    def solve(self):
        self.isRandom=False

        text = Text("Solve the equation x + 3 = 7").scale(1).move_to([0,3,0])
        e1 = Text("L.H.S is x + 3 \n\n x + 3 = 7 \n\n x + 3 - 3 = 7 - 3 \n\n x = 7 - 3 \n\n x = 4").scale(0.7)

        self.play(Write(text))
        self.play(Write(e1))
        self.wait(2)
        self.fadeOutCurrentScene()

    def transpose1(self):

        text = Text("Transposing Terms from L.H.S to R.H.S").scale(1).move_to([0,3,0])
        self.play(Write(text))

    def ADD(self):
        
        t1 = Text("1. '+ quantity' becomes '- quantity'").scale(0.7).move_to([0,2,0])
        eg = Text("example:").move_to([-5,1,0]).scale(0.7)
        eg1 = Text("x + 3 = 5 \n\n On Transposing 3 from L.H.S to R.H.S it becomes -3 \n\n x = 5 - 3 \n\n x = 2").scale(0.7).move_to([0,-1,0])

        self.play(FadeIn(t1))
        self.play(FadeIn(eg),FadeIn(eg1),Wait(2))
        self.play(FadeOut(t1),FadeOut(eg),FadeOut(eg1))

        
    def SUB(self):
        
        t1 = Text("1. '- quantity' becomes '+ quantity'").scale(0.7).move_to([0,2,0])
        eg = Text("example:").move_to([-5,1,0]).scale(0.7)
        eg1 = Text("x - 3 = 4 \n\n On Transposing -3 from L.H.S to R.H.S it becomes +3 \n\n x = 4 + 3 \n\n x = 7").scale(0.7).move_to([0,-1,0])

        self.play(FadeIn(t1))
        self.play(FadeIn(eg),FadeIn(eg1),Wait(2))
        self.play(FadeOut(t1),FadeOut(eg),FadeOut(eg1))

    def MUL(self):
        t1 = Text("1. ‘× quantity’ becomes ÷ quantity").scale(0.7).move_to([0,2,0])
        eg = Text("example:").move_to([-5,1,0]).scale(0.7)
        eg1 = Text("x ×  3 = 15 \n\n On Transposing 3 from L.H.S to R.H.S it becomes 1/3 \n\n x = 15/ 3 \n\n x = 5").scale(0.7).move_to([0,-1,0])

        self.play(FadeIn(t1))
        self.play(FadeIn(eg),FadeIn(eg1),Wait(2))
        self.play(FadeOut(t1),FadeOut(eg),FadeOut(eg1))

    def DIV(self):
       
        t1 = Text("1. ‘÷ quantity’ becomes ‘ × quantity’").scale(0.7).move_to([0,2,0])
        eg = Text("example:").move_to([-5,1,0]).scale(0.7)
        eg1 = Text("x ÷ 3 = 5 \n\n On Transposing 1/3 from L.H.S to R.H.S it becomes 3 \n\n x = 5 * 3 \n\n x = 15").scale(0.7).move_to([0,-1,0])

        self.play(FadeIn(t1))
        self.play(FadeIn(eg),FadeIn(eg1),Wait(2))
        self.play(FadeOut(t1),FadeOut(eg),FadeOut(eg1))
        self.fadeOutCurrentScene()

    def SetDeveloperList(self):
        self.DeveloperList="Bhaskar"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade7Chapter3SimpleEquations.py"

if __name__ == "__main__":
    scene = simpleEquation()
    scene.render()



