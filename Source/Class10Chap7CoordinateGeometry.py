import json
from manim import*
from AbstractAnim import AbstractAnim

import cvo

class CoordinateGeoAnim(AbstractAnim):
    def construct(self):
        self.distance()
        self.fadeOutCurrentScene()
        self.distani()
        self.fadeOutCurrentScene()
        self.section()
        self.fadeOutCurrentScene()
        self.secani()
        self.fadeOutCurrentScene()
        self.midpoint()
        self.fadeOutCurrentScene()
        self.midanim()
        self.fadeOutCurrentScene()
        self.centroid()
        self.fadeOutCurrentScene()
        self.centani()
        self.fadeOutCurrentScene()
        self.triarea()
        self.fadeOutCurrentScene()
        self.slope()
        self.fadeOutCurrentScene()
        self.slopeani()
        self.fadeOutCurrentScene()
        self.herons()
        self.fadeOutCurrentScene()
        self.herani()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        self.fadeOutCurrentScene()

    def distance(self):
        self.isRandom=False
        p10=cvo.CVO().CreateCVO("Two points","")
        p11=cvo.CVO().CreateCVO("Point A","(x1,y1)")
        p12=cvo.CVO().CreateCVO("Point B","(x2,y2)")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p13 = cvo.CVO().CreateCVO("Distance", r"\sqrt{(x1 - x2)^2 + (y1 - y2)^2}").SetIsMathText(True)
        p13.setcircleradius(2)
        
        p10.setPosition([-4,-1,0])
        p11.setPosition([-2, 0, 0])
        p12.setPosition([-4, 1, 0])
        p13.setPosition([3,0,0])

        self.construct1(p10,p10)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        self.construct1(p13, p13)
        self.wait(2)
        
    
    def distani(self):
        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 5, 1],
            axis_config={"color": BLUE},
            ).add_coordinates()

        x_axis_label = Text("x-axis", font_size=16, color=WHITE).next_to(axes.x_axis.get_end(), DOWN)
        y_axis_label = Text("y-axis", font_size=16, color=WHITE).next_to(axes.y_axis.get_end(), LEFT)
        y_axis_label.shift(DOWN*0.3)

        x1, y1 = 1, 1
        x2, y2 = 4, 3
        point_A = axes.coords_to_point(x1, y1)
        point_B = axes.coords_to_point(x2, y2)

        distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

        dot_A = Dot(point_A, color=RED)
        dot_B = Dot(point_B, color=RED)
        label_A = Text("A(1, 1)", font_size=24).next_to(dot_A, DOWN)
        label_B = Text("B(4, 3)", font_size=24).next_to(dot_B, RIGHT)

        line_AB = Line(point_A, point_B, color=GREEN)

        distance_formula = Tex(f"$\\text{{Distance}} = \\sqrt{{(x_2 - x_1)^2 + (y_2 - y_1)^2}} = \\sqrt{{(4 - 1)^2 + (3 - 1)^2}} = {distance}$").to_corner(UL)

        self.play(Create(axes),Write(x_axis_label),Write(y_axis_label))
        self.play(Create(line_AB))
        self.play(FadeIn(dot_A, label_A), FadeIn(dot_B, label_B))
        self.wait(1)
        self.play(Write(distance_formula,run_time=5))
        self.wait(5)


    def section(self):
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("two points","")
        p11=cvo.CVO().CreateCVO("point A","(x1,y1)")
        p12=cvo.CVO().CreateCVO("point B","(x2,y2)")
        p14=cvo.CVO().CreateCVO("Divided Ratio","m:n")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p14)
        p13 = cvo.CVO().CreateCVO("Section formula", r"\left(\frac{mx2 + nx1}{m+n}, \frac{my2 + ny1}{m+n}\right)").SetIsMathText(True)
        p13.setcircleradius(2)
        
        p10.setPosition([-4,-3,0])
        p11.setPosition([-2, -2, 0])
        p12.setPosition([-4, -1, 0])
        p14.setPosition([3,-2,0])
        p13.setPosition([3,2,0])

        self.construct1(p10,p10)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        self.construct1(p13, p13)
        self.wait(2)
    
    def secani(self):
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            axis_config={"color": BLUE},
        ).add_coordinates().shift(DOWN * 0.5)

        x_axis_label = Text("x-axis", font_size=16, color=WHITE).next_to(axes.x_axis.get_end(), DOWN)
        y_axis_label = Text("y-axis", font_size=16, color=WHITE).next_to(axes.y_axis.get_end(), LEFT)
        y_axis_label.shift(DOWN*0.3)

        # Points A and B
        x1, y1 = 1, 1
        x2, y2 = 4, 3
        point_A = axes.coords_to_point(x1, y1)
        point_B = axes.coords_to_point(x2, y2)

        # Ratio m:n
        m, n = 2, 3

        # Calculate section point
        x = (m * x2 + n * x1) / (m + n)
        y = (m * y2 + n * y1) / (m + n)
        point_P = axes.coords_to_point(x, y)

        # Create points and labels
        dot_A = Dot(point_A, color=RED)
        dot_B = Dot(point_B, color=RED)
        dot_P = Dot(point_P, color=YELLOW)
        label_A = MathTex("A(1, 1)", font_size=24).next_to(dot_A, DOWN)
        label_B = MathTex("B(4, 3)", font_size=24).next_to(dot_B, RIGHT)
        label_P = MathTex(f"P({x:.1f}, {y:.1f})", font_size=24).next_to(dot_P, UP)

        # Line segment AB
        line_AB = Line(point_A, point_B, color=GREEN)

        # Section formula label
        section_label = Text("Section Formula", font_size=32).to_corner(UL)

        # Create section formula
        section_formula_x = MathTex(
            r"x = \frac{m x_2 + n x_1}{m + n} = \frac{2 \cdot 4 + 3 \cdot 1}{2 + 3} = " + f"{x:.1f}", font_size=24
        ).to_corner(UR).shift(LEFT * 2)

        section_formula_y = MathTex(
            r"y = \frac{m y_2 + n y_1}{m + n} = \frac{2 \cdot 3 + 3 \cdot 1}{2 + 3} = " + f"{y:.1f}", font_size=24
        ).next_to(section_formula_x, DOWN)

        # Display elements
        self.play(Create(axes),Write(x_axis_label),Write(y_axis_label))
        self.play(Create(line_AB))
        self.play(FadeIn(dot_A, label_A), FadeIn(dot_B, label_B))
        self.wait(1)
        self.play(FadeIn(dot_P, label_P))
        self.wait(1)

        # Show the section formula label
        self.play(Write(section_label))
        self.wait(1)
        # Write section formulas slowly
        self.play(Write(section_formula_x, run_time=4))
        self.wait(2)
        self.play(Write(section_formula_y, run_time=4))
        self.wait(3)
        
    def midpoint(self):
        self.isRandom = False
        self.positionChoice = [[-4,0,0],[4,0,0]]
        p10=cvo.CVO().CreateCVO("Mid point","")
        p11=cvo.CVO().CreateCVO("Formula",r"\left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)").SetIsMathText(True)
        p11.setcircleradius(1.8)
        p10.cvolist.append(p11)
        
        self.construct1(p10,p10)

    def midanim(self):
        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 5, 1],
            axis_config={"color": BLUE},
        ).add_coordinates()

        x_axis_label = Text("x-axis", font_size=16, color=WHITE).next_to(axes.x_axis.get_end(), DOWN)
        y_axis_label = Text("y-axis", font_size=16, color=WHITE).next_to(axes.y_axis.get_end(), LEFT)
        y_axis_label.shift(DOWN*0.3)

        x1, y1 = 1, 1
        x2, y2 = 4, 3
        point_A = axes.coords_to_point(x1, y1)
        point_B = axes.coords_to_point(x2, y2)

        mx = (x1 + x2) / 2
        my = (y1 + y2) / 2
        point_M = axes.coords_to_point(mx, my)

        dot_A = Dot(point_A, color=RED)
        dot_B = Dot(point_B, color=RED)
        dot_M = Dot(point_M, color=YELLOW)
        label_A = Text("A(1, 1)", font_size=24).next_to(dot_A, DOWN)
        label_B = Text("B(4, 3)", font_size=24).next_to(dot_B, RIGHT)
        label_M = Text(f"M({mx}, {my})", font_size=24).next_to(dot_M, UP)

        line_AB = Line(point_A, point_B, color=GREEN)

        midpoint_formula = Tex(
            f"$\\text{{Midpoint}} = \\left( \\frac{{x_1 + x_2}}{2}, \\frac{{y_1 + y_2}}{2} \\right) = \\left( \\frac{{1 + 4}}{2}, \\frac{{1 + 3}}{2} \\right) = ({mx}, {my})$").to_corner(UL)

        self.play(Create(axes),Write(x_axis_label),Write(y_axis_label))
        self.play(Create(line_AB))
        self.play(FadeIn(dot_A, label_A), FadeIn(dot_B, label_B))
        self.play(FadeIn(dot_M, label_M))
        self.wait(1)
        self.play(Write(x_axis_label),Write(y_axis_label))
        self.play(Write(midpoint_formula,run_time=4))
        self.wait(4)


    def centroid(self):
        self.isRandom = False
        self.positionChoice = [[-4, -3, 0], [-3, 0, 0], [3, 0, 0]]

        p20 = cvo.CVO().CreateCVO("Triangle", "")
        p21 = cvo.CVO().CreateCVO("centroid", "")
        p22 = cvo.CVO().CreateCVO("Formula", r"\left(\frac{x_1 + x_2 + x_3}{3}, \frac{y_1 + y_2 + y_3}{3}\right)").SetIsMathText(True)
        p20.setcircleradius(1.2)
        p22.setcircleradius(2.1)
        p20.cvolist.append(p21)
        p21.cvolist.append(p22)
        self.construct1(p20,p20)

    def centani(self):
        vertices = [
            [-3, -2, 0],
            [3, -2, 0],
            [0, 3, 0]
        ]

        vertex_labels = ["(x1, y1)", "(x2, y2)", "(x3, y3)"]
        label_directions = [DOWN, DOWN, UP]

        centroid_x = sum(v[0] for v in vertices) / 3
        centroid_y = sum(v[1] for v in vertices) / 3

        triangle = Polygon(*vertices, stroke_color=WHITE, stroke_width=2, fill_color=BLUE, fill_opacity=0.5)

        labels = [
            Text(label, font_size=18, color=WHITE).next_to(vertex, direction, buff=0.2)
            for vertex, label, direction in zip(vertices, vertex_labels, label_directions)
        ]

        centroid_dot = Dot(color=ORANGE).move_to([centroid_x, centroid_y, 0])
        centroid_label = Text("Centroid", font_size=18, color=WHITE).next_to(centroid_dot, DOWN, buff=0.3)

        centroid_formula = MathTex(r"\left(\frac{x_1 + x_2 + x_3}{3}, \frac{y_1 + y_2 + y_3}{3}\right)", font_size=18, color=WHITE).next_to(centroid_label, DOWN, buff=0.3)

        self.play(Create(triangle), Create(centroid_dot))
        self.play(*[Create(label) for label in labels])
        self.play(Write(centroid_label))
        self.play(Write(centroid_formula, run_time=4))
        self.wait(2)

    def triarea(self):
        self.isRandom = False
        self.positionChoice = [[-4,-2,0], [0,-2,0], [3,1,0],]
        p61 = cvo.CVO().CreateCVO("Triangle", "")
        p62 = cvo.CVO().CreateCVO("Area",r"\frac{1}{2} base*height").SetIsMathText(True)
        p62.setcircleradius(1.5)

        p61.cvolist.append(p62)

        triangle = Polygon([-1, -0.5, 0], [1, -0.5, 0], [0, 1.5, 0], color=BLUE)
        base_line = Line(start=[-1, -0.5, 0], end=[1, -0.5, 0], color=YELLOW)
        height_line = Line(start=[0, -0.5, 0], end=[0, 1.5, 0], color=YELLOW)
        base_label = Tex("base").next_to(base_line, DOWN, buff=0.1)
        height_label = Tex("height").next_to(height_line, RIGHT, buff=0.1)
    
        # Move the triangle up
        triangle.shift(UP * 2.3)
        base_line.shift(UP * 2.3)
        height_line.shift(UP * 2.3)
        base_label.shift(UP * 2.3)
        height_label.shift(UP * 2.3)  
        self.construct1(p61, p61)
        self.play(Create(triangle), Create(base_line), Create(height_line), Create(base_label), Create(height_label))
        self.wait(3)
        
    def herons(self):
        self.isRandom = False
        self.positionChoice = [[-4, 2, 0], [0, 2, 0], [4, 2, 0]]

    
        p13 = cvo.CVO().CreateCVO("Area of Triangle", "")
        p14 = cvo.CVO().CreateCVO("Heron's Formula", r"\sqrt{s(s-a)(s-b)(s-c)}").SetIsMathText(True)
        p15 = cvo.CVO().CreateCVO("to find S", "(a + b + c)/2").SetIsMathText(True)

        p14.setcircleradius(1.8)
        p15.setcircleradius(1.4)

        p13.cvolist.append(p14)

        # Constructing the scene
        self.construct1(p13, p13)
        self.construct1(p15, p15)

    def herani(self):
        A = [-1, -0.5, 0]
        B = [1, -0.5, 0]
        C = [0, 1.5, 0]

        # Create the triangle
        triangle = Polygon(A, B, C, color=BLUE)

        # Labels for sides a, b, c
        label_a = MathTex("a").next_to(Line(C, B).get_center(), LEFT, buff=0.1)
        label_b = MathTex("b").next_to(Line(A, C).get_center(), RIGHT, buff=0.1)
        label_c = MathTex("c").next_to(Line(A, B).get_center(), DOWN, buff=0.1)
        line=Line(start=[-1, -0.5, 0], end=[1, -0.5, 0])
        label_a.shift(RIGHT * 0.4)
        label_b.shift(LEFT* 0.4)
        

        # Create labels for the sides
        side_labels = VGroup(label_a, label_b, label_c)

        # Calculate side lengths
        a = np.linalg.norm(np.array(B) - np.array(C))
        b = np.linalg.norm(np.array(A) - np.array(C))
        c = np.linalg.norm(np.array(A) - np.array(B))

        # Semi-perimeter calculation
        s = (a + b + c) / 2
        semi_perimeter = MathTex(r"s = \frac{a + b + c}{2} ", font_size=30).next_to(line,DOWN)
        semi_perimeter.shift(DOWN*0.2)

        # Heron's formula for area calculation
        herons_formula = MathTex(r"\text{Area using Heron's formula} = \sqrt{s(s-a)(s-b)(s-c)}", font_size=30).next_to(semi_perimeter, DOWN)
        area = np.sqrt(s * (s - a) * (s - b) * (s - c))

        # Display elements
        self.play(Create(triangle), Write(side_labels))
        self.wait(1)
        self.play(Write(semi_perimeter,run_time=4))
        self.play(Write(herons_formula,run_time=5))
        self.wait(5)

    def slope(self):
        self.isRandom = False
        self.positionChoice = [[-4,0,0],[4,0,0]]

        p12 = cvo.CVO().CreateCVO("slope", "m")
        p13 = cvo.CVO().CreateCVO("Slope formula","m = (y2 - y1)/(x2 - x1)").SetIsMathText(True)

        p13.setcircleradius(1.5)
        p12.cvolist.append(p13)

        self.construct1(p12, p12)
        self.wait(2)
    
    def slopeani(self):
        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 5, 1],
            axis_config={"color": BLUE},
        ).add_coordinates()

        x_axis_label = Text("x-axis", font_size=16, color=WHITE).next_to(axes.x_axis.get_end(), DOWN)
        y_axis_label = Text("y-axis", font_size=16, color=WHITE).next_to(axes.y_axis.get_end(), LEFT)
        y_axis_label.shift(DOWN*0.3)

        x1, y1 = 0, 0
        x2, y2 = 3, 3
        point_A = axes.coords_to_point(x1, y1)
        point_B = axes.coords_to_point(x2, y2)

        line = Line(start=point_A, end=point_B, color=GREEN)

        slope = (y2 - y1) / (x2 - x1)

        slope_equation = Tex(
            f"$\\text{{Slope}} = \\frac{{y_2 - y_1}}{{x_2 - x_1}} = \\frac{{3 - 0}}{{3 - 0}} = {slope}$").to_corner(UL)
        slope_equation.shift(UP*0.2)
        
        dot_A = Dot(point_A, color=RED)
        dot_B = Dot(point_B, color=RED)
        label_A = Text("A(0, 0)", font_size=24).next_to(dot_A, DOWN)
        label_B = Text("B(3, 3)", font_size=24).next_to(dot_B, RIGHT)

        self.play(Create(axes),Write(x_axis_label),Write(y_axis_label))
        self.play(Create(line))
        self.play(FadeIn(dot_A, label_A), FadeIn(dot_B, label_B))
        self.wait(1)
        self.play(Write(slope_equation,run_time=4))
        self.wait(2)

    def SetDeveloperList(self): 
       self.DeveloperList="T Sai Rohith Reddy" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Class10Chap7CoordinateGeometry.py"
        
    

if __name__=="__main__":
    scene=CoordinateGeoAnim()
    scene.render()
