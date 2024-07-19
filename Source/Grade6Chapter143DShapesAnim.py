import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class Grade6Chapter143DShapesAnim(AbstractAnim,ThreeDScene):

    def construct(self):
        self.RenderSkillbancLogo()
        self.intro()  
        self.fadeOutCurrentScene()
        self.intro1()
        self.fadeOutCurrentScene()
        self.intro2()
        self.fadeOutCurrentScene()
        self.cupy()
        self.fadeOutCurrentScene()
        self.cyco()
        self.fadeOutCurrentScene()
        self.cone3D()
        self.sphere3D()
        self.cylinder3D()
        self.cube3D()
        self.cuboid3D()
        self.extro()
        self.fadeOutCurrentScene()
        self.intro3()
        self.fadeOutCurrentScene()
        self.intro5()
        self.fadeOutCurrentScene()
        self.intro4()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()


    def SetDeveloperList(self):
        self.DeveloperList="Lasya Nannapaneni"   


    def SetSourceCodeFileName(self):
        self.SourceCodeFileName = "Grade6Chapter143DShapesAnim.py"  


    def intro(self):

        self.isRandom = False
        
        # self.play(Write(NumberPlane())) 

        p1=cvo.CVO().CreateCVO("Understanding 2D,3D Shapes","").setPosition([0,2.2,0])
        p2=cvo.CVO().CreateCVO("2D Shapes","").setPosition([-5,0.5,0])
        p3=cvo.CVO().CreateCVO("3D Shapes","").setPosition([5,0.5,0])

        p4=cvo.CVO().CreateCVO("Two-Dimensional","2 Directions").setPosition([-2.6,-2.2,0])
        
        p5=cvo.CVO().CreateCVO("Three-Dimensional","3 Directions").setPosition([2.6,-2.2,0])

        p1.cvolist.append(p2)
        p1.cvolist.append(p3)
        p2.cvolist.append(p4)
        p3.cvolist.append(p5)

        p4.setcircleradius(1.2)
        p5.setcircleradius(1.2)
        self.construct1(p1,p1)
    
    
    def intro1(self):
        
        self.isRandom = False
        
        # self.play(Write(NumberPlane())) 

        p1=cvo.CVO().CreateCVO("Types of 3D Shapes","").setPosition([0,2.2,0])
       
        p2=cvo.CVO().CreateCVO("Cube","").setPosition([-5,2.2,0])
        p3=cvo.CVO().CreateCVO("Cuboid","").setPosition([5,2.2,0])
        p4=cvo.CVO().CreateCVO("Cylinder","").setPosition([-2,-1.5,0])
        p5=cvo.CVO().CreateCVO("Sphere","").setPosition([-5,-2,0])
        p6=cvo.CVO().CreateCVO("Prism","").setPosition([2,-1.5,0])
        p7=cvo.CVO().CreateCVO("Pyramid","").setPosition([5,-2,0])
        p8=cvo.CVO().CreateCVO("Cone","").setPosition([-3.5,0.8,0])


        p1.cvolist.append(p2)
        p1.cvolist.append(p3)
        p1.cvolist.append(p4)
        p1.cvolist.append(p5)
        p1.cvolist.append(p6)
        p1.cvolist.append(p7)
        p1.cvolist.append(p8)

      
        self.construct1(p1,p1)
       
        
    def intro2(self):
        
        self.isRandom = False
        
        # self.play(Write(NumberPlane())) 
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

        t1 = Text("3D SHAPE - cube",font="Comic Sans MS",font_size=45,color=LIGHT_PINK,weight=BOLD)
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
        t4.move_to([-5.5,1.3,0])
        

        self.play(Write(base))
        self.play(Write(top))
        self.play(Write(face1))
        self.play(Write(face2))
        self.play(Write(face3))
        self.play(Write(face4))
        self.play(Write(t1))
        self.play(Create(u))
        self.play(Write(a1))
        self.play(Write(a2))
        self.play(Write(t2))
        self.play(Write(a3))
        self.play(Write(a4))
        self.play(Write(t3))
        self.play(Write(a5))
        self.play(Write(t4))


        # self.wait()

        p1=cvo.CVO().CreateCVO("Most 3D Shapes have","").setPosition([4,2.8,0])

        p2=cvo.CVO().CreateCVO("Faces","").setPosition([0.5,1.5,0])
        p3=cvo.CVO().CreateCVO("Edges","").setPosition([3.3,0.5,0])
        p4=cvo.CVO().CreateCVO("Vertices","").setPosition([6,1.2,0])

        p5=cvo.CVO().CreateCVO("Plane surfaces are the faces","").setPosition([-0.5,-0.5,0])
        p6=cvo.CVO().CreateCVO("Sides of the Faces are the Edges","").setPosition([0.7,-3,0])
        p7=cvo.CVO().CreateCVO("Corners of the Edges are the Vertices","").setPosition([4,-1.7,0])

        p1.cvolist.append(p4)
        p1.cvolist.append(p3)
        p1.cvolist.append(p2)
        p4.cvolist.append(p7)
        p3.cvolist.append(p6)
        p2.cvolist.append(p5)
        self.construct1(p1,p1)


    def cupy(self):
        

        a = ((6,-1.75,0),(4.25,-1.75,0),(3,-2.25,0),(4.75,-2.25,0),(6,-1.75,0))
        base = Polygon(*a,color="#6DC9CD",fill_opacity=0.5,stroke_width=5)
       

        b = ((6,1.25,0),(4.25,1.25,0),(3,0.75,0),(4.75,0.75,0),(6,1.25,0))
        top = Polygon(*b,color="#6DC9CD",fill_opacity=0.5,stroke_width=5)


        c = ((6.1,1.25,0),(6.1,-1.75,0),(4.75,-2.25,0),(4.75,0.75,0),(6,1.25,0))
        face1 = Polygon(*c,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)


        d = ((6,1.25,0),(4.25,1.25,0),(4.25,-1.75,0),(6.1,-1.75,0),(6.1,1.25,0))
        face2 = Polygon(*d,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)


        e = ((4.25,1.25,0),(4.25,-1.75,0),(2.9,-2.25,0),(2.9,0.75,0),(4.25,1.25,0))
        face3 = Polygon(*e,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)
 
        f = ((4.75,0.75,0),(4.75,-2.25,0),(2.9,-2.25,0),(2.9,0.75,0),(4.75,0.75,0))
        face4 = Polygon(*f,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)

        t1 = Text("Cuboid",font="Comic Sans MS",color=LIGHT_PINK,weight=BOLD)
        t1.move_to([4.5,2.5,0])

        dot = Dot(color=WHITE)

        h = Text("The paths, dot is moving along are\n\n"
                 "the Edges of a 3D Shape",font_size=22)
        h.move_to([-0.25,-1.5,0])

        h1 = Text("The colored dots where edges meet are\n\n"
                 "the Vertices of a 3D Shape",font_size=22)
        h1.move_to([0,1.5,0])


        d11 = Dot(color="#CF1161")
        d11.move_to([6.1,-1.75,0])
        d21 = Dot(color="#CF1161")
        d21.move_to([4.25,-1.75,0])
        d31 = Dot(color="#CF1161")
        d31.move_to([2.9,-2.25,0])
        d41 = Dot(color="#CF1161")
        d41.move_to([4.75,-2.25,0])
        d51 = Dot(color="#CF1161")
        d51.move_to([6.1,1.25,0])
        d61 = Dot(color="#CF1161")
        d61.move_to([4.25,1.25,0])
        d71 = Dot(color="#CF1161")
        d71.move_to([2.9,0.75,0])
        d81 = Dot(color="#CF1161")
        d81.move_to([4.75,0.75,0])
        
        



        a1 = ((-6,-1.25,0),(-4.6,-1,0),(-3.8,-1.7,0),(-6,-1.25,0))
        base1 = Polygon(*a1,color="#6DC9CD",fill_opacity=0.5,stroke_width=5)


        c1 = ((-4.8,1,0),(-6.1,-1.25,0),(-3.8,-1.7,0),(-4.8,1,0))
        face11 = Polygon(*c1,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)


        d1 = ((-4.8,1,0),(-4.6,-1,0),(-6.1,-1.25,0),(-4.8,1,0))
        face21 = Polygon(*d1,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)


        e1 = ((-4.8,0.9,0),(-4.6,-1,0),(-3.8,-1.7,0),(-4.8,0.9,0))
        face31 = Polygon(*e1,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)
 

        t11 = Text("Triangular",font="Comic Sans MS",color=LIGHT_PINK,weight=BOLD)
        t11.move_to([-4.7,3,0])

        t21 = Text("Pyramid",font="Comic Sans MS",color=LIGHT_PINK,weight=BOLD)
        t21.move_to([-4.7,2,0])

        dot1 = Dot(color=WHITE)
        
        d1 = Dot(color="#CF1161")
        d1.move_to([-4.8,1,0])
        d2 = Dot(color="#CF1161")
        d2.move_to([-4.6,-1,0])
        d3 = Dot(color="#CF1161")
        d3.move_to([-6.1,-1.25,0])
        d4 = Dot(color="#CF1161")
        d4.move_to([-3.8,-1.7,0])
        

        self.play(Write(base))
        self.play(Write(top))
        self.play(Write(face1))
        self.play(Write(face2))
        self.play(Write(face3))
        self.play(Write(face4))
        self.play(Write(t1))
        self.play(Write(base1))
        self.play(Write(face11))
        self.play(Write(face21))
        self.play(Write(face31))
        self.play(Write(t11))
        self.play(Write(t21))
        self.play(Create(d1))
        self.play(Create(d2))
        self.play(Create(d3))
        self.play(Create(d4))
        self.play(Create(d11))
        self.play(Create(d21))
        self.play(Create(d31))
        self.play(Create(d41))
        self.play(Create(d51))
        self.play(Create(d61))
        self.play(Create(d71))
        self.play(Create(d81))

        self.play(Write(dot))
        self.play(Write(dot1))
        self.play(Write(h))
        self.play(Write(h1))
        self.play(MoveAlongPath(dot,top),run_time=2)
        self.play(MoveAlongPath(dot,face1),run_time=2)
        self.play(MoveAlongPath(dot1,face11),run_time=2)
        self.play(MoveAlongPath(dot1,face21),run_time=2)
        self.play(MoveAlongPath(dot,face2),run_time=2)
        self.play(MoveAlongPath(dot1,face31),run_time=1)
        self.play(MoveAlongPath(dot,face3),run_time=1)
        self.play(MoveAlongPath(dot1,base1),run_time=1)
        self.play(MoveAlongPath(dot,face4),run_time=2)
        self.play(MoveAlongPath(dot,base),run_time=1)
        self.play(Unwrite(h))
        self.play(Unwrite(h1))
        self.play(Unwrite(dot))
        self.play(Unwrite(dot1))



        m1 = ((-1.75,2.25,0),(1.75,2.25,0),(1.75,1.25,0),(-1.75,1.25,0),(-1.75,2.25,0))
        sur1 = Polygon(*m1,color="#6DC9CD",fill_opacity=0.5,stroke_width=5)
        n1 = Text("Rectangular Surface",font_size=25)
        n1.move_to([0,0.8,0])
        l1 = DashedLine(start=[2.8,-0.5,0],end=[1.8,1.5,0]).add_tip(at_start=True)


        m2 = ((-0,-0.7,0),(1,-2.5,0),(-1,-2.5,0),(-0,-0.7,0))
        sur2 = Polygon(*m2,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)
        n2 = Text("Triangular Surface",font_size=25)
        n2.move_to([0,-0.3,0])
        l2 = DashedLine(start=[-4.3,-0.3,0],end=[-0.8,-1.5,0]).add_tip(at_start=True)

        self.play(Write(sur1))
        self.play(Write(n1))
        self.play(Write(l1))
        self.play(Write(sur2))
        self.play(Write(n2))
        self.play(Write(l2))


    def cyco(self):
        
        # self.play(Write(NumberPlane()))

        base= Ellipse(color="#6DC9CD",fill_opacity=0.3)
        top= Ellipse(color="#6DC9CD",fill_opacity=0.3)

        line1 = Line(start=[-5,-1.5,0],end=[-5,1.5,0],color="#6DC9CD")
        line2 = Line(start=[-3,-1.5,0],end=[-3,1.5,0],color="#6DC9CD")

        t1 = Text("Cylinder",font="Comic Sans MS",color=LIGHT_PINK,weight=BOLD)
        t1.move_to([-4,2.5,0])


        base.move_to([-4,-1.5,0])
        top.move_to([-4,1.5,0])

        self.play(Write(base))
        self.play(Write(top))
        self.play(Write(line1))
        self.play(Write(line2))
        self.play(Write(t1))


        base1= Ellipse(color="#6DC9CD",fill_opacity=0.3)
       
        line11 = Line(start=[5,-1.5,0],end=[4,1.5,0],color="#6DC9CD")
        line21 = Line(start=[3,-1.5,0],end=[4,1.5,0],color="#6DC9CD")

        t11 = Text("Cone",font="Comic Sans MS",color=LIGHT_PINK,weight=BOLD)
        t11.move_to([4,2.5,0])


        base1.move_to([4,-1.5,0])


        self.play(Write(base1))
        self.play(Write(line11))
        self.play(Write(line21))
        self.play(Write(t11))
        
        # self.wait()

       


        # m2 = ((-0,-0.7,0),(1,-2.5,0),(-1,-2.5,0),(-0,-0.7,0))
        # sur2 = Polygon(*m2,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)
        base11= Ellipse(color="#6DC9CD",fill_opacity=0.3)
        base11.move_to([0,-1.5,0])
        n2 = Text("Circular Surface",font_size=25)
        n3 = Text("Curved Surface",font_size=25)
        n3.move_to([0,1.5,0])
        n2.move_to([0,-0.4,0])
        l1 = DashedLine(start=[4,-1.5,0],end=[0.8,-1.5,0]).add_tip(at_start=True)
        l2 = DashedLine(start=[-4,-1.6,0],end=[-0.6,-1.5,0]).add_tip(at_start=True)
        pl1 = DashedLine(start=[4,0.5,0],end=[1,1.5,0]).add_tip(at_start=True)
        pl2 = DashedLine(start=[-4,0.6,0],end=[-1.2,1.5,0]).add_tip(at_start=True)
        pl3 = DashedLine(start=[4,1.5,0],end=[2.4,2,0]).add_tip(at_start=True)
        n4 = Text("Apex",font_size=25)
        n4.move_to([2,2,0])
      

        self.play(Write(base11))
        self.play(Write(n2))
        self.play(Write(l1))
        self.play(Write(l2))
        self.play(Write(n3))
        self.play(Write(pl1))
        self.play(Write(pl2))
        self.play(Write(pl3))
        self.play(Write(n4))


    def cone3D(self):
        
        h = Text("Let's look at some 3D shapes")
        self.play(Write(h))
        self.play(Unwrite(h))

        #CONE
        cone = Cone(resolution=10, height=2, base_radius=1.5, fill_color="#6DC9CD")
        self.set_camera_orientation(phi= 75* DEGREES,theta= -45*DEGREES)
        cone.move_to([-1, -3, 0])
        text1=Text("Cone").scale(2).set_shade_in_3d(True) 
        text1.rotate(PI/2, axis=RIGHT)
        text1.to_corner(UL*3)
        self.play(Write(cone))    
        self.play(Write(text1))
        self.wait(1)
        self.play(Unwrite(text1))
        self.play(Unwrite(cone))
        self.set_camera_orientation(phi= 0, theta= -90 * DEGREES, gamma= 0)
    
    def sphere3D(self):

        #SPHERE
        self.set_camera_orientation(phi= 75* DEGREES, theta= -45*DEGREES)
        sphere2 = Sphere(center=(-2, -3, 0), radius=2, resolution=(18, 18))
        sphere2.set_color(GREEN)
        self.add(sphere2)
        text2=Text("Sphere").scale(2).set_shade_in_3d(True) 
        text2.rotate(PI/2,axis=RIGHT)
        text2.to_corner(UL*3)
        
        self.play(Write(sphere2))
        self.play(Write(text2))
        self.wait()
        self.play(Unwrite(text2))
        self.play(Uncreate(sphere2)) 
        self.set_camera_orientation(phi= 0, theta= -90 * DEGREES, gamma= 0)
    
    def cylinder3D(self):

        #CYLINDER
        self.set_camera_orientation(phi= 75* DEGREES, theta= -45*DEGREES)
        cyc= Cylinder(resolution = (18, 18),fill_color=RED)
        cyc.set_color(RED)
        cyc.move_to([-1, -3, 0])
        text3=Text("cylinder").scale(2).set_shade_in_3d(True) 
        text3.rotate(PI/2,axis=RIGHT)
        text3.to_corner(UL*3)

        self.play(Write(cyc))
        self.play(Write(text3))
        self.wait()
        self.play(Unwrite(text3))
        self.play(Unwrite(cyc))
        self.set_camera_orientation(phi= 0 , theta= -90 * DEGREES , gamma= 0)
    
    def cube3D(self):

        #CUBE
        self.set_camera_orientation(phi= 75* DEGREES , theta= -45*DEGREES)
        cube = Cube(side_length=2 , fill_opacity=0.7 , fill_color="#6A53C6")
        cube.move_to([-2, -3, 0])
        text4=Text("Cube").scale(2).set_shade_in_3d(True) 
        text4.rotate(PI/2,axis=RIGHT)
        text4.to_corner(UL*3)
        
        self.play(Write(cube))
        self.play(Write(text4))
        self.wait()
        self.play(Unwrite(text4))
        self.play(Unwrite(cube))
        self.set_camera_orientation(phi= 0 , theta= -90 * DEGREES , gamma= 0)
    
    def cuboid3D(self):

        #CUBOID
        self.set_camera_orientation(phi= 75 * DEGREES , theta= -45*DEGREES)
        cuboid = Prism(dimensions=[1.5, 3, 4.5], fill_opacity=0.7, fill_color="#CD289F")
        cuboid.move_to([-2, -3, 0])
        text5=Text("Cuboid").scale(2).set_shade_in_3d(True) 
        text5.rotate(PI/2,axis=RIGHT)
        text5.to_corner(UL*3)
        
        self.play(Write(cuboid))
        self.play(Write(text5))
        self.wait()
        self.play(Unwrite(text5))
        self.play(Unwrite(cuboid))
        self.set_camera_orientation(phi= 0 , theta= -90 * DEGREES , gamma= 0)
 

    def extro(self):
    
        t2 = Table(
            [["6", "12","8","0"],
            ["6", "12","8","0"],["2", "1","2","1"],
            ["3", "2","0","1"],["5","9","6","0"],["5", "8","5","0"],
            ["4", "6","4","0"],["0","0","0","1"]],
            row_labels=[Text("Cube"), Text("Cuboid"),Text("Cone"), 
                    Text("Cylinder"),Text("Prism"),Text("Square Pyramid"), 
                    Text("Triangular Pyramid"),Text("Sphere")],
            col_labels=[Text("Faces"), Text("Edges"),Text("Vertices"),Text("Curved Surface")],
            top_left_entry=Star().scale(0.3),
            include_outer_lines=True,
            arrange_in_grid_config={"cell_alignment": LEFT})
        t2.scale(0.5)
        self.play(Create(t2),run_time=6)
        self.wait(5)


    def intro3(self):
        
        # self.play(Write(NumberPlane()))

        p2 = cvo.CVO().CreateCVO("Closed figures","").setPosition([-5,1.8,0])
        p3 = cvo.CVO().CreateCVO("Polygon","").setPosition([-2,0,0])

        t = Text("A figure is a polygon if it is a closed figure,\n\n"
                 "formed with a definite number of straight lines.\n\n"
                 "Some examples are shown here.",font_size= 26)  
        
        a = ((2,-0.8,0),(3.8,-1.4,0),(4.5,-0.5,0),(3.4,0.5,0),(2,-0.8,0))
        d1 = Polygon(*a,color=WHITE,fill_opacity=0.5,stroke_width=5)

        b = ((1.3,-3,0),(2.3,-1.5,0),(3.3,-3,0),(1.3,-3,0))
        d2 = Polygon(*b,color=WHITE,fill_opacity=0.5,stroke_width=5)

        c = ((3.6,-2.2,0),(4.2,-1.4,0),(5.1,-1.7,0),(5.6,-2.5,0),(4.2,-3.2,0),(3.6,-2.2,0))
        d3 = Polygon(*c,color=WHITE,fill_opacity=0.5,stroke_width=5)
    
        t.move_to([2.7,2.5,0])
        p2.cvolist.append(p3)
        self.construct1(p2,p2)
        self.play(Write(t))
        self.play(Write(d1))
        self.play(Write(d2))
        self.play(Write(d3))
        self.wait()

        # a = Arc(0.5,TAU*1/4,-TAU*2.6/4,color=BLUE,stroke_width=2)

        # a.move_to([-5,0,0])
        # self.play(Create(a))
    
    def intro5(self):

        self.isRandom =  False
        self.positionChoice=[[-5,2,0],[-3,2,0],[-1,2,0],[1,2,0],[-5,-2,0],[-3,-2,0],[-1,-2,0],[1,-2,0],[3,2,0],[5,2,0],[3,-2,0],[5,-2,0]]

        p1= cvo.CVO().CreateCVO("Name","Triangle")
        p2= cvo.CVO().CreateCVO("No. of sides","3")
        p1.cvolist.append(p2)
        self.construct1(p1,p1)

        p3= cvo.CVO().CreateCVO("Name","Quadrilateral")
        p4= cvo.CVO().CreateCVO("No. of sides","4")
        p3.cvolist.append(p4)
        self.construct1(p3,p3)

        p5= cvo.CVO().CreateCVO("Name","Pentagon")
        p6= cvo.CVO().CreateCVO("No. of sides","5")
        p5.cvolist.append(p6)
        self.construct1(p5,p5)

        p7= cvo.CVO().CreateCVO("Name","Hexagon")
        p8= cvo.CVO().CreateCVO("No. of sides","6")
        p7.cvolist.append(p8)
        self.construct1(p7,p7)

        p9= cvo.CVO().CreateCVO("Name","Septagon")
        p10= cvo.CVO().CreateCVO("No. of sides","7")
        p9.cvolist.append(p10)
        self.construct1(p9,p9)

        p11= cvo.CVO().CreateCVO("Name","Octagon")
        p12= cvo.CVO().CreateCVO("No. of sides","8")
        p11.cvolist.append(p12)
        self.construct1(p11,p11)



    def intro4(self):

        # self.play(Write(NumberPlane()))
        self.isRandom = False
        self.positionChoice=[[0,2.5,0],[-4,1,0],[4,1,0]]
        p2 = cvo.CVO().CreateCVO("Regular Polygon","")
        p3 = cvo.CVO().CreateCVO("Square","").setangle([-TAU/4])
        p4 = cvo.CVO().CreateCVO("Equilateral Triangle","").setangle([ TAU/4])

        t = Text("A polygon with all equal sides, and\n\n"
                 "all equal angles is called a regular polygon",font_size= 22)  
        t.move_to([0.35,0.5,0])

        a = ((-3,-1,0),(-3,-3,0),(-1,-3,0),(-1,-1,0),(-3,-1,0))
        d1 = Polygon(*a,color="#FF5D7F",fill_opacity=0.5,stroke_width=5)

        b = ((1.5,-3,0),(2.5,-1.2,0),(3.5,-3,0),(1.5,-3,0))
        d2 = Polygon(*b,color=YELLOW_E,fill_opacity=0.5,stroke_width=5)

        t1 = Text("A Triangle with all sides\n\n"
                   "and all angles equal",font_size= 22)  
        t1.move_to([4.5,-1,0])

        t2 = Text("A Quadrilateral with all sides\n\n"
                   "and all angles equal",font_size= 22)  
        t2.move_to([-4.9,-1,0])

        p2.cvolist.append(p3)
        p2.cvolist.append(p4)
        self.construct1(p2,p2)
        self.play(Write(t))
        self.play(Write(d1))
        self.play(Write(d2))
        self.play(Write(t1))
        self.play(Write(t2))
        self.wait()
   

    
    
    
    


if __name__ == "__main__":
    scene = Grade6Chapter143DShapesAnim()
    scene.render()