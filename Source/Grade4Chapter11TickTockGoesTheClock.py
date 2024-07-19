import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class Time(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.Clock()
        self.fadeOutCurrentScene()
        self.Con()
        self.fadeOutCurrentScene()
        self.Clock4()  
        self.fadeOutCurrentScene()
        self.Clock5()
        self.fadeOutCurrentScene()
        self.Clock2()  
        self.fadeOutCurrentScene()
        self.Clock3()  
        self.fadeOutCurrentScene()
        self.Year()
        self.fadeOutCurrentScene()
        self.year2()
        self.fadeOutCurrentScene()
        self.year3()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
             
  
    def Clock(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Time ","").setPosition([-4,0,0])
        p11=cvo.CVO().CreateCVO("Before Noon", "am").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("After Noon", "pm").setPosition([4,-2,0])
         
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
      
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10) 
    
    def Con(self):
        self.isRandom = False
        self.angleChoice = [TAU/10,TAU/10,TAU/10]
        p10=cvo.CVO().CreateCVO("Day ","1").setPosition([-4,2,0])
        p15=cvo.CVO().CreateCVO("Hours", "24").setPosition([3,2,0])
        p11=cvo.CVO().CreateCVO("Hour", "1").setPosition([-4,0,0])
        p12=cvo.CVO().CreateCVO("Minutes", "60").setPosition([3,0,0])
        p13=cvo.CVO().CreateCVO("Minute", "1").setPosition([-4,-2,0])        
        p14=cvo.CVO().CreateCVO("Seconds", "60").setPosition([3,-2,0])
        p10.cvolist.append(p15)
        p11.cvolist.append(p12)
        p13.cvolist.append(p14)
        self.setNumberOfCirclePositions(6)
        self.construct1(p10,p10)  
        self.construct1(p11,p11)
        self.construct1(p13,p13)

    def Clock4(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Clock ","").setPosition([-4,2,0])
        p11=cvo.CVO().CreateCVO("Smaller Hand", "Hours").setPosition([-4,-2,0])
        p12=cvo.CVO().CreateCVO("Longer Hand", "Minutes").setPosition([0,0,0])
       
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
      
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)

    def Clock5(self):
        self.isRandom = False
        self.angleChoice = [TAU/10,TAU/10,TAU/10]
        p10=cvo.CVO().CreateCVO("Longer Hand ","at 1").setPosition([-4,2,0])
        p15=cvo.CVO().CreateCVO("Minutes", "5").setPosition([3,2,0])
        p11=cvo.CVO().CreateCVO("Longer Hand ", "at 2").setPosition([-4,0,0])
        p12=cvo.CVO().CreateCVO("Minutes", "10").setPosition([3,0,0])
        p13=cvo.CVO().CreateCVO("Longer Hand", "at 3").setPosition([-4,-2,0])        
        p14=cvo.CVO().CreateCVO("Minute", "15").setPosition([3,-2,0])
        p10.cvolist.append(p15)
        p11.cvolist.append(p12)
        p13.cvolist.append(p14)
        self.setNumberOfCirclePositions(6)
        self.construct1(p10,p10)  
        self.construct1(p11,p11)
        self.construct1(p13,p13)
        title = Text("and so on..")
        title.center()
        title.to_edge(DOWN)
        self.play(Write(title))
        self.wait(2)  
        
    def Clock2(self):
        title = Text("Clock").to_edge(UP)
        self.play(Write(title))
        triangle1_vert=[[-0.1, 0, 0],[0.1, 0, 0],[0, 0.2, 0]]
        triangle1 = Polygon(*triangle1_vert, color=RED, fill_opacity=1)
        triangle1.shift(UP* 0.7)
        
        
        triangle2_vert=[[-0.1, 0, 0],[0.1, 0, 0],[0, 0.2, 0]]
        triangle2 = Polygon(*triangle2_vert, color=BLUE, fill_opacity=1)
        triangle2.shift(LEFT * 1.2,DOWN *0.1)

        triangle2.rotate(PI / 2)  
        
       
             
        clock_face = Circle(radius=2, color=WHITE)
        self.play(Create(clock_face))

        hour_labels = VGroup()
        for hour in range(1, 13):
            angle = (hour / 12) * TAU 
            label = Text(str(hour), font_size=24)
            label.move_to(2.3 * np.array([np.sin(angle), np.cos(angle), 0]))
            hour_labels.add(label)

        self.play(Create(hour_labels))
      
        hour_hand = Line(ORIGIN, 0.7 * UP, color=RED, stroke_width=8)
        minute_hand = Line(ORIGIN, LEFT *1.2, color=BLUE, stroke_width=6)
        
        self.play(Create(hour_hand),Create (triangle1))
        self.play(Create(minute_hand),Create (triangle2))
        
        twxt = Text("The time is 12:45").to_edge(DOWN)
        self.play(Write(twxt))
        self.wait(5)

    def Clock3(self):
        title = Text("Clock").to_edge(UP)
        self.play(Write(title))
        
        clock_face = Circle(radius=2, color=WHITE)
        self.play(Create(clock_face))

        hour_labels = VGroup()
        for hour in range(1, 13):
            angle = (hour / 12) * TAU 
            label = Text(str(hour), font_size=24)
            label.move_to(2.3 * np.array([np.sin(angle), np.cos(angle), 0]))
            hour_labels.add(label)

        self.play(Create(hour_labels))
      
        hour_hand = Line(ORIGIN, 0.7 * DOWN, color=RED, stroke_width=8)
        minute_hand = Line(ORIGIN, RIGHT * 1.2, color=BLUE, stroke_width=6)

        triangle1_vert=[[-0.1, 0, 0],[0.1, 0, 0],[0, 0.2, 0]]
        triangle1 = Polygon(*triangle1_vert, color=RED, fill_opacity=1)
        triangle1.shift(DOWN* 0.8)
        
        triangle1.rotate( PI ) 
        
        triangle2_vert=[[-0.1, 0, 0],[0.1, 0, 0],[0, 0.2, 0]]
        triangle2 = Polygon(*triangle2_vert, color=BLUE, fill_opacity=1)
        triangle2.shift(RIGHT * 1.2,DOWN *0.1)

        triangle2.rotate(3 * PI / 2) 
        
        self.play(Create(hour_hand),Create (triangle1))
        self.play(Create(minute_hand),Create (triangle2))
        
        twxt = Text("The time is 06:15").to_edge(DOWN)
        self.play(Write(twxt))
        self.wait(5)

    def Year(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Year ","1").setPosition([-4,2,0])
        p11=cvo.CVO().CreateCVO("Months", "12 ").setPosition([-3,-2,0])
        p13=cvo.CVO().CreateCVO(" Days", "365").setPosition([-1,2,0])
        
        p12=cvo.CVO().CreateCVO("Month Names", "").setPosition([3,0,0])
        p12.extendOname(["January","February","March","April","May","June","July","August","September","October","November","December"])
       
        p12.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p10.cvolist.append(p13)
        p10.cvolist.append(p12)
        
       
        self.setNumberOfCirclePositions(4)
        self.construct1(p10,p10) 

    def year2(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Leap Year ","").setPosition([-4,2,0])
        p11=cvo.CVO().CreateCVO("Days", "366 ").setPosition([1,2,0])
        p14=cvo.CVO().CreateCVO("Condition", "Once in 4 Years ").setPosition([4,2,0]).setangle(- TAU/ 10)
        p15=cvo.CVO().CreateCVO("Extra day "," February - 29 Days").setPosition([4,0,0]).setangle(- TAU/ 10)
        p12=cvo.CVO().CreateCVO("Last Occured", "2024").setPosition([4,-2,0]).setangle(- TAU/ 10)
        p10.cvolist.append(p11)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        p10.cvolist.append(p12)
        
        self.setNumberOfCirclePositions(5)
        self.construct1(p10,p10) 

    def year3(self):

        intro_text = Text("How to Determine a Leap Year", color=YELLOW).scale(0.8)
        intro_text.to_edge(UP)
        self.play(Write(intro_text))
        rule1 = Text("1. Year is divisible by 4.", color=BLUE).scale(0.7)
        rule1.next_to(intro_text, DOWN, buff=0.5)
        self.play(Write(rule1))
        rule2 = Text("2. If year is divisible by 100, it must also be divisible by 400.", color=BLUE).scale(0.7)
        rule2.next_to(rule1, DOWN, buff=0.5)
        self.play(Write(rule2))
        examples_title = Text("Examples:", color=GREEN).scale(0.7)
        examples_title.next_to(rule2, DOWN, buff=0.5)
        self.play(Write(examples_title))
        example1 = Text("2024: 2024 / 4 = 506 -> Leap Year", color=WHITE).scale(0.6)
        example1.next_to(examples_title, DOWN, buff=0.5)
        self.play(Write(example1))
        example2 = Text("1900: 1900 / 4 = 475, 1900 / 100 = 19, 1900 / 400 = 4.75 -> Not a Leap Year", color=WHITE).scale(0.6)
        example2.next_to(example1, DOWN, buff=0.5)
        self.play(Write(example2))
        example3 = Text("2000: 2000 / 4 = 500, 2000 / 100 = 20, 2000 / 400 = 5 -> Leap Year", color=WHITE).scale(0.6)
        example3.next_to(example2, DOWN, buff=0.5)
        self.play(Write(example3))
        self.wait(5)

      
    def SetDeveloperList(self): 
       self.DeveloperList="Khanak Gupta" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade4Chapter11TickTockGoesTheClock.py"

if __name__ == "__main__":
    scene = Time()
    scene.render()