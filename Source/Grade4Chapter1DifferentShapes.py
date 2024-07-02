from manim import *
from AbstractAnim import AbstractAnim
import cvo

class ShapeProperties(AbstractAnim, ThreeDScene):

    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.intro()
        self.fadeOutCurrentScene()
        self.show_2d_shapes()
        self.fadeOutCurrentScene()
        self.circle()
        self.fadeOutCurrentScene()
        self.square()
        self.fadeOutCurrentScene()
        self.rectangle()
        self.fadeOutCurrentScene()
        self.rhombus()
        self.fadeOutCurrentScene()
        self.show_3d_shapes()
        self.fadeOutCurrentScene()
        self.cube()
        self.fadeOutCurrentScene()
        self.Coneanim()
        self.fadeOutCurrentScene()
        self.Cylinderanim()
        self.fadeOutCurrentScene()
        self.Sphereanim()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

    def intro(self):
        self.positionChoice = [[-3, 0, 0], [2, 2, 0], [2, -2, 0]]
        self.isRandom = False
        p10 = cvo.CVO().CreateCVO("Shapes", "")
        p11 = cvo.CVO().CreateCVO("2-Dimensional", "")
        p12 = cvo.CVO().CreateCVO("3-Dimensional", "")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10, p10)
        self.wait(2)

    def show_2d_shapes(self):
        self.positionChoice = [[-3, 0, 0], [3, 0, 0]]
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Shapes", "")
        p11 = cvo.CVO().CreateCVO("2-D Shapes", "")
        p11.extendOname(["Circle", "Square", "Rectangle", "Rhombus"])
        p10.cvolist.append(p11)
        self.construct1(p10, p10)
        self.wait(3)
    
    def circle(self):
        circle = Circle(radius=1, color="#6DC9CD", fill_opacity=0.5, stroke_width=5)
        circle.move_to([-4, 0, 0])

        circle_text = Text("Circle", font="Comic Sans MS", color=LIGHT_PINK, weight=BOLD).next_to(circle, DOWN)

        circle_properties = [
            {"name": "Vertices", "value": "0"},
            {"name": "Edges", "value": "1"},
            {"name": "Faces", "value": "0"}
        ]
        properties_text = self.create_properties_text(circle_properties, circle.get_center() + RIGHT * 4)

        self.play(Create(circle))
        self.play(Write(circle_text))
        self.play(Write(properties_text))
        self.wait(3)

    def square(self):
        square = Square(side_length=2, color="#6DC9CD", fill_opacity=0.5, stroke_width=5)
        square.move_to([-4, 0, 0])

        square_text = Text("Square", font="Comic Sans MS", color=LIGHT_PINK, weight=BOLD).next_to(square, DOWN)

        square_properties = [
            {"name": "Vertices", "value": "4"},
            {"name": "Edges", "value": "4"},
            {"name": "Faces", "value": "1"}
        ]
        properties_text = self.create_properties_text(square_properties, square.get_center() + RIGHT * 4)

        self.play(Create(square))
        self.play(Write(square_text))
        self.play(Write(properties_text))
        self.wait(3)

    def rectangle(self):
        rectangle = Rectangle(width=3, height=1.5, color="#6DC9CD", fill_opacity=0.5, stroke_width=5)
        rectangle.move_to([-4, 0, 0])

        rectangle_text = Text("Rectangle", font="Comic Sans MS", color=LIGHT_PINK, weight=BOLD).next_to(rectangle, DOWN)

        rectangle_properties = [
            {"name": "Vertices", "value": "4"},
            {"name": "Edges", "value": "4"},
            {"name": "Faces", "value": "0"}
        ]
        properties_text = self.create_properties_text(rectangle_properties, rectangle.get_center() + RIGHT * 4)

        self.play(Create(rectangle))
        self.play(Write(rectangle_text))
        self.play(Write(properties_text))
        self.wait(3)

    def rhombus(self):
        rhombus = Polygon(np.array([-1.5, 0, 0]), np.array([0, 1.5, 0]), np.array([1.5, 0, 0]), np.array([0, -1.5, 0]), color="#6DC9CD", fill_opacity=0.5, stroke_width=5)
        rhombus.move_to([-4, 0, 0])

        rhombus_text = Text("Rhombus", font="Comic Sans MS", color=LIGHT_PINK, weight=BOLD).next_to(rhombus, DOWN)

        rhombus_properties = [
            {"name": "Vertices", "value": "4"},
            {"name": "Edges", "value": "4"},
            {"name": "Faces", "value": "0"}
        ]
        properties_text = self.create_properties_text(rhombus_properties, rhombus.get_center() + RIGHT * 4)

        self.play(Create(rhombus))
        self.play(Write(rhombus_text))
        self.play(Write(properties_text))
        self.wait(3)

    def create_properties_text(self, properties, start_position):
        text_lines = []
        for prop in properties:
            line = f"{prop['name']}: {prop['value']}"
            text_lines.append(Text(line, font="Comic Sans MS", font_size=20, color=WHITE))

        text_group = VGroup(*text_lines)
        text_group.arrange(DOWN, aligned_edge=LEFT)
        text_group.next_to(start_position, RIGHT)

        return text_group

    def show_3d_shapes(self):
        self.positionChoice = [[-3, 0, 0], [3, 0, 0]]
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Shapes", "")
        p11 = cvo.CVO().CreateCVO("3-D Shapes", "")
        p11.extendOname(["Cube", "Cuboid", "Cone", "Sphere", "Cylinder"])
        p10.cvolist.append(p11)
        self.construct1(p10, p10)
        self.wait(3)

    def cube(self):
        title = Text("Cube", color=LIGHT_PINK, weight=BOLD)
        title.move_to([0, 3, 0])
        

        cube = Cube(side_length=2, color="#6DC9CD", fill_opacity=0.5, stroke_width=5)
        cube.move_to([-4, 0, 0])


        cube_properties = [
            {"name": "Vertices", "value": "8"},
            {"name": "Edges", "value": "12"},
            {"name": "Faces", "value": "6"}
        ]
        properties_text = self.create_properties_text(cube_properties, cube.get_center() + RIGHT * 4)

        self.play(Create(title))
        self.play(Create(cube))
        self.play(Write(properties_text))
        self.wait(3)

    def Coneanim(self):
        # Title
        title = Text("Cone", color=LIGHT_PINK, weight=BOLD)
        title.move_to([0, 3, 0])
        
        # Create the cone
        cone = Polygon(
            [0, 2, 0],  # Top point of the cone
            [-2, -1, 0],  # Bottom left point
            [2, -1, 0],  # Bottom right point
            color=WHITE
        )
       
        # Create the horizontal ellipse (base)
        base = Ellipse(width=4, height=0.4, color=WHITE).shift(DOWN*1.5)
        
        # Create the vertical line representing the height
        height_line = Line(start=[0, 2, 0], end=[0, -1, 0], color=WHITE)
        
        # Create the small filled circle at the center of the base
        center_dot = Dot(point=[0, -1, 0], color=WHITE)
        
        # Create the labels "h", "l", and "r"
        height_label = MathTex("h", color=WHITE)
        height_label.next_to(height_line, LEFT)
        
        slant_label = MathTex("l", color=WHITE)
        slant_label.move_to([1, 1, 0])
        
        radius_label = MathTex("r", color=WHITE)
        radius_label.move_to([1, -1.5, 0])
        
        # Position elements
        cone.shift(DOWN*0.5)
        height_line.shift(DOWN*0.5)
        center_dot.shift(DOWN*0.5)
        height_label.shift(DOWN*0.5)
        slant_label.shift(DOWN*0.5)
        radius_label.shift(DOWN*0.5)


        cone_properties = [
            {"name": "Vertices", "value": "1"},
            {"name": "Edges", "value": "1"},
            {"name": "Faces", "value": "1"}
        ]
        properties_text = self.create_properties_text(cone_properties, cone.get_center() + RIGHT * 4)

       
        # Play animations
        self.play(Create(title))
        self.play(Create(cone))
        self.play(Create(base))
        self.play(Create(height_line))
        self.play(Create(center_dot))
        self.play(Write(height_label))
        self.play(Write(slant_label))
        self.play(Write(radius_label))
        self.play(Write(properties_text))
        self.wait(3)
        
        # Final animation
        self.wait(4)

   
    def Cylinderanim(self):
         # Create the text
        t1 = Text("Cylinder", color=LIGHT_PINK, weight=BOLD)
        t1.move_to([0, 2.7, 0])

        # Create base and top ellipses
        base = Ellipse(color=WHITE)
        top = Ellipse(color=WHITE)

        # Set the angle for the ellipses
        angle = PI / 4  # 45 degrees in radians
        base.rotate(angle, axis=RIGHT)
        top.rotate(angle, axis=RIGHT)

        # Create the lines
        line1 = Line(start=[-1, -1.5, 0], end=[-1, 1.5, 0],color=WHITE)
        line2 = Line(start=[1, -1.5, 0], end=[1, 1.5, 0],color=WHITE)

        # Position the base and top
        base.move_to([0, -1.5, 0])
        top.move_to([0, 1.5, 0])
         # Create labels
        l_label = Text("r", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        l_label.next_to(base.get_edge_center(DOWN), DOWN)
        h_label = Text("h", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        h_label.next_to(base.get_edge_center(RIGHT) + RIGHT * 0.5, UP * 2)

        # Play animations
        self.play(Write(t1))
        self.play(Write(base))
        self.play(Write(top))
        self.play(Write(line1))
        self.play(Write(line2))
        self.play(Write(l_label), Write(h_label))


        cylinder_properties = [
            {"name": "Vertices", "value": "0"},
            {"name": "Edges", "value": "2"},
            {"name": "Faces", "value": "3"}
        ]
        properties_text = self.create_properties_text(cylinder_properties, RIGHT * 4)

        self.play(Write(properties_text))
        self.wait(4)


    def Sphereanim(self):
        # Title
        title = Text("Sphere", color=LIGHT_PINK, weight=BOLD)
        title.move_to([0, 3, 0])
        
         # Create the circle representing the sphere
        sphere = Circle(radius=2, color=WHITE)
        
        # Create the horizontal ellipse (equator)
        equator = Ellipse(width=4, height=0.4, color=WHITE).shift(DOWN*0.5)
        
        # Create the dashed line representing the radius
        radius_line_horizontal = DashedLine(start=[0, 0, 0], end=[2, 0, 0], color=WHITE).shift(DOWN*0.5)
        
        # Create the small filled circle at the center of the horizontal ellipse
        center_dot = Dot(point=[0, 0, 0], color=WHITE).shift(DOWN*0.5)
        
        # Create the label "r"
        radius_label_horizontal = MathTex("r", color=WHITE)
        radius_label_horizontal.next_to(radius_line_horizontal, UP*0.1)
        
        # Position elements
        sphere.shift(DOWN*0.5)
        radius_label_horizontal.shift(DOWN*0.5)
        
        # Play animations
        self.play(Create(title))
        self.play(Create(sphere))
        self.play(Create(equator))
        self.play(Create(radius_line_horizontal))
        self.play(Create(center_dot))
        self.play(Write(radius_label_horizontal))
        
        # Final animation
        self.wait(4)


        sphere_properties = [
            {"name": "Vertices", "value": "0"},
            {"name": "Edges", "value": "0"},
            {"name": "Faces", "value": "1"}
        ]
        properties_text = self.create_properties_text(sphere_properties, sphere.get_center() + RIGHT * 4)

        self.play(Create(sphere))
        self.play(Write(properties_text))
        self.wait(3)    
    
    def SetDeveloperList(self):  
        self.DeveloperList="Shanmukha Priya"
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade4Chapter1DifferentShapes.py"

if __name__ == "__main__":
    scene = ShapeProperties()
    scene.render()