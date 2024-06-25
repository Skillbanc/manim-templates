import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class shapesanim(AbstractAnim):

    
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
        p10=cvo.CVO().CreateCVO("Shapes", "").setPosition([0,2,0]).setangle(-TAU/6)
        p11=cvo.CVO().CreateCVO("3DShapes", "").setPosition([3,0,0]).setangle(-TAU/6)
        
        p12=cvo.CVO().CreateCVO("2DShapes", "").setPosition([-3,0,0]).setangle(-TAU/6)
        
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
       
        
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Components(self):
        p10=cvo.CVO().CreateCVO("3DShapes", "").setPosition([-6,0,0])
        p11=cvo.CVO().CreateCVO("Components", "").setPosition([-3,0,0]).setangle(-TAU/4)
        p12=cvo.CVO().CreateCVO("Faces", "").setPosition([3,2.5,0]).setangle(-TAU/4)
        p13=cvo.CVO().CreateCVO("Edges", "").setPosition([3,0,0]).setangle(-TAU/4)
        p14=cvo.CVO().CreateCVO("Vertices", "").setPosition([3,-2.5,0]).setangle(-TAU/4)

        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p11.cvolist.append(p14)
        p11.cvolist.append(p13)
        

        self.setNumberOfCirclePositions(6)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def ExampleCube(self):
        
        p10=cvo.CVO().CreateCVO("Cube", "").setPosition([-6,0,0])
        p11=cvo.CVO().CreateCVO("Components", "").setPosition([-3,0,0]).setangle(-TAU/4)
        p12=cvo.CVO().CreateCVO("Faces", "6").setPosition([3,2.5,0]).setangle(-TAU/4)
        p13=cvo.CVO().CreateCVO("Edges", "12").setPosition([3,0,0]).setangle(-TAU/4)
        p14=cvo.CVO().CreateCVO("Vertices", "8").setPosition([2,-2.5,0]).setangle(-TAU/4)
        
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
        p11.cvolist.append(p14)

        self.setNumberOfCirclePositions(5)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Nets(self):
        title = Text("Nets of 3D Shapes", font_size=40, color=BLUE)
        title.to_edge(UP)
        colors = [RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE]

        self.play(Write(title))
        self.wait(1)
        # Create the net of the cube
        net = VGroup(
            Square(side_length=2, fill_opacity=0.5, fill_color=colors[0]).shift(UP*2),
            Square(side_length=2, fill_opacity=0.5, fill_color=colors[1]).shift(LEFT*2),
            Square(side_length=2, fill_opacity=0.5, fill_color=colors[2]),
            Square(side_length=2, fill_opacity=0.5, fill_color=colors[3]).shift(RIGHT*2),
            Square(side_length=2, fill_opacity=0.5, fill_color=colors[4]).shift(DOWN*2),
            Square(side_length=2, fill_opacity=0.5, fill_color=colors[5]).shift(DOWN*4)
        )

        self.play(FadeIn(net))
        self.wait(2)

        # Fold the net into a cube
        folds = [
            # Fold the top face down
            (0, DOWN, PI/2),
            # Fold the left face to the right
            (1, RIGHT, PI/2),
            # Fold the right face to the left
            (3, LEFT, PI/2),
            # Fold the bottom face up
            (4, UP, PI/2),
            
            (5, UP, PI/2)
        ]

        for index, direction, angle in folds:
            face = net[index]
            axis = np.cross([0, 0, 1], direction)
            self.play(Rotate(face, angle, axis=axis, about_point=face.get_center() + direction))
            self.wait(1)

        # Adjust final face to align properly
        face = net[5]
        self.play(Rotate(face, PI/2, axis=RIGHT, about_point=face.get_center() + UP*2))

        self.wait(2)
        self.fadeOutCurrentScene()



    def Sketches(self):
       p10=cvo.CVO().CreateCVO("Sketches","").setPosition([0,2.5,0])
       p11=cvo.CVO().CreateCVO("Oblique Sketches", "").setPosition([-3,1,0]).setangle(-TAU/6)
       p12=cvo.CVO().CreateCVO("Isometric Sketches", "").setPosition([3,1,0]).setangle(-TAU/6)
       p13=cvo.CVO().CreateCVO("Property", "Focuses on face of object").setPosition([-5,-2,0]).setangle(-TAU/6)
       p14=cvo.CVO().CreateCVO("Property", "45 degree for lines").setPosition([-2,-2,0]).setangle(-TAU/6)
       p15=cvo.CVO().CreateCVO("Property", "Focuses on edge of object").setPosition([2,-2,0]).setangle(-TAU/6)
       p16=cvo.CVO().CreateCVO("Property", "lines are drawn at 30 degree").setPosition([5,-2,0]).setangle(-TAU/6)
      
       p10.cvolist.append(p11)
       p10.cvolist.append(p12)
       p11.cvolist.append(p13)
       p11.cvolist.append(p14)
       p12.cvolist.append(p15)
       p12.cvolist.append(p16)
       
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
        p10=cvo.CVO().CreateCVO("Shadow of Shape","").setPosition([0,-2,0])
        p11=cvo.CVO().CreateCVO("Property ","Depends on shape of object").setPosition([-3,1,0])
        p12=cvo.CVO().CreateCVO("Property ","Depends on source of light with respect to object").setPosition([3,1,0])
        p11.setcircleradius(2)
        p12.setcircleradius(2)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)

        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Shadow1(self):
       p10=cvo.CVO().CreateCVO("Shape1","Cube").setPosition([-2,2,0])
       p11=cvo.CVO().CreateCVO("Shadow of shape1", "Square").setPosition([2,2,0]).setangle(-TAU/4)
       p10.cvolist.append(p11)
       
       
       self.setNumberOfCirclePositions(2)
       self.construct1(p10,p10)
    
    def Shadow2(self):

       p10=cvo.CVO().CreateCVO("Shape2", "Pyramid").setPosition([-2,-2,0])
       p11=cvo.CVO().CreateCVO("Shadow of shape2", "Triangle").setPosition([2,-2,0]).setangle(-TAU/4)
       p10.cvolist.append(p11)
      
       self.setNumberOfCirclePositions(2)
       self.construct1(p10,p10)
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="ShapesAnim.py"

    def SetDeveloperList(self):  
        self.DeveloperList="Lagichetty Kushal"
   

if __name__ == "__main__":
    scene = shapesanim()
    scene.render()
