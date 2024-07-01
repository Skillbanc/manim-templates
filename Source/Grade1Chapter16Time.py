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


class Grade1TimeChapter(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.introduction()
        self.fadeOutCurrentScene()
        self.intro()
        self.fadeOutCurrentScene()
        self.intro1()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
     
    def SetDeveloperList(self):  
        self.DeveloperList="Vasudha"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade1Chapter16Time.py"    
    
    def introduction(self):
         # Create and display the title
        title = Text("TIME", font_size=40)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))   
        
    def intro(self):
        
        # Create and display the title
        title = Text("Learning to Tell Time", font_size=20)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        def create_clock():
            # Create the clock face (a white circle)
            clock_face = Circle(radius=2, color=WHITE)
            
            # Add numbers around the clock face
            numbers = VGroup(*[
                Text(str(num), font_size=24).move_to(
                    clock_face.point_at_angle(TAU * (0.25 - num / 12))
                )
                for num in range(1, 13)
            ])
            
            # Create hour and minute hands
            hour_hand = Line(ORIGIN, UP).scale(1.2).set_color(BLUE)
            minute_hand = Line(ORIGIN, UP).scale(1.6).set_color(RED)
            
            # Group all clock elements
            clock = VGroup(clock_face, numbers, hour_hand, minute_hand)
            
            return clock, hour_hand, minute_hand

        # Create the clock
        clock, hour_hand, minute_hand = create_clock()
        
        # Add clock to the scene
        self.play(Create(clock))
        
        # Explain the clock hands
        hour_text = Text("Hour hand", color=BLUE, font_size=28).next_to(clock, DOWN, buff=0.5)
        minute_text = Text("Minute hand", color=RED, font_size=28).next_to(hour_text, DOWN, buff=0.5)
        
        self.play(Write(hour_text), Indicate(hour_hand, color=BLUE, scale_factor=1.2))
        self.play(Write(minute_text), Indicate(minute_hand, color=RED, scale_factor=1.2))
        self.wait(2)

        # Show different times
        times = [
            (3, 0, "12:15"),
            (6, 30, "8:00"),
            (9, 45, "1:30"),
            (12, 15, "4:30")
        ]

        for hour, minute, time_str in times:
            # Calculate angles for hour and minute hands
            hour_angle = TAU * ((hour % 12 + minute / 60) / 12 - 1/4)
            minute_angle = TAU * (minute / 60 - 1/4)
            
            # Animate the clock hands
            self.play(
                Rotate(hour_hand, angle=hour_angle, about_point=ORIGIN),
                Rotate(minute_hand, angle=minute_angle, about_point=ORIGIN),
                run_time=1
            )
            
            # Show the time
            time_text = Text(f"This shows {time_str}", font_size=32).next_to(clock, DOWN, buff=1.5)
            self.play(Transform(hour_text, time_text), FadeOut(minute_text))
            self.wait(2)

        # Conclusion
        conclusion = Text("Now you can read different times!", font_size=32).next_to(clock, DOWN, buff=1.5)
        self.play(Transform(hour_text, conclusion))
        self.wait(3)
        
    def intro1(self):
        # Define heading for the amount to be paid to the bus agency
        heading = Text("what we do in day", font_size=20, color=RED)
        heading.to_edge(UP)
        self.play(FadeIn(heading))
        p10=cvo.CVO().CreateCVO("6:30AM","we wake up ").setPosition([-3.5,2,0])
        p11=cvo.CVO().CreateCVO("7:00AM","we take a bath and get ready").setPosition([-1,2,0])
        p12=cvo.CVO().CreateCVO("8:00AM","eating breakfast").setPosition([3,2,0])
        p13=cvo.CVO().CreateCVO("8:30AM","go to school").setPosition([3,-0.5,0])
        p14=cvo.CVO().CreateCVO("3:00PM","come back to home").setPosition([-1,-0.5,0])
        p15=cvo.CVO().CreateCVO("3:30PM","freshup again").setPosition([-3.5,-0.5,0]).setangle(-TAU/4)
        p16=cvo.CVO().CreateCVO("4:00PM","playing games and doing homework").setPosition([-3.5,-3,0]).setangle(-TAU/4)
        p17=cvo.CVO().CreateCVO("8:00PM"," dinner time").setPosition([-1,-3,0]).setangle(-TAU/4)
        p18=cvo.CVO().CreateCVO("8:30PM","we sleep").setPosition([3,-3,0]).setangle(-TAU/4)
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
    scene = Grade1TimeChapter()
    scene.render()
