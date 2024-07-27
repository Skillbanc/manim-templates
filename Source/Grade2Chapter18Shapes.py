from manim import *
from AbstractAnim import AbstractAnim
import cvo


class Grade2Chapter18Shapes(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.diffshapes()
        self.fadeOutCurrentScene()
        self.matchshapes()
        self.fadeOutCurrentScene()
        self.Counttriangles()
        self.fadeOutCurrentScene()
        self.CountSquares()
        self.fadeOutCurrentScene()
        
        self.differentshape()
        self.fadeOutCurrentScene()
        self.JoinDotsToDrawShapes()
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
        
    def matchshapes(self):
        text = Text("Match the shapes with their similar shapes on the right ")
        text.scale(0.75)
        text.to_edge(UP)
        self.play(Write(text))

       


        square1 = Square(side_length=1, color=BLUE)
        square2 = Square(side_length=1, color=BLUE)
        rectangle1 = Rectangle(width=2, height=1, color=GREEN)
        rectangle2 = Rectangle(width=2, height=1, color=GREEN)
        triangle1 = Triangle().scale(0.7).set_color(RED)
        triangle2 = Triangle().scale(0.7).set_color(RED)
        circle1 = Circle(radius=0.7, color=WHITE)
        circle2 = Circle(radius=0.7, color=WHITE)

        # Arrange shapes in columns
        shapes_col1 = VGroup(square1, rectangle1, triangle1, circle1).arrange(DOWN, buff=0.5)
        shapes_col2 = VGroup(circle2, triangle2, square2, rectangle2).arrange(DOWN, buff=0.5)

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



    def Counttriangles(self):
        instruction_text = Text("Look at the picture and write how many upward facing triangles are there")
        instruction_text.scale(0.5)
        instruction_text.to_edge(UP)
        self.play(Write(instruction_text))
        
        # Step 2: Create and display the shapes in the middle of the screen
        shapes = VGroup(
            Polygon([0, 0, 0], [2, 0, 0], [1, 1.73, 0], color=WHITE),  # Triangle 1
            Polygon([2, 0, 0], [4, 0, 0], [3, 1.73, 0], color=WHITE),  # Triangle 2
            Polygon([0, 0, 0], [4, 0, 0], [2, 3.46, 0], color=WHITE),  # Larger triangle
            Polygon([1, 1.73, 0], [3, 1.73, 0], [2, 3.46, 0], color=WHITE)  # Triangle 3
        )
        shapes.move_to(ORIGIN)
        
        self.play(Create(shapes))
        self.wait(2)
        
        # Step 3: Highlight each triangle and count them
        triangle_count = 0
        for shape in shapes:
            self.play(Indicate(shape, color=RED))
            triangle_count += 1
            self.wait(1)
        
        # Step 4: Display the count text below the shapes with some space
        count_text = Text(f'There are {triangle_count} triangles.', font_size=24, color=WHITE)
        count_text.next_to(shapes, DOWN, buff=0.5)
        self.play(FadeIn(count_text))
        self.wait(2)

        # Step 5: Fade out everything
        self.play(FadeOut(shapes), FadeOut(count_text), FadeOut(instruction_text))


    def CountSquares(self):
        instruction_text = Text("Look at the picture and write how many squares are there")
        instruction_text.scale(0.5)
        instruction_text.to_edge(UP)
        self.play(Write(instruction_text))
        
        # Step 2: Create the large square
        large_square = Square(side_length=4, color=WHITE)
        
        # Create smaller squares to fit inside the large square
        small_squares = VGroup(
            Square(side_length=1, color=WHITE).shift(LEFT * 1.5 + DOWN * 1.5),  # Bottom-left
            Square(side_length=1, color=WHITE).shift(RIGHT * 1.5 + DOWN * 1.5),  # Bottom-right
            Square(side_length=1, color=WHITE).shift(LEFT * 1.5 + UP * 1.5),    # Top-left
            Square(side_length=1, color=WHITE).shift(RIGHT * 1.5 + UP * 1.5)    # Top-right
        )
        
        # Position the large square and small squares
        large_square.move_to(ORIGIN)
        small_squares.move_to(ORIGIN)
        
        # Display the large square and small squares
        self.play(Create(large_square))
        self.wait(1)
        self.play(Create(small_squares))
        self.wait(2)
        
        # Step 3: Highlight each square and count them
        square_count = 1  # Count the large square
        self.play(Indicate(large_square, color=RED))
        self.wait(1)
        
        for shape in small_squares:
            self.play(Indicate(shape, color=RED))
            square_count += 1
            self.wait(1)
        
        # Step 4: Display the count text below the large square with some space
        count_text = Text(f'There are {square_count} squares.', font_size=24, color=WHITE)
        count_text.next_to(large_square, DOWN, buff=0.5)
        self.play(FadeIn(count_text))
        self.wait(2)

        # Step 5: Fade out everything
        self.play(FadeOut(large_square), FadeOut(small_squares), FadeOut(count_text), FadeOut(instruction_text))


    def differentshape(self):
        text = Text("Observe the shapes in each row. Mark the different one by putting a crosss mark")
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

    def JoinDotsToDrawShapes(self):
    
        # Define points for various shapes
        shapes = {
            "Triangle": {
                "points": [np.array([0, 2, 0]), np.array([-2, -2, 0]), np.array([2, -2, 0])],
                "color": BLUE,
                "heading": "Join Dots to Form Triangle"
            },
            "Square": {
                "points": [np.array([-1, 1, 0]), np.array([1, 1, 0]), np.array([1, -1, 0]), np.array([-1, -1, 0])],
                "color": RED,
                "heading": "Join Dots to Form Square"
            },
            "Pentagon": {
                "points": [
                    np.array([0, 2, 0]),
                    np.array([1.9, 0.6, 0]),
                    np.array([1.2, -1.6, 0]),
                    np.array([-1.2, -1.6, 0]),
                    np.array([-1.9, 0.6, 0])
                ],
                "color": GREEN,
                "heading": "Join Dots to Form Pentagon"
            },
            "Rectangle": {
                "points": [
                    np.array([-2, 1, 0]),
                    np.array([2, 1, 0]),
                    np.array([2, -1, 0]),
                    np.array([-2, -1, 0])
                ],
                "color": YELLOW,
                "heading": "Join Dots to Form Rectangle"
            },
            "Rhombus": {
                "points": [
                    np.array([0, 2, 0]),
                    np.array([2, 0, 0]),
                    np.array([0, -2, 0]),
                    np.array([-2, 0, 0])
                ],
                "color": PURPLE,
                "heading": "Join Dots to Form Rhombus"
            },
        }

        # Function to create dots and lines
        def create_shape(points, dot_color=WHITE, line_color=WHITE, close=True):
            dots = VGroup(*[Dot(point, color=dot_color) for point in points])
            lines = VGroup(*[Line(points[i], points[(i + 1) % len(points)], color=line_color) for i in range(len(points) - (0 if close else 1))])
            return dots, lines

        # Create and animate each shape
        for shape_name, info in shapes.items():
            points = info["points"]
            color = info["color"]
            heading_text = info["heading"]

            dots, lines = create_shape(points, dot_color=WHITE, line_color=color, close=(shape_name != "Circle"))

            # Create heading text
            heading = Text(heading_text, font_size=36).to_edge(UP)

            # Animate dots
            self.play(FadeIn(heading))
            self.play(LaggedStart(*[GrowFromCenter(dot) for dot in dots], lag_ratio=0.5))
            self.play(LaggedStart(*[Create(line) for line in lines], lag_ratio=0.5))
            self.wait(1)

            # Fade out the current shape before moving to the next
            self.play(FadeOut(heading), FadeOut(dots), FadeOut(lines))


    def SetDeveloperList(self): 
       self.DeveloperList="Snehith" 
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Shapes.py"



if __name__ == "__main__":
    scene = Grade2Chapter18Shapes()
    scene.render()