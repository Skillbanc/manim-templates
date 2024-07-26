from manim import *
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class Chapter13Anim(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.BasicConstructions()
        self.fadeOutCurrentScene()
        self.PerpenBisector()
        self.fadeOutCurrentScene()
        self.PerpendicularBisector()
        self.fadeOutCurrentScene()
        self.BisectorAngle()
        self.fadeOutCurrentScene()
        self.AngleBisector()
        self.fadeOutCurrentScene()
        self.Create60DegreeAngle()
        self.fadeOutCurrentScene()
        self.BBAS2()
        self.fadeOutCurrentScene()
        self.ConstructTriangle()
        self.fadeOutCurrentScene()
        self.BBAD2()
        self.fadeOutCurrentScene()
        self.ConstructTriangle2()
        self.fadeOutCurrentScene()
        self.ChordTriangle()
        self.fadeOutCurrentScene()
        self.ConstructTriangle3()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
    

    def SetDeveloperList(self):  
        self.DeveloperList = "Mukthanand Reddy"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName = "Grade9Chapter13Chapter13Anim.py"


    def PerpendicularBisector(self):
        title = Text("Perpendicular Bisector for a given line segment", font_size=35).shift(UP*3 + LEFT)
        self.play(Write(title))
        self.wait(1.5)
        
        # Define a smaller line segment and radius
        line_length = 3
        radius = line_length / 1.5
        shift_amount = LEFT * 0.5

        # Step 1: Draw line segment AB
        step_1 = Text("Step 1: Draw a line segment AB with any length.", font_size=24, color=BLUE).to_edge(LEFT).shift(UP*2 + shift_amount + RIGHT*0.5)
        point_a = Dot(LEFT * (line_length / 2) + RIGHT * 4, color=BLUE).shift(shift_amount)
        point_b = Dot(RIGHT * (line_length / 2) + RIGHT * 4, color=BLUE).shift(shift_amount)
        label_a = Text("A", color=BLUE).next_to(point_a, DOWN)
        label_b = Text("B", color=BLUE).next_to(point_b, DOWN)
        line_ab = Line(point_a.get_center(), point_b.get_center(), color=WHITE)
        
        self.play(Write(step_1))
        self.wait(1)
        self.play(FadeIn(point_a, point_b), Write(label_a), Write(label_b))
        self.wait(1.5)
        self.play(Create(line_ab))
        self.wait(1.5)

        # Step 2: Draw two circles with radius slightly more than half the length of AB, centered at points A and B.
        step_2 = Text("Step 2: Draw two circles with radius slightly\n""           more than half the length of AB,\n""           centered at points A and B.", font_size=24, color=RED).to_edge(LEFT).shift(UP*1 + shift_amount + RIGHT*0.5)
        self.play(Write(step_2))
        self.wait(1)
        circle_a = Circle(radius=radius, color=RED).move_to(point_a.get_center())
        circle_b = Circle(radius=radius, color=RED).move_to(point_b.get_center())
        
        self.play(Create(circle_a))
        self.wait(1)
        self.play(Create(circle_b))
        self.wait(1.5)

        # Step 3: Mark the intersections of the circles
        step_3 = Text("Step 3: Find the Intersection Points\n""           of the circles", font_size=24, color=YELLOW).to_edge(LEFT).shift(DOWN*0.1 +shift_amount + RIGHT*0.5)
        self.play(Write(step_3))
        self.wait(1.5)
        
        midpoint = line_ab.get_center()

        # Correctly calculate intersection points
        dx = point_b.get_center()[0] - point_a.get_center()[0]
        dy = point_b.get_center()[1] - point_a.get_center()[1]
        d = (dx**2 + dy**2)**0.5
        a = d / 2
        h = (radius**2 - a**2)**0.5
        xm = point_a.get_center()[0] + a * (dx) / d
        ym = point_a.get_center()[1] + a * (dy) / d
        xs1 = xm + h * (-dy) / d
        ys1 = ym + h * (dx) / d
        xs2 = xm - h * (-dy) / d
        ys2 = ym - h * (dx) / d

        intersection_1 = [xs1, ys1, 0]
        intersection_2 = [xs2, ys2, 0]
        point_p = Dot(intersection_1, color=YELLOW)
        point_q = Dot(intersection_2, color=YELLOW)
        
        self.play(FadeIn(point_p, point_q))
        self.wait(1.5)

        # Step 4: Draw the perpendicular bisector
        step_4 = Text("Step 4: Connect the intersection points", font_size=24, color=GREEN).to_edge(LEFT).shift(DOWN*1.2 + shift_amount + RIGHT*0.5)
        self.play(Write(step_4))
        self.wait(1)
        perp_bisector = Line(point_p.get_center(), point_q.get_center(), color=GREEN)
        
        self.play(Create(perp_bisector))
        self.wait(1.5)

        # Step 5: Label the intersection points
        step_5 = Text("Step 5: Label the intersection points as P & Q ", font_size=24, color=ORANGE).to_edge(LEFT).shift(DOWN*2 + shift_amount + RIGHT*0.5)
        self.play(Write(step_5))
        label_p = Text("P", color=ORANGE).next_to(point_p, UP)
        label_q = Text("Q", color=ORANGE).next_to(point_q, DOWN)
        
        self.play(Write(label_p))
        self.wait(1)
        self.play(Write(label_q))
        self.wait(1)
        step_6 = Text("Step 6 : The line segment PQ is the perpendicular bisector\n""            of the segment AB.", font_size=24, color=ORANGE).to_edge(LEFT).shift(DOWN*3 + shift_amount + RIGHT*0.5)
        self.play(Write(step_6))
        self.wait(3)


    def AngleBisectorWithSteps(self):
        title = Text("To Construct the Bisector of a Given Angle", font_size=35).shift(UP*3+LEFT)
        self.play(Write(title))
        self.wait(1.5)

        # Define shift amount
        shift_amount = LEFT * 0.5

        # Step 1: Draw the given angle ABC
        step_1 = Text("Step 1: Draw the given angle ABC.", font_size=24, color=BLUE).to_edge(LEFT).shift(UP*2 + shift_amount)
        self.play(Write(step_1))
        self.wait(1)
        
        point_a = Dot(ORIGIN, color=BLUE)
        point_b = Dot(RIGHT * 2, color=BLUE)
        point_c = Dot(UP * 2, color=BLUE)
        label_a = Text("A", color=BLUE).next_to(point_a, DOWN)
        label_b = Text("B", color=BLUE).next_to(point_b, RIGHT)
        label_c = Text("C", color=BLUE).next_to(point_c, UP)
        line_ab = Line(point_a.get_center(), point_b.get_center(), color=WHITE)
        line_bc = Line(point_b.get_center(), point_c.get_center(), color=WHITE)
        
        self.play(FadeIn(point_a, point_b, point_c), Write(label_a), Write(label_b), Write(label_c))
        self.play(Create(line_ab), Create(line_bc))
        self.wait(1.5)

        # Step 2: Draw an arc from B intersecting BA and BC
        step_2 = Text("Step 2: Draw an arc from B intersecting BA and BC.", font_size=24, color=RED).to_edge(LEFT).shift(UP*1 + shift_amount)
        self.play(Write(step_2))
        self.wait(1)
        
        arc_radius = 2
        arc = Arc(radius=arc_radius, start_angle=PI, angle=0, color=RED).shift(UP*0.5 + RIGHT*1)
        point_d = Dot(arc.get_center() + LEFT*0.5, color=RED)
        point_e = Dot(arc.get_center() + RIGHT*0.5, color=RED)
        label_d = Text("D", color=RED).next_to(point_d, DOWN)
        label_e = Text("E", color=RED).next_to(point_e, UP)
        
        self.play(Create(arc))
        self.play(FadeIn(point_d, point_e), Write(label_d), Write(label_e))
        self.wait(1.5)

        # Step 3: Draw arcs from D and E with equal radii to intersect at F
        step_3 = Text("Step 3: Draw arcs from D and E with equal radii to intersect at F.", font_size=24, color=YELLOW).to_edge(LEFT).shift(shift_amount)
        self.play(Write(step_3))
        self.wait(1.5)
        
        arc_radius_de = 1.5
        arc_from_d = Arc(radius=arc_radius_de, start_angle=0, angle=PI, color=YELLOW).move_to(point_d.get_center())
        arc_from_e = Arc(radius=arc_radius_de, start_angle=PI, angle=2*PI, color=YELLOW).move_to(point_e.get_center())

        # Find the intersection of the two arcs
        center_a, radius_a = arc_from_d.get_center(), arc_from_d.radius
        center_b, radius_b = arc_from_e.get_center(), arc_from_e.radius

        d = np.linalg.norm(center_a - center_b)
        if d > radius_a + radius_b:
            intersection_f = ORIGIN  # Placeholder for no intersection
        else:
            x2 = (center_a[0] + center_b[0]) / 2
            y2 = (center_a[1] + center_b[1]) / 2
            intersection_f = [x2, y2, 0]

        point_f = Dot(intersection_f, color=YELLOW)
        label_f = Text("F", color=YELLOW).next_to(point_f, RIGHT)

        self.play(Create(arc_from_d))
        self.play(Create(arc_from_e))
        self.play(FadeIn(point_f), Write(label_f))
        self.wait(1.5)

        # Step 4: Draw the ray BF (the bisector)
        step_4 = Text("Step 4: Draw the ray BF. It is the required bisector of ∠ABC.", font_size=24, color=GREEN).to_edge(LEFT).shift(DOWN + shift_amount)
        self.play(Write(step_4))
        self.wait(1)
        
        ray_bf = Line(point_b.get_center(), point_f.get_center(), color=GREEN)
        
        self.play(Create(ray_bf))
        self.wait(1.5)
    
    def AngleBisector(self):
        title = Text("Perpendicular Bisector of a Given Angle", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))
        # Define points and labels
        point_a = Dot(RIGHT * 2.5 + DOWN * 1.5, color=BLUE)
        point_b = Dot(LEFT * 3 + DOWN * 1.5, color=BLUE)
        point_c = Dot(UP * 2, color=BLUE)
        label_a = Text("A", color=BLUE).next_to(point_a, DOWN)
        label_b = Text("B", color=BLUE).next_to(point_b, LEFT)
        label_c = Text("C", color=BLUE).next_to(point_c, DOWN)
        
        # Define lines
        line_ab = Line(point_a.get_center(), point_b.get_center(), color=WHITE)
        line_bc = Line(point_b.get_center(), point_c.get_center(), color=WHITE)
        
        # Define the arc
        radius = 1.5
        start_angle = PI / 2
        angle = -PI / 1.5
        arc = Arc(radius=radius, start_angle=start_angle, angle=angle, arc_center=point_b.get_center(), color=YELLOW)
        
        # Calculate intersection points
        def arc_line_intersection(line, arc_center, radius):
            line_start, line_end = line.get_start(), line.get_end()
            A = line_end - line_start
            B = line_start - arc_center
            a = np.dot(A, A)
            b = 2 * np.dot(A, B)
            c = np.dot(B, B) - radius**2
            discriminant = b**2 - 4*a*c
            
            if discriminant < 0:
                return None
            
            sqrt_disc = np.sqrt(discriminant)
            t1 = (-b + sqrt_disc) / (2*a)
            t2 = (-b - sqrt_disc) / (2*a)
            
            intersections = []
            if 0 <= t1 <= 1:
                intersections.append(line_start + t1 * A)
            if 0 <= t2 <= 1:
                intersections.append(line_start + t2 * A)
            
            return intersections

        intersections_ab = arc_line_intersection(line_ab, point_b.get_center(), radius)
        intersections_bc = arc_line_intersection(line_bc, point_b.get_center(), radius)
        
        # Create dots at intersection points
        dot_d = Dot(intersections_ab[0], color=RED) if intersections_ab else None
        dot_e = Dot(intersections_bc[0], color=RED) if intersections_bc else None
        
        # Create labels for the intersection points
        label_d = Text("D", color=RED).next_to(dot_d, DOWN+RIGHT*0.3) if dot_d else None
        label_e = Text("E", color=RED).next_to(dot_e, UP) if dot_e else None
        
        # Define arcs centered at D and E
        radius_arc = 1.5
        arc_d = Arc(radius=radius_arc, start_angle=-PI/3, angle=PI/1.5, arc_center=intersections_ab[0], color=GREEN, stroke_width=2)
        arc_e = Arc(radius=radius_arc, start_angle=-PI/3, angle=PI/1.5, arc_center=intersections_bc[0], color=BLUE, stroke_width=2)
        
        # Find intersection points of the two arcs
        def arc_intersections(arc1_center, arc2_center, radius):
            d = np.linalg.norm(arc1_center - arc2_center)
            
            if d > 2 * radius or d == 0:
                return []  # No intersection or coincident arcs
            
            a = (radius**2 - radius**2 + d**2) / (2 * d)
            h = np.sqrt(radius**2 - a**2)
            x2 = arc1_center[0] + a * (arc2_center[0] - arc1_center[0]) / d
            y2 = arc1_center[1] + a * (arc2_center[1] - arc1_center[1]) / d
            
            x3 = x2 + h * (arc2_center[1] - arc1_center[1]) / d
            y3 = y2 - h * (arc2_center[0] - arc1_center[0]) / d
            
            x4 = x2 - h * (arc2_center[1] - arc1_center[1]) / d
            y4 = y2 + h * (arc2_center[0] - arc1_center[0]) / d
            
            return [np.array([x3, y3, 0]), np.array([x4, y4, 0])]
        
        intersections_arc = arc_intersections(intersections_ab[0], intersections_bc[0], radius_arc)
        
        # Create dot at intersection point F
        dot_f = Dot(intersections_arc[0], color=PURPLE) if intersections_arc else None
        label_f = Text("F", color=PURPLE).next_to(dot_f, UP) if dot_f else None
        
        # Define ray BF, extend it, and increase thickness
        ray_bf_start = point_b.get_center()  # Extend start point
        ray_bf_end = point_b.get_center() + 2 * (dot_f.get_center() - point_b.get_center())  # Extend end point
        ray_bf = Line(start=ray_bf_start, end=ray_bf_end, color=ORANGE, stroke_width=4)
        step_1 = Text("Step 1. Draw the given angle ABC", font_size=24).to_edge(UP+RIGHT)
        
        step_2 = Text("Step 2. Taking B as centre and with any radius,\n" "draw an arc  to intersect the rays BA  and BC,\n" "at D and E respectively.", font_size=24).to_edge(UP+RIGHT)
        
        step_3 = Text("Step 3 : Taking E and D as centres draw two arcs \n" "with equal radii to intersect each other.\n" "Let the point of intersection be F.", font_size=24).to_edge(UP+RIGHT)
        
        step_4 = Text("Step 4 : Draw the ray BF. It is the required bisector of ∠ABC .", font_size=24).to_edge(UP+RIGHT)
        
        # Animate
        self.play(FadeIn(step_1))
        self.wait(2)
        self.play(FadeIn(point_a))
        self.play(FadeIn( point_b))
        self.play(FadeIn( point_c))
        self.wait(1)
        self.play( Write(label_a))
        self.play( Write(label_b))
        self.play(Write(label_c) )
        self.wait(1)
        self.play(Create(line_ab))
        self.play(Create(line_bc))
        self.wait(1.5)
        self.play(ReplacementTransform(step_1, step_2))
        self.wait(2)
        self.play(Create(arc))
        self.wait(1.5)
        if dot_d:
            self.play(FadeIn(dot_d), Write(label_d))
            self.wait(1.5)
        if dot_e:
            self.play(FadeIn(dot_e), Write(label_e))
            self.wait(1.5)
        self.play(ReplacementTransform(step_2, step_3))
        self.wait(2)
        if arc_d:
            self.play(Create(arc_d))
            self.wait(1.5)
        
        if arc_e:
            self.play(Create(arc_e))
            self.wait(1.5)
        
        if dot_f:
            self.play(FadeIn(dot_f), Write(label_f))
            self.wait(1.5)
        self.play(ReplacementTransform(step_3, step_4))
        self.wait(2)
        if ray_bf:
            self.play(Create(ray_bf))
        
        # Wait for a moment
        self.wait(2)
    
    def Create60DegreeAngle(self):
        title = Text("Constructing a 60-Degree Angle", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Define points and radius
        radius = 2
        point_a = Dot(ORIGIN, color=BLUE)
        point_b = Dot(RIGHT * 3, color=BLUE)
        label_a = Text("A").next_to(point_a, DOWN)
        label_b = Text("B").next_to(point_b, DOWN)
        
        # Step 1: Draw the given ray AB and draw an arc centered at A
        step_1 = Text("Step 1: Draw the line segment AB. Centered at A, draw an circle with any\n""        radius intersecting AB at D.", font_size=24).shift(LEFT+UP*3.5)
        ray_ab = Line(point_a.get_center(), point_b.get_center(), color=WHITE)
        arc_center_a = Circle(radius=radius, color=RED).move_to(point_a.get_center())
        intersection_d = arc_center_a.get_right()  # Approximate Intersection point D on AB

        # Points and Labels
        point_d = Dot(intersection_d, color=YELLOW)
        label_d = Text("D").next_to(point_d, DOWN)
        
        self.play(Write( step_1))
        self.wait(2)
        self.play(FadeIn(point_a))
        self.play(FadeIn(point_b))
        self.play(Write(label_a))
        self.play(Write(label_b))
        self.play(Create(ray_ab))
        self.wait(1)

        # Step 2: Draw an arc centered at D with the same radius
        step_2 = Text("Step 2: Centered at D, draw an circle with the same radius intersecting the first circle at E.", font_size=24).shift(UP*2.8)
        self.play(Write(step_2))
        self.wait(2)
        self.play(Create(arc_center_a))
        self.wait(1)
        self.play( FadeIn(point_d))
        self.play(Write(label_d))
        # Arc centered at D
        arc_center_d = Circle(radius=radius, color=RED).move_to(point_d.get_center())
        def intersection_of_circles(circle1, circle2):
            """Returns the intersection point of two circles."""
            center1, center2 = circle1.get_center(), circle2.get_center()
            radius1, radius2 = circle1.radius, circle2.radius
            d = np.linalg.norm(center1 - center2)

            if d > radius1 + radius2 or d < abs(radius1 - radius2) or d == 0:
                raise Exception("No intersection or circles are identical")

            a = (radius1**2 - radius2**2 + d**2) / (2 * d)
            h = np.sqrt(radius1**2 - a**2)
            p2 = center1 + a * (center2 - center1) / d
            intersection1 = p2 + h * np.array([- (center2[1] - center1[1]) / d, (center2[0] - center1[0]) / d, 0])
            intersection2 = p2 - h * np.array([- (center2[1] - center1[1]) / d, (center2[0] - center1[0]) / d, 0])

            return intersection1 
        # Calculate intersection of two circles
        intersection_e = intersection_of_circles(arc_center_a, arc_center_d)

        point_e = Dot(intersection_e, color=YELLOW)
        label_e = Text("E").next_to(point_e, UP)
        self.wait(1)
        self.play(Create(arc_center_d))
        self.wait(1)
        self.play(FadeIn(point_e), Write(label_e))
        self.wait(1)

        # Step 3: Draw the ray AE
        step_3 = Text("Step 3: Connect the points A and E to form the 60-degree angle ∠BAE.", font_size=24).shift(LEFT+DOWN*2.5)
        self.play(Write(step_3))
        self.wait(2)
        ray_ae = Line(point_a.get_center(), point_e.get_center(), color=WHITE)
        angle_arc = Arc(radius=0.5, start_angle=0, angle=PI/3, color=GREEN)
        
        # Center the angle arc at point_a
        angle_arc.move_to(point_a.get_center() + RIGHT * 0.5+UP*0.25)  # Adjust position based on the radius and angle visibility
        
        # Correct Position of Angle Label
        angle_label = Tex(r"$60^\circ$").next_to(angle_arc, RIGHT, buff=0.3)
        
        self.play(Create(ray_ae))
        self.wait(1)
        self.play(Create(angle_arc))
        self.wait(1)
        self.play(Write(angle_label))
        self.wait(2)

    def ConstructTriangle(self):
        Example_text = Text(" Example - Construct a ΔABC \n""given BC = 5 cm., AB + AC = 8 cm\n"" and ∠ABC = 60 degree",font_size=24).shift(UP*3+LEFT*4.3)
        self.play(Write(Example_text))
        self.wait(2)
        # Step 1 Text
        step1_text = Text("Step 1: Draw line segment BC with \n" " length 5cm, the 60-degree angle \n"" at B,and a line segment of any radius BX",font_size=24).shift(UP*1.5+LEFT*4.2+RIGHT*0.1)
        
        # Setup points B and C and initial elements
        B = np.array([-1, -3, 0])
        C = np.array([4, -3, 0])
        
        # Create the line segment BC
        line_BC = Line(B, C, color=BLUE)
        point_B = Dot(B, color=RED)
        point_C = Dot(C, color=RED)
        label_B = Tex("B").next_to(point_B, LEFT, )
        label_C = Tex("C").next_to(point_C, RIGHT, buff=0.1)
        
        # Draw the 60 degree angle at B
        angle_arc = Arc(radius=1, start_angle=0, angle=PI/3, arc_center=B, color=RED)
        angle_label = MathTex(r"60^\circ").next_to(angle_arc, UP+RIGHT+DOWN, buff=0.1)
        F = np.array([-1.3, -3, 0])
        # Draw the extended ray BX with a larger length
        ray_length = 8
        ray_direction = np.array([np.cos(PI/3), np.sin(PI/3), 0])
        ray_BX = Line(B, B + ray_length * ray_direction, color=GREEN)
        # ray_BX_start = B + np.array([0, -0.5, 0])  # Shift starting point slightly lower
        # ray_BX_end = ray_BX_start + ray_length * ray_direction  # Calculate the new end position
        # ray_BX = Arrow(ray_BX_start, ray_BX_end, color=GREEN)
        point_X = B + ray_length * ray_direction
        label_X = Tex("X").next_to(point_X, RIGHT+DOWN*0.4, buff=0.1)
        
        # Draw the arc with center B and increased radius
        radius_arc = 7.7
        arc = Arc(radius=radius_arc, start_angle=PI/5, angle=2 * PI/6, arc_center=B, color=BLUE, stroke_width=2)
        intersection_point_D = B + radius_arc * ray_direction
        point_D = Dot(intersection_point_D, color=PURPLE, radius=0.1)
        label_D = Tex("D").next_to(point_D, LEFT+DOWN*0.3, buff=0.1)
        length_label = Tex("5 cm").next_to(line_BC, DOWN, buff=0.1)
        
        # Display Step 1: Draw points B, C, angle arc, and ray BX
        self.play(Write(step1_text))
        self.wait(2)
        self.play(Create(line_BC))
        self.wait(1)
        self.play(FadeIn(point_B))
        self.play(FadeIn(point_C))
        self.wait(1)
        self.play(Write(label_B))
        self.play(Write(label_C))
        self.wait(1)
        self.play(Write(length_label))
        self.wait(1)
        self.play(Create(ray_BX))
        self.wait(1)
        self.play(FadeIn(Dot(point_X, color=RED)))
        self.wait(1)
        self.play( Write(label_X))
        self.wait(1)
        self.play(Create(angle_arc))
        self.wait(1)
        
        self.play(Write(angle_label))
        self.wait(1)
        
        
        self.wait(1)
        
        self.wait(2)  # Wait for 2 seconds
        
        # Transition to Step 2
        step2_text = Text("Step 2: Draw an arc with radius 8cm.\n "" on BX to intersect at D and join CD",font_size=24).shift(UP*0.2+LEFT*3.8)
        self.play(Write(step2_text))
        self.wait(2)
        self.play(Create(arc))
        self.wait(1)
        self.play(FadeIn(point_D))
        self.wait(1)
        self.play(Write(label_D))
        self.wait(1)
        # Step 2 Elements
        line_CD = Line(C, intersection_point_D, color=ORANGE)
        radius_circle = np.linalg.norm(C - intersection_point_D) / 2 + 1
        circle_C = Circle(radius=radius_circle, arc_center=C, color=BLUE, stroke_width=2)
        circle_D = Circle(radius=radius_circle, arc_center=intersection_point_D, color=BLUE, stroke_width=2)

        # Calculate intersection points of the circles
        def find_circle_intersections(c1, c2, r):
            d = np.linalg.norm(c1 - c2)
            if d > 2 * r or d < 0 or d == 0:
                return []
            a = (r**2 - r**2 + d**2) / (2 * d)
            h = np.sqrt(r**2 - a**2)
            p2 = c1 + a * (c2 - c1) / d
            direction = np.array([- (c2[1] - c1[1]), c2[0] - c1[0]])
            direction = direction / np.linalg.norm(direction)
            intersection1 = p2 + h * direction
            intersection2 = p2 - h * direction
            return [intersection1, intersection2]
        
        intersections = find_circle_intersections(C[:2], intersection_point_D[:2], radius_circle)
        if len(intersections) == 2:
            intersection1, intersection2 = intersections
            point_intersection1 = Dot(np.append(intersection1, 0), color=YELLOW)
            point_intersection2 = Dot(np.append(intersection2, 0), color=YELLOW)
            bisector = Line(point_intersection1.get_center(), point_intersection2.get_center(), color=RED)
            self.play(Create(line_CD))
            self.wait(1)
            step3_text = Text("Step 3: Draw a perpendicular  bisector of \n""CD to meet BD at A ",font_size=24).shift(DOWN*1+LEFT*3.5)
            self.play(Write(step3_text))
            
            self.play(Create(circle_C))
            self.wait(1)
            self.play(Create(circle_D))
            self.wait(1)
            
            self.play(FadeIn(point_intersection1), FadeIn(point_intersection2))
            self.wait(1)
            self.play(Create(bisector))
            self.wait(2)  # Wait for 2 seconds
            
            # Transition to Step 3
            step4_text = Text("Step 4: Join AC to get the required\n"" triangle △ABC ",font_size=24).shift(DOWN*2+LEFT*4)
            
            
            # Step 3 Elements
            line_BD = Line(B, intersection_point_D, color=GREEN)
            def intersection(p1, p2, p3, p4):
                def det(a, b):
                    return a[0] * b[1] - a[1] * b[0]
                
                xdiff = (p1[0] - p2[0], p3[0] - p4[0])
                ydiff = (p1[1] - p2[1], p3[1] - p4[1])
                div = det(xdiff, ydiff)
                if div == 0:
                    return None
                d = (det(p1, p2), det(p3, p4))
                x = det(d, xdiff) / div
                y = det(d, ydiff) / div
                return np.array([x, y, 0])
            
            p1, p2 = tuple(B), tuple(intersection_point_D)
            p3, p4 = tuple(intersection1), tuple(intersection2)
            intersection_with_BD = intersection(p1, p2, p3, p4)
            point_A = Dot(intersection_with_BD, color=BLUE)
            label_A = Tex("A").next_to(point_A, LEFT, buff=0.1)
            ray_AC = Line(point_A, C, color=PURPLE)
            
            # Display Step 3: Draw line BD, find intersection A, and draw ray AC
            self.play(Create(line_BD))
            self.wait(1)
            self.play(FadeIn(point_A))
            self.wait(1)
            self.play(Write(label_A))
            self.wait(1)
            self.play(Write(step4_text))
            self.wait(1)
            self.play(Create(ray_AC))
            self.wait(2)  

        # Show final result
        self.wait(3)



    def ConstructTriangle2(self):
        # Step 0: Example Text
        Example_text = Text("Example - Construct a ΔABC \n"
                            "given BC = 4.2 cm, ∠B = 30°, AB - AC = 1.6 cm",
                            font_size=24).shift(UP*3 + LEFT*3)
        self.play(Write(Example_text))
        self.wait(2)

        # Setup points B and C
        B = np.array([1, 0, 0])
        C = np.array([4.5, 0, 0])

        # Create the line segment BC
        line_BC = Line(B, C, color=BLUE)
        point_B = Dot(B, color=RED)
        point_C = Dot(C, color=RED)
        label_B = Tex("B").next_to(point_B, LEFT, buff=0.1)
        label_C = Tex("C").next_to(point_C, RIGHT, buff=0.1)
        length_label = Tex("4.2 cm").next_to(line_BC, DOWN, buff=0.1)

        # Draw the 30 degree angle at B
        angle_arc = Arc(radius=1, start_angle=0, angle=PI/6, arc_center=B, color=RED)
        angle_label = MathTex(r"30^\circ").next_to(angle_arc, UP+RIGHT+DOWN, buff=0.1)

        # Draw the extended ray BX with a larger length
        ray_length = 6
        ray_direction = np.array([np.cos(PI/6), np.sin(PI/6), 0])
        ray_BX = Line(B, B + ray_length * ray_direction, color=GREEN)
        point_X = B + ray_length * ray_direction
        label_X = Tex("X").next_to(point_X, RIGHT + DOWN * 0.4, buff=0.1)

        # Draw the arc with center B and increased radius
        radius_arc = 1.5
        arc = Arc(radius=radius_arc, start_angle=PI/10, angle=PI/3, arc_center=B, color=BLUE, stroke_width=2)

        # Step 1 Text
        step1_text = Text("Step 1: Draw line segment BC with length ,\n"
                          " 4.2 cm, the 30-degree angle at B and a ,\n"
                          " line segment of any length BX", font_size=24).shift(UP*1.5 + LEFT*3.7+RIGHT*0.2)
        
        # Display Step 1: Draw points B, C, angle arc, and ray BX
        self.play(Write(step1_text))
        self.wait(2)
        self.play(Create(line_BC))
        self.wait(1)
        self.play(FadeIn(point_B))
        self.play(FadeIn(point_C))
        self.wait(1)
        self.play(Write(label_B))
        self.play(Write(label_C))
        self.play(Write(length_label))
        self.wait(1)
        self.play(Create(ray_BX))
        self.wait(1)
        self.play(FadeIn(Dot(point_X, color=RED)))
        self.play(Write(label_X))
        self.wait(1)
        self.play(Create(angle_arc))
        self.wait(1)
        self.play(Write(angle_label))
        self.wait(1)

        # Step 2: Place point D on BX
        step2_text = Text("Step 2: Draw an arc with radius 1.6cm.\n"
                          " on BX to intersect at D and join CD", font_size=24).shift(UP*0.2 + LEFT*4)
        self.play(Write(step2_text))
        self.wait(2)
        self.play(Create(arc))
        self.wait(1)
        # Calculate point D
        distance_BD = 1.6
        point_D = B + distance_BD * ray_direction
        label_D = Tex("D").next_to(point_D, UP + LEFT * 0.3, buff=0.1)
        point_D_dot = Dot(point_D, color=PURPLE, radius=0.1)

        # Create the line CD
        line_CD = Line(C, point_D, color=ORANGE)
        line_BD = Line(B, point_D, color=GREEN)
        
        # Display Step 2: Draw point D and line CD
        self.play(FadeIn(point_D_dot))
        self.wait(1)
        self.play(Write(label_D))
        self.wait(1)
        #length_label2 = Tex("1.6 cm").next_to(line_BD, UP+LEFT*0.3, buff=0.1)
        #self.play(Write(length_label2))
        self.wait(1)
        self.play(Create(line_CD))
        self.wait(2)

        # Transition to Step 3
        step3_text = Text("Step 3:Draw a perpendicular bisector of\n"
                              "CD to meet BX at A,and join the points A & C" , font_size=26).shift(DOWN*1 + LEFT*3.5)
        self.play(Write(step3_text))
        self.wait(2)
        

        # Step 3 Elements
        radius_circle = np.linalg.norm(C - point_D) / 2 + 1
        circle_C = Circle(radius=radius_circle, arc_center=C, color=BLUE, stroke_width=2)
        circle_D = Circle(radius=radius_circle, arc_center=point_D, color=BLUE, stroke_width=2)

        # Calculate intersection points of the circles
        def find_circle_intersections(c1, c2, r):
            d = np.linalg.norm(c1 - c2)
            if d > 2 * r or d < 0 or d == 0:
                return []
            a = (r**2 - r**2 + d**2) / (2 * d)
            h = np.sqrt(r**2 - a**2)
            p2 = c1 + a * (c2 - c1) / d
            direction = np.array([- (c2[1] - c1[1]), c2[0] - c1[0]])
            direction = direction / np.linalg.norm(direction)
            intersection1 = p2 + h * direction
            intersection2 = p2 - h * direction
            return [intersection1, intersection2]

        intersections = find_circle_intersections(C[:2], point_D[:2], radius_circle)
        if len(intersections) == 2:
            intersection1, intersection2 = intersections
            point_intersection1 = Dot(np.append(intersection1, 0), color=YELLOW)
            point_intersection2 = Dot(np.append(intersection2, 0), color=YELLOW)
            bisector = Line(point_intersection1.get_center(), point_intersection2.get_center(), color=RED)
            self.play(Create(circle_C))
            self.wait(1)
            self.play(Create(circle_D))
            self.wait(1)
            self.play(FadeIn(point_intersection1), FadeIn(point_intersection2))
            self.wait(1)
            self.play(Create(bisector))
            self.wait(2)

            # Transition to Step 4
            step4_text = Text("Step 4:Therefore ΔABC is the required\n"" triangle"  , font_size=24).shift(DOWN*2 + LEFT*3.5)
            

            # Step 4 Elements
            def intersection(p1, p2, p3, p4):
                def det(a, b):
                    return a[0] * b[1] - a[1] * b[0]

                xdiff = (p1[0] - p2[0], p3[0] - p4[0])
                ydiff = (p1[1] - p2[1], p3[1] - p4[1])
                div = det(xdiff, ydiff)
                if div == 0:
                    return None
                d = (det(p1, p2), det(p3, p4))
                x = det(d, xdiff) / div
                y = det(d, ydiff) / div
                return np.array([x, y, 0])

            p1, p2 = tuple(B), tuple(point_D)
            p3, p4 = tuple(intersection1), tuple(intersection2)
            intersection_with_BD = intersection(p1, p2, p3, p4)
            point_A = Dot(intersection_with_BD, color=BLUE)
            label_A = Tex("A").next_to(point_A, LEFT, buff=0.1)
            ray_AC = Line(point_A, C, color=PURPLE)

            # Display Step 4: Draw line BD, find intersection A, and draw ray AC
            self.play(Create(line_BD))
            self.wait(1)
            self.play(FadeIn(point_A))
            self.wait(1)
            self.play(Write(label_A))
            self.wait(1)
            self.play(Create(ray_AC))
            self.wait(2)
            self.play(Write(step4_text))
            self.wait()
            #step5_text = Text("Step 5:  ", font_size=26).shift(DOWN*1 + LEFT*4.2)
        # Show final result
        self.wait(3)
    def ConstructTriangle3(self):

        Title_text = Text("To Construct a circle segment given a chord \n""and a given angle", font_size=35, font="Georgia").shift(UP)
        self.play(Write(Title_text))
        self.wait(2)
        self.play(FadeOut(Title_text))
        self.wait(1)
        
        # Example and Step 1
        example_text = Text("Example: Construct a segment of Circle on a chord of 5 cm.\n""and containing angle of 60 degrees", font_size=24).to_edge(UP)
        self.play(Write(example_text))
        self.wait(2)
        step1_text = Text("Step 1: Draw the line segment AB = 5 cm", font_size=24).shift(LEFT*4 + UP*1.5)
        self.play(Write(step1_text))
        self.wait(2)
        
        
        A = np.array([1, -1, 0])
        B = np.array([4.5, -1, 0])
        chord_AB = Line(A, B, color=BLUE)
        point_A = Dot(A, color=RED)
        point_B = Dot(B, color=RED)
        label_A = Tex("A").next_to(point_A, DOWN, buff=0.1)
        label_B = Tex("B").next_to(point_B, DOWN, buff=0.1)
        label_AB_length = Tex("5 cm").next_to(chord_AB, DOWN, buff=0.1)
        self.play(Create(chord_AB))
        self.play(FadeIn(point_A), FadeIn(point_B))
        self.play(Write(label_A), Write(label_B))
        self.play(FadeIn(label_AB_length))
        self.wait(2)
        
        # Step 2
        step2_text = Text("Step 2: Draw lines segments AX and BY \n""with any length such that ∠BAX = 30° \n""and ∠YBA = 30°", font_size=24).shift(LEFT*4 + UP*0.5)
        self.play(Write(step2_text))
        self.wait(2)
        
        ray_length = 6  # Increase length for visibility
        angle_30 = PI / 6
        direction_AX = np.array([np.cos(angle_30), np.sin(angle_30), 0])
        direction_BY = np.array([-np.cos(angle_30), np.sin(angle_30), 0])
        line_AX = Line(A, A + ray_length * direction_AX, color=GREEN)
        line_BY = Line(B, B + ray_length * direction_BY, color=GREEN)
        
        # Find intersection O of AX and BY
        intersection_O = self.get_intersection(A, direction_AX, B, direction_BY)
        point_O = Dot(intersection_O, color=YELLOW)
        label_O = Tex("O").next_to(point_O, UP, buff=0.1)
        
        # End points X and Y
        X = A + ray_length * direction_AX
        Y = B + ray_length * direction_BY
        
        point_X = Dot(X, color=RED)
        point_Y = Dot(Y, color=RED)
        label_X = Tex("X").next_to(point_X, UP, buff=0.1)
        label_Y = Tex("Y").next_to(point_Y, UP, buff=0.1)
        
        self.play(Create(line_AX))
        self.play(Create(line_BY))
        self.play(FadeIn(point_X), FadeIn(point_Y))
        self.play(Write(label_X), Write(label_Y))
        self.play(FadeIn(point_O))
        self.play(Write(label_O))
        self.wait(2)
        
        # Draw angle labels for 30 degrees
        # angle_30_A = Angle(line_AX, chord_AB, radius=0.5, other_angle=True)
        # angle_label_30_A = MathTex(r"30^\circ",font_size = 20).next_to(angle_30_A, buff=0.1)
        # angle_30_B = Angle(line_BY, chord_AB, radius=0.5, other_angle=False)
        # angle_label_30_B = MathTex(r"30^\circ",font_size = 20).next_to(angle_30_B, buff=0.1)
        angle_arc_A = Arc(radius=0.5, start_angle=PI, angle=-PI/6, arc_center=A, color=YELLOW).shift(RIGHT*3.5)
        angle_arc_B = Arc(radius=0.5, start_angle=0, angle=PI/6, arc_center=B, color=YELLOW).shift(LEFT*3.5)
        angle_label_A = MathTex(r"30^\circ",font_size = 20).next_to(angle_arc_A, LEFT, buff=0.1)
        angle_label_B = MathTex(r"30^\circ",font_size = 20).next_to(angle_arc_B, RIGHT, buff=0.1)

        self.play(Create(angle_arc_A))
        self.play(Write(angle_label_A))
        self.play(Create(angle_arc_B))
        self.play(Write(angle_label_B))
        self.wait(2)
        
        # Step 3: Draw the circle with center O and radius OA or OB
        radius = np.linalg.norm(intersection_O - A)
        circle = Circle(radius=radius, arc_center=intersection_O, color=ORANGE)
        step3_text = Text("Step 3: With center O and radius OA or OB,\n""draw the circle", font_size=24).shift(LEFT*3.6 + DOWN*1.)
        self.play(Write(step3_text))
        self.wait(2)
        self.play(Create(circle))
        self.wait(1)
        
        # Step 4: Mark point C on the arc and join AC and BC
        point_C = intersection_O + radius * np.array([0, 1, 0])
        point_C_dot = Dot(point_C, color=RED)
        label_C = Tex("C").next_to(point_C, UP, buff=0.1)
        line_AC = Line(A, point_C, color=WHITE)
        line_BC = Line(B, point_C, color=WHITE)
        angle_ACB = Angle(line_AC, line_BC, radius=0.5, other_angle=False)
        angle_label_60 = MathTex(r"60^\circ",font_size = 30).next_to(angle_ACB, DOWN*1.5, buff=0.1)
        step4_text = Text("Step 4: Mark a point C on the circumference of the\n"" circle and join AC and BC.", font_size=24).shift(LEFT*3.6 + DOWN*2)
        
        self.play(Write(step4_text))
        self.wait(2)
        self.play(FadeIn(point_C_dot))
        self.play(Write(label_C))
        self.play(Create(line_AC))
        self.play(Create(line_BC))
        #self.play(Create(angle_ACB))
        #self.play(Write(angle_label_60))
        self.wait(1)
        step5_text = Text("Step 5: Therefore ΔABC is the required triangle ", font_size=24).shift(LEFT*3.6 + DOWN*3)
        self.play(Write(step5_text))
        self.wait(2)
    def get_intersection(self, point1, direction1, point2, direction2):
            # Calculate intersection point of two lines given by point1 + t * direction1 and point2 + t * direction2
            A = np.array([direction1[:2], -direction2[:2]]).T
            b = point2[:2] - point1[:2]
            t = np.linalg.solve(A, b)
            return point1 + t[0] * direction1
        
    def BasicConstructions(self):
        p10=cvo.CVO().CreateCVO("Basic Constructions","").setPosition([-3.5,0,0])
        p11=cvo.CVO().CreateCVO("Perpendicular Bisector","").setPosition([3.5,2.5,0]).setangle([-TAU/4])
        p13=cvo.CVO().CreateCVO("Bisector of angle","").setPosition([3.5,0,0]).setangle([-TAU/4])
        p12=cvo.CVO().CreateCVO("60 degrees angle","").setPosition([3.5,-2.5,0]).setangle([-TAU/4])
        p10.cvolist.append(p11)
        p10.cvolist.append(p13)
        p10.cvolist.append(p12)
        self.isRandom=False       
        self.setNumberOfCirclePositions(4)
        self.construct1(p10,p10)
    


    def PerpenBisector(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Perpendicular bisector","").setPosition([-4,0,0]).setangle(-TAU/4)
        p11=cvo.CVO().CreateCVO("Divides segment perpendicularly","" ).setPosition([4,0,0]).setangle(-TAU/4)
        p11.setcircleradius(2)
        p10.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def BisectorAngle(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Angle bisector","").setPosition([-4,0,0]).setangle(-TAU/4)
        p11=cvo.CVO().CreateCVO("Divides angle into equal parts.","" ).setPosition([4,0,0]).setangle(-TAU/4)
        p11.setcircleradius(2)
        p10.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def BBAS2(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Construction of Triangles","").setPosition([-4,0,0]).setangle(-TAU/4)
        p11=cvo.CVO().CreateCVO("Condition","Given base, Base angle, \\\\Sum of 2 sides").setPosition([4,0,0]).setangle(-TAU/4)
        p11.setcircleradius(2)
        p10.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def BBAD2(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Construction of Triangles","").setPosition([-4,0,0]).setangle(-TAU/4)
        p11=cvo.CVO().CreateCVO("Condition","Given base, Base angle, \\\\Difference of 2 sides").setPosition([4,0,0]).setangle(-TAU/4)
        p11.setcircleradius(2)
        p11.setcircleradius(2)
        p10.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)
    

    def ChordTriangle(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Construction of Triangles","").setPosition([-4,0,0]).setangle(-TAU/4)
        p11=cvo.CVO().CreateCVO("Condition","Cirlce segement\\\\for given chord and angle").setPosition([4,0,0]).setangle(-TAU/4)
        p11.setcircleradius(2)
        p11.setcircleradius(2)
        p10.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)
    

if __name__ == "__main__":
    from manim import *
    scene = Chapter13Anim()
    scene.render()
