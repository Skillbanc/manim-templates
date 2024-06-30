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

        

    def construct(self):
        self.camera.background_color = WHITE

        self.set_camera_orientation(phi=0 * DEGREES, theta=0* DEGREES)

        axes = ThreeDAxes()
        circle = Circle(radius=1, color=RED)

        self.add(circle, axes)

        sphere = Sphere(radius=0.1,color=RED).shift(RIGHT)
    #completed the setup

        self.play(MoveAlongPath(sphere, circle), run_time=3, rate_func=linear)
    #circular motion
    
        self.move_camera(phi=90 * DEGREES, theta=0 * DEGREES,run_time =2)
    #Camera movement 
    
        self.wait()

        self.move_camera(phi=0 * DEGREES, theta=0 * DEGREES)
    #again camera movement
        self.wait()

       
 


if __name__ == "__main__":
    scene = example()
    scene.render()