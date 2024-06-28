import json
from manim import *
from AbstractAnim import AbstractAnim
import cvo
class ConstructionofTriangle(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.constructoftri()
        self.threes()
        self.twosonea()
        self.fadeOutCurrentScene()
        self.onestwoa()
        self.oneratwos()
        self.GithubSourceCodeReference()
    def constructoftri(self):
        self.isRandom = False
        self.positionChoice = [[0,0,0],[-4,2,0],[4,2,0],[-4,-2,0],[4,-2,0]]
        p10=cvo.CVO().CreateCVO("Construction of Triangles","")
        p11=cvo.CVO().CreateCVO("S-S-S","")
        p12=cvo.CVO().CreateCVO("S-A-S","")
        p13=cvo.CVO().CreateCVO("A-S-A","")
        p14=cvo.CVO().CreateCVO("R-H-S","")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
    def threes(self):
        self.isRandom = False
        self.positionChoice = [[-4,0,0],[4,0,0]]
        a10=cvo.CVO().CreateCVO("S-S-S","")
        a11=cvo.CVO().CreateCVO("Side-Side-Side","This triangle is constructed using 3 sides")
        a10.cvolist.append(a11)
        a11.setcircleradius(1.5)
        self.construct1(a10,a10)
        self.fadeOutCurrentScene()
        text = Text("SSS TRIANGLE CONSTRUCTION", font_size=22)
        text.add(Underline(text, buff=0.1))
        text.to_corner(UP)
        self.play(Write(text))
        ab = Line([-5, -2, 0], [-2, -2, 0])
        label1_A = Text("A").next_to(ab.get_start(),DOWN)
        label1_B = Text("B").next_to(ab.get_end(),DOWN)

        text1=Text("(1)Take a linesegment AB=3",font_size=24).to_edge(RIGHT)
        text2=Text("(2)Take a as center and create an arc taking 4cm",font_size=24).next_to(text1,DOWN)
        text3=Text("(3)Repeat the step-2 taking 2cm",font_size=24).next_to(text2,DOWN)
        text4=Text("(4)Combine all the lines",font_size=24).next_to(text3,DOWN)
        text5=Text("(5)Triangle is Constructed",font_size=24).next_to(text4,DOWN)

        text1.shift(LEFT*3)
        text2.shift(LEFT*1.75)
        text3.shift(LEFT*1.5)
        text4.shift(LEFT*3)
        text5.shift(LEFT*3)
         
        # Define the arcs
        side1 = Text("3cm").next_to(ab,DOWN)
        arc1 = Arc(radius=4, start_angle=20*DEGREES, angle=20*DEGREES, color=GREEN).move_arc_center_to([-5, -2, 0])
        arc2 = Arc(radius=2, start_angle=60*DEGREES, angle=30*DEGREES, color=GOLD).move_arc_center_to([-2, -2, 0])
        
        # Calculate the midpoint between the centers of the two arcs
        center1 = arc1.get_center()
        center2 = arc2.get_center()
        midpoint = (center1 + center2) / 2
        
        # Create the dot at the midpoint
        dot = Dot(midpoint, color=RED)
        label1_C = Text("C").next_to(dot,RIGHT)
        
        # Create lines from the dot to the endpoints of the line segment
        line_to_start = Line(dot.get_center(), [-5, -2, 0])
        line_to_end = Line(dot.get_center(), [-2, -2, 0])
        side2 = Text("4cm").next_to(line_to_end, LEFT*5 )
        side3 = Text("2cm").next_to( line_to_start,RIGHT)
        
        # Play the animations
        self.play(Write(text1))
        self.play(Create(ab))
        self.play(Write(label1_A),Write(label1_B))
        self.play(Write(side1))
        self.play(Write(text2))
        self.play(Create(arc1))
        self.play(Write(text3))
        self.play(Create(arc2))
        self.play(Create(dot))
        self.play(Write(label1_C))
        self.play(Write(text4))
        self.play(Create(line_to_start), Create(line_to_end))
        self.play(Write(text5))
        self.play(Write(side2),Write(side3))
        self.wait(2)
        self.fadeOutCurrentScene()
    def twosonea(self):
        self.isRandom = False
        self.positionChoice = [[-4,0,0],[4,0,0]]
        r10=cvo.CVO().CreateCVO("S-A-S","")
        r11=cvo.CVO().CreateCVO("Side-Angle-Side","This triangle is constructed based on two sides and 1 angle")
        r10.cvolist.append(r11)
        r11.setcircleradius(1.5)
        self.construct1(r10,r10)
        self.fadeOutCurrentScene()

        text = Text("SAS TRIANGLE CONSTRUCTION", font_size=22)
        text.add(Underline(text, buff=0.1))
        text.to_corner(UP)
        self.play(Write(text))

        ab = Line([-5, -2, 0], [-2, -2, 0])
        label1_A = Text("A").next_to(ab.get_start(),DOWN)
        label1_B = Text("B").next_to(ab.get_end(),DOWN)

        text1=Text("(1)Take a linesegment AB=4cm",font_size=24).to_edge(RIGHT)
        text2=Text("(2)Take B as center and draw an arc taking 5cm",font_size=24).next_to(text1,DOWN)
        text3=Text("(3)Mark it as C",font_size=24).next_to(text2,DOWN)
        text4=Text("(4)Combine all the lines",font_size=24).next_to(text3,DOWN)
        text5=Text("(5)Triangle is Constructed",font_size=24).next_to(text4,DOWN)

        text1.shift(LEFT*1.5)
        text2.shift(LEFT*1.5)
        text3.shift(LEFT*1.75)
        text4.shift(LEFT*1.5)
        text5.shift(LEFT*1.5)

        side1 = Text("4cm").next_to(ab,DOWN)
        arc1 = Arc(radius=4, start_angle=50*DEGREES, angle=20*DEGREES, color=GREEN).move_arc_center_to([-5, -2, 0])

        dot_position = arc1.point_from_proportion(0.5)
        dot = Dot(point=dot_position, color=RED)
        
        triangle1 = Polygon([-5, -2, 0], [-2, -2, 0] , dot.get_center())
        triangle1.set_fill(GREEN, opacity=0.5)


        angle1_label = MathTex(r"50^\circ").move_to(triangle1.get_vertices()[1] + 0.6 * LEFT + 0.4 * UP)


        label1_C = Text("C").next_to(dot,UP)

        line_to_start = Line(dot.get_center(), [-5, -2, 0])
        line_to_end = Line(dot.get_center(), [-2, -2, 0])
        
        side2 = Text("").next_to(line_to_end, LEFT*5 )
        side3 = Text("5cm").next_to( line_to_start,RIGHT*3)
        
        # arc2 = Arc(radius=2, start_angle=60*DEGREES, angle=30*DEGREES, color=GOLD).move_arc_center_to([-2, -2, 0])
        self.play(Write(text1))
        self.play(Create(ab))
        self.play(Write(label1_A),Write(label1_B))
        self.play(Write(side1))
        self.play(Write(text2))
        self.play(Write(angle1_label))
        self.play(Create(arc1))
        self.add(dot)
        self.play(Create(dot))
        self.play(Write(text3))
        self.play(Create(label1_C))
        self.play(Write(text4))
        self.play(Write(line_to_start))
        self.play(Write(line_to_end))
        self.play(Write(side2),Write(side3))
        self.play(Write(text5))
        self.play(Write(triangle1))
        self.wait(2)
        self.fadeOutCurrentScene()

    def onestwoa(self):
        self.isRandom = False
        self.positionChoice = [[-4,0,0],[4,0,0]]
        m1=cvo.CVO().CreateCVO("A-S-A","")
        m2=cvo.CVO().CreateCVO("Angle-Side-Angle","The Construction of Triangle is done by two angles and 1 side")
        m1.cvolist.append(m2)
        m2.setcircleradius(2)
        self.construct1(m1,m1)
        self.fadeOutCurrentScene()
        text = Text("ASA TRIANGLE CONSTRUCTION", font_size=22)
        text.add(Underline(text, buff=0.1))
        text.to_corner(UP)
        self.play(Write(text))
        ab = Line([-5, -2, 0], [-2, -2, 0])
        label1_A = Text("A").next_to(ab.get_start(),DOWN)
        label1_B = Text("B").next_to(ab.get_end(),DOWN)

        text1=Text("(1)Take a linesegment AB=4cm",font_size=24).to_edge(RIGHT)
        text2=Text("(2)From A draw an arc taking 45*Degrees",font_size=24).next_to(text1,DOWN)
        text3=Text("(3)From B draw an arc taking 100*Degrees",font_size=24).next_to(text2,DOWN)
        text4=Text("(4)Mark the Intersection of arcs point as C",font_size=24).next_to(text3,DOWN)
        text5=Text("(5)Combine AC and BC line",font_size=24).next_to(text4,DOWN)
        text6=Text("(6)Triangle is Constructed",font_size=24).next_to(text5,DOWN)

        text1.shift(UP + LEFT*3)
        text2.shift(UP + LEFT*2)
        text3.shift(UP + LEFT*2)
        text4.shift(UP + LEFT*2)
        text5.shift(UP + LEFT*3)
        text6.shift(UP + LEFT*3)

        side1 = Text("4cm").next_to(ab,DOWN)
        arc1 = Arc(radius=4, start_angle=45*DEGREES, angle=30*DEGREES, color=GREEN).move_arc_center_to([-5, -2, 0])
        arc2 = Arc(radius=4, start_angle=100*DEGREES, angle=30*DEGREES, color=GOLD).move_arc_center_to([-2, -2, 0])

        center1 = arc1.get_center()
        center2 = arc2.get_center()
        midpoint = (center1 + center2) / 2
        
        # Create the dot at the midpoint
        dot = Dot(midpoint, color=RED)
        dot = Dot([-3.5,1.63,0])
        label1_C = Text("C").next_to(dot,RIGHT)

        line_to_start = Line(dot.get_center(), [-5, -2, 0])
        line_to_end = Line(dot.get_center(), [-2, -2, 0])

        triangle1 = Polygon([-5, -2, 0], [-2, -2, 0] , dot.get_center())
        triangle1.set_fill(GREEN, opacity=0.5)

        angle1_label = MathTex(r"100^\circ").move_to(triangle1.get_vertices()[1] + 0.6 * LEFT + 0.4 * UP)
        angle2_label = MathTex(r"45^\circ").move_to(triangle1.get_vertices()[0] + 0.6 * RIGHT + 0.4 * UP)

        self.play(Create(text1))
        self.play(Create(ab))
        self.play(Create(label1_A))
        self.play(Create(label1_B))
        self.play(Create(side1))
        self.play(Create(text2))
        self.play(Create(arc1))
        self.play(Create(angle2_label))
        self.play(Write(text3))
        self.play(Create(arc2))
        self.play(Create(angle1_label))
        self.play(Write(text4))
        self.play(GrowFromCenter(dot))
        self.play(Write(label1_C))
        self.play(Write(text5))
        self.play(Create(line_to_start), Create(line_to_end))
        self.play(Write(text6))
        self.play(Create(triangle1))
        self.wait(2) 

        self.fadeOutCurrentScene()

    def oneratwos(self):
        self.isRandom = False
        self.positionChoice = [[-4,0,0],[2.75,0,0]]
        a1=cvo.CVO().CreateCVO("R-H-S","")
        a2=cvo.CVO().CreateCVO("Right Angle Hypotenues","This triangle is constructed using 90degree,hypotenuse and normal side")
        a1.cvolist.append(a2)
        a2.setcircleradius(1.5)
        self.construct1(a1,a1)
        self.fadeOutCurrentScene()

        text = Text("RHS TRIANGLE CONSTRUCTION", font_size=22)
        text.add(Underline(text, buff=0.1))
        text.to_corner(UP)
        self.play(Write(text))
        ab = Line([-5, -2, 0], [-2, -2, 0])
        label1_A = Text("A").next_to(ab.get_start(),DOWN)
        label1_B = Text("B").next_to(ab.get_end(),DOWN)

        text1=Text("(1)Take a linesegment AB=5cm",font_size=24).to_edge(RIGHT)
        text2=Text("(2)From A draw an arc taking 90*Degrees and mark it C",font_size=24).next_to(text1,DOWN)
        text3=Text("(3)From B join a line to C taking radius 11cm",font_size=24).next_to(text2,DOWN)
        text4=Text("(4)Combine AC line",font_size=24).next_to(text3,DOWN)
        text5=Text("(5)Triangle is Constructed",font_size=24).next_to(text4,DOWN)

        text1.shift(LEFT*3)
        text2.shift(LEFT*2)
        text3.shift(LEFT*2)
        text4.shift(LEFT*3)
        text5.shift(LEFT*3)
         
        side1 = Text("5cm").next_to(ab,DOWN)
        arc1 = Arc(radius=5, start_angle=90*DEGREES, angle=20*DEGREES, color=GREEN).move_arc_center_to([-5, -2, 0])
        # arc2 = Arc(radius=5, start_angle=60*DEGREES, angle=30*DEGREES, color=GOLD).move_arc_center_to([-2, -2, 0])

        dot_position = arc1.point_from_proportion(0)
        dot = Dot(point=dot_position, color=RED)

        label1_C = Text("C").next_to(dot,UP)

        line_to_start = Line(dot.get_center(), [-5, -2, 0])
        line_to_end = Line(dot.get_center(), [-2, -2, 0])
        
        
        side2 = Text("").next_to(line_to_end, LEFT*5 )
        side3 = Text("11cm").next_to( line_to_start,RIGHT*6)

        triangle = Polygon([-5, -2, 0], [-2, -2, 0], dot.get_center())
        triangle.set_fill(GREEN, opacity=0.5)
        angle1_label = Square(side_length=0.5).move_to(triangle.get_vertices()[1] + 2.75 * LEFT + 0.3 * UP)

        self.play(Write(text1))
        self.play(Create(ab))
        self.play(Create(label1_A),Create(label1_B))
        self.play(Create(side1))
        self.play(Create(text2))
        self.play(Create(arc1))
        self.play(Create(angle1_label))
        self.play(Create(dot))
        self.play(Create(label1_C))
        self.play(Create(text3))
        self.play(Create(text4))
        self.play(Create(line_to_start))
        self.play(Create(line_to_end))
        self.play(Create(side2))
        self.play(Create(side3))
        self.play(Create(text5))
        self.play(Create(triangle))
        self.wait(2)
        self.fadeOutCurrentScene()
    def SetDeveloperList(self): 
       self.DeveloperList="Abhiram" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Class7Chap9ConstructionOfTriangle.py"  

if __name__ == "__main__":
    scene = ConstructionofTriangle()
    scene.render()
