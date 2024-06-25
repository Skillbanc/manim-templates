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

class TimeAnim(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.Time()
        self.Hour()
        self.Minutes()
        self.ExampleTime()
        self.TimeMeasure()
        self.TimeConversion()
        self.ExampleConversion()
        self.GithubSourceCodeReference()

        
        # self.fadeOut()
        # self.constructDataByJSON()
        # self.fadeOut()
        
    def SetDeveloperList(self):  
        self.DeveloperList="Hriday Bhushan"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Chap12Class5TimeAnim.py"
    
    # render using CVO data object
    def Time(self):
        title = Text("Time", font_size=36).to_edge(UP)
        self.play(Create(title))
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Time","")
        p11=cvo.CVO().CreateCVO("Definition","Continued sequence of existence and events")
        
        p10.setcircleradius(1.2)
        p11.setcircleradius(1.2)
        p10.cvolist.append(p11)
        
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()


    def Hour(self):
        title = Text("Hours", font_size=36).to_edge(UP)
        self.play(Create(title))
        self.isRandom = False
        self.angleChoice = [TAU/2]
        p10=cvo.CVO().CreateCVO("1 Hour", "").setPosition([-4.5,1.5,0])
        p11=cvo.CVO().CreateCVO("Consists of", "60 Minutes").setPosition([-4.5,-1.5,0])
        
        p10.cvolist.append(p11)
        
        p10.setcircleradius(1)
        p11.setcircleradius(1)
       
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)


        # Create clock face
        clock_face = Circle(radius=2, color=WHITE)
        self.play(Create(clock_face))

        # Create hour and minute labels
        hour_labels = VGroup()
        for hour in range(1, 13):
            angle = (hour / 12) * TAU  # Convert hour to angle in radians
            label = Text(str(hour), font_size=24)
            label.move_to(2.3 * np.array([np.sin(angle), np.cos(angle), 0]))
            hour_labels.add(label)

        

        self.play(Create(hour_labels))
        

        # Create hour, minute, and second hands
        hour_hand = Line(ORIGIN, 0.5 * UP, color=RED, stroke_width=8)
        minute_hand = Line(ORIGIN, RIGHT, color=BLUE, stroke_width=6)
        second_hand = Line(ORIGIN, 1.2 * DOWN, color=GREEN, stroke_width=4)
        self.play(Create(hour_hand))
        self.wait(2)
        self.play(Create (minute_hand))
        self.wait(2)
        self.play(Create(second_hand))
        self.wait(2)

        # Animation of the clock
        def update_clock(mob, dt):
            # Update time
            mob.second += dt
            total_seconds = mob.second
            # Calculate the angles for each hand
            hour_angle =  PI * (total_seconds / 3600) / 12
            minute_angle = -2 * PI * (total_seconds / 60) / 60
            second_angle = -4 * PI * (total_seconds % 60) / 60
            # Rotate hands
            hour_hand.set_angle(hour_angle)
            minute_hand.set_angle(minute_angle)
            second_hand.set_angle(second_angle)

        clock = VGroup(hour_hand, minute_hand, second_hand)
        clock.second = 0
        clock.add_updater(update_clock)

        self.add(clock)
        self.wait(5)  # Run the animation for 5 seconds
        
        
        self.fadeOutCurrentScene()

    
    def Minutes(self):
        title = Text("Minutes", font_size=36).to_edge(UP)
        self.play(Create(title))
        
        self.isRandom = False
        self.angleChoice = [TAU/2]
        p10=cvo.CVO().CreateCVO("1 Minute", "").setPosition([-4.5,1.5,0])
        p11=cvo.CVO().CreateCVO("Consists of", "60 Seconds").setPosition([-4.5,-1.5,0])
        p10.cvolist.append(p11)
        
        p10.setcircleradius(1)
        p11.setcircleradius(1)
       
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)

        
        # Create clock face
        clock_face = Circle(radius=2, color=WHITE)
        self.play(Create(clock_face))


        minute_labels = VGroup()
        for minute in range(5, 61, 5):
            angle = (minute / 60) * TAU  # Convert minute to angle in radians
            label = Text(str(minute), font_size=16, color=YELLOW)
            label.move_to(2.3 * np.array([np.sin(angle), np.cos(angle), 0]))
            minute_labels.add(label)

        
        self.play(Create(minute_labels))

        # Create hour, minute, and second hands
        hour_hand = Line(ORIGIN, 0.5 * UP, color=RED, stroke_width=8)
        minute_hand = Line(ORIGIN, RIGHT, color=BLUE, stroke_width=6)
        second_hand = Line(ORIGIN, 1.2 * DOWN, color=GREEN, stroke_width=4)
        self.play(Create(hour_hand))
        self.wait(2)
        self.play(Create (minute_hand))
        self.wait(2)
        self.play(Create(second_hand))
        self.wait(2)

        # Animation of the clock
        def update_clock(mob, dt):
            # Update time
            mob.second += dt
            total_seconds = mob.second
            # Calculate the angles for each hand
            hour_angle =  PI * (total_seconds / 3600) / 12
            minute_angle = -2 * PI * (total_seconds / 60) / 60
            second_angle = -4 * PI * (total_seconds % 60) / 60
            # Rotate hands
            hour_hand.set_angle(hour_angle)
            minute_hand.set_angle(minute_angle)
            second_hand.set_angle(second_angle)

        clock = VGroup(hour_hand, minute_hand, second_hand)
        clock.second = 0
        clock.add_updater(update_clock)

        self.add(clock)
        self.wait(5)  # Run the animation for 5 seconds
        

        self.fadeOutCurrentScene()
    
    def ExampleTime(self):
        self.isRandom=False
        self.angleChoice=[TAU/2]
        p10=cvo.CVO().CreateCVO("1 Hour", "").setPosition([4.5,1.5,0])
        p11=cvo.CVO().CreateCVO("Consists of", "60 Minutes").setPosition([4.5,-1.5,0])
        
        p10.cvolist.append(p11)
        
        p10.setcircleradius(1)
        p11.setcircleradius(1)
       
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)

        title1 = Text("Example: Converting Hours to Minutes", font_size=36).to_edge(UP)
        self.play(Create(title1))
        self.wait(2)
        ex11 = Text("Convert 2Hrs 15Mins to minutes", font_size=26).move_to(LEFT*3 + UP*1.5)
        self.play(Create(ex11))
        self.wait(2)
        ex12 = Text("2Hrs = 2 * 60Mins", font_size=26).next_to(ex11, DOWN*1.5)
        self.play(Create(ex12))
        self.wait(2)
        ex13 = Text("2Hrs 15Mins = 120 + 15 Mins", font_size=26).next_to(ex12, DOWN*1.5)
        self.play(Create(ex13))
        self.wait(2)
        ex14 = Text("2Hrs 15Mins = 135 Mins", font_size=26).next_to(ex13, DOWN*1.5)
        self.play(Create(ex14))
        self.wait(2)
        self.fadeOutCurrentScene()


    def TimeMeasure(self):
        self.isRandom=False
        title = Text("12-Hour and 24-Hour Time", font_size=36).to_edge(UP)
        self.play(Create(title))
        p10=cvo.CVO().CreateCVO("Time","")
        p11=cvo.CVO().CreateCVO("12-Hour Format","")
        p11onamelist=["two 12-hour cycles per day","AM - Before noon", "PM - After noon"]
        p11.extendOname(p11onamelist)
        p12=cvo.CVO().CreateCVO("24-Hour Format","")
        p12onamelist=["Runs from midnight to midnight","AM and PM not required"]
        p12.extendOname(p12onamelist)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()


    def TimeConversion(self):
        # Title
        title = Text("12-Hour to 24-Hour Time Conversion", font_size=36).to_edge(UP)
        self.play(Create(title))

        groundlevel = Line(config.left_side/1.05, config.right_side/1.05)
        # Define the width of the canvas in Manim units
        canvas_width = config.frame_width - 1.2
        

        # 12-Hour time labels
        twelve_hour_times = [
            "12AM", "1AM", "2AM", "3AM", "4AM", "5AM",
            "6AM", "7AM", "8AM", "9AM", "10AM", "11AM",
            "12PM", "1PM", "2PM", "3PM", "4PM", "5PM",
            "6PM", "7PM", "8PM", "9PM", "10PM", "11PM"
        ]

        twelve_hour_labels = VGroup()
        for i, label in enumerate(twelve_hour_times):
            text = Text(label, font_size=17, color=YELLOW)
            x_pos = (i / 23) * (canvas_width) - (canvas_width / 2)  # Adjust position within the canvas
            text.move_to(x_pos * RIGHT + 2 * UP)
            twelve_hour_labels.add(text)

        # 24-Hour time labels
        twenty_four_hour_labels = VGroup()
        for i in range(24):
            label = Text(f"{i:02}:00", font_size=17, color=PINK)
            x_pos = (i / 23) * (canvas_width) - (canvas_width / 2)  # Adjust position within the canvas
            label.move_to(x_pos * RIGHT + 2 * DOWN)
            twenty_four_hour_labels.add(label)

        self.play(Create(twelve_hour_labels))
        self.play(Create(twenty_four_hour_labels))
        self.play(Create(groundlevel))

        # Connecting lines
        lines = VGroup()
        for i in range(24):
            x_pos = (i / 23) * (canvas_width) - (canvas_width / 2)  # Adjust position within the canvas
            line = Line(
                start=x_pos * RIGHT + 1.5 * UP,
                end=x_pos * RIGHT + 1.5 * DOWN,
                color=RED
            )
            lines.add(line)


        self.play(Create(lines))

        self.wait(4)

        self.fadeOutCurrentScene()
       
    def ExampleConversion(self):
         # Title
        title = Text("Example: Time Conversion").scale(1.2)
        title.to_edge(UP)
        self.play(Create(title))
        self.wait(1)
        
        
        # Create table headers
        headers = ["Time (12 hours clock)", "Time (24 hours clock)"]
        table_header = VGroup(*[Text(header) for header in headers]).arrange(RIGHT, buff=2)
        table_header.shift(UP * 2)
        self.play(Write(table_header))

        # 12-hour clock times
        times_12h = ["6:00 AM", "1:30 PM", "4:30 PM", "8:00 PM", "5:30 AM"]
        times_12h_mob = VGroup(*[Text(time) for time in times_12h]).arrange(DOWN*1.5, aligned_edge=LEFT)
        times_12h_mob.next_to(table_header[0], DOWN, aligned_edge=LEFT)

        # 24-hour clock times
        times_24h = ["06:00 Hours", "13:30 Hours", "16:30 Hours", "20:00 Hours", "5:30 Hours"]
        times_24h_mob = VGroup(*[Text(time) for time in times_24h]).arrange(DOWN*1.5, aligned_edge=LEFT)
        times_24h_mob.next_to(table_header[1], DOWN, aligned_edge=LEFT)

        # Display initial times
        self.play(Write(times_12h_mob), Write(times_24h_mob))
        
       
        self.wait(2)
        self.fadeOutCurrentScene

    
if __name__ == "__main__":
    scene = TimeAnim()
    scene.render()