from manim import *
from AbstractAnim import AbstractAnim
import cvo

class LinesAndAngles(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Lines()
        self.fadeOutCurrentScene()
        self.parallelanim()
        self.fadeOutCurrentScene()
        self.Intersectanim()
        self.fadeOutCurrentScene()
        self.Angle()
        self.fadeOutCurrentScene()
        self.Complementary()
        self.fadeOutCurrentScene()
        self.ComplementaryAnim()
        self.fadeOutCurrentScene()
        self.Supplementary()
        self.fadeOutCurrentScene()
        self.SupplementaryAnim()
        self.fadeOutCurrentScene()
        self.Adjacent()
        self.fadeOutCurrentScene()
        self.AdjacentAnim()
        self.fadeOutCurrentScene()
        self.Linear()
        self.fadeOutCurrentScene()
        self.Vertopp()
        self.fadeOutCurrentScene()
        self.Transversal()
        self.fadeOutCurrentScene()
        self.Corresponding()
        self.fadeOutCurrentScene()
        self.Interior()
        self.fadeOutCurrentScene()
        self.Exterior()
        self.fadeOutCurrentScene()
        self.VertOpp()
        self.fadeOutCurrentScene()
        self.AltInt()
        self.fadeOutCurrentScene()
        self.AltExt()
        self.fadeOutCurrentScene()
        self.ConsecIntExt()
        self.fadeOutCurrentScene()
        self.TransversalAnim()
        self.fadeOutCurrentScene()
        self.TransversalIntersectsParallelLinesProperties()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()


    def Lines(self):
        self.positionChoice=[[0,2,0],[-3,-2,0],[3,-2,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Lines","")
        p11=cvo.CVO().CreateCVO("Parallel lines","do not intersect at any point")
        p12=cvo.CVO().CreateCVO("Intersecting lines","lines meet at a point")
        p10.setcircleradius(1.75)
        p11.setcircleradius(1.75)
        p12.setcircleradius(1.75)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
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
       


    def Angle(self):
        self.positionChoice=[[-5,-2,0],[-1,-2,0],[-4,2,0],[-1,2,0],[3,2,0],[3,-2,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Angles","")
        p11=cvo.CVO().CreateCVO("Acute",r"$Angle<90^\circ$")
        p11.setcircleradius(1)
        p12=cvo.CVO().CreateCVO("Right",r"$Angle=90^\circ$")
        p12.setcircleradius(1)
        p13=cvo.CVO().CreateCVO("Obtuse",r"$90^\circ<Angle<180^\circ$")
        p13.setcircleradius(1)
        p14=cvo.CVO().CreateCVO("Straight",r"$Angle=180^\circ$")
        p14.setcircleradius(1)
        p15=cvo.CVO().CreateCVO("Reflex",r"$Angle>180^\circ$")
        p15.setcircleradius(1)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        self.construct1(p10,p10)

    

    def Complementary(self):
        self.positionChoice=[[3,-2,0],[0,2,0],[-3,-2,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Complementary Angle","")
        p11=cvo.CVO().CreateCVO("Property",r"$Adjacent \quad angles \quad summing \quad to \quad 90^\circ$")
        p12=cvo.CVO().CreateCVO("Example",r"$50^\circ,40^\circ$")
        p11.setcircleradius(2)
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        self.construct1(p10,p10)

    def ComplementaryAnim(self):
        # Title
        title = Text("Complementary Angles").to_edge(UP)
        self.play(Write(title))

        # Create a right angle with a complementary split
        line1 = Line(ORIGIN, RIGHT * 3, color=BLUE)
        line2 = Line(ORIGIN, UP * 3, color=BLUE)
        line3 = Line(ORIGIN, RIGHT * 2 + UP * 2, color=RED)  # Complementary angle line

        # Create arcs for the complementary angles
        arc_30 = Arc(radius=0.7, start_angle=0, angle=PI / 6, color=GREEN).move_arc_center_to(ORIGIN)
        arc_60 = Arc(radius=0.7, start_angle=PI / 6, angle=PI / 3, color=GREEN).move_arc_center_to(ORIGIN)

        # Labels for the angles
        label_30 = MathTex(r"30^\circ").next_to(arc_30, DR, buff=0.1)
        label_60 = MathTex(r"60^\circ").next_to(arc_60, UL, buff=0.1)
        label_90 = MathTex(r"90^\circ").next_to(line2.get_end(), UR)

        # Group right angle elements
        right_angle = VGroup(line1, line2, line3, arc_30, arc_60, label_30, label_60, label_90)

        # Position the right angle diagram on the left half of the screen
        right_angle.move_to(LEFT * 4.5)

        # Play animations for the right angle diagram
        self.play(Create(line1), Create(line2))
        self.play(Create(line3))
        self.play(Create(arc_30), Create(arc_60))
        self.play(Write(label_30), Write(label_60), Write(label_90))

        # Explanation of complementary angles
        explanation = [
            r"\text{If the sum of two angles is } 90^\circ, \text{ they are called complementary angles.}",
            r"\text{These angles are complementary, as} 30^\circ + 60^\circ = 90^\circ.",
            r"\text{We can also say that the complement of } 30^\circ \text{ is } 60^\circ \text{ and}",
            r"\text{the complement of } 60^\circ \text{ is } 30^\circ."
        ]

        # Create the explanation text
        explanation_text = VGroup(
            *[MathTex(text, font_size=40) for text in explanation]
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.8).to_edge(RIGHT*1.5)

        # Display the explanation text on the right side of the screen
        self.play(Write(explanation_text))

        # Highlight the complementary relationship
        box_30 = SurroundingRectangle(label_30, color=YELLOW, buff=0.1)
        box_60 = SurroundingRectangle(label_60, color=GREEN, buff=0.1)
        self.play(Create(box_30), Create(box_60))

        self.wait(4)



    def Supplementary(self):
        self.positionChoice=[[3,-2,0],[0,2,0],[-3,-2,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Supplementary Angle","")
        p11=cvo.CVO().CreateCVO("Property",r"$Adjacent \quad angles \quad summing \quad to \quad 180^\circ$")
        p12=cvo.CVO().CreateCVO("Example",r"$80^\circ,100^\circ$")
        p11.setcircleradius(2)
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        self.construct1(p10,p10)

    def SupplementaryAnim(self):
        # Title
        title = Text("Supplementary Angles").to_edge(UP)
        self.play(Write(title))

        # Create a straight line to represent 180 degrees
        line = Line(start=LEFT*4, end=RIGHT*4, color=BLUE)

        # Create the yellow line (separating arm)
        separating_arm = Line(
            start=line.get_center(),
            end=line.get_center() + 3 * UP + 2.5 * LEFT,  # Adjusted endpoint to decrease size
            color=YELLOW
        )

        # Create arcs for the supplementary angles
        arc_120 = Arc(radius=1, start_angle=0 * DEGREES, angle=120 * DEGREES, color=GREEN)
        arc_60 = Arc(radius=1, start_angle=120 * DEGREES, angle=60 * DEGREES, color=GREEN)

        # Labels for the angles
        label_120 = MathTex(r"120^\circ").next_to(arc_120, UR, buff=0.2)
        label_60 = MathTex(r"60^\circ").next_to(arc_60, UL + LEFT, buff=0.2)
        label_180 = MathTex(r"180^\circ").next_to(line, DOWN, buff=0.2)

        # Group supplementary angle elements
        supplementary_angles = VGroup(line, separating_arm, arc_120, arc_60, label_120, label_60, label_180)

        # Position the diagram on the left half of the screen
        supplementary_angles.shift(LEFT * 2)

        # Play animations for the diagram
        self.play(Create(line))
        self.play(Create(separating_arm))
        self.play(Create(arc_120), Create(arc_60))
        self.play(Write(label_120), Write(label_60), Write(label_180))

        # Explanation of supplementary angles
        explanation = [
            r"\text{If the sum of two angles is} 180^\circ, \text{they are called supplementary angles.}",
            r"\text{These are a pair of supplementary angles, as} 120^\circ + 60^\circ = 180^\circ.",
            r"\text{We say that the supplement of} 120^\circ \text{ is } 60^\circ \text{ and}",
            r"\text{the supplement of} 60^\circ \text{ is } 120^\circ."
        ]

        # Create the explanation text
        explanation_text = VGroup(
            *[MathTex(text, font_size=40) for text in explanation]
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.8).to_edge(DOWN)

        # Display the explanation text on the right side of the screen
        self.play(Write(explanation_text))

        # Highlight the supplementary relationship
        box_120 = SurroundingRectangle(label_120, color=YELLOW, buff=0.1)
        box_60 = SurroundingRectangle(label_60, color=GREEN, buff=0.1)
        self.play(Create(box_120), Create(box_60))

        self.wait(4)

        # Clear the scene
        self.clear_scene()

    def clear_scene(self):
        self.play(*[FadeOut(mob) for mob in self.mobjects])
# To render the scene, use the following command in your terminal:
# manim -pql supplementary_angles.py SupplementaryAngles

# To render the scene


    def Adjacent (self):
        self.setNumberOfCirclePositions(2)
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Adjacent Angle","")
        p11=cvo.CVO().CreateCVO("Property","Angles having a common arm \& vertex")
        p11.setcircleradius(2)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def AdjacentAnim(self):
        title = Text("Adjacent Angles").to_edge(UP)
        self.play(Write(title))

        # Define points for the angles
        O = ORIGIN
        A = UP * 2
        B = 3 * RIGHT
        C = 3 * RIGHT + UP

        # Define the lines/segments for the angles
        line_OA = Line(O, A, color=BLUE)
        line_OB = Line(O, B, color=BLUE)
        line_OC = Line(O, C, color=BLUE)

        # Create angles
        arc_AOC = Angle(line_OC, line_OA, radius=0.6, other_angle=False, color=YELLOW)
        arc_BOC = Angle(line_OB, line_OC, radius=0.6, other_angle=False, color=GREEN)

        # Create labels for points
        label_A = MathTex("A").next_to(A, LEFT, buff=0.1)
        label_B = MathTex("B").next_to(B, DOWN, buff=0.1)
        label_C = MathTex("C").next_to(C, RIGHT, buff=0.1)
        label_O = MathTex("O").next_to(O, DOWN, buff=0.1)

        # Create angle labels and position them between the lines
        angle_AOC_label = MathTex(r"\angle AOC").next_to(label_A, RIGHT, buff=0.2)
        angle_BOC_label = MathTex(r"\angle BOC").next_to(label_C, DOWN, buff=0.2)

        # Position the diagram on the left side
        diagram = VGroup(line_OA, line_OB, line_OC, arc_AOC, arc_BOC, label_A, label_B, label_C, label_O, angle_AOC_label, angle_BOC_label)
        diagram.shift(LEFT * 2.5)  # Shift the diagram to the left

        # Play animations to create the diagram
        self.play(Create(line_OA), Create(line_OB), Create(line_OC))
        self.play(Create(arc_AOC), Create(arc_BOC))
        self.play(Write(label_A), Write(label_B), Write(label_C), Write(label_O))
        self.play(Write(angle_AOC_label), Write(angle_BOC_label))
        
        # Explanation of adjacent angles
        explanation_text = VGroup(
            MathTex(r"\text{The angles } \angle AOC \text{ and } \angle BOC \text{ are adjacent angles.}"),
            MathTex(r"\text{They share a common vertex } O \text{ and a common arm } OB.")
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.8).to_edge(DOWN * 2)  # Position text to the right

        self.play(Write(explanation_text))

        self.wait(4)

        # Clear the scene
        self.clear_scene()

    def clear_scene(self):
        self.play(*[FadeOut(mob) for mob in self.mobjects])

    def Linear(self):
        self.setNumberOfCirclePositions(2)
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Linear Pair", "")
        p11=cvo.CVO().CreateCVO("Property","Adjacent angles forming a straight line")
        p11.setcircleradius(2)
        p10.cvolist.append(p11) 
        self.construct1(p10, p10)  

    def Vertopp(self):
        title=Text("Vertically opposite angles").to_edge(UP)
        self.play(Write(title))
        line1 = Line(LEFT*1.5, RIGHT*1.5)
        line2 = Line(UP*1.5, DOWN*1.5)
        intersection = Dot(ORIGIN)
        
        # Labels for points
        A = Text("A").next_to(line1.get_start(), LEFT)
        B = Text("B").next_to(line1.get_end(), RIGHT)
        C = Text("C").next_to(line2.get_start(), UP)
        D = Text("D").next_to(line2.get_end(), DOWN)
        O = Text("O").next_to(intersection, DOWN)

        # Drawing the angle arcs
        angle_arc1 = Arc(radius=0.5, angle=90 * DEGREES, start_angle=0, color=YELLOW).shift(0.25*RIGHT + 0.25*UP)
        angle_arc2 = Arc(radius=0.5, angle=90 * DEGREES, start_angle=90 * DEGREES, color=GREEN).shift(0.25*LEFT + 0.25*UP)
        angle_arc3 = Arc(radius=0.5, angle=90 * DEGREES, start_angle=180 * DEGREES, color=YELLOW).shift(0.25*LEFT + 0.25*DOWN)
        angle_arc4 = Arc(radius=0.5, angle=90 * DEGREES, start_angle=270 * DEGREES, color=GREEN).shift(0.25*RIGHT + 0.25*DOWN)
        
        # Labels for angles
        angle1 = MathTex("\\angle 1").next_to(angle_arc1, UP + RIGHT)
        angle2 = MathTex("\\angle 2").next_to(angle_arc2, UP + LEFT)
        angle3 = MathTex("\\angle 3").next_to(angle_arc3, DOWN + LEFT)
        angle4 = MathTex("\\angle 4").next_to(angle_arc4, DOWN + RIGHT)
        
        self.play(Create(line1), Create(line2), FadeIn(intersection))
        self.play(Write(A), Write(B), Write(C), Write(D), Write(O))
        self.play(Create(angle_arc1), Create(angle_arc2), Create(angle_arc3), Create(angle_arc4))
        self.play(Write(angle1), Write(angle2), Write(angle3), Write(angle4))

        info=MathTex("\\angle 1=\\angle 3").next_to(B,RIGHT*2).set_color_by_tex("1",YELLOW).set_color_by_tex("3",YELLOW)
        info1=MathTex("\\angle 2=\\angle 4").next_to(info,DOWN).set_color_by_tex("2",GREEN).set_color_by_tex("2",GREEN)
        self.play(Write(info))
        self.wait(1)
        self.play(Write(info1))
        self.wait(1)
        # Conclusion text
        conclusion = Text("Therefore, Vertically opposite angles are equal.",font_size=35).to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(2)



    def Transversal(self):
        self.isRandom = False
        self.positionChoice = [[-1,2,0],[-4,-2,0],[3,0,0]]
        p10=cvo.CVO().CreateCVO("Transversal","").setangle(-TAU/4)
        p11=cvo.CVO().CreateCVO("Property","line intersecting 2 or more lines")
        p11.setcircleradius(1)
        p12=cvo.CVO().CreateCVO("Angles on Transversal", "")
        p12.extendOname(["Corresponding","Interior","Exterior","Vertically Opposite","Consecutive Interior","Alternate Interior","Consecutive Exterior","Alternate Exterior"])
        p12.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)

    def Corresponding(self):
        self.setNumberOfCirclePositions(3)
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Corresponding Angle","")
        p11=cvo.CVO().CreateCVO("Property","Angles on same side of transversal")
        p12=cvo.CVO().CreateCVO("Condition","one being Interior\&other is Exterior angle")
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        self.construct1(p10,p10)

    def Interior(self):
        self.setNumberOfCirclePositions(2)
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Interior Angle","")
        p11=cvo.CVO().CreateCVO("Property","within the shape")
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def Exterior(self):
        self.setNumberOfCirclePositions(2)
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Exterior Angle","")
        p11=cvo.CVO().CreateCVO("Property","outside the shape")
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def VertOpp(self):
        self.setNumberOfCirclePositions(3)
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Vertically Opposite Angle","")
        p11=cvo.CVO().CreateCVO("Property","opposite eachother at intersection point")
        p12=cvo.CVO().CreateCVO("Property","These angles are Equal")
        p11.setcircleradius(2)
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        self.construct1(p10,p10)

    def AltInt(self):
        self.positionChoice=[[-4,-2,0],[1,-2,0],[-4,2,0],[-1,2,0],[3,2,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Alternate Interior \& Exterior Angle","")
        p11=cvo.CVO().CreateCVO("Property","have different vertices")
        p12=cvo.CVO().CreateCVO("Property","on either side of transversal")
        p13=cvo.CVO().CreateCVO("Property","lie b/w the 2 lines is interior")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.construct1(p10,p10)

    def AltExt(self):
        self.positionChoice=[[-4,-2,0],[1,-2,0],[-4,2,0],[-1,2,0],[3,2,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Alternate Interior \& Exterior Angle","")
        p11=cvo.CVO().CreateCVO("Property","have different vertices")
        p12=cvo.CVO().CreateCVO("Property","on either side of transversal")
        p13=cvo.CVO().CreateCVO("Property","lie outside the 2 lines is exterior")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.construct1(p10,p10)


    def ConsecIntExt(self):
        self.setNumberOfCirclePositions(2)
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Consecutive Interior \& Exterior Angle","")
        p11=cvo.CVO().CreateCVO("Property","Angles on same side of transversal")
        p10.cvolist.append(p11)
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


    def TransversalIntersectsParallelLinesProperties(self):
        # Step-by-step text representations
        title=Text("Properties of Parallel Lines").to_edge(UP)
        step1 = Text("When a transversal intersects a pair of parallel lines:", font_size=34).next_to(title,DOWN)
        step2 = Text("(i) Each pair of corresponding angles are equal.", font_size=30).next_to(step1, DOWN, aligned_edge=LEFT)
        step3 = Text("(ii) Each pair of alternate interior angles are equal.", font_size=30).next_to(step2, DOWN, aligned_edge=LEFT)
        step4 = Text("(iii) Each pair of alternate exterior angles are equal.", font_size=30).next_to(step3, DOWN, aligned_edge=LEFT)
        step5 = Text("(iv) Each pair of interior angles on the same side of the transversal are \n supplementary.", font_size=30).next_to(step4, DOWN, aligned_edge=LEFT)
        
        # Animating the steps
        self.play(Write(title))
        self.play(Write(step1))
        self.wait(1)
        self.play(Write(step2))
        self.wait(1)
        self.play(Write(step3))
        self.wait(1)
        self.play(Write(step4))
        self.wait(1)
        self.play(Write(step5))
        self.wait(2)

    def SetDeveloperList(self):  
        self.DeveloperList="Gayathri Veeramreddy"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade7Chapter4LinesAndAngles.py"

if __name__ == "__main__":
    scene = LinesAndAngles()
    scene.render()
