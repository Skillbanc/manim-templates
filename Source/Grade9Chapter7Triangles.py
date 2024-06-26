import json
from manim import*
from AbstractAnim import AbstractAnim
import cvo

class TrianglesAnim(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.LineSegment()
        self.fadeOutCurrentScene()
        self.Anim1()
        self.fadeOutCurrentScene()
        self.Triangle()
        self.fadeOutCurrentScene()
        self.SSS()
        self.fadeOutCurrentScene()
        self.Anim2()
        self.fadeOutCurrentScene()
        self.SAS()
        self.fadeOutCurrentScene()
        self.Anim3()
        self.fadeOutCurrentScene()
        self.ASA()
        self.fadeOutCurrentScene()
        self.Anim4()
        self.fadeOutCurrentScene()
        self.RHS()
        self.fadeOutCurrentScene()
        self.Anim5()
        self.fadeOutCurrentScene()
        self.inequalities()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        self.fadeOutCurrentScene()

        # self.fadeOutCurrentScene()
        
    # render using CVO data object 
    
    def LineSegment(self):
        self.isRandom=False
        self.positionChoice=[[-5,2,0],[-4,-0.5,0],[4,0,0]]
        p13=cvo.CVO().CreateCVO("Line segment","").setangle(-TAU/4)
        p10=cvo.CVO().CreateCVO("Congruency","")
        p11=cvo.CVO().CreateCVO("Rule","Equal Lengths")
        p13.cvolist.append(p10)
        p10.cvolist.append(p11)
        self.construct1(p13,p13)

    def Anim1(self):
        heading = Text("Congruent Line Segment")
        heading.to_edge(UP)

        # Define the length of the lines
        line_length = 4
        
        # Create two lines with the specified length
        line1 = Line(start=ORIGIN - line_length / 2 * RIGHT, end=ORIGIN + line_length / 2 * RIGHT)
        line2 = Line(start=ORIGIN - line_length / 2 * RIGHT, end=ORIGIN + line_length / 2 * RIGHT)
        
        # Position the lines side by side
        line1.move_to(2 * LEFT)
        line2.next_to(line1, RIGHT, buff=1)
        
        # Create labels for the lines
        label1_A = Text("A").next_to(line1.get_start(), DOWN)
        label1_B = Text("B").next_to(line1.get_end(), DOWN)
        label2_C = Text("C").next_to(line2.get_start(), DOWN)
        label2_D = Text("D").next_to(line2.get_end(), DOWN)
        mp_label1 = Text(str(line_length)).next_to(line1.get_center(), UP)
        mp_label2 = Text(str(line_length)).next_to(line2.get_center(), UP)

        # Animate the heading, lines, and labels
        self.play(Write(heading))
        self.play(Create(line1),  Write(label1_A), Write(label1_B), Write(mp_label1),)
        self.play(Create(line2), Write(label2_C), Write(label2_D), Write(mp_label2))

        # Hold the scene for a moment
        self.wait(2)
        
        # Animate the merging of the lines
        self.play(
            line2.animate.move_to(line1.get_center()),
            FadeOut(label2_C),
            FadeOut(label2_D),
            FadeOut(mp_label2),
            FadeOut(label1_A),
            FadeOut(label1_B)
        )

        # Remove old labels and add new merged labels
        self.play(
            FadeOut(label1_A),
            FadeOut(label1_B),
            FadeOut(mp_label1)
        )

        merged_label_start = Text("").next_to(line1.get_start(), DOWN)
        merged_label_end = Text("").next_to(line1.get_end(), DOWN)
        self.play(Write(merged_label_start), Write(merged_label_end), Write(mp_label1))
        
        # Hold the final scene
        self.wait(2)

    def Triangle(self):
        self.isRandom=False
        self.positionChoice=[[-5,2,0],[-4,-0.5,0],[4,2.25,0],[4,-2.25,0]]
        
        p13=cvo.CVO().CreateCVO("Triangle","").setangle(-TAU/4)
        p10=cvo.CVO().CreateCVO("Congruency","").setangle(-TAU/4)
        p11=cvo.CVO().CreateCVO("Types","")
        p11onamelist=["SSS","SAS","ASA","RAH"]
        p12=cvo.CVO().CreateCVO("Rules","")
        p12onamelist=["Equal Vertices","Equal Sides","Equal Angles"]
        
        p10.setcircleradius(1.25)
        p11.setcircleradius(1.6)
        p12.setcircleradius(1.6)

        p13.cvolist.append(p10)
        p10.cvolist.append(p11)
        p11.extendOname(p11onamelist)
        p10.cvolist.append(p12)
        p12.extendOname(p12onamelist)
        self.construct1(p13,p13)

    def SSS(self):
        self.isRandom=False
        self.positionChoice=[[-4,0,0],[4,2,0],[4,-2,0]]
        p10=cvo.CVO().CreateCVO("SSS","").setangle(-TAU/4)
        p11=cvo.CVO().CreateCVO("Abbreviation","Side-Side-Side")
        p12=cvo.CVO().CreateCVO("Rule","All sides equal")

        p12.setcircleradius(1.5)
        p11.setcircleradius(1.5)

        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)

    def Anim2(self):
        triangle1_vert=[[-2, 0, 0],[2, 0, 0],[0, 3, 0]] 
        triangle2_vert=[[-2, 0, 0],[2, 0, 0],[0, 3, 0]]

        triangle1 = Polygon(*triangle1_vert, color=BLUE)
        triangle2 = Polygon(*triangle2_vert, color=GREEN)

        triangle1.shift(3 * LEFT)
        triangle2.shift(3 * RIGHT)
        triangle1.shift(2*DOWN)
        triangle2.shift(2*DOWN)

        label1_A = Text("A").next_to(triangle1.get_vertices()[0], DOWN)
        label1_B = Text("B").next_to(triangle1.get_vertices()[1], DOWN)
        label1_C = Text("C").next_to(triangle1.get_vertices()[2], UP)

        label2_D = Text("D").next_to(triangle2.get_vertices()[0], DOWN)
        label2_E = Text("E").next_to(triangle2.get_vertices()[1], DOWN)
        label2_F = Text("F").next_to(triangle2.get_vertices()[2], UP)

        sss_rule = Text("Side-Side-Side (SSS) Rule").to_edge(UP)
        
        
        # Side lengths
        side1 = Text("a").next_to(Line(triangle1.get_vertices()[0], triangle1.get_vertices()[1]).get_center(), DOWN)
        side2 = Text("b").next_to(Line(triangle1.get_vertices()[1], triangle1.get_vertices()[2]).get_center(), RIGHT)
        side3 = Text("c").next_to(Line(triangle1.get_vertices()[2], triangle1.get_vertices()[0]).get_center(), LEFT)
        
        side4 = Text("a").next_to(Line(triangle2.get_vertices()[0], triangle2.get_vertices()[1]).get_center(), DOWN)
        side5 = Text("b").next_to(Line(triangle2.get_vertices()[1], triangle2.get_vertices()[2]).get_center(), RIGHT)
        side6 = Text("c").next_to(Line(triangle2.get_vertices()[2], triangle2.get_vertices()[0]).get_center(), LEFT)

        self.play(Write(sss_rule))
        self.play(Create(triangle1), Write(label1_A), Write(label1_B), Write(label1_C))
        self.play(Write(side1), Write(side2), Write(side3))
        self.play(Create(triangle2), Write(label2_D), Write(label2_E), Write(label2_F))
        self.play(Write(side4), Write(side5), Write(side6))

        self.wait(2)
        
        # Animate merging the triangles
        self.play(
            triangle2.animate.move_to(triangle1.get_center()),
            FadeOut(label2_D),
            FadeOut(label2_E),
            FadeOut(label2_F),
            FadeOut(side4),
            FadeOut(side5),
            FadeOut(side6),
            FadeOut(label1_A),
            FadeOut(label1_B),
            FadeOut(label1_C)
        )

        self.wait(2)

    def SAS(self):
        self.isRandom=False
        self.positionChoice=[[-4,0,0],[4,2,0],[4,-2,0]]
        p10=cvo.CVO().CreateCVO("SAS","").setangle(-TAU/4)
        p11=cvo.CVO().CreateCVO("Abbreviation","Side-Angle-Side")
        p12=cvo.CVO().CreateCVO("Rule","")
        p12onameList=["2 sides equal","included angle equal"]

        p12.setcircleradius(1.5)
        p11.setcircleradius(1.5)

        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p12.extendOname(p12onameList)
        self.construct1(p10,p10)

    def Anim3(self):
        triangle1_vert = [[-2, 0, 0], [2, 0, 0], [0, 3, 0]] 
        triangle2_vert = [[-2, 0, 0], [2, 0, 0], [0, 3, 0]]

        # Create triangles
        triangle1 = Polygon(*triangle1_vert, color=BLUE)
        triangle2 = Polygon(*triangle2_vert, color=GREEN)

        # Shift triangles
        triangle1.shift(3 * LEFT)
        triangle2.shift(3 * RIGHT)
        triangle1.shift(2 * DOWN)
        triangle2.shift(2 * DOWN)

        # Labels for vertices
        label1_A = Text("A").next_to(triangle1.get_vertices()[0], DOWN)
        label1_B = Text("B").next_to(triangle1.get_vertices()[1], DOWN)
        label1_C = Text("C").next_to(triangle1.get_vertices()[2], UP)

        label2_D = Text("D").next_to(triangle2.get_vertices()[0], DOWN)
        label2_E = Text("E").next_to(triangle2.get_vertices()[1], DOWN)
        label2_F = Text("F").next_to(triangle2.get_vertices()[2], UP)

        # Rule text
        sas_rule = Text("Side-Angle-Side (SAS) Rule").to_edge(UP)

        # Angle labels
        angle1_label = MathTex(r"\alpha").move_to(triangle1.get_vertices()[1] + 0.6 * LEFT + 0.4 * UP)
        angle2_label = MathTex(r"\alpha").move_to(triangle2.get_vertices()[1] + 0.6 * LEFT + 0.4 * UP)

        # Angle arcs
        angle1_arc = Arc(radius=0.5, start_angle=90, angle=np.pi/3).move_arc_center_to(triangle1.get_vertices()[1])
        angle2_arc = Arc(radius=0.5, start_angle=90, angle=np.pi/3).move_arc_center_to(triangle2.get_vertices()[1])

        # Side lengths
        side1 = Text("a").next_to(Line(triangle1.get_vertices()[0], triangle1.get_vertices()[1]).get_center(), DOWN)
        side2 = Text("b").next_to(Line(triangle1.get_vertices()[1], triangle1.get_vertices()[2]).get_center(), RIGHT)
        
        side4 = Text("a").next_to(Line(triangle2.get_vertices()[0], triangle2.get_vertices()[1]).get_center(), DOWN)
        side5 = Text("b").next_to(Line(triangle2.get_vertices()[1], triangle2.get_vertices()[2]).get_center(), RIGHT)

        # Animate the creation of elements
        self.play(Write(sas_rule))
        self.play(Create(triangle1), Write(label1_A), Write(label1_B), Write(label1_C))
        self.play(Create(angle1_arc),Write(angle1_label), Write(side1), Write(side2),)
        self.play(Create(triangle2), Write(label2_D), Write(label2_E), Write(label2_F))
        self.play(Create(angle2_arc), Write(angle2_label), Write(side4), Write(side5))

        self.wait(2)
        
        # Animate merging the triangles
        self.play(
            triangle2.animate.move_to(triangle1.get_center()),
            FadeOut(label2_D),
            FadeOut(label2_E),
            FadeOut(label2_F),
            FadeOut(angle2_arc),
            FadeOut(angle2_label),
            FadeOut(side4),
            FadeOut(side5),
            FadeOut(label1_A),
            FadeOut(label1_B),
            FadeOut(label1_C)
        )

        self.wait(2)

    def ASA(self):
        self.isRandom=False
        self.positionChoice=[[-4,0,0],[4,2,0],[4,-2,0]]
        p10=cvo.CVO().CreateCVO("ASA","").setangle(-TAU/4)
        p11=cvo.CVO().CreateCVO("Abbreviation","Angle-Side-Angle")
        p12=cvo.CVO().CreateCVO("Rule","")
        p12onameList=["2 angles equal","side b/w equal"]

        p12.setcircleradius(1.5)
        p11.setcircleradius(1.5)

        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p12.extendOname(p12onameList)
        self.construct1(p10,p10)

    def Anim4(self):
        triangle1_vert = [[-2, 0, 0], [2, 0, 0], [0, 3, 0]] 
        triangle2_vert = [[-2, 0, 0], [2, 0, 0], [0, 3, 0]]

        # Create triangles
        triangle1 = Polygon(*triangle1_vert, color=BLUE)
        triangle2 = Polygon(*triangle2_vert, color=GREEN)

        # Shift triangles
        triangle1.shift(3 * LEFT)
        triangle2.shift(3 * RIGHT)
        triangle1.shift(2 * DOWN)
        triangle2.shift(2 * DOWN)

        # Labels for vertices
        label1_A = Text("A").next_to(triangle1.get_vertices()[0], DOWN)
        label1_B = Text("B").next_to(triangle1.get_vertices()[1], DOWN)
        label1_C = Text("C").next_to(triangle1.get_vertices()[2], UP)

        label2_D = Text("D").next_to(triangle2.get_vertices()[0], DOWN)
        label2_E = Text("E").next_to(triangle2.get_vertices()[1], DOWN)
        label2_F = Text("F").next_to(triangle2.get_vertices()[2], UP)

        # Rule text
        asa_rule = Text("Angle-Side-Angle (ASA) Rule").to_edge(UP)

        # Angle labels
        angle1_label = MathTex(r"\alpha").move_to(triangle1.get_vertices()[1] + 0.6 * LEFT + 0.4 * UP)
        angle2_label = MathTex(r"\beta").move_to(triangle1.get_vertices()[0] + 0.6 * RIGHT + 0.4 * UP)

        angle3_label = MathTex(r"\alpha").move_to(triangle2.get_vertices()[1] + 0.6 * LEFT + 0.4 * UP)
        angle4_label = MathTex(r"\beta").move_to(triangle2.get_vertices()[0] + 0.6 * RIGHT + 0.4 * UP)

        # Angle arcs
        angle1_arc = Arc(radius=0.5, start_angle=90, angle=np.pi/3).move_arc_center_to(triangle1.get_vertices()[1])
        angle2_arc = Arc(radius=0.5, start_angle=66*DEGREES, angle=-np.pi/3).move_arc_center_to(triangle1.get_vertices()[0])

        angle3_arc = Arc(radius=0.5, start_angle=90, angle=np.pi/3).move_arc_center_to(triangle2.get_vertices()[1])
        angle4_arc = Arc(radius=0.5, start_angle=66*DEGREES, angle=-np.pi/3).move_arc_center_to(triangle2.get_vertices()[0])

        # Side lengths
        side1 = Text("a").next_to(Line(triangle1.get_vertices()[0], triangle1.get_vertices()[1]).get_center(), DOWN)
        side2 = Text("a").next_to(Line(triangle2.get_vertices()[0], triangle2.get_vertices()[1]).get_center(), DOWN)

        # Animate the creation of elements
        self.play(Write(asa_rule))
        self.play(Create(triangle1), Write(label1_A), Write(label1_B), Write(label1_C))
        self.play(Create(triangle2), Write(label2_D), Write(label2_E), Write(label2_F))
        self.play(Create(angle1_arc), Create(angle2_arc),Write(angle1_label), Write(angle2_label) )
        self.play(Create(angle3_arc), Create(angle4_arc), Write(angle3_label), Write(angle4_label))
        self.play(Write(side1))
        self.play(Write(side2))

        self.wait(2)
        
        # Animate merging the triangles
        self.play(
            triangle2.animate.move_to(triangle1.get_center()),
            FadeOut(label2_D),
            FadeOut(label2_E),
            FadeOut(label2_F),
            FadeOut(angle3_arc),
            FadeOut(angle4_arc),
            FadeOut(angle3_label),
            FadeOut(angle4_label),
            FadeOut(side2),
            FadeOut(side1),
            FadeOut(label1_A),
            FadeOut(label1_B),
            FadeOut(label1_C)
        )
        self.play(Write(side1))
        self.wait(2)

    def RHS(self):
        self.isRandom=False
        self.positionChoice=[[-4,0,0],[4,1.5,0],[4,-2,0]]
        p10=cvo.CVO().CreateCVO("RHS","").setangle(-TAU/4)
        p11=cvo.CVO().CreateCVO("Abbreviation","Right-Angle-Hypotenuse-Side")
        p12=cvo.CVO().CreateCVO("Rule","")
        p12onameList=["Hypotenuse equal","another side equal"]

        p12.setcircleradius(2)
        p11.setcircleradius(1.8)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p12.extendOname(p12onameList)
        self.construct1(p10,p10)

    def Anim5(self):
        triangle1_vert = [[-2, 0, 0], [2, 0, 0], [-2, 2, 0]] 
        triangle2_vert = [[-2, 0, 0], [2, 0, 0], [-2, 2, 0]]

        # Create triangles
        triangle1 = Polygon(*triangle1_vert, color=BLUE)
        triangle2 = Polygon(*triangle2_vert, color=GREEN)

        # Shift triangles
        triangle1.shift(3 * LEFT + 2 * DOWN)
        triangle2.shift(3 * RIGHT + 2 * DOWN)

        # Labels for vertices
        label1_A = Text("A").next_to(triangle1.get_vertices()[0], LEFT)
        label1_B = Text("B").next_to(triangle1.get_vertices()[1], RIGHT)
        label1_C = Text("C").next_to(triangle1.get_vertices()[2], UP)

        label2_D = Text("D").next_to(triangle2.get_vertices()[0], LEFT)
        label2_E = Text("E").next_to(triangle2.get_vertices()[1], RIGHT)
        label2_F = Text("F").next_to(triangle2.get_vertices()[2], UP)

        # Rule text
        rhs_rule = Text("Right-Angle-Hypotenuse-Side (RHS) Rule").to_edge(UP)

        # Right angle squares
        right_angle1 = Square(side_length=0.5).move_to(triangle1.get_vertices()[0] + np.array([0.25, 0.25, 0]))
        right_angle2 = Square(side_length=0.5).move_to(triangle2.get_vertices()[0] + np.array([0.25, 0.25, 0]))

        # Side lengths
        hypotenuse1 = Text("c").next_to(Line(triangle1.get_vertices()[1], triangle1.get_vertices()[2]).get_center(), RIGHT)
        side1 = Text("a").next_to(Line(triangle1.get_vertices()[0], triangle1.get_vertices()[2]).get_center(), LEFT)
        
        hypotenuse2 = Text("c").next_to(Line(triangle2.get_vertices()[1], triangle2.get_vertices()[2]).get_center(), RIGHT)
        side2 = Text("a").next_to(Line(triangle2.get_vertices()[0], triangle2.get_vertices()[2]).get_center(), LEFT)

        # Animate the creation of elements
        self.play(Write(rhs_rule))
        self.play(Create(triangle1), Write(label1_A), Write(label1_B), Write(label1_C) )
        self.play(Create(triangle2), Write(label2_D), Write(label2_E), Write(label2_F))
        self.play(Create(right_angle1), Write(hypotenuse1), Write(side1))
        self.play(Create(right_angle2), Write(hypotenuse2), Write(side2))

        self.wait(2)
        
        # Animate merging the triangles
        self.play(
            triangle2.animate.move_to(triangle1.get_center()),
            FadeOut(label2_D),
            FadeOut(label2_E),
            FadeOut(label2_F),
            FadeOut(right_angle2),
            FadeOut(hypotenuse2),
            FadeOut(side2),
            FadeOut(side1),
            FadeOut(label1_A),
            FadeOut(label1_B),
            FadeOut(label1_C)
        )

        self.wait(2)
    
    def inequalities(self):
        self.isRandom=False
        self.positionChoice=[[-5,2,0],[-4,0,0],[4,1.5,0],[4,-2,0]]
        p10=cvo.CVO().CreateCVO("inequalities","").setangle(-TAU/4)
        p13=cvo.CVO().CreateCVO("triangle","").setangle(-TAU/4)
        
        p11=cvo.CVO().CreateCVO("theorem","the angle opposite to the longer side is greater").setangle(-TAU/4)
        p12=cvo.CVO().CreateCVO("theorem","side opposite to the larger angle is longer").setangle(-TAU/4)
        p12.setcircleradius(2)
        p11.setcircleradius(1.8)
        p13.cvolist.append(p10)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p13,p13)

    def SetDeveloperList(self): 
       self.DeveloperList="T Sai Rohith Reddy" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade9Chapter7Triangles.py"

if __name__ == "__main__":
    scene=TrianglesAnim()
    scene.render()

