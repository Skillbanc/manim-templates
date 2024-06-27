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
        c1=cvo.CVO().CreateCVO("Definitiom","A Physical,Digital device Which shows Time")
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
        
        # Create clock hour and minute markers
        for angle in range(0, 360, 30):
            start = clock_face.point_at_angle(angle * DEGREES)
            end = start + 0.2 * (start - clock_face.get_center())
            if angle % 90 == 0:
                end = start + 0.3 * (start - clock_face.get_center())
            self.add(Line(start, end, color=WHITE))

        # Create hour hand
        text3= Text("Representation",font_size=22)
        # text3.add(Underline(text))
        text3.to_corner(RIGHT*1.5)
        self.play(Write(text3))

        hour_hand = Line(clock_face.get_center(), clock_face.point_at_angle(90 * DEGREES), color=ORANGE, stroke_width=8)
        text1 = Text("HOURS HAND=ORANGE",font_size=22).next_to(text3,DOWN)
        text1.to_corner(RIGHT*1.5)
        self.play(Write(text1))

        # Create minute hand
        minute_hand = Line(clock_face.get_center(), clock_face.point_at_angle(0 * DEGREES), color=GREEN, stroke_width=4)
        text2 = Text("MINUTES HAND=RED",font_size=22).next_to(text1,DOWN)
        text2.to_corner(RIGHT*1.5)
        self.play(Write(text2))


        # Add clock face and hands to the scene
        self.add(clock_face, hour_hand, minute_hand)
        self.wait(2)

        # Add the time text below the clock
        time_text = Text("3'O CLOCK").next_to(clock_face, DOWN)
        self.add(time_text)

        # Show the animation
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
        d=cvo.CVO().CreateCVO("WEEK","Days")
        d1=cvo.CVO().CreateCVO("7 DAYS","")
        d1.appendOname=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Satruday"]
        d.cvolist.append(d1)
        d1.extendOname(d1.appendOname)
        self.construct1(d,d)
        self.fadeOutCurrentScene()
    def months(self):
        self.isRandom = False
        self.positionChoice = [[-5,0,0],[3,0,0]]
        m=cvo.CVO().CreateCVO("MONTHS","")
        m1=cvo.CVO().CreateCVO("12 Months","")
        m1.appendOname=["January","February","March","April","May","June","July","August","September","October","November","December"]
        m.cvolist.append(m1)
        m1.extendOname(m1.appendOname)
        self.construct1(m,m)
        self.fadeOutCurrentScene()
    def SetDeveloperList(self): 
       self.DeveloperList="Abhiram" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Class3Chapter9Time.py"

if __name__ == "__main__":
     scene = time()
     scene.render()  