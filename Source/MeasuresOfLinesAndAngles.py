from manim import *
from AbstractAnim import AbstractAnim
import cvo

class MeasuresOfLinesAndAngles(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Lines()
        self.fadeOutCurrentScene()
        self.Line()
        self.fadeOutCurrentScene()
        self.display_point()
        self.display_line_segment()
        self.display_ray()
        self.display_line()
        self.fadeOutCurrentScene()
        self.collinear()
        self.collinear1()
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
        p11=cvo.CVO().CreateCVO("Property",r"$Adjacent \quad angles \quad sum \quad is \quad 90^\circ$")
        p12=cvo.CVO().CreateCVO("Example",r"$60^\circ,30^\circ$")
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
            r"\text{These angles are complementary, as } 30^\circ + 60^\circ = 90^\circ.",
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
        p11=cvo.CVO().CreateCVO("Property",r"$Adjacent \quad angles \quad sum \quad is \quad 180^\circ$")
        p12=cvo.CVO().CreateCVO("Example",r"$70^\circ,110^\circ$")
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
            r"\text{These are a pair of supplementary angles, as } 120^\circ + 60^\circ = 180^\circ.",
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
 
        



    def SetDeveloperList(self):  
        self.DeveloperList="Snehith Chowdary"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="MeasuresOfLinesAndAngles.py"


if __name__ == "__main__":
    scene = MeasuresOfLinesAndAngles()
    scene.render()