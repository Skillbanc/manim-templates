import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo


class testshapes(ThreeDScene,AbstractAnim):

    def construct(self):
    #      self.GithubSourceCodeReference()

    # def SetDeveloperList(self):
    #     self.DeveloperList="lasya"  


    #     # self.play(Write(NumberPlane())) 
    #     # direction=X_AXIS+Y_AXIS+2*Z_AXIS, self.set_camera_orientation(phi=6*PI/11, theta=PI/9)
    #     cone = Cone( resolution=10,height=2,base_radius=1.5,fill_color="#6DC9CD")
    #     self.set_camera_orientation(phi=75* DEGREES,theta=-45*DEGREES)
    #     cone.move_to([-1, -3, 0])
    #     text1=Text("Cone").scale(2).set_shade_in_3d(True) 
    #     text1.rotate(PI/2,axis=RIGHT)
    #     text1.to_corner(UL*3)
    #     self.play(Write(cone))    
    #     self.play(Write(text1))
    #     self.wait(1)
    #     self.play(Unwrite(text1))
    #     self.play(Unwrite(cone))
        
       
    #     # self.play(Write(NumberPlane()))
    #     # self.set_camera_orientation(phi=75* DEGREES,theta=-45*DEGREES)
    #     sphere2 = Sphere(center=(-2, -3, 0), radius=2, resolution=(18, 18))
    #     sphere2.set_color(GREEN)
    #     self.add(sphere2)
    #     text2=Text("Sphere").scale(2).set_shade_in_3d(True) 
    #     text2.rotate(PI/2,axis=RIGHT)
    #     text2.to_corner(UL*3)
        
    #     self.play(Write(sphere2))
    #     self.play(Write(text2))
    #     self.wait()
    #     self.play(Unwrite(text2))
    #     self.play(Uncreate(sphere2))

        
    #     # self.play(Write(NumberPlane()))
    #     # self.set_camera_orientation(phi=75 * DEGREES,theta=-45*DEGREES)
    #     cyc= Cylinder(resolution=(18, 18),fill_color=RED)
    #     cyc.set_color(RED)
    #     cyc.move_to([-1, -3, 0])
    #     text3=Text("cylinder").scale(2).set_shade_in_3d(True) 
    #     text3.rotate(PI/2,axis=RIGHT)
    #     text3.to_corner(UL*3)

    #     self.play(Write(cyc))
    #     self.play(Write(text3))
    #     self.wait()
    #     self.play(Unwrite(text3))
    #     self.play(Unwrite(cyc))


        # cube = Cube(side_length=2, fill_opacity=0.7, fill_color="#6A53C6")
        # cube.move_to([-2, -3, 0])
        # text4=Text("Cube").scale(2).set_shade_in_3d(True) 
        # text4.rotate(PI/2,axis=RIGHT)
        # text4.to_corner(UL*3)
        
    #     self.play(Write(cube))
    #     self.play(Write(text4))
    #     self.wait()
    #     self.play(Unwrite(text4))
    #     self.play(Unwrite(cube))

    #     # prismLarge = Prism(dimensions=[1.5, 3, 4.5]).move_to([2, 0, 0])
    #     cuboid = Prism(dimensions=[1.5, 3, 4.5], fill_opacity=0.7, fill_color="#CD289F")
    #     cuboid.move_to([-2, -3, 0])
    #     text5=Text("Cuboid").scale(2).set_shade_in_3d(True) 
    #     text5.rotate(PI/2,axis=RIGHT)
    #     text5.to_corner(UL*3)
        
    #     self.play(Write(cuboid))
    #     self.play(Write(text5))
    #     self.wait()
    #     self.play(Unwrite(text5))
    #     self.play(Unwrite(cuboid))

        # t2 = Table(
        #     [["6", "12","8"],
        #     ["6", "12","8"],["2", "1","2"],
        #     ["3", "2","0"],["5","9","6"],["5", "8","5"],
        #     ["4", "6","4"],["0","0","0"]],
        #     row_labels=[Text("Cube"), Text("Cuboid"),Text("Cone"), 
        #             Text("Cylinder"),Text("Prism"),Text("Square Pyramid"), 
        #             Text("Triangular Pyramid"),Text("Sphere")],
        #     col_labels=[Text("Faces"), Text("Edges"),Text("Vertices")],
        #     top_left_entry=Star().scale(0.3),
        #     include_outer_lines=True,
        #     arrange_in_grid_config={"cell_alignment": LEFT})
        # t2.scale(0.5)

        # self.play(Write(NumberPlane()))

        # m1 = ((-1.75,2.25,0),(1.75,2.25,0),(1.75,1.25,0),(-1.75,1.25,0),(-1.75,2.25,0))
        # sur1 = Polygon(*m1,color="#6DC9CD",fill_opacity=0.5,stroke_width=5)
        # n1 = Text("Rectangular Surface",font_size=25)
        # n1.move_to([0,0.8,0])
        # l1 = DashedLine(start=[2.8,-0.5,0],end=[1.8,1.5,0]).add_tip(at_start=True)


        # m2 = ((-0,-0.7,0),(1,-2.5,0),(-1,-2.5,0),(-0,-0.7,0))
        # sur2 = Polygon(*m2,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)
        # n2 = Text("Triangular Surface",font_size=25)
        # n2.move_to([0,-0.3,0])
        # l2 = DashedLine(start=[-4.3,-0.3,0],end=[-0.8,-1.5,0]).add_tip(at_start=True)

        # self.play(Write(sur1))
        # self.play(Write(n1))
        # self.play(Write(l1))
        # self.play(Write(sur2))
        # self.play(Write(n2))
        # self.play(Write(l2))

        cone = Cone( resolution=10,height=2,base_radius=1.5,fill_color="#6DC9CD")
        self.set_camera_orientation(phi=75* DEGREES,theta=-45*DEGREES)
        cone.move_to([-1, -3, 0])
        text1=Text("Cone").scale(2).set_shade_in_3d(True) 
        text1.rotate(PI/2,axis=RIGHT)
        text1.to_corner(UL*3)
        self.play(Write(cone))    
        self.play(Write(text1))
        self.wait(1)
        # self.play(Unwrite(text1))
        # self.play(Unwrite(cone))
        self.set_camera_orientation(phi=0,theta=-90 * DEGREES,gamma=0)

        p1=cvo.CVO().CreateCVO("Cone has","").setPosition([4,2.8,0])

        p2=cvo.CVO().CreateCVO("Faces","2").setPosition([0.5,1.5,0])
        p3=cvo.CVO().CreateCVO("Edges","1").setPosition([3.3,0.5,0])
        p4=cvo.CVO().CreateCVO("Vertices","1").setPosition([6,1.2,0])

        p5=cvo.CVO().CreateCVO("1 Circular Face","").setPosition([-0.5,-0.5,0])
        p6=cvo.CVO().CreateCVO("1 Curved Face","").setPosition([0.7,-3,0])
        p7=cvo.CVO().CreateCVO("Corners of the Edges are the Vertices","").setPosition([4,-1.7,0])

        p1.cvolist.append(p2)
        p1.cvolist.append(p3)
        p1.cvolist.append(p4)
        p2.cvolist.append(p5)
        p2.cvolist.append(p6)
        self.construct1(p1,p1)
        self.isFadeOutAtTheEndOfThisScene

        #SPHERE
        self.set_camera_orientation(phi=75* DEGREES,theta=-45*DEGREES)
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
        self.set_camera_orientation(phi=0,theta=-90 * DEGREES,gamma=0)

        #CYLINDER
        self.set_camera_orientation(phi=75* DEGREES,theta=-45*DEGREES)
        cyc= Cylinder(resolution=(18, 18),fill_color=RED)
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
        self.set_camera_orientation(phi=0,theta=-90 * DEGREES,gamma=0)

        #CUBE
        self.set_camera_orientation(phi=75* DEGREES,theta=-45*DEGREES)
        cube = Cube(side_length=2, fill_opacity=0.7, fill_color="#6A53C6")
        cube.move_to([-2, -3, 0])
        text4=Text("Cube").scale(2).set_shade_in_3d(True) 
        text4.rotate(PI/2,axis=RIGHT)
        text4.to_corner(UL*3)
        
        self.play(Write(cube))
        self.play(Write(text4))
        self.wait()
        self.play(Unwrite(text4))
        self.play(Unwrite(cube))
        self.set_camera_orientation(phi=0,theta=-90 * DEGREES,gamma=0)

        #CUBOID
        self.set_camera_orientation(phi=75* DEGREES,theta=-45*DEGREES)
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

        self.set_camera_orientation(phi=0,theta=-90 * DEGREES,gamma=0)


    def cuboid(self):  


        # self.play(Write(NumberPlane()))
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



        self.play(Write(base))
        self.play(Write(top))
        self.play(Write(face1))
        self.play(Write(face2))
        self.play(Write(face3))
        self.play(Write(face4))
        self.play(Write(t1))
        # self.wait()  

    def cube(self): 

        # self.play(Write(NumberPlane()))
        
        a = ((-6,-0.75,0),(-4.25,-0.75,0),(-3,-1.25,0),(-4.75,-1.25,0),(-6,-0.75,0))
        base = Polygon(*a,color="#6DC9CD",fill_opacity=0.5,stroke_width=5)
       

        b = ((-6,0.5,0),(-4.25,0.5,0),(-3,0,0),(-4.75,0,0),(-6,0.5,0))
        top = Polygon(*b,color="#6DC9CD",fill_opacity=0.5,stroke_width=5)


        c = ((-6.1,0.5,0),(-6.1,-0.75,0),(-4.75,-1.25,0),(-4.75,0,0),(-6,0.5,0))
        face1 = Polygon(*c,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)


        d = ((-6,0.5,0),(-4.25,0.5,0),(-4.25,-0.75,0),(-6.1,-0.75,0),(-6.1,0.5,0))
        face2 = Polygon(*d,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)


        e = ((-4.25,0.5,0),(-4.25,-0.75,0),(-2.9,-1.25,0),(-2.9,0,0),(-4.25,0.5,0))
        face3 = Polygon(*e,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)
 
        f = ((-4.75,0,0),(-4.75,-1.25,0),(-2.9,-1.25,0),(-2.9,0,0),(-4.75,0,0))
        face4 = Polygon(*f,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)

        t1 = Text("Cube",font="Comic Sans MS",color=LIGHT_PINK,weight=BOLD)
        t1.move_to([-4.5,1.5,0])



        self.play(Write(base))
        self.play(Write(top))
        self.play(Write(face1))
        self.play(Write(face2))
        self.play(Write(face3))
        self.play(Write(face4))
        self.play(Write(t1))
        # self.wait()

    def tripyramid(self):  


        # self.play(Write(NumberPlane()))

        a = ((-6,-1.25,0),(-4.6,-1,0),(-3.8,-1.7,0),(-6,-1.25,0))
        base = Polygon(*a,color="#6DC9CD",fill_opacity=0.5,stroke_width=5)


        c = ((-4.8,1,0),(-6.1,-1.25,0),(-3.8,-1.7,0),(-4.8,1,0))
        face1 = Polygon(*c,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)


        d = ((-4.8,1,0),(-4.6,-1,0),(-6.1,-1.25,0),(-4.8,1,0))
        face2 = Polygon(*d,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)


        e = ((-4.8,1,0),(-4.6,-1,0),(-3.8,-1.7,0),(-4.8,1,0))
        face3 = Polygon(*e,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)
 

        t1 = Text("Triangular",font="Comic Sans MS",color=LIGHT_PINK,weight=BOLD)
        t1.move_to([-4.7,3,0])

        t2 = Text("Pyramid",font="Comic Sans MS",color=LIGHT_PINK,weight=BOLD)
        t2.move_to([-4.7,2,0])


        self.play(Write(base))
        self.play(Write(face1))
        self.play(Write(face2))
        self.play(Write(face3))
        self.play(Write(t1))
        self.play(Write(t2))
        # self.wait()  


    def prism(self):  


        # self.play(Write(NumberPlane()))
        a = ((5,-1.75,0),(3.2,-1.75,0),(2.9,-2.25,0),(5,-1.75,0))
        base = Polygon(*a,color="#6DC9CD",fill_opacity=0.5,stroke_width=5)
       

        b = ((5,1.25,0),(3.2,1.25,0),(2.9,0.75,0),(5,1.25,0))
        top = Polygon(*b,color="#6DC9CD",fill_opacity=0.5,stroke_width=5)


        c = ((5.1,-1.75,0),(5.1,1.25,0),(2.9,0.75,0),(2.9,-2.25,0),(5,-1.75,0))
        face1 = Polygon(*c,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)


        d = ((5.1,-1.75,0),(5.1,1.25,0),(3.2,1.25,0),(3.2,-1.75,0),(5.1,-1.75,0))
        face2 = Polygon(*d,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)


        e = ((3.2,1.25,0),(3.2,-1.75,0),(2.9,-2.25,0),(2.9,0.75,0),(3.2,1.25,0))
        face3 = Polygon(*e,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)
 

        t1 = Text("Prism",font="Comic Sans MS",color=LIGHT_PINK,weight=BOLD)
        t1.move_to([4,2.5,0])


        self.play(Write(base))
        self.play(Write(top))
        self.play(Write(face2))
        self.play(Write(face3))
        self.play(Write(face1))
        self.play(Write(t1))     
    

    def sqpyramid(self):


        a = ((1,-1.75,0),(-0.75,-1.75,0),(-2,-2.25,0),(-0.25,-2.25,0),(1,-1.75,0))
        base = Polygon(*a,color="#6DC9CD",fill_opacity=0.5,stroke_width=5)

        c = ((-0.2,1,0),(1,-1.75,0),(-0.75,-1.75,0),(-0.2,1,0))
        face1 = Polygon(*c,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)

        d = ((-0.2,1,0),(1,-1.75,0),(-0.25,-2.25,0),(-0.2,1,0))
        face2 = Polygon(*d,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)

        e = ((-0.2,1,0),(-0.75,-1.75,0),(-2,-2.25,0),(-0.2,1,0))
        face3 = Polygon(*e,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)
 
        f = ((-0.2,1,0),(-0.25,-2.25,0),(-2,-2.25,0),(-0.2,1,0))
        face4 = Polygon(*f,color="#6DC9CD",fill_opacity=0.2,stroke_width=5)

        t1 = Text("Square",font="Comic Sans MS",color=LIGHT_PINK,weight=BOLD)
        t1.move_to([-0.2,3,0])

        t2 = Text("Pyramid",font="Comic Sans MS",color=LIGHT_PINK,weight=BOLD)
        t2.move_to([-0.2,2,0])


        self.play(Write(base))
        self.play(Write(face1))
        self.play(Write(face2))
        self.play(Write(face3))
        self.play(Write(face4))
        self.play(Write(t1))
        self.play(Write(t2))
  
    


        t2 = Table(
            [["6", "12","8"],
            ["6", "12","8"],["2", "1","2"],
            ["3", "2","0"],["5","9","6"],["5", "8","5"],
            ["4", "6","4"],["0","0","0"]],
            row_labels=[Text("Cube"), Text("Cuboid"),Text("Cone"), 
                    Text("Cylinder"),Text("Prism"),Text("Square Pyramid"), 
                    Text("Triangular Pyramid"),Text("Sphere")],
            col_labels=[Text("Faces"), Text("Edges"),Text("Vertices")],
            top_left_entry=Star().scale(0.3),
            include_outer_lines=True,
            arrange_in_grid_config={"cell_alignment": LEFT})
        t2.scale(0.5)

        self.play(Create(t2))
        
        
    def test1(self):

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
                 "the Edges of a 3D Shape",font_size=20)
        h.move_to([-0.25,-1.5,0])

        h1 = Text("The colored dots where edges meet are\n\n"
                 "the Vertices of a 3D Shape",font_size=20)
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
       

        # top = Dot([-4.8,1,0],color="#6DC9CD")


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
        self.play(Write(t21))
        self.play(Write(t11))
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



if __name__ == "__main__":
    scene = testshapes()
    scene.render()








