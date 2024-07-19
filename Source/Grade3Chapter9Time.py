import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo
class time(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.time()
        self.clock()
        self.hm()
        self.trythese()
        self.week()
        self.days()
        self.months()
        self.GithubSourceCodeReference()
    def time(self):
        text = Text("TIME", font_size=22)
        self.isRandom = False
        self.positionChoice = [[-5,0,0],[3,0,0]]
        t=cvo.CVO().CreateCVO("TIME","")
        t1=cvo.CVO().CreateCVO("Definition","The measured period during which an action,process or condition exists")
        t.cvolist.append(t1)
        self.construct1(t,t)
        self.fadeOutCurrentScene()
    def clock(self):
        self.isRandom = False
        self.positionChoice = [[-5,0,0],[3,0,0]]
        c=cvo.CVO().CreateCVO("CLOCK","")
        c1=cvo.CVO().CreateCVO("Definition","A Physical,Digital device Which shows Time")
        c.cvolist.append(c1)
        self.construct1(c,c)
        self.fadeOutCurrentScene()
    def hm(self):
        self.isRandom = False
        self.positionChoice = [[-5,0,0],[3,2,0],[3,-2,0]]
        h=cvo.CVO().CreateCVO("Clock","Parts")
        h1=cvo.CVO().CreateCVO("Hours Hand","")
        h2=cvo.CVO().CreateCVO("Minutes Hand","")
        h.cvolist.append(h1)
        h.cvolist.append(h2)
        self.construct1(h,h) 
        self.fadeOutCurrentScene()
    def trythese(self):
        text = Text("CLOCK  ANIMATION", font_size=22)
        text.add(Underline(text, buff=0.1))
        text.to_corner(UP)
        self.play(Write(text))
        clock_face = Circle(radius=2, color=WHITE)
        self.add(clock_face)
        
        # Add hour numbers
        for hour in range(1, 13):
            angle = PI / 2 - hour * PI / 6
            number = Text(str(hour), font_size=24)
            number.move_to(1.6 * np.array([np.cos(angle), np.sin(angle), 0]))
            self.add(number)

        # Create the hour hand
        hour_hand = Line(start=ORIGIN, end=0.7 * UP, color=BLUE, stroke_width=8)
        hour_hand.shift(ORIGIN)
        
        # Create the minute hand
        minute_hand = Line(start=ORIGIN, end=1.2 * UP, color=RED, stroke_width=4)
        minute_hand.shift(ORIGIN)
        
        # Add the hands to the scene
        self.add(hour_hand, minute_hand)
        
        # Animation to rotate the hands
        hour_rotation = Rotate(hour_hand, angle=PI / 6, about_point=ORIGIN, run_time=2)
        minute_rotation = Rotate(minute_hand, angle=PI, about_point=ORIGIN, run_time=2)
        
        self.play(hour_rotation, minute_rotation)
        self.wait(2)
        self.fadeOutCurrentScene()
    def week(self):
        self.isRandom = False
        self.positionChoice = [[-5,0,0],[3,0,0]]
        w=cvo.CVO().CreateCVO("WEEK","")
        w1=cvo.CVO().CreateCVO("A Period of SEVEN Days","")
        w.cvolist.append(w1)
        self.construct1(w,w)
        self.fadeOutCurrentScene()
    def days(self):
        self.isRandom = False
        self.positionChoice = [[-5,0,0],[3,0,0]]
        d=cvo.CVO().CreateCVO("WEEK","")
        d1=cvo.CVO().CreateCVO("DAYS","")
        d1.appendOname=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Satruday"]
        d.cvolist.append(d1)
        d1.extendOname(d1.appendOname)
        self.construct1(d,d)
        self.fadeOutCurrentScene()
    def months(self):
        self.isRandom = False
        self.positionChoice = [[-5,0,0],[3,0,0]]
        m=cvo.CVO().CreateCVO("MONTHS","")
        m1=cvo.CVO().CreateCVO("Names","")
        m1.appendOname=["January","February","March","April","May","June","July","August","September","October","November","December"]
        m.cvolist.append(m1)
        m1.extendOname(m1.appendOname)
        self.construct1(m,m)
        self.fadeOutCurrentScene()
    def SetDeveloperList(self): 
       self.DeveloperList="Abhiram" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade3Chater9Time.py"

if __name__ == "__main__":
     scene = time()
     scene.render()  