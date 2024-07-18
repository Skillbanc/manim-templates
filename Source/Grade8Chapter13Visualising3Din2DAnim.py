import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class Grade8Chapter13Visualising3Din2DAnim(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.intro()
        self.fadeOutCurrentScene()
        self.layers()
        self.fadeOutCurrentScene()
        self.positions()
        self.fadeOutCurrentScene()
        self.views()
        self.fadeOutCurrentScene()
        self.iso1()
        self.fadeOutCurrentScene()
        self.objects()
        self.fadeOutCurrentScene()
        self.surfaces()
        self.fadeOutCurrentScene()
        self.regpoly()
        self.fadeOutCurrentScene()
        self.regpoly()



    def intro(self):

        self.angleChoice = [(TAU/4),(TAU/4),(-TAU/4),(-TAU/4)]
         
        p1=cvo.CVO().CreateCVO("Visualising 3-D in 2-D","").setPosition([0,2.2,0])
        p2=cvo.CVO().CreateCVO("2-D Shapes","").setPosition([-5,0.5,0])
        p3=cvo.CVO().CreateCVO("3-D Shapes","").setPosition([5,0.5,0])

        p4=cvo.CVO().CreateCVO("Two Measurements","length , breadth").setPosition([-2.6,-2.2,0])
        
        p5=cvo.CVO().CreateCVO("Three Measurements","length, breadth, height").setPosition([2.6,-2.2,0])

        p1.cvolist.append(p2)
        p1.cvolist.append(p3)
        p2.cvolist.append(p4)
        p3.cvolist.append(p5)

        p4.setcircleradius(1.2)
        p5.setcircleradius(1.2)
        self.construct1(p1,p1)

        self.fadeOutCurrentScene()

        
    def layers(self):
        t1 = Text("Triangle, Square, Rectangle are plane figures\n\n"
                  "of 2-dimensions. While, a cube and cuboid are\n\n"
                  "solid objects with 3-dimensions. By arranging\n\n"
                  "2-D objects one above another it occupies some\n\n" 
                  "space and becomes a 3-D. It has volume also.",font_size=28).move_to([-2,1.5,0])
        self.play(Write(t1))

        a = ((5.5,-1.75,0),(3.75,-1.75,0),(2,-2.25,0),(3.75,-2.25,0),(5.5,-1.75,0))
        base = Polygon(*a,color="#6DC9CD",fill_opacity=0.5,stroke_width=5).move_to([-4.5,-2,0])
        n1 = Text("(1)",font_size=22).move_to([-4.5,-3,0])
        self.play(Create(base),Write(n1))

        ar1 = Arrow(start=[-4,-3,0],end=[-1,-3,0])
        self.play(Write(ar1))

        a1 = ((5.5,-1.75,0),(3.75,-1.75,0),(2,-2.25,0),(3.75,-2.25,0),(5.5,-1.75,0))
        spacing = 0.08
        for i in range(10):  
            base1 = Polygon(*a1, color="#6DC9CD", fill_opacity=0.5, stroke_width=5).move_to([-0.5,-2,0])
            base1.shift(UP * i * spacing) 
            n2 = Text("(2)",font_size=22).move_to([-0.5,-3,0])
            self.play(Create(base1),Write(n2))
            

        ar2 = Arrow(start=[0,-3,0],end=[3.25,-3,0])
        self.play(Write(ar2))

        a2 = ((5.4,-1.75,0),(3.75,-1.75,0),(2.1,-2.25,0),(3.75,-2.25,0),(5.4,-1.75,0))
        base_face = Polygon(*a2, color=BLUE, fill_opacity=0.5, stroke_width=5)
        self.play(Create(base_face))

        c = ((5.5,-1,0),(5.5, -1.75, 0),(3.75, -2.25, 0),(3.75, -1.5, 0),(5.5,-1,0))
        face1 = Polygon(*c,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)
        self.play(Create(face1))


        d = ((5.5,-1,0),(3.75, -1, 0),(3.75, -1.75, 0),(5.5, -1.75, 0),(5.5,-1,0))
        face2 = Polygon(*d,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)
        self.play(Create(face2))


        e = ((3.75, -1, 0),(3.75, -1.75, 0),(2, -2.25, 0),(2, -1.5, 0),(3.75, -1, 0))
        face3 = Polygon(*e,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)
        self.play(Create(face3))

 
        f = ((2, -2.25, 0),(3.75, -2.25, 0),(3.75, -1.5, 0),(2, -1.5, 0),(2, -2.25, 0))
        face4 = Polygon(*f,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)
        self.play(Create(face4))

        b1 = ((5.4,-1,0), (3.75, -1.5, 0),(2.1, -1.5, 0),(3.75, -1, 0),(5.5,-1,0))
        top_face = Polygon(*b1, color=BLUE, fill_opacity=0.5, stroke_width=5)
        self.play(Create(top_face))

        n3 = Text("(3)",font_size=22).move_to([3.75,-3,0])
        self.play(Write(n3))

    def positions(self):
        
        
        t1 = Text("If we observe a 3-D object from different positions,\n\n"
                  "it seems to be different. But the object is same.",font_size=28).move_to([-2,2.5,0])
        self.play(Write(t1))
        
        polygons = [
            ((-5, -0.75, 0), (-5, 0, 0), (-4.25, 0, 0), (-4.25, -0.75, 0), (-5, -0.75, 0)),
            ((-4.5, 0.25, 0), (-5, 0, 0), (-4.25, 0, 0), (-3.75, 0.25, 0), (-4.5, 0.25, 0)),
            ((-4.25, 0, 0), (-4.25, -0.75, 0), (-3.75, -0.5, 0), (-3.75, 0.25, 0), (-4.25, 0, 0)),
            ((-5, -1.5, 0), (-5, -0.75, 0), (-4.25, -0.75, 0), (-4.25, -1.5, 0), (-5, -1.5, 0)),
            ((-4.25, -0.75, 0), (-4.25, -1.5, 0), (-3.75, -1.25, 0), (-3.75, -0.5, 0), (-4.25, -0.75, 0)),
            ((-3.75, 0.25, 0), (-3.75, -0.5, 0), (-3.25, -0.25, 0), (-3.25, 0.5, 0), (-3.75, 0.25, 0)),
            ((-4.5, 0.25, 0), (-4.5, 1, 0), (-3.75, 1, 0), (-3.75, 0.25, 0), (-4.5, 0.25, 0)),
            ((-4, 1.25, 0), (-4.5, 1, 0), (-3.75, 1, 0), (-3.25, 1.25, 0), (-4, 1.25, 0)),
            ((-3.75, 0.75, 0), (-3.75, 0.25, 0), (-3.25, 0.5, 0), (-3.25, 1.25, 0), (-3.75, 1, 0))
        ]
        
        colors = ["#6DC9CD", "RED", "#6DC9CD", "#6DC9CD", "#6DC9CD", "#6DC9CD", "#6DC9CD", "RED", "#6DC9CD"]
        
        animations = []
        for vertices, color in zip(polygons, colors):
            polygon = Polygon(*vertices, color=WHITE, fill_color=color, fill_opacity=1, stroke_width=2)
            animations.append(Create(polygon, lag_ratio=0))
        
        self.play(*animations)
        
        s2 = Text("Front view", font_size=27).move_to([-2.5, -0.75, 0])
        self.play(Write(s2, lag_ratio=0.5))
        
        self.wait()


        polygons = [
            ((-5.25,-2.75,0),(-5.25,-2,0),(-4.5,-2,0),(-4.5,-2.75,0),(-5.25,-2.75,0)),
            ((-4.5,-2.75,0),(-4.5,-2,0),(-3.75,-2,0),(-3.75,-2.75,0),(-4.5,-2.75,0)),
            ((-4.75,-1.75,0),(-5.25,-2,0),(-4.5,-2,0),(-4,-1.75,0),(-4.75,-1.75,0)),
            ((-4,-1.75,0),(-4.5,-2,0),(-3.75,-2,0),(-3.25,-1.75,0),(-4,-1.75,0)),
            ((-3.75,-2,0),(-3.75,-2.75,0),(-3.25,-2.5,0),(-3.25,-1.75,0),(-3.75,-2,0)),
            ((-6.5,-3,0),(-6.5,-2.25,0),(-5.75,-2.25,0),(-5.75,-3,0),(-6.5,-3,0)),
            ((-5.75,-3,0),(-5.75,-2.25,0),(-5,-2.25,0),(-5,-3,0),(-5.75,-3,0)),
            ((-6.49,-2.25,0),(-6,-2,0),(-5.25,-2,0),(-5.75,-2.25,0),(-6.5,-2.25,0)),
            ((-5.25,-2,0),(-5.75,-2.25,0),(-5,-2.25,0),(-4.5,-2,0),(-5.25,-2,0)),
             ((-5,-2.25,0),(-5,-3,0),(-4.5,-2.75,0),(-4.5,-2,0),(-5,-2.25,0))            
            ]
        
        colors = ["#6DC9CD", "#6DC9CD", "#6DC9CD", "#6DC9CD", RED, "#6DC9CD", "#6DC9CD", "#6DC9CD", "#6DC9CD", RED]


        animations = []
        for vertices, color in zip(polygons, colors):
            polygon = Polygon(*vertices, color=WHITE, fill_color=color, fill_opacity=1, stroke_width=2)
            animations.append(Create(polygon, lag_ratio=0))
        
        self.play(*animations)
        
        s2 = Text("Side view", font_size=27).move_to([-4,-3.25,0])
        self.play(Write(s2, lag_ratio=0.5))
        
        self.wait()

        p11=cvo.CVO().CreateCVO("Different Positions","").setPosition([3.5,0.5,0])
        p12=cvo.CVO().CreateCVO("Top View","").setPosition([5,-1.5,0])
        p13=cvo.CVO().CreateCVO("Front View","").setPosition([2.5,-2.3,0])
        p14=cvo.CVO().CreateCVO("Side View","").setPosition([0,-2,0])

        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
        p11.cvolist.append(p14)  
        
        self.construct1(p11,p11)

    def views(self):

        polygons = [
            ((-5,-3,0),(-5,-2.25,0),(-4.25,-2.25,0),(-4.25,-3,0),(-5,-3,0)),
            ((-5.75,-3,0),(-5.75,-2.25,0),(-5,-2.25,0),(-5,-3,0),(-5.75,-3,0)),
            ((-5.75,-2.25,0),(-5.25,-2,0),(-4.5,-2,0),(-5,-2.25,0),(-5.75,-2.25,0)),
            ((-4.5,-2,0),(-5,-2.25,0),(-4.25,-2.25,0),(-3.75,-2,0),(-4.5,-2,0)),
            ((-4.25,-2.25,0),(-4.25,-3,0),(-3.75,-2.75,0),(-3.75,-2,0),(-4.25,-2.25,0)),
            ((-4.75,-1.75,0),(-5.25,-2,0),(-4.5,-2,0),(-4,-1.75,0),(-4.75,-1.75,0)),
            ((-4,-1.75,0),(-4.5,-2,0),(-3.75,-2,0),(-3.25,-1.75,0),(-4,-1.75,0)),
            ((-3.75,-2,0),(-3.75,-2.75,0),(-3.25,-2.5,0),(-3.25,-1.75,0),(-3.75,-2,0)),
            ((-4.25,-1.5,0),(-4.75,-1.75,0),(-4,-1.75,0),(-3.5,-1.5,0),(-4.25,-1.5,0)),
            ((-3.5,-1.5,0),(-4,-1.75,0),(-3.25,-1.75,0),(-2.75,-1.5,0),(-3.5,-1.5,0)),
            ((-3.25,-1.75,0),(-3.25,-2.5,0),(-2.75,-2.25,0),(-2.75,-1.5,0),(-3.25,-1.75,0)),
            ((-4.25,-0.75,0),(-4.75,-1,0),(-4,-1,0),(-3.5,-0.75,0),(-4.25,-0.75,0)),
            ((-4.75,-1.75,0),(-4.75,-1,0),(-4,-1,0),(-4,-1.75,0),(-4.75,-1.75,0)),
            ((-4,-1,0),(-4,-1.75,0),(-3.5,-1.5,0),(-3.5,-0.75,0),(-4,-1,0))
            ]
        
        colors = [LOGO_GREEN,LOGO_GREEN,LOGO_BLUE, LOGO_BLUE,LOGO_RED, LOGO_BLUE,LOGO_BLUE, LOGO_RED, LOGO_BLUE, LOGO_BLUE, LOGO_RED,LOGO_BLUE, LOGO_GREEN, LOGO_RED]


        animations = []
        for vertices, color in zip(polygons, colors):
            polygon = Polygon(*vertices, color=LOGO_WHITE, fill_color=color, fill_opacity=1, stroke_width=2).shift(UP*2)
            animations.append(Create(polygon, lag_ratio=0))
        self.play(*animations)

        t1 = Text("Top View",font_size=26).move_to([-3.7,2,0])
        a1 = Arrow(start=[-3.7,2,0],end=[-4,1,0])
        self.play(Write(t1),Create(a1))

        t2 = Text("Front View",font_size=26).move_to([-5,-2,0])
        a2 = Arrow(end=[-5,-1,0],start=[-5,-2,0])
        self.play(Write(t2),Create(a2))

        t3 = Text("Side View",font_size=26).move_to([-2.7,-1.3,0])
        a3 = Arrow(end=[-3.5,-0.5,0],start=[-2.7,-1.3,0])
        self.play(Write(t3),Create(a3))

        s1 = Square(fill_color=LOGO_GREEN, side_length=0.75,color=LOGO_WHITE, fill_opacity=1,stroke_width=2).move_to([-1, 1, 0])
        s2 = Square(fill_color=LOGO_GREEN, side_length=0.75,color=LOGO_WHITE, fill_opacity=1,stroke_width=2).move_to([-1, 1.75, 0])
        s3 = Square(fill_color=LOGO_GREEN, side_length=0.75,color=LOGO_WHITE, fill_opacity=1,stroke_width=2).move_to([-0.25, 1, 0])
        t10 = Text("Front Position",font_size=24).move_to([-0.5,0.2,0])
        self.add(s1,s2,s3)
        self.wait(1)
        self.add(t10)
        self.wait(2)

        s11 = Square(fill_color=LOGO_RED, side_length=0.75,color=LOGO_WHITE, fill_opacity=1,stroke_width=2).move_to([1.5, -1.25, 0])
        s21 = Square(fill_color=LOGO_RED, side_length=0.75,color=LOGO_WHITE, fill_opacity=1,stroke_width=2).move_to([2.25, -1.25, 0])
        s31 = Square(fill_color=LOGO_RED, side_length=0.75,color=LOGO_WHITE, fill_opacity=1,stroke_width=2).move_to([3, -1.25, 0])
        s41 = Square(fill_color=LOGO_RED, side_length=0.75,color=LOGO_WHITE, fill_opacity=1,stroke_width=2).move_to([3, -0.5, 0])
        t11 = Text("Side Position",font_size=24).move_to([2.3,-2.2,0])
        self.add(s11,s21,s31,s41)
        self.wait(1)
        self.add(t11)
        self.wait(2)
        
        i3 = [4.5, 0, 0]  
        s3 = 0.75  
        for i in range(2):  
            for j in range(3):  
            
                x = i3[0] + j * s3
                y = i3[1] + i * s3

                square3 = Square(fill_color=LOGO_BLUE, side_length=0.75,color=LOGO_WHITE, fill_opacity=1,stroke_width=2).move_to([x, y, 0])
                self.add(square3)
        self.wait(1)
        t12 = Text("Top View",font_size=24).move_to([5.3,-1,0])
        self.play(Write(t12))

    def iso1(self):

        t = Text("When 3-D figures are drawn on the paper, we are only able\n\n"
                 "to represent only two dimensions. All edges of the cube are\n\n"
                 "equal length. But in the adjacent figure they are not equal.\n\n"
                 "It has been drawn according to our view.",font_size=27).move_to([0,2.4,0])
        
        self.play(Write(t),run_time=10)


        a = ((6,-0.75,0),(4.25,-0.75,0),(3,-1.25,0),(4.75,-1.25,0),(6,-0.75,0))
        base = Polygon(*a,color="#6A53C6",fill_opacity=0.2,stroke_width=5)
        self.play(Write(base))
       

        b = ((6,0.5,0),(4.25,0.5,0),(3,0,0),(4.75,0,0),(6,0.5,0))
        top = Polygon(*b,color="#6A53C6",fill_opacity=0.2,stroke_width=5)
        self.play(Write(top))


        c = ((6.1,0.5,0),(6.1,-0.75,0),(4.75,-1.25,0),(4.75,0,0),(6,0.5,0))
        face1 = Polygon(*c,color="#6A53C6",fill_opacity=0.2,stroke_width=5)
        self.play(Write(face1))


        d = ((6,0.5,0),(4.25,0.5,0),(4.25,-0.75,0),(6.1,-0.75,0),(6.1,0.5,0))
        face2 = Polygon(*d,color="#6A53C6",fill_opacity=0.2,stroke_width=5)
        self.play(Write(face2))


        e = ((4.25,0.5,0),(4.25,-0.75,0),(2.9,-1.25,0),(2.9,0,0),(4.25,0.5,0))
        face3 = Polygon(*e,color="#6A53C6",fill_opacity=0.2,stroke_width=5)
        self.play(Write(face3))

 
        f = ((4.75,0,0),(4.75,-1.25,0),(2.9,-1.25,0),(2.9,0,0),(4.75,0,0))
        face4 = Polygon(*f,color="#6A53C6",fill_opacity=0.2,stroke_width=5)
        self.play(Write(face4))

        self.fadeOutCurrentScene()

        t= Text("Find the measurements of cuboid in the adjacent figure.\n\n"
                "Considering the distance between every two consecutive dots to be 1 unit.\n\n"
                "Also draw a side view, front view and top view",font_size=28).move_to([0,2.4,0])
        
        self.play(Write(t))

        rows = 20
        cols = 8
        dot_radius = 0.05
        horizontal_spacing = 0.8
        vertical_spacing = horizontal_spacing * np.sqrt(3) / 6
        dots = VGroup()
        for row in range(rows):
            for col in range(cols):
                x = col * horizontal_spacing + (row % 2) * (horizontal_spacing / 2)
                y = row * vertical_spacing
                dot = Dot(radius=dot_radius).move_to([x, y, 0])
                dots.add(dot)
        dots.move_to([3,-1.3,0])
        self.play(FadeIn(dots, lag_ratio=0.1))

        p = ((3.6,0.5,0),(1.6,-0.7,0),(1.6,-2.1,0),(2.4,-2.6,0),(4.4,-1.4,0),(4.4,0,0),(3.6,0.5,0))
        p1 = Polygon(*p,color=PURPLE,stroke_width=8)
        self.play(Write(p1))

        p = ((2.4,-1.2,0),(1.6,-0.7,0),(2.4,-1.2,0),(2.4,-2.6,0),(2.4,-1.2,0),(4.4,0,0),(2.4,-1.2,0))
        p1 = Polygon(*p,color=PURPLE,stroke_width=8)
        self.play(Write(p1))
        self.wait(2)

        formula_steps = [
            Tex("Length of the cuboid  = 5 units",font_size=32,color=BLUE).move_to([-4,0.5,0]),
            Tex("Breadth of the cuboid = 2 units",font_size=32,color=BLUE).move_to([-4,0,0]),
            Tex("Height of the cuboid  = 3 units",font_size=32,color=BLUE).move_to([-4,-0.5,0]),
        ]
        for step in formula_steps:
            self.play(Write(step))
            self.wait() 

        sv = Rectangle(height=1.3,width=2.2).move_to([-5.5,-2.5,0])
        st = Text("Side View",font_size=20).move_to([-5.5,-1.2,0])
        self.play(Create(sv),Write(st))

        fv = Rectangle(height=1.3,width=0.82).move_to([-3.5,-2.5,0])
        ft = Text("Front View",font_size=20).move_to([-3.5,-1.2,0])
        self.play(Create(fv),Write(ft))

        tv = Rectangle(height=1,width=2).move_to([-1.5,-2.5,0])
        tt = Text("Top View",font_size=20).move_to([-1.5,-1.2,0])
        self.play(Create(tv),Write(tt))

    def objects(self):

        self.angleChoice = [(TAU/4),(-TAU/4)]

        p11=cvo.CVO().CreateCVO("3-D Objects","").setPosition([0,2.5,0])
        p12=cvo.CVO().CreateCVO("Polyhedra","Objects that don't have curved surfaces").setPosition([-3,-1.5,0])
        p13=cvo.CVO().CreateCVO("Non-Polyhedra","Objects that have curved surfaces").setPosition([3.5,-1.5,0])
        

        p11.cvolist.append(p12)
        p11.cvolist.append(p13)  
        
        self.construct1(p11,p11)  

        self.fadeOutCurrentScene()

        pt = Text("Polyhedra",font_size=30).move_to([-4,2.8,0])
        u = Underline(pt)
        spt = Text("have only flat surfaces\n\n no curved surfaces",font_size=25).move_to([-3.8,1.5,0])
        self.play(Write(pt),Write(spt),Write(u))

        polygons = [
            ((-5,-3,0),(-5,-2.25,0),(-4.25,-2.25,0),(-4.25,-3,0),(-5,-3,0)),
            ((-4.5,-2,0),(-5,-2.25,0),(-4.25,-2.25,0),(-3.75,-2,0),(-4.5,-2,0)),
            ((-4.25,-2.25,0),(-4.25,-3,0),(-3.75,-2.75,0),(-3.75,-2,0),(-4.25,-2.25,0))
            ]
        colors = [LOGO_GREEN,LOGO_GREEN,LOGO_BLUE, LOGO_BLUE,LOGO_RED, LOGO_BLUE,LOGO_BLUE, LOGO_RED, LOGO_BLUE, LOGO_BLUE, LOGO_RED,LOGO_BLUE, LOGO_GREEN, LOGO_RED]

        animations = []
        for vertices, color in zip(polygons,colors):
            polygon = Polygon(*vertices, color=LOGO_WHITE, fill_color=color, fill_opacity=1, stroke_width=2).shift(UP*2)
            animations.append(Create(polygon, lag_ratio=0))
        self.play(*animations)


        polygons1 = [
            ((-3,-1,0),(-2.2,-1,0),(-2.6,-0.2,0),(-3,-1,0)),
            ((-2.6,-0.2,0),(-1.5,0.2,0),(-1.1,-0.6,0),(-2.2,-1,0))
             ]
        colors = [LOGO_GREEN,LOGO_BLUE,LOGO_BLUE,LOGO_RED, LOGO_BLUE,LOGO_BLUE, LOGO_RED, LOGO_BLUE, LOGO_BLUE, LOGO_RED,LOGO_BLUE, LOGO_GREEN, LOGO_RED]

        animations1 = []
        for vertices, color in zip(polygons1,colors):
            polygon1 = Polygon(*vertices, color=LOGO_WHITE, fill_color=color, fill_opacity=1, stroke_width=2)
            animations1.append(Create(polygon1, lag_ratio=0))
        self.play(*animations1)


        polygons2 = [
            ((-4.3,-3,0),(-3.4,-3.2,0),(-3.5,-1.7,0),(-4.3,-3,0)),
            ((-3.4,-3.2,0),(-2.7,-3,0),(-3.5,-1.7,0),(-3.4,-3.2,0))
           ]
        colors = [LOGO_GREEN,LOGO_BLUE,LOGO_BLUE,LOGO_RED, LOGO_BLUE,LOGO_BLUE, LOGO_RED, LOGO_BLUE, LOGO_BLUE, LOGO_RED,LOGO_BLUE, LOGO_GREEN, LOGO_RED]

        animations2 = []
        for vertices, color in zip(polygons2,colors):
            polygon2 = Polygon(*vertices, color=LOGO_WHITE, fill_color=color, fill_opacity=1, stroke_width=2)
            animations2.append(Create(polygon2, lag_ratio=0))
        self.play(*animations2)


        nt = Text("Non-Polyhedra",font_size=30).move_to([3.7,2.8,0])
        un = Underline(nt)
        snt = Text("have both flat surfaces\n\n and curved surfaces",font_size=25).move_to([3.8,1.5,0])
        self.play(Write(nt),Write(snt),Write(un))

        c = Circle(fill_color=LOGO_GREEN,color=LOGO_BLUE,fill_opacity=1,stroke_width=4).scale(0.6).move_to([2.2,-0.8,0])
        self.play(Create(c))

        r = Rectangle(height=1.4,width=1,fill_color=LOGO_GREEN,color=LOGO_BLUE,fill_opacity=1,stroke_width=4).move_to([5,-1.7,0])
        self.play(Create(r))
        e1 = Ellipse(fill_color=LOGO_BLUE,color=LOGO_GREEN,fill_opacity=1,stroke_width=4).scale(0.5).move_to([5,-1,0])
        self.play(Create(e1))
        e2 = Ellipse(fill_color=LOGO_BLUE,color=LOGO_GREEN,fill_opacity=1,stroke_width=4).scale(0.5).move_to([5,-2.4,0])
        self.play(Create(e2))
    
         
        t= Triangle(fill_color=LOGO_GREEN,color=LOGO_BLUE,fill_opacity=1,stroke_width=4).scale(0.6).move_to([3,-2.5,0])
        self.play(Create(t))
        e3 = Ellipse(fill_color=LOGO_BLUE,color=LOGO_GREEN,fill_opacity=1,stroke_width=4).scale(0.5).move_to([3,-3,0])
        self.play(Create(e3))

    def surfaces(self):

        self.angleChoice = [(TAU/4),(-TAU/4),(-TAU/4)]
        
        p1=cvo.CVO().CreateCVO("3D Objects have","").setPosition([4,2,0])
        p2=cvo.CVO().CreateCVO("Faces","").setPosition([0.5,-1,0])
        p3=cvo.CVO().CreateCVO("Edges","").setPosition([3.3,0,0])
        p4=cvo.CVO().CreateCVO("Vertices","").setPosition([6,-0.7,0])
      
        p1.cvolist.append(p4)
        p1.cvolist.append(p3)
        p1.cvolist.append(p2)
       
        self.construct1(p1,p1)
        
        a = ((-6,-0.75,0),(-4.25,-0.75,0),(-3,-1.25,0),(-4.75,-1.25,0),(-6,-0.75,0))
        base = Polygon(*a,color="#6DC9CD",fill_opacity=0.5,stroke_width=5)
       

        b = ((-6,0.5,0),(-4.25,0.5,0),(-3,0,0),(-4.75,0,0),(-6,0.5,0))
        top = Polygon(*b,color="#961C39",fill_opacity=1.5,stroke_width=5)


        c = ((-6.1,0.5,0),(-6.1,-0.75,0),(-4.75,-1.25,0),(-4.75,0,0),(-6,0.5,0))
        face1 = Polygon(*c,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)


        d = ((-6,0.5,0),(-4.25,0.5,0),(-4.25,-0.75,0),(-6.1,-0.75,0),(-6.1,0.5,0))
        face2 = Polygon(*d,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)


        e = ((-4.25,0.5,0),(-4.25,-0.75,0),(-2.9,-1.25,0),(-2.9,0,0),(-4.25,0.5,0))
        face3 = Polygon(*e,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)
 
        f = ((-4.75,0,0),(-4.75,-1.25,0),(-2.9,-1.25,0),(-2.9,0,0),(-4.75,0,0))
        face4 = Polygon(*f,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)

        t1 = Text("3D SHAPE - cube",font_size=45,color=LIGHT_PINK,weight=BOLD)
        t1.move_to([-4,2.7,0])
        u = Underline(t1)

        a1 = DashedLine(start=[-4.25,0.5,0],end=[-2.8,1,0]).add_tip(at_start=True)
        a2 = DashedLine(start=[-2.9,0,0],end=[-2.8,1,0]).add_tip(at_start=True)
        
        t2 = Text("Vertices",color="#DDCB2F",font_size=24,font= "Comic Sans MS",weight=BOLD)
        t2.move_to([-2.8,1.3,0])

        a3 = DashedLine(start=[-5.5,-1,0],end=[-6,-2,0]).add_tip(at_start=True)
        a4 = DashedLine(start=[-4,-1.25,0],end=[-6,-2,0]).add_tip(at_start=True)
        
        t3 = Text("Edges",color="#DDCB2F",font_size=24,font= "Comic Sans MS",weight=BOLD)
        t3.move_to([-6,-2.2,0])

        a5 = DashedLine(start=[-4.6,0.3,0],end=[-5.5,1.2,0]).add_tip(at_start=True)
        
        t4 = Text("Faces",color="#DDCB2F",font_size=24,font= "Comic Sans MS",weight=BOLD)
        t4.move_to([-5.5,1.4,0])
        

        self.play(Write(base),Write(top),Write(face1),Write(face2),Write(face3),Write(face4))
        self.play(Write(t1),Create(u))
        self.play(Write(a1),Write(a2),Write(t2))
        self.play(Write(a3),Write(a4),Write(t3))
        self.play(Write(a5),Write(t4))

    def regpoly(self):

        self.angleChoice = [(TAU/4),(-TAU/4)]
        self.isRandom = False
        self.positionChoice=[[0,2.5,0],[-4,1,0],[4,1,0]]
        p2 = cvo.CVO().CreateCVO("Regular Polyhedron","")
        p3 = cvo.CVO().CreateCVO("Cube","")
        p4 = cvo.CVO().CreateCVO("Triangular Pyramid","")

        t = Text("all their faces are congruent. All their\n\n"
                 "edges are equal  and vertices are formed\n\n"
                 "by equal number of  edges. Such type of\n\n"
                  "solid objects are called regular polyhedra.",font_size= 22)  
        t.move_to([0.35,0.5,0])
        
        p2.cvolist.append(p3)
        p2.cvolist.append(p4)
        self.construct1(p2,p2)
        self.play(Write(t))  
        self.wait()
       

        polygons = [
            ((-6,-1.25,0),(-4.6,-1,0),(-3.8,-1.7,0),(-6,-1.25,0)),
            ((-4.8,1,0),(-6.1,-1.25,0),(-3.8,-1.7,0),(-4.8,1,0)),
            ((-4.8,1,0),(-4.6,-1,0),(-6.1,-1.25,0),(-4.8,1,0)),
            ((-4.8,1,0),(-4.6,-1,0),(-3.8,-1.7,0),(-4.8,1,0)),
            ]
        
        colors = ["#6A53C6", "#6A53C6", "#6A53C6", "#6A53C6",  "#6A53C6", "#6A53C6", "#6A53C6 ", "#6DC9CD"]


        animations = []
        for vertices, color in zip(polygons, colors):
            polygon = Polygon(*vertices, color=LIGHT_PINK, fill_color=color, fill_opacity=1, stroke_width=4).shift(RIGHT*9 + DOWN*1.5)
            animations.append(Create(polygon, lag_ratio=0))
        
        self.play(*animations)


        polygons1 = [
            ((-6,-0.75,0),(-4.25,-0.75,0),(-3,-1.25,0),(-4.75,-1.25,0),(-6,-0.75,0)),
            ((-6,0.5,0),(-4.25,0.5,0),(-3,0,0),(-4.75,0,0),(-6,0.5,0)),
            ((-6.1,0.5,0),(-6.1,-0.75,0),(-4.75,-1.25,0),(-4.75,0,0),(-6,0.5,0)),
            ((-4.75,0,0),(-4.75,-1.25,0),(-2.9,-1.25,0),(-2.9,0,0),(-4.75,0,0))
            ]
        
        colors = [LIGHT_PINK,LIGHT_PINK,LIGHT_PINK,LIGHT_PINK,LIGHT_PINK,LIGHT_PINK,LIGHT_PINK,LIGHT_PINK]


        animations1 = []
        for vertices, color in zip(polygons1, colors):
            polygon1 = Polygon(*vertices, color="#6A53C6", fill_color=color, fill_opacity=1, stroke_width=4).shift(RIGHT*2 + DOWN*1.5)
            animations1.append(Create(polygon1, lag_ratio=0))
        
        self.play(*animations1)









if __name__ == "__main__":
    scene = Grade8Chapter13Visualising3Din2DAnim()
    scene.render()        