from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class polynomials(AbstractAnim):

    def construct(self):
        self.ptypes()
        self.Exp()
        self.div()
        self.poly()
        self.graph()

    def ptypes(self):

        self.isRandom=False
        p21=cvo.CVO().CreateCVO("Polynomial","")
        p21.setPosition([0,2.5,0])

        p22=cvo.CVO().CreateCVO("Linear Polynomial","")
        p22.setPosition([-3,1,0])
        p22.setangle([-TAU/3])
        p21.cvolist.append(p22)

        p23=cvo.CVO().CreateCVO("Quadratic polynomial","")
        p23.setPosition([0,-2.5,0])
        p23.setangle([-TAU/3])
        p21.cvolist.append(p23)

        p24=cvo.CVO().CreateCVO("Cubic polynomial","")
        p24.setPosition([3,1,0])
        p24.setangle([-TAU/4])
        p21.cvolist.append(p24)

        self.construct1(p21,p21)
        self.fadeOutCurrentScene()
        
    def Exp(self):
        
        self.isRandom=False

        p1=cvo.CVO().CreateCVO("Expression","$ 3x^2 + 2x + 7 $")
        p1.setPosition([-4,0,0])

        p2=cvo.CVO().CreateCVO("degree","2")
        p2.setPosition([3,2,0])
        p1.cvolist.append(p2)

        p3=cvo.CVO().CreateCVO("co.efficient of polynomial","3")
        p3.setPosition([3,-1,0])
        p1.cvolist.append(p3)

        self.construct1(p1,p1)
        self.fadeOutCurrentScene()
        
    def div(self):
        self.isRandom=False

        p1=cvo.CVO().CreateCVO("g(x)","$ x-1 $").setPosition([-1,2,0])
        p2=cvo.CVO().CreateCVO("p(x)","$ x^3-6x^2+9x+3 $").setPosition([1,2,0])
        p3=cvo.CVO().CreateCVO(" Divisor ","").setPosition([-4,-1,0])
        p4=cvo.CVO().CreateCVO("Dividend","").setPosition([4,-1,0])
        p5=cvo.CVO().CreateCVO("operation","Division").setPosition([0,-2,0])
        p6=cvo.CVO().CreateCVO("Remainder","7").setPosition([3,-2.5,0])

        self.construct1(p1,p1)
        self.construct1(p2,p2)
        self.construct1(p3,p3)
        self.play(Create(CurvedArrow(p3.pos,p1.pos)))
        self.construct1(p4,p4)
        self.play(Create(CurvedArrow(p4.pos,p2.pos)))
        self.construct1(p5,p5)
        self.play(Create(CurvedArrow(p1.pos,p5.pos)),Create(CurvedArrow(p2.pos,p5.pos)))
        self.construct1(p6,p6)
        self.play(Create(CurvedArrow(p5.pos,p6.pos)))

        self.fadeOutCurrentScene()

    def poly(self):

        self.isRandom=False

        p1=cvo.CVO().CreateCVO("g(x)","$ 4x^2+2x^2-2x+6 $").setPosition([0,2.5,0])

        p2=cvo.CVO().CreateCVO("X values","3").setPosition([-4,1,0])
        p1.cvolist.append(p2)

        p3=cvo.CVO().CreateCVO("g(3)","54").setPosition([4,1,0])
        p1.cvolist.append(p3)
        self.play(Create(CurvedArrow(p2.pos,p3.pos)))

        p4=cvo.CVO().CreateCVO("No. of terms","4").setPosition([-2,-1,0])
        p1.cvolist.append(p4)

        p5=cvo.CVO().CreateCVO("Like terms","$ 4x^2 and 2x^2 $").setPosition([2,-1,0])
        p1.cvolist.append(p5)

        p6=cvo.CVO().CreateCVO("unlike terms","$ 4x^2, 2x^2, -2x and 6 $").setPosition([-2,-3,0])
        p1.cvolist.append(p6)

        p7=cvo.CVO().CreateCVO("Addtional like terms","$ 6x^2 $").setPosition([2,-3,0])
        p1.cvolist.append(p7)

        self.construct1(p1,p1)
        
        self.fadeOutCurrentScene()



    def graph(self):

        self.isRandom=False

        p1=cvo.CVO().CreateCVO("Equation","$ y=2x+3 $").setPosition([0,2.5,0])

        p2=cvo.CVO().CreateCVO("X values","-2, -1, 0, 3").setPosition([-4,-1,0])
        p1.cvolist.append(p2)

        p3=cvo.CVO().CreateCVO("Y values","-1,1,3,7").setPosition([-2,-1,0])
        p1.cvolist.append(p3)

        p4=cvo.CVO().CreateCVO("(X,Y) values","(-2,-1),(-1,1),(0,3),(3,7)").setPosition([1,-1,0])
        p1.cvolist.append(p4)
        self.construct1(p1,p1)

        self.fadeOutCurrentScene()

        graph_title = Text("Graphical representation of y = 2x + 3 ").scale(0.7).to_edge(DOWN)
        plane = Axes(x_range=[-3, 3], y_range=[-2, 8], axis_config={"include_numbers": True}).scale(0.7)
        graph = plane.plot(lambda x: 2 * x + 3, color=BLUE)
        self.play(Create(plane),Write(graph_title))
        self.play(Create(graph))

        points = [plane.coords_to_point(x, 2 * x + 3) for x in [-2, -1, 0, 2]]
        dots = VGroup(*[Dot(point, color=RED) for point in points])
        self.play(FadeIn(dots))

        self.wait(3)


if __name__ == "__main__":
    scene = polynomials()
    scene.render()
