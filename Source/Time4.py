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
        self.Clock2()  
        self.fadeOutCurrentScene()
        self.Year()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
             
  
    def Clock(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Time ","").setPosition([4,0,0])
        p11=cvo.CVO().CreateCVO("Before Noon", "am").setPosition([-4,2,0])
        p12=cvo.CVO().CreateCVO("After Noon", "pm").setPosition([-4,0,0])
        p15=cvo.CVO().CreateCVO("1 day", "24 hours").setPosition([-4,-2,0])
        p13=cvo.CVO().CreateCVO("1 hour", "60 minutes").setPosition([-2,-2,0]).setangle(-TAU/4)
        p14=cvo.CVO().CreateCVO("1 minute", "60 seconds").setPosition([0,-2,0])
        
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p15)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
       
        self.setNumberOfCirclePositions(6)
        self.construct1(p10,p10)  


    def Clock2(self):
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
      
        hour_hand = Line(ORIGIN, 0.5 * UP, color=RED, stroke_width=8)
        minute_hand = Line(ORIGIN, RIGHT, color=BLUE, stroke_width=6)
        second_hand = Line(ORIGIN, 1.2 * DOWN, color=GREEN, stroke_width=4)
        self.play(Create(hour_hand))
        self.play(Create (minute_hand))
        self.play(Create(second_hand))

        twxt = Text("The time is 12:15").to_edge(DOWN)
        self.play(Write(twxt))


    def Year(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Year ","")
        p11=cvo.CVO().CreateCVO("1 Year", "12 Months")
        p12=cvo.CVO().CreateCVO("Names", "")
        p12.extendOname(["January","February","March","April","May","June","July","August","September","October","November","December"])
       
        p12.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        
       
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10) 

    
    
        

        
    def SetDeveloperList(self): 
       self.DeveloperList="Khanak Gupta" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Time4.py"

if __name__ == "__main__":
    scene = Time()
    scene.render()