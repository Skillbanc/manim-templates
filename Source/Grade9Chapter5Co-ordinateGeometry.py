# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla
import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo

class cordinateAnim(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
         self.RenderSkillbancLogo()
         self.constructDataByCVO()
         self.fadeOutCurrentScene()
         self.parallel()
         self.fadeOutCurrentScene()
         self.quadrants()
         self.fadeOutCurrentScene()
         self.geo1()
         self.fadeOutCurrentScene()
         self.add_quadrants()
         self.fadeOutCurrentScene()
         self.origin00()
         self.fadeOutCurrentScene()
         self.origin()
         self.fadeOutCurrentScene()
         self.parallelogram()
         self.fadeOutCurrentScene()
         self.GithubSourceCodeReference()
   
    def constructDataByCVO(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Co-ordinate Geometry","")
        p11=cvo.CVO().CreateCVO("Definition","The study of algebraic equations on graphs")
        
        p10.cvolist.append(p11)

        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)


    def parallel(self):
    
     

     
   
        # Title
        title = Text("Number Line", font_size=36)
        title.to_edge(UP, buff=1)
        self.play(Write(title))

        # Create the number line
        number_line = NumberLine(
            x_range=[-7, 8, 1],
            length=14,
            include_numbers=True,
            label_direction=DOWN,
        ).shift(DOWN)

        # Create labels for negative and positive integers
        negative_label = Text("Negative Integer", font_size=24)
        positive_label = Text("Positive Integer", font_size=24)
        
        # Add brackets
        negative_bracket = Brace(Line(number_line.n2p(-7), number_line.n2p(0)), direction=UP)
        positive_bracket = Brace(Line(number_line.n2p(0), number_line.n2p(7)), direction=UP)
        
        # Position labels above the brackets
        negative_label.next_to(negative_bracket, UP, buff=0.1)
        positive_label.next_to(positive_bracket, UP, buff=0.1)
        
        # Add all elements to the scene
        self.play(Create(number_line))
        self.play(Create(negative_bracket), Create(positive_bracket))
        self.play(Write(negative_label), Write(positive_label))

        # Add arrows at the ends of the number line
        left_arrow = Arrow(start=number_line.n2p(-7), end=number_line.n2p(-7.5), buff=0)
        right_arrow = Arrow(start=number_line.n2p(7), end=number_line.n2p(7.5), buff=0)
        self.play(Create(left_arrow), Create(right_arrow))

        # Conclusion text
        conclusion = Text("The fixed point corresponding to zero is called Origin", font_size=24)
        conclusion.next_to(number_line, DOWN, buff=1)
        self.play(Write(conclusion))

        self.wait(2)



       
    def quadrants(self):
     
        
        # Create the axes with x and y labels
        axes = NumberPlane(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            axis_config={"color": WHITE},
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 2},
            x_axis_config={"label_direction": UP},  # Label direction for x-axis
            y_axis_config={"label_direction": RIGHT},  # Label direction for y-axis
        ).scale(0.5).to_edge(LEFT, buff=1)  # Scale down the axes and move to the left
        axes.add_coordinates()

        # Labels for the axes
        x_label = axes.get_x_axis_label("X", direction=RIGHT, buff=0.1)
        y_label = axes.get_y_axis_label("Y", direction=UP, buff=0.2)

        # Add points
        point_Q = Dot(axes.c2p(-4, 5), color=RED)
        point_P = Dot(axes.c2p(4, 3), color=RED)
        point_R = Dot(axes.c2p(-2, -4), color=RED)
        point_S = Dot(axes.c2p(4, -5), color=RED)

        # Add labels for the points
        label_Q = MathTex("Q", font_size=24).next_to(point_Q, UP, buff=0.1)
        label_P = MathTex("P", font_size=24).next_to(point_P, UP, buff=0.1)
        label_R = MathTex("R", font_size=24).next_to(point_R, UP, buff=0.1)
        label_S = MathTex("S", font_size=24).next_to(point_S, UP, buff=0.1)
        
        # Add dashed lines (changed color to GREEN)
        dashed_line_Q = DashedLine(point_Q.get_center(), axes.c2p(-4, 0), color=GREEN)
        dashed_line_Q_y = DashedLine(point_Q.get_center(), axes.c2p(0, 5), color=GREEN)
        dashed_line_P = DashedLine(point_P.get_center(), axes.c2p(4, 0), color=GREEN)
        dashed_line_P_y = DashedLine(point_P.get_center(), axes.c2p(0, 3), color=GREEN)
        dashed_line_R = DashedLine(point_R.get_center(), axes.c2p(-2, 0), color=GREEN)
        dashed_line_R_y = DashedLine(point_R.get_center(), axes.c2p(0, -4), color=GREEN)
        dashed_line_S = DashedLine(point_S.get_center(), axes.c2p(4, 0), color=GREEN)
        dashed_line_S_y = DashedLine(point_S.get_center(), axes.c2p(0, -5), color=GREEN)

        # Add all elements to the scene
        self.add(axes, x_label, y_label)  # Add axes, x_label, and y_label
        self.play(Create(point_Q), Create(label_Q), Create(dashed_line_Q), Create(dashed_line_Q_y))
        self.play(Create(point_P), Create(label_P), Create(dashed_line_P), Create(dashed_line_P_y))
        self.play(Create(point_R), Create(label_R), Create(dashed_line_R), Create(dashed_line_R_y))
        self.play(Create(point_S), Create(label_S), Create(dashed_line_S), Create(dashed_line_S_y))
        
        # Add conclusions
        conclusion_Q = Text("The coordinates of point Q are (-4, 5)", font_size=24).to_edge(RIGHT, buff=1).shift(UP*1.5)
        conclusion_P = Text("The coordinates of point P are (4, 3)", font_size=24).next_to(conclusion_Q, DOWN, buff=0.3)
        conclusion_R = Text("The coordinates of point R are (-2, -4)", font_size=24).next_to(conclusion_P, DOWN, buff=0.3)
        conclusion_S = Text("The coordinates of point S are (4, -5)", font_size=24).next_to(conclusion_R, DOWN, buff=0.3)

        self.play(Write(conclusion_Q))
        self.play(Write(conclusion_P))
        self.play(Write(conclusion_R))
        self.play(Write(conclusion_S))

        self.wait(2)


      

        


    def geo1(self):
        self.isRandom = False
        p20=cvo.CVO().CreateCVO("Cartesian System", "Quadrants").setPosition([-4,0,0])
        p21=cvo.CVO().CreateCVO("Quadrant 1", "(+,+)").setPosition([-1,2,0]).setangle(-TAU/4)
        p22=cvo.CVO().CreateCVO("Quadrant 2", "(-,+)").setPosition([1,2.5,0]).setangle(-TAU/4)
        p23=cvo.CVO().CreateCVO("Quadrant 3", "(-,-)").setPosition([4.5,0,0]).setangle(-TAU/4)
        p24=cvo.CVO().CreateCVO("Quadrant 4", "(+,-)").setPosition([0,-1.5,0]).setangle(-TAU/4)
       
        p20.cvolist.append(p21)
        p20.cvolist.append(p22)
        p20.cvolist.append(p23)
        p20.cvolist.append(p24)

        self.setNumberOfCirclePositions(5)

        self.construct1(p20,p20)

    def add_quadrants(self):
    
    
        # Set up the axes
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"color": BLUE},
        )

        # Create vertical and horizontal lines at the origin to divide quadrants
        v_line = Line(start=axes.c2p(0, -5), end=axes.c2p(0, 5), color=WHITE)
        h_line = Line(start=axes.c2p(-5, 0), end=axes.c2p(5, 0), color=WHITE)

        # Add labels for each quadrant
        label_1 = Text("I \n (+,+)").move_to(axes.c2p(2, 2))
        label_2 = Text("II \n (-,+)").move_to(axes.c2p(-2, 2))
        label_3 = Text("III \n (+,-)").move_to(axes.c2p(-2, -2))
        label_4 = Text("IV \n (-,-)").move_to(axes.c2p(2, -2))

        # Add everything to the scene
        self.add(axes, v_line, h_line, label_1, label_2, label_3, label_4)

        # Add the title
        title = Text("Quadrants", font_size=36).to_corner(UP + LEFT)
        self.add(title)
        
        self.wait(3)





    def origin00(self):
        self.isRandom = False
        p30=cvo.CVO().CreateCVO("Origin","Intersecting point of x and y axis")
        p31=cvo.CVO().CreateCVO("Notation=(x,y)", "(0,0)").setangle(-TAU/4).setangle(-TAU/4)
        p32=cvo.CVO().CreateCVO("x cordinate(Absicca)", "0").setangle(-TAU/4)
        p33=cvo.CVO().CreateCVO("y cordinate(Ordinate)", "0").setangle(-TAU/4)
       
       
        p30.cvolist.append(p31)
        p30.cvolist.append(p32)
        p30.cvolist.append(p33)

        self.setNumberOfCirclePositions(4)

        self.construct1(p30,p30)

    def origin(self):
      
        # Create the axes
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"color": BLUE},
        )

        # Create vertical and horizontal lines at the origin to divide quadrants
        v_line = Line(start=axes.c2p(0, -5), end=axes.c2p(0, 5), color=WHITE)
        h_line = Line(start=axes.c2p(-5, 0), end=axes.c2p(5, 0), color=WHITE)

        # Add labels for each quadrant
        label_1 = Text("I").move_to(axes.c2p(2, 2))
        label_2 = Text("II").move_to(axes.c2p(-2, 2))
        label_3 = Text("III").move_to(axes.c2p(-2, -2))
        label_4 = Text("IV").move_to(axes.c2p(2, -2))

        # Add everything to the scene
        self.add(axes, v_line, h_line, label_1, label_2, label_3, label_4)
        
        # Create smaller axes
        small_axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 5, 1],
            axis_config={"color": BLUE},
        )
        small_axes.add_coordinates()
        
        # Create points
        points = [(2, 3)]
        dots = [Dot(small_axes.c2p(x, y), color=GREEN) for x, y in points]
        labels = [MathTex(f"({x},{y})").next_to(dot, UP) for (x, y), dot in zip(points, dots)]
        
        # Create moving origin
        origin = Dot(color=RED)
        origin_label = MathTex("(0,0)").next_to(origin, DOWN + LEFT)
        
        animations = []
        for dot, label in zip(dots, labels):
            animations.append(AnimationGroup(
                FadeIn(dot),
                Write(label),
                run_time=1
            ))
            animations.append(ApplyMethod(origin.move_to, dot.get_center(), run_time=1))
            animations.append(FadeOut(dot))
            animations.append(FadeOut(label))
        
        # Add the title
        title = Text("origin-(0,0)", font_size=24).to_corner(UP + LEFT)
        self.add(title)

        # Display the origin and its label
        self.play(FadeIn(origin), Write(origin_label))

        # Run the animations
        self.wait(3)
        self.play(*animations)

        


    def parallelogram(self):
   
        # Define points as float arrays
        A = np.array([1.0, 1.0, 0.0])
        B = np.array([4.0, 1.0, 0.0])
        C = np.array([5.0, 4.0, 0.0])
        D = np.array([2.0, 4.0, 0.0])
        P = np.array([2.0, 1.0, 0.0])

        # Title
        title = Text("Example:Find the Area of the Parallelogram", font_size=36)
        title.to_edge(UP)

        # Adjust the parallelogram's position to span the first and fourth quadrants
        shift_vector = np.array([1.0, -1.5, 0.0])
        A += shift_vector
        B += shift_vector
        C += shift_vector
        D += shift_vector
        P += shift_vector

        # Draw parallelogram
        parallelogram = Polygon(A, B, C, D, color=BLUE)

        # Draw altitude line
        altitude = DashedLine(D, P, color=YELLOW, stroke_width=2)

        # Labels
        label_A = Text("A").next_to(A, LEFT)
        label_B = Text("B").next_to(B, DOWN)
        label_C = Text("C").next_to(C, RIGHT)
        label_D = Text("D").next_to(D, LEFT)
        label_P = Text("P").next_to(P, DOWN)

        # Calculation steps
        base_text = Text("Base (AB) = 4 units").to_edge(LEFT).shift(UP*2)
        height_text = Text("Height (DP) = 3 units").next_to(base_text, DOWN)
        area_calc_text = Text("Area = Base × Height").next_to(height_text, DOWN)
        area_value_text = Text("Area = 4 × 3 = 12 units²").next_to(area_calc_text, DOWN)

        # Display elements
        self.play(Write(title))
        self.play(Write(parallelogram))
        self.play(Write(altitude))
        self.play(Write(label_A), Write(label_B), Write(label_C), Write(label_D), Write(label_P))
        self.play(Write(base_text))
        self.play(Write(height_text))
        self.play(Write(area_calc_text))
        self.play(Write(area_value_text))

        # Show area formula step-by-step
        self.wait(3)

    def SetDeveloperList(self):  
        self.DeveloperList="Habeeb Unissa"
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade9Chapter5Co-ordinate Geometry.py"


if __name__ == "__main__":
         scene = cordinateAnim()
         scene.render()
        
