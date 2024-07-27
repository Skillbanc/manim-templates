import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class Grade8Chapter9PlanefiguresAreasAnim(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Intro()
        self.fadeOutCurrentScene()
        self.shape1()
        self.fadeOutCurrentScene()
        self.shape2()
        self.fadeOutCurrentScene()
        self.shape3()
        self.fadeOutCurrentScene()
        self.shape4()
        self.fadeOutCurrentScene()
        self.shape5()
        self.fadeOutCurrentScene()
        self.shape6()
        self.fadeOutCurrentScene()
        self.shape7()
        self.fadeOutCurrentScene()
        self.quad()
        self.fadeOutCurrentScene()
        self.poly()
        self.fadeOutCurrentScene()
        self.cirpath()
        self.fadeOutCurrentScene()
        self.sector()
        self.fadeOutCurrentScene()
        self.shaded()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
    

    def SetDeveloperList(self):
        self.DeveloperList = "Lasya Nannapaneni"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName = "Grade8Chapter9PlanefiguresAreasAnim.py"    


    def Intro(self):
        
        self.isRandom = False
        
        self.positionChoice=[[-4.5,2,0],[0,2,0],[-5,-2,0],[5,0,0],[5,2,0],[-1,-2,0],[1,-2,0],[-1,0,0],[1,0,0]]

        p1=cvo.CVO().CreateCVO("Plane Figures and their Areas","")
        p2=cvo.CVO().CreateCVO("Types of plane figures", "")
       
        p12=cvo.CVO().CreateCVO("","")
        p12.appendOname("Triangle")
        p12.appendOname("Rectangle")
        p14=cvo.CVO().CreateCVO("","")
        p14.appendOname("Parallelogram")
        p14.appendOname("Square")
        p16=cvo.CVO().CreateCVO("","")
        p16.appendOname("Trapezium")
        p16.appendOname("Rhombus")
        p18=cvo.CVO().CreateCVO("","")
        p18.appendOname("Sector")
        p18.appendOname("Circle")
        p15=cvo.CVO().CreateCVO("","")
        p15.appendOname("Polygon")
        p15.appendOname("Quadrilateral")


        p1.cvolist.append(p2)
        p2.cvolist.append(p12)
        p2.cvolist.append(p14)
        p2.cvolist.append(p15)
        p2.cvolist.append(p16)
        p2.cvolist.append(p18)
        
        self.construct1(p1,p1)
        

    
    def shape1(self):
        
        t1 = Text("Circle", font = "Comic Sans MS", color= LIGHT_PINK,weight = BOLD).move_to([-4,2,0])
        t2 = Text("r", color=WHITE).move_to([-4.5,0.75,0])
        c = Circle(color=BLUE, 
                   stroke_width = 10,
                   fill_opacity = 0.2,
                   fill_color = ORANGE,
                   radius = 1.5
                   ).move_to(LEFT*4)
        
        arrow = DoubleArrow(color = ORANGE,start=[-4,-0.25,0],end=[-4,1.75,0])

        self.play(Write(c))
        self.play(Write(t1)) 
       
        self.play(Create(arrow))
        self.play(Write(t2)) 
        self.wait(1)

        self.isRandom = False

        p2=cvo.CVO().CreateCVO("Area Formula","(3.14)r*r").setPosition([2.5,2,0])
        p3=cvo.CVO().CreateCVO("Radius","r").setPosition([6,2,0])
    
        p2.cvolist.append(p3)

        self.construct1(p2,p2)
      

        a1 = Text("Area Formula = (3.14)r*r \n\n Example: r=3 \n\n Area of Circle = (3.14)(3*3) = 28.26",font_size=25).move_to([0,-2,0])
        self.play(Write(a1),run_time=6)
       

    def shape2(self):

        t1 = Text("Square", font = "Comic Sans MS",color=LIGHT_PINK,weight=BOLD).move_to([-4,2,0])
        t2 = Text("a",color=WHITE).move_to([-6,0,0])
        s = Square(color=BLUE, 
                   side_length = 2.5,
                   stroke_width = 10,
                   fill_opacity = 0.2,
                   fill_color = YELLOW
                   ).move_to(LEFT*4)
        
        arrow = DoubleArrow(color = ORANGE,start=[-5.5,1.5,0],end=[-5.5,-1.5,0])

       
        self.play(Write(s))
        self.play(Write(t1))
        self.play(Create(arrow))
        self.play(Write(t2))
        self.wait(1)

        self.isRandom = False

        p4=cvo.CVO().CreateCVO("Side","a").setPosition([6,2,0])
        p5=cvo.CVO().CreateCVO("Area Formula","a*a").setPosition([2.5,2,0])
       
        p5.cvolist.append(p4)

        self.construct1(p5,p5)

        a1 = Text("Area Formula = a*a \n\n Example: a=4 \n\n Area of Square = 4*4 = 16",font_size=25).move_to([0,-2,0])
        self.play(Write(a1),run_time=6)
       

    def shape3(self):

        t1 =  Text("Rectangle",font="Comic Sans MS",color=LIGHT_PINK,weight=BOLD).move_to([-4,3,0])
        t2 = Text("l",color=WHITE).move_to([-6,0,0])
        t3 = Text("b",color=WHITE).move_to([-4,-3,0])
        r = Rectangle(color=BLUE, 
                   stroke_width = 10,
                   fill_opacity = 0.2,
                   fill_color = YELLOW,
                   width = 2.5,
                   height = 4).move_to(LEFT*4)
        
        arrow1 = DoubleArrow(color= ORANGE,start=[-5.5,2.25,0],end=[-5.5,-2.25,0])
        arrow2 = DoubleArrow(color=ORANGE,start=[-2.5,-2.25,0],end=[-5.5,-2.25,0])
    
        self.play(Write(r))
        self.play(Write(t1))
        self.play(Create(arrow1))
        self.play(Write(t2))
        self.play(Create(arrow2))
        self.play(Write(t3))
       
        self.wait(1)

        self.isRandom = False
   
        p2=cvo.CVO().CreateCVO("Area Formula", "l*b").setPosition([2.5,2,0])
        p3=cvo.CVO().CreateCVO("length","l").setPosition([6,2,0])
        p4=cvo.CVO().CreateCVO("breadth","b").setPosition([4,-0.5,0])
       
        p2.cvolist.append(p3)
        p2.cvolist.append(p4)
      
        self.construct1(p2,p2)

        a1 = Text("Area Formula = l*b \n\n Example: l=6, b=8 \n\n Area of Rectangle = 6*8 = 48",font_size=25).move_to([0,-2,0])
        self.play(Write(a1),run_time=6)

    

    def shape4(self):

        t1 = Text("Triangle",font="Comic Sans MS",color=LIGHT_PINK,weight=BOLD).move_to([-5,1.5,0])
        t2= Text("h",color=WHITE).move_to([-4.5,0.5,0])
        t3= Text("b",color=WHITE).move_to([-5,-1.5,0])
        tri = Triangle(color=BLUE, stroke_width = 10,fill_opacity = 0.2,fill_color = ORANGE,
        ).scale(1.2).move_to([LEFT*5])
        
        arrow1 = DoubleArrow(color=ORANGE,start=[-5,1,0],end=[-5,-1,0])
        arrow2 = DoubleArrow(color=ORANGE,start=[-6.25,-1.2,0],end=[-3.75,-1.2,0])

        self.play(Write(tri))
        self.play(Write(t1))
        self.play(Create(arrow1))
        self.play(Write(t2))
        self.play(Create(arrow2))
        self.play(Write(t3))

      
        self.wait(1)

        p2=cvo.CVO().CreateCVO("Area Formula", "1/2(b*h)").setPosition([2.5,2,0]).setangle(-TAU/4)
        p3=cvo.CVO().CreateCVO("base","b").setPosition([6,2,0])
        p4=cvo.CVO().CreateCVO("height","h").setPosition([4,-0.5,0])
        
        p2.cvolist.append(p3)
        p2.cvolist.append(p4)


        self.construct1(p2,p2)

        a1 = Text("Area Formula = 1/2(b*h) \n\n Example: b=8, h=8 \n\n Area of Triangle = 1/2(8*8) = 32",font_size=25).move_to([0,-2,0])
        self.play(Write(a1),run_time=6)
       

    def shape5(self):  
         
    
        t1 = Text("Parallelogram",font="Comic Sans MS",color=LIGHT_PINK,weight=BOLD)
        t2 = Text("b",color=WHITE)
        t3 = Text("h",color=WHITE)
        e = ((-6,2,0),(-3,1,0),(-3,-3,0),(-6,-2,0),(-6,2,0))
        e1 = Polygon(*e,color=BLUE,stroke_width=10)

        t1.move_to([-4,3,0])
        t2.move_to([-6.5,0,0])
        t3.move_to([-3.5,-1.25,0])
        arrow1 = DoubleArrow(color=ORANGE,start=[-6.25,2.25,0],end=[-6.25,-2.25,0])
        arrow2 = DoubleArrow(color=ORANGE,start=[-6.25,-1.75,0],end=[-2.75,-1.75,0])

       
        self.play(Create(e1))
        self.play(Write(t1))
        self.play(Create(arrow1))
        self.play(Write(t2))
        self.play(Create(arrow2))
        self.play(Write(t3))
        self.wait(1)

        p2=cvo.CVO().CreateCVO("Area Formula", "b*h").setPosition([2.5,2,0])
        p3=cvo.CVO().CreateCVO("base","b").setPosition([6,2,0])
        p4=cvo.CVO().CreateCVO("height","h").setPosition([4,-0.5,0])
       
        p2.cvolist.append(p3)
        p2.cvolist.append(p4)

        self.construct1(p2,p2)
        

        a1 = Text("Area Formula = b*h \n\n Example: b=8, h=8 \n\n Area of Parallelogram = 8*8 = 64",font_size=25).move_to([0,-2,0])
        self.play(Write(a1),run_time=6)


    def shape6(self):  
         
        
        t1 = Text("Rhombus",font="Comic Sans MS",color=LIGHT_PINK,weight=BOLD)
        t2 = Text("d1",color=WHITE)
        t3 = Text("d2",color=WHITE)
        e = ((-6,0,0),(-4.5,2,0),(-3,0,0),(-4.5,-2,0),(-6,0,0))
        e1 = Polygon(*e,color=BLUE,stroke_width=10)
        
        t1.move_to([-4.5,3,0])
        t2.move_to([-4.25,1,0])
        t3.move_to([-5.25,-0.25,0])
        arrow1 = DoubleArrow(color=ORANGE,start=[-4.5,2.25,0],end=[-4.5,-2.25,0])
        arrow2 = DoubleArrow(color=ORANGE,start=[-6.25,0,0],end=[-2.75,0,0])

        self.play(Create(e1))
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
        
        p2.cvolist.append(p3)
        p2.cvolist.append(p4)

        self.construct1(p2,p2)

        a1 = Text("Area Formula = 1/2(d1*d2) \n\n Example: d1=8, d2=6 \n\n Area of Rhombus = 1/2(8*6) = 24",font_size=25).move_to([0,-2,0])
        self.play(Write(a1),run_time=6)

    

    def shape7(self):  
         
        t1 = Text("Trapezium",font="Comic Sans MS",color=LIGHT_PINK,weight=BOLD)
        t2 = Text("a",color=WHITE)
        t3 = Text("b",color=WHITE)
        t4 = Text("h",color=WHITE)
        e = ((-5,1,0),(-3,1,0),(-2,-1,0),(-6,-1,0),(-5,1,0))
        e1 = Polygon(*e,color=BLUE,stroke_width=10)
    
        t1.move_to([-4,3,0])
        t2.move_to([-4,1.5,0])
        t3.move_to([-4,-2,0])
        t4.move_to([-4.75,0,0])
        arrow1 = DoubleArrow(color=ORANGE,start=[-2.75,1.25,0],end=[-5.25,1.25,0])
        arrow2 = DoubleArrow(color=ORANGE,start=[-1.75,-1.25,0],end=[-6.25,-1.25,0])
        arrow3 = DoubleArrow(color=ORANGE,start=[-5,1.25,0],end=[-5,-1.25,0])

        self.play(Create(e1))
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
        p2.cvolist.append(p3)
        p2.cvolist.append(p4)
        p2.cvolist.append(p5)
        self.construct1(p2,p2)

        a1 = Text("Area Formula = h*((a+b)/2) \n\n Example: a=8, b=8, h=4 \n\n Area of Trapezium = 4*((8+8)/2) = 24",font_size=25).move_to([1.3,-2,0])
        self.play(Write(a1),run_time=6)
        

    def quad(self):
        

        title = Text("Area of a Quadrilateral",font_size=45)
        title.move_to([-3,3.3,0])
        u = Underline(title)
        subtil = Text("A quadrilateral can be split into two"
                      "\n\ntriangles by drawing one of its diagonals",font_size=25)
        subtil.move_to([-2.5,2,0])
        self.play(Write(title))
        self.play(Write(u))
        self.play(Write(subtil))

        a = ((2.1,0.2,0),(5.1,0.6,0),(5.5,2.5,0),(2.5,2,0),(2,0.2,0),(5.5,2.5,0))
        ex1 = Polygon(*a,color=BLUE,stroke_width= 10)
        self.wait()

        s1= Text("A").move_to([1.5,0.2,0])
        s2= Text("B").move_to([2.1,2.1,0])
        s3= Text("C").move_to([5.8,2.5,0])
        s4= Text("D").move_to([5.5,0.6,0])

        dia = DoubleArrow(start=[1.8,0,0], end=[5.6,2.4,0],color=ORANGE)

        t1 = Text("d",color=RED,font_size=25).move_to([3.7,1.7,0])

        d1 = DashedLine(start=[2.5,2,0],end=[3.1,1,0],color=ORANGE)

        d2 = DashedLine(start=[5.1,0.6,0],end=[4.4,1.7,0],color=ORANGE)

        a1 = Text("h1",font_size=25,color=ORANGE).move_to([3,1.8,0])
        a2 = Text("h2",font_size=25,color=ORANGE).move_to([4.3,1,0])

        elements = VGroup(ex1, s1, s2, s3, s4, dia, t1, d1, d2, a1, a2)
        
        self.play(Write(ex1), Write(s1), Write(s2), Write(s3), Write(s4), Write(dia), Write(t1), Write(d1), Write(d2), Write(a1), Write(a2))
        self.wait()
        
        self.fadeOutCurrentScene()
        
        self.play(
            elements.animate.scale(0.8).to_corner(UR)
        )
        self.wait()

        are =  Text("Calculating the area of quadrilateral",font_size=40).move_to([-2.5,3,0])
        un = Underline(are)
        self.play(Write(are))
        self.play(Write(un))


        formula_steps = [
            MathTex(r"Area \ of \ the \ quadrilateral ABCD =  (Area \ of \ \triangle ABC) + (Area \ of \ \triangle ADC)", font_size=40, color=WHITE).shift(UP),
            
            MathTex(r"= ((\frac{1}{2} * AC * h1) + (\frac{1}{2} * AC * h2))",font_size=40,color=WHITE),
            MathTex(r"= \frac{1}{2} AC(h1 + h2)",font_size=40,color=WHITE).shift(DOWN),
            MathTex(r"Area \ of \ quadrilateral ABCD = \frac{1}{2} d(h1 + h2),",font_size=40,color=WHITE).shift(DOWN*2),
            MathTex(r"where \ 'd' \ denotes \ the \ length \ of \ the \ diagonal AC",font_size=40,color=WHITE).shift(DOWN*3)
        ]
         
        for step in formula_steps:
            self.play(Write(step))
            self.wait(2)



    def poly(self):

        title = Text("Area of a Polygon",font_size=45)
        title.move_to([-3,3.3,0])
        u = Underline(title)
        subtil = Text("The area of a polygon may be obtained by dividing\n\n"
                      "the polygon into a number of simple shapes \n\n"
                      "(triangles, rectangles etc.) Then the areas of \n\n"
                       "each of them can be calculated and added up \n\n"
                       "to get the required area.",font_size=25)
        subtil.move_to([-2.25,0.5,0])
        self.play(Write(title))
        self.play(Write(u))
        self.play(Write(subtil,run_time=6))

        a = ((4.6,3.3,0),(6.3,1.5,0),(5.6,-0.2,0),(4.6,-1.3,0),(2.3,0.5,0),(4.6,3.3,0))
        ex1 = Polygon(*a,color=BLUE,stroke_width= 10)
        self.wait()

        s1= Text("A",font_size=30).move_to([4.6,-1.6,0])
        s2= Text("B",font_size=30).move_to([5.9,-0.2,0])
        s3= Text("C",font_size=30).move_to([6.6,1.5,0])
        s4= Text("D",font_size=30).move_to([4.6,3.7,0])
        s5= Text("E",font_size=30).move_to([1.9,0.5,0])

        d1 = Line(start=[4.6,-1.3,0],end=[4.6,3.3,0],color=ORANGE,stroke_width= 10)

        d2 = Line(start=[6.3,1.5,0],end=[4.6,1.5,0],color=ORANGE,stroke_width= 10)

        d3 = Line(start=[5.6,-0.2,0],end=[4.6,-0.2,0],color=ORANGE,stroke_width= 10)

        d4 = Line(start=[2.3,0.5,0],end=[4.6,0.5,0],color=ORANGE,stroke_width= 10)

        s6= Text("F",font_size=30).move_to([4.2,1.5,0])
        s7= Text("G",font_size=30).move_to([4.8,0.5,0])
        s8= Text("H",font_size=30).move_to([4.3,-0.2,0])

        a1 = Text("50",font_size=25,color=ORANGE).move_to([4.4,2.3,0])
        a2 = Text("50",font_size=25,color=ORANGE).move_to([5.3,1.8,0])
        a3 = Text("60",font_size=25,color=ORANGE).move_to([3.5,0.7,0])
        a4 = Text("40",font_size=25,color=ORANGE).move_to([4.3,1,0])
        a5 = Text("15",font_size=25,color=ORANGE).move_to([4.3,0.2,0])
        a6 = Text("25",font_size=25,color=ORANGE).move_to([4.3,-0.7,0])
        a7 = Text("25",font_size=25,color=ORANGE).move_to([5.1,0,0])

        elements = VGroup(
            ex1, s1, s2, s3, s4, s5, d1, d2, d3, d4, 
            s6, s7, s8, a1, a2, a3, a4, a5, a6, a7
        )

        self.play(
            Write(ex1),
            Write(s1), Write(s2), Write(s3), Write(s4), Write(s5),
            Write(d1), Write(d2), Write(d3), Write(d4),
            Write(s6), Write(s7), Write(s8),
            Write(a1), Write(a2), Write(a3), Write(a4),
            Write(a5), Write(a6), Write(a7)
        )
        self.wait()


        self.fadeOutCurrentScene()

        self.play(
            elements.animate.scale(0.7).to_corner(UR)
        )
        self.wait()

        are =  Text("Calculating the area of given polygon",font_size=40).move_to([-2.3,3,0])
        un = Underline(are)
        self.play(Write(are))
        self.play(Write(un))


        formula_steps = [
            MathTex(r"Area \ of \ ABCDE = ", font_size=40, color=WHITE).shift(UP*2+LEFT*2.5),
            MathTex(r"Area \ of \ \triangle ABH + Area \ of \ trap \ BCFH", font_size=40, color=WHITE).shift(UP*1.5+LEFT*1.5),
            MathTex(r"+ Area \ of \ \triangle CDF + Area \ of \ \triangle AED", font_size=40, color=WHITE).shift(UP+LEFT*1.5),
            MathTex(r"Now, Area \ of \ \triangle ABH",font_size=40,color=WHITE).shift(LEFT*3),
            MathTex(r"= \frac{1}{2}*AH*HB",font_size=40,color=WHITE).shift(DOWN),
            MathTex(r"=\frac{1}{2}*25*25",font_size=40,color=WHITE).shift(DOWN*2),
            MathTex(r"=\frac{652}{2} \ m^2 = 312.5 \ m^2",font_size=40,color=WHITE).shift(DOWN*3)
        ]
         
        for step in formula_steps:
            self.play(Write(step))
            self.wait(2)

        self.fadeOutCurrentScene()   

        self.play(
            elements.animate.scale(0.9).to_corner(UR)
        )
        self.wait() 

        
        formula_steps = [
            MathTex(r"Area \ of \ trap \ BCFH =\ \frac{1}{2}*(HB + FC)*HF ", font_size=40, color=WHITE).shift(UP*3 + LEFT*2.5),
            MathTex(r"=\ \frac{1}{2}*(25 + 50)*55 \ m^2 ", font_size=40, color=WHITE).shift(UP*2),
            MathTex(r"=\ \frac{75*55}{2} \ m^2\ =2062.5\ m^2",font_size=40,color=WHITE).shift(UP),
            MathTex(r"Area \ of \ \triangle CDF =\ \frac{1}{2}*FC*DF",font_size=40,color=WHITE).shift(DOWN + LEFT*2.5),
            MathTex(r"=\ \frac{1}{2}*50*50\ m^2 ",font_size=40,color=WHITE).shift(DOWN*2),
            MathTex(r"=1250\ m^2",font_size=40,color=WHITE).shift(DOWN*3)
        ]
         
        for step in formula_steps:
            self.play(Write(step))
            self.wait(2)


        self.fadeOutCurrentScene()  

        self.play(
            elements.animate.scale(1).to_corner(UR)
        )
        self.wait()  
  
        formula_steps = [
            MathTex(r"Area \ of \ \triangle AED =\ \frac{1}{2}*AD*EG", font_size=40, color=WHITE).shift(UP*3 + LEFT*2.5),
            MathTex(r"=\ \frac{1}{2}*130*60\ m^2", font_size=40, color=WHITE).shift(UP*2),
            MathTex(r"=3900\ m^2",font_size=40,color=WHITE).shift(UP),
            MathTex(r"Thus,\ area\ of\ ABCDE ",font_size=40,color=WHITE).shift(DOWN + LEFT*2.5),
            MathTex(r"=312.5\ m^2 +2062.5\ m^2 + 1250\ m^2 + 3900\ m^2 ",font_size=40,color=WHITE).shift(DOWN*2),
            MathTex(r"=7525\ m^2",font_size=40,color=WHITE).shift(DOWN*3)
        ]
         
        for step in formula_steps:
            self.play(Write(step))
            self.wait(2)    


    def cirpath(self):
        

        title = Text("Area of a Circular Path or Ring",font_size=45).move_to([-2.7,3.3,0])
        u = Underline(title)
        subtil = Text("The Area of the circular path is the difference\n\n"
                      "of Area of outer circle and inner circle.",font_size=28).move_to([-2.25,2,0])
        self.play(Write(title))
        self.play(Write(u))
        self.play(Write(subtil,run_time=6))

        c1 = Circle(radius=2, color=GREEN, fill_color=GREEN, fill_opacity=0.6).move_to([4,-1.5,0])
        c2 = Circle(radius=1, color=GREEN, fill_color=BLACK, fill_opacity=1).move_to([4,-1.5,0])

        r1 = Line(start=[4,-1.5,0], end=[4,0.5,0], color=WHITE)
        t1 = Text("R", font_size=28).move_to([3.6,0,0])

        r2 = Line(start=[4,-1.5,0], end=[5,-1.5,0], color=WHITE)
        t2 = Text("r", font_size=28).move_to([4.5,-1.2,0])
        
        elements = VGroup(c1, c2, r1, t1, r2, t2)
        
        self.play(Write(c1),Write(c2),Write(r1),Write(t1),Write(r2),Write(t2))
        self.wait()


        self.fadeOutCurrentScene() 


        are =  Text("Calculating the area of circular path",font_size=40).move_to([-2.3,3,0])
        un = Underline(are)
        self.play(Write(are))
        self.play(Write(un))

        formula_steps = [
            MathTex(r"Area \ of \ circular \ path \ where,\ R=10cm, \ r=4cm.", font_size=40, color=WHITE).shift(UP*1.5),
            MathTex(r"(i) Find\ the\ area\ of\ larger\ circle\ with\ radius\ R", font_size=40, color=WHITE).shift(UP),
            MathTex(r"(ii) Find\ the\ area\ of\ smaller\ circle\ with\ radius\ r",font_size=40,color=WHITE),
            MathTex(r"(iii) Find\ the\ area\ of\ circular\ path\ (where\ \pi =3.14)",font_size=40,color=WHITE).shift(DOWN),           
        ]
         
        for step in formula_steps:
            self.play(Write(step))
            self.wait(2)

        self.fadeOutCurrentScene()

        self.play(
            elements.animate.scale(0.7).to_corner(UR)
        )
        self.wait()
        
        formula_steps = [
            MathTex(r"Radius\ of\ the\ larger\ circle\ =\ 10cm", font_size=40, color=WHITE).shift(UP*3 + LEFT*2.5),
            MathTex(r"So,area\ of\ the\ larger\ circle=\ \pi R^2", font_size=40, color=WHITE).shift(UP*2),
            MathTex(r"=3.14*10*10\ =\ 314cm^2",font_size=40,color=WHITE).shift(UP),
            MathTex(r"Radius\ of\ the\ smaller\ circle\ =\ 4cm",font_size=40,color=WHITE).shift(DOWN + LEFT*2.5),
            MathTex(r"So,area\ of\ the\ smaller\ circle=\ \pi r^2",font_size=40,color=WHITE).shift(DOWN*2),
            MathTex(r"=3.14*4*4\ =\ 50.24cm^2",font_size=40,color=WHITE).shift(DOWN*3)
        ]
         
        for step in formula_steps:
            self.play(Write(step))
            self.wait(2)  

        self.fadeOutCurrentScene()

        self.play(
            elements.animate.scale(0.8).to_corner(UR)
        )
        self.wait()
        
        formula_steps = [
            MathTex(r"Area\ of\ the\ circular\ path\ =\ ", font_size=40, color=WHITE).shift(UP*3 + LEFT*2.5),
            MathTex(r"Area\ of\ the\ larger\ circle-\ Area\ of\ the\ smaller\ circle", font_size=40, color=WHITE).shift(UP*2 + LEFT),
            MathTex(r"=(314\ -\ 50.24)cm^2",font_size=40,color=WHITE).shift(UP),
            MathTex(r"=\ 263.76cm^2",font_size=40,color=WHITE),
        ]
        for step in formula_steps:
            self.play(Write(step))
            self.wait(2)        

 
    def sector(self):


        title = Text("Area of Sector",font_size=45).move_to([-3.5,3.3,0])
        u = Underline(title)
        subtil = Text("A part of a circle bounded by two radii\n\n" 
                      "and an arc is called sector.\n\n",font_size=28).move_to([-2.25,2,0])
        self.play(Write(title))
        self.play(Write(u))
        self.play(Write(subtil,run_time=6))
        
        c1 = Circle(radius=2, color=WHITE).move_to([4,1,0])
        
        r1 = Line(start=[4,1,0], end=[3,-0.7,0], color=RED)
        t1 = Text("r", font_size=28).move_to([3.2,0,0])
        r2 = Line(start=[4,1,0], end=[5,-0.7,0], color=RED)
        t2 = Text("r", font_size=28).move_to([4.8,0,0])
        t3 = Text("O", font_size=28).move_to([4,1.3,0])
       
        p0 = [3,-0.7,0]
        p00 = [5,-0.7,0]
        a0 = ArcBetweenPoints(p0, p00, color=RED, radius=2)
        
        p1 = [3,-1,0]
        p2 = [5,-1,0]
        a1 = ArcBetweenPoints(p1, p2, radius=2)
        t4 = Text("A", font_size=28).move_to([2.8,-1,0])
        t5 = Text("B", font_size=28).move_to([5.2,-1,0])
        t6 = Text("l", font_size=28).move_to([4,-2,0])
        
        p3 = [3.8,0.7,0]
        p4 = [4.2,0.7,0]
        a2 = ArcBetweenPoints(p3, p4)
        tt = MathTex(r"x^\circ", font_size=30).move_to([4,0.3,0])
        
        elements = VGroup(c1, r1, t1, r2, t2, t3, a0, a1, t4, t5, t6, a2, tt)
        
        self.play(Write(c1),Write(r1),Write(t1),Write(r2),Write(t2),Write(t3),Write(a0),Write(a1),Write(t4),Write(t5),Write(t6),Write(a2),Write(tt))
        self.wait()

        self.fadeOutCurrentScene()

        self.play(
            elements.animate.scale(0.8).to_corner(UR)
        )
        self.wait()

        formula_steps = [
            MathTex(r"\small The\ Area\ of\ a\ circle\ with\ radius\ r = \pi r^2", font_size=40, color=WHITE).shift(UP*2.2+LEFT*1.5),
            MathTex(r"\\ \small Angle\ subtended\ by\ the\ arc\ of\ the\ sector", font_size=40, color=WHITE).shift(UP*1.2+LEFT*1.5),
            MathTex(r"at\ centre\ of\ the\ circle\ is\ x^\circ",font_size=40,color=WHITE).shift(UP*0.8+LEFT*1.5),
            MathTex(r"Area\ of\ a\ sector\ and\ its\ angle\ are\ in\ direct\ proportion",font_size=40,color=WHITE).shift(LEFT*1.5),
            MathTex(r"Area\ of\ sector\ :\ Area\ of\ circle = x^\circ\ :\ 360^\circ",font_size=40,color=WHITE).shift(DOWN+LEFT*1.5),           
            MathTex(r"Area\ of\ sector\ OAB\ = \frac{x^\circ}{360^\circ}*Area\ of\ the\ circle",font_size=40,color=WHITE).shift(DOWN*2+LEFT*1.5),           
        ]
         
        for step in formula_steps:
            self.play(Write(step))
            self.wait(2)

        self.fadeOutCurrentScene()

        self.play(
            elements.animate.scale(0.9).to_corner(DR)
        )
        self.wait()

        formula_steps = [
            MathTex(r"Hence,\ Area\ of\ sector\ OAB = \frac{x^\circ}{360^\circ}* \pi r^2\ \ \ \ \ [\pi r^2 = \pi r *\frac{2r}{2}] ", font_size=40, color=WHITE).shift(UP*3 + LEFT*1.2),
            MathTex(r"= \frac{x^\circ}{360^\circ}*2 \pi r * \frac{r}{2}", font_size=40, color=WHITE).shift(UP*2),
            MathTex(r"=l *\frac{r}{2}",font_size=40,color=WHITE).shift(UP),
            MathTex(r"=\frac{lr}{2} \ \ \ [l\ is\ length\ of\ the\ arc]",font_size=40,color=WHITE),     
        ]
         
        for step in formula_steps:
            self.play(Write(step))
            self.wait(2)



    def shaded(self):


        square_side_length = 2
        square = Square(side_length=square_side_length, color=WHITE, fill_color=BLUE, fill_opacity=0.5).move_to([4.5,2.5,0])
        circle_radius = square_side_length / 2  
        circle = Circle(radius=circle_radius, color=WHITE, fill_color=BLACK, fill_opacity=1).move_to(square.get_center())

        self.play(Create(square),Create(circle))
        self.wait(1)

        g1 = DoubleArrow(buff=2).next_to(square, DOWN)
        t1 = Text("21m", font_size=24).next_to(g1, DOWN)
        g2 = DoubleArrow(buff=2).next_to(square, LEFT, buff=0).rotate(PI/2)
        t2 = Text("21m", font_size=24).next_to(g2, LEFT, buff=0)

        elements = VGroup(square, circle, g1, t1, g2, t2)

        self.play(Create(g1), Write(t1))
        self.play(Create(g2), Write(t2))
        self.wait()

       
        title = Text("Find the area of the shaded region",font_size=33).move_to([-3.5,2.8,0])
        self.play(Write(title))


        formula_steps = [
            MathTex(r"Area \ of \ the\ shaded\ region =", font_size=40, color=WHITE).shift(UP+LEFT*2.5),
            MathTex(r"{Area \ of \ square\ with\ side\ 21m} - {Area \ of \ the\ circle\ with\ diameter\ 21m}", font_size=40, color=WHITE),
            MathTex(r"If\ the\ diameter\ of\ the\ circle\ is\ 21m\ \\ Then\ the\ radius\ of\ the\ circle\ is\ \frac{21}{2} = 10.5m", font_size=40, color=WHITE).shift(DOWN*2),
            ]
         
        for step in formula_steps:
            self.play(Write(step))
            self.wait(2)


        self.fadeOutCurrentScene()

        self.play(
            elements.animate.scale(1).to_corner(DR)
        )
        self.wait()

        formula_steps = [
            MathTex(r"Area\ of\ the\ shaded\ region\ = (21*21)-(\frac{22}{7}*\frac{21}{2}*\frac{21}{2})*m^2",font_size=40,color=WHITE).shift(UP*2),
            MathTex(r"= 441 - 346.5",font_size=40,color=WHITE).shift(UP),
            MathTex(r"= 94.5 m^2",font_size=40,color=WHITE),
        ]
         
        for step in formula_steps:
            self.play(Write(step))
            self.wait(2)
            
 


if __name__ == "__main__":
    scene = Grade8Chapter9PlanefiguresAreasAnim()
    scene.render()