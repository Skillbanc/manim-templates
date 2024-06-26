from manim import *
from AbstractAnim import AbstractAnim
import cvo

class ShapesWithText(AbstractAnim, ThreeDScene):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.show_2d_shapes()
        self.fadeOutCurrentScene()
        self.triangle()
        self.fadeOutCurrentScene()
        self.circle()
        self.fadeOutCurrentScene()
        self.square()
        self.fadeOutCurrentScene()
        self.rectangle()
        self.fadeOutCurrentScene()
        self.show_3d_shapes()
        self.fadeOutCurrentScene()
        self.threeviews()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

    

    def show_2d_shapes(self):
        self.positionChoice = [[-3, 0, 0], [3, 0, 0]]
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Shapes", "")
        p11 = cvo.CVO().CreateCVO("2-D Shapes", "")
        p11.extendOname(["Circle", "Square", "Rectangle", "Rectangle"])
        p10.cvolist.append(p11)
        self.construct1(p10, p10)
        self.wait(3)


    def triangle(self):
        self.positionChoice = [[-3, 0, 0], [3, 0, 0]]
        self.isRandom = False
        p10 = cvo.CVO().CreateCVO("Shapes", "Triangle")
        p11 = cvo.CVO().CreateCVO("Properties", "")
        p11.extendOname(["Three sides", "Three vertices", "Three angles", "Sum of angles is 180 degrees"])
        p10.cvolist.append(p11)
        self.construct1(p10, p10)
        self.wait(4)
        self.fadeOutCurrentScene()

        # Create shapes
        Title = Text("Triangle").to_edge(UP)
        triangle = Polygon(np.array([-3, -1, 0]), np.array([-2, 1, 0]), np.array([-1, -1, 0]), color=BLUE, fill_opacity=0.5).shift(LEFT*3)
        text_triangle = Text("A triangle is a polygon with three edges and three vertices.\n"
                             "It is one of the basic shapes in geometry.\n"
                             "Triangles can be classified by their sides(equilateral, isosceles, scalene)\n"
                             "and by their angles (acute, right, obtuse).",
                             font="Arial", font_size=20).next_to(triangle, RIGHT)
        self.play(Write(Title), Write(triangle), Write(text_triangle))
        self.wait(4)

    def circle(self):
        self.positionChoice = [[-3, 0, 0], [3, 0, 0]]
        self.isRandom = False
        p10 = cvo.CVO().CreateCVO("Shapes", "Circle")
        p11 = cvo.CVO().CreateCVO("Properties", "")
        p11.extendOname(["Round shape", "Infinite points equidistant from the center", "No edges", "360 degrees"])
        p10.cvolist.append(p11)
        self.construct1(p10, p10)
        self.wait(2)
        self.fadeOutCurrentScene()


        Title = Text("Circle").to_edge(UP)
        circle = Circle(radius=1, color=RED, fill_opacity=0.5).shift(LEFT*4)
        text_circle = Text("A circle is a shape consisting of all points in a plane that are\n"
                           "at a given distance from a given point, the center.\n"
                           "It is a type of ellipse and one of the most fundamental shapes in geometry.",
                           font="Arial", font_size=20).next_to(circle, RIGHT)
        self.play(Write(Title), Write(circle), Write(text_circle))
        self.wait(4)

    def square(self):
        self.positionChoice = [[-3, 0, 0], [3, 0, 0]]
        self.isRandom = False
        p10 = cvo.CVO().CreateCVO("Shapes", "Square")
        p11 = cvo.CVO().CreateCVO("Properties", "")
        p11.extendOname(["Four equal sides", "Four right angles", "Opposite sides are parallel", "Diagonals bisect each other"])
        p10.cvolist.append(p11)
        self.construct1(p10, p10)
        self.wait(2)
        self.fadeOutCurrentScene()


        Title = Text("Square").to_edge(UP)
        square = Square(side_length=2, color=GREEN, fill_opacity=0.5).shift(LEFT*4)
        text_square = Text("A square is a regular quadrilateral, which means that it has four equal sides\n"
                           "and four equal angles (90-degree angles, or right angles).\n"
                           "All squares are rectangles, but not all rectangles are squares.",
                           font="Arial", font_size=20).next_to(square, RIGHT)
        self.play(Write(Title), Write(square), Write(text_square))
        self.wait(4)

    def rectangle(self):
        self.positionChoice = [[-3, 0, 0], [3, 0, 0]]
        self.isRandom = False
        p10 = cvo.CVO().CreateCVO("Shapes", "Rectangle")
        p11 = cvo.CVO().CreateCVO("Properties", "")
        p11.extendOname(["Four sides", "Opposite sides are equal", "Four right angles", "Diagonals bisect each other"])
        p10.cvolist.append(p11)
        self.construct1(p10, p10)
        self.wait(2)
        self.fadeOutCurrentScene()


        Title = Text("Rectangle").to_edge(UP)
        rectangle = Rectangle(height=1.5, width=2.5, color=YELLOW, fill_opacity=0.5).shift(LEFT*4)
        text_rectangle = Text("A rectangle is a quadrilateral with opposite sides that are equal and\n"
                              "four right angles.\n"
                              "It is a type of parallelogram and one of the most common shapes\n"
                               "in geometry.",
                              font="Arial", font_size=20).next_to(rectangle, RIGHT)
        self.play(Write(Title), Write(rectangle), Write(text_rectangle))
        self.wait(4)

    def show_3d_shapes(self):
        self.positionChoice = [[-3, 0, 0], [3, 0, 0]]
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Shapes", "")
        p11 = cvo.CVO().CreateCVO("3-D Shapes", "")
        p11.extendOname(["Cube", "Cuboid", "Cone", "Sphere", "Cylinder"])
        p10.cvolist.append(p11)
        self.construct1(p10, p10)
        self.wait(3)


    def threeviews(self):
        self.positionChoice = [[-3, 0, 0],[3, 0, 0]]
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("3D-Shapes", "")
        p11 = cvo.CVO().CreateCVO("3 Views", "")
        p11.extendOname(["Front View", "Side View", "Top View"])
        p10.cvolist.append(p11)
        self.construct1(p10, p10)
        self.wait(3)
        self.fadeOutCurrentScene()
    
        Title = Text("Cube").to_edge(UP)
        self.add(Title)
    
        # Create the cube
        cube = Cube(side_length=2, fill_opacity=0.5, color=BLUE)
        cube.move_to([-4, 2, 0])
        self.add(cube)

        # Front view
        front_view = Cube(side_length=1, fill_opacity=0.5, color=BLUE)
        front_view_label = Text("Front View").next_to(front_view, DOWN)

        # Side view
        side_view = Cube(side_length=1, fill_opacity=0.5, color=BLUE).rotate(PI/2, axis=UP)
        side_view_label = Text("Side View").next_to(side_view, DOWN)

        # Top view
        top_view = Cube(side_length=1, fill_opacity=0.5, color=BLUE).rotate(-PI/2, axis=RIGHT)
        top_view_label = Text("Top View").next_to(top_view, DOWN)

        # Arrange the views
        front_view_group = VGroup(front_view, front_view_label).arrange(DOWN, buff=0.2).next_to(cube,RIGHT*2,buff=2)
        side_view_group = VGroup(side_view, side_view_label).arrange(DOWN, buff=0.2).next_to(cube, DOWN, buff=2)
        top_view_group = VGroup(top_view, top_view_label).arrange(DOWN, buff=0.2).next_to(side_view_group, RIGHT*2, buff=2)

        # Add all views to the scene
        self.add(front_view_group, side_view_group, top_view_group)
        self.wait(4)

    def SetDeveloperList(self):  
        self.DeveloperList="Shanmukha Priya"
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade3CH1SHAPESANDSPATIALUNDERSTANDING.py"

if __name__ == "__main__":
    scene = ShapesWithText()
    scene.render()
