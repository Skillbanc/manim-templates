# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla

from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo


class ExploringGeometricalFigures(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.GeometricFigures()
        self.fadeOutCurrentScene()
        self.congruency()
        self.fadeOutCurrentScene()
        self.congruent()
        self.fadeOutCurrentScene()
        self.rotation()
        self.fadeOutCurrentScene()
        self.flipping()
        self.fadeOutCurrentScene()
        self.similarshapes()
        self.fadeOutCurrentScene()
        self.similaritycheck()
        self.fadeOutCurrentScene()
        self.constructDataByCVO() #
        self.fadeOutCurrentScene()
        self.symmetry()
        self.fadeOutCurrentScene()
        self.linesymmetry()
        self.fadeOutCurrentScene()
        self.rotationalsymmetry()
        self.fadeOutCurrentScene()
        self.pointsymmetry()
        self.fadeOutCurrentScene()










    def Introduction(self):
         
         
         self.colorChoice = [PINK,BLUE,LOGO_GREEN,ORANGE,WHITE,YELLOW]
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("Exploring Geometrical Figures","Introduction").setPosition([0,2.5,0])
         p11=cvo.CVO().CreateCVO("triangles","").setPosition([4,2,0])
         p12=cvo.CVO().CreateCVO("rectangles","").setPosition([5,-2,0])
         p13=cvo.CVO().CreateCVO("rhombus","").setPosition([-4,2,0]).setangle(-TAU/4)
         p14=cvo.CVO().CreateCVO("circles","").setPosition([-4,0,0]).setangle(-TAU/4)
         p15=cvo.CVO().CreateCVO("squares","").setPosition([4,0,0]).setangle(-TAU/6)

         p10.cvolist.append(p12)
         p10.cvolist.append(p11)
         p10.cvolist.append(p13)
         p10.cvolist.append(p14)
         p10.cvolist.append(p15)
         self.construct1(p10,p10)
         self.wait(2)


#geometric 
    def GeometricFigures(self):
         title = Text("Geometrical Figures", font_size=40).shift(UP * 3.5)
        

        # Create a group
         group = VGroup( title)
 
         self.add(group)


        # Create a circle
         circle = Circle(radius=2, color=BLUE)
         circle_label = Text("Circle", font_size=24).next_to(circle, DOWN)
        
        # Create a square
         square = Square(side_length=3, color=GREEN)
         square_label = Text("Square", font_size=24).next_to(square, DOWN)
        
        # Create a triangle
         triangle = Triangle(color=RED)
         triangle_label = Text("Triangle", font_size=24).next_to(triangle, DOWN)
        
        # Position the figures in a row
         circle.shift(LEFT * 4)
         square.shift(RIGHT * 4)
        
        # Animate the creation of the circle
         self.play(Create(circle), Write(circle_label))
         self.wait(1)
        
        # Animate the transformation from circle to square
         self.play(Transform(circle, square), Transform(circle_label, square_label))
         self.wait(1)
        
        # Animate the transformation from square to triangle
         self.play(Transform(circle, triangle), Transform(circle_label, triangle_label))
         self.wait(1)

        # Reset labels
         self.remove(circle_label)
         self.remove(triangle_label)

        # Create new shapes
         circle = Circle(radius=2, color=BLUE).shift(LEFT * 4)
         square = Square(side_length=3, color=GREEN).shift(RIGHT * 4)
         triangle = Triangle(color=RED)

        # Animate the drawing of shapes simultaneously
         self.play(
            Create(circle),
            Create(square),
            Create(triangle)
        )
        
         self.wait(2)



#Congruency
    def congruency(self):
         
         self.colorChoice = [ORANGE,WHITE,YELLOW]
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("congruency ","Object").setPosition([0,2.5,0])
         p11=cvo.CVO().CreateCVO("Equal sides","").setPosition([4,-2,0])
         p12=cvo.CVO().CreateCVO("Equal angles ","").setPosition([-4,-2,0])
         
         p10.cvolist.append(p11)
         p10.cvolist.append(p12)
        
         self.construct1(p10,p10)
         self.wait(2)



#conguent
    def congruent(self):
        
        
        # Create the title\

    #("Hello,\\nWorld!"
     

        title = Text("               CONGRUENT   \n\n    Same Sides & Same Angles ", font_size=47)
        title.to_edge(UP)

        # Create the first square
        square1 = Square(side_length=2, fill_color=ORANGE, fill_opacity=10)
        square1.shift(2*LEFT)

        # Create the second square
        square2 = Square(side_length=2, fill_color=BLUE, fill_opacity=10)
        square2.shift(2*RIGHT)

        # Create the congruency marks
        mark1 = VGroup(*[Dot(square1.get_vertices()[i], color=YELLOW) for i in range(4)])
        mark2 = VGroup(*[Dot(square2.get_vertices()[i], color=YELLOW) for i in range(4)])

        # Create the congruency lines
        line1 = Line(square1.get_vertices()[0], square2.get_vertices()[0], color=YELLOW)
        line2 = Line(square1.get_vertices()[1], square2.get_vertices()[1], color=YELLOW)
        line3 = Line(square1.get_vertices()[2], square2.get_vertices()[2], color=YELLOW)
        line4 = Line(square1.get_vertices()[3], square2.get_vertices()[3], color=YELLOW)

        # Add the title, squares, congruency marks, and congruency lines to the scene
        self.add(title, square1, square2, mark1, mark2, line1, line2, line3, line4)

        # Wait for a few seconds
        self.wait(3)

        # Animate the transformation from one square to the other
        self.play(Transform(square1, square2), run_time=3)

        # Wait for a few seconds
        self.wait(2)


#rotation
    def rotation(self):
        

        title = Text("Rotation ", font_size=53)
        title.to_edge(UP)

        axes = ThreeDAxes()
        self.add(axes)

        square = Square(side_length=2, fill_color=YELLOW, fill_opacity=4)
        square.shift(UP + RIGHT)

        self.play(Write(title))
        self.wait()

        self.play(Create(square))
        self.wait()

        rotation_animation = Rotate(square, 2*PI, axis=OUT, rate_func=linear)
        self.play(rotation_animation)
        self.wait()

        self.play(Unwrite(title))
        self.wait(2)



#flipping
    def flipping(self):
        
        title = Text("Flipping ", font_size=48)
        title.to_edge(UP)

        grid = NumberPlane(x_range=[-10, 10], y_range=[-10, 10], background_line_style={"stroke_color": BLUE})
        self.add(grid)

        square = Square(side_length=2.0, fill_color=ORANGE, fill_opacity =6)
        square.shift(UP + RIGHT)

        self.play(Write(title))
        self.wait()

        self.play(Create(square))
        self.wait()

        flip_animation = square.animate.flip(axis=UP)
        self.play(flip_animation)
        self.wait()

        self.play(Unwrite(title))
        self.wait(2)



#similar shapes
    def similarshapes(self):
        
        # Create squares
        square1 = Square(side_length=2, color=RED)
        square2 = Square(side_length=1, color=BLUE)
        square3 = Square(side_length=3, color=GREEN)

        # Create circles
        circle1 = Circle(radius=1, color=YELLOW)
        circle2 = Circle(radius=0.5, color=PURPLE)
        circle3 = Circle(radius=1.5, color=ORANGE)

        # Set starting positions of shapes
        square1.shift(LEFT * 4)
        square2.shift(LEFT * 2)
        square3.shift(RIGHT * 2)

        circle1.shift(LEFT * 4 + UP * 2)
        circle2.shift(LEFT * 2 + UP * 2)
        circle3.shift(RIGHT * 2 + UP * 2)

        # Create titles
        square_title = Text("Similarity of Squares & Circles", font_size=40).shift(UP * 3.5)
        circle_title = Text("", font_size=40).shift(UP * 5.5)

        # Create a group
        group = VGroup(square1, square2, square3, circle1, circle2, circle3, square_title, circle_title)

        self.add(group)
        self.wait()
        self.play(group.animate.shift(DOWN))  # shift all shapes down
        self.play(square1.animate.shift(RIGHT))  # move only one square
        self.play(circle1.animate.shift(UP))  # move only one circle
        self.play(group.animate.shift(RIGHT))  # shift all shapes to the right
        self.wait(2)



#similarity  check

    def similaritycheck(self):
        
         title = Text(" Checking Similarity Of Two Objects", font_size=40).shift(UP * 3.5)
        

        # Create a group
         group = VGroup( title)

         self.add(group)

         
          #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         self.colorChoice = [WHITE,BLUE,PINK,ORANGE,YELLOW]
         p10=cvo.CVO().CreateCVO("Sides and Angles","Each Shape ").setPosition([2,1,0])
         p11=cvo.CVO().CreateCVO("Square"," 1/2 and   90 degree").setPosition([4.5,1,0])
         p12=cvo.CVO().CreateCVO("Equilateral triangle","2/3 and   60 degree").setPosition([5,-2,0])
         p13=cvo.CVO().CreateCVO("Rectangle","2/3 and   90 degree").setPosition([-5,0,0]).setangle(-TAU/4)
         p14=cvo.CVO().CreateCVO("Right angled triangle","3/6 and   90 degree").setPosition([-2,-0.5,0]).setangle(-TAU/4)
         

         p10.cvolist.append(p12)
         p10.cvolist.append(p11)
         p10.cvolist.append(p13)
         p10.cvolist.append(p14)


         p11.setcircleradius(1.5)
         p12.setcircleradius(1.5)
         p13.setcircleradius(1.5)
         p14.setcircleradius(1.5)
        


         self.construct1(p10,p10)
         self.wait(2)



#dilation
    
        
        # self.fadeOut()
        # self.constructDataByJSON()
        # self.fadeOut()
        
    # render using CVO data object
    def constructDataByCVO(self):
        self.colorChoice = [ORANGE,WHITE,YELLOW,BLUE,GREEN,PINK,RED]
        p10=cvo.CVO().CreateCVO("Dilation","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Defination", "transformation of shape with keeping same proportions").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("scale factor", "proportion that changes the size of a shape").setPosition([5,-2,0])
        p13=cvo.CVO().CreateCVO("construction", "").setPosition([-4,2.8,0]).setangle(-TAU/4)
        p14=cvo.CVO().CreateCVO("Step:1", "Choose a center").setPosition([-4,0.5,0]).setangle(-TAU/4)
        
        p15=cvo.CVO().CreateCVO("step:2", "Stretch or shrink shapes").setPosition([-4,-1.2,0]).setangle(-TAU/4)
        p16=cvo.CVO().CreateCVO("step:3", "Stretch the projected points").setPosition([-4,-3,0]).setangle(-TAU/4)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p13.cvolist.append(p14)
        p14.cvolist.append(p15)
        p15.cvolist.append(p16)
        
        self.construct1(p10,p10)
        
        #self.play()
        
























        

#symmetry
    def symmetry(self):
        
        # Create butterfly shape
        square = VGroup()
        wing1 = Polygon(
            [-2, 0, 0],
            [0, 2, 0],
            [2, 0, 0],
            [0, -2, 0],
            fill_color=BLUE,
            fill_opacity=0.5
        )
        wing2 = wing1.copy().rotate(PI)
        body = Circle(radius=0.5, fill_opacity=0.5)
        square.add(wing1, wing2, body)

        # Create line of symmetry
        line_of_symmetry = Line(start=[-3, 0, 0], end=[3, 0, 0], color=YELLOW)

        # Create titles
        title = Text(" Symmetry", font_size=40).shift(UP * 3.5)
        symmetry_title = Text("Square is Symmetry", font_size=30).shift(UP * 2.5)

        # Create a group
        group = VGroup(square, line_of_symmetry, title, symmetry_title)

        self.add(group)
        self.wait()
        self.play(square.animate.shift(UP))  # shift butterfly up
        self.play(line_of_symmetry.animate.shift(UP))  # shift line of symmetry up
        self.wait(2)




#linesymmetry
    def linesymmetry(self):
        
        title = Title("Line Of Symmetry  or  Mirror Line",color = PINK)
        self.add(title)

        square1 = Square(color=BLUE, fill_opacity=5)
        square1.shift(LEFT * 3 + DOWN * 2)

        square2 = Square(color=BLUE, fill_opacity=5)
        square2.shift(RIGHT * 3 + UP * 2)
######
        line1 = Line(start=DOWN * 2 + LEFT * 0, end=UP * 2 + LEFT * 0, color=YELLOW)
        self.add( line1)

        self.play(Write(square1), Write(square2))

        self.play(
            square1.animate.shift(RIGHT * 2),
            square2.animate.shift(LEFT * 2),
            #line_of_symmetry.animate.shift(RIGHT * 2),
            run_time=2
        )

        self.play(
            square1.animate.shift(UP * 2),
            square2.animate.shift(DOWN * 2),
           # line_of_symmetry.animate.shift(UP * 2),
            run_time=3
        )

        self.play(
            square1.animate.shift(LEFT * 2),
            square2.animate.shift(RIGHT * 2),
           # line_of_symmetry.animate.shift(LEFT * 2),
            run_time=2
        )

       

        self.wait(2)


#rotationalsymmetry
    def rotationalsymmetry(self):
        
        title = Text("Rotational Symmetry", font_size=40).shift(UP * 3.5)
        

        # Create a group
        group = VGroup( title)

        self.add(group)



        # Square
        s = Rectangle(width=3, height=3)
        s.set_color(ORANGE)
        s.shift(RIGHT * 2)
        self.add(s)

        # Lines of Symmetry for Triangle
        #line1 = DashedLine(start=DOWN * 2 + LEFT * 3, end=UP * 2 + LEFT * 3, color=YELLOW)
        line2 = DashedLine(start=RIGHT*2 + RIGHT * 3, end=LEFT*2 + RIGHT * 3, color=YELLOW)
        self.add( line2)
        

        # Rotational Symmetry Animation for Rectangle
        self.wait(2)
        self.play(Rotating(s, about_point=s.get_center(), radians=PI/2, run_time=2))
        self.wait(2)

       

        #

        # Rectangle
        rectangle = Rectangle(width=2, height=1)
        rectangle.set_color(BLUE)
        rectangle.shift(RIGHT * 2)
        self.add(rectangle)

        # Lines of Symmetry for Rectangle
        line4 = DashedLine(start=DOWN + RIGHT * 2, end=UP + RIGHT * 2, color=YELLOW)
        line5 = DashedLine(start=LEFT + RIGHT * 2, end=RIGHT + RIGHT * 2, color=YELLOW)
        self.add(line4, line5)

        # Rotational Symmetry Animation for Rectangle
        self.wait(2)
        self.play(Rotating(rectangle, about_point=rectangle.get_center(), radians=PI/2, run_time=2))
        self.wait(2)

        # Circle
        circle = Circle(radius=1)
        circle.set_color(GREEN)
        circle.shift(UP * 2)
        self.add(circle)

        # Lines of Symmetry for Circle
        line6 = DashedLine(start=DOWN + UP * 2, end=UP + UP * 2, color=YELLOW)
        line7 = DashedLine(start=LEFT + UP * 2, end=RIGHT + UP * 2, color=YELLOW)
        self.add(line6, line7)

        # Rotational Symmetry Animation for Circle
        self.wait(2)
        self.play(Rotating(circle, about_point=circle.get_center(), radians=PI/4, run_time=2))
        self.wait(2)



    # Isosceles Triangle
        isosceles_triangle = Polygon(np.array([-1, -1, 0]), np.array([1, -1, 0]), np.array([0, 1, 0]))
        isosceles_triangle.set_color(WHITE)
        isosceles_triangle.shift(LEFT + UP)
        self.add(isosceles_triangle)

        # Dashed Lines of Symmetry for Isosceles Triangle
        line8 = DashedLine(start=DOWN + LEFT, end=UP + LEFT, color=YELLOW)
        line9 = DashedLine(start=LEFT + UP, end=RIGHT + UP, color=YELLOW)
        self.add(line8, line9)

        # Rotational Symmetry Animation for Isosceles Triangle
        self.wait(2)
        self.play(Rotating(isosceles_triangle, about_point=isosceles_triangle.get_center(), radians=PI/2, run_time=2))
        self.wait(2)




#pointsymmetry
    def pointsymmetry(self):
        
        title = Title("Point Symmetry ",color = ORANGE)
        self.add(title)

        axis_x = DashedLine(start=LEFT * 4, end=RIGHT * 4, color=YELLOW)
        axis_y = DashedLine(start=DOWN * 4, end=UP * 4, color=YELLOW)

        self.play(Write(axis_x), Write(axis_y))

        star = Star(n=5, outer_radius=1.5, inner_radius=0.6, color=BLUE, fill_opacity=3)
        star.move_to(ORIGIN)

        self.play(Write(star))

        self.play(
            star.animate.scale(-1, about_point=ORIGIN),
            run_time=2
        )
        self.play(
            star.animate.scale(-1, about_point=ORIGIN),
            run_time=2
        )

        self.wait(2)





















#SKILLBANC LOGO

    def RenderSkillbancLogo(self):
        
        self.orange = "#D76800"
        self.blue = "#3F64A7"
        self.green = "#96D24D"
        self.circles = VGroup(
            Circle(radius=1).rotate(PI/2).set_fill(self.orange, opacity=1).set_stroke(self.orange, opacity=1).shift(LEFT*3),
            Circle(radius=1).rotate(PI/2).set_fill(self.blue, opacity=1).set_stroke(self.blue, opacity=1),
            Circle(radius=1).rotate(PI/2).set_fill(self.green, opacity=1).set_stroke(self.green, opacity=1).shift(RIGHT*3)
        )
        circle1, circle2, circle3 = self.circles
        
        lines = VGroup(
            Arrow(circle1.get_right(), circle2.get_left(), max_tip_length_to_length_ratio=2),
            Arrow(circle2.get_right(), circle3.get_left(), max_tip_length_to_length_ratio=2),
            CurvedArrow(circle1.get_top(), circle3.get_top(), angle=-TAU/4),
            CurvedArrow(circle1.get_bottom(), circle3.get_bottom(), angle=TAU/4)
        )

        # Adjust the starting points of the straight arrows to touch the circumference
        lines[0].put_start_and_end_on(circle1.get_right(), circle2.get_left())
        lines[1].put_start_and_end_on(circle2.get_right(), circle3.get_left())

        # Add the text "skillbanc" below the curved arrows
        self.play(Create(circle1), Create(circle2), Create(circle3), rate_func=smooth, run_time=1)
        self.play(Create(lines), rate_func=smooth, run_time=1)
        text = Text("Skillbanc.com, Inc.").next_to(lines[3], DOWN)
        self.play(Create(text), rate_func=smooth, run_time=0.75)
        
        self.logoGroup = VGroup().add(self.circles).add(lines).add(text)
        self.play(self.logoGroup.animate.scale(0),run_time=1)
        # self.play(self.circles.animate.scale(0),lines.animate.scale(0),text.animate.scale(0),run_time=3)
        

      
if __name__ == "__main__":
    scene = ExploringGeometricalFigures()
    scene.render()
