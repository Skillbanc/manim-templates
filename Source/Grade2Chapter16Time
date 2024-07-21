# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
import random  # Import the random module
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo

class Grade2Ch16Time(AbstractAnim):
    
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.Time()
        self.fadeOutCurrentScene()
        self.intro()
        self.fadeOutCurrentScene()
        self.weeks()
        self.fadeOutCurrentScene()
        self.months()
        self.fadeOutCurrentScene()
        self.anim()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference() 
        
    def SetDeveloperList(self):
        # return super().SetDeveloperList()
        self.DeveloperList="Bharathi Priyadarshini"
        
    def SetSourceCodeFileName(self):
        # return super().SetSourceCodeFileName()
        self.SourceCodeFileName="Grade2Chapter16Time"
    
    def Time(self):
         self.isRandom=False
         self.angleChoice = [TAU/4]
         self.colorChoice=[PINK,GREY_BROWN]
         p1 = cvo.CVO().CreateCVO("Time", "").setPosition([-4,0,0])
         p2 = cvo.CVO().CreateCVO("Definition", "Time helps us understand when things happen and how long they take.").setPosition([3,0,0])
         p1.cvolist.append(p2)
         p2.setcircleradius(1.5)  
         self.setNumberOfCirclePositions(2)
         self.construct1(p1,p1)
         self.wait(3)
    
    def intro(self):
        t1 = Text("Time",font_size=40,color=PINK)
        t1.move_to([-6,3, 0])
        self.play(Write(t1))
        t2= Text("Time helps us understand when things happen and how long they take. ",font_size=23)
        t2.move_to([-1.8,2, 0])
        self.play(Write(t2))
        t3 = Text("It's like a big clock in the sky that keeps ticking, so we know if it's morning, afternoon, or bedtime.",font_size=23)
        t3.move_to([-0,1, 0])
        self.play(Write(t3))
        self.wait(3)

    def weeks(self):
        # self.play(Write(NumberPlane()))
        title = Text("Names of days in a week", font_size=25,color=PINK)
        title.move_to([-5, 3.6, 0])
        self.play(Write(title))
        self.wait(1.5)
        t = Text("A week starts from sunday ", font_size=20)
        t.move_to([-5.5, 3, 0])
        self.play(Write(t))
        self.wait(1.5)
        # Main circle, moved slightly to the left
        main_circle = Circle(radius=3, color=WHITE)
        main_circle.shift(LEFT * 2)
        self.add(main_circle)
        
        # Define the angles for the segments
        segment_angles = [TAU / 7] * 7
        
        # Create segments
        for i in range(7):
            angle = sum(segment_angles[:i])
            arc = Arc(radius=3, start_angle=angle, angle=segment_angles[i], color=WHITE)
            arc.shift(LEFT * 2)
            line = Line(start=main_circle.get_center(), end=arc.get_start(), color=WHITE)
            self.add((arc),(line))
        
        # Draw the final line to close the circle
        self.play(Create(Line(main_circle.get_center(), arc.get_end(), color=WHITE)))
        
        # Position and label the days, shifted accordingly
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        positions = [
            [0.5, 2.5, 0], [2, 1, 0], [2, -0.9, 0], [0.5, -2.5, 0],
            [-1.5, -1.9, 0], [-2, 0, 0], [-1.5, 1.9, 0]
        ]
        for day, pos in zip(days, positions):
            day_text = Text(day, font_size=20)
            day_text.move_to(pos + LEFT * 2)
            self.play(Write(day_text))
            self.wait(1)

        arrow1 = Arrow(start=[-4.5, 2.1, 0], end=[-3.3, 3, 0], color=WHITE)
        
        arrow2 = Arrow(start=[-0.5, 2.9, 0], end=[0.5, 2, 0], color=WHITE)
        self.play(Create(arrow2))
        arrow3 = Arrow(start=[0.5, -2.2, 0], end=[-0.9, -3.1, 0], color=WHITE)
        self.play(Create(arrow3))
        arrow4 = Arrow(start=[-4.3, -2.5, 0], end=[-5.1, -1.4, 0], color=WHITE)
        self.play(Create(arrow4))
        self.play(Create(arrow1))
        self.wait(2)
        t10= Text("EXAMPLE:",font_size=22)
        t10.move_to([4,3.5, 0])
        self.play(Write(t10))
        self.wait(1)
        t10= Text("After how many days does friday come after sunday?",font_size=22)
        t10.move_to([3.5,3, 0])
        self.play(Write(t10))
        self.wait(2)
        t11= Text("Answer: 4 days",font_size=27)
        t11.move_to([4.5,2.3, 0])
        self.play(Write(t11))
        self.wait(3)
        t8 = Text("what is the day after sunday?",font_size=23)
        t8.move_to([4,1, 0])
        self.play(Write(t8))
        self.wait(2)
        t9= Text("Answer: Monday",font_size=27)
        t9.move_to([4.5,0.3, 0])
        self.play(Write(t9))
        self.wait(2)
        
    def months(self):
        title = Text("Look at the months in the picture", font_size=27,color=LIGHT_PINK)
        title.move_to([-4,3.5,0])
        self.play(Write(title))
        t = Text("A Month starts from January ", font_size=20)
        t.move_to([-5.4, 3, 0])
        self.play(Write(t))
        self.wait(1.5)
        # Main circle for the months
        main_circle = Circle(radius=3, color=WHITE)
        main_circle.shift(LEFT * 2)
        self.add(main_circle)

        # Define the angles for the segments (12 months)
        segment_angles = [TAU / 12] * 12

        # Create segments for each month
        for i in range(12):
            angle = sum(segment_angles[:i])
            arc = Arc(radius=3, start_angle=angle, angle=segment_angles[i], color=WHITE)
            arc.shift(LEFT * 2)
            line = Line(start=main_circle.get_center(), end=arc.get_start(), color=WHITE)
            self.add((arc),(line))

        # Draw the final line to close the circle
        self.play(Create(Line(main_circle.get_center(), arc.get_end(), color=WHITE)))

        # Position and label the months, shifted accordingly
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        positions = [
            (0.6,2.1, 0), (1.5, 1.5, 0), (2, 0.5, 0), (2, -0.5, 0), (1.5, -1.5, 0),
            (0.5,-2.5, 0), (-0.5,-2.5, 0), (-1.5, -1.5, 0), (-2, -0.5, 0), (-2, 0.5, 0),
            (-1.5, 1.5, 0), (-0.5,2.5, 0)
        ]
        for month, pos in zip(months, positions):
            month_text = Text(month, font_size=20)
            month_text.move_to(pos + LEFT * 2)
            self.play(Write(month_text))
        arrow1 = Arrow(start=[-4.5, 2.1, 0], end=[-3.3, 3, 0], color=WHITE) 
        arrow2 = Arrow(start=[-0.5, 2.9, 0], end=[0.5, 2, 0], color=WHITE)
        self.play(Create(arrow2))
        arrow3 = Arrow(start=[0.5, -2.2, 0], end=[-0.9, -3.1, 0], color=WHITE)
        self.play(Create(arrow3))
        arrow4 = Arrow(start=[-4.3, -2.5, 0], end=[-5.1, -1.4, 0], color=WHITE)
        self.play(Create(arrow4))
        self.play(Create(arrow1))
        self.wait(2)
        t10= Text("EXAMPLE:",font_size=22)
        t10.move_to([4,3.5, 0])
        self.play(Write(t10))
        self.wait(1)
        t10= Text("Which is the month between April and June?",font_size=22)
        t10.move_to([3.6,3, 0])
        self.play(Write(t10))
        self.wait(2)
        t11= Text("Answer: May",font_size=27)
        t11.move_to([4.5,2.3, 0])
        self.play(Write(t11))
        self.wait(3)
        t8 = Text("Which month comes after july?",font_size=23)
        t8.move_to([4,1, 0])
        self.play(Write(t8))
        self.wait(2)
        t9= Text("Answer: August",font_size=27)
        t9.move_to([4.5,0.3, 0])
        self.play(Write(t9))
        self.wait(2)

    def anim(self):
        # self.play(Write(NumberPlane()))
        t0 = Text("Put tick for the one which goes faster",font_size=30)
        t0.move_to([-3,3.5, 0])
        self.play(Write(t0))
        activities = [
            ("🚲", BLUE),      # Cycle
            ("🏍️",WHITE)   # Bike
        ]

        # Create Text objects for each emoji with reduced font size and color
        emoji_objs = [Text(emoji, font_size=90, color=color) for emoji, color in activities]

        # Position emojis in a horizontal line with spacing
        for i, emoji in enumerate(emoji_objs):
            emoji.move_to(np.array([-1.5 + i * 3, 1, 0]))

        # Add emojis to the scene
        self.play(*[Write(emoji) for emoji in emoji_objs])
        self.wait(2)
        t1 = Text("cycle",font_size=30)
        t1.move_to([-1.5,2, 0])
        t2 = Text("Bike",font_size=30)
        t2.move_to([1.5,2, 0])
        
        # Create boxes under both emojis
        box_tick_group = VGroup()

        for emoji_obj in emoji_objs:
            # Create a box under the emoji
            box = Rectangle(
                width=emoji_obj.get_width() + 0.5,
                height=0.6,
                stroke_width=2
            )
            box.move_to(emoji_obj.get_center() + DOWN * 1.5)

            # Add box to group
            box_tick_group.add(box)

        # Create a tick mark inside the box under the bike emoji
        tick = VGroup(
            Line(ORIGIN, [0.2, -0.2, 0], color=GREEN),
            Line([0.2, -0.2, 0], [0.5, 0.3, 0], color=GREEN)
        )
        tick.scale(1.5)  # Scale the tick mark
        tick.move_to(box_tick_group[1].get_center())  # Move tick to center of bike box
        
        t3 = Text("Bike is faster than cycle",font_size=30)
        t3.move_to([-0.5,-2, 0])
        
        # Add the tick mark to the scene
        self.add((t1),(t2),(box_tick_group))
        self.wait(2)
        self.play(Write(t3))
        self.wait(1)
        self.play(Create(tick))
        self.wait(3)
        
if __name__ == "__main__":
    scene = Grade2Ch16Time()
    scene.render()