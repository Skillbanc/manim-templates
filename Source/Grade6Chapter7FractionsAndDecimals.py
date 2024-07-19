import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo

class Grade6Chapter7FractionsAndDecimalsAnim(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.Intro()
        self.fadeOutCurrentScene()
        self.Definition()
        self.fadeOutCurrentScene()
        self.CircleExample()
        self.fadeOutCurrentScene()
        self.CircleExample2()
        self.fadeOutCurrentScene()
        self.CircleExample3()
        self.fadeOutCurrentScene()
        self.RectangleExample()
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
        self.fadeOutCurrentScene()
        self.EquiExp()
        self.Example1()
        self.Equall1()
        self.Example2()
        self.Equall2()
        self.Example3()
        self.Equall3()
        self.Example4()
        self.fadeOutCurrentScene()
        self.StanderdForm()
        self.fadeOutCurrentScene()
        self.NonStanderd()
        self.fadeOutCurrentScene()
        self.LikeFractions()
        self.fadeOutCurrentScene()
        self.UnLikeFractions()
        self.fadeOutCurrentScene()
        self.AscendingOrder()
        self.fadeOutCurrentScene()
        self.DesendingOrder()
        self.fadeOutCurrentScene()
        self.AdditionOfFractions()
        self.AddSymbol()
        self.AddOfFractionExp2()
        self.EquallSym()
        self.AddOfFractionExp3()
        self.fadeOutCurrentScene()
        self.AddCircel1()
        self.AdditionSymbol()
        self.AddCircel2()
        self.EquallSymbol()
        self.AddCircleFinal()
        self.fadeOutCurrentScene()
        self.AdditionOfUnlike()
        self.fadeOutCurrentScene()
        self.SubOfFractions()
        self.fadeOutCurrentScene()
        self.Decimals()
        self.fadeOutCurrentScene()
        self.DecimalsAddition()
        self.fadeOutCurrentScene()
        self.DecimalsSubstraction()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

    def SetDeveloperList(self):  
        self.DeveloperList = "Mukthanand Reddy"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName = "Grade6Chapter7Frac.py"
         

    def Intro(self):
        title = Text("Fractions and Decimals", font_size=72)
        self.play(FadeIn(title, shift=UP))
        self.wait(0.5)
        self.play(FadeOut(title))

    def Definition(self):
        self.isRandom= False
        p10 = cvo.CVO().CreateCVO("Fractions", "").setPosition([-4, 0, 0]).setangle(-TAU/4)
        p11 = cvo.CVO().CreateCVO("Definition", "A fraction represents a part of a whole").setPosition([4,2, 0]).setangle(-TAU/4)
        p12 = cvo.CVO().CreateCVO("Fraction Form", "$(p/q)$").setPosition([4,-2 , 0]).setangle(-TAU/4)
        #p13 = cvo.CVO().CreateCVO(r"$\frac{p}{q}$", "").setPosition([-4, -2, 0]).setangle(-TAU/3)
       # p14 = cvo.CVO().CreateCVO("Numerator", "p").setPosition([3,2,0]).setangle(-TAU/4)
       # p15 = cvo.CVO().CreateCVO("Denominator", "q").setPosition([3,-1,0]).setangle(-TAU/2)
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        #p12.cvolist.append(p14)
       # p12.cvolist.append(p15)
       # p13.cvolist.append(p15)
        self.construct1(p10, p10)




    def CircleExample(self):
        examples_title = MathTex("Example 1: ", r"\frac{3}{4}", font_size=36).to_edge(UP*3 + LEFT)
        self.wait(1)
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

        self.play(Create(circle) )
        self.wait(1)
        self.play(Create(vertical_line))
        self.wait(1)
        self.play(Create(horizontal_line))
        self.wait(1)
          
        self.play(Write(label_1) )
        self.play(Write(label_2))
        self.play(Write(label_3))
        self.play( Write(label_4))



        # Shade quarters 1, 2, and 3 in green
        quarter_1 = Sector(outer_radius=1, start_angle=PI / 2, angle=PI / 2, color=GREEN, fill_opacity=0.5).shift(LEFT*3)
        quarter_2 = Sector(outer_radius=1, start_angle=0, angle=PI / 2, color=GREEN, fill_opacity=0.5).shift(LEFT*3)
        quarter_3 = Sector(outer_radius=1, start_angle=PI, angle=PI / 2, color=GREEN, fill_opacity=0.5).shift(LEFT*3)

        self.play(Create(quarter_1) )  # show the shaded quarters
        self.play( Create(quarter_2))
        self.play(Create(quarter_3))


        self.wait(1) 
        # Indicate the fraction 3/4
        fraction = Tex(r"$\frac{3}{4}$", font_size=96).shift(RIGHT*3)

        # Create arrow from circle to fraction
        arrow_to_fraction = Arrow(circle.get_right(), fraction, color=WHITE)

        self.play(Create(arrow_to_fraction))
        self.wait(1)
        self.play(Write(fraction))
        self.wait(2)
        
    def CircleExample2(self):
        examples_title = MathTex("Example 2: ", r"\frac{1}{3}", font_size=36).to_edge(UP*3 + LEFT)
        
        self.play(Write(examples_title))
        self.wait(1)
        circle = Circle(radius=1, fill_color=BLUE, fill_opacity=0.5).shift(LEFT * 4)
        self.play(Create(circle))

        # Create the dividing lines
        lines = VGroup()
        for i in range(3):
            angle = i * 2 * PI / 3
            line = Line(circle.get_center(), circle.point_at_angle(angle), color=YELLOW)
            lines.add(line)

        self.play(Create(lines))
        self.wait(1)

        label_1 = Text("1", color=BLACK).move_to(DOWN * 0.2 + LEFT * 4.5)
        label_2 = Text("2", color=BLACK).move_to(UP * 0.5 + LEFT * 0.5 + LEFT*3)
        label_3 = Text("3", color=BLACK).move_to(DOWN * 0.5 + LEFT * 0.5 + LEFT*3)
        
        self.play(Write(label_1) )
        self.play(Write(label_2))
        self.play(Write(label_3))
        # Create a sector to highlight one part
        sector = Sector(outer_radius=1, angle=2 * PI / 3, start_angle=0, color=GREEN, fill_opacity=0.5).shift(LEFT * 4)
        self.play(Create(sector))

        # Add boundaries to the sector
        sector_boundary_lines = VGroup(
            Line(circle.get_center(), circle.point_at_angle(0), color=RED).shift(LEFT * 4),
            Line(circle.get_center(), circle.point_at_angle(2 * PI / 3), color=RED).shift(LEFT * 4)
        )
        #self.play(Create(sector_boundary_lines))
        # Indicate the fraction 1/3
        fraction = MathTex(r"\frac{1}{3}", font_size=96).shift(RIGHT * 5)
        
        # Create an arrow from the circle to the fraction
        arrow_to_fraction = Arrow(circle.get_right(), fraction, color=WHITE)
        self.play(Create(arrow_to_fraction))
        self.wait(1)
        self.play(Write(fraction))
        self.wait(2)
    
    def CircleExample3(self):
        examples_title = MathTex("Example 3: ", r"\frac{1}{4}", font_size=36).to_edge(UP*3 + LEFT)
        
        self.play(Write(examples_title))
        self.wait(1)
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

        self.play(Create(circle))  # show the circle and lines on screen
        self.play( Create(vertical_line))
        self.play(Create(horizontal_line))
        self.wait(1)
       
        self.play(Write(label_1))  # show the labels on screen
        self.play( Write(label_2))
        self.play( Write(label_3))
        self.play( Write(label_4))
        quarter_1 = Sector(outer_radius=1, start_angle=PI / 2, angle=PI / 2, color=GREEN, fill_opacity=0.5).shift(LEFT*3)
        self.wait(1)
        self.play(Create(quarter_1)) 
        self.wait(1)
        fraction = Tex(r"$\frac{1}{4}$", font_size=96).shift(RIGHT*3)
        

        arrow_to_fraction = Arrow(circle.get_right(), fraction, color=WHITE)

        self.play(Create(arrow_to_fraction))
        self.wait(1)
        self.play(Write(fraction))
        self.wait(2)

    
    def RectangleExample(self):
        examples_title = MathTex("Example 4: ", r"\frac{2}{7}", font_size=36).to_edge(UP*3 + LEFT)
        
        self.play(Write(examples_title))
        self.wait(1)
        rect = Rectangle(width=7, height=1, color=WHITE, stroke_width=2).shift(LEFT * 3)
        lines = VGroup(*[Line(start=rect.get_corner(DL) + RIGHT * i, end=rect.get_corner(UL) + RIGHT * i) for i in range(1, 7)])

        shaded_rect1 = Rectangle(width=1, height=1, color=YELLOW, fill_opacity=0.5).move_to(rect.get_center() + RIGHT * 2 )
        shaded_rect2 = Rectangle(width=1, height=1, color=YELLOW, fill_opacity=0.5).move_to(rect.get_center() +  RIGHT * 3)

        # Create fraction
        fraction = MathTex(r"\frac{2}{7}", font_size=96).shift(RIGHT*5)

        arrow_to_fraction = Arrow(shaded_rect2.get_right(), fraction.get_left(), color=WHITE)
        label_1 = Text("1", color=BLUE).move_to(rect.get_corner(UL) + RIGHT * 0.5).shift(DOWN*0.5)
        label_2 = Text("2", color=BLUE).move_to(rect.get_corner(UL) + RIGHT * 1.5).shift(DOWN*0.5)
        label_3 = Text("3", color=BLUE).move_to(rect.get_corner(UL) + RIGHT * 2.5).shift(DOWN*0.5)
        label_4 = Text("4", color=BLUE).move_to(rect.get_corner(UL) + RIGHT * 3.5).shift(DOWN*0.5)
        label_5 = Text("5", color=BLUE).move_to(rect.get_corner(UL) + RIGHT * 4.5).shift(DOWN*0.5)
        label_6 = Text("6", color=BLUE).move_to(rect.get_corner(UL) + RIGHT * 5.5).shift(DOWN*0.5)
        label_7 = Text("7", color=BLUE).move_to(rect.get_corner(UL) + RIGHT * 6.5).shift(DOWN*0.5)


        self.play(Create(rect))
        self.play(Create(lines))
        self.wait(1)
        self.play(FadeIn(label_1))
        self.play(FadeIn(label_2))
        self.play(FadeIn(label_3))
        self.play(FadeIn(label_4))
        self.play(FadeIn(label_5))
        self.play(FadeIn(label_6))
        self.play(FadeIn(label_7))
        self.wait(1)
        self.play(Create(shaded_rect1))
        self.wait(1.5)
        self.play( Create(shaded_rect2))
        self.wait(1)
        self.play(Create(arrow_to_fraction))
        self.wait(1)
        
        
        self.play(Write(fraction))
        self.wait(2)
        


    def ImproperFraction(self):  
        self.isRandom = False
        self.angleChoice = [TAU/2,TAU/4]
        p10=cvo.CVO().CreateCVO("Improper Fractions","").setPosition([-4,2,0])
        p11=cvo.CVO().CreateCVO( r" Is $\frac{p}{q}$" ,"Yes" ).setPosition([-4,-2,0])
        p12=cvo.CVO().CreateCVO("Condition ", "$p \geq q$").setPosition([3,2,0])
        #p13=cvo.CVO().CreateCVO("Example",  r"$\frac{6}{5}$").setPosition([5,0.5,0]).setangle(-TAU/4)
       # p10.setcircleradius(1.5)
       # p11.setcircleradius(1.5)
       # p12.setcircleradius(1.5)
        #p13.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        #p11.cvolist.append(p13)
        self.construct1(p10,p10)
    def ImproperExp1(self):
        examples_title = Text("Improper Fractions Examples ", font_size=30).to_edge(UP)
        self.play(Write(examples_title))
        self.wait(1)
        circle = Circle(fill_color=PINK, fill_opacity=1).shift(LEFT*4)  # create a circle and move it to the left
        # Create vertical and horizontal lines
        vertical_line = Line(ORIGIN, UP * 2, color=BLACK).shift(LEFT*3)
        horizontal_line = Line(ORIGIN, RIGHT * 2, color=BLACK).shift(LEFT*3)

        # Position the lines at the center
        vertical_line.move_to(circle.get_center())
        horizontal_line.move_to(circle.get_center())

        self.play(Create(circle))
        self.wait(1)
        self.play( Create(vertical_line))
        self.play(Create(horizontal_line))
        
        
        self.wait(1)
        # Indicate the fraction 3/4
        arc_1 = Sector(radius=2.5, start_angle=5 * PI / 2, angle=PI / 2, color=PINK).shift(LEFT*1)
        self.play(Create(arc_1))
        self.wait(1)
        sector = Sector(radius=2, start_angle=PI/2, angle=PI/2, color=PINK).shift(RIGHT*1)
        self.play(Create(sector))
        self.wait(1)

        fraction = Tex(r"$\frac{6}{4}$", font_size=96).shift(RIGHT*5)
        
        # Create arrow from circle to fraction
        arrow_to_fraction = Arrow(sector.get_bottom(), fraction, color=WHITE)

        self.play(Create(arrow_to_fraction))
        self.wait(1)
        self.play(Write(fraction))
        self.wait(2)
    
    def ImproperExp2(self):
        examples_title = MathTex("Example 2: ", r"\frac{8}{6}", font_size=36).to_edge(UP*3 + LEFT)
        
        self.play(Write(examples_title))
        self.wait(1)
        circle = Circle(radius=1, fill_color=BLUE, fill_opacity=0.5).shift(LEFT * 4)
        self.play(Create(circle))
        self.wait(1)
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
        
        self.play(Create(lines))
        self.wait(1)
        self.play(Create(sectors))

        # Add vertical and horizontal lines
        vertical_line = Line(circle.get_top(), circle.get_bottom(), color=BLACK).shift(LEFT * 4)
        horizontal_line = Line(circle.get_left(), circle.get_right(), color=BLACK).shift(LEFT * 4)

        self.play(Create(vertical_line))
        self.play(Create(horizontal_line))

        sector1 = Sector(radius=2.5, start_angle=5 * PI / 2, angle=PI / 2, color=BLUE).shift(LEFT*1)
        self.play(Create(sector1))
        self.wait(1)
        sector2 = Sector(radius=2, start_angle=PI/2, angle=PI/2, color=BLUE).shift(RIGHT*1)
        self.play(Create(sector2))
        self.wait(1)


        # Indicate the fraction 6/4
        fraction = Tex(r"$\frac{8}{6}$", font_size=96).shift(RIGHT * 5)
        

        # Create an arrow from the circle to the fraction
        arrow_to_fraction = Arrow(sector2.get_bottom(), fraction, color=WHITE)
        self.play(Create(arrow_to_fraction))
        self.wait(1)
        self.play(Write(fraction))
        self.wait(2)

    def ImproperExp3(self):
        examples_title = MathTex("Example 3: ", r"\frac{4}{3}", font_size=36).to_edge(UP*3 + LEFT)
        
        self.play(Write(examples_title))
        self.wait(1)
        # Create a circle and move it to the left
        circle = Circle(radius=1, fill_color=BLUE, fill_opacity=0.5).shift(LEFT * 4)
        self.play(Create(circle))
        self.wait(1)

        # Create the dividing lines
        lines = VGroup()
        for i in range(3):
            angle = i * 2 * PI / 3
            line = Line(circle.get_center(), circle.point_at_angle(angle), color=YELLOW)
            lines.add(line)

        self.play(Create(lines))
        self.wait(1)

        sector_boundary_lines = VGroup(
            Line(circle.get_center(), circle.point_at_angle(0), color=RED).shift(LEFT * 4),
            Line(circle.get_center(), circle.point_at_angle(2 * PI / 3), color=RED).shift(LEFT * 4)
            
        )
        
        
        #self.play(Create(sector_boundary_lines))
        sector1 = Sector(radius=2.5, start_angle=5 * PI / 2, angle=PI / 2, fill_color=BLUE, fill_opacity=0.5).shift(LEFT*1)
        self.play(Create(sector1))
        self.wait(1)
        # Indicate the fraction 1/3
        fraction = MathTex(r"\frac{4}{3}", font_size=96).shift(RIGHT * 5)
        

        # Create an arrow from the circle to the fraction
        arrow_to_fraction = Arrow(sector1.get_bottom(), fraction, color=WHITE)
        self.play(Create(arrow_to_fraction))
        self.wait(1)
        self.play(Write(fraction))
        self.wait(2)


    def MixedFractions(self):
        self.isRandom = False
        self.angleChoice=[TAU/2,TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Mixed Fractions ","").setPosition([-4,2,0])
        #p11=cvo.CVO().CreateCVO("Defination  ", "A fraction that has both a whole number and a fractional part").setPosition([0,1,0])
        p12=cvo.CVO().CreateCVO("Example",r"$(2\frac{3}{4})$").setPosition([-4,-2,0])
        p13=cvo.CVO().CreateCVO("Whole Number ", "$2$").setPosition([1,2,0])
        p14=cvo.CVO().CreateCVO("Fraction Part  ", "$(3/4)$").setPosition([5,2,0])
        
        p10.setcircleradius(1.5)
        p12.setcircleradius(1.5)
        p13.setcircleradius(1.5)
        p14.setcircleradius(1.5)
       
        #p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p12.cvolist.append(p13)
        p12.cvolist.append(p14)
        self.construct1(p10,p10)
    


    def MixedFractionExp1(self):
        title = Text(" Mixed Fractions Examples", font_size=36).to_edge(UP)
        self.play(Write(title))
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
        

        arrow_to_fraction = Arrow(arc.get_center(), fraction.get_left(), color=WHITE)

       
        # Show animations
        self.play(Create(circle1))
        self.wait(1)
        self.play(Create(vertical_line1))
        self.wait(1)
        self.play(Create(circle2))
        self.wait(1)
        self.play(Create(vertical_line2))
        self.wait(1)
        self.play(Create(arc))
        self.wait(1)
        self.play(Create(arrow_to_fraction))
        self.wait(1)
        self.play(Write(fraction))
        self.wait(2)
    def MixedFractionExp2(self):
        examples_title = MathTex("Example 2: ", font_size=36).to_edge(UP*3 + LEFT)
        
        self.play(Write(examples_title))
        # Create a circle and move it to the left
        circle = Circle(radius=1, fill_color=BLUE, fill_opacity=0.5).shift(LEFT * 4)
        self.wait(1)
        self.play(Create(circle))

        # Create the dividing lines for the circle
        lines = VGroup()
        for i in range(3):
            angle = i * 2 * PI / 3
            line = Line(circle.get_center(), circle.point_at_angle(angle), color=YELLOW)
            lines.add(line)
        self.wait(1)
        self.play(Create(lines))

        # Create two sectors with 120 degrees each
        radius = 1
        angle = 120 * DEGREES  # Convert degrees to radians

        sector1 = Sector(radius=radius, angle=angle, fill_color=BLUE, fill_opacity=0.5).shift(LEFT * 1)
        sector2 = Sector(radius=radius, angle=angle, start_angle=angle, fill_color=BLUE, fill_opacity=0.5).shift(LEFT * 1)

        self.play(Create(sector1))
        self.wait(1)
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
        self.wait(1)
        self.play(Create(sector_lines))
        self.wait(1)
        # Indicate the fraction 1/3
        fraction = Tex(r"$1\frac{2}{3}$", font_size=96).shift(RIGHT * 5.3)
        # Create an arrow from sector2 to the fraction
        arrow_to_fraction = Arrow(sector1.get_bottom(), fraction.get_left(), color=WHITE)
        self.play(Create(arrow_to_fraction))
        self.wait(1)
        self.play(Write(fraction))  
        self.wait(2)

    def NumberLineExp1(self):
        # Title
        examples_title = Text("Fractions on Number Line", font_size=40).to_edge(UP)
        self.play(Write(examples_title))
        self.wait(1)
        # Fraction heading
        fraction_heading = MathTex("Example 1: ", r"\frac{7}{6}", font_size=36).to_edge(UP*3 + LEFT)
        self.play(Write(fraction_heading))
        self.wait(1)
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
        highlight_rect = Rectangle(width=1, height=2, color=RED, fill_opacity=0.3).move_to(number_line.number_to_point(1.12))

        # Animation sequence
        self.play(Create(number_line))
        self.wait(1.5)
        self.play(Create(fraction_labels))
        self.wait(1.5)
        self.play(Create(highlight_rect))
        self.wait(2)


    def NumberLineExp2(self):
        # Fraction heading
        fraction_heading = MathTex("Example 2: ", r"\frac{5}{2}", font_size=36).to_edge(UP*3 + LEFT)
        self.play(Write(fraction_heading))
        self.wait(1)
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
        highlight_rect = Rectangle(width=1, height=2, color=YELLOW, fill_opacity=0.2).move_to(number_line.number_to_point(2.5))

        # Animation sequence
        self.play(Create(number_line))
        self.wait(1.5)
        self.play(Create(fraction_labels))
        self.wait(1.5)
        self.play(Create(highlight_rect))
        self.wait(2)
    
    def EquiExp(self):
        examples_title = Text("Equivalent Fractions", font_size=36).to_edge(UP)
        self.play(Write(examples_title))
    def Example1(self):
        # Define the radius of the square
        radius = 1
        
        # Create a square with the specified radius (side length will be 2 * radius)
        side_length = radius * 2
        square1 = Square(side_length=side_length)
        
        # Create vertical and horizontal lines matching the radius of the square
        vertical_line1 = Line(start=[0, -radius, 0], end=[0, radius, 0])
        horizontal_line1 = Line(start=[-radius, 0, 0], end=[radius, 0, 0])

        # Group all elements of square1
        group1 = VGroup(square1, vertical_line1, horizontal_line1)

        # Create a polygon to shade one quarter of square1
        shaded_area1 = Polygon(
            [0, 0, 0], [0, radius, 0], [radius, radius, 0], [radius, 0, 0],
            fill_opacity=0.5, fill_color=BLUE
        )
        
        # Add the shaded area to group1
        group1.add(shaded_area1)
        
        # Shift square1 to its position
        group1.shift(LEFT * 4)

        # Add group1 to the scene
        self.play(Create(square1))
        self.play( Create(vertical_line1))
        self.play(Create(horizontal_line1))
        self.play(Create(shaded_area1))
        # Create the text "1/4" and position it below square1
        text1 = Tex(r"$\frac{1}{4}$")
        text1.shift(DOWN * 2 + LEFT * 4)
        
        # Add text1 to the scene
        self.play(Write(text1))
        self.wait(1.5)
    def Equall1(self):
        equals_signs = Tex("=").scale(1.5).shift(UP*0.1+LEFT*2.5)
        self.play(Write(equals_signs))
        self.wait(1)
    def Example2(self):
        # Define the radius of the square
        radius = 1
        
        # Create a square with the specified radius (side length will be 2 * radius)
        side_length = radius * 2
        square2 = Square(side_length=side_length)
        
        # Create vertical and horizontal lines matching the radius of the square
        vertical_lines2 = VGroup(
            Line(start=[-radius / 2, -radius, 0], end=[-radius / 2, radius, 0]),
            Line(start=[0, -radius, 0], end=[0, radius, 0]),
            Line(start=[radius / 2, -radius, 0], end=[radius / 2, radius, 0])
        )
        horizontal_line2 = Line(start=[-radius, 0, 0], end=[radius, 0, 0])

        # Group all elements of square2
        group2 = VGroup(square2, vertical_lines2, horizontal_line2)

        # Create polygons to shade two quarters of square2
        shaded_area2_1 = Polygon(
            [0, 0, 0], [0, radius, 0], [radius / 2, radius, 0], [radius / 2, 0, 0],
            fill_opacity=0.5, fill_color=BLUE
        )
        shaded_area2_2 = Polygon(
            [0, 0, 0], [0, -radius, 0], [radius / 2, -radius, 0], [radius / 2, 0, 0],
            fill_opacity=0.5, fill_color=BLUE
        )

        # Add shaded areas to group2
        group2.add(shaded_area2_1, shaded_area2_2)
        
        # Shift square2 to its position
        group2.shift(LEFT * 1)

        # Add group2 to the scene
        self.play(Create(square2))
        self.wait(1)
        self.play(Create(vertical_lines2))
        self.play( Create(horizontal_line2))
        # Play each shaded area separately for square2
        self.play(FadeIn(shaded_area2_1))
        self.wait(1)
        self.play(FadeIn(shaded_area2_2))
        
        # Create the text "2/8" and position it below square2
        text2 = Tex(r"$\frac{2}{8}$")
        text2.shift(DOWN * 2 + LEFT * 1)

        # Add text2 to the scene
        self.play(Write(text2))
        self.wait(1.5)
    def Equall2(self):
        equals_signs = Tex("=").scale(1.5).shift(UP*0.1+RIGHT*0.4)
        self.play(Write(equals_signs))
        self.wait(1)

    def Example3(self):
        # Define the radius of the square
        radius = 1
        
        # Number of divisions per side
        divisions_per_side = 6
        
        # Create a square with the specified radius (side length will be 2 * radius)
        side_length = radius * 2
        square3 = Square(side_length=side_length)
        
        # Calculate the step size for divisions
        step_size = side_length / divisions_per_side
        
        # Create vertical lines (5 lines) and 1 horizontal line from center
        vertical_lines3 = VGroup(*[
            Line(start=[-radius + i * step_size, -radius, 0], end=[-radius + i * step_size, radius, 0])
            for i in range(1, divisions_per_side)
        ])
        horizontal_line3 = Line(start=[-radius, 0, 0], end=[radius, 0, 0])

        # Group all elements of square3
        group3 = VGroup(square3, vertical_lines3, horizontal_line3)

        # Calculate the size of each shaded area (quarter of the step_size)
        shaded_area_size = step_size
        
        # Create polygons to shade three quarters of square3
        shaded_area3_1 = Polygon(
            [0, 0, 0], [0, radius, 0], [shaded_area_size, radius, 0], [shaded_area_size, 0, 0],
            fill_opacity=0.5, fill_color=BLUE
        )
        shaded_area3_2 = Polygon(
            [0, 0, 0], [0, -radius, 0], [shaded_area_size, -radius, 0], [shaded_area_size, 0, 0],
            fill_opacity=0.5, fill_color=BLUE
        )
        shaded_area3_3 = Polygon(
            [0, 0, 0], [0, radius, 0], [-shaded_area_size, radius, 0], [-shaded_area_size, 0, 0],
            fill_opacity=0.5, fill_color=BLUE
        )

        # Add shaded areas to group3
        group3.add(shaded_area3_1, shaded_area3_2, shaded_area3_3)
        
        # Shift square3 to its position
        group3.shift(RIGHT * 2)

        # Add group3 to the scene
        self.play(Create(square3))
        self.wait(1)
        self.play(Create(vertical_lines3))
        self.play(Create(horizontal_line3))
        
        # Play each shaded area separately for square3
        self.play(FadeIn(shaded_area3_1))
        self.play(FadeIn(shaded_area3_2))
        self.play(FadeIn(shaded_area3_3))
        
        # Create the text "3/12" and position it below square3
        text3 = Tex(r"$\frac{3}{12}$")
        text3.shift(DOWN * 2 + RIGHT * 2)  # Adjusted position

        # Add text3 to the scene
        self.play(Write(text3))
        self.wait(1)
    def Equall3(self):
        equals_signs = Tex("=").scale(1.5).shift(UP*0.1+RIGHT*3.5)
        self.play(Write(equals_signs))
        self.wait(1)
    def Example4(self):
        # Define the radius of the square
        radius = 1
        
        # Number of divisions per side
        divisions_per_side = 4
        
        # Create a square with the specified radius (side length will be 2 * radius)
        side_length = radius * 2
        square4 = Square(side_length=side_length)
        
        # Calculate the step size for divisions
        step_size = side_length / divisions_per_side
        
        # Create vertical and horizontal lines (3 lines each)
        vertical_lines4 = VGroup(*[
            Line(start=[-radius + i * step_size, -radius, 0], end=[-radius + i * step_size, radius, 0])
            for i in range(1, divisions_per_side)
        ])
        horizontal_lines4 = VGroup(*[
            Line(start=[-radius, -radius + i * step_size, 0], end=[radius, -radius + i * step_size, 0])
            for i in range(1, divisions_per_side)
        ])

        # Group all elements of square4
        group4 = VGroup(square4, vertical_lines4, horizontal_lines4)

        # Calculate the size of each shaded area
        shaded_area_size = step_size

        # Create polygons to shade four quarters of square4
        shaded_area4_1 = Polygon(
            [0, 0, 0], [0, shaded_area_size, 0], [shaded_area_size, shaded_area_size, 0], [shaded_area_size, 0, 0],
            fill_opacity=0.5, fill_color=BLUE
        )
        shaded_area4_2 = Polygon(
            [0, 0, 0], [0, -shaded_area_size, 0], [shaded_area_size, -shaded_area_size, 0], [shaded_area_size, 0, 0],
            fill_opacity=0.5, fill_color=BLUE
        )
        shaded_area4_3 = Polygon(
            [0, 0, 0], [0, shaded_area_size, 0], [-shaded_area_size, shaded_area_size, 0], [-shaded_area_size, 0, 0],
            fill_opacity=0.5, fill_color=BLUE
        )
        shaded_area4_4 = Polygon(
            [0, 0, 0], [0, -shaded_area_size, 0], [-shaded_area_size, -shaded_area_size, 0], [-shaded_area_size, 0, 0],
            fill_opacity=0.5, fill_color=BLUE
        )

        # Add shaded areas to group4
        group4.add(shaded_area4_1, shaded_area4_2, shaded_area4_3, shaded_area4_4)
        
        # Shift square4 to its position
        group4.shift(RIGHT * 5)

        # Add group4 to the scene
        self.play(Create(square4))
        self.wait(1)
        self.play(Create(vertical_lines4))
        self.play(Create(horizontal_lines4))
        
        # Play each shaded area separately for square4
        self.play(FadeIn(shaded_area4_1))
        self.play(FadeIn(shaded_area4_2))
        self.play(FadeIn(shaded_area4_3))
        self.play(FadeIn(shaded_area4_4))
        
        # Create the text "4/16" and position it below square4
        text4 = Tex(r"$\frac{4}{16}$")
        text4.shift(DOWN * 2 + RIGHT * 5)  # Adjusted position

        # Add text4 to the scene
        self.play(Write(text4))
        self.wait(2.5)
    def StanderdForm(self):
        self.isRandom = False
        self.angleChoice = [TAU/2,TAU/4,TAU/4]
        p10 = cvo.CVO().CreateCVO("Standard Form of Fractions", "").setPosition([-4,2,0])
        p11 = cvo.CVO().CreateCVO("Definition", "Fraction with no common factors").setPosition([-4,-2,0])
        p12 = cvo.CVO().CreateCVO("Example 1 ","$(1/3)$" ).setPosition([3,2,0])
        p13 = cvo.CVO().CreateCVO("Example 2", "$(2/3)$").setPosition([3,-1,0])
        #p14 = cvo.CVO().CreateCVO("Example 3", r"$\frac{3}{11}$").setPosition([1,-2,0])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        #p13.cvolist.append(p14)
        self.construct1(p10, p10)

    def NonStanderd(self):
        self.isRandom = False
        self.angleChoice = [TAU/2,TAU/4,TAU/4]
        p10 = cvo.CVO().CreateCVO("Non Standard Fractions", "").setPosition([-4,2,0])
        p11 = cvo.CVO().CreateCVO("Definition","Fraction not in simplest form").setPosition([-4,-2,0])
        p12 = cvo.CVO().CreateCVO("Example 1 ", "$(5/10)$").setPosition([3,2,0])
        p13 = cvo.CVO().CreateCVO("Example 2", "$(2/4)$").setPosition([3,-1,0])
       # p14 = cvo.CVO().CreateCVO("Example 3", r"$\frac{16}{36}$").setPosition([0,-2,0])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        #p10.cvolist.append(p14)
        self.construct1(p10, p10)
    def LikeFractions(self):
        self.isRandom = False
        self.angleChoice = [TAU/2,TAU/4,TAU/4]
        p10 = cvo.CVO().CreateCVO("Like Fractions", "").setPosition([-4,2,0])
        p11 = cvo.CVO().CreateCVO("Definition","Fractions with same denominator.").setPosition([-4,-2,0])
        p12 = cvo.CVO().CreateCVO("Example 1 ", r"$\frac{2}{7}$,$\frac{3}{7}$,$\frac{5}{7}$").setPosition([3,2,0])
        p13 = cvo.CVO().CreateCVO("Example 2", r"$\frac{1}{9}$,$\frac{2}{9}$,$\frac{4}{9}$").setPosition([3,-1,0])
       # p14 = cvo.CVO().CreateCVO("Exp3", r"$\frac{16}{36}$").setPosition([0,-2,0])
        p11.setcircleradius(1.5)
        p13.setcircleradius(1.5)
        p12.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        #p10.cvolist.append(p14)
        self.construct1(p10, p10)
        
    
    def UnLikeFractions(self):
        self.isRandom = False
        self.angleChoice = [TAU/2,TAU/4,TAU/4]
        p10 = cvo.CVO().CreateCVO("UnLike Fractions", "").setPosition([-4,2,0])
        p11 = cvo.CVO().CreateCVO("Definition","Fractions with different denominators.").setPosition([-4,-2,0])
        p12 = cvo.CVO().CreateCVO("Example 1 ", r"$\frac{2}{5}$,$\frac{3}{2}$,$\frac{5}{9}$").setPosition([3,2,0])
        p13 = cvo.CVO().CreateCVO("Example 2", r"$\frac{1}{5}$,$\frac{2}{7}$,$\frac{4}{9}$").setPosition([3,-1,0])
       # p14 = cvo.CVO().CreateCVO("Exp3", r"$\frac{16}{36}$").setPosition([0,-2,0])
        p11.setcircleradius(1.8)
        p12.setcircleradius(1.5)
        p13.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        #p10.cvolist.append(p14)
        self.construct1(p10, p10)

    def AscendingOrder(self):
        self.isRandom = False
        self.angleChoice = [TAU/2,TAU/4,TAU/4]
        p10 = cvo.CVO().CreateCVO("Ascending Order Fractions", "").setPosition([-4,2,0])
        p11 = cvo.CVO().CreateCVO("Definition","Fractions arranged smallest to largest").setPosition([-4,-2,0])
        p12 = cvo.CVO().CreateCVO("Example 1", r"$\frac{3}{5} < \frac{7}{5} < \frac{9}{5}$").setPosition([3,2,0])
        p13 = cvo.CVO().CreateCVO("Example 2", r"$\frac{4}{3} < \frac{8}{3} < \frac{10}{3}$").setPosition([3,-1,0])
        p11.setcircleradius(1.8)
        p12.setcircleradius(1.5)
        p13.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.construct1(p10, p10)

    def DesendingOrder(self):
        self.isRandom = False
        self.angleChoice = [TAU/2,TAU/4,TAU/4]
        p10 = cvo.CVO().CreateCVO("Descending Order Fractions", "").setPosition([-4,2,0])
        p11 = cvo.CVO().CreateCVO("Definition","Fractions arranged Largest to Smallest").setPosition([-4,-2,0])
        p12 = cvo.CVO().CreateCVO("Example 1", r"$\frac{9}{5} > \frac{7}{5} > \frac{3}{5}$").setPosition([3,2,0])
        p13 = cvo.CVO().CreateCVO("Example 2", r"$\frac{10}{3} > \frac{8}{3} > \frac{4}{3}$").setPosition([3,-1,0])
        p11.setcircleradius(1.8)
        p12.setcircleradius(1.5)
        p13.setcircleradius(1.5)

        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.construct1(p10, p10)
       
    def AdditionOfFractions(self):
        examples_title = Text("Addition of Fractions Examples", font_size=36).to_edge(UP)
        self.play(Write(examples_title))
        radius = 1
        side_length = radius * 2
        square1 = Square(side_length=side_length)
        
        # Create vertical and horizontal lines matching the radius of the square
        vertical_line1 = Line(start=[0, -radius, 0], end=[0, radius, 0])
        horizontal_line1 = Line(start=[-radius, 0, 0], end=[radius, 0, 0])

        # Group all elements of square1
        group1 = VGroup(square1, vertical_line1, horizontal_line1)

        # Create a polygon to shade one quarter of square1
        shaded_area1 = Polygon(
            [0, 0, 0], [0, radius, 0], [radius, radius, 0], [radius, 0, 0],
            fill_opacity=0.5, fill_color=BLUE
        )
        
        # Add the shaded area to group1
        group1.add(shaded_area1)
        
        # Shift square1 to its position
        group1.shift(LEFT * 4)

        # Add group1 to the scene
        self.play(Create(square1))
        self.play(Create(vertical_line1))
        self.play( Create(horizontal_line1))
        self.wait(1)
        self.play(Create(shaded_area1))
        # Create the text "1/4" and position it below square1
        text1 = Tex(r"$\frac{1}{4}$")
        text1.shift(DOWN * 2 + LEFT * 4)
        
        self.wait(1)
        self.play(Write(text1))
    def AddSymbol(self):
        equals_signs = Tex("+").scale(1.5).shift(UP*0.1+LEFT*2.5)
        self.play(Write(equals_signs))

    def AddOfFractionExp2(self):
        radius = 1
        
        # Create a square with the specified radius (side length will be 2 * radius)
        side_length = radius * 2
        square1 = Square(side_length=side_length)
        
        # Create vertical and horizontal lines matching the radius of the square
        vertical_line1 = Line(start=[0, -radius, 0], end=[0, radius, 0])
        horizontal_line1 = Line(start=[-radius, 0, 0], end=[radius, 0, 0])

        # Group all elements of square1
        group1 = VGroup(square1, vertical_line1, horizontal_line1)

        # Create a polygon to shade one quarter of square1
        shaded_area1 = Polygon(
            [0, 0, 0], [0, radius, 0], [radius, radius, 0], [radius, 0, 0],
            fill_opacity=0.5, fill_color=BLUE
        )
        
        # Add the shaded area to group1
        group1.add(shaded_area1)
        
        # Shift square1 to its position
        group1.shift(LEFT * 1)

        # Add group1 to the scene
        self.play(Create(square1))
        self.play(Create(vertical_line1))
        self.play( Create(horizontal_line1))
        self.wait(1)
        self.play(Create(shaded_area1))
        # Create the text "1/4" and position it below square1
        text1 = Tex(r"$\frac{1}{4}$")
        text1.shift(DOWN * 2 + LEFT * 1)
        # Add text1 to the scene
        self.play(Write(text1))
        self.wait(1)

    def EquallSym(self):
        equals_signs = Tex("=").scale(1.5).shift(UP*0.1+RIGHT*1)
        self.play(Write(equals_signs))
        self.wait(1)
    def AddOfFractionExp3(self):

        radius = 1
        
        # Create a square with the specified radius (side length will be 2 * radius)
        side_length = radius * 2
        square1 = Square(side_length=side_length)
        
        # Create vertical and horizontal lines matching the radius of the square
        vertical_line1 = Line(start=[0, -radius, 0], end=[0, radius, 0])
        horizontal_line1 = Line(start=[-radius, 0, 0], end=[radius, 0, 0])

        # Group all elements of square1
        group1 = VGroup(square1, vertical_line1, horizontal_line1)
        shaded_area_size = side_length / 2
        # Create a polygon to shade one quarter of square1
        shaded_area1_1 = Polygon(
            [0, 0, 0], [0, radius, 0], [radius, radius, 0], [radius, 0, 0],
            fill_opacity=0.5, fill_color=BLUE
        )
        shaded_area1_2 = Polygon(
            [0, 0, 0], [0, radius, 0], [-radius, radius, 0], [-radius, 0, 0],
            fill_opacity=0.5, fill_color=BLUE
        )

        # Add shaded areas to group1
        group1.add(shaded_area1_1, shaded_area1_2)
        
        # Shift square1 to its position
        group1.shift(RIGHT*3)

        # Add group1 to the scene
        self.play(Create(square1))
        self.play(Create(vertical_line1))
        self.play(Create(horizontal_line1))
        self.wait(1)
        self.play(Create(shaded_area1_1))
        
        self.play(Create(shaded_area1_2))
        self.wait(1)
        # Create the text "1/4" and position it below square1
        text1 = Tex(r"$\frac{1}{2}$")
        text1.shift(DOWN * 2 + RIGHT * 3)
        self.wait(1)
        # Add text1 to the scene
        self.play(Write(text1))
        self.wait(2)
    
    def AddCircel1(self):
        examples_title = MathTex("Example 2: 1 ", font_size=36).to_edge(UP*3 + LEFT)
        
        self.play(Write(examples_title))
        # Define the radius of the circle
        radius = 1
        
        # Create a circle with the specified radius
        circle = Circle(radius=radius, color=WHITE, stroke_width=2)
        
        # Create a horizontal line from the center
        horizontal_line = Line(start=[-radius, 0, 0], end=[radius, 0, 0], color=WHITE)
        
        # Group all elements together
        group = VGroup(circle, horizontal_line)
        
        # Create a semicircle to shade (for example, the upper semicircle)
        shaded_area = Sector(
            outer_radius=radius,
            start_angle=180*DEGREES,
            angle=180 * DEGREES,
            fill_opacity=0.5,
            fill_color=BLUE
        )
        
        # Add shaded area to the group
        group.add(shaded_area)
        
        # Shift circle and horizontal line to their positions
        group.shift(LEFT*4)
        
        # Add everything to the scene
        self.play(Create(circle))
        self.play(Create(horizontal_line))
        self.wait(1)
        self.play( Create(shaded_area))
        
        
        text1 = Tex(r"$\frac{1}{2}$")
        text1.shift(DOWN * 2 + LEFT * 4)
        self.wait(1)
        # Add text1 to the scene
        self.play(Write(text1))
    def AdditionSymbol(self):
        equals_signs = Tex("+").scale(1.5).shift(UP*0.1+LEFT*2.5)
        self.wait(1)
        self.play(Write(equals_signs))
        
    def AddCircel2(self):
        # Define the radius of the circle
        radius = 1
        
        # Create a circle with the specified radius
        circle = Circle(radius=radius, color=WHITE, stroke_width=2)
        
        # Create a horizontal line from the center
        horizontal_line = Line(start=[-radius, 0, 0], end=[radius, 0, 0], color=WHITE)
        
        # Group all elements together
        group = VGroup(circle, horizontal_line)
        
        # Create a semicircle to shade (for example, the upper semicircle)
        shaded_area = Sector(
            outer_radius=radius,
            start_angle=0,
            angle=180 * DEGREES,
            fill_opacity=0.5,
            fill_color=BLUE
        )
        
        # Add shaded area to the group
        group.add(shaded_area)
        
        # Shift circle and horizontal line to their positions
        group.shift(LEFT*1)
        
        # Add everything to the scene
        self.play(Create(circle))
        self.play(Create(horizontal_line))
        self.wait(1)
        self.play(Create(shaded_area))
        
        
        
        text1 = Tex(r"$\frac{1}{2}$")
        text1.shift(DOWN * 2 + LEFT * 1)
        
        # Add text1 to the scene
        self.play(Write(text1))
        self.wait(1)

    def EquallSymbol(self):
        equals_signs = Tex("=").scale(1.5).shift(UP*0.1+RIGHT*1)
        self.play(Write(equals_signs))
        self.wait(1)

    def AddCircleFinal(self):
        radius = 1
        
        # Create a circle with the specified radius
        circle = Circle(radius=radius, fill_color=BLUE,fill_opacity=0.5, stroke_width=2).shift(RIGHT * 3)
        
        # Create the text "1/2" and position it relative to the circle
        text1 = Tex("1")
        text1.next_to( DOWN * 2 + RIGHT * 3)
        
        # Add the circle and text to the scene
        self.play(Create(circle))
        self.play(Write(text1))
        self.wait(2)

    def AdditionOfUnlike(self):
        title = Text("Addition of Unlike Fractions", font_size=36).to_edge(UP)
        self.play(Write(title))
        # Define the radius of the squares
        radius = 1
        
        # Create the first square with the specified radius (side length will be 2 * radius)
        side_length = radius * 2
        square1 = Square(side_length=side_length)
        
        # Create vertical line for the first square
        vertical_line1 = Line(start=[0, -radius, 0], end=[0, radius, 0])

        # Group all elements of square1
        group1 = VGroup(square1, vertical_line1)

        # Create a polygon to shade one quarter of square1
        shaded_area1 = Polygon(
            [-radius, -radius, 0], [-radius, radius, 0], [0, radius, 0], [0, -radius, 0],
            fill_opacity=0.5, fill_color=BLUE
        )
        
        # Add the shaded area to group1
        group1.add(shaded_area1)
        
        # Shift group1 to its position
        group1.shift(LEFT * 4)

        self.wait(1)
        self.play(Create(group1))
        
        # Create the text "1/4" and position it below square1
        text1 = Tex(r"$\frac{1}{2}$")
        text1.shift(DOWN * 2 + LEFT * 4)
        
        self.wait(1)
        self.play(Write(text1))
        self.wait(1.5)
        # Create the addition sign
        plus_sign = Tex("+").scale(1.5).shift(LEFT * 2.5)
        self.play(Write(plus_sign))

        # Create the second square
        square2 = Square(side_length=side_length)

        # Create two horizontal lines for the second square
        horizontal_line1 = Line(start=[-radius, radius / 3, 0], end=[radius, radius / 3, 0])
        horizontal_line2 = Line(start=[-radius, -radius / 3, 0], end=[radius, -radius / 3, 0])

        # Group all elements of square2
        group2 = VGroup(square2, horizontal_line1, horizontal_line2)

        # Create a polygon to shade the top part of square2
        shaded_area2 = Polygon(
            [-radius, radius, 0], [-radius, radius / 3, 0], [radius, radius / 3, 0], [radius, radius, 0],
            fill_opacity=0.5, fill_color=BLUE
        )
        
        # Add the shaded area to group2
        group2.add(shaded_area2)
        
        # Shift group2 to its position
        group2.shift(LEFT * 1)

        self.wait(1)
        self.play(Create(group2))
        
        # Create the text "1/3" and position it below square2
        text2 = Tex(r"$\frac{1}{3}$")
        text2.shift(DOWN * 2 + LEFT * 1)
        
        self.wait(1.5)
        self.play(Write(text2))

        # Create the equals sign
        equals_sign = Tex("=").scale(1.5).shift(RIGHT * 1)
        self.wait(1.5)
        self.play(Write(equals_sign))

        # Create the third square
        square3 = Square(side_length=side_length)

        # Create two horizontal lines and one vertical line for the third square
        horizontal_line3 = Line(start=[-radius, radius / 3, 0], end=[radius, radius / 3, 0])
        horizontal_line4 = Line(start=[-radius, -radius / 3, 0], end=[radius, -radius / 3, 0])
        vertical_line2 = Line(start=[0, -radius, 0], end=[0, radius, 0])

        # Group all elements of square3
        group3 = VGroup(square3, horizontal_line3, horizontal_line4, vertical_line2)

        # Create polygons to shade all parts except the bottom left one
        shaded_areas = [
            Polygon(
        [-radius, radius, 0], [0, radius, 0], [0, radius/3, 0], [-radius, radius/3, 0],
        fill_opacity=0.5, fill_color=BLUE
    ),
    Polygon(
        [0, radius, 0], [radius, radius, 0], [radius, radius/3, 0], [0, radius/3, 0],
        fill_opacity=0.5, fill_color=BLUE
    ),
    Polygon(
        [-radius, radius/3, 0], [0, radius/3, 0], [0, -radius/3, 0], [-radius, -radius/3, 0],
        fill_opacity=0.5, fill_color=BLUE
    ),
    Polygon(
        [0, radius/3, 0], [radius, radius/3, 0], [radius, -radius/3, 0], [0, -radius/3, 0],
        fill_opacity=0.5, fill_color=BLUE
    ),
    Polygon(
        [-radius, -radius/3, 0], [0, -radius/3, 0], [0, -radius, 0], [-radius, -radius, 0],
        fill_opacity=0.5, fill_color=BLUE
    ),
        ]

        # Add the shaded areas to group3
        for area in shaded_areas:
            group3.add(area)
        
        # Shift group3 to its position
        group3.shift(RIGHT * 4)

        self.wait(1.5)
        self.play(Create(group3))
        # Create the text "5/6" and position it below square3
        text3 = Tex(r"$\frac{5}{6}$")
        text3.shift(DOWN * 2 + RIGHT * 4)
        self.wait(1.5)
        # Add text3 to the scene
        self.play(Write(text3))
        self.wait(2)
    def SubOfFractions(self):
        title = Text("Subtraction of Fractions", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        radius = 1
        side_length = radius * 2
        
        # Create square1
        square1 = Square(side_length=side_length)
        
        # Create vertical and horizontal lines for square1
        vertical_line1 = Line(start=[0, -radius, 0], end=[0, radius, 0])
        horizontal_line1 = Line(start=[-radius, 0, 0], end=[radius, 0, 0])
        
        # Create shaded areas for square1
        shaded_area1_1 = Polygon(
            [0, 0, 0], [0, radius, 0], [radius, radius, 0], [radius, 0, 0],
            fill_opacity=0.5, fill_color=BLUE
        )
        shaded_area1_2 = Polygon(
            [0, 0, 0], [0, radius, 0], [-radius, radius, 0], [-radius, 0, 0],
            fill_opacity=0.5, fill_color=BLUE
        )
        shaded_area1_3 = Polygon(
            [0, 0, 0], [-radius, 0, 0], [-radius, -radius, 0], [0, -radius, 0],
            fill_opacity=0.5, fill_color=BLUE
        )
        
        # Group all elements of square1
        group1 = VGroup(square1, vertical_line1, horizontal_line1, shaded_area1_1, shaded_area1_2, shaded_area1_3)
        
        # Position and shift square1
        group1.shift(LEFT * 4)
        
        # Add square1 to the scene
        self.play(Create(group1))
        self.wait(1.5)
        
        # Create the text "3/4" and position it below square1
        text1 = Tex(r"$\frac{3}{4}$")
        text1.shift(DOWN * 2 + LEFT * 4)
        
        # Add text1 to the scene
        self.play(Write(text1))
        self.wait(1.5)
        
        # Create the addition sign
        plus_sign = Tex("-").scale(1.5).shift(UP * 0.1 + LEFT * 2.5)
        self.play(Write(plus_sign))
        self.wait(1)
        
        # Create square2
        square2 = Square(side_length=side_length)
        
        # Create vertical and horizontal lines for square2
        vertical_line2 = Line(start=[0, -radius, 0], end=[0, radius, 0])
        horizontal_line2 = Line(start=[-radius, 0, 0], end=[radius, 0, 0])
        
        # Create shaded areas for square2
        shaded_area2_1 = Polygon(
            [0, 0, 0], [0, radius, 0], [radius, radius, 0], [radius, 0, 0],
            fill_opacity=0.5, fill_color=BLUE
        )
        shaded_area2_2 = Polygon(
            [0, 0, 0], [0, -radius, 0], [-radius, -radius, 0], [-radius, 0, 0],
            fill_opacity=0.5, fill_color=BLUE
        )
        
        # Group all elements of square2
        group2 = VGroup(square2, vertical_line2, horizontal_line2, shaded_area2_1, shaded_area2_2)
        
        # Position and shift square2
        group2.shift(LEFT * 1)
        
        # Add square2 to the scene
        self.play(Create(group2))
        self.wait(1.5)
        
        # Create the text "2/4" and position it below square2
        text2 = Tex(r"$\frac{2}{4}$")
        text2.shift(DOWN * 2 + LEFT * 1)
        
        # Add text2 to the scene
        self.play(Write(text2))
        self.wait(1.5)
        # Create the equals sign
        equals_sign = Tex("=").scale(1.5).shift(UP * 0.1 + RIGHT * 1)
        self.play(Write(equals_sign))
        self.wait(1.5)
        
        # Create square3
        square3 = Square(side_length=side_length)
        
        # Create vertical and horizontal lines for square3
        vertical_line3 = Line(start=[0, -radius, 0], end=[0, radius, 0])
        horizontal_line3 = Line(start=[-radius, 0, 0], end=[radius, 0, 0])
        
        # Create shaded area for square3
        shaded_area3 = Polygon(
            [0, 0, 0], [0, -radius, 0], [-radius, -radius, 0], [-radius, 0, 0],
            fill_opacity=0.5, fill_color=BLUE
        )
        
        # Group all elements of square3
        group3 = VGroup(square3, vertical_line3, horizontal_line3, shaded_area3)
        
        # Position and shift square3
        group3.shift(RIGHT * 3)
        
        # Add square3 to the scene
        self.play(Create(group3))
        self.wait(1.5)
        
        # Create the text "1/4" and position it below square3
        text3 = Tex(r"$\frac{1}{4}$")
        text3.shift(DOWN * 2 + RIGHT * 3)
        
        # Add text3 to the scene
        self.play(Write(text3))
        self.wait(2)

    def Decimals(self):
        self.isRandom = False
        p10 = cvo.CVO().CreateCVO("Decimals", "").setPosition([-4,0,0]).setangle(-TAU/4)
        p11 = cvo.CVO().CreateCVO("Example 1 ","$3.14159$").setPosition([1,2.5,0]).setangle(-TAU/4)
        p12 = cvo.CVO().CreateCVO("Example 2", "$2.312$").setPosition([2.5, 0, 0]).setangle(-TAU/4)
        p13 = cvo.CVO().CreateCVO("Example 3", r"$4.2321$").setPosition([4,-1.5, 0]).setangle(-TAU/4)

        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.construct1(p10, p10)

    def DecimalsAddition(self):
        title = Title("Addition Of Decimals ")
        fraction_heading = MathTex("Example : ", r" 47.2 + 54.8", font_size=36).to_edge(UP*3 + LEFT)
        num1 = Tex("4 7 . 2", font_size=70).shift(LEFT * 3)
        num2 = Tex("5 4 . 8", font_size=70).shift(DOWN * 0.6 + LEFT * 3)
        plus_sign = Tex("+").scale(1.5).shift(DOWN * 0.6 + LEFT * 4.5)
        line_start = num2.get_corner(DOWN + LEFT) + DOWN *0.1-RIGHT * 0.5  
        line_end = line_start + RIGHT * 2.8 
        line = Line(line_start, line_end)
        s_result = Tex(r" 2 + 8 = 10", font_size=60,color=BLUE).shift(UP* 1 + RIGHT * 3)
        s_result2= Tex(r" 1 + 7 + 4 = 12", font_size=60,color=GREEN).shift(UP* 0.2 + RIGHT * 3)
        s_result3= Tex(r" 1 + 4 + 5 = 10", font_size=60,color=YELLOW).shift(DOWN*0.5 + RIGHT * 3)
        self.play(Write(title))
        self.wait(1)
        self.play(Write(fraction_heading))
        self.wait(1)
        self.play(Write(num1))
        self.wait(1)
        self.play( Write(num2))
        self.wait(1)
        self.play(Write(plus_sign))
        self.wait(1)
        self.play(Create(line))
        self.wait(1)
        line2_start  = num2.get_corner(DOWN + LEFT) + DOWN * 1- RIGHT * 0.5
        line2_end = line2_start + RIGHT  * 2.8
        line2 = Line(line2_start, line2_end)
        self.play(Create(line2))
        self.wait(1)

        # Units place addition
        highlight_rect1 = Rectangle(width=0.5, height=1.5, color=RED, fill_opacity=0.2).shift(DOWN * 0.2 + LEFT * 2.2)
        self.play(FadeIn(highlight_rect1))
        result1 = Tex(". 0", font_size=70).shift(DOWN * 1.5 + LEFT * 2.3)
        carry1 = Tex("1", font_size=60,color=YELLOW).shift(UP * 1 + LEFT * 3.2)
        self.play(Create(s_result))
        self.wait(1)
        self.play(Create(result1))
        

        self.play(FadeIn(carry1))
        self.wait(1)

        self.play(FadeOut(highlight_rect1))
        # Tens place addition
        highlight_rect2 = Rectangle(width=0.5, height=2.3, color=RED, fill_opacity=0.2).shift(UP * 0.2 + LEFT * 3.25)
        self.play(FadeIn(highlight_rect2))
        result2 = Tex("2", font_size=70).shift(DOWN * 1.5 + LEFT * 3.2)
        carry2 = Tex("1", font_size=60,color=YELLOW).shift(UP * 1 + LEFT * 3.8)
        self.play(Create(s_result2))
        self.wait(1)
        self.play(Create(result2))
        self.wait(1)
        
        self.play(FadeOut(highlight_rect2))
        self.wait(1)
        self.play(FadeIn(carry2))
        self.wait(1)
        # Hundreds place addition
        highlight_rect3 = Rectangle(width=0.5, height=2.5, color=RED, fill_opacity=0.2).shift(UP * 0.2 + LEFT * 3.8)
        self.play(FadeIn(highlight_rect3))
        result3 = Tex("1 0 ", font_size=70).shift(DOWN * 1.5 + LEFT * 4)
        self.play(Create(s_result3))
        self.wait(1)
        self.play(Create(result3))
        self.wait(1)
        self.play(FadeOut(highlight_rect3))
        self.wait(2)

    def DecimalsSubstraction(self):
        title = Title("Substraction Of Decimals ")
        fraction_heading = MathTex("Example : ", r" 59.5 + 35.2", font_size=36).to_edge(UP*3 + LEFT)
        num1 = Tex("5 9 . 5", font_size=70).shift(LEFT * 3)
        num2 = Tex("3 5 . 2", font_size=70).shift(DOWN * 0.6 + LEFT * 3)
        plus_sign = Tex("-").scale(1.5).shift(DOWN * 0.6 + LEFT * 4.3)
        line_start = num2.get_corner(DOWN + LEFT) + DOWN * 0.3  
        line_end = line_start + RIGHT * 2.2  
        line = Line(line_start, line_end)
        s_result = Tex(r" 5 - 2 = 3", font_size=60,color=BLUE).shift(UP* 1 + RIGHT * 3)
        s_result2= Tex(r" 9 - 5 = 4", font_size=60,color=GREEN).shift(UP* 0.2 + RIGHT * 3)
        s_result3= Tex(r" 5 - 3 = 2", font_size=60,color=YELLOW).shift(DOWN*0.5 + RIGHT * 3)
        self.play(Write(title))
        self.wait(1)
        self.play(Write(fraction_heading))
        self.wait(1)
        self.play(Write(num1))

        self.wait(1)
        self.play( Write(num2))
        self.wait(1)
        self.play(Create(line))
        self.wait(1)
        self.play(Write(plus_sign))
        self.wait(1)
        line2_start  = num2.get_corner(DOWN + LEFT) + DOWN * 1- RIGHT * 0
        line2_end = line2_start + RIGHT  * 2.2
        line2 = Line(line2_start, line2_end)
        self.play(Create(line2))
        self.wait(1)

        # Units place addition
        highlight_rect1 = Rectangle(width=0.5, height=1.5, color=RED, fill_opacity=0.2).shift(DOWN * 0.2 + LEFT * 2.2)
        self.play(FadeIn(highlight_rect1))
        result1 = Tex(". 3", font_size=70).shift(DOWN * 1.5 + LEFT * 2.2)
        #carry1 = Tex("1", font_size=60).shift(UP * 1 + LEFT * 3.15)
        self.play(Create(s_result))
        self.wait(1)
        self.play(Create(result1))
        self.wait(1)

        #self.play(FadeIn(carry1))
        self.play(FadeOut(highlight_rect1))
        self.wait(1)
        #self.play(FadeOut(carry1))
        # Tens place addition
        highlight_rect2 = Rectangle(width=0.5, height=2.0, color=RED, fill_opacity=0.2).shift(DOWN * 0.2 + LEFT * 3.25)
        self.play(FadeIn(highlight_rect2))
        result2 = Tex("4", font_size=70).shift(DOWN * 1.5 + LEFT * 3.2)
        #carry2 = Tex("1", font_size=60).shift(UP * 1 + LEFT * 3.8)
        self.play(Create(s_result2))
        self.wait(1)
        self.play(Create(result2))
        self.wait(1)
        self.play(FadeOut(highlight_rect2))
        self.wait(1)
        # Hundreds place addition
        highlight_rect3 = Rectangle(width=0.5, height=2.0, color=RED, fill_opacity=0.2).shift(DOWN * 0.2 + LEFT * 3.8)
        self.play(FadeIn(highlight_rect3))
        self.wait(1)
        result3 = Tex("2 ", font_size=70).shift(DOWN * 1.5 + LEFT * 4)
        self.play(Create(s_result3))
        self.wait(1)
        self.play(Create(result3))
        self.wait(1)
        self.play(FadeOut(highlight_rect3))
        self.wait(2)
    
if __name__ == "__main__":
    scene = Grade6Chapter7FractionsAndDecimalsAnim()
    scene.render()
