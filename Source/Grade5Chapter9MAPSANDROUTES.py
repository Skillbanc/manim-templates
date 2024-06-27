import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo
class Class5(AbstractAnim):
    def construct(self):
        self.maps()
        self.floor()
        self.animfloor()
        self.route()
        self.routeanim()
        self.GithubSourceCodeReference()
    def maps(self):
        self.isRandom = False
        self.positionChoice = [[-5,0,0],[3,0,0]]
        text = Text("MAPS AND ROUTES", font_size=30)
        text.add(Underline(text, buff=0.1))
        text.to_corner(UP)
        self.play(Write(text))
        m=cvo.CVO().CreateCVO("Maps","")
        m1=cvo.CVO().CreateCVO("Definiton","A Diagramatic Representation of a Place")
        m.cvolist.append(m1)
        self.construct1(m,m)
        self.fadeOutCurrentScene()
    def floor(self):
        self.isRandom = False
        self.positionChoice = [[-5,0,0],[3,0,0]]
        f=cvo.CVO().CreateCVO("Types","Floor Map")
        f1=cvo.CVO().CreateCVO("Definition","A Map that shows Shape,Size and Arrangments of a room")
        f.cvolist.append(f1)
        self.construct1(f,f)
        self.fadeOutCurrentScene()
    def animfloor(self):
        text = Text("FLOOR MAP OF A BEDROOM", font_size=30)
        text.add(Underline(text, buff=0.1))
        text.to_corner(UP + LEFT)
        self.play(Write(text))

        room_width = 8
        room_height = 5
        room = Rectangle(width=room_width, height=room_height)
        room.set_fill(GRAY, opacity=0.5)
        room.set_stroke(BLACK, width=2)
        
        bed = Rectangle(width=3, height=1.5)
        bed.set_fill(BLUE, opacity=0.7)
        bed.set_stroke(BLACK, width=2)
        bed.move_to([-2, 1, 0])

        bathroom = Rectangle(width=2, height=2)
        bathroom.set_fill(GREEN, opacity=0.7)
        bathroom.set_stroke(BLACK, width=2)
        bathroom.move_to([3, 1.5, 0]) 

        cupboards = Rectangle(width=3, height=1)
        cupboards.set_fill(DARK_BROWN, opacity=0.7)
        cupboards.set_stroke(BLACK, width=2)
        cupboards.move_to([0, -1.5, 0])

        entrance = Rectangle(width=1,height=1)
        entrance.move_to([-3,-2.5,0])
        entrance.set_stroke(BLACK, width=4)

        bed_label = Text("Bed").next_to(bed, UP)
        bathroom_label = Text("Bathroom").next_to(bathroom, UP)
        cupboards_label = Text("Cupboards").next_to(cupboards, DOWN)
        entrance_label = Text("Entrance").next_to(entrance, UP)

        self.play(Create(room))
        self.play(FadeIn(bed), FadeIn(bed_label))
        self.play(FadeIn(bathroom), FadeIn(bathroom_label))
        self.play(FadeIn(cupboards), FadeIn(cupboards_label))
        self.play(Create(entrance), FadeIn(entrance_label))

        self.wait(2)
        self.fadeOutCurrentScene()
    def route(self):
        text = Text("ROUTES", font_size=30)
        text.add(Underline(text, buff=0.1))
        text.to_corner(UP)
        self.play(Write(text))
        self.positionChoice = [[-5,0,0],[3,0,0]]
        self.isRandom = False
        r=cvo.CVO().CreateCVO("Route","")
        r1=cvo.CVO().CreateCVO("Definition","The Path from PointA to PointB")
        r.cvolist.append(r1)
        self.construct1(r,r)
        self.fadeOutCurrentScene()
    def routeanim(self):
        text = Text("ROUTE MAP", font_size=30)
        text.add(Underline(text, buff=0.1))
        text.to_corner(UP)
        self.play(Write(text))

        house = Dot(LEFT * 3, color=BLUE).scale(1.5)
        hospital = Dot(LEFT * 1 + UP * 2, color=RED).scale(1.5)
        temple = Dot(RIGHT * 2 + DOWN * 1, color=GREEN).scale(1.5)
        school = Dot(RIGHT * 4 + UP * 1, color=YELLOW).scale(1.5)
        
        house_label = Text("House").next_to(house, DOWN)
        hospital_label = Text("Hospital").next_to(hospital, LEFT)
        temple_label = Text("Temple").next_to(temple, RIGHT)
        school_label = Text("School").next_to(school, RIGHT)
    
        self.add(house, house_label, hospital, hospital_label, temple, temple_label, school, school_label)
        
        path1 = Line(house.get_center(), hospital.get_center(), color=WHITE)
        path2 = Line(hospital.get_center(), temple.get_center(), color=WHITE)
        path3 = Line(temple.get_center(), school.get_center(), color=WHITE)
        
        self.play(Create(path1))
        self.play(Create(path2))
        self.play(Create(path3))
        
        traveler = Dot(house.get_center(), color=YELLOW).scale(1.2)
        self.add(traveler)
        
        self.play(traveler.animate.move_to(hospital), run_time=2)
        self.play(traveler.animate.move_to(temple), run_time=2)
        self.play(traveler.animate.move_to(school), run_time=2)
        
        finish_message = Text("Arrived at School!", font_size=36).move_to(DOWN * 3)
        self.play(Write(finish_message))
        self.fadeOutCurrentScene()

    def SetDeveloperList(self): 
       self.DeveloperList="Abhiram" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Class5Chapter9MAPSANDROUTES.py"

if __name__ == "__main__":
    scene = Class5()
    scene.render()