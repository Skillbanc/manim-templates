import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class Shapesanim(AbstractAnim):

    
    def construct(self):
        self.RenderSkillbancLogo()
        self.Shapes()
        self.Components()
        self.ExampleCube()
        self.Nets()
        self.Sketches()
        self.Oblique()
        self.Isometric()
        self.Shadows()
        self.Shadow1()
        self.Shadow2()
        self.GithubSourceCodeReference()
    
        # self.fadeOut()
        # self.constructDataByJSON()
        # self.fadeOut()
    

    def Shapes(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Shapes", "").setPosition([-3,0,0])
        p11=cvo.CVO().CreateCVO("3DShapes", "").setPosition([2,2,0]).setangle(-TAU/4)
        
        p12=cvo.CVO().CreateCVO("2DShapes", "").setPosition([2,-2,0]).setangle(-TAU/4)
        
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
       
        
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Components(self):

        self.isRandom = False
        p10=cvo.CVO().CreateCVO("3DShapes", "").setPosition([-6,0,0])
        p11=cvo.CVO().CreateCVO("Components", "").setPosition([-3,0,0]).setangle(-TAU/4)
        p12=cvo.CVO().CreateCVO("Faces", "").setPosition([1,2.5,0]).setangle(-TAU/4)
        p13=cvo.CVO().CreateCVO("Edges", "").setPosition([2,0,0]).setangle(-TAU/4)
        p14=cvo.CVO().CreateCVO("Vertices", "").setPosition([1,-2.5,0]).setangle(-TAU/4)

        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
        p11.cvolist.append(p14)
        
        
        

        self.setNumberOfCirclePositions(6)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def ExampleCube(self):
        
        base_vertices = [
            [-3, -0.75, 0], [-1.25, -0.75, 0], [0, -1.25, 0], [-1.75, -1.25, 0], [-3, -0.75, 0]
        ]
        top_vertices = [
            [-3, 0.5, 0], [-1.25, 0.5, 0], [0, 0, 0], [-1.75, 0, 0], [-3, 0.5, 0]
        ]
        face1_vertices = [
            [-3.1, 0.5, 0], [-3.1, -0.75, 0], [-1.75, -1.25, 0], [-1.75, 0, 0], [-3, 0.5, 0]
        ]
        face2_vertices = [
            [-3.1, 0.5, 0], [-1.25, 0.5, 0], [-1.25, -0.75, 0], [-3.1, -0.75, 0], [-3.1, 0.5, 0]
        ]
        face3_vertices = [
            [-1.25, 0.5, 0], [-1.25, -0.75, 0], [0.1, -1.25, 0], [0.1, 0, 0], [-1.25, 0.5, 0]
        ]
        face4_vertices = [
            [-1.75, 0, 0], [-1.75, -1.25, 0], [0.1, -1.25, 0], [0.1, 0, 0], [-1.75, 0, 0]
        ]

        # Create the cuboid faces with different colors
        base = Polygon(*base_vertices, color=BLUE, fill_opacity=0.5, stroke_width=5)
        top = Polygon(*top_vertices, color=YELLOW, fill_opacity=0.5, stroke_width=5)
        face1 = Polygon(*face1_vertices, color=BLUE, fill_opacity=0.2, stroke_width=5)
        face2 = Polygon(*face2_vertices, color=BLUE, fill_opacity=0.2, stroke_width=5)
        face3 = Polygon(*face3_vertices, color=BLUE, fill_opacity=0.2, stroke_width=5)
        face4 = Polygon(*face4_vertices, color=BLUE, fill_opacity=0.2, stroke_width=5)

        # Animate the creation of the cuboid faces
        self.play(Create(base))
        self.play(Create(top))
        self.play(Create(face1))
        self.play(Create(face2))
        self.play(Create(face3))
        self.play(Create(face4))

        # Add text indicating 3D Shape - Cuboid
        t1 = Text( "Cuboid", font_size=45, color=PURPLE)
        t1.move_to([0, 2.7, 0])
        self.play(Write(t1))

        # Highlight the vertices with dots
        vertices = [
            Dot(point=vert, color=RED, radius=0.07) for vert in 
            [(-3.1, -0.75, 0), (-1.25, -0.75, 0), [0.1, -1.25, 0], [-1.75, -1.25, 0],
             [-3.1, 0.5, 0], [-1.25, 0.5, 0], [0.1, 0, 0], [-1.75, 0, 0]]
        ]
        self.play(*[GrowFromCenter(vert) for vert in vertices])

        # Highlight the edges with normal lines
        edges = [
            Line(start=[-3.1, -0.75, 0], end=[-1.25, -0.75, 0], color=WHITE),
            Line(start=[-1.25, -0.75, 0], end=[0.1, -1.25, 0], color=WHITE),
            Line(start=[0.1, -1.25, 0], end=[-1.75, -1.25, 0], color=WHITE),
            Line(start=[-1.75, -1.25, 0], end=[-3.1, -0.75, 0], color=WHITE),
            Line(start=[-3.1, 0.5, 0], end=[-1.25, 0.5, 0], color=WHITE),
            Line(start=[-1.25, 0.5, 0], end=[0.1, 0, 0], color=WHITE),
            Line(start=[0.1, 0, 0], end=[-1.75, 0, 0], color=WHITE),
            Line(start=[-1.75, 0, 0], end=[-3.1, 0.5, 0], color=WHITE),
            Line(start=[-3.1, -0.75, 0], end=[-3.1, 0.5, 0], color=WHITE),
            Line(start=[-1.25, -0.75, 0], end=[-1.25, 0.5, 0], color=WHITE),
            Line(start=[0.1, -1.25, 0], end=[0.1, 0, 0], color=WHITE),
            Line(start=[-1.75, -1.25, 0], end=[-1.75, 0, 0], color=WHITE),
        ]
        self.play(*[Create(edge) for edge in edges])

        # Annotate vertices, edges, and faces
        a1 = Line(start=[-1.25, 0.5, 0], end=[0.2, 1, 0], color=RED).add_tip(at_start=True)
        a2 = Line(start=[0, 0, 0], end=[0.2, 1, 0], color=RED).add_tip(at_start=True)
        
        t2 = Text("Vertices = 8", color="RED", font_size=24)
        t2.move_to([0.2, 1.3, 0])

        a3 = Line(start=[-2.5, -1, 0], end=[-3, -2, 0]).add_tip(at_start=True)
        a4 = Line(start=[-1, -1.25, 0], end=[-3, -2, 0]).add_tip(at_start=True)
        
        t3 = Text("Edges = 12", color="WHITE", font_size=24)
        t3.move_to([-3, -2.2, 0])

        a5 = Line(start=[-1.6, 0.3, 0], end=[-2.5, 1.2, 0],color=YELLOW).add_tip(at_start=True)
        
        t4 = Text("Faces = 6", color=YELLOW, font_size=24)
        t4.move_to([-2.5, 1.3, 0])

        self.play(Write(a1), Write(a2), Write(t2))
        self.play(Write(a3), Write(a4), Write(t3))
        self.play(Write(a5), Write(t4))
        self.wait(2)
        self.fadeOutCurrentScene()

    def Nets(self):
        title = Text("Nets of 3D Shapes", font_size=40, color=BLUE)
        title.to_edge(UP)
        colors = [BLUE, BLUE, BLUE, BLUE, BLUE, BLUE]

        self.play(Write(title))
        self.wait(1)

        # Create the net of the cube
        net = VGroup(
            Square(side_length=1.5, fill_opacity=0.5, fill_color=colors[0]).shift(UP*2),
            Square(side_length=1.5, fill_opacity=0.5, fill_color=colors[1]).shift(LEFT*1.5 + UP*0.5),
            Square(side_length=1.5, fill_opacity=0.5, fill_color=colors[2]).shift(UP*0.5),
            Square(side_length=1.5, fill_opacity=0.5, fill_color=colors[3]).shift(RIGHT*1.5 + UP*0.5),
            Square(side_length=1.5, fill_opacity=0.5, fill_color=colors[4]).shift(DOWN*1.5 + UP*0.5),
            Square(side_length=1.5, fill_opacity=0.5, fill_color=colors[5]).shift(DOWN*3 + UP*0.5)
        )

        self.play(FadeIn(net))
        self.wait(2)

        # Fold the net into a cube
        folds = [
            # Fold the top face down
            (0, DOWN, PI / 2),
            # Fold the left face to the right
            (1, RIGHT, PI / 2),
            # Fold the right face to the left
            (3, LEFT, PI / 2),
            # Fold the bottom face up
            (4, UP, PI / 2),
            # Fold the far bottom face up
            (5, UP, PI / 2)
        ]

        for index, direction, angle in folds:
            face = net[index]
            axis = np.cross([0, 0, 1], direction)
            self.play(Rotate(face, angle, axis=axis, about_point=face.get_center() + direction * 0.75))
            self.wait(1)

        # Adjust the final face to align properly
        self.play(Rotate(net[5], -PI / 2, axis=RIGHT, about_point=net[5].get_center() + UP*1.5))

        self.wait(2)
        self.play(FadeOut(net))
        self.wait(2)
        self.fadeOutCurrentScene()



    def Sketches(self):
       self.isRandom = False
       p10=cvo.CVO().CreateCVO("Sketches","").setPosition([-6,0,0])
       p11=cvo.CVO().CreateCVO("Oblique Sketches", "").setPosition([-3,1.5,0]).setangle(-TAU/4)
       p12=cvo.CVO().CreateCVO("Isometric Sketches", "").setPosition([-3,-1.5,0]).setangle(-TAU/4)
       p13=cvo.CVO().CreateCVO("Property", "Focuses on face of object").setPosition([2,2.5,0]).setangle(-TAU/4)
       p14=cvo.CVO().CreateCVO("Property", "45 degree for lines").setPosition([4.5,1.5,0]).setangle(-TAU/4)
       p15=cvo.CVO().CreateCVO("Property", "Focuses on edge of object").setPosition([4.5,-1.5,0]).setangle(-TAU/4)
       p16=cvo.CVO().CreateCVO("Property", "lines are drawn at 30 degree").setPosition([2,-2.5,0]).setangle(-TAU/4)
      
       p10.cvolist.append(p11)
       p10.cvolist.append(p12)
       p11.cvolist.append(p13)
       p11.cvolist.append(p14)
       p12.cvolist.append(p16)
       p12.cvolist.append(p15)
       
       p13.setcircleradius(1.5)
       p14.setcircleradius(1.5)
       p15.setcircleradius(1.5)
       p16.setcircleradius(1.5)
       
       self.setNumberOfCirclePositions(5)
       self.construct1(p10,p10)
       self.fadeOutCurrentScene()

    def Oblique(self):

        title = Text("Oblique Sketch of Cube", font_size=40, color=BLUE)
        self.play(Write(title))
        self.fadeOutCurrentScene()

        grid = NumberPlane(
            x_range=[-8, 8, 1],
            y_range=[-5, 5, 1],
            axis_config={"color": RED},
            background_line_style={
                "stroke_color": RED_D,
                "stroke_width": 1,
                "stroke_opacity": 0.6,
            }
        )
        
        
        self.play(Create(grid))
        self.wait(2)
        
        vertices = [
            [0, 0, 0],  # A
            [2, 0, 0],  # B
            [2, 2, 0],  # C
            [0, 2, 0],  # D
            [1, 1, 2],  # E
            [3, 1, 2],  # F
            [3, 3, 2],  # G
            [1, 3, 2],  # H
        ]
        
        # Convert vertices to 3D coordinates
        points = [np.array(point) for point in vertices]

        # Create the edges of the cube
        edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),  # Base square
            (4, 5), (5, 6), (6, 7), (7, 4),  # Top square
            (0, 4), (1, 5), (2, 6), (3, 7)   # Vertical edges
        ]

        # Create lines for each edge
        lines = [Line(points[start], points[end]) for start, end in edges]

        # Animate drawing the cube step by step
        for line in lines:
            self.play(Create(line))
            self.wait(0.5)  # Pause between drawing each line

        # Add labels for each vertex (optional)
        labels = ["", "", "", "", "", "", "", ""]
        for label, point in zip(labels, points):
            self.add(Text(label).scale(0.5).next_to(point, direction=UP,))
        labels = ["A", "", "", "D", "E", "", "", "H"]
        for label, point in zip(labels, points):
            self.add(Text(label).scale(0.5).next_to(point, direction=LEFT))
        labels = ["", "B", "C", "", "", "F", "G", ""]
        for label, point in zip(labels, points):
            self.add(Text(label).scale(0.5).next_to(point, direction=RIGHT))
        self.wait(2)
        self.wait(2)

        
        self.wait(2)
        self.fadeOutCurrentScene()

    def Isometric(self):

        title = Text("Isometric Sketch of Cube", font_size=40, color=BLUE)
        self.play(Write(title))
        self.fadeOutCurrentScene()


        grid_size = 12  # Size of the grid
        spacing = 1  # Adjusted distance between the dots

        # Group to hold the dots
        dots = VGroup()
        for x in range(-grid_size, grid_size + 1):
            for y in range(-grid_size, grid_size + 1):
                iso_x = (x - y) * spacing * np.sqrt(3) / 2
                iso_y = (x + y) * spacing / 2
                dot = Dot(point=[iso_x, iso_y, 0], radius=0.05)
                dots.add(dot)
        self.play(Create(dots))

        # Define a function to convert 3D points to isometric 2D points
        def iso_point(x, y, z):
            # Isometric projection transformation
            iso_x = (x - y) * np.sqrt(3) / 2
            iso_y = (x + y) / 2 - z
            return np.array([iso_x, iso_y, 0])
        
        # Define the vertices for the cube
        vertices = {
            "A": iso_point(0, 0, 0),
            "B": iso_point(1, 0, 0),
            "C": iso_point(1, 1, 0),
            "D": iso_point(0, 1, 0),
            "E": iso_point(0, 0, 1),
            "F": iso_point(1, 0, 1),
            "G": iso_point(1, 1, 1),
            "H": iso_point(0, 1, 1),
        }
        
        
        # Create edges of the cube
        edges = [
            Line(vertices["A"], vertices["B"],color=RED),
            Line(vertices["B"], vertices["C"],color=RED),
            Line(vertices["C"], vertices["D"],color=RED),
            Line(vertices["D"], vertices["A"],color=RED),
            Line(vertices["A"], vertices["E"],color=RED),
            Line(vertices["B"], vertices["F"],color=RED),
            Line(vertices["C"], vertices["G"],color=RED),
            Line(vertices["D"], vertices["H"],color=RED),
            Line(vertices["E"], vertices["F"],color=RED),
            Line(vertices["F"], vertices["G"],color=RED),
            Line(vertices["G"], vertices["H"],color=RED),
            Line(vertices["H"], vertices["E"],color=RED),
        ]
        
        for edge in edges:
            self.play(Create(edge))
            self.wait(0.3)
        self.wait(2)
        self.fadeOutCurrentScene()


    def Shadows(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Shadow of Shape","").setPosition([-3,0,0])
        p11=cvo.CVO().CreateCVO("Property ","Depends on shape of object").setPosition([1,2,0])
        p12=cvo.CVO().CreateCVO("Property ","Depends on source of light with respect to object").setPosition([1,-2,0])
        p11.setcircleradius(2)
        p12.setcircleradius(2)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)

        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Shadow1(self):
        
        
        title = Text("Shape - Cube", color=YELLOW, font_size=30)
        title.move_to([-4,2,0])
        

        self.play(Write(title))
        
        self.wait()

        # Coordinates for the cuboid centered around the origin with increased height
        a = ((-1, -0.75, 0), (1, -0.75, 0), (2, -1.25, 0), (0, -1.25, 0), (-1, -0.75, 0))
        base = Polygon(*a, stroke_width=5, color=WHITE)

        # Adjusted y-coordinates for the top to increase height
        b = ((-1, 1.0, 0), (1, 1.0, 0), (2, 0.5, 0), (0, 0.5, 0), (-1, 1.0, 0))
        top = Polygon(*b, stroke_width=5, color=WHITE)

        c = ((-1.1, 1.0, 0), (-1.1, -0.75, 0), (0, -1.25, 0), (0, 0.5, 0), (-1, 1.0, 0))
        face1 = Polygon(*c, stroke_width=5, color=WHITE)

        d = ((-1, 1.0, 0), (1, 1.0, 0), (1, -0.75, 0), (-1.1, -0.75, 0), (-1.1, 1.0, 0))
        face2 = Polygon(*d, stroke_width=5, color=WHITE)

        e = ((1, 1.0, 0), (1, -0.75, 0), (2.1, -1.25, 0), (2.1, 0.5, 0), (1, 1.0, 0))
        face3 = Polygon(*e, stroke_width=5, color=WHITE)

        f = ((0, 0.5, 0), (0, -1.25, 0), (2.1, -1.25, 0), (2.1, 0.5, 0), (0, 0.5, 0))
        face4 = Polygon(*f, stroke_width=5, color=WHITE)

        # Labels for dimensions
        

        cube_group = VGroup(base, top, face1, face2, face3, face4)
        cube_group.move_to([-4, 0, 0])  # Move the cube towards the left

        self.play(Create(cube_group))
        
        self.wait()

        face1.set_fill(color=BLUE, opacity=0.5)
        
        face2.set_fill(color=BLUE, opacity=0.5)
        
        face3.set_fill(color=BLUE, opacity=0.5)
        
        face4.set_fill(color=BLUE, opacity=0.5)
        
    
        title = Text("Shadow - Square",color=YELLOW,font_size=30)
        title.move_to([4,2,0])
        

        self.play(Write(title))
        
        self.wait()

        g = ((-1, 1.0, 0), (1, 1.0, 0), (1, -0.75, 0), (-1.1, -0.75, 0), (-1.1, 1.0, 0))
        Square1 = Polygon(*g, stroke_width=5, color=WHITE)
        
        Square1.move_to([4, 0, 0])
        self.play(Write(Square1))

        self.fadeOutCurrentScene()

    def Shadow2(self):

        title = Text("Shape - Pyramid", color=YELLOW, font_size=30)
        title.move_to([-4,2,0])

        self.play(Write(title))
        
        # Define the reduced base of the pyramid (square)
        base_points = [(-1, -1, 0), (1, -1, 0), (0.5, -2, 0), (-1.5, -2, 0)]
        base = Polygon(*base_points, stroke_width=5, color=WHITE)

        # Apex of the pyramid
        apex = [0, 1, 0]

        # Faces of the pyramid
        face1 = Polygon(apex, base_points[0], base_points[1], stroke_width=5, color=WHITE)
        face2 = Polygon(apex, base_points[1], base_points[2], stroke_width=5, color=WHITE)
        face3 = Polygon(apex, base_points[2], base_points[3], stroke_width=5, color=WHITE)
        face4 = Polygon(apex, base_points[3], base_points[0], stroke_width=5, color=WHITE)

       # Group all objects to move them together
        group = VGroup(base, face1, face2, face3, face4)
        
        face1.set_fill(color=BLUE, opacity=0.5)
        
        face2.set_fill(color=BLUE, opacity=0.5)
        
        face3.set_fill(color=BLUE, opacity=0.5)
        
        face4.set_fill(color=BLUE, opacity=0.5)
        
        group.move_to([-4,0,0]) 
        self.play(Create(group))
        self.wait()

        title = Text("Shadow - Triangle", color=YELLOW, font_size=30)
        title.move_to([4,2,0])

        self.play(Write(title))

        face = Polygon(apex, base_points[0], base_points[1], stroke_width=5, color=WHITE)
        face.move_to([4,0,0])
        self.play(Write(face))
        
        self.fadeOutCurrentScene()
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade7Chapter14Understanding2DShapesand3DShapes.py"

    def SetDeveloperList(self):  
        self.DeveloperList="Lagichetty Kushal"
   

if __name__ == "__main__":
    scene = Shapesanim()
    scene.render()
