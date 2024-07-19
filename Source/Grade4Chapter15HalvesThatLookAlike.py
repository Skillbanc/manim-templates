import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo
class Chapter15Grade4(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.constructDataByCVO()
        self.fadeOutCurrentScene()
        self.Example()
        self.fadeOutCurrentScene()
        self.LineDivision()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        self.fadeOutCurrentScene()
        #self.constructDataByJSON()
        #self.fadeOut()
        
    # render using CVO data object
    def constructDataByCVO(self):
        p16=cvo.CVO().CreateCVO("Halves that look alike","").setPosition([-3.5,0,0])
        p17=cvo.CVO().CreateCVO("Condition","If we divide, both look alike").setPosition([3.5,0,0]).setangle([-TAU/4])
        p16.cvolist.append(p17)
        self.isRandom=False        
        self.setNumberOfCirclePositions(2)
        self.construct1(p16,p16)
    def Example(self):
        title = Text("Halves that look alike")
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Define the original arc and leaves
        arc = Arc(radius=1, start_angle=-PI/2, angle=PI, color=WHITE)
        leaf1 = Ellipse(width=0.4, height=0.8, color=WHITE).rotate(PI/4).move_to(arc.point_from_proportion(0.2) + LEFT * 0.5 + UP * 0.3)
        leaf2 = Ellipse(width=0.4, height=0.8, color=WHITE).rotate(-PI/4).move_to(arc.point_from_proportion(0.4) + LEFT * 0.5 + DOWN * 0.3)
        leaf3 = Ellipse(width=0.4, height=0.8, color=WHITE).rotate(PI/4).move_to(arc.point_from_proportion(0.6) + LEFT * 0.5 + UP * 0.3)
        leaf4 = Ellipse(width=0.4, height=0.8, color=WHITE).rotate(-PI/4).move_to(arc.point_from_proportion(0.8) + LEFT * 0.5 + DOWN * 0.3)

        # Group the arc and leaves into a single half figure
        half_figure = VGroup(arc, leaf1, leaf2, leaf3, leaf4)

        # Position the half figure to the left
        half_figure.to_edge(ORIGIN)

        # Animate drawing the half figure
        self.play(Create(arc))
        self.play(Create(leaf1), Create(leaf2), Create(leaf3), Create(leaf4))
        self.wait(1)
        text1 = Text("This is half of a figure.")
        text1.to_edge(DOWN)
        text2 = Text("The figure gets completed after placing a mirror.")
        text2.to_edge(DOWN)
        self.play(Write(text1))
        self.wait(1)
        self.play(Transform(text1, text2))

        # Reflect the half figure horizontally to create the mirrored half
        mirrored_half = half_figure.copy().scale([-1, 1, 1]).shift(LEFT)

        # Animate the appearance of the mirrored half
        self.play(FadeIn(mirrored_half))
        self.wait(1)
       
        

        # Combine the figures to show the complete image
        full_figure = VGroup(half_figure, mirrored_half)

        # Show the complete figure
        self.play(FadeIn(full_figure))
        self.wait(2)
    def LineDivision(self):
        title = Text("Dividing with line")
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        top = UP * 2
        bottom = DOWN * 2
        left = LEFT * 1
        right = RIGHT * 3
        
        # Create the kite
        kite = Polygon(top, right, bottom, left, color=BLUE, fill_opacity=0.5)
        
        # Create the line of symmetry
        symmetry_line = Line(left + LEFT * 0.5, right + RIGHT * 0.5, color=YELLOW)
        
        # Animate the creation of the kite
        self.play(Create(kite))
        self.wait(1)
        
        # Animate the drawing of the symmetry line
        self.play(Create(symmetry_line))
        self.wait(2)
        self.fadeOutCurrentScene()
        title = Text("Dividing with a line")
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        square = Square(side_length=2, color=BLUE, fill_opacity=0.5)
        center_x = (square.get_center()[0])
        line = Line([center_x, -3, 0], [center_x, 3, 0], color=YELLOW)
        self.play(Create(square))
        self.play(square.animate.shift(0.5 * line.get_unit_vector()))
        self.play(Create(line))
        self.wait(1)
    def SetDeveloperList(self): 
       self.DeveloperList="Preetham" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade4Chapter15Patterns.py"    

    
if __name__ == "__main__":
    scene = Chapter15Grade4()
    scene.render()