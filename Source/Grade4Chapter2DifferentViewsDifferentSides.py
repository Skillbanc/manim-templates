from AbstractAnim import AbstractAnim
import cvo
from manim import ThreeDScene
from manim import *

class DifferentViews(AbstractAnim):
    def construct(self):
        # self.RenderSkillbancLogo()
        # self.Views()
        # self.fadeOutCurrentScene()
        # self.Sides()
        # self.fadeOutCurrentScene()
        # self.Cuboidscene()
        # self.fadeOutCurrentScene()
        # self.GithubSourceCodeReference()
        self.test()

    def Views(self):
        self.angleChoice=[TAU/4,TAU/4,TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Views of an Object","").setPosition([-3,0,0])
        p11=cvo.CVO().CreateCVO("Front View","").setPosition([0,2.5,0])
        p12=cvo.CVO().CreateCVO("Back View","").setPosition([3,0,0])
        p13=cvo.CVO().CreateCVO("Top View","").setPosition([0,-2.5,0])
        p14=cvo.CVO().CreateCVO("Bottom View","").setPosition([0,0,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        self.construct1(p10,p10)
    
    def Sides(self):
        self.angleChoice=[TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Sides of an Object","").setPosition([-3,0,0])
        p11=cvo.CVO().CreateCVO("Right Side","").setPosition([0,2.5,0])
        p12=cvo.CVO().CreateCVO("Left Side","").setPosition([0,-2.5,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)

    def Cuboidscene(self):
        title = Text("Views of Cuboid",font_size=40).to_edge(UP)
        self.play(Write(title))
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
        text = Text("Front View",font_size=38).next_to(front,UP)
        self.play(FadeIn(text))
        self.wait(2)
        self.play(FadeOut(front,text))
        top = Rectangle(width=4, height=0.75).set_fill(YELLOW, opacity=0.95)
        self.play(Create(top.shift(LEFT*3)))
        text = Text("Top View",font_size=38).next_to(front,UP)
        self.play(FadeIn(text))
        self.wait(2)
        self.play(FadeOut(top,text))
        side = Rectangle(width=0.75, height=2).set_fill(RED, opacity=0.95)
        self.play(Create(side.shift(LEFT*3)))
        text = Text("Side View",font_size=38).next_to(side,UP)
        self.play(FadeIn(text))
        self.wait(2)

    def show_views(self, shape, shape_name):
        # Positions to place shapes for different views
        positions = {
            "Front": ORIGIN,
            "Side": 3 * RIGHT,
            "Top": 3 * LEFT,
        }

        # Angles to rotate shapes for different views
        rotations = {
            "Front": [0, 0, 0],
            "Side": [0, -PI / 2, 0],
            "Top": [PI / 2, 0, 0],
        }

        # Create and animate the different views
        for label, pos in positions.items():
            rotated_shape = shape.copy()
            rotated_shape.rotate(rotations[label][0], axis=RIGHT)
            rotated_shape.rotate(rotations[label][1], axis=UP)
            rotated_shape.rotate(rotations[label][2], axis=OUT)

            shape_label = Text(f"{shape_name} - {label} View", font_size=24).next_to(rotated_shape, UP)
            self.play(FadeIn(rotated_shape), Write(shape_label))
            self.wait(2)
            self.play(FadeOut(rotated_shape), FadeOut(shape_label))
            self.wait(1)

    def test(self):
        # Create shapes
        cube = Cube()
        cylinder = Cylinder()
        cone = Cone()

        # Show views for each shape
        self.show_views(cube, "Cube")
        self.show_views(cylinder, "Cylinder")
        self.show_views(cone, "Cone")

# To render the video, you would use the following command in your terminal:
# manim -pql different_views.py DifferentViews



    def SetDeveloperList(self):
        self.DeveloperList="Sindhu"
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade4Chapter2DifferentViewsDifferentSides.py"


if __name__ == "__main__":
    from manim import *
    scene = DifferentViews()
    scene.render()