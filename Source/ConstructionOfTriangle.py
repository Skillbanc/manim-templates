import json
from manim import *
from AbstractAnim import AbstractAnim
import cvo
class ConstructionofTriangle(AbstractAnim):
    def construct(self):
        self.constructoftri()
        self.threes()
        self.twosonea()
        self.fadeOutCurrentScene()
        self.onestwoa()
        self.oneratwos()
    def constructoftri(self):
        self.isRandom = False
        self.positionChoice = [[0,0,0],[-4,2,0],[4,2,0],[-4,-2,0],[4,-2,0]]
        p10=cvo.CVO().CreateCVO("Construction of Triangles","")
        p11=cvo.CVO().CreateCVO("S-S-S","")
        p12=cvo.CVO().CreateCVO("S-A-S","")
        p13=cvo.CVO().CreateCVO("A-S-A","")
        p14=cvo.CVO().CreateCVO("RA-S-S","")
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
        a11=cvo.CVO().CreateCVO("Construction","")
        a11onnamelist=["Select a Side-3cm","Draw arc from starting side-take 2cm","ViceVersa from other end-take 4cm","Traingle is formed"]
        a10.cvolist.append(a11)
        a11.extendOname(a11onnamelist)
        a11.setcircleradius(2)
        self.construct1(a10,a10)
        self.fadeOutCurrentScene()
        triangle1_vert=[[-2, 0, 0],[2, 0, 0],[0, 3, 0]] 
    #  triangle2_vert=[[-2, 0, 0],[2, 0, 0],[0, 3, 0]]

        triangle1 = Polygon(*triangle1_vert, color=BLUE)
    #  triangle2 = Polygon(*triangle2_vert, color=GREEN)

        triangle1.shift(3 * LEFT)
    #  triangle2.shift(3 * RIGHT)
        triangle1.shift(2*DOWN)
    #  triangle2.shift(2*DOWN)

        label1_A = Text("A").next_to(triangle1.get_vertices()[0], DOWN)
        label1_B = Text("B").next_to(triangle1.get_vertices()[1], DOWN)
        label1_C = Text("C").next_to(triangle1.get_vertices()[2], UP)

    #  label2_D = Text("D").next_to(triangle2.get_vertices()[0], DOWN)
    #  label2_E = Text("E").next_to(triangle2.get_vertices()[1], DOWN)
    #  label2_F = Text("F").next_to(triangle2.get_vertices()[2], UP)

        sss_rule = Text("Side-Side-Side (SSS) Example").to_edge(UP)
        
        
        # Side lengths
        side1 = Text("3cm").next_to(Line(triangle1.get_vertices()[0], triangle1.get_vertices()[1]).get_center(), DOWN)
        side2 = Text("2cm").next_to(Line(triangle1.get_vertices()[1], triangle1.get_vertices()[2]).get_center(), RIGHT)
        side3 = Text("4cm").next_to(Line(triangle1.get_vertices()[2], triangle1.get_vertices()[0]).get_center(), LEFT)
        
    #  side4 = Text("a").next_to(Line(triangle2.get_vertices()[0], triangle2.get_vertices()[1]).get_center(), DOWN)
    #  side5 = Text("b").next_to(Line(triangle2.get_vertices()[1], triangle2.get_vertices()[2]).get_center(), RIGHT)
    #  side6 = Text("c").next_to(Line(triangle2.get_vertices()[2], triangle2.get_vertices()[0]).get_center(), LEFT)

        self.play(Write(sss_rule))
        self.play(Create(triangle1))
        self.play(Write(label1_A), Write(label1_B), Write(label1_C))
        self.play(Write(side1), Write(side2), Write(side3))

        self.wait(2)
        self.fadeOutCurrentScene()
    def twosonea(self):
        self.isRandom = False
        self.positionChoice = [[-4,0,0],[4,0,0]]
        r10=cvo.CVO().CreateCVO("S-A-S","")
        r11=cvo.CVO().CreateCVO("Construction","")
        r11onnamelist=["Select a side-4cm","Draw arc from starting side-take 50","ViceVersa from other end-take 5cm","Traingle is formed"]
        r10.cvolist.append(r11)
        r11.extendOname(r11onnamelist)
        r11.setcircleradius(2)
        self.construct1(r10,r10)
        self.fadeOutCurrentScene()
        triangle1_vert = [[-2, 0, 0], [2, 0, 0], [0, 3, 0]] 
        # triangle2_vert = [[-2, 0, 0], [2, 0, 0], [0, 3, 0]]

        # Create triangles
        triangle1 = Polygon(*triangle1_vert, color=BLUE)
        # triangle2 = Polygon(*triangle2_vert, color=GREEN)

        # Shift triangles
        triangle1.shift(3 * LEFT)
        # triangle2.shift(3 * RIGHT)
        triangle1.shift(2 * DOWN)
        # triangle2.shift(2 * DOWN)

        # Labels for vertices
        label1_A = Text("A").next_to(triangle1.get_vertices()[0], DOWN)
        label1_B = Text("B").next_to(triangle1.get_vertices()[1], DOWN)
        label1_C = Text("C").next_to(triangle1.get_vertices()[2], UP)

        # label2_D = Text("D").next_to(triangle2.get_vertices()[0], DOWN)
        # label2_E = Text("E").next_to(triangle2.get_vertices()[1], DOWN)
        # label2_F = Text("F").next_to(triangle2.get_vertices()[2], UP)

        # Rule text
        sas_rule = Text("Side-Angle-Side (SAS) Example").to_edge(UP)

        # Angle labels
        angle1_label = MathTex("50").move_to(triangle1.get_vertices()[1] + 0.6 * LEFT + 0.4 * UP)
        # angle2_label = MathTex(r"\alpha").move_to(triangle2.get_vertices()[1] + 0.6 * LEFT + 0.4 * UP)

        # Angle arcs
        angle1_arc = Arc(radius=0.5, start_angle=90, angle=np.pi/3).move_arc_center_to(triangle1.get_vertices()[1])
        # angle2_arc = Arc(radius=0.5, start_angle=90, angle=np.pi/3).move_arc_center_to(triangle2.get_vertices()[1])

        # Side lengths
        side1 = Text("4cm").next_to(Line(triangle1.get_vertices()[0], triangle1.get_vertices()[1]).get_center(), DOWN)
        side2 = Text("5cm").next_to(Line(triangle1.get_vertices()[1], triangle1.get_vertices()[2]).get_center(), RIGHT)
        
        # side4 = Text("a").next_to(Line(triangle2.get_vertices()[0], triangle2.get_vertices()[1]).get_center(), DOWN)
        # side5 = Text("b").next_to(Line(triangle2.get_vertices()[1], triangle2.get_vertices()[2]).get_center(), RIGHT)

        # Animate the creation of elements
        self.play(Write(sas_rule))
        self.play(Create(triangle1))
        self.play(Write(label1_A), Write(label1_B), Write(label1_C))
        self.play(Create(angle1_arc))
        self.play(Write(angle1_label))
        self.play(Write(side1), Write(side2))

        self.wait(2)

    def onestwoa(self):
        self.isRandom = False
        self.positionChoice = [[-4,0,0],[4,0,0]]
        m1=cvo.CVO().CreateCVO("A-S-A","")
        m2=cvo.CVO().CreateCVO("Construction","")
        m2onnamelist=["Select a side-4cm","Draw arc from starting side-take 50","ViceVersa from other end-take 80","Triangle is formed"]
        m1.cvolist.append(m2)
        m2.extendOname(m2onnamelist)
        m2.setcircleradius(2)
        self.construct1(m1,m1)
        self.fadeOutCurrentScene()
        triangle1_vert = [[-2, 0, 0], [2, 0, 0], [0, 3, 0]] 
        # triangle2_vert = [[-2, 0, 0], [2, 0, 0], [0, 3, 0]]

        # Create triangles
        triangle1 = Polygon(*triangle1_vert, color=BLUE)
        # triangle2 = Polygon(*triangle2_vert, color=GREEN)

        # Shift triangles
        triangle1.shift(3 * LEFT)
        # triangle2.shift(3 * RIGHT)
        triangle1.shift(2 * DOWN)
        # triangle2.shift(2 * DOWN)

        # Labels for vertices
        label1_A = Text("A").next_to(triangle1.get_vertices()[0], DOWN)
        label1_B = Text("B").next_to(triangle1.get_vertices()[1], DOWN)
        label1_C = Text("C").next_to(triangle1.get_vertices()[2], UP)

        # label2_D = Text("D").next_to(triangle2.get_vertices()[0], DOWN)
        # label2_E = Text("E").next_to(triangle2.get_vertices()[1], DOWN)
        # label2_F = Text("F").next_to(triangle2.get_vertices()[2], UP)

        # Rule text
        asa_rule = Text("Angle-Side-Angle (ASA) Example").to_edge(UP)

        # Angle labels
        angle1_label = MathTex("50").move_to(triangle1.get_vertices()[1] + 0.6 * LEFT + 0.4 * UP)
        angle2_label = MathTex("80").move_to(triangle1.get_vertices()[0] + 0.6 * RIGHT + 0.4 * UP)

        # angle3_label = MathTex(r"\alpha").move_to(triangle2.get_vertices()[1] + 0.6 * LEFT + 0.4 * UP)
        # angle4_label = MathTex(r"\beta").move_to(triangle2.get_vertices()[0] + 0.6 * RIGHT + 0.4 * UP)

        # Angle arcs
        angle1_arc = Arc(radius=0.5, start_angle=90, angle=np.pi/3).move_arc_center_to(triangle1.get_vertices()[1])
        angle2_arc = Arc(radius=0.5, start_angle=66*DEGREES, angle=-np.pi/3).move_arc_center_to(triangle1.get_vertices()[0])

        # angle3_arc = Arc(radius=0.5, start_angle=90, angle=np.pi/3).move_arc_center_to(triangle2.get_vertices()[1])
        # angle4_arc = Arc(radius=0.5, start_angle=66*DEGREES, angle=-np.pi/3).move_arc_center_to(triangle2.get_vertices()[0])

        # Side lengths
        side1 = Text("4cm").next_to(Line(triangle1.get_vertices()[0], triangle1.get_vertices()[1]).get_center(), DOWN)
        # side2 = Text("a").next_to(Line(triangle2.get_vertices()[0], triangle2.get_vertices()[1]).get_center(), DOWN)

        # Animate the creation of elements
        self.play(Write(asa_rule))
        self.play(Create(triangle1))
        self.play(Write(label1_A), Write(label1_B), Write(label1_C))
        self.play(Create(angle1_arc), Create(angle2_arc))
        self.play(Write(angle1_label), Write(angle2_label))
        self.play(Write(side1))

        self.wait(2)
        self.fadeOutCurrentScene()

    def oneratwos(self):
        self.isRandom = False
        self.positionChoice = [[-4,0,0],[4,0,0]]
        a1=cvo.CVO().CreateCVO("RA-S-S","")
        a2=cvo.CVO().CreateCVO("Construction","")
        a2onnamelist=["Select a side-3cm","Draw arc from starting side-take 90","ViceVersa from other end-take 5cm","Traingle is formed"]
        a1.cvolist.append(a2)
        a2.extendOname(a2onnamelist)
        a2.setcircleradius(2)
        self.construct1(a1,a1)
        self.fadeOutCurrentScene()
        triangle1_vert = [[-2, 0, 0], [2, 0, 0], [-2, 2, 0]] 
        # triangle2_vert = [[-2, 0, 0], [2, 0, 0], [-2, 2, 0]]

        # Create triangles
        triangle1 = Polygon(*triangle1_vert, color=BLUE)
        # triangle2 = Polygon(*triangle2_vert, color=GREEN)

        # Shift triangles
        triangle1.shift(3 * LEFT + 2 * DOWN)
        # triangle2.shift(3 * RIGHT + 2 * DOWN)

        # Labels for vertices
        label1_A = Text("A").next_to(triangle1.get_vertices()[0], LEFT)
        label1_B = Text("B").next_to(triangle1.get_vertices()[1], RIGHT)
        label1_C = Text("C").next_to(triangle1.get_vertices()[2], UP)

        # label2_D = Text("D").next_to(triangle2.get_vertices()[0], LEFT)
        # label2_E = Text("E").next_to(triangle2.get_vertices()[1], RIGHT)
        # label2_F = Text("F").next_to(triangle2.get_vertices()[2], UP)

        # Rule text
        rhs_rule = Text("Right-Angle-Hypotenuse-Side (RHS) Example").to_edge(UP)

        # Right angle squares
        right_angle1 = Square(side_length=0.5).move_to(triangle1.get_vertices()[0] + np.array([0.25, 0.25, 0]))
        # right_angle2 = Square(side_length=0.5).move_to(triangle2.get_vertices()[0] + np.array([0.25, 0.25, 0]))

        # Side lengths
        hypotenuse1 = Text("5cm").next_to(Line(triangle1.get_vertices()[1], triangle1.get_vertices()[2]).get_center(), RIGHT)
        side1 = Text("3cm").next_to(Line(triangle1.get_vertices()[0], triangle1.get_vertices()[2]).get_center(), LEFT)
        
        # hypotenuse2 = Text("c").next_to(Line(triangle2.get_vertices()[1], triangle2.get_vertices()[2]).get_center(), RIGHT)
        # side2 = Text("a").next_to(Line(triangle2.get_vertices()[0], triangle2.get_vertices()[2]).get_center(), LEFT)

        # Animate the creation of elements
        self.play(Write(rhs_rule))
        self.play(Create(triangle1))
        self.play(Write(label1_A), Write(label1_B), Write(label1_C))
        self.play(Create(right_angle1))
        self.play(Write(hypotenuse1), Write(side1))

        self.wait(2)

       
        self.fadeOutCurrentScene()


        

if __name__ == "__main__":
    scene = ConstructionofTriangle()
    scene.render()
