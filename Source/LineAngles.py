from manim import *
from AbstractAnim import AbstractAnim
import cvo

class LineAngle(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Line()
        self.fadeOutCurrentScene()
        self.display_point()
        self.display_line_segment()
        self.display_ray()
        self.display_line()
        self.fadeOutCurrentScene()
        self.collinear()
        # self.fadeOutCurrentScene()
        self.collinear1()
        self.fadeOutCurrentScene()
        self.Angle()
        #self.fadeOutCurrentScene()
        self.Angle1()
        self.fadeOutCurrentScene()
        self.Lines()
        self.fadeOutCurrentScene()
        self.parallelanim()
        self.fadeOutCurrentScene()
        self.Intersectanim()
        self.fadeOutCurrentScene()
        self.Concurrentanim()
        self.fadeOutCurrentScene()
        self.Pairs()
        self.fadeOutCurrentScene()
        self.intersect()
        self.fadeOutCurrentScene()
        self.VerticalTheorem()
        self.fadeOutCurrentScene()
        self.parallel()
        self.fadeOutCurrentScene()
        self.ParallelLinesTheorem()
        self.fadeOutCurrentScene()
        self.Transversal()
        self.fadeOutCurrentScene()
        self.TransversalAnim()
        self.fadeOutCurrentScene()
        self.Triangle()
        self.fadeOutCurrentScene()
        self.Triangle1()


    def Line(self):
        self.positionChoice=[[-5,-2,0],[1,-2,0],[-4,2,0],[-1,2,0],[3,2,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Lines","")
        p11=cvo.CVO().CreateCVO("Point","")
        p12=cvo.CVO().CreateCVO("Line","")
        p13=cvo.CVO().CreateCVO("Ray","")
        p14=cvo.CVO().CreateCVO("Line Segment","")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        self.construct1(p10,p10)

   
    def display_point(self):
        # Title
        title = Text("LINE TYPES").to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Create point and its label
        point = Dot(LEFT*2)
        point_label = Text("Point").next_to(point, DOWN)
        point_name = MathTex("A").next_to(point, LEFT)
        info=Text("A is point",font_size=24).next_to(point_label,RIGHT)
        
        # Animate point and its labels
        self.play(Create(point), Write(point_label))
        self.play(Write(point_name))
        self.play(Write(info))
        self.wait(1)
        self.play(FadeOut(point), FadeOut(point_label), FadeOut(point_name), FadeOut(title),FadeOut(info))
        
    def display_line_segment(self):
        # Title
        title = Text("LINE TYPES").to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Create line segment and its labels
        start_point = Dot(LEFT*3)
        end_point = Dot(RIGHT*3)
        segment = Line(start_point.get_center(), end_point.get_center(), color=BLUE)
        segment_label = Text("Line Segment").next_to(segment, UP)
        start_label = MathTex("A").next_to(start_point, LEFT)
        end_label = MathTex("B").next_to(end_point, RIGHT)
        info=Text("AB is a line segment",font_size=24).next_to(segment,DOWN)
        
        # Animate line segment and its labels
        self.play(Create(start_point), Create(end_point))
        self.play(Create(segment), Write(segment_label))
        self.play(Write(start_label), Write(end_label))
        self.play(Write(info))
        self.wait(1)
        self.play(FadeOut(start_point), FadeOut(end_point), FadeOut(segment), FadeOut(segment_label),
                  FadeOut(start_label), FadeOut(end_label), FadeOut(title),FadeOut(info))
        
    def display_ray(self):
        # Title
        title = Text("LINE TYPES").to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Create ray and its labels
        start_point = Dot(ORIGIN)
        end_point = Dot(RIGHT*3)
        ray = Arrow(start_point.get_center(), end_point.get_center(), color=GREEN)
        ray_label = Text("Ray").next_to(ray, UP)
        start_label = MathTex("A").next_to(start_point, LEFT)
        end_label = MathTex("B").next_to(end_point, RIGHT)
        info=Text("AB is a Ray",font_size=24).next_to(ray,DOWN)
        
        # Animate ray and its labels
        self.play(Create(start_point), Create(end_point))
        self.play(Create(ray), Write(ray_label))
        self.play(Write(start_label), Write(end_label))
        self.play(Write(info))
        self.wait(1)
        self.play(FadeOut(start_point), FadeOut(end_point), FadeOut(ray), FadeOut(ray_label),
                  FadeOut(start_label), FadeOut(end_label), FadeOut(title),FadeOut(info))
        
    def display_line(self):
        # Title
        title = Text("LINE TYPES").to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Create line and its labels
        start_point = Dot(LEFT*3)
        end_point = Dot(RIGHT)
        line = DoubleArrow(start_point.get_center(), end_point.get_center(), color=RED)
        line_label = Text("Line").next_to(line, UP)
        start_label = MathTex("A").next_to(start_point, LEFT)
        end_label = MathTex("B").next_to(end_point, RIGHT)
        info=Text("AB is a Line",font_size=24).next_to(line,DOWN)
        
        # Animate line and its labels
        self.play(Create(start_point), Create(end_point))
        self.play(Create(line), Write(line_label))
        self.play(Write(start_label), Write(end_label))
        self.play(Write(info))
        self.wait(1)
        self.play(FadeOut(start_point), FadeOut(end_point), FadeOut(line), FadeOut(line_label),
                  FadeOut(start_label), FadeOut(end_label), FadeOut(title),Write(info))


    def collinear(self):
        self.positionChoice=[[-4,-2,0],[-4,2,0],[3,-2,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Collinear Points", "")
        p11=cvo.CVO().CreateCVO("Property","Points lying on same line")
        p12=cvo.CVO().CreateCVO("Example","A,B,C,D,E")
        p11.setcircleradius(2) 
        p10.cvolist.append(p11) 
        p10.cvolist.append(p12) 
        self.construct1(p10, p10)

    def collinear1(self):
        title = Text("Collinear Points").to_edge(UP)
        
        # Create dots representing points A, B, C, D
        points = [Dot(np.array([x, 1, 0])) for x in range(-2, 3)]
        
        # Create a line passing through these points
        line = Line(points[0].get_center(), points[-1].get_center(), color=RED)
        
        # Label points as A, B, C, D
        labels = [Text(chr(65 + i)).next_to(point, DOWN) for i, point in enumerate(points)]
        
        # Animate title and line
        self.play(Write(title))
        self.wait(0.5)
        self.play(Create(line))
        self.wait(0.5)
        
        # Animate creation of points and labels
        self.play(*[Create(point) for point in points])
        self.wait(0.5)
        self.play(*[Write(label) for label in labels])
        self.wait(1)

        # Clear scene after displaying all


    def Angle(self):
        self.positionChoice=[[-4,-2,0],[4,-2,0],[4,1,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Angle", "")
        p11=cvo.CVO().CreateCVO("Property","Two rays share common end point")
        p12=cvo.CVO().CreateCVO("Example",r"$\angle BAC \quad is \quad an \quad angle$")
        p10.cvolist.append(p11)  
        p10.cvolist.append(p12)  
        self.construct1(p10, p10)

    def Angle1(self):
        title = Text("Angle").to_edge(UP)
        
        # Define points A, B, C
        A = np.array([-2, 0, 0])
        B = np.array([0, 2, 0])
        C = np.array([2, 0, 0])
        
        # Create lines AB and AC
        line_AB = Line(A, B, color=BLUE)
        line_AC = Line(A, C, color=GREEN)
        
        # Create angle arc with label
        angle_arc = Angle(line_AC, line_AB, radius=0.5, color=RED)
        angle_label = MathTex(r"\theta").next_to(angle_arc, UP)

        # Label points A, B, C
        points_labels = [Text(label, font_size=18).next_to(point, DOWN) for point, label in zip([A, B, C], ["A", "B", "C"])]

        # Animate title and lines
        self.play(Write(title))
        self.wait(0.5)
        self.play(Create(line_AB), Create(line_AC))
        self.wait(0.5)
        
        # Animate angle arc and label
        self.play(Create(angle_arc), Write(angle_label))
        self.wait(0.5)

        # Animate labels for points A, B, C
        self.play(*[Write(label) for label in points_labels])
        self.wait(1)



    def Lines(self):
        self.positionChoice=[[-3,-2,0],[-3,2,0],[3,2,0],[4,-2,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Lines","")
        p11=cvo.CVO().CreateCVO("Parallel lines","")
        p12=cvo.CVO().CreateCVO("Intersecting lines","")
        p13=cvo.CVO().CreateCVO("Concurrent lines","")
        p10.setcircleradius(1)
        p11.setcircleradius(1)
        p12.setcircleradius(1)
        p13.setcircleradius(1)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.construct1(p10,p10)

    def parallelanim(self):
        title = Text("Parallel Lines").to_edge(UP)
        description = Text("Definition: Lines which do not meet at any point", font_size=24).next_to(title, DOWN)

    # Define the lines
        line1 = Line([-4, -1, 0], [4, -1, 0], color=BLUE)
        line2 = Line([-4, 1, 0], [4, 1, 0], color=BLUE)
    # Animations
        self.play(Write(title), Write(description))
        self.play(Create(line1), Create(line2))
        self.wait(2)
        

    def Intersectanim(self):
         # Title and description
        title = Text("Intersecting Lines").to_edge(UP)
        description = Text("Definition: Lines which meet at a point", font_size=24).next_to(title, DOWN)

        # Define the lines
        line3 = Line([-3, -2, 0], [3, 2, 0], color=GREEN)
        line4 = Line([-3, 2, 0], [3, -2, 0], color=GREEN)

        # Compute intersection point (assuming intersection at origin for simplicity)
        intersection_point = np.array([0, 0, 0])

        # Create a dot at the intersection point
        dot = Dot(intersection_point, color=RED)
        dot_label = Text("Intersection Point", font_size=18).next_to(dot, RIGHT)

        # Animations
        self.play(Write(title), Write(description))
        self.play(Create(line3), Create(line4))
        self.play(FadeIn(dot), Write(dot_label))
        self.wait(2)
       

    def Concurrentanim(self):
        title = Text("Concurrent Lines").to_edge(UP)
        description = Text("Definition:Two or more lines meet at a point", font_size=24).next_to(title, DOWN)

    # Define the lines
       
        line3 = Line([-3, -2, 0], [3, 2, 0], color=RED).scale(0.5)
        line4 = Line([-3, 2, 0], [3, -2, 0], color=RED).scale(0.5)
        line5 = Line([-2, -3, 0], [2, 3, 0], color=RED).scale(0.5)
        line6 = Line([-2, 3, 0], [2, -3, 0], color=RED).scale(0.5)
        line7 = Line([-3, 0, 0], [3, 0 ,0], color=RED).scale(0.5)

        intersection_point = np.array([0, 0, 0])

        # Create a dot at the intersection point
        dot = Dot(intersection_point, color=WHITE)
        dot_label = Text("Intersection Point", font_size=18).next_to(line7.get_end(), RIGHT)

    # Animations
        self.play(Write(title), Write(description))
        self.play(Create(line3), Create(line4),Create(line5), Create(line6),Create(line7))
        self.play(FadeIn(dot), Write(dot_label))
        self.wait(2)
       

    def Pairs(self):
        self.positionChoice=[[0,2,0],[-4,2,0],[4,2,0],[-4,-1,0],[4,-1,0],[0,-2,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Angle Pairs","")
        p11=cvo.CVO().CreateCVO("Complementary Angles",r"$Sum \quad of \quad Adjacent \quad angles = 90^\circ$")
        p12=cvo.CVO().CreateCVO("Supplementary Angles",r"$Sum \quad of \quad Adjacent \quad angles = 180^\circ$")
        p13=cvo.CVO().CreateCVO("Conjugate Angles",r"$Sum \quad of \quad Adjacent \quad angles = 360^\circ$")
        p14=cvo.CVO().CreateCVO("Adjacent Angle","having a common arm \& vertex")
        p15=cvo.CVO().CreateCVO("Linear Pair","Adjacent angles forming a straight line")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        self.construct1(p10,p10)

    def intersect(self):
        self.setNumberOfCirclePositions(2)
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Intersecting lines", "")
        p11=cvo.CVO().CreateCVO("Property","When 2 lines intersect,vertically opposite angles are equal")
        p11.setcircleradius(2) 
        p10.cvolist.append(p11) 
        self.construct1(p10, p10)

    def VerticalTheorem(self):
        # Title
       
        title = Text("Vertically Opposite Angles Theorem").to_edge(UP)
        self.play(Write(title))

        # Define lines and intersection point
        line_AB = Line(LEFT*3, RIGHT*3, color=BLUE)
        line_CD = Line(DOWN*1.5, UP*1.5, color=BLUE)
        intersection = line_AB.get_center()

        # Labels for lines and intersection point
        label_AB = MathTex("A").next_to(line_AB, RIGHT)
        label_BA = MathTex("B").next_to(line_AB, LEFT)
        label_CD = MathTex("C").next_to(line_CD, UP)
        label_DC = MathTex("D").next_to(line_CD, DOWN)
        label_O = MathTex("O").move_to(intersection).shift(UP*0.5)

        self.play(Create(line_AB), Create(line_CD))
        self.play(Write(label_AB), Write(label_BA), Write(label_CD), Write(label_DC), Write(label_O))

        # Create arcs for angles
        arc_AOC = Arc(radius=0.8, angle=TAU/8, start_angle=PI/4, color=YELLOW).move_arc_center_to(intersection)
        arc_BOD = Arc(radius=0.8, angle=TAU/8, start_angle=PI+PI/4, color=YELLOW).move_arc_center_to(intersection)
        arc_DOA = Arc(radius=0.8, angle=TAU/8, start_angle=-PI/4, color=YELLOW).move_arc_center_to(intersection)
        arc_COB = Arc(radius=0.8, angle=TAU/8, start_angle=PI-PI/4, color=YELLOW).move_arc_center_to(intersection)

        self.play(Create(arc_AOC), Create(arc_BOD), Create(arc_DOA), Create(arc_COB))

        # Labels for angles
        label_AOC = MathTex(r"\angle AOC").next_to(arc_AOC.point_from_proportion(0.5), UR)
        label_BOD = MathTex(r"\angle BOD").next_to(arc_BOD.point_from_proportion(0.5), UL)
        label_DOA = MathTex(r"\angle DOA").next_to(arc_DOA.point_from_proportion(0.5), DR)
        label_COB = MathTex(r"\angle COB").next_to(label_CD, DL)

        explanation_text = VGroup(
            MathTex(r"\angle AOC = \angle BOD"),
            MathTex(r"\angle COB = \angle DOA"),
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.8).to_edge(DOWN)

        self.play(Write(label_AOC), Write(label_BOD), Write(label_DOA), Write(label_COB))
        self.wait(2)
        self.play(Write(explanation_text))

        self.wait(4)
        self.play(
            FadeOut(title),
            FadeOut(line_AB), FadeOut(line_CD),
            FadeOut(label_AB), FadeOut(label_BA), FadeOut(label_CD), FadeOut(label_DC), FadeOut(label_O),
            FadeOut(arc_AOC), FadeOut(arc_BOD), FadeOut(arc_DOA), FadeOut(arc_COB),
            FadeOut(label_AOC), FadeOut(label_BOD), FadeOut(label_DOA), FadeOut(label_COB),FadeOut(explanation_text))


        # Proof steps
        # proof_steps = [
        # "Proof:",
        # "1. Ray OA stands on line CD at point O.",
        # "2. Thus, by the linear pair of angles axiom:",
        # "AOC + DOA = 180",
        # "3. Similarly,",
        # "DOA + BOD = 180",
        # "4. Therefore, equating the above two equations:",
        # "AOC + DOA = DOA + BOD",
        # "5. Cancelling out DOA from both sides gives us:",
        # "AOC = BOD",
        # "Similarly, we can prove:",
        # "DOA = COB"
        #  ]

        # proof_text = VGroup(*[Text(step,font_size=30) for step in proof_steps]).arrange(DOWN, aligned_edge=LEFT).scale(0.8).to_edge(UP)

        # self.play(Write(proof_text))

        # self.wait(6)

    def parallel(self):
        self.positionChoice=[[0,2,0],[-3,-2,0],[3,-2,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Parallel Lines", "")
        p11=cvo.CVO().CreateCVO("Theorem","Line parallel to the same line are parallel to each other").setangle(-TAU/4)
        p11.setcircleradius(2) 
        p12=cvo.CVO().CreateCVO("Conditions", "")
        p12.extendOname(["Corresponding angles are equal","Alternate Interior angles are equal","Interior angles on same side are supplementary","$Both lines \parallel to third line$","$Both lines \perp to third line$"])
        p12.setcircleradius(1.5)
        p10.cvolist.append(p11) 
        p10.cvolist.append(p12) 
        self.construct1(p10, p10)

    def ParallelLinesTheorem(self):
        # Title and description
        # Title and description
        title = Text("Parallel Lines Theorem").to_edge(UP)
        description = Text(
            "If two lines are parallel to the same line, they will be parallel to each other.",
            font_size=24
        ).next_to(title, DOWN)

        # Define the lines l, m, n (parallel lines) with reduced height
        line_l = Line([-4, 1, 0], [4, 1, 0], color=BLUE).set_stroke(width=2)
        line_m = Line([-4, 0, 0], [4, 0, 0], color=BLUE).set_stroke(width=2)
        line_n = Line([-4, -1, 0], [4, -1, 0], color=BLUE).set_stroke(width=2)

        # Define the transversal line t with double arrow
        transversal = DoubleArrow([-4.5, -2, 0], [4.5, 2, 0], color=RED).set_stroke(width=2)

        # Add names to the lines
        line_labels = [
            Tex("l").next_to(line_l, LEFT),
            Tex("m").next_to(line_m, LEFT),
            Tex("n").next_to(line_n, LEFT),
            Tex("t").next_to(transversal, UP + RIGHT)
        ]

        # Create lines and transversal
        self.play(Write(title))
        self.play(Write(description))
        self.wait(1)
        self.play(Create(line_l), Create(line_m), Create(line_n))
        self.play(Create(transversal))
        self.play(*[Write(label) for label in line_labels])

        # Explanation text
        explanation_text = Text(
            "From the figure, line m is parallel to l and n is parallel to l. Therefore, m is parallel to n.",
            font_size=25
        ).to_edge(DOWN)
        self.play(Write(explanation_text))
        self.wait(2)

        # Fade out
        self.play(FadeOut(title), FadeOut(description), FadeOut(line_l), FadeOut(line_m),
                  FadeOut(line_n), FadeOut(transversal),
                  FadeOut(*line_labels), FadeOut(explanation_text))

        self.wait(1)

    def Transversal(self):
        self.positionChoice=[[-4,-2,0],[0,-2,0],[-4,2,0],[-1,2,0],[4,2,0],[4,-2,0],[2,1,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Angles by Transversal","")
        p11=cvo.CVO().CreateCVO("Corresponding angles","")
        p12=cvo.CVO().CreateCVO("Interior angles","")
        p13=cvo.CVO().CreateCVO("Exterior angles","")
        p14=cvo.CVO().CreateCVO("Vertically Opposite angles","")
        p15=cvo.CVO().CreateCVO("Alternate angles","")
        p16=cvo.CVO().CreateCVO("Consecutive angles","")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        p10.cvolist.append(p16)
        self.construct1(p10,p10)

    def TransversalAnim(self):

        title = Text("Angles Made by a Transversal").to_edge(UP)
        self.play(Write(title))

        # Define the lines and transversal
        line_l = Line(LEFT * 3, RIGHT * 3, color=BLUE).shift(UP)
        line_m = Line(LEFT * 3, RIGHT * 3, color=BLUE).shift(DOWN)
        transversal = Line(LEFT * 2 + UP * 2, RIGHT * 2 + DOWN * 2, color=RED)

        # Create lines
        lines = VGroup(line_l, line_m, transversal).scale(0.8).to_edge(LEFT)
        self.play(Create(lines))

        # Define angles
        angles = [
            Angle(line_l, transversal, radius=0.5, quadrant=(1, 1), other_angle=False, color=YELLOW),
            Angle(line_l, transversal, radius=0.5, quadrant=(1, -1), other_angle=True, color=GREEN),
            Angle(line_m, transversal, radius=0.5, quadrant=(1, 1), other_angle=False, color=YELLOW),
            Angle(line_m, transversal, radius=0.5, quadrant=(1, -1), other_angle=True, color=GREEN),
            Angle(line_l, transversal, radius=0.5, quadrant=(-1, 1), other_angle=False, color=ORANGE),
            Angle(line_l, transversal, radius=0.5, quadrant=(-1, -1), other_angle=True, color=PINK),
            Angle(line_m, transversal, radius=0.5, quadrant=(-1, 1), other_angle=False, color=ORANGE),
            Angle(line_m, transversal, radius=0.5, quadrant=(-1, -1), other_angle=True, color=PINK)
        ]

        # Label angles
        labels = [
            MathTex(r"\angle 1").next_to(angles[0].point_from_proportion(0.5), UR, buff=0.2),
            MathTex(r"\angle 2").next_to(angles[1].point_from_proportion(0.5), UP*4+ LEFT*2, buff=0.2),
            MathTex(r"\angle 3").next_to(angles[2].point_from_proportion(0.5), UR, buff=0.2),
            MathTex(r"\angle 4").next_to(angles[3].point_from_proportion(0.5), UP*4 + LEFT*2, buff=0.2),
            MathTex(r"\angle 5").next_to(angles[4].point_from_proportion(0.5), RIGHT*3, buff=0.2),
            MathTex(r"\angle 6").next_to(angles[5].point_from_proportion(0.5), DOWN*2, buff=0.2),
            MathTex(r"\angle 7").next_to(angles[6].point_from_proportion(0.5), RIGHT*3, buff=0.2),
            MathTex(r"\angle 8").next_to(angles[7].point_from_proportion(0.5), DOWN*2, buff=0.2)
        ]

        # Group angles and labels
        all_angles = VGroup(*angles, *labels)

        # Animate angles and labels
        self.play(Create(VGroup(*angles)))
        self.play(Write(VGroup(*labels)))

        # Explanation
        explanation_text = VGroup(
            MathTex(r"\text{Angles formed by a transversal are categorized as:}"),
            MathTex(r"\text{1. Corresponding Angles: } \angle 1 = \angle 3 \text{ and } \angle 5 = \angle 7"),
            MathTex(r"\text{2. Interior Angles: } \angle 3, \angle 4, \angle 5, \angle 6"),
            MathTex(r"\text{3. Exterior Angles: } \angle 1, \angle 2, \angle 7, \angle 8"),
            MathTex(r"\text{4. Vertically Opposite Angles: } \angle 1 = \angle 3 \text{ and } \angle 2 = \angle 4"),
            MathTex(r"\text{5. Alternate Interior Angles: } \angle 5 = \angle 4 \text{ and } \angle 3 = \angle 6"), 
            MathTex(r"\text{6. Alternate Exterior Angles: } \angle 1, \angle 8 \text{ and } \angle 2, \angle 7"),
            MathTex(r"\text{7. Consecutive Interior Angles: } \angle 5, \angle 3 \text{ and } \angle 6, \angle 4"),
            MathTex(r"\text{8. Consecutive Exterior Angles: } \angle 1, \angle 7 \text{ and } \angle 2, \angle 8")

        ).arrange(DOWN, aligned_edge=LEFT).scale(0.8).to_edge(RIGHT)

        self.play(Write(explanation_text))

        self.wait(10)

        # Clear the scene
        self.clear_scene()

    def clear_scene(self):
        self.play(*[FadeOut(mob) for mob in self.mobjects])
    
    def Triangle(self):
        self.positionChoice=[[-3,-2,0],[3,-2,0],[-2,2,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Triangle", "")
        p11=cvo.CVO().CreateCVO("Angle Sum Property",r"$Sum of angles=180^\circ$")
        p12=cvo.CVO().CreateCVO("Theorem","Extended triangle side equals sum of 2 opposite interior angles.")
        p11.setcircleradius(2) 
        p10.cvolist.append(p11) 
        p10.cvolist.append(p12) 
        self.construct1(p10, p10)


    def Triangle1(self):
        title = Text("Triangle").to_edge(UP)
        A = np.array([-2, -1, 0])
        B = np.array([2, -1, 0])
        C = np.array([0, 2, 0])
        triangle = Polygon(A, B, C, color=BLUE)

        # Labels for vertices
        label_A = MathTex("A").next_to(A, DOWN)
        label_B = MathTex("B").next_to(B, DOWN)
        label_C = MathTex("C").next_to(C, UP)

        # Create arcs to represent angles
        # Properly calculate start and end angles for the arcs
        arc_A = Arc(radius=0.5, start_angle=np.arctan2(B[1] - A[1], B[0] - A[0]), angle=np.arctan2(C[1] - A[1], C[0] - A[0]) - np.arctan2(B[1] - A[1], B[0] - A[0]), color=RED)
        arc_A.move_arc_center_to(A)

        arc_B = Arc(radius=0.5, start_angle=np.arctan2(C[1] - B[1], C[0] - B[0]), angle=np.arctan2(A[1] - B[1], A[0] - B[0]) - np.arctan2(C[1] - B[1], C[0] - B[0]), color=RED)
        arc_B.move_arc_center_to(B)

        arc_C = Arc(radius=0.5, start_angle=np.arctan2(A[1] - C[1], A[0] - C[0]), angle=np.arctan2(B[1] - C[1], B[0] - C[0]) - np.arctan2(A[1] - C[1], A[0] - C[0]), color=RED)
        arc_C.move_arc_center_to(C)

        # Angle labels
        angle_A_label = MathTex(r"\alpha").move_to(A + 0.7 * np.array([1, 0.5, 0]))
        angle_B_label = MathTex(r"\beta").move_to(B + 0.7 * np.array([-1, 0.5, 0]))
        angle_C_label = MathTex(r"\gamma").move_to(C + 0.7 * np.array([0, -0.5, 0]))

        # Angle sum text
        angle_sum = MathTex(r"\sum \text{ angles} = 180^\circ").move_to(4*RIGHT + UP)
        angle_sum_text = MathTex(r"\alpha + \beta + \gamma = 180^\circ").next_to(angle_sum,DOWN)

        self.play(Write(title))
        self.wait(0.5)
        self.play(Create(triangle))
        self.play(Write(label_A), Write(label_B), Write(label_C))
        self.play(Create(arc_A), Write(angle_A_label))
        self.play(Create(arc_B), Write(angle_B_label))
        self.play(Create(arc_C), Write(angle_C_label))
        self.wait(0.5)
        self.play(Write(angle_sum))
        self.play(Write(angle_sum_text))
        self.wait(1)

        self.play(FadeOut(title),FadeOut(triangle), FadeOut(label_A), FadeOut(label_B), FadeOut(label_C),
                         FadeOut(arc_A), FadeOut(arc_B), FadeOut(arc_C), FadeOut(angle_A_label), FadeOut(angle_B_label), FadeOut(angle_C_label),
                         FadeOut(angle_sum),FadeOut(angle_sum_text))
        self.wait(1)



 

if __name__ == "__main__":
    scene = LineAngle()
    scene.render()