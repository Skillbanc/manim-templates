# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla
# Project: Manim-Templates
import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

config.max_files_cached = 800  # Change this number to your desired value


class Grade1Chapter16Time(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.time()
        self.fadeOutCurrentScene()
        self.Hour()
        self.fadeOutCurrentScene()
        self.Minutes()
        self.fadeOutCurrentScene()
        self.intro()
        self.fadeOutCurrentScene()
        self.intro1()
        self.fadeOutCurrentScene()
        self.intro2()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
     
    def SetDeveloperList(self):  
        self.DeveloperList="Vasudha"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade1Chapter16Time.py"   
        
    def time(self):
        p10=cvo.CVO().CreateCVO("Time", "").setPosition([-3,1.5,0])
        p11=cvo.CVO().CreateCVO("Definition", "Time helps us understand when things happen\nand how long they take.").setPosition([2,-1.5,0])
        
        p10.cvolist.append(p11)
        
        self.construct1(p10,p10)
        
    def Hour(self):
        title = Text("Hours", font_size=36).to_edge(UP)
        self.play(Create(title))
        self.isRandom = False
        self.angleChoice = [TAU/4]
        p10 = cvo.CVO().CreateCVO("Hours", "1").setPosition([-2,0,0])
        p11 = cvo.CVO().CreateCVO("Minutes", "60").setPosition([2,0,0])
    
        p10.cvolist.append(p11)
    
        p10.setcircleradius(1)
        
        p11.setcircleradius(1)
   
        self.setNumberOfCirclePositions(2)
        self.construct1(p10, p10)


    def Minutes(self):
        title = Text("Minutes", font_size=36).to_edge(UP)
        self.play(Create(title))
        
        self.isRandom = False
        self.angleChoice = [TAU/4]
        p10=cvo.CVO().CreateCVO("Minutes", "1").setPosition([-2,0,0])
        p11=cvo.CVO().CreateCVO("Seconds", "60").setPosition([2,0,0])
        p10.cvolist.append(p11)
        
        p10.setcircleradius(1)
        p11.setcircleradius(1)
       
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)

    def intro(self):
        title = Text("Minutes", font_size=36).to_edge(UP)
        self.play(Create(title))
        
        circle = Circle(radius=2, color=WHITE)
    
        # Add numbers inside the clock with correct positioning
        numbers = VGroup()
        for i in range(1, 13):  # Start from 12, go counter-clockwise
            angle = i * TAU / 12  # Start from top (12 o'clock position)
            number = Text(str(i), font_size=24)
            number_pos = circle.get_center() + 1.7 * np.array([np.sin(angle), np.cos(angle), 0])
            number.move_to(number_pos)
            numbers.add(number)

        # Create clock hands (one-sided arrows)
        hour_hand = Arrow(start=ORIGIN, end=UP, buff=0, color=BLUE).scale(0.8)
        minute_hand = Arrow(start=ORIGIN, end=UP, buff=0, color=GREEN).scale(1.2)
        second_hand = Arrow(start=ORIGIN, end=UP, buff=0, color=RED).scale(1.4)

        # Rotate hands to show a specific time (e.g., 3:25:45)
        hour_hand.rotate(angle=-PI/2 + (3/12 + 25/720) * 2*PI, about_point=ORIGIN)
        minute_hand.rotate(angle=-PI/2 + (25/60) * 2*PI, about_point=ORIGIN)
        second_hand.rotate(angle=-PI/2 + (45/60) * 2*PI, about_point=ORIGIN)

        hands = VGroup(hour_hand, minute_hand, second_hand)

        # Create rectangular box for hand labels
        box = Rectangle(height=1.5, width=4, color=WHITE).to_corner(UR, buff=0.5)
    
        # Create hand labels
        hour_label = Text("Hour hand", color=BLUE, font_size=24)
        minute_label = Text("Minute hand", color=GREEN, font_size=24)
        second_label = Text("Second hand", color=RED, font_size=24)
    
        labels = VGroup(hour_label, minute_label, second_label).arrange(DOWN, aligned_edge=LEFT).move_to(box)
    
        # Group box and labels
        box_group = VGroup(box, labels)

        # Animate the clock elements one by one
        self.play(Create(circle))
        self.wait(0.5)
    
        self.play(Write(numbers))
        self.wait(0.5)
    
        self.play(Create(hands))
        self.wait(0.5)

        # Animate the box and labels
        self.play(Create(box), Write(labels))

        # Display for 5 seconds
        self.wait(5)
    
    def intro1(self):
        title = Text("Let us learn how to tell time", font_size=36).to_edge(UP)
        self.play(Create(title))
        
         # Create the clock and initial time
        clock, hour_hand, minute_hand = self.create_clock()
        label = Text("1:00").scale(0.5).next_to(clock, DOWN)
        
        self.play(Create(clock), Write(label))
        self.wait(1)

        # Create the clock and initial time
        initial_time = "1:00"
        time_label_prefix = "It is showing "
        final_time = "pm"
        time_label = Text(f"{time_label_prefix}{initial_time}{final_time}").scale(0.5).next_to(clock, LEFT, buff=1)
        time_box = SurroundingRectangle(time_label, color=WHITE, buff=0.2)
        
        self.play( Write(time_label), Create(time_box))
        self.wait(1)

        # Define times and corresponding transformations
        times = [
            (1, 0, "1:00"), 
            (1, 15, "1:15"), 
            (2, 30, "2:30"), 
            (2, 45, "2:45"), 
            (3, 0, "3:00"), 
            (3, 15, "3:15")
        ]
        
        for hour, minute, time_text in times:
            new_hour_hand, new_minute_hand = self.create_clock_hands(hour, minute)
            new_label = Text(time_text).scale(0.5).next_to(clock, DOWN)
            new_time_label = Text(f"{time_label_prefix}{time_text}{final_time}").scale(0.5).move_to(time_label, LEFT)
            new_time_box = SurroundingRectangle(new_time_label, color=WHITE, buff=0.2).move_to(time_box)

            self.play(
                Transform(hour_hand, new_hour_hand), 
                Transform(minute_hand, new_minute_hand), 
                Transform(label, new_label),
                Transform(time_label, new_time_label), 
                Transform(time_box, new_time_box)
            )
            self.wait(2)

    def create_clock(self):
        clock = VGroup()
        circle = Circle(radius=2, color=WHITE)

        # Add numbers inside the clock
        numbers = VGroup()
        for num in range(1, 13):
            angle = TAU * (0.25 - num / 12)
            number_position = circle.point_at_angle(angle) * 0.8
            number = Text(str(num), font_size=24).move_to(number_position)
            numbers.add(number)

        # Create clock hands (one-sided arrows)
        hour_hand = Arrow(start=ORIGIN, end=UP * 0.8, buff=0, color=BLUE)
        minute_hand = Arrow(start=ORIGIN, end=UP * 1.2, buff=0, color=GREEN)
        
        clock.add(circle, numbers, hour_hand, minute_hand)
        return clock, hour_hand, minute_hand

    def create_clock_hands(self, hour, minute):
        # Create clock hands (one-sided arrows)
        hour_hand = Arrow(start=ORIGIN, end=UP * 0.8, buff=0, color=BLUE)
        minute_hand = Arrow(start=ORIGIN, end=UP * 1.2, buff=0, color=GREEN)

        # Adjust the rotation of the hands
        hour_angle = (hour % 12 + minute / 60) * 30 * DEGREES
        minute_angle = (minute / 60) * 360 * DEGREES

        hour_hand.rotate(-hour_angle, about_point=ORIGIN)
        minute_hand.rotate(-minute_angle, about_point=ORIGIN)
        
        return hour_hand, minute_hand
        
    def intro2(self):
        # Define heading for the amount to be paid to the bus agency
        heading = Text("what we do in a day", font_size=26, color=RED)
        heading.to_edge(UP)
        self.play(FadeIn(heading))
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("6:30AM","we wake up ").setPosition([-4.5,2,0]).setangle(-TAU/4)
        p11=cvo.CVO().CreateCVO("7:00AM","we take a bath and get ready").setPosition([-2,2,0]).setangle(-TAU/4)
        p12=cvo.CVO().CreateCVO("8:00AM","eating breakfast").setPosition([2,2,0]).setangle(-TAU/4)
        p13=cvo.CVO().CreateCVO("8:30AM","go to school").setPosition([4.5,2,0]).setangle(-TAU/4)
        p14=cvo.CVO().CreateCVO("3:00PM","come back to home").setPosition([4.5,0,0]).setangle(-TAU/4)
        p15=cvo.CVO().CreateCVO("3:30PM","freshup again").setPosition([4.5,-2.5,0]).setangle(-TAU/4)
        p16=cvo.CVO().CreateCVO("4:00PM","playing games and doing homework").setPosition([2,-2.5,0]).setangle(-TAU/4)
        p17=cvo.CVO().CreateCVO("8:00PM"," dinner time").setPosition([-2,-2.5,0]).setangle(-TAU/4)
        p18=cvo.CVO().CreateCVO("8:30PM","we sleep").setPosition([-4.5,-2.5,0]).setangle(-TAU/4)
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        p13.cvolist.append(p14)
        p14.cvolist.append(p15)
        p15.cvolist.append(p16)
        p16.cvolist.append(p17)
        p17.cvolist.append(p18)
        
    
        self.construct1(p10,p10)    
    
if __name__ == "__main__":
    scene = Grade1Chapter16Time()
    scene.render()
