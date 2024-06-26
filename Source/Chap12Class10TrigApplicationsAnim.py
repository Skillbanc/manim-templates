# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla
import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class TrigAppAnim(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.LoS()
        self.LoSAnim()
        self.Formula()
        self.Requirements()
        self.AoE()
        self.AoEAnim()
        self.AoD()
        self.AoDAnim()
        self.GithubSourceCodeReference()

        
        # self.fadeOut()
        # self.constructDataByJSON()
        # self.fadeOut()
        
    def SetDeveloperList(self):  
        self.DeveloperList="Hriday Bhushan"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Chap12Class10TrigApplicationsAnim.py"
    
    # render using CVO data object
    def LoS(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Line of Sight","").setPosition([-4,2.5,0])
        p11=cvo.CVO().CreateCVO("Definition","a line from an observer's eye to a distant point").setPosition([0,2.5,0])
        
        p10.setcircleradius(1.2)
        p11.setcircleradius(1.2)
        p10.cvolist.append(p11)
        
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)

    def Formula(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Formula", "Tan Theta = Height/Base")
        p11=cvo.CVO().CreateCVO("Key", "").setPosition([2,1.5,0])
        p11onameList=["Theta: Angle between Line of Sight and Horizontal Line", "Height: Height of the object", "Base: Distance from Object"]
        p11.extendOname(p11onameList)
        p12=cvo.CVO().CreateCVO("Uses", "To compute height, distance or angle between observer").setPosition([2,-1.5,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.setcircleradius(1.5)
        p11.setcircleradius(1.5)
        p12.setcircleradius(1.5)
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def LoSAnim(self):
        # Define the observer position
        observer = Dot(LEFT * 3)
        observer_label = Text("Observer").next_to(observer, DOWN)
        
        # Define the initial object position
        moving_object = Dot(RIGHT * 3)
        object_label = Text("Object").next_to(moving_object, DOWN)

        #ground level
        groundlevel = DashedLine(config.left_side/2, config.right_side/2)
        groundlabel = Tex("Ground Level").next_to(groundlevel, RIGHT).scale(0.5).shift(LEFT*0.5)
        # Create a line of sight
        line_of_sight = always_redraw(lambda: Line(observer.get_center(), moving_object.get_center(), color=YELLOW))
        
        # Add all elements to the scene
        self.add(observer, observer_label, moving_object, object_label, groundlevel, groundlabel, line_of_sight)
        
        # Animate the object moving
        self.play(moving_object.animate.move_to(UP * 2 + RIGHT * 2), run_time=2)
        self.play(moving_object.animate.move_to(DOWN * 2 + RIGHT * 2), run_time=2)
       

        # Ensure the line of sight updates during the animation
        self.wait(1)
        self.fadeOutCurrentScene()
       
    
    def AoE(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Angle of Elevation", "").setPosition([-5,2.5,0])
        p11=cvo.CVO().CreateCVO("Definition", " line of sight is above the horizontal line and angle between the line of sight and the horizontal line").setPosition([-3,1.1,0])
        p10.setcircleradius(1)
        p11.setcircleradius(1)
        p10.cvolist.append(p11)
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        
       
    def AoEAnim(self):
        # Shift the entire diagram downwards
        shift_down = 2 * DOWN

        # Define the observer position
        observer = Dot(LEFT * 3 + shift_down)
        observer_label = Text("Observer").next_to(observer, DOWN)
        
        # Define the initial object position
        object = Dot(UP * 3 + RIGHT * 3 + shift_down)
        object_label = Text("Object").next_to(object, UP)
        
        # Create a line of sight
        line_of_sight = always_redraw(lambda: Line(observer.get_center(), object.get_center(), color=YELLOW))
        
        # Create horizontal line (distance) and vertical line (height)
        horizontal_line = always_redraw(lambda: Line(observer.get_center(), observer.get_center() + RIGHT * (object.get_center()[0] - observer.get_center()[0]), color=BLUE))
        vertical_line = always_redraw(lambda: Line(object.get_center(), observer.get_center() + RIGHT * (object.get_center()[0] - observer.get_center()[0]), color=RED))
        
        # Create the angle of elevation arc and label
        angle_arc = always_redraw(lambda: Angle(horizontal_line, line_of_sight, radius=0.5))
        angle_label = always_redraw(lambda: MathTex(r"\theta").next_to(angle_arc, UP + RIGHT, buff=0.1))

        # Key labels
        key_labels = VGroup(
            Text("Horizontal line (Distance)", color=BLUE),
            Text("Vertical line (Height)", color=RED),
            Text("Line of Sight", color=YELLOW)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).shift(3*UP + 4*RIGHT)
        key_labels.scale(0.6)
        
        # Add all elements to the scene
        self.add(observer, observer_label, object, object_label, line_of_sight, horizontal_line, vertical_line, angle_arc, angle_label, key_labels)
        self.play(FadeIn(observer), FadeIn(observer_label), FadeIn(object), FadeIn(object_label),
                  FadeIn(line_of_sight), FadeIn(horizontal_line),FadeIn(angle_arc), FadeIn(angle_label),FadeIn(key_labels))
    
        # Animate the object moving up and to the right
        self.play(object.animate.move_to(UP * 1.5 + RIGHT * 1.5), run_time=3)

        self.wait(2)
        self.fadeOutCurrentScene()

        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Example", "Distance=10m and Angle of Elevation=45Deg, find Height").setPosition([-4,0.5,0])
        p11=cvo.CVO().CreateCVO("Solution", "Height = Tan45 * 10m(Distance) = 10 metres").setPosition([-3.5,2.5,0])
        p10.setcircleradius(1)
        p11.setcircleradius(1)
        p12=cvo.CVO().CreateCVO("Formula", "Tan Theta = Height/Base").setPosition([-4.5,-1.5,0])
        p10.cvolist.append(p12)
        p10.cvolist.append(p11)
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)

        # Shift the entire diagram downwards
        shift_down = 2 * DOWN

        # Define the observer position
        observer = Dot(LEFT * 3 + shift_down)
        observer_label = Text("Observer").next_to(observer, DOWN)
        
        # Define the initial object position
        object = Dot(UP * 3 + RIGHT * 3 + shift_down)
        object_label = Text("Object").next_to(object, UP)
        
        # Create a line of sight
        line_of_sight = always_redraw(lambda: Line(observer.get_center(), object.get_center(), color=YELLOW))
        
        # Create horizontal line (distance) and vertical line (height)
        horizontal_line = always_redraw(lambda: Line(observer.get_center(), observer.get_center() + RIGHT * (object.get_center()[0] - observer.get_center()[0]), color=BLUE))
        vertical_line = always_redraw(lambda: Line(object.get_center(), observer.get_center() + RIGHT * (object.get_center()[0] - observer.get_center()[0]), color=RED))
        
        # Create the angle of elevation arc and label
        angle_arc = always_redraw(lambda: Angle(horizontal_line, line_of_sight, radius=0.5))
        angle_label = always_redraw(lambda: MathTex(r"\theta").next_to(angle_arc, UP + RIGHT, buff=0.1))

        # Key labels
        key_labels = VGroup(
            Text("Distance=10m", color=BLUE),
            Text("Theta=45 Degree", color=YELLOW),
            Text("Height=?", color=RED)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).shift(3*UP + 4*RIGHT)
        key_labels.scale(0.6)
        
        # Add all elements to the scene
        self.add(observer, observer_label, object, object_label, line_of_sight, horizontal_line, vertical_line, angle_arc, angle_label, key_labels)
    
        # Animate the object moving up and to the right
        
        self.wait(5)
        self.fadeOutCurrentScene()
    

    def AoD(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Angle of Depression", "").setPosition([-5,2.5,0])
        p11=cvo.CVO().CreateCVO("Definition", "Angle between the line of sight and the horizontal line").setPosition([-4,-1,0])
        p10.cvolist.append(p11)
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)

    def AoDAnim(self):
        # Define the observer position
        observer = Dot(UP * 2 + LEFT * 2)
        observer_label = Text("Observer").next_to(observer, UP)

        # Define the initial object position
        object = Dot(DOWN * 1)
        object_label = Text("Object").next_to(object, RIGHT)

        # Create a line of sight
        line_of_sight = always_redraw(lambda: Line(observer.get_center(), object.get_center(), color=YELLOW))

        # Create horizontal line (distance) and vertical line (height)
        horizontal_line = always_redraw(lambda: Line(observer.get_center(), observer.get_center() + RIGHT * 2, color=BLUE))
        vertical_line = always_redraw(lambda: Line(object.get_center(), observer.get_center() + RIGHT * 2, color=RED))

        # Create the angle of depression arc and label
        angle_arc = always_redraw(lambda: Angle(line_of_sight, horizontal_line, radius=0.3))
        angle_label = always_redraw(lambda: MathTex(r"\theta").next_to(angle_arc.point_from_proportion(0.5), UP + RIGHT, buff=0.05))

         # Key labels
        key_labels = VGroup(
            Text("Line of Sight", color=YELLOW),
            Text("Horizontal line (Distance)", color=BLUE),
            Text("Vertical line (Height)", color=RED)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).shift(3*UP + 4*RIGHT)
        key_labels.scale(0.6)

        # Add all elements to the scene
        self.add(observer, observer_label, object, object_label, line_of_sight, horizontal_line, vertical_line, angle_arc, angle_label, key_labels)

        # Animate the object moving down and to the right
        self.play(object.animate.move_to(DOWN * 1.5 ), run_time=3)
        
        # Ensure the lines and angle update during the animation
        self.wait(3)
        self.fadeOutCurrentScene()

        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Example", "Depth=20m and Angle of Depression=45Deg, find Distance").setPosition([-3.5,-2.5,0])
        p11=cvo.CVO().CreateCVO("Solution", "Distance = 20m(Height)/Tan45 = 20 metres").setPosition([-4.2,0.5,0])
        p10.setcircleradius(1)
        p11.setcircleradius(1)
        p12=cvo.CVO().CreateCVO("Formula", "Tan Theta = Height/Base").setPosition([4.5,-1.5,0])
        p10.cvolist.append(p12)
        p10.cvolist.append(p11)
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)

        # Define the observer position
        observer = Dot(UP * 2 + LEFT * 2)
        observer_label = Text("Observer").next_to(observer, UP)

        # Define the initial object position
        object = Dot(DOWN * 1)
        object_label = Text("Object").next_to(object, RIGHT)

        # Create a line of sight
        line_of_sight = always_redraw(lambda: Line(observer.get_center(), object.get_center(), color=YELLOW))

        # Create horizontal line (distance) and vertical line (height)
        horizontal_line = always_redraw(lambda: Line(observer.get_center(), observer.get_center() + RIGHT * 2, color=BLUE))
        vertical_line = always_redraw(lambda: Line(object.get_center(), observer.get_center() + RIGHT * 2, color=RED))

        # Create the angle of depression arc and label
        angle_arc = always_redraw(lambda: Angle(line_of_sight, horizontal_line, radius=0.3))
        angle_label = always_redraw(lambda: MathTex(r"\theta").next_to(angle_arc.point_from_proportion(0.5), UP + RIGHT, buff=0.05))

         # Key labels
        key_labels = VGroup(
            Text("Distance", color=BLUE),
            Text("Theta=45 Deg", color=YELLOW),
            Text("Depth=20m", color=RED)
            
            
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).shift(3*UP + 4*RIGHT)
        key_labels.scale(0.6)

        # Add all elements to the scene
        self.add(observer, observer_label, object, object_label, line_of_sight, horizontal_line, vertical_line, angle_arc, angle_label, key_labels)

        
        # Ensure the lines and angle update during the animation
        self.wait(5)
        self.fadeOutCurrentScene()

    def Requirements(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Diagram", "")
        p12=cvo.CVO().CreateCVO("Condition", "All objects should be considered linear").setPosition([2,-2,0])
        p11=cvo.CVO().CreateCVO("Condition", "Angle of elevation or depression is with reference to horizontal line").setPosition([2.5,2,0])
        p13=cvo.CVO().CreateCVO("Condition", "Height of observer is neglected if not given").setPosition([-3,2,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p11.setcircleradius(1.5)
        p12.setcircleradius(1.5)
        p13.setcircleradius(1.5)
        self.setNumberOfCirclePositions(4)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
    
    
if __name__ == "__main__":
    scene = TrigAppAnim()
    scene.render()