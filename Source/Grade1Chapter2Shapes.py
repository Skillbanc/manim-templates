from manim import *
from AbstractAnim import AbstractAnim
import cvo


class Grade1Chapter2Shapes(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.diffshapes()
        self.fadeOutCurrentScene()
        self.square()
        self.fadeOutCurrentScene()
        self.rectangle()
        self.fadeOutCurrentScene()
        self.triangle()
        self.fadeOutCurrentScene()
        self.circle()
        self.fadeOutCurrentScene()
        self.matchshapes()
        self.fadeOutCurrentScene()
        #self.shapecolor()
        #self.fadeOutCurrentScene()
        self.nextshape()
        self.fadeOutCurrentScene()
        self.differentshape()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()


    def diffshapes(self):

        self.setNumberOfCirclePositions(5)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Shapes","").setPosition([-4,2,0])
        p12=cvo.CVO().CreateCVO("Square","").setPosition([3,2,0])
        p13=cvo.CVO().CreateCVO("Rectangle", "").setPosition([4,0,0])
        p14=cvo.CVO().CreateCVO("Triangle","").setPosition([2,-3,0])
        p15=cvo.CVO().CreateCVO("Circle", "").setPosition([-4,-3,0])
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        self.construct1(p10,p10)
        self.wait(3)


    def square(self):

        text = Text("SQUARE")
        text.scale(0.5)
        text.to_edge(UP)
        self.play(Write(text))
        self.wait(1)

        square = Square(color = RED).set_color(RED)
        square.shift(UP)
        self.play(Create(square))  # Animate the creation of the square
        self.wait(2)

        text1 = Text("A square is a four-sided polygon which has it's all sides equal in length\n\nand the measure of the angles are 90 degrees.")
        text1.scale(0.5)
        text1.shift(DOWN)
        self.play(Write(text1))
        self.wait(2)


    def rectangle(self):

        text = Text("RECTANGLE")
        text.scale(0.5)
        text.to_edge(UP)
        self.play(Write(text))
        self.wait(1)

        rectangle = Rectangle(width=4.0, height=2.0).set_color(RED)
        rectangle.shift(UP)
        self.play(Create(rectangle))
        self.wait(2)

        text1 = Text("A rectangle is a type of quadrilateral that has its parallel sides equal to\n\neach other and all the four vertices are equal to 90 degrees.")
        text1.scale(0.5)
        text1.shift(DOWN)
        self.play(Write(text1))
        self.wait(2)


    def triangle(self):

        text = Text("TRIANGLE")
        text.scale(0.5)
        text.to_edge(UP)
        self.play(Write(text))
        self.wait(1)

        triangle = Triangle().set_color(RED)
        triangle.shift(UP)
        self.play(Create(triangle))
        self.wait(2)

        text1 = Text("A triangle is a polygon with three sides having three vertices. The angle\n\nformed inside the triangle is equal to 180 degrees.")
        text1.scale(0.5)
        text1.shift(DOWN)
        self.play(Write(text1))
        self.wait(2)


    def circle(self):

        text = Text("CIRCLE")
        text.scale(0.5)
        text.to_edge(UP)
        self.play(Write(text))
        self.wait(1)

        circle = Circle().set_color(RED)
        circle.shift(UP)
        self.play(Create(circle))
        self.wait(2)

        text1 = Text("A circle is a round-shaped figure that has no corners or edges")
        text1.scale(0.5)
        text1.shift(DOWN)
        self.play(Write(text1))
        self.wait(2)


    def matchshapes(self):
        text = Text("Match the shapes with their similar shapes on the right ")
        text.scale(0.75)
        text.to_edge(UP)
        self.play(Write(text))
        square1 = Square(side_length=0.8, color=BLUE)
        square2 = Square(side_length=0.8, color=BLUE)
        rectangle1 = Rectangle(width=1.8, height=0.8, color=GREEN)
        rectangle2 = Rectangle(width=1.8, height=0.8, color=GREEN)
        triangle1 = Triangle().scale(0.65).set_color(RED)
        triangle2 = Triangle().scale(0.65).set_color(RED)
        circle1 = Circle(radius=0.6, color=WHITE)
        circle2 = Circle(radius=0.6, color=WHITE)

        # Arrange shapes in columns
        shapes_col1 = VGroup(square1, rectangle1, triangle1, circle1).arrange(DOWN, buff=0.45)
        shapes_col2 = VGroup(circle2, triangle2, square2, rectangle2).arrange(DOWN, buff=0.45)

        # Position the columns
        shapes_col1.move_to(LEFT * 3)
        shapes_col2.move_to(RIGHT * 3)
        
        # Create arrows
        arrow1 = Arrow(square1.get_right(), square2.get_left(), color=BLUE, buff=0)
        arrow2 = Arrow(rectangle1.get_right(), rectangle2.get_left(), color=GREEN, buff=0)
        arrow3 = Arrow(triangle1.get_right(), triangle2.get_left(), color=RED, buff=0)
        arrow4 = Arrow(circle1.get_right(), circle2.get_left(), color=WHITE, buff=0)
        # Animate shapes and arrows step by step
        self.play(FadeIn(shapes_col1), FadeIn(shapes_col2))
        self.wait(1)
        
        self.play(Create(arrow1))
        self.wait(1)
        self.play(Create(arrow2))
        self.wait(1)
        self.play(Create(arrow3))
        self.wait(1)
        self.play(Create(arrow4))
        self.wait(2)


    def shapecolor(self):

        text = Text("Colour the shapes of the following picture with the same colours.")
        text.scale(0.75)
        text.to_edge(UP)
        self.play(Write(text))
        
        head = Circle(radius=0.5).set_fill(YELLOW, opacity=1).shift(UP * 1.5)
        body = Rectangle(height=2, width=1).set_fill(BLUE, opacity=1)
        left_arm = Rectangle(height=0.5, width=1.5).set_fill(RED, opacity=1).next_to(body, LEFT, buff=0)
        right_arm = Rectangle(height=0.5, width=1.5).set_fill(RED, opacity=1).next_to(body, RIGHT, buff=0)
        left_leg = Rectangle(height=1.5, width=0.5).set_fill(GREEN, opacity=1).next_to(body, DOWN, buff=0).shift(LEFT * 0.3)
        right_leg = Rectangle(height=1.5, width=0.5).set_fill(GREEN, opacity=1).next_to(body, DOWN, buff=0).shift(RIGHT * 0.3)
        left_foot = Triangle().set_fill(PURPLE, opacity=1).scale(0.5).next_to(left_leg, DOWN, buff=0)
        right_foot = Triangle().set_fill(PURPLE, opacity=1).scale(0.5).next_to(right_leg, DOWN, buff=0)
        left_eye = Circle(radius=0.1).set_fill(YELLOW, opacity=1).shift(UP * 1.7 + LEFT * 0.2)
        right_eye = Circle(radius=0.1).set_fill(YELLOW, opacity=1).shift(UP * 1.7 + RIGHT * 0.2)
        mouth = Rectangle(height=0.1, width=0.3).set_fill(BLACK, opacity=1).shift(UP * 1.2)

        human_toy = VGroup(head, body, left_arm, right_arm, left_leg, right_leg, left_foot, right_foot, left_eye, right_eye, mouth)

        self.play(FadeIn(human_toy))
        self.wait(2)

    def nextshape(self):
        text = Text("Observe the series of shapes. Draw the next shape")
        text.scale(0.75)
        text.to_edge(UP)
        self.play(Write(text))
    
        circle1 = Circle().set_color(BLUE).scale(1)
        triangle1 = Triangle().set_color(RED).scale(1)
        circle2 = Circle().set_color(GREEN).scale(1)
        triangle2 = Triangle().set_color(YELLOW).scale(1)
        circle3 = Circle().set_color(ORANGE).scale(1)

        shapes = VGroup(circle1, triangle1, circle2, triangle2, circle3).arrange(RIGHT, buff=1)

        self.play(FadeIn(shapes))

        self.wait(2)


        text1 = Text("The next shape is:")
        text1.scale(0.75)
        text1.shift(DOWN * 2 + LEFT * 4)
        self.play(Write(text1))

        triangle = Triangle()
        # Set the fill color and opacity
        #triangle.set_fill(BLUE, opacity=0.5)
        # Set the stroke color and width
        triangle.set_stroke(WHITE, width=4)
        triangle.shift(DOWN * 3)
        # Add the triangle to the scene
        self.play(Create(triangle))
        # Wait for 2 seconds before ending the scene
        self.wait(2)



    def differentshape(self):
        text = Text("Observe the shapes in each row. Mark the different one by putting mark")
        text.scale(0.5)
        text.to_edge(UP)
        self.play(Write(text))

        # First row of shapes
        circle1 = Circle().set_color(BLUE).scale(0.5)
        circle2 = Circle().set_color(BLUE).scale(0.5)
        triangle1 = Triangle().set_color(RED).scale(0.5)
        circle3 = Circle().set_color(BLUE).scale(0.5)

        row1 = VGroup(circle1, circle2, triangle1, circle3).arrange(RIGHT, buff=1)

        # Display first row
        self.play(FadeIn(row1))

        self.wait(2)

        # Mark the odd one in the first row
        cross1 = Cross(triangle1).set_color(YELLOW).scale(0.5)
        mark_row1 = VGroup(row1, cross1)
        self.play(Create(cross1))

        self.wait(2)

        # Shift the first row upward along with the mark
        self.play(mark_row1.animate.shift(UP * 1))

        # Second row of shapes
        triangle2 = Triangle().set_color(RED).scale(0.5)
        square1 = Square().set_color(GREEN).scale(0.5)
        triangle3 = Triangle().set_color(RED).scale(0.5)
        triangle4 = Triangle().set_color(RED).scale(0.5)

        row2 = VGroup(triangle2, square1, triangle3, triangle4).arrange(RIGHT, buff=1)

        # Shift the second row downward to account for the shift of the first row
        row2.shift(DOWN * 1)

        # Display second row
        self.play(FadeIn(row2))

        self.wait(2)

        # Mark the odd one in the second row
        cross2 = Cross(square1).set_color(YELLOW).scale(0.5)
        self.play(Create(cross2))

        self.wait(2)


    
    def SetDeveloperList(self):
        self.DeveloperList="SURADHYA REDDY"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Shapes.py"

if __name__ == "__main__":
    scene = Grade1Chapter2Shapes()
    scene.render()