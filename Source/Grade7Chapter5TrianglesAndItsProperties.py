import cvo
import json
from AbstractAnim import AbstractAnim
from manim import*

class TrianglesAndItsProperties(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.triangles()
        self.fadeOutCurrentScene()
        self.extriangle()
        self.fadeOutCurrentScene()
        self.classification()
        self.fadeOutCurrentScene()
        self.sides()
        self.fadeOutCurrentScene()
        self.angles()
        self.fadeOutCurrentScene()
        self.median()
        self.fadeOutCurrentScene()
        self.centroid()
        self.fadeOutCurrentScene()
        self.asp()
        self.fadeOutCurrentScene()
        self.extang()
        self.fadeOutCurrentScene()
        self.expro()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        self.fadeOutCurrentScene()
        
    def triangles(self):
        self.isRandom=False
        self.positionChoice=[[0,0,0]]
        p10=cvo.CVO().CreateCVO("Triangle","A closed figure made up of three line segments.")
        p10.setcircleradius(1.8)
        self.construct1(p10,p10)

    def extriangle(self):
        A = [-3, -1, 0]
        B = [3, -1, 0]
        C = [1, 2, 0]

        # Create triangle
        triangle = Polygon(A, B, C, color=BLUE, fill_opacity=0.3)

        # Center the triangle
        triangle.move_to(ORIGIN)
        

        Title = Text("Triangle").scale(0.7)
        Title.to_edge(UP)
        self.play(Write(Title,run_time=1))
        self.play(Create(triangle))

        # Label vertices
        labels = [MathTex(tex).next_to(point, direction)
                  for tex, point, direction in zip(["A", "B", "C"], [A, B, C], [LEFT*0.2+DOWN, RIGHT*0.2+DOWN, DOWN*0.5])]
        for label in labels:
            self.add(label)
        self.wait(2)
        sides=MathTex(r"\text{Sides : } \overline{AB} , \overline{BC} , \overline{CA}").next_to(triangle,DOWN*2)
        self.play(Write(sides,runtime=4))
        angles=MathTex(r"\text{Angles : }\angle{ABC} , \angle{BCA} , \angle{CAB}").next_to(sides,DOWN*0.5)
        self.play(Write(angles,runtime=4))

    def classification(self):
        self.isRandom=False
        self.setNumberOfCirclePositions(2)
        p10=cvo.CVO().CreateCVO("Triangle","Classifying them")
        p11=cvo.CVO().CreateCVO("Classification","")
        p11onamelist=["Based on Sides","Based on Angles"]
        p10.cvolist.append(p11)
        p11.extendOname(p11onamelist)
        self.construct1(p10,p10)
        
        
    def sides(self):
        side=Text("Classification based on sides :",font_size=28,color=GREEN).to_edge(UP)
        eqtext=Text("1.Equilateral Triangle",font_size=24).next_to(side,DOWN*3)
        eqtext.shift(LEFT*0.5)
        self.play(Write(side))
        self.play(Write(eqtext))
        A = [-1, 0, 0]
        B = [0, 0, 0]
        C = [-0.5, 1, 0]

        # Create triangle
        triangle = Polygon(A, B, C, color=BLUE, stroke_width=2).scale(1.5)
        self.play(Create(triangle))
        labels = [MathTex(tex).next_to(point, direction).scale(0.75)
                  for tex, point, direction in zip(["A", "B", "C"], [A, B, C], [LEFT*0.2+DOWN, RIGHT*0.2+DOWN, UP*0.7])]
        for label in labels:
            self.add(label)
            side_labels = [
            MathTex("1\\text{ cm}").scale(0.5),
            MathTex("1\\text{ cm}").scale(0.5),
            MathTex("1\\text{ cm}").scale(0.5)
        ]

        side_labels[0].move_to((np.array(A) + np.array(B)) / 2 + DOWN * 0.5)
        side_labels[1].move_to((np.array(B) + np.array(C)) / 2 + RIGHT * 0.2)
        side_labels[2].move_to((np.array(C) + np.array(A)) / 2 + LEFT * 0.2)

        side_labels[0].rotate(np.arctan2(B[1] - A[1], B[0] - A[0]))
        side_labels[1].rotate(np.arctan2(C[1] - B[1], C[0] - B[0]))
        side_labels[2].rotate(np.arctan2(A[1] - C[1], A[0] - C[0]))

        for side_label in side_labels:
            self.add(side_label)
        text=Text("All sides are Equal",font_size=24,color=BLUE).next_to(triangle,DOWN*3)
        self.play(Write(text,run_time=4))
        self.wait(4)
        self.fadeOutCurrentScene()
        self.add(side)

        #2222
        isotext=Text("2.Isoceles Triangle",font_size=24).next_to(side,DOWN*3)
        isotext.shift(LEFT*0.5)
        self.play(Write(isotext))
        A = [-1, 0, 0]
        B = [1, 0, 0]
        C = [0, 1, 0]

        # Create triangle
        triangle = Polygon(A, B, C, color=BLUE, stroke_width=2)
        self.play(Create(triangle))
        labels = [MathTex(tex).next_to(point, direction).scale(0.75)
                  for tex, point, direction in zip(["A", "B", "C"], [A, B, C], [LEFT*0.2+DOWN, RIGHT*0.2+DOWN, UP*0.7])]
        for label in labels:
            self.add(label)
        side_labels = [
            MathTex("2\\text{ cm}").scale(0.5),
            MathTex("1\\text{ cm}").scale(0.5),
            MathTex("1\\text{ cm}").scale(0.5)
        ]

        side_labels[0].move_to((np.array(A) + np.array(B)) / 2 + DOWN * 0.5)
        side_labels[1].move_to((np.array(B) + np.array(C)) / 2 + RIGHT * 0.2)
        side_labels[2].move_to((np.array(C) + np.array(A)) / 2 + LEFT * 0.2)

        side_labels[0].rotate(np.arctan2(B[1] - A[1], B[0] - A[0]))
        side_labels[1].rotate(np.arctan2(C[1] - B[1], C[0] - B[0]))
        side_labels[2].rotate(np.arctan2(A[1] - C[1], A[0] - C[0]))

        for side_label in side_labels:
            self.add(side_label)

        text=Text("Two sides are Equal",font_size=24,color=BLUE).next_to(triangle,DOWN*3)
        self.play(Write(text,run_time=4))
        self.wait(3)
        self.fadeOutCurrentScene()
        self.add(side)
        
        #3333333
        scatext=Text("3.Scalene Triangle",font_size=24).next_to(side,DOWN*3)
        scatext.shift(LEFT*0.5)
        self.play(Write(scatext))

        A = [-1, 0, 0]
        B = [2, 0, 0]
        C = [0, 1, 0]

        triangle = Polygon(A, B, C, color=BLUE, stroke_width=2)
        self.play(Create(triangle))
        labels = [MathTex(tex).next_to(point, direction).scale(0.75)
                  for tex, point, direction in zip(["A", "B", "C"], [A, B, C], [LEFT*0.2+DOWN, RIGHT*0.2+DOWN, UP*0.7])]
        for label in labels:
            self.add(label)
        side_labels = [
            MathTex("3\\text{ cm}").scale(0.5),
            MathTex("2\\text{ cm}").scale(0.5),
            MathTex("1\\text{ cm}").scale(0.5)
        ]

        side_labels[0].move_to((np.array(A) + np.array(B)) / 2 + DOWN * 0.5)
        side_labels[1].move_to((np.array(B) + np.array(C)) / 2 + RIGHT * 0.2)
        side_labels[2].move_to((np.array(C) + np.array(A)) / 2 + LEFT * 0.2)

        side_labels[0].rotate(np.arctan2(B[1] - A[1], B[0] - A[0]))
        side_labels[1].rotate(np.arctan2(C[1] - B[1], C[0] - B[0]))
        side_labels[2].rotate(np.arctan2(A[1] - C[1], A[0] - C[0]))

        for side_label in side_labels:
            self.add(side_label)

        text=Text("All Three sides are different",font_size=24,color=BLUE).next_to(triangle,DOWN*3)
        self.play(Write(text,run_time=4))
        self.wait(3)

    def angles(self):
        angle=Text("Classification based on angles :",font_size=28,color=GREEN).to_edge(UP)
        acutext=Text("1.Acute-angled Triangle",font_size=24).next_to(angle,DOWN*3)
        acutext.shift(LEFT*0.5)
        self.play(Write(angle))
        self.play(Write(acutext))
        
        vert = [[-2, 0, 0], [2, 0, 0], [0, 3, 0]]
        triangle1 = Polygon(*vert, color=BLUE)
        triangle1.shift(2 * DOWN)

        # Define vertex labels
        label1_A = Text("A").next_to(triangle1.get_vertices()[0], DOWN).scale(0.5)
        label1_B = Text("B").next_to(triangle1.get_vertices()[1], DOWN).scale(0.5)
        label1_C = Text("C").next_to(triangle1.get_vertices()[2], UP).scale(0.5)

        # Define angle labels
        angle1_label = MathTex(r"60^\circ").move_to(triangle1.get_vertices()[1] + 0.6 * LEFT + 0.4 * UP).scale(0.5)
        angle2_label = MathTex(r"70^\circ").move_to(triangle1.get_vertices()[0] + 0.6 * RIGHT + 0.4 * UP).scale(0.5).shift(RIGHT*0.1)
        angle3_label = MathTex(r"50^\circ").move_to(triangle1.get_vertices()[2] + 0.6 * LEFT + 0.4 * DOWN).scale(0.5)

        # Define angle arcs
        angle1_arc = Arc(radius=0.5, start_angle=90, angle=np.pi/3).move_arc_center_to(triangle1.get_vertices()[1])
        angle2_arc = Arc(radius=0.5, start_angle=60*DEGREES, angle=-np.pi/3).move_arc_center_to(triangle1.get_vertices()[0])
        angle3_arc = Arc(radius=0.6, start_angle=-PI/2 + PI/6, angle=-60*DEGREES).move_arc_center_to(triangle1.get_vertices()[2])

        # Play animations
        self.play(Create(triangle1), Write(label1_A), Write(label1_B), Write(label1_C))
        self.play(Create(angle1_arc), Create(angle2_arc), Create(angle3_arc), Write(angle1_label), Write(angle2_label), Write(angle3_label))
        therefore=Text("All angles inside the triangle are acute",font_size=24).next_to(triangle1,DOWN*3)
        self.play(Write(therefore,run_time=4))
        self.wait(4)
        self.fadeOutCurrentScene()

        #222
        self.add(angle)
        te=Text("2.Right-angled Triangle",font_size=24).next_to(angle,DOWN*3)
        self.play(Write(te))
        A = [-1, 0, 0]
        B = [0, 0, 0]
        C = [0, 1, 0]

        # Create triangle
        triangle = Polygon(A, B, C, color=BLUE, stroke_width=2).scale(1.5)
        self.play(Create(triangle))
        labels = [MathTex(tex).next_to(point, direction).scale(0.75)
                  for tex, point, direction in zip(["A", "B", "C"], [A, B, C], [LEFT*0.2+DOWN, RIGHT*0.2+DOWN, UP*0.7])]
        for label in labels:
            self.add(label)
        square = Square(side_length=0.2, color=BLUE).move_to([0, 0, 0]).shift(RIGHT*0.15+DOWN*0.15)
        self.play(Write(square))
        therefore=Text("one of angles is a right angle",font_size=24).next_to(triangle,DOWN*3)
        self.play(Write(therefore,run_time=4))
        self.wait(4)
        self.fadeOutCurrentScene()
        
        #333
        self.add(angle)
        te=Text("3.Obtuse-angled Triangle",font_size=24).next_to(angle,DOWN*3)
        self.play(Write(te))

        vertices = [[-2, 0, 0], [2, 0, 0], [-3, 3, 0]]
        triangle = Polygon(*vertices, color=BLUE).shift(DOWN*2)
        
        label_A = Text("A").next_to(vertices[0], DOWN).scale(0.5).shift(DOWN*2)
        label_B = Text("B").next_to(vertices[1], DOWN).scale(0.5).shift(DOWN*2)
        label_C = Text("C").next_to(vertices[2], UP).scale(0.5).shift(DOWN*2+LEFT*0.5)

        # Define angle labels
        angle1_label = MathTex(r"30^\circ").move_to(vertices[1] + 0.6 * LEFT + 0.4 * UP).scale(0.5).shift(DOWN*2)
        angle2_label = MathTex(r"100^\circ").move_to(vertices[0] + 0.6 * RIGHT + 0.4 * UP).scale(0.5).shift(DOWN*2)
        angle3_label = MathTex(r"50^\circ").move_to(vertices[2] + 0.6 * LEFT + 0.4 * DOWN).scale(0.5).shift(DOWN*2)

        # Define angle arcs
        angle1_arc = Arc(radius=0.5, start_angle=150*DEGREES, angle=30*DEGREES).move_arc_center_to(vertices[1]).shift(DOWN*2)
        angle2_arc = Arc(radius=0.5, start_angle=100*DEGREES, angle=-100*DEGREES).move_arc_center_to(vertices[0]).shift(DOWN*2)
        angle3_arc = Arc(radius=0.6, start_angle=-30*DEGREES, angle=-50*DEGREES).move_arc_center_to(vertices[2]).shift(DOWN*2)

        # Play animations
        self.play(Create(triangle), Write(label_A), Write(label_B), Write(label_C))
        self.play(Create(angle1_arc), Create(angle2_arc), Create(angle3_arc), Write(angle1_label), Write(angle2_label), Write(angle3_label))
        therefore=Text("one of angles is obtuse",font_size=24).next_to(triangle,DOWN*3.5)
        self.play(Write(therefore,run_time=4))
        self.wait(4)


    def median(self):
        
        title=Text("Median of a Triangle",font_size=28).to_edge(UP)
        self.play(Write(title))
        A = [-1, 0, 0]
        B = [2, 0, 0]
        C = [0, 1, 0]

        # Create triangle
        triangle = Polygon(A, B, C, color=BLUE, stroke_width=2)
        self.play(Create(triangle))

        # Create median from A to midpoint of BC
        midpoint_AB = [(A[0] + B[0]) / 2, (A[1] + B[1]) / 2, 0]
        median = Line(midpoint_AB, C, color=GREEN, stroke_width=2)
        self.play(Create(median))

        # Create labels for points A, B, C
        labels = [MathTex(tex).next_to(point, direction).scale(0.75)
                  for tex, point, direction in zip(["A", "B", "C"], [A, B, C], [LEFT*0.2, RIGHT*0.2, UP*0.2])]
        
        # Add the labels to the scene
        for label in labels:
            self.add(label)

        # Create and add label for midpoint D
        label_D = Text("D",font_size=24).next_to(midpoint_AB, DOWN*0.4)
        self.add(label_D)
        med=Text("The line drawn from a midpoint of a side to its opposite vertex is called median",font_size=24).next_to(triangle,DOWN*2)
        mte=MathTex(r"\text{In this case it is } \overline{AD}").next_to(med,DOWN*0.3).scale(0.8)
        self.play(Write(med,run_time=5))
        self.wait(3)
        self.play(Write(mte,run_time=4))
        self.wait(4)
        
    def centroid(self):
        title=Text("Centroid of a Triangle",font_size=28).to_edge(UP)
        self.play(Write(title))
        A = [-1, 0, 0]
        B = [2, 0, 0]
        C = [0, 1, 0]

        # Create triangle
        triangle = Polygon(A, B, C, color=BLUE, stroke_width=2)
        self.play(Create(triangle))

        # Create median from A to midpoint of BC
        midpoint_AB = [(A[0] + B[0]) / 2, (A[1] + B[1]) / 2, 0]
        midpoint_BC = [(B[0] + C[0]) / 2, (B[1] + C[1]) / 2, 0]
        midpoint_CA = [(C[0] + A[0]) / 2, (C[1] + A[1]) / 2, 0]
        
        median1 = Line(midpoint_AB, C, color=GREEN, stroke_width=2)
        median2 = Line(midpoint_BC, A, color=GREEN, stroke_width=2)
        median3 = Line(midpoint_CA, B, color=GREEN, stroke_width=2)
        
        
        self.play(Create(median1),Create(median2),Create(median3))

        # Create labels for points A, B, C
        labels = [MathTex(tex).next_to(point, direction).scale(0.75)
                  for tex, point, direction in zip(["A", "B", "C"], [A, B, C], [LEFT*0.2, RIGHT*0.2, UP*0.2])]
        
        # Add the labels to the scene
        for label in labels:
            self.add(label)

        # Create and add label for midpoint D
        label_D = Text("D",font_size=24).next_to(midpoint_AB, DOWN*0.4)
        label_E = Text("E",font_size=24).next_to(midpoint_BC, RIGHT*0.4)
        label_F = Text("F",font_size=24).next_to(midpoint_CA, LEFT*0.4)
        self.play(Write(label_D),Write(label_E),Write(label_F))
        label_G=Text("G", font_size=20).next_to(A,RIGHT*4.3 + UP*1.4)
        cen=Text("The point where all the 3 medians meet is called Centroid of a Triangle",font_size=24).next_to(triangle,DOWN*2)
        cen1=Text("In this case it is G",font_size=24).next_to(cen,DOWN*0.6)
        self.play(Write(label_G))
        self.play(Write(cen,run_time=4))
        self.play(Write(cen1,run_time=3))
        self.wait(4)


    def asp(self):
        self.isRandom=False
        self.setNumberOfCirclePositions(2)
        p10=cvo.CVO().CreateCVO("Triangle","Property")
        p11=cvo.CVO().CreateCVO("Angle Sum Property","The sum of the angles of a triangle is 180")
        p11.setcircleradius(2)
        p10.cvolist.append(p11)
        
        self.construct1(p10,p10)

    def extang(self):
        self.isRandom=False
        self.setNumberOfCirclePositions(2)
        p10=cvo.CVO().CreateCVO("Triangle","")
        p11=cvo.CVO().CreateCVO("Exterior Angle ","Lies to the exterior of the triangle")
        p11.setcircleradius(2)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
        t1=Text("Exterior angle example:",font_size=28).to_edge(UP)
        self.play(Write(t1,run_time=2))

        vert = [[-2, 0, 0], [2, 0, 0], [0, 3, 0]]
        triangle1 = Polygon(*vert, color=BLUE)
        triangle1.shift(2 * DOWN)

        # Define vertex labels
        label1_A = Text("A").next_to(triangle1.get_vertices()[0], DOWN).scale(0.5)
        label1_B = Text("B").next_to(triangle1.get_vertices()[1], DOWN).scale(0.5)
        label1_C = Text("C").next_to(triangle1.get_vertices()[2], UP).scale(0.5)
        label1_D = Text("D").next_to([4,-2,0], RIGHT).scale(0.5)

        # Define angle labels
        # angle1_label = MathTex(r"60^\circ").move_to(triangle1.get_vertices()[1] + 0.6 * LEFT + 0.4 * UP).scale(0.5)
        # angle2_label = MathTex(r"70^\circ").move_to(triangle1.get_vertices()[0] + 0.6 * RIGHT + 0.4 * UP).scale(0.5).shift(RIGHT*0.1)
        # angle3_label = MathTex(r"50^\circ").move_to(triangle1.get_vertices()[2] + 0.6 * LEFT + 0.4 * DOWN).scale(0.5)

        # Define angle arcs
        angle1_arc = Arc(radius=0.5, start_angle=90, angle=-np.pi/1.6).move_arc_center_to(triangle1.get_vertices()[1])
        angle2_arc = Arc(radius=0.5, start_angle=60*DEGREES, angle=-np.pi/3).move_arc_center_to(triangle1.get_vertices()[0])
        angle3_arc = Arc(radius=0.6, start_angle=-PI/2 + PI/6, angle=-60*DEGREES).move_arc_center_to(triangle1.get_vertices()[2])
        line=Line([2,-2,0],[4,-2,0],color=BLUE)
        t2=MathTex(r"\angle{CBD} \text{ is an Exterior angle}",font_size=30).next_to(triangle1,DOWN*3)
        
        self.play(Create(triangle1), Write(label1_A), Write(label1_B), Write(label1_C))
        self.play(Create(angle3_arc), Create(angle2_arc))
        self.play(Write(line),Write(angle1_arc),Write(label1_D))
        self.play(Write(t2,run_time=4))
        self.wait(4)

    def expro(self):
        self.isRandom=False
        self.setNumberOfCirclePositions(2)
        p10=cvo.CVO().CreateCVO("Exterior Angle","")
        p11=cvo.CVO().CreateCVO("Property ","An Exterior angle is equal to sum of its interior opposite angles")
        p11.setcircleradius(2)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

        t1=Text("Exterior angle property:",font_size=28).to_edge(UP)
        self.play(Write(t1,run_time=2))

        vert = [[-2, 0, 0], [2, 0, 0], [0, 3, 0]]
        triangle1 = Polygon(*vert, color=BLUE)
        triangle1.shift(2 * DOWN)

        # Define vertex labels
        label1_A = Text("A").next_to(triangle1.get_vertices()[0], DOWN).scale(0.5)
        label1_B = Text("B").next_to(triangle1.get_vertices()[1], DOWN).scale(0.5)
        label1_C = Text("C").next_to(triangle1.get_vertices()[2], UP).scale(0.5)
        label1_D = Text("D").next_to([4,-2,0], RIGHT).scale(0.5)

        # Define angle labels
        angle1_label = MathTex(r"120^\circ").move_to(triangle1.get_vertices()[1] + 0.8 * RIGHT + 0.4 * UP).scale(0.5)
        angle2_label = MathTex(r"60^\circ").move_to(triangle1.get_vertices()[0] + 0.6 * RIGHT + 0.4 * UP).scale(0.5).shift(RIGHT*0.1)
        angle3_label = MathTex(r"60^\circ").move_to(triangle1.get_vertices()[2] + 0.6 * RIGHT+ 0.3 * DOWN).scale(0.5)

        # Define angle arcs
        angle1_arc = Arc(radius=0.5, start_angle=90, angle=-np.pi/1.6).move_arc_center_to(triangle1.get_vertices()[1])
        angle2_arc = Arc(radius=0.5, start_angle=60*DEGREES, angle=-np.pi/3).move_arc_center_to(triangle1.get_vertices()[0])
        angle3_arc = Arc(radius=0.6, start_angle=-PI/2 + PI/6, angle=-60*DEGREES).move_arc_center_to(triangle1.get_vertices()[2])
        line=Line([2,-2,0],[4,-2,0],color=BLUE)
        t2=MathTex(r"\angle{CAB} + \angle{ACB} = \angle{CBD}",font_size=30).next_to(triangle1,DOWN*3)
        
        self.play(Create(triangle1), Write(label1_A), Write(label1_B), Write(label1_C))
        self.play(Create(angle3_arc), Create(angle2_arc), Write(angle2_label), Write(angle3_label))
        self.play(Write(line),Write(angle1_arc),Write(label1_D))
        self.play(Write(t2,run_time=4))
        self.play(Write(angle1_label))
        self.wait(4)

    def SetDeveloperList(self): 
       self.DeveloperList="T Sai Rohith Reddy" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade7Chapter5Triangles.py"
if __name__=="__main__":
    scene=TrianglesAndItsProperties()
    scene.render()