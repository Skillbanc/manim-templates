import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class SymmetryAnim3(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.constructDataByCVO()
        self.fadeOutCurrentScene()
        self.linesymmetry()
        self.fadeOutCurrentScene()
        self.ExamplesLine()
        self.fadeOutCurrentScene()
        self.rotsymmetry()
        self.fadeOutCurrentScene()
        self.ExamplesRot()
        self.fadeOutCurrentScene()
        self.lineandrot()
        self.fadeOutCurrentScene()
        self.ExamplesLR()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        #self.fadeOutCurrentScene()
        #self.constructDataByJSON()
        #self.fadeOut()
        
    # render using CVO data object
    def constructDataByCVO(self):
        p10=cvo.CVO().CreateCVO("Symmetry","").setPosition([0,2,0])
        p11=cvo.CVO().CreateCVO("Line symmetry","").setPosition([4.5,-2.5,0]).setangle([-TAU/4])
        p12=cvo.CVO().CreateCVO("Rotational symmetry","").setPosition([-4.5,-2.5,0]).setangle([-TAU/4])
        p13=cvo.CVO().CreateCVO("Line and Rotational Symmetry","").setPosition([0,-2.5,0]).setangle([TAU/2])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.isRandom=False
        self.setNumberOfCirclePositions(4)
        self.construct1(p10,p10)
    def linesymmetry(self):
        p14=cvo.CVO().CreateCVO("Line symmetry","").setPosition([-4.5,0,0])
        p16=cvo.CVO().CreateCVO("Condition","based on axes of symmetry").setPosition([4.5,2,0]).setangle([-TAU/4])
        p15=cvo.CVO().CreateCVO("Examples","based on axes of symmetry").setPosition([4.5,-2.5,0]).setangle([-TAU/4])
        p14onamelist=["regular polygons","rectangle","others"]
        p15.extendOname(p14onamelist)
        p14.cvolist.append(p16)
        p14.cvolist.append(p15)
        self.isRandom=False  
        self.setNumberOfCirclePositions(2)
        self.isRandom=False
        self.construct1(p14,p14)
    def ExamplesLine(self):
       # Create a square
        square = Square(side_length=2, color=BLUE, fill_opacity=0.5)
        square_label = Text("Square", font_size=24).next_to(square, LEFT)  
        # Create a triangle
        triangle = Polygon([-2, -1, 0], [0, 2, 0], [2, -1, 0], color=RED, fill_opacity=0.5)
        triangle_label = Text("Triangle", font_size=24).next_to(triangle, LEFT) 
        # Create a circle
        circle = Circle(radius=1, color=GREEN, fill_opacity=0.5)
        circle_label = Text("Circle", font_size=24).next_to(circle, LEFT)
        center_x = (square.get_center()[0] + triangle.get_center()[0] + circle.get_center()[0]) / 3
        # Create a line of symmetry
        line = Line([center_x, -3, 0], [center_x, 3, 0], color=YELLOW)
        line_label = Text("Line of Symmetry", font_size=24).next_to(line, UP)
        # Add everything to the scene
        self.play(Create(square), Write(square_label))
        self.play(square.animate.shift(0.5 * line.get_unit_vector()))
        self.play(Create(line), Write(line_label))
        self.wait(1)
        self.fadeOutCurrentScene()
        self.play(Create(triangle), Write(triangle_label))
        self.play(triangle.animate.shift(0.5 * line.get_unit_vector()))
        self.play(Create(line), Write(line_label))
        self.wait(1)
        self.fadeOutCurrentScene()
        self.play(Create(circle), Write(circle_label))
        self.play(circle.animate.shift(0.5 * line.get_unit_vector()))
        self.play(Create(line), Write(line_label))
        self.wait(1)
        self.fadeOutCurrentScene()
    def rotsymmetry(self):
        p16=cvo.CVO().CreateCVO("Rotational symmetry","").setPosition([-4.5,0,0])
        p18=cvo.CVO().CreateCVO("Condition","based on angle of rotation ").setPosition([4.5,2,0]).setangle(-TAU/4)
        p17=cvo.CVO().CreateCVO("Examples","based on angle of rotation ").setPosition([4.5,-2.5,0]).setangle(-TAU/4)
        p12onamelist=["regular polygons","others"]
        p17.extendOname(p12onamelist)
        p16.cvolist.append(p18)
        p16.cvolist.append(p17)
        self.isRandom=False
        self.setNumberOfCirclePositions(3)
        self.construct1(p16,p16)
    def ExamplesRot(self):
       def create_arrow(polygon):
            # Get a point on the perimeter of the polygon
            point_on_perimeter = polygon.get_vertices()[0]
            direction_vector = point_on_perimeter - polygon.get_center()
            arrow = Arrow(start=polygon.get_center(), end=polygon.get_center() + direction_vector, buff=0)
            return arrow
        # Create a pentagon
       pentagon = RegularPolygon(n=5, color=BLUE, fill_opacity=0.5)
       pentagon_label = Text("Pentagon", font_size=24).next_to(pentagon, DOWN) 
        # Create a hexagon
       hexagon = RegularPolygon(n=6, color=RED, fill_opacity=0.5)
       hexagon_label = Text("Hexagon", font_size=24).next_to(hexagon, DOWN)
        # Create an octagon
       octagon = RegularPolygon(n=8, color=GREEN, fill_opacity=0.5)
       octagon_label = Text("Octagon", font_size=24).next_to(octagon, DOWN) 
        # Create a center point for rotat
       center_point = Dot(color=YELLOW)
# Add and animate the pentagon
       self.play(Create(pentagon), Write(pentagon_label))
       arrow = create_arrow(pentagon)
       self.play(Create(arrow))
       self.play(pentagon.animate.set_color(YELLOW).rotate(2*PI/5, about_point=center_point.get_center()), Rotate(arrow, angle=2*PI/5, about_point=center_point.get_center()))
       self.play(pentagon.animate.set_color(BLUE))
       self.play(FadeOut(pentagon), FadeOut(pentagon_label), FadeOut(arrow), FadeOut(center_point))
        # Add and animate the hexagon
       self.play(Create(hexagon), Write(hexagon_label))
       arrow = create_arrow(hexagon)
       self.play(Create(arrow))
       self.play(hexagon.animate.set_color(YELLOW).rotate(PI/3, about_point=center_point.get_center()), Rotate(arrow, angle=PI/3, about_point=center_point.get_center()))
       self.play(hexagon.animate.set_color(RED))
       self.play(FadeOut(hexagon), FadeOut(hexagon_label), FadeOut(arrow), FadeOut(center_point))
        # Add and animate the octagon
       self.play(Create(octagon), Write(octagon_label))
       arrow = create_arrow(octagon)
       self.play(Create(arrow))
       self.play(octagon.animate.set_color(YELLOW).rotate(PI/4, about_point=center_point.get_center()), Rotate(arrow, angle=PI/4, about_point=center_point.get_center()))
       self.play(octagon.animate.set_color(GREEN))
       self.play(FadeOut(octagon), FadeOut(octagon_label), FadeOut(arrow), FadeOut(center_point))
       self.wait()
    def lineandrot(self):
        p13=cvo.CVO().CreateCVO("Line and Rotational Symmetry","").setPosition([-4.5,0,0])
        p16=cvo.CVO().CreateCVO("Condition","some figures have both").setPosition([4.5,2,0]).setangle([-TAU/4])
        p18=cvo.CVO().CreateCVO("Examples","based on angle of rotation ").setPosition([4.5,-2.5,0]).setangle([-TAU/4])
        p13onamelist=["regular polygons","others"]
        p18.extendOname(p13onamelist)
        p13.cvolist.append(p16)
        p13.cvolist.append(p18)
        self.isRandom=False
        self.setNumberOfCirclePositions(2)
        self.construct1(p13,p13)
    def ExamplesLR(self):    
        def create_arrow(shape):
            # Get a point on the perimeter of the shape
            if isinstance(shape, Square):
                point_on_perimeter = shape.get_vertices()[0]
            elif isinstance(shape, Circle):
                point_on_perimeter = shape.point_at_angle(0)
            direction_vector = point_on_perimeter - shape.get_center()
            arrow = Arrow(start=shape.get_center(), end=shape.get_center() + direction_vector, buff=0)
            return arrow
        # Create a square
        square = Square(side_length=2, color=BLUE, fill_opacity=0.5)
        square_label = Text("Square", font_size=24).next_to(square, DOWN)
        # Create a circle
        circle = Circle(radius=1, color=GREEN, fill_opacity=0.5)
        circle_label = Text("Circle", font_size=24).next_to(circle, DOWN)
        # Create a center point for rotation
        center_point = Dot(color=YELLOW)
        # Create a line of symmetry passing through the center
        line = Line([-4, 0, 0], [4, 0, 0], color=PURPLE)
        line_label = Text("Line of Symmetry", font_size=24).next_to(line, RIGHT)
        # Add and animate the square
        self.play(Create(square), Write(square_label))
        self.play(Create(center_point))
        arrow = create_arrow(square)
        self.play(Create(arrow))
        self.play(square.animate.set_color(RED).rotate(PI/2, about_point=center_point.get_center()), Rotate(arrow, angle=PI/2, about_point=center_point.get_center()))
        self.play(square.animate.set_color(BLUE))
        self.play(Create(line), Write(line_label))
        self.play(FadeOut(square), FadeOut(square_label), FadeOut(arrow), FadeOut(center_point), FadeOut(line), FadeOut(line_label))
        # Add and animate the circle
        self.play(Create(circle), Write(circle_label))
        self.play(Create(center_point))
        arrow = create_arrow(circle)
        self.play(Create(arrow))
        self.play(circle.animate.set_color(RED).rotate(PI/2, about_point=center_point.get_center()), Rotate(arrow, angle=PI/2, about_point=center_point.get_center()))
        self.play(circle.animate.set_color(GREEN))
        self.play(Create(line), Write(line_label))
        self.play(FadeOut(circle), FadeOut(circle_label), FadeOut(arrow), FadeOut(center_point), FadeOut(line), FadeOut(line_label))
        self.wait()
    def SetDeveloperList(self): 
       self.DeveloperList="Preetham" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade7Chapter15Symmetry.py"    
if __name__ == "__main__":
    scene = SymmetryAnim3()
    scene.render()