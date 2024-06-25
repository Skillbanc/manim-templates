import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo

class FractionIntro(AbstractAnim):
    def construct(self):
        self.Intro()
        self.fadeOutCurrentScene()
        self.Definition()
        self.fadeOutCurrentScene()
        self.CircleExample()
        self.fadeOutCurrentScene()
        self.Example2()
        self.fadeOutCurrentScene()
        self.Example3()
        self.fadeOutCurrentScene()
        self.Example4()
        self.fadeOutCurrentScene()
        self.ImproperFraction()
        self.fadeOutCurrentScene()
        self.ImproperExp1()
        self.fadeOutCurrentScene()
        self.ImproperExp2()
        self.fadeOutCurrentScene()
        self.ImproperExp3()
        self.fadeOutCurrentScene()
        self.MixedFractions()
        self.fadeOutCurrentScene()
        self.MixedFractionExp1()
        self.fadeOutCurrentScene()
        self.MixedFractionExp2()
        self.fadeOutCurrentScene()
        self.NumberLineExp1()
        self.fadeOutCurrentScene()
        self.NumberLineExp2()
        


    def Intro(self):
        title = Text("Fractions and Decimals", font_size=72)
        self.play(FadeIn(title, shift=UP))
        self.wait(0.5)
        self.play(FadeOut(title))

    def Definition(self):
        p10 = cvo.CVO().CreateCVO("Fractions", "").setPosition([3,1,0])
        p11 = cvo.CVO().CreateCVO("Definition", "A fraction represents a part of a whole").setPosition([3,-1,0])
        p12 = cvo.CVO().CreateCVO("Fraction Form", r"$\frac{p}{q}$").setPosition([-3,1,0]).setangle(-TAU/4)
        p13 = cvo.CVO().CreateCVO("Numerator", "p").setPosition([-3,-1,0]).setangle(-TAU/4)
        p14 = cvo.CVO().CreateCVO("Denominator", "q").setPosition([0,-2,0])
    
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p12.cvolist.append(p13)
        p12.cvolist.append(p14)
        self.construct1(p10, p10)



    def CircleExample(self):
        examples_title = Text("Examples", font_size=36).to_edge(UP)
        self.play(Write(examples_title)) 
        circle = Circle(fill_color=PINK, fill_opacity=0.5).shift(LEFT*3)  # create a circle and move it to the left

        # Create vertical and horizontal lines
        vertical_line = Line(ORIGIN, UP * 2, color=BLACK).shift(LEFT*3)
        horizontal_line = Line(ORIGIN, RIGHT * 2, color=BLACK).shift(LEFT*3)

        # Position the lines at the center
        vertical_line.move_to(circle.get_center())
        horizontal_line.move_to(circle.get_center())

        # Create labels for each quarter circle at their midpoints
        label_1 = Text("1", color=BLACK).move_to(UP * 0.5 + LEFT * 0.5 + LEFT*3)
        label_2 = Text("2", color=BLACK).move_to(UP * 0.5 + RIGHT * 0.5 + LEFT*3)
        label_3 = Text("3", color=BLACK).move_to(DOWN * 0.5 + LEFT * 0.5 + LEFT*3)
        label_4 = Text("4", color=BLACK).move_to(DOWN * 0.5 + RIGHT * 0.5 + LEFT*3)

        self.play(Create(circle), Create(vertical_line), Create(horizontal_line))  # show the circle and lines on screen
        self.play(Write(label_1), Write(label_2), Write(label_3), Write(label_4))  # show the labels on screen

        # Shade quarters 1, 2, and 3 in green
        quarter_1 = Sector(outer_radius=1, start_angle=PI / 2, angle=PI / 2, color=GREEN, fill_opacity=0.5).shift(LEFT*3)
        quarter_2 = Sector(outer_radius=1, start_angle=0, angle=PI / 2, color=GREEN, fill_opacity=0.5).shift(LEFT*3)
        quarter_3 = Sector(outer_radius=1, start_angle=PI, angle=PI / 2, color=GREEN, fill_opacity=0.5).shift(LEFT*3)

        self.play(Create(quarter_1), Create(quarter_2), Create(quarter_3))  # show the shaded quarters

        self.wait() 
        # Indicate the fraction 3/4
        fraction = Tex(r"$\frac{3}{4}$", font_size=96).shift(RIGHT*3)
        self.play(Write(fraction))

        # Create arrow from circle to fraction
        arrow_to_fraction = Arrow(circle.get_right(), fraction, color=WHITE)

        self.play(Create(arrow_to_fraction))
        
    def Example2(self):
        # Create a circle and move it to the left
        circle = Circle(radius=1, fill_color=BLUE, fill_opacity=0.5).shift(LEFT * 4)
        self.play(Create(circle))

        # Create the dividing lines
        lines = VGroup()
        for i in range(3):
            angle = i * 2 * PI / 3
            line = Line(circle.get_center(), circle.point_at_angle(angle), color=YELLOW)
            lines.add(line)

        self.play(Create(lines))

        # Create a sector to highlight one part
        sector = Sector(outer_radius=1, angle=2 * PI / 3, start_angle=0, color=GREEN, fill_opacity=0.5).shift(LEFT * 4)
        self.play(Create(sector))

        # Add boundaries to the sector
        sector_boundary_lines = VGroup(
            Line(circle.get_center(), circle.point_at_angle(0), color=RED).shift(LEFT * 4),
            Line(circle.get_center(), circle.point_at_angle(2 * PI / 3), color=RED).shift(LEFT * 4)
        )
        self.play(Create(sector_boundary_lines))
        # Indicate the fraction 1/3
        fraction = MathTex(r"\frac{1}{3}", font_size=96).shift(RIGHT * 5)
        self.play(Write(fraction))

        # Create an arrow from the circle to the fraction
        arrow_to_fraction = Arrow(circle.get_right(), fraction, color=WHITE)
        self.play(Create(arrow_to_fraction))

    def Example3(self):
        circle = Circle(fill_color=PINK, fill_opacity=0.5).shift(LEFT*3) 
        vertical_line = Line(ORIGIN, UP * 2, color=BLACK).shift(LEFT*3)
        horizontal_line = Line(ORIGIN, RIGHT * 2, color=BLACK).shift(LEFT*3)

        # Position the lines at the center
        vertical_line.move_to(circle.get_center())
        horizontal_line.move_to(circle.get_center())

        label_1 = Text("1", color=BLACK).move_to(UP * 0.5 + LEFT * 0.5 + LEFT*3)
        label_2 = Text("2", color=BLACK).move_to(UP * 0.5 + RIGHT * 0.5 + LEFT*3)
        label_3 = Text("3", color=BLACK).move_to(DOWN * 0.5 + LEFT * 0.5 + LEFT*3)
        label_4 = Text("4", color=BLACK).move_to(DOWN * 0.5 + RIGHT * 0.5 + LEFT*3)

        self.play(Create(circle), Create(vertical_line), Create(horizontal_line))  # show the circle and lines on screen
        self.play(Write(label_1), Write(label_2), Write(label_3), Write(label_4))  # show the labels on screen

        quarter_1 = Sector(outer_radius=1, start_angle=PI / 2, angle=PI / 2, color=GREEN, fill_opacity=0.5).shift(LEFT*3)

        self.play(Create(quarter_1)) 
        fraction = Tex(r"$\frac{1}{4}$", font_size=96).shift(RIGHT*3)
        self.play(Write(fraction))

        arrow_to_fraction = Arrow(circle.get_right(), fraction, color=WHITE)

        self.play(Create(arrow_to_fraction))
    def Example4(self):
        rect = Rectangle(width=7, height=1, color=WHITE, stroke_width=2).shift(LEFT * 3)
        lines = VGroup(*[Line(start=rect.get_corner(DL) + RIGHT * i, end=rect.get_corner(UL) + RIGHT * i) for i in range(1, 6)])

        shaded_rect1 = Rectangle(width=1, height=1, color=BLUE, fill_opacity=0.5).move_to(rect.get_center() + RIGHT * 2 )
        shaded_rect2 = Rectangle(width=1, height=1, color=BLUE, fill_opacity=0.5).move_to(rect.get_center() +  RIGHT * 3)

        # Create fraction
        fraction = MathTex(r"\frac{2}{7}", font_size=96).shift(RIGHT*5)

        arrow_to_fraction = Arrow(shaded_rect2.get_right(), fraction.get_left(), color=WHITE)

        self.play(Create(rect))
        self.play(Create(lines))
        self.play(Create(shaded_rect1), Create(shaded_rect2))
        self.play(Write(fraction))
        self.play(Create(arrow_to_fraction))

    def ImproperFraction(self):
        p10=cvo.CVO().CreateCVO("Improper Fractions","").setPosition([-2,2.5,0])
        p11=cvo.CVO().CreateCVO(" Form ", r"$\frac{p}{q}$").setPosition([0,1,0])
        p12=cvo.CVO().CreateCVO("Rule ", "$p \geq q$").setPosition([3,0,0])
        p13=cvo.CVO().CreateCVO("Example",  r"$\frac{6}{5}$").setPosition([-3,-1.5,0])

        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
        self.construct1(p10,p10)
    
    def ImproperExp1(self):
        examples_title = Text("Improper Fractions Examples ", font_size=30).to_edge(UP)
        self.play(Write(examples_title))
        circle = Circle(fill_color=PINK, fill_opacity=1).shift(LEFT*4)  # create a circle and move it to the left
        # Create vertical and horizontal lines
        vertical_line = Line(ORIGIN, UP * 2, color=BLACK).shift(LEFT*3)
        horizontal_line = Line(ORIGIN, RIGHT * 2, color=BLACK).shift(LEFT*3)

        # Position the lines at the center
        vertical_line.move_to(circle.get_center())
        horizontal_line.move_to(circle.get_center())

        self.play(Create(circle), Create(vertical_line), Create(horizontal_line))
        # Indicate the fraction 3/4
        arc_1 = Sector(radius=2.5, start_angle=5 * PI / 2, angle=PI / 2, color=PINK).shift(LEFT*1)
        self.play(Create(arc_1))
        sector = Sector(radius=2, start_angle=PI/2, angle=PI/2, color=BLUE, fill_opacity=0.5).shift(RIGHT*1)
        self.play(Create(sector))



        fraction = Tex(r"$\frac{6}{4}$", font_size=96).shift(RIGHT*5)
        self.play(Write(fraction))

        # Create arrow from circle to fraction
        arrow_to_fraction = Arrow(sector.get_bottom(), fraction, color=WHITE)

        self.play(Create(arrow_to_fraction))
    
    def ImproperExp2(self):
        circle = Circle(radius=1, fill_color=BLUE, fill_opacity=0.5).shift(LEFT * 4)
        self.play(Create(circle))

        # Create the sectors and the dividing lines
        sectors = VGroup()
        lines = VGroup()

        for i in range(6):
            start_angle = i * PI / 3
            end_angle = (i + 1) * PI / 3

            # Create each sector
            sector = Sector(radius=1, start_angle=start_angle, angle=PI / 3, color=BLUE, fill_opacity=0.5).shift(LEFT * 4)
            sectors.add(sector)

            # Create each dividing line
            line = Line(circle.get_center(), circle.point_at_angle(start_angle), color=BLACK)
            lines.add(line)

        self.play(Create(sectors), Create(lines))

        # Add vertical and horizontal lines
        vertical_line = Line(circle.get_top(), circle.get_bottom(), color=BLACK).shift(LEFT * 4)
        horizontal_line = Line(circle.get_left(), circle.get_right(), color=BLACK).shift(LEFT * 4)

        self.play(Create(vertical_line), Create(horizontal_line))

        sector1 = Sector(radius=2.5, start_angle=5 * PI / 2, angle=PI / 2, color=BLUE).shift(LEFT*1)
        self.play(Create(sector1))
        sector2 = Sector(radius=2, start_angle=PI/2, angle=PI/2, color=BLUE).shift(RIGHT*1)
        self.play(Create(sector2))


        # Indicate the fraction 6/4
        fraction = Tex(r"$\frac{8}{6}$", font_size=96).shift(RIGHT * 5)
        self.play(Write(fraction))

        # Create an arrow from the circle to the fraction
        arrow_to_fraction = Arrow(sector2.get_bottom(), fraction, color=WHITE)
        self.play(Create(arrow_to_fraction))

    def ImproperExp3(self):
        # Create a circle and move it to the left
        circle = Circle(radius=1, fill_color=BLUE, fill_opacity=0.5).shift(LEFT * 4)
        self.play(Create(circle))

        # Create the dividing lines
        lines = VGroup()
        for i in range(3):
            angle = i * 2 * PI / 3
            line = Line(circle.get_center(), circle.point_at_angle(angle), color=YELLOW)
            lines.add(line)

        self.play(Create(lines))

        # Create a sector to highlight one part
        #sector = Sector(outer_radius=1, angle=2 * PI / 3, start_angle=0, color=GREEN, fill_opacity=0.5).shift(LEFT * 4)
        #self.play(Create(sector))

        # Add boundaries to the sector
        sector_boundary_lines = VGroup(
            Line(circle.get_center(), circle.point_at_angle(0), color=RED).shift(LEFT * 4),
            Line(circle.get_center(), circle.point_at_angle(2 * PI / 3), color=RED).shift(LEFT * 4)
            
        )
        
        
        self.play(Create(sector_boundary_lines))
        sector1 = Sector(radius=2.5, start_angle=5 * PI / 2, angle=PI / 2, fill_color=BLUE, fill_opacity=0.5).shift(LEFT*1)
        self.play(Create(sector1))
        # Indicate the fraction 1/3
        fraction = MathTex(r"\frac{4}{3}", font_size=96).shift(RIGHT * 5)
        self.play(Write(fraction))

        # Create an arrow from the circle to the fraction
        arrow_to_fraction = Arrow(sector1.get_bottom(), fraction, color=WHITE)
        self.play(Create(arrow_to_fraction))
    def MixedFractions(self):
        p10=cvo.CVO().CreateCVO("Mixed Fractions ","").setPosition([-2,2.5,0])
        #p11=cvo.CVO().CreateCVO("Defination  ", "A fraction that has both a whole number and a fractional part").setPosition([0,1,0])
        p12=cvo.CVO().CreateCVO("Example",r"$(2\frac{3}{4})$").setPosition([0,1,0])
        p13=cvo.CVO().CreateCVO("Whole Number ", "$2$").setPosition([3,0,0])
        p14=cvo.CVO().CreateCVO("Fraction Part  ", r"$\frac{3}{4}$").setPosition([-3,-1.5,0])

       
        #p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p12.cvolist.append(p13)
        p12.cvolist.append(p14)
        self.construct1(p10,p10)
    def MixedFractionExp1(self):
        # Create circles
        circle1 = Circle(radius=1, fill_color=BLUE, fill_opacity=1).shift(LEFT * 4)
        circle2 = Circle(radius=1, fill_color=BLUE, fill_opacity=1).shift(LEFT * 1)

        # Get centers of circles
        center_circle1 = circle1.get_center()
        center_circle2 = circle2.get_center()
        
        # Calculate endpoints for the vertical line within circle1
        start_point1 = center_circle1 + UP * 1  # Start slightly above the center
        end_point1 = center_circle1 + DOWN * 1  # End slightly below the center

        # Calculate endpoints for the vertical line within circle2
        start_point2 = center_circle2 + UP * 1  # Start slightly left of the center
        end_point2 = center_circle2 + DOWN * 1  # End slightly right of the center

        # Create vertical lines inside circles
        vertical_line1 = Line(start=start_point1, end=end_point1, color=BLACK)
        vertical_line2 = Line(start=start_point2, end=end_point2, color=BLACK)

        # Create an arc
        arc = Arc(radius=1, start_angle=PI/2, angle=PI, fill_color=BLUE, fill_opacity=1).shift(RIGHT * 2)
        fraction = Tex(r"$2\frac{1}{2}$", font_size=80).shift(RIGHT*5)
        

        arrow_to_fraction = Arrow(arc.get_center(), fraction, color=WHITE)

       
        # Show animations
        self.play(Create(circle1))
        self.play(Create(vertical_line1))
        self.play(Create(circle2))
        self.play(Create(vertical_line2))
        self.play(Create(arc))
        self.play(Write(fraction))
        self.play(Create(arrow_to_fraction))
    def MixedFractionExp2(self):
        # Create a circle and move it to the left
        circle = Circle(radius=1, fill_color=BLUE, fill_opacity=0.5).shift(LEFT * 4)
        self.play(Create(circle))

        # Create the dividing lines for the circle
        lines = VGroup()
        for i in range(3):
            angle = i * 2 * PI / 3
            line = Line(circle.get_center(), circle.point_at_angle(angle), color=YELLOW)
            lines.add(line)

        self.play(Create(lines))

        # Create two sectors with 120 degrees each
        radius = 1
        angle = 120 * DEGREES  # Convert degrees to radians

        sector1 = Sector(radius=radius, angle=angle, fill_color=BLUE, fill_opacity=0.5).shift(LEFT * 1)
        sector2 = Sector(radius=radius, angle=angle, start_angle=angle, fill_color=BLUE, fill_opacity=0.5).shift(LEFT * 1)

        self.play(Create(sector1))
        self.play(Create(sector2))

        # Create the dividing lines for the sectors
        sector_lines = VGroup()
        sector_angles = [0, 120 * DEGREES, 240 * DEGREES]
        for sector in [sector1, sector2]:
            center = LEFT*1
            for angle in sector_angles:
                # Update the calculation for the end point
                end_point = center + radius * np.array([np.cos(angle), np.sin(angle), 0])
                line = Line(center, end_point, color=YELLOW)
                sector_lines.add(line)

        self.play(Create(sector_lines))

        # Indicate the fraction 1/3
        fraction = Tex(r"$1\frac{2}{3}$", font_size=96).shift(RIGHT * 5)
        self.play(Write(fraction))

        # Create an arrow from sector2 to the fraction
        arrow_to_fraction = Arrow(sector1.get_bottom(), fraction.get_center(), color=WHITE)
        self.play(Create(arrow_to_fraction))
    def NumberLineExp1(self):
        # Title
        examples_title = Text("Fractions on Number Line", font_size=40).to_edge(UP)
        self.play(Write(examples_title))
        
        # Fraction heading
        fraction_heading = MathTex("Example 1: ", r"\frac{7}{6}", font_size=36).to_edge(UP*3 + LEFT)
        self.play(Write(fraction_heading))
        
        # Create NumberLine
        number_line = NumberLine(
            x_range=[0, 1.5, 0.16],
            length=10,
            color=BLUE,
            include_numbers=True,
            label_direction=DOWN,
            font_size=36
        )

        # Fractions to add
        fractions = {
            0.16: r"\frac{1}{6}",
            0.32: r"\frac{2}{6}",
            0.48: r"\frac{3}{6}",
            0.64: r"\frac{4}{6}",
            0.80: r"\frac{5}{6}",
            0.96: r"\frac{6}{6}",
            1.12: r"\frac{7}{6}",
            1.28: r"\frac{8}{6}",
            1.44: r"\frac{9}{6}"
        }

        # Create labels for fractions
        fraction_labels = VGroup()
        for number, label_tex in fractions.items():
            label = MathTex(label_tex, font_size=24).move_to(number_line.number_to_point(number) + UP * 0.5)
            fraction_labels.add(label)
        highlight_rect = Rectangle(width=1, height=1.5, color=RED, fill_opacity=0.3).move_to(number_line.number_to_point(1.12))

        # Animation sequence
        self.play(Create(number_line))
        self.play(Create(fraction_labels))
        self.play(Create(highlight_rect))
    def NumberLineExp2(self):
        # Fraction heading
        fraction_heading = MathTex("Example 2: ", r"\frac{5}{2}", font_size=36).to_edge(UP*3 + LEFT)
        self.play(Write(fraction_heading))
        
        # Create NumberLine
        number_line = NumberLine(
            x_range=[0, 3, 0.5],
            length=10,
            color=BLUE,
            include_numbers=True,
            label_direction=DOWN,
            font_size=36
        )

        # Fractions to add
        fractions = {
            0.5: r"\frac{1}{2}",
            1.0: r"\frac{2}{2}",
            1.5: r"\frac{3}{2}",
            2.0: r"\frac{4}{2}",
            2.5: r"\frac{5}{2}"
            
        }

        # Create labels for fractions
        fraction_labels = VGroup()
        for number, label_tex in fractions.items():
            label = MathTex(label_tex, font_size=24).move_to(number_line.number_to_point(number) + UP * 0.5)
            fraction_labels.add(label)
        highlight_rect = Rectangle(width=1, height=1.5, color=RED, fill_opacity=0.2).move_to(number_line.number_to_point(2.5))

        # Animation sequence
        self.play(Create(number_line))
        self.play(Create(fraction_labels))
        self.play(Create(highlight_rect))

       
    

if __name__ == "__main__":
    scene = FractionIntro()
    scene.render()
