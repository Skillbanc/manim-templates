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
        self.Clock2()  
        self.fadeOutCurrentScene()
        self.Clock3()  
        self.fadeOutCurrentScene()
        self.Year()
        self.fadeOutCurrentScene()
        self.year2()
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
        self.angleChoice = [TAU/10,-TAU/2,TAU/10,TAU/2,TAU/10]
        p10=cvo.CVO().CreateCVO("Day ","1").setPosition([-4,2,0])
        p15=cvo.CVO().CreateCVO("Hours", "24").setPosition([3,2,0])
        p11=cvo.CVO().CreateCVO("Hour", "1").setPosition([3,0,0])
        p12=cvo.CVO().CreateCVO("Minutes", "60").setPosition([-4,0,0])
        p13=cvo.CVO().CreateCVO("Minute", "1").setPosition([-4,-2,0])        
        p14=cvo.CVO().CreateCVO("Seconds", "60").setPosition([3,-2,0])
        p10.cvolist.append(p15)
        p15.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        p13.cvolist.append(p14)
        self.setNumberOfCirclePositions(6)
        self.construct1(p10,p10)  
    
    def Clock4(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Clock ","").setPosition([-4,2,0])
        p11=cvo.CVO().CreateCVO("Smaller Hand", "Hours").setPosition([-4,-2,0])
        p12=cvo.CVO().CreateCVO("Longer Hand", "Minutes").setPosition([0,0,0])
        p13=cvo.CVO().CreateCVO("", "").setPosition([4,0,0])
        p13.extendOname(["Long hand 1 - 5 min","Long hand 2 - 10 min","Long hand 3 - 15 min","and so on"])
        p13.setcircleradius(2.5)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p12.cvolist.append(p13)
       
       
        self.setNumberOfCirclePositions(6)
        self.construct1(p10,p10)
        
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
        p14=cvo.CVO().CreateCVO("Condition", "Once in 4Years ").setPosition([4,2,0]).setangle(- TAU/ 10)
        p15=cvo.CVO().CreateCVO("Extra day "," February - 29 Days").setPosition([4,0,0]).setangle(- TAU/ 10)
        p12=cvo.CVO().CreateCVO("Last Occured", "2024").setPosition([4,-2,0]).setangle(- TAU/ 10)
       

        p10.cvolist.append(p11)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        p10.cvolist.append(p12)
        

        self.setNumberOfCirclePositions(5)
        self.construct1(p10,p10) 
      
    def SetDeveloperList(self): 
       self.DeveloperList="Khanak Gupta" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade4Chapter11TickTockGoesTheClock.py"

if __name__ == "__main__":
    scene = Time()
    scene.render()