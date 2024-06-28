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

class Grade4Chapter8HowLongisThis(AbstractAnim):
    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.Length()
        self.fadeOutCurrentScene()
        self.Measurement()
        self.fadeOutCurrentScene()
        self.Anim1()        
        self.fadeOutCurrentScene()
        self.Anim2()
        self.fadeOutCurrentScene()
        self.Anim3()
        self.GithubSourceCodeReference()
        
    def SetDeveloperList(self):  
        self.DeveloperList="Prithiv Shiv M V"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade4Chapter8HowLongisThis.py"
        
        
    # render using CVO data object 
    
    def Length(self):
        self.isRandom=False
        self.positionChoice=[[-4,0,0],[4,0,0]]
        p10=cvo.CVO().CreateCVO("Length","Measurement")
        p11=cvo.CVO().CreateCVO("Types","cm\\\\m\\\\inches")
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def Measurement(self):
        self.isRandom = False
        self.setNumberOfCirclePositions(4)
        p10=cvo.CVO().CreateCVO("Length","1 Meter")
        p11=cvo.CVO().CreateCVO("Equals", "100 cm\\\\39.3 inches")
        p12=cvo.CVO().CreateCVO("Length", "1 Centimeter")
        p13=cvo.CVO().CreateCVO("Equals", "10mm\\\\0.39 inches")
        p10.cvolist.append(p11)
        p12.cvolist.append(p13)
        self.construct1(p10,p10)
        self.construct1(p12,p12)
       
    def Anim1(self):
        # Title
        title = Text("Measurement Rulers: cm and inches", font_size=48)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Ruler length in centimeters (1 meter = 100 cm)
        ruler_length_cm = 100
        cm_to_inch = 2.54
        ruler_length_inch = int(ruler_length_cm / cm_to_inch)
        
        # Define scale factor for visualization
        scale_factor = 0.1

        # Draw the centimeter ruler
        cm_ruler = Line(start=ORIGIN, end=RIGHT * ruler_length_cm * scale_factor, stroke_width=2).move_to(UP)
        self.play(Create(cm_ruler))
        
        # Draw centimeter markings on the top ruler
        cm_marks = VGroup()
        for i in range(0, ruler_length_cm + 1):
            if i % 10 == 0:
                mark_length = 0.4
            else:
                mark_length = 0.2
            mark = Line(start=UP * mark_length, end=ORIGIN).move_to(cm_ruler.point_from_proportion(i / ruler_length_cm))
            cm_marks.add(mark)
        self.play(*[Create(mark) for mark in cm_marks])
        
        # Add centimeter labels every 10 cm on the top ruler
        cm_labels = VGroup()
        for i in range(0, ruler_length_cm + 1, 10):
            label = Text(f"{i} cm", font_size=24).next_to(cm_marks[i], UP)
            cm_labels.add(label)
        self.play(*[Write(label) for label in cm_labels])
        
        # Draw the inch ruler
        inch_ruler = Line(start=ORIGIN, end=RIGHT * ruler_length_cm * scale_factor, stroke_width=2).next_to(cm_ruler, DOWN, buff=1)
        self.play(Create(inch_ruler))
        
        # Draw inch markings on the bottom ruler
        inch_marks = VGroup()
        for i in range(0, ruler_length_inch + 1):
            if i % 2 == 0:
                mark_length = 0.3
            else:
                mark_length = 0.15
            proportion = i * cm_to_inch / ruler_length_cm
            if proportion <= 1:  # Ensure the proportion is within the ruler's length
                mark = Line(start=DOWN * mark_length, end=ORIGIN).move_to(inch_ruler.point_from_proportion(proportion))
                inch_marks.add(mark)
        self.play(*[Create(mark) for mark in inch_marks])
        
        # Add inch labels every inch on the bottom ruler
        inch_labels = VGroup()
        for i in range(0, ruler_length_inch + 1, 1):
            proportion = i * cm_to_inch / ruler_length_cm
            if proportion <= 1:  # Ensure the proportion is within the ruler's length
                label = Text(f"{i}\nin", font_size=12).next_to(inch_ruler.point_from_proportion(proportion), DOWN)
                inch_labels.add(label)
        self.play(*[Write(label) for label in inch_labels])
        
        # Add meter label at the end of the centimeter ruler
        meter_label = Text(f"1 meter", font_size=36).next_to(cm_ruler.get_end(), UP, buff=0.5).shift(RIGHT+DOWN)
        self.play(Write(meter_label))
        
        self.wait(2)
        
        # Fade out all elements
        all_elements = VGroup(cm_ruler, cm_marks, cm_labels, inch_ruler, inch_marks, inch_labels, meter_label)
        self.play(FadeOut(all_elements))
        self.wait(1)

    def Anim2(self):
        title = Text("Measuring a pencil").to_edge(UP)
        self.play(Write(title))
        ruler_length_cm = 15
        
        # Define scale factor for visualization
        scale_factor = 0.2

        # Draw the centimeter ruler
        cm_ruler = Line(start=ORIGIN, end=RIGHT * ruler_length_cm * scale_factor, stroke_width=2).move_to(UP * 1.5)
        self.play(Create(cm_ruler))
        
        # Draw centimeter markings on the top ruler
        cm_marks = VGroup()
        for i in range(0, ruler_length_cm + 1):
            if i % 5 == 0:
                mark_length = 0.4
            else:
                mark_length = 0.2
            mark = Line(start=UP * mark_length, end=ORIGIN).move_to(cm_ruler.point_from_proportion(i / ruler_length_cm))
            cm_marks.add(mark)
        self.play(*[Create(mark) for mark in cm_marks])
        
        # Add centimeter labels every 5 cm on the top ruler
        cm_labels = VGroup()
        for i in range(0, ruler_length_cm + 1, 5):
            label = Text(f"{i} cm", font_size=24).next_to(cm_marks[i], UP)
            cm_labels.add(label)
        self.play(*[Write(label) for label in cm_labels])
        
        # Draw inch ruler below centimeter ruler
        inch_ruler = Line(start=ORIGIN, end=RIGHT * ruler_length_cm * scale_factor, stroke_width=2).next_to(cm_ruler, DOWN, buff=1.5)
        self.play(Create(inch_ruler))
        
        # Draw inch markings on the bottom ruler
        inch_marks = VGroup()
        inch_length = 15 / 2.54
        for i in range(0, int(inch_length) + 1):
            if i % 2 == 0:
                mark_length = 0.3
            else:
                mark_length = 0.15
            proportion = i * 2.54 / ruler_length_cm
            if proportion <= 1:  # Ensure the proportion is within the ruler's length
                mark = Line(start=DOWN * mark_length, end=ORIGIN).move_to(inch_ruler.point_from_proportion(proportion))
                inch_marks.add(mark)
        self.play(*[Create(mark) for mark in inch_marks])
        
        # Add inch labels every inch on the bottom ruler
        inch_labels = VGroup()
        for i in range(0, int(inch_length) + 1, 1):
            proportion = i * 2.54 / ruler_length_cm
            if proportion <= 1:  # Ensure the proportion is within the ruler's length
                label = Text(f"{i}\nin", font_size=16).next_to(inch_ruler.point_from_proportion(proportion), DOWN)
                inch_labels.add(label)
        self.play(*[Write(label) for label in inch_labels])

        # Draw the pencil with a simple triangular nib
        pencil_length_cm = 10  # Length of the pencil in cm
        pencil_body = Rectangle(height=0.2, width=(pencil_length_cm - 1) * scale_factor, color=BLUE, fill_opacity=1)
        pencil_nib = Polygon(
            pencil_body.get_right()+UP*0.1,
            pencil_body.get_right() + RIGHT * 0.5 * scale_factor, 
            pencil_body.get_right() + DOWN * 0.1, 
            color=ORANGE, fill_opacity=1
        )
        pencil = VGroup(pencil_body, pencil_nib)
        pencil.next_to(cm_ruler, DOWN, buff=0.3)  # Position the pencil below the ruler
        pencil.shift(LEFT * 0.5)  # Shift pencil to start from 0 cm mark
        self.play(FadeIn(pencil))

        # Show measurement label
        measurement_label = Text(f"{pencil_length_cm} cm", font_size=24, color=YELLOW)
        measurement_label.next_to(pencil, DOWN, buff=0.1)
        self.play(Write(measurement_label))

        self.wait(2)
        
        # Fade out all elements
        all_elements = VGroup(cm_ruler, cm_marks, cm_labels, inch_ruler, inch_marks, inch_labels, pencil, measurement_label)
        self.play(FadeOut(all_elements))
        self.wait(1)

    def Anim3(self):
        title = Text("Find the Distance Between Buildings A and C", font_size=48).to_edge(UP)
        self.play(Write(title))

        # Define scale factor for visualization
        scale_factor = 0.05  # Adjusted to keep all buildings on screen

        # Define building parameters
        building_height_m = 20
        building_width_m = 10
        building_color = BLUE

        def create_building(height, width, color, label):
            building = Rectangle(height=height * scale_factor, width=width * scale_factor, color=color, fill_opacity=1)
            windows = VGroup()
            for y in range(0, height, 2):  # Windows every 2 meters
                for x in range(-width // 2 + 1, width // 2):
                    window = Rectangle(height=1 * scale_factor, width=1 * scale_factor, color=WHITE, fill_opacity=0.7)
                    window.move_to(building.get_bottom() + UP * (y * scale_factor + 1 * scale_factor) + RIGHT * (x * scale_factor))
                    windows.add(window)
            building_label = Text(label, font_size=24).next_to(building, DOWN)
            return VGroup(building, windows, building_label)

        # Create buildings with windows
        building_left = create_building(building_height_m, building_width_m, building_color, "A")
        building_middle = create_building(building_height_m, building_width_m, building_color, "B")
        building_right = create_building(building_height_m, building_width_m, building_color, "C")

        # Position buildings
        building_middle.move_to(ORIGIN)
        building_left.next_to(building_middle, LEFT*0.6, buff=9.0)  # Adjusted buffer to keep left building on screen
        building_right.next_to(building_middle, RIGHT*0.5, buff=7.5)  # 150 m distance

        # Animate buildings appearing
        self.play(FadeIn(building_left), FadeIn(building_middle), FadeIn(building_right))
        self.wait(1)

        # Create distance labels
        distance_450m = Tex("450 m", font_size=24).move_to(midpoint(building_left[0].get_right(), building_middle[0].get_left())).shift(UP * 0.5)
        distance_150m = Tex("150 m", font_size=24).move_to(midpoint(building_middle[0].get_right(), building_right[0].get_left())).shift(UP * 0.5)

        # Create distance lines
        distance_line_450m = Line(start=building_left[0].get_right(), end=building_middle[0].get_left())
        distance_line_150m = Line(start=building_middle[0].get_right(), end=building_right[0].get_left())

        # Animate distance labels and lines
        self.play(Create(distance_line_450m), Write(distance_450m))
        self.wait(1)
        self.play(Create(distance_line_150m), Write(distance_150m))
        self.wait(1)

        # Create and show the addition
        addition_450 = Tex("450 m", font_size=36).to_edge(LEFT).shift(DOWN * 2)
        plus_sign = Tex("+", font_size=36).next_to(addition_450, RIGHT, buff=0.5)
        addition_150 = Tex("150 m", font_size=36).next_to(plus_sign, RIGHT, buff=0.5)
        equals_sign = Tex("=", font_size=36).next_to(addition_150, RIGHT, buff=0.5)
        result_600 = Tex("600 m", font_size=36).next_to(equals_sign, RIGHT, buff=0.5)
        self.play(Write(addition_450), Write(plus_sign), Write(addition_150), Write(equals_sign), Write(result_600))
        self.wait(2)

        # Create the total distance line
        total_distance_line = Line(start=building_left.get_left(), end=building_right.get_right()).shift(DOWN)
        total_distance_label = Tex("600 m", font_size=24).next_to(total_distance_line, DOWN, buff=0.1)

        # Animate the total distance line
        self.play(Create(total_distance_line), Write(total_distance_label))
        self.wait(2)

        # Fade out all elements
        all_elements = VGroup(addition_450, plus_sign, addition_150, equals_sign, result_600, total_distance_line, total_distance_label,total_distance_label, total_distance_line)
        self.play(FadeOut(all_elements))
        self.wait(1)

    def midpoint(p1, p2):
        return (p1 + p2) / 2

   
               
if __name__ == "__main__":
    scene = Grade4Chapter8HowLongisThis()
    scene.render()
    