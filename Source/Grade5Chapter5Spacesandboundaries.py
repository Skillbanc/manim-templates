from manim import *
from AbstractAnim import AbstractAnim
import cvo

class Spacesandboundaries(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.square()
        self.fadeOutCurrentScene()
        self.triangle()
        self.fadeOutCurrentScene()
        self.rectangle()
        self.fadeOutCurrentScene()
        self.circle()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

    def square(self):
        self.positionChoice = [[-4, 0, 0], [0, 2, 0], [0, -2, 0]]
        self.angleChoice=[(TAU/3),(TAU/3)]
        self.isRandom = False
       

        p10 = cvo.CVO().CreateCVO("Square", "")
        p11 = cvo.CVO().CreateCVO("Perimeter ", "4 * a")
        p12 = cvo.CVO().CreateCVO("Area ", "a * a")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10, p10)
        self.wait(2)

        square = Square(side_length=2, color=BLUE).shift([3, 2, 0])
        side1 = Text("a cm", font_size=24).next_to(square, LEFT)
        side2 = Text("a cm", font_size=24).next_to(square, UP)
        side3 = Text("a cm", font_size=24).next_to(square, DOWN)
        side4 = Text("a cm", font_size=24).next_to(square, RIGHT)
        square_text = Text("""
                    Perimeter = 4 * a 
                    Area = a * a
                           """, font_size=24).next_to(side3, DOWN)

        self.play(Create(square))
        self.play(Write(side1), Write(side2), Write(side3), Write(side4))
        self.wait(3)
        self.play(Write(square_text))
        self.wait(2)

        self.fadeOutCurrentScene()

        # Second demonstration with specific side length
        title = Text("Square", font_size=30).to_edge(UP)
        square = Square(side_length=4, color=BLUE)
        square.shift(LEFT * 3)

        # Labels for known sides
        side1 = Text("4 cm", font_size=24).next_to(square, LEFT)
        side2 = Text("4 cm", font_size=24).next_to(square, UP)
        side3 = Text("4 cm", font_size=24).next_to(square, DOWN)
        side4 = Text("4 cm", font_size=24).next_to(square, RIGHT)
        
        # Steps for perimeter and area
        perimeter_steps = [
            "Perimeter = 4 * side",
            "           = 4 * 4 = 16",
            "Perimeter of square = 16 cm",
        ]
        area_steps = [
            "Area = a * a",
            "     = 4 * 4 = 16",
            "Area of square = 16",
        ]
        area_units = MathTex(r"\text{cm}^2", font_size=24)

        # Create VGroups for perimeter and area steps with extra space
        perimeter_group = VGroup(*[Text(step, font_size=24) for step in perimeter_steps]).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        area_text_group = VGroup(*[Text(step, font_size=24) for step in area_steps]).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        # Position the area_units next to the last element of area_text_group
        area_units.next_to(area_text_group[-1], RIGHT)
        
        # Combine area_text_group and area_units into one group
        area_group = VGroup(area_text_group, area_units)

        perimeter_group.next_to(side4, UP + RIGHT * 2)
        area_group.next_to(perimeter_group, DOWN, buff=0.5)

        # Animate the square and labels
        self.play(Write(title))
        self.play(Create(square))
        self.play(Write(side1), Write(side2), Write(side3), Write(side4))
        self.wait(2)

        # Animate each step with a 1-second gap for perimeter
        for step in perimeter_group:
            self.play(Write(step))
            self.wait(1)
        
        # Animate each step with a 1-second gap for area
        for step in area_text_group:
            self.play(Write(step))
            self.wait(1)
        self.play(Write(area_units))
        
        self.wait(3)


    def triangle(self):
        self.positionChoice=[(-4.5,1.5,0),(-4.5,-1.5,0)]
        self.angleChoice=[(TAU/2)]
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Triangle", "")
        p11 = cvo.CVO().CreateCVO("Perimeter ", "a + b + c")
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

        triangle = Triangle().scale(2).set_color(RED)
    
        side1 = Text("a cm", font_size=24).next_to(triangle, LEFT)
        side2 = Text("b cm", font_size=24).next_to(triangle, RIGHT)
        side3 = Text("c cm", font_size=24).next_to(triangle, DOWN)
        
       
        triangle_text = Text("Triangle: Perimeter = a + b + c", font_size=24)
        triangle_text.next_to(side3, DOWN)
        self.play(Create(triangle))
        self.play(Write(side1), Write(side2), Write(side3))
        self.play(Write(triangle_text))
        self.wait(2)

        self.fadeOutCurrentScene()

        title = Text("Triangle", font_size=30).to_edge(UP)
        triangle = Triangle().scale(2).set_color(RED)
        triangle.shift(LEFT * 3)


        # Labels for known sides
        side1 = Text("6 cm", font_size=24).next_to(triangle, LEFT)
        side2 = Text("8 cm", font_size=24).next_to(triangle, RIGHT)
        side3 = Text("10 cm", font_size=24).next_to(triangle, DOWN)
 
        # Perimeter label
        perimeter_text_lines = [
            "Perimeter = a + b + c",
            "= 6 + 8 + 10",
            "Perimeter of triangle = 24 cm"
        ]
        perimeter_label = VGroup(*[Text(line, font_size=30) for line in perimeter_text_lines])
        perimeter_label.arrange(DOWN, aligned_edge=LEFT).next_to(side2,RIGHT*3)

        # Animation
        self.play(Write(title))
        self.play(Create(triangle))
        self.play(Write(side1))
        self.wait(1)
        self.play(Write(side2))
        self.wait(1)
        self.play(Write(side3))
        self.wait(1)
        
        for line in perimeter_label:
            self.play(Write(line))
            self.wait(1)
        
        self.wait(2)

    
    def rectangle(self):
        self.positionChoice=[(-4.5,1.5,0),(-3.5,-1.5,0)]
        self.angleChoice=[(TAU/2)]
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Rectangle", "")
        p11 = cvo.CVO().CreateCVO("Perimeter ", " 2 * (length + width)")
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

        length = 4   # Length of the rectangle
        width = 2   # Width of the rectangle

        # Create the rectangle and move it towards the right
        rectangle = Rectangle(width=length, height=width, color=BLUE)
        rectangle.shift(RIGHT * 3)
        side1 = Text("a cm", font_size=24).next_to(rectangle, UP)
        side2 = Text("b cm", font_size=24).next_to(rectangle, RIGHT)

        rectangle_text = Text("Perimeter = 2 * (length + width)", font_size=24)
        rectangle_text.next_to(rectangle, DOWN )

        self.play(Create(rectangle))
        self.wait(2)
        self.play(Write(side1), Write(side2))
        self.wait(2)
        self.play(Write(rectangle_text))
        self.wait(2)

        self.fadeOutCurrentScene()

        title = Text("Rectangle", font_size=30).to_edge(UP)
        length = 6  # Length of the rectangle
        width = 4   # Width of the rectangle

        # Create the rectangle
        rectangle = Rectangle(width=length, height=width, color=BLUE)
        rectangle.shift(LEFT * 3)

        # Labels for sides
        side1_label = Text(f"{length} cm", font_size=24).next_to(rectangle, UP)
        side2_label = Text(f"{width} cm", font_size=24).next_to(rectangle, RIGHT)
        side3_label = Text(f"{length} cm", font_size=24).next_to(rectangle, DOWN)
        side4_label = Text(f"{width} cm", font_size=24).next_to(rectangle, LEFT)

        # Display the rectangle and labels
        self.play(Write(title))
        self.play(Create(rectangle))
        self.wait(2)
        self.play(Write(side1_label), Write(side2_label), Write(side3_label), Write(side4_label))
        self.wait(2)

        # Perimeter label
        perimeter = 2 * (length + width)
        perimeter_lines = [
            f"Perimeter = 2 * (length + width)",
            f"           = 2 * ({length} + {width})",
            f"           = {perimeter} cm"
        ]

        # Create VGroup for perimeter text
        perimeter_label = VGroup(*[Text(line, font_size=30) for line in perimeter_lines]).arrange(DOWN, aligned_edge=LEFT)
        perimeter_label.next_to(side2_label, RIGHT)

        # Animate each line of the perimeter label with a 1-second gap
        for line in perimeter_label:
            self.play(Write(line))
            self.wait(1)

        self.wait(2)
        self.fadeOutCurrentScene()

        blackboard = Rectangle(width=6, height=5, color=WHITE).shift(LEFT * 4)
        blackboard_text = Text("Blackboard", font_size=24).next_to(blackboard, UP)

        # Create the squares
        squares = VGroup()
        square_side = 1  # Adjust the side length to fit the new blackboard size
        num_rows = 5
        num_cols = 6
        for i in range(num_rows):
            for j in range(num_cols):
                square = Square(side_length=square_side, color=BLUE, fill_opacity=0.5)
                square.move_to(blackboard.get_corner(DL) + np.array([square_side / 2 + j * square_side, square_side / 2 + i * square_side, 0]))
                squares.add(square)

        # Create labels and explanation
        area_text_lines = [
            "Area = Number of squares in the blackboard",
            "= 6 * 5 = 30",
            "Area of the blackboard = 30 squares"
        ]
        area_text = VGroup(*[Text(line, font_size=24).move_to(np.array([3, 2 - i, 0])) for i, line in enumerate(area_text_lines)])

        # Create number labels for the first row and first column
        number_labels = VGroup()
        for i in range(1, num_cols + 1):
            number_label = Text(str(i), font_size=24)
            number_label.move_to(squares[i - 1].get_center())
            number_labels.add(number_label)

        for i in range(1, num_rows + 1):
            number_label = Text(str(i), font_size=24)
            number_label.move_to(squares[(i - 1) * num_cols].get_center())
            number_labels.add(number_label)

        # Animation
        self.play(Create(blackboard), Write(blackboard_text))
        self.wait(2)

        # Show the first line of area text
        self.play(Write(area_text[0]))
        self.wait(1)

        # Create the first row and first column of squares with numbers
        first_row_and_col_squares = VGroup(*[squares[i * num_cols] for i in range(num_rows)] + [squares[j] for j in range(num_cols)])
        self.play(LaggedStart(*[Create(square) for square in first_row_and_col_squares], lag_ratio=0.1))
        self.play(Write(number_labels))
        self.wait(1)

        # Create the rest of the squares
        remaining_squares = VGroup(*[squares[i] for i in range(len(squares)) if squares[i] not in first_row_and_col_squares])
        self.play(LaggedStart(*[Create(square) for square in remaining_squares], lag_ratio=0.1))
        self.wait(1)

        # Show the remaining lines of area text
        self.play(Write(area_text[1]))
        self.wait(1)
        self.play(Write(area_text[2]))
        self.wait(3)


    def circle(self):
        self.positionChoice=[(-4.5,1.5,0),(-3.5,-1.5,0)]
        self.angleChoice=[(TAU/2)]
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Circle", "")
        p11 = cvo.CVO().CreateCVO("Perimeter ", "$2 * \\pi * radius$")
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

       
        circle1 = Circle(radius=1, color=YELLOW)
        circle1_text = MathTex(r"\text{Circle: Perimeter} = 2 \pi \times \text{radius}", font_size=24)
        circle1_text.next_to(circle1, DOWN)
        
        # Radius line and center point for first circle
        radius_line1 = Line(circle1.get_center(), circle1.get_right(), color=WHITE)
        center_point1 = Dot(point=circle1.get_center(), color=WHITE)
        radius_label1 = MathTex(r"\text{radius}", font_size=18).next_to(radius_line1, UP)
        center_label1 = MathTex(r"c", font_size=30).move_to(center_point1.get_center() + UP * 0.5)

        self.play(Create(circle1))
        self.play(Write(circle1_text))
        self.play(Create(radius_line1), Create(center_point1), Write(radius_label1))
        self.play(Write(center_label1))
        self.wait(2)
        self.fadeOutCurrentScene()

        # Second Circle
        radius = 2  # Radius of the circle
        perimeter = 2 * np.pi * radius  # Calculating perimeter

        title = Text("Circle", font_size=30).to_edge(UP)
        circle2 = Circle(radius=radius, color=RED)
        circle2.shift(LEFT * 3)

        # Radius line and center point for second circle
        radius_label = MathTex(f"\\text{{Radius}} = {radius} \\, \\text{{cm}}", font_size=24).next_to(circle2, UP)
        radius_line2 = Line(circle2.get_center(), circle2.get_right(), color=WHITE)
        center_point2 = Dot(point=circle2.get_center(), color=WHITE)
        radius_label2 = MathTex(f"\\text{{Radius}}", font_size=24).next_to(radius_line2, UP)
        center_label2 = MathTex(r"c", font_size=30).move_to(center_point2.get_center() + UP * 0.5)

        perimeter_label = VGroup(
            MathTex(r"\text{Perimeter} = 2 \pi \times \text{radius}", font_size=30),
            MathTex(r"= 2 \pi \times {:.2f}".format(radius), font_size=30),
            MathTex(r"= {:.2f} \, \text{{cm}}".format(perimeter), font_size=30)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(circle2, RIGHT*2)

        self.play(Write(title))
        self.play(Create(circle2))
        self.play(Create(radius_label))
        self.play(Create(radius_line2), Create(center_point2), Write(radius_label2))
        self.play(Write(center_label2))
        self.wait(2)
        self.play(LaggedStart(*[Write(step) for step in perimeter_label]), lag_ratio=1)
        self.wait(3)


    def SetDeveloperList(self):  
        self.DeveloperList="Shanmukha Priya"
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade5Chapter5Spacesandboundaries.py"

if __name__ == "__main__":
    scene = Spacesandboundaries()
    scene.render()