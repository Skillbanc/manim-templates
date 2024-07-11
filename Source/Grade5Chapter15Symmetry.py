import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo
class SymmetryGrade5(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.constructDataByCVO()
        self.fadeOutCurrentScene()
        self.Examples()
        self.fadeOutCurrentScene()
        self.Clockwises()
        self.fadeOutCurrentScene()
        self.ExamplesClock()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        #self.constructDataByJSON()
        #self.fadeOut()
        
    # render using CVO data object
    def constructDataByCVO(self):
        p10=cvo.CVO().CreateCVO("Symmetry","").setPosition([-4.5,0,0])
        p11=cvo.CVO().CreateCVO("Condition","Looks same if placed in front of a mirror").setPosition([4.5,2.5,0]).setangle([-TAU/4])
        p12=cvo.CVO().CreateCVO("Example","Letter M looks same if placed in front of mirror").setPosition([4.5,0,0]).setangle([-TAU/4])
        p13=cvo.CVO().CreateCVO("Representation","With a dotted line").setPosition([4.5,-2.5,0]).setangle([TAU/2])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.isRandom=False
        self.setNumberOfCirclePositions(4)
        self.construct1(p10,p10)
    def Examples(self):
        title = Text("Symmetrical Represtation")
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        letter_M = Text("M", font_size=200, color=WHITE)
        letter_M.move_to(ORIGIN)
        midline = DashedLine(start=UP * 1.5, end=DOWN * 1.5, color=RED, dash_length=0.1)
        self.play(Write(letter_M))
        self.wait(1)
        self.play(Create(midline)) 
        self.wait(1)
        self.fadeOutCurrentScene()
        title = Text("Symmetrical Represtation")
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        letter_K = Text("K", font_size=200, color=WHITE)
        letter_K.move_to(ORIGIN)
        midline = DashedLine(start=LEFT * 1.5, end=RIGHT * 1.5, color=RED, dash_length=0.1).move_to(ORIGIN)
        self.play(Write(letter_K))
        self.wait(1)
        self.play(Create(midline))
        self.wait(1)
        self.fadeOutCurrentScene()
        """points = [
            np.array([0, 0, 0]),
            np.array([1, 1, 0]),
            np.array([2, 0, 0]),
            np.array([1, -1, 0]),
            np.array([0, 0, 0.5]),  # Body of the butterfly
            np.array([0, 1, 0]),
            np.array([-1, 0, 0]),
            np.array([0, -1, 0])
        ]"""
        title = Text("Symmetrical Represtation")
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        # Create a smooth curve
        butterfly =Text("🦋", font_size=100)

        # Add the emoji text to the scene
        self.add(butterfly)

        # Optionally, animate the emoji (e.g., moving it)
        self.play(butterfly.animate.move_to(UP))

        # Keep the scene displayed for a few seconds
        self.wait(1)
        #butterfly.set_points_smoothly([*points, points[0]])

        # Create a line of symmetry (y-axis)
        symmetry_line = DashedLine(start=np.array([0, 0, 0]), end=np.array([0, 2, 0]), color=RED)

        # Reflect one half of the butterfly across the symmetry line
        """reflected_butterfly = butterfly.copy()
        reflected_butterfly.apply_function(lambda p: np.array([-p[0], p[1], p[2]]))

        # Grouping the original butterfly, symmetry line, and reflected butterfly
        full_scene = VGroup(butterfly, reflected_butterfly)"""

        # Displaying the scene
        #self.play(butterfly)
        #self.play(Transform(butterfly.copy(), full_scene))
        self.play(Create(symmetry_line))
        self.wait(2)
    def Clockwises(self):
       p13=cvo.CVO().CreateCVO("Rotations","").setPosition([-4.5,0,0])
       p14=cvo.CVO().CreateCVO("Clockwise rotation","").setPosition([0,2.5,0]).setangle([-TAU/4])
       p15=cvo.CVO().CreateCVO("Anti-Clockwise","").setPosition([0,-2.5,0]).setangle([-TAU/4])
       p16=cvo.CVO().CreateCVO("Definition","moving in the direction of clock").setPosition([3.5,2.5,0]).setangle([-TAU/4])
       p17=cvo.CVO().CreateCVO("Definition","moving in the opposite\\\\ direction of clock").setPosition([3.5,-2.5,0]).setangle([-TAU/4])
        
       p13.cvolist.append(p14)
       p13.cvolist.append(p15)
       p14.cvolist.append(p16)
       p15.cvolist.append(p17)
       self.isRandom=False
       self.setNumberOfCirclePositions(3)

       self.construct1(p13,p13)
    def ExamplesClock(self):
       number_9 = Tex("9")
       number_9.scale(3)  # Scale up the size of the number 9

        # Create text labels for clockwise and counterclockwise
       clockwise_text = Text("Clockwise", font_size=24).next_to(number_9, DOWN, buff=1)
       anticlockwise_text = Text("Anti-clockwise", font_size=24).next_to(number_9, DOWN, buff=0.5)

        # Position the number 9 and labels in a group
       number_group = VGroup(number_9, clockwise_text, anticlockwise_text)
       number_group.arrange(DOWN, buff=0.5)
       number_group.move_to(ORIGIN)

        # Show the number 9 and labels initially
       self.play(Write(number_9))

        # Add labels after showing number 9
       self.play(Write(anticlockwise_text))
        # Rotate clockwise and then counterclockwise
       self.play(Rotate(number_9, TAU, about_point=ORIGIN, run_time=2))
       self.wait(1)
       self.play(Transform(anticlockwise_text, clockwise_text))
       self.play(Write(clockwise_text))
       self.wait(1)
       self.play(Rotate(number_9, -TAU, about_point=ORIGIN, run_time=2))
       self.wait(1)
    def SetDeveloperList(self): 
       self.DeveloperList="Preetham" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade5Chapter15Symmetry.py"   
if __name__ == "__main__":
    scene = SymmetryGrade5()
    scene.render()