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
        self.PatternWithTurns()
        self.fadeOutCurrentScene()
        self.PatternsWithNumbers()
        self.fadeOutCurrentScene()
        self.PatternsWithCalendars()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        #self.constructDataByJSON()
        #self.fadeOut()
        
    # render using CVO data object
    def constructDataByCVO(self):
        p16=cvo.CVO().CreateCVO("Patterns","").setPosition([-3.5,-2,0])
        p17=cvo.CVO().CreateCVO("Definition","The repeated design").setPosition([-3.5,2,0]).setangle([-TAU/4])
        p18=cvo.CVO().CreateCVO("Patterns with Turn","").setPosition([3.5,2,0]).setangle([-TAU/4])
        p19=cvo.CVO().CreateCVO("Patterns with Numbers","").setPosition([3.5,-2,0]).setangle([-TAU/4])
        p20=cvo.CVO().CreateCVO("Patterns with Calendar","").setPosition([0,0,0]).setangle([-TAU/4])
        
        p16.cvolist.append(p17)
        p16.cvolist.append(p18)
        p16.cvolist.append(p19)
        p16.cvolist.append(p20)
        self.isRandom=False        
        self.setNumberOfCirclePositions(5)
        self.construct1(p16,p16)
    def PatternWithTurns(self):
        title = Text("Patterns with Turns")
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Arrow 1
        arrow1 = Arrow(start=DOWN, end=UP)
        # Arrow 2
        arrow2 = Arrow(start=UP, end=DOWN)
        # Arrow 3
        arrow3 = Arrow(start=DOWN, end=UP)
        # Arrow 4
        arrow4 = Arrow(start=UP, end=DOWN)

        # Arrange the arrows
        arrows = VGroup(arrow1, arrow2, arrow3, arrow4,arrow1,arrow2,arrow3)
        arrows.arrange(RIGHT, buff=1.5).shift(DOWN)

        # Animate the appearance of each arrow
        for arrow in arrows:
            self.play(FadeIn(arrow))
            self.wait(1)

        self.wait(2)
    def PatternsWithNumbers(self):
        # Title
        title = Text("Patterns with Numbers")
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Number 1 to 6
        numbers = [Text(str(num)) for num in [27, 30, 33, 36, 39, 42]]
        numbers_vgroup = VGroup(*numbers)
        numbers_vgroup.arrange(RIGHT, buff=1.0).shift(DOWN)

        # Animate the appearance of each number
        for number in numbers_vgroup:
            self.play(FadeIn(number))
            self.wait(1)
        
        self.wait(2)

        # Create curved arrows and text above them
        arrows = VGroup()
        texts = VGroup()
        for i in range(len(numbers) - 1):
            start_point = numbers[i].get_right()
            end_point = numbers[i+1].get_left()
            arrow = CurvedArrow(start_point, end_point, angle=-PI/2)  # Adjust the angle to get the desired curve
            arrows.add(arrow)

            # Calculate the position for the text above the arrow
            midpoint = (start_point + end_point) / 2
            text = Text("+3").move_to(midpoint + UP * 0.5)  # Adjust the UP value to position text as needed
            texts.add(text)
        
        # Animate the appearance of each arrow and text
        for arrow, text in zip(arrows, texts):
            self.play(Create(arrow), FadeIn(text))
            self.wait(1)
        
        self.wait(2)
    def PatternsWithCalendars(self):
         # Title
        title = Text("Patterns with Calendars")
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

    # Calendar Dates and Days
        dates = ["1", "8", "15", "22", "29"]
        days = ["Monday", "Monday", "Monday", "Monday", "Monday"]

    # Create Text objects for dates and days
        date_texts = VGroup(*[Text(date) for date in dates])
        day_texts = VGroup(*[Text(day) for day in days])

    # Arrange dates horizontally
        date_texts.arrange(RIGHT, buff=1.5).shift(UP * 1)

    # Arrange days below the dates, with staggered vertical positions to prevent overlap
        for i, (day, date) in enumerate(zip(day_texts, date_texts)):
            day.next_to(date, DOWN, buff=0.3).shift(DOWN * i * 0.3)

    # Animate the appearance of each date and day
        for date, day in zip(date_texts, day_texts):
            self.play(FadeIn(date), FadeIn(day))
            self.wait(1)

        self.wait(2)

    # Create curved arrows and texts for patterns
        arrows = VGroup()
        pattern_texts = VGroup()
        for i in range(len(date_texts) - 1):
            start_point = date_texts[i].get_right()
            end_point = date_texts[i + 1].get_left()
            arrow = CurvedArrow(start_point, end_point, angle=-PI / 2)  # Adjust the angle to get the desired curve
            arrows.add(arrow)

        # Calculate the position for the text above the arrow
            midpoint = (start_point + end_point) / 2
            text = Text("+7").move_to(midpoint + UP * 0.5)  # Adjust the UP value to position text as needed
            pattern_texts.add(text)

    # Animate the appearance of each arrow and text
        for arrow, text in zip(arrows, pattern_texts):
            self.play(Create(arrow), FadeIn(text))
            self.wait(1)

        self.wait(2)
    def SetDeveloperList(self): 
       self.DeveloperList="Preetham" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade4Chapter15Patterns.py"    

    
if __name__ == "__main__":
    scene = Chapter15Grade4()
    scene.render()