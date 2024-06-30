import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class Class8Chap9PlanefiguresAreasAnim(AbstractAnim):

    def construct(self):
        # self.RenderSkillbancLogo()
        # self.Intro()
        # self.fadeOutCurrentScene()
        # self.shape1()
        # self.fadeOutCurrentScene()
        # self.shape2()
        # self.fadeOutCurrentScene()
        # self.shape3()
        # self.fadeOutCurrentScene()
        # self.shape4()
        # self.fadeOutCurrentScene()
        # self.shape5()
        # self.fadeOutCurrentScene()
        # self.shape6()
        # self.fadeOutCurrentScene()
        # self.shape7()
        # self.fadeOutCurrentScene()
        self.quad()
        # self.GithubSourceCodeReference()
    

    def SetDeveloperList(self):
        self.DeveloperList = "Lasya Nannapaneni"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName = "Class8Chap9PlanefiguresAreasAnim.py"    


    def Intro(self):
        
        self.isRandom = False
        # self.play(Write(NumberPlane()))
        self.positionChoice=[[-4.5,2,0],[0,2,0],[-5,-2,0],[-1,0,0],[-1,-2,0],[1,0,0],[1,-2,0],[5,0,0],[5,-2,0]]

        p1=cvo.CVO().CreateCVO("Plane Figures and their Areas","")
        p2=cvo.CVO().CreateCVO("Types of plane figures", "")
       
        p12=cvo.CVO().CreateCVO("Rectangle","")
        p13=cvo.CVO().CreateCVO("Triangle", "")
        p14=cvo.CVO().CreateCVO("Square","")
        p15=cvo.CVO().CreateCVO("parallelogram", "")
        p16=cvo.CVO().CreateCVO("Rhombus", "")
        p17=cvo.CVO().CreateCVO("Trapezium","")
        p18=cvo.CVO().CreateCVO("Circle", "")

        p1.cvolist.append(p2)
        p2.cvolist.append(p12)
        p2.cvolist.append(p13)
        p2.cvolist.append(p14)
        p2.cvolist.append(p15)
        p2.cvolist.append(p16)
        p2.cvolist.append(p17)
        p2.cvolist.append(p18)
        
        self.construct1(p1,p1)

    
    def shape1(self):
        
        t1 = Text("Circle", font = "Comic Sans MS", color= LIGHT_PINK,weight = BOLD)
        t2 = Text("r", color=WHITE)
        c = Circle(color=BLUE, 
                   stroke_width = 10,
                   fill_opacity = 0.2,
                   fill_color = ORANGE,
                   radius = 1.5
                   )
        
        c.move_to(LEFT*4)
        t1.move_to([-4,2,0])
        t2.move_to([-4.5,0.75,0])
        arrow = DoubleArrow(color = ORANGE,start=[-4,-0.25,0],end=[-4,1.75,0])

        self.play(Write(c))
        self.play(Write(t1)) 
        # self.play(Write(NumberPlane()))
        self.play(Create(arrow))
        self.play(Write(t2)) 
        self.wait(1)

        self.isRandom = False

        p2=cvo.CVO().CreateCVO("Area Formula","1/2(3.14)r*r").setPosition([2.5,2,0])
        p3=cvo.CVO().CreateCVO("Radius","r").setPosition([6,2,0])
        p4=cvo.CVO().CreateCVO("Example", "r=7").setPosition([1,-2,0])
        p5=cvo.CVO().CreateCVO("Area of Circle", "1/2(3.14)(7*7) = 77").setPosition([5,-2.5,0])

        p2.cvolist.append(p3)
        p2.cvolist.append(p4)
        p4.cvolist.append(p5)

        self.construct1(p2,p2)
        # p2.setcircleradius(1.5)
        # p3.setcircleradius(1.5)
        # p4.setcircleradius(3)
        # p5.setcircleradius(2)


    def shape2(self):

        t1 = Text("Square", font = "Comic Sans MS",color=LIGHT_PINK,weight=BOLD)
        t2 = Text("a",color=WHITE)
        s = Square(color=BLUE, 
                   side_length = 2.5,
                   stroke_width = 10,
                   fill_opacity = 0.2,
                   fill_color = YELLOW
                   )
        
        s.move_to(LEFT*4)
        t1.move_to([-4,2,0])
        t2.move_to([-6,0,0])
        arrow = DoubleArrow(color = ORANGE,start=[-5.5,1.5,0],end=[-5.5,-1.5,0])

        # self.play(Write(NumberPlane()))
        self.play(Write(s))
        self.play(Write(t1))
        self.play(Create(arrow))
        self.play(Write(t2))
        self.wait(1)

        self.isRandom = False

        p4=cvo.CVO().CreateCVO("Side","a").setPosition([6,2,0])
        p5=cvo.CVO().CreateCVO("Area Formula","a*a").setPosition([2.5,2,0])
        p6=cvo.CVO().CreateCVO("Example", "a=4").setPosition([1,-2,0])
        p7=cvo.CVO().CreateCVO("Area of Square", "4*4=16").setPosition([5,-2.5,0])

        p5.cvolist.append(p4)
        p5.cvolist.append(p6)
        p6.cvolist.append(p7)

        self.construct1(p5,p5)
 
    def shape3(self):

        t1 =  Text("Rectangle",font="Comic Sans MS",color=LIGHT_PINK,weight=BOLD)
        t2 = Text("l",color=WHITE)
        t3 = Text("b",color=WHITE)
        r = Rectangle(color=BLUE, 
                   stroke_width = 10,
                   fill_opacity = 0.2,
                   fill_color = YELLOW,
                   width = 2.5,
                   height = 4)
        
        r.move_to(LEFT*4)
        t1.move_to([-4,3,0])
        t2.move_to([-6,0,0])
        t3.move_to([-4,-3,0])
        arrow1 = DoubleArrow(color= ORANGE,start=[-5.5,2.25,0],end=[-5.5,-2.25,0])
        arrow2 = DoubleArrow(color=ORANGE,start=[-2.5,-2.25,0],end=[-5.5,-2.25,0])
    
        self.play(Write(r))
        self.play(Write(t1))
        self.play(Create(arrow1))
        self.play(Write(t2))
        self.play(Create(arrow2))
        self.play(Write(t3))
        # self.play(Write(NumberPlane()))
        self.wait(1)

        self.isRandom = False
   
        p2=cvo.CVO().CreateCVO("Area Formula", "l*b").setPosition([2.5,2,0])
        p3=cvo.CVO().CreateCVO("length","l").setPosition([6,2,0])
        p4=cvo.CVO().CreateCVO("breadth","b").setPosition([4,-0.5,0])
        p5=cvo.CVO().CreateCVO("Example","l=6 b=8").setPosition([1,-2,0])
        p6=cvo.CVO().CreateCVO("Area of Rectangle", "6*8=48").setPosition([5,-2.5,0])
        
        p2.cvolist.append(p3)
        p2.cvolist.append(p4)
        p2.cvolist.append(p5)
        p5.cvolist.append(p6)
        
        self.construct1(p2,p2)
    

    def shape4(self):

        t1 = Text("Triangle",font="Comic Sans MS",color=LIGHT_PINK,weight=BOLD)
        t2= Text("h",color=WHITE)
        t3= Text("b",color=WHITE)
        tri = Triangle(color=BLUE, 
                   stroke_width = 10,
                   fill_opacity = 0.2,
                   fill_color = ORANGE,
                  )
        
        tri.move_to([LEFT*5])
        t1.move_to([-5,1.5,0])
        t2.move_to([-4.5,0.5,0])
        t3.move_to([-5,-1.25,0])
        arrow1 = DoubleArrow(color=ORANGE,start=[-5,1,0],end=[-5,-1,0])
        arrow2 = DoubleArrow(color=ORANGE,start=[-6.25,-1,0],end=[-3.75,-1,0])

        self.play(Write(tri))
        self.play(Write(t1))
        self.play(Create(arrow1))
        self.play(Write(t2))
        self.play(Create(arrow2))
        self.play(Write(t3))

        # self.play(Write(NumberPlane()))
        self.wait(1)

        p2=cvo.CVO().CreateCVO("Area Formula", "1/2(b*h)").setPosition([2.5,2,0]).setangle(-TAU/4)
        p3=cvo.CVO().CreateCVO("base","b").setPosition([6,2,0])
        p4=cvo.CVO().CreateCVO("height","h").setPosition([4,-0.5,0])
        p5=cvo.CVO().CreateCVO("Example", "b=8 h=8").setPosition([1,-2,0]).setangle(-TAU/4)
        p6=cvo.CVO().CreateCVO("Area of Triangle", "1/2(8*8) = 32").setPosition([5,-2.5,0])

        p2.cvolist.append(p3)
        p2.cvolist.append(p4)
        p2.cvolist.append(p5)
        p5.cvolist.append(p6)

        self.construct1(p2,p2)

    def shape5(self):  
         
        # self.play(Write(NumberPlane()))
        t1 = Text("Parallelogram",font="Comic Sans MS",color=LIGHT_PINK,weight=BOLD)
        t2 = Text("b",color=WHITE)
        t3 = Text("h",color=WHITE)
        l1 = Line(color=BLUE,stroke_width= 10,start=[-6,2,0],end=[-3,1,0])
        l2 = Line(color=BLUE,stroke_width= 10,start=[-3,1,0],end=[-3,-3,0])
        l3 = Line(color=BLUE,stroke_width= 10,start=[-3,-3,0],end=[-6,-2,0])
        l4 = Line(color=BLUE,stroke_width= 10,start=[-6,-2,0],end=[-6,2,0])

        t1.move_to([-4,3,0])
        t2.move_to([-6.5,0,0])
        t3.move_to([-3.5,-1.25,0])
        arrow1 = DoubleArrow(color=ORANGE,start=[-6.25,2.25,0],end=[-6.25,-2.25,0])
        arrow2 = DoubleArrow(color=ORANGE,start=[-6.25,-1.75,0],end=[-2.75,-1.75,0])

        self.play(Write(l1))
        self.play(Write(l2))
        self.play(Write(l3))
        self.play(Write(l4))
        self.play(Write(t1))
        self.play(Create(arrow1))
        self.play(Write(t2))
        self.play(Create(arrow2))
        self.play(Write(t3))
        self.wait(1)

        p2=cvo.CVO().CreateCVO("Area Formula", "b*h").setPosition([2.5,2,0])
        p3=cvo.CVO().CreateCVO("base","b").setPosition([6,2,0])
        p4=cvo.CVO().CreateCVO("height","h").setPosition([4,-0.5,0])
        p5=cvo.CVO().CreateCVO("Example", "b=8 h=8").setPosition([1,-2,0])
        p6=cvo.CVO().CreateCVO("Area of Parallelogram", "8*8 = 64").setPosition([5,-2.5,0])

        p2.cvolist.append(p3)
        p2.cvolist.append(p4)
        p2.cvolist.append(p5)
        p5.cvolist.append(p6)

        self.construct1(p2,p2)


    def shape6(self):  
         
        # self.play(Write(NumberPlane()))
        t1 = Text("Rhombus",font="Comic Sans MS",color=LIGHT_PINK,weight=BOLD)
        t2 = Text("d1",color=WHITE)
        t3 = Text("d2",color=WHITE)
        l1 = Line(color=BLUE,stroke_width= 10,start=[-6,0,0],end=[-4.5,2,0])
        l2 = Line(color=BLUE,stroke_width= 10,start=[-4.5,2,0],end=[-3,0,0])
        l3 = Line(color=BLUE,stroke_width= 10,start=[-3,0,0],end=[-4.5,-2,0])
        l4 = Line(color=BLUE,stroke_width= 10,start=[-4.5,-2,0],end=[-6,0,0])

        t1.move_to([-4.5,3,0])
        t2.move_to([-4.25,1,0])
        t3.move_to([-5.25,-0.25,0])
        arrow1 = DoubleArrow(color=ORANGE,start=[-4.5,2.25,0],end=[-4.5,-2.25,0])
        arrow2 = DoubleArrow(color=ORANGE,start=[-6.25,0,0],end=[-2.75,0,0])

        self.play(Write(l1))
        self.play(Write(l2))
        self.play(Write(l3))
        self.play(Write(l4))
        self.play(Write(t1))
        self.play(Create(arrow1))
        self.play(Write(t2))
        self.play(Create(arrow2))
        self.play(Write(t3))
        self.wait(1)

        self.isRandom = False
       
        p2=cvo.CVO().CreateCVO("Area Formula", "1/2(d1*d2)").setPosition([2.5,2,0])
        p3=cvo.CVO().CreateCVO("diagonal 1","d1").setPosition([6,2,0])
        p4=cvo.CVO().CreateCVO("diagonal 2","d2").setPosition([4,-0.5,0])
        p5=cvo.CVO().CreateCVO("Example","d1=8 d2=6").setPosition([1,-2,0])
        p6=cvo.CVO().CreateCVO("Area of Rhombus", "1/2(8*6) = 24").setPosition([5,-2.5,0])

        p2.cvolist.append(p3)
        p2.cvolist.append(p4)
        p2.cvolist.append(p5)
        p5.cvolist.append(p6)

        self.construct1(p2,p2)

    

    def shape7(self):  
         
        # self.play(Write(NumberPlane()))
        t1 = Text("Trapezium",font="Comic Sans MS",color=LIGHT_PINK,weight=BOLD)
        t2 = Text("a",color=WHITE)
        t3 = Text("b",color=WHITE)
        t4 = Text("h",color=WHITE)
        l1 = Line(color=BLUE,stroke_width= 10,start=[-5,1,0],end=[-3,1,0])
        l2 = Line(color=BLUE,stroke_width= 10,start=[-2,-1,0],end=[-6,-1,0])
        l3 = Line(color=BLUE,stroke_width= 10,start=[-5,1,0],end=[-6,-1,0])
        l4 = Line(color=BLUE,stroke_width= 10,start=[-2,-1,0],end=[-3,1,0])

        t1.move_to([-4,3,0])
        t2.move_to([-4,1.5,0])
        t3.move_to([-4,-2,0])
        t4.move_to([-4.75,0,0])
        arrow1 = DoubleArrow(color=ORANGE,start=[-2.75,1.25,0],end=[-5.25,1.25,0])
        arrow2 = DoubleArrow(color=ORANGE,start=[-1.75,-1.25,0],end=[-6.25,-1.25,0])
        arrow3 = DoubleArrow(color=ORANGE,start=[-5,1.25,0],end=[-5,-1.25,0])

        self.play(Write(l1))
        self.play(Write(l2))
        self.play(Write(l3))
        self.play(Write(l4))
        self.play(Write(t1))
        self.play(Create(arrow1))
        self.play(Write(t2))
        self.play(Create(arrow2))
        self.play(Write(t3))
        self.play(Create(arrow3))
        self.play(Write(t4))
        self.wait(1)    

        self.isRandom = False
       
        p2=cvo.CVO().CreateCVO("Area Formula", "h*((a+b)/2)").setPosition([2.5,2,0])
        p3=cvo.CVO().CreateCVO("height","h").setPosition([6,2,0])
        p4=cvo.CVO().CreateCVO("parallel side 1","a").setPosition([4,-0.5,0])
        p5=cvo.CVO().CreateCVO("parallel side 2","b").setPosition([-0.5,2,0])
        p6=cvo.CVO().CreateCVO("Example", "a=8 b=8 h=4").setPosition([1,-2,0])
        p7=cvo.CVO().CreateCVO("Area of Trapezium", "4*((8+8)/2) = 24").setPosition([5,-2.5,0])
        p2.cvolist.append(p3)
        p2.cvolist.append(p4)
        p2.cvolist.append(p5)
        p2.cvolist.append(p6)
        p6.cvolist.append(p7)
        self.construct1(p2,p2)


    def quad(self):
        
        self.play(Write(NumberPlane()))
        title = Text("Area of a Quadrilateral",font_size=45)
        title.move_to([-3,3.3,0])
        u = Underline(title)
        subtil = Text("A quadrilateral can be split into two"
                      "\n\ntriangles by drawing one of its diagonals",font_size=25)
        subtil.move_to([-2.5,2,0])
        self.play(Write(title))
        self.play(Write(u))
        self.play(Write(subtil))

        a = ((1.9,0.2,0),(5.1,0.6,0),(5.5,2.5,0),(2.5,2,0),(1.9,0.2,0),(5.5,2.5,0))
        ex1 = Polygon(*a,color=WHITE,stroke_width=5)
        self.play(Write(ex1))
        self.wait()

        s1= Text("A").move_to([1.5,0.2,0])
        s2= Text("B").move_to([2.1,2.1,0])
        s3= Text("C").move_to([5.8,2.5,0])
        s4= Text("D").move_to([5.5,0.6,0])
        self.play(Write(s1))
        self.play(Write(s2))
        self.play(Write(s3))
        self.play(Write(s4))

        dia = DoubleArrow(start=[1.8,0.05,0], end=[5.6,2.4,0],color=RED,stroke_width=1)
        self.play(Write(dia))

        t1 = Text("d",color=RED,font_size=25).move_to([3.7,1.7,0])
        self.play(Write(t1))

        d1 = DashedLine(start=[2.5,2,0],end=[3.1,1,0],color=BLUE)
        self.play(Write(d1))

        d2 = DashedLine(start=[5.1,0.6,0],end=[4.4,1.7,0],color=BLUE)
        self.play(Write(d2))

        a1 = ((3,1.1,0),(3.1,1,0))


            




if __name__ == "__main__":
    scene = Class8Chap9PlanefiguresAreasAnim()
    scene.render()