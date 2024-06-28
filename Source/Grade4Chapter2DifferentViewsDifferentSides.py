from AbstractAnim import AbstractAnim
import cvo
from manim import ThreeDScene
from manim import *

class DifferentViews(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.Views()
        self.GithubSourceCodeReference()

    def Views(self):
        self.angleChoice=[TAU/4,TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Views of an Object","").setPosition([-3,0,0])
        p11=cvo.CVO().CreateCVO("Front View","").setPosition([0,2.5,0])
        p12=cvo.CVO().CreateCVO("Top View","").setPosition([3,0,0])
        p13=cvo.CVO().CreateCVO("Side View","").setPosition([0,-2.5,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

        cuboid = Cube()
        cuboid.stretch(2, 0)  # stretch along x-axis
        cuboid.stretch(1, 1)  # normal along y-axis
        cuboid.stretch(0.5, 2)  # compress along z-axis

        cuboid.set_color_by_gradient(BLUE, GREEN, RED)
        faces = cuboid.family_members_with_points()
        faces[0].set_fill(GREEN, opacity=0.95)    # front face
        faces[1].set_fill(BLUE, opacity=0)  # back face
        faces[2].set_fill(RED, opacity=0.95)   # right face
        faces[3].set_fill(ORANGE, opacity=0) # left face
        faces[4].set_fill(YELLOW, opacity=0.95) # top face
        faces[5].set_fill(PURPLE, opacity=0) # bottom face

        # Rotate and position the cuboid to show three visible sides
        # axis=up--along y axis
        # axis=out--along z axis
        cuboid.rotate(-20 * DEGREES, axis=UP)
        cuboid.rotate(330 * DEGREES, axis=RIGHT)
        cuboid.move_to(ORIGIN).shift(RIGHT*3)

        # Add cuboid to the scene
        self.add(cuboid)
        self.wait(2)
        front = Rectangle(width=4, height=2).set_fill(GREEN, opacity=0.95)
        self.play(Create(front.shift(LEFT*3)))
        text = Text("Front View").next_to(front,UP)
        self.play(FadeIn(text))
        self.wait(2)
        self.play(FadeOut(front,text))
        top = Rectangle(width=4, height=0.75).set_fill(YELLOW, opacity=0.95)
        self.play(Create(top.shift(LEFT*3)))
        text = Text("Top View").next_to(front,UP)
        self.play(FadeIn(text))
        self.wait(2)
        self.play(FadeOut(top,text))
        side = Rectangle(width=0.75, height=2).set_fill(RED, opacity=0.95)
        self.play(Create(side.shift(LEFT*3)))
        text = Text("Side View").next_to(side,UP)
        self.play(FadeIn(text))
        self.wait(2)



        # # Create a 3D cuboid (a box)
        # cuboid = Cube()

        # # Scale to make it a cuboid
        # cuboid.stretch(2, 0)  # stretch along x-axis
        # cuboid.stretch(1, 1)  # normal along y-axis
        # cuboid.stretch(0.5, 2)  # compress along z-axis

        # # Apply different colors to each face of the cuboid
        # cuboid.set_color_by_gradient(BLUE, GREEN, RED)
        # faces = cuboid.family_members_with_points()
        # faces[0].set_fill(RED, opacity=0.25)    # front face
        # faces[1].set_fill(GREEN, opacity=0.25)  # back face
        # faces[2].set_fill(BLUE, opacity=0.25)   # right face
        # faces[3].set_fill(YELLOW, opacity=0.25) # left face
        # faces[4].set_fill(PURPLE, opacity=0.25) # top face
        # faces[5].set_fill(ORANGE, opacity=0.25) # bottom face

        # # Add cuboid to the scene
        # self.add(cuboid)

        # # Show the front view
        # front_view_label = Text("Front View").to_edge(UP)
        # self.play(Write(front_view_label))
        # self.wait(2)
        # self.play(Unwrite(front_view_label))

        # # Rotate cuboid to show the top view
        # self.play(Rotate(cuboid, angle=PI/2, axis=RIGHT))
        # top_view_label = Text("Top View").to_edge(UP)
        # self.play(Write(top_view_label))
        # self.wait(2)
        # self.play(Unwrite(top_view_label))

        # # Rotate cuboid to show the side view
        # self.play(Rotate(cuboid, angle=PI/2, axis=OUT))
        # side_view_label = Text("Side View").to_edge(UP)
        # self.play(Write(side_view_label))
        # self.wait(2)
        # self.play(Unwrite(side_view_label))

        # # Rotate back to the original orientation
        # self.play(Rotate(cuboid, angle=-PI/2, axis=OUT))
        # self.wait(2)
    def SetDeveloperList(self):
        self.DeveloperList="Sindhu"
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="DifferentViews.py"


if __name__ == "__main__":
    from manim import *
    scene = DifferentViews()
    scene.render()