from AbstractAnim import AbstractAnim
import cvo
import numpy as np
from manim import *

class DifferentViews(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.Views()
        self.fadeOutCurrentScene()
        self.Cuboidscene()
        self.fadeOutCurrentScene()
        self.Cubescene()
        self.fadeOutCurrentScene()
        self.House()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

    def Views(self):
        self.angleChoice=[TAU/4,TAU/4,TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Views of an Object","").setPosition([-3,0,0])
        p11=cvo.CVO().CreateCVO("Front View","").setPosition([0,2.5,0])
        p12=cvo.CVO().CreateCVO("Side View","").setPosition([3,0,0])
        p13=cvo.CVO().CreateCVO("Top View","").setPosition([0,-2.5,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
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

    def Cubescene(self):
        title = Text("Views of Cube",font_size=40).to_edge(UP)
        self.play(Write(title))
        cube = Cube()

        cube.set_color_by_gradient(BLUE, GREEN, RED)
        faces = cube.family_members_with_points()
        faces[0].set_fill(GREEN, opacity=0.95)    # front face
        faces[1].set_fill(BLUE, opacity=0)  # back face
        faces[2].set_fill(RED, opacity=0.95)   # right face
        faces[3].set_fill(ORANGE, opacity=0) # left face
        faces[4].set_fill(YELLOW, opacity=0.95) # top face
        faces[5].set_fill(PURPLE, opacity=0) # bottom face

        # Rotate and position the cuboid to show three visible sides
        # axis=up--along y axis
        # axis=out--along z axis
        cube.rotate(-20 * DEGREES, axis=UP)
        cube.rotate(330 * DEGREES, axis=RIGHT)
        cube.move_to(ORIGIN).shift(RIGHT*3)

        # Add cuboid to the scene
        self.add(cube)
        self.wait(2)
        front = Rectangle(width=2, height=2).set_fill(GREEN, opacity=0.95)
        self.play(Create(front.shift(LEFT*3)))
        text = Text("Front View",font_size=38).next_to(front,UP)
        self.play(FadeIn(text))
        self.wait(2)
        self.play(FadeOut(front,text))
        top = Rectangle(width=2, height=2).set_fill(YELLOW, opacity=0.95)
        self.play(Create(top.shift(LEFT*3)))
        text = Text("Top View",font_size=38).next_to(front,UP)
        self.play(FadeIn(text))
        self.wait(2)
        self.play(FadeOut(top,text))
        side = Rectangle(width=2, height=2).set_fill(RED, opacity=0.95)
        self.play(Create(side.shift(LEFT*3)))
        text = Text("Side View",font_size=38).next_to(side,UP)
        self.play(FadeIn(text))
        self.wait(2)

    def House(self):
        title = Text("Views of a House",font_size=42)
        self.play(FadeIn(title))
        self.wait(2)
        self.play(FadeOut(title))
        self.create_house_front_view()
        self.create_house_front_view()
        self.wait(2)
        self.fadeOutCurrentScene()

        self.create_house_side_view()
        self.wait(2)

        self.fadeOutCurrentScene()
        self.create_house_top_view()
        self.wait(2)
    def create_house_front_view(self):
        house_body = Rectangle(width=4, height=3)
        house_body.set_fill(BLUE, opacity=0.5)
        
        door = Rectangle(width=1, height=1.5)
        door.set_fill(BLACK, opacity=1)
        door.next_to(house_body, DOWN, buff=-1.5)

        roof_points = [
            np.array([-2.5, 1.5, 0]),  # Bottom left
            np.array([2.5, 1.5, 0]),   # Bottom right
            np.array([1.5, 3, 0]),     # Top right
            np.array([-1.5, 3, 0])     # Top left
        ]
        
        roof = Polygon(*roof_points)
        roof.set_fill(RED, opacity=0.5)
        roof.next_to(house_body, UP, buff=0)

        roof_lines = self.create_roof_lines(roof_points)
        
        text = Text("Front View", font_size=36).set_color(YELLOW).shift(DOWN*2.5)
        
        self.play(Create(house_body), Create(roof), Create(door), Create(roof_lines))
        self.play(Write(text))
    def create_house_side_view(self):
        house_body = Rectangle(width=3, height=3)
        house_body.set_fill(BLUE, opacity=0.5)
        
        window = Square(side_length=1)
        window.set_fill(BLACK, opacity=1)
        window.next_to(house_body, DOWN, buff=-2.5)

        roof_points = [
            np.array([-2, 1.5, 0]),  # Bottom left
            np.array([2, 1.5, 0]),   # Bottom right
            np.array([0, 3, 0]),     # Top right
            np.array([0, 3, 0])      # Top left
        ]
        
        roof = Polygon(*roof_points)
        roof.set_fill(RED, opacity=0.5)
        roof.next_to(house_body, UP, buff=0)

        roof_lines = self.create_roof_lines(roof_points)

        text = Text("Side View", font_size=36).set_color(YELLOW).shift(DOWN*2.5)

        self.play(Create(house_body), Create(roof), Create(window), Create(roof_lines))
        self.play(Write(text))

    def create_roof_lines(self, roof_points):
        roof_lines = VGroup()
        num_lines = 5
        for i in range(num_lines):
            alpha = i / (num_lines - 1)
            start = (1 - alpha) * roof_points[0] + alpha * roof_points[3]
            end = (1 - alpha) * roof_points[1] + alpha * roof_points[2]
            line = Line(start, end)
            roof_lines.add(line)
        return roof_lines

    def create_house_top_view(self):
        rectangle = Rectangle(width=4, height=2, color=RED)
        rectangle.set_fill(RED, opacity=0.5)
        # Add horizontal lines inside the rectangle
        num_lines = 5
        line_spacing = rectangle.height / (num_lines + 1)
        
        lines = VGroup(*[
            Line(
                start=rectangle.get_left() + UP * (rectangle.get_bottom()[1] + i * line_spacing),
                end=rectangle.get_right() + UP * (rectangle.get_bottom()[1] + i * line_spacing),
                color=WHITE
            )
            for i in range(1, num_lines + 1)
        ])
        line = Line(rectangle.get_left()+UP*0.1,rectangle.get_right()+UP*0.1)
        text = Text("Top View", font_size=36).set_color(YELLOW).shift(DOWN*2)
    
        self.play(Create(rectangle),FadeIn(lines),FadeIn(line))
        self.play(Write(text))

    def SetDeveloperList(self):
        self.DeveloperList="A. Sindhu sri"
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade4Chapter2DifferentViewsDifferentSides.py"


if __name__ == "__main__":
    from manim import *
    scene = DifferentViews()
    scene.render()