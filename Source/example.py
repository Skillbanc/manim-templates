import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class example(AbstractAnim): #Scene

    def construct(self):
    #     # self.cir()
    #     self.VolumeAnim()
    #     self.test()
       self.test1()


    # def cir(self):

    #     self.play(Write(NumberPlane()))

    #     cir= Circle( radius=1, color=PINK)

    #     d1= Dot([-0.5,0.5,0])
    #     d2= Dot([0.5,0.5,0])

    #     self.play(Write(cir))
    #     self.play(Write(d1))
    #     self.play(Write(d2))

        
    # def VolumeAnim(self):
       
    #     # Title
    #     title = Text("VOLUME OF COMBINATION OF SOLIDS").to_edge(UP)
    #     underline = Underline(title)
    #     self.play(Write(title))
    #     self.play(Create(underline))
        
    #     self.wait(1)

    #     # Description text
    #     description = Text(
    #         "Let us understand the volume of a combined solid through an example:"
    #         ).scale(0.6).next_to(title, DOWN, buff=0.5)
    #     self.play(Write(description))
    #     self.wait(1)

    #     # Example setup
    #     example_text = Text(
    #         "Suresh runs an industry in a shed which is in the shape of a cuboid"
    #         "surmounted by a half-cylinder.\nThe base of the shed is 7m x 15m and"
    #         "the height of the cuboid portion is 8m. \nFind the volume of air that"
    #         "the shed can hold.""Next, the total space occupied by the machinery\n is 300 m^3 and there are"
    #         "20 workers, each occupying about 0.08 m^3 space.\n Then, the volume of the"
    #         "air in the shed is given by.The length,breadth,height of the cuboid\n are 15m,7m,8m respectively.Diameter of half cylinder is 7m and its height is 15m.\n"
    #     ).scale(0.5).next_to(description, DOWN, buff=0.5)
    #     self.play(Write(example_text))
    #     self.wait(2)

    #     self.play(Unwrite(description))    #a
    #     self.play(Unwrite(example_text))   #a
    #     self.play(Unwrite(title))          #a

    # def test(self):   #added

    #     # Define parameters
    #     length = 5
    #     width = 2
    #     height = 2

    #     # Create a cuboid
    #     cuboid = Cube()
    #     cuboid.scale([length / 2, width / 2, height / 2])
    #     cuboid.set_fill(WHITE, opacity=0.5)
    #     cuboid.set_stroke(BLACK, width=3)

    #     # Create a semicylinder above the cuboid
    #     semicylinder = Surface(
    #         lambda u, v: np.array([
    #             v,
    #             (width / 2) * np.cos(u),
    #             (width / 2) * np.sin(u) + height  # Shifted up by the height of the cuboid
    #         ]),
    #         u_range=[0, PI],
    #         v_range=[-length / 2, length / 2],  # Adjusted v_range to fit the cuboid's length
    #         fill_color=BLUE,  # Color the entire surface with blue
    #         fill_opacity=0.5,
    #         stroke_color=BLACK
    #     )

    #     # Position the semicylinder to place it slightly above the cuboid
    #     offset = 0.5  # Adjust this value to set how much above the cuboid the semicylinder should be
    #     semicylinder.move_to(cuboid.get_center() + np.array([0, 0, height / 2 + offset]))

    #     # Combine shapes
    #     self.add(cuboid, semicylinder)

    #     # Set the camera position and rotate somewhat towards the left
    #     self.set_camera_orientation(phi=75* DEGREES,theta=-45*DEGREES)
    #     # title1 = Text("VOLUME OF COMBINATION OF SOLIDS").to_edge(UP)
    #     # underline = Underline(title1)
    #     # title1.rotate(PI/2,axis=LEFT)
    #     # self.play(Write(title1))
    #     # self.play(Create(underline))
        
    #     self.wait(1)

    #     # Description text
    #     desc = Text(
    #         "Let us understand the volume of a combined solid through an example:"
    #         )
    #     #.next_to(title1, DOWN, buff=0.5)
    #     desc.rotate(PI/2,axis=LEFT)
    #     desc.to_corner(UL)
    #     self.play(Write(desc))
    #     self.wait(1)
    #     # Example setup
    #     # text = Text(
    #     #     "Suresh runs an industry in a shed which is in the shape of a cuboid"
    #     #     "surmounted by a half-cylinder.\nThe base of the shed is 7m x 15m and"
    #     #     "the height of the cuboid portion is 8m. \nFind the volume of air that"
    #     #     "the shed can hold.""Next, the total space occupied by the machinery\n is 300 m^3 and there are"
    #     #     "20 workers, each occupying about 0.08 m^3 space.\n Then, the volume of the"
    #     #     "air in the shed is given by.The length,breadth,height of the cuboid\n are 15m,7m,8m respectively.Diameter of half cylinder is 7m and its height is 15m.\n"
    #     # ).next_to(desc, DOWN, buff=0.5)
    #     # self.play(Write(text))
    #     # text.rotate(PI/2,axis=LEFT)
    #     # self.wait(2)
    #     # self.wait(2)


    # def construct(self):
    #     self.camera.background_color = WHITE

    #     self.set_camera_orientation(phi=0 * DEGREES, theta=0* DEGREES)

    #     axes = ThreeDAxes()
    #     circle = Circle(radius=1, color=RED)

    #     self.add(circle, axes)

    #     sphere = Sphere(radius=0.1,color=RED).shift(RIGHT)
    # #completed the setup

    #     self.play(MoveAlongPath(sphere, circle), run_time=3, rate_func=linear)
    # #circular motion
    
    #     self.move_camera(phi=90 * DEGREES, theta=0 * DEGREES,run_time =2)
    # #Camera movement 
    
    #     self.wait()

    #     self.move_camera(phi=0 * DEGREES, theta=0 * DEGREES)
    # #again camera movement
    #     self.wait()

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

        # self.play(Create(t2))
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
    scene = example()
    scene.render()