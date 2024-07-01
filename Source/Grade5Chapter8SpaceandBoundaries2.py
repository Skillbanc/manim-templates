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

class Chap8G5_SandB_2(AbstractAnim):
    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.Anim1()
        self.fadeOutCurrentScene()
        self.Anim2()
        self.fadeOutCurrentScene()
        self.Anim3()
        self.fadeOutCurrentScene()
        self.Anim4()
        self.fadeOutCurrentScene()
        self.Anim5()
        self.fadeOutCurrentScene()

    def Anim1(self):
        heading = Text("Area of Different Shapes-Triangle", font_size=36).to_edge(UP)

        # Create the grid
        grid = VGroup()
        for x in range(5):
            grid.add(Line(np.array([x-2, -2, 0]), np.array([x-2, 2, 0]), color=WHITE))
            grid.add(Line(np.array([-2, x-2, 0]), np.array([2, x-2, 0]), color=WHITE))

        # Create the right-angled triangle
        triangle = Polygon(
            np.array([-2, 2, 0]),   # Top left corner
            np.array([2, 2, 0]),    # Top right corner
            np.array([2, -2, 0]),   # Bottom right corner
            color=BLACK
        ).set_fill(RED, opacity=0.5)

        # Labels for area
        area_text = Text("8 square cm", font_size=24, color=RED).next_to(triangle, DOWN)

        # Create whole squares and half squares within the triangle
        whole_squares = VGroup(
            Square(side_length=1, fill_color=RED, fill_opacity=0.5).move_to(np.array([-0.5, 1.5, 0])),
            Square(side_length=1, fill_color=RED, fill_opacity=0.5).move_to(np.array([0.5, 1.5, 0])),
            Square(side_length=1, fill_color=RED, fill_opacity=0.5).move_to(np.array([1.5, 1.5, 0])),
            Square(side_length=1, fill_color=RED, fill_opacity=0.5).move_to(np.array([0.5, 0.5, 0])),
            Square(side_length=1, fill_color=RED, fill_opacity=0.5).move_to(np.array([1.5, 0.5, 0])),
            Square(side_length=1, fill_color=RED, fill_opacity=0.5).move_to(np.array([1.5, -0.5, 0]))
        )

        half_squares = VGroup(
            Polygon(np.array([-2, 2, 0]), np.array([-1, 2, 0]), np.array([-1, 1, 0]), color=BLACK).set_fill(GREEN, opacity=0.5),
            Polygon(np.array([-1, 1, 0]), np.array([0, 1, 0]), np.array([0, 0, 0]), color=BLACK).set_fill(GREEN, opacity=0.5),
            Polygon(np.array([0, 0, 0]), np.array([1,0 , 0]), np.array([1, -1, 0]), color=BLACK).set_fill(GREEN, opacity=0.5),
            Polygon(np.array([1, -1, 0]), np.array([2, -1, 0]), np.array([2, -2, 0]), color=BLACK).set_fill(GREEN, opacity=0.5)
        )

        # Add elements to the scene
        self.play(Write(heading))
        self.play(Create(grid))
        self.play(Create(triangle))
        self.play(Write(area_text))

        # Animate the breakdown of the triangle into whole squares and half squares
        self.play(FadeOut(triangle))
        self.play(Create(whole_squares))
        self.wait(1)
        self.play(Create(half_squares))

        # Add explanation for area calculation
        explanation = Text(
            "The area of the triangle is 8 square cm.\n"
            "It is made up of 6 whole squares (6 sq cm) and 4 half squares (2 sq cm).",
            font_size=24
        ).next_to(area_text, DOWN)
        self.play(Write(explanation))
        self.wait(2)

        self.play(
            FadeOut(triangle),
            FadeOut(whole_squares),
            FadeOut(half_squares)
        )

    def Anim2(self):
        heading = Text("Area of Different Shapes-Octagon", font_size=36).to_edge(UP)
        grid = VGroup()
        for x in range(4):
            grid.add(Line(np.array([x-1.5, -1.5, 0]), np.array([x-1.5, 1.5, 0]), color=WHITE))
            grid.add(Line(np.array([-1.5, x-1.5, 0]), np.array([1.5, x-1.5, 0]), color=WHITE))



        octagon = VGroup(
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([0, 1, 0])),
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([0, 0, 0])),
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([0, -1, 0])),
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([1, 0, 0])),
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([-1, 0, 0])),
            Polygon(np.array([-1.5, 0.5, 0]), np.array([-0.5, 0.5, 0]), np.array([-0.5, 1.5, 0])).set_fill(BLUE, opacity=0.5),
            Polygon(np.array([1.5, 0.5, 0]), np.array([0.5, 0.5, 0]), np.array([0.5, 1.5, 0])).set_fill(BLUE, opacity=0.5),
            Polygon(np.array([-1.5, -0.5, 0]), np.array([-0.5, -0.5, 0]), np.array([-0.5, -1.5, 0])).set_fill(BLUE, opacity=0.5),
            Polygon(np.array([1.5, -0.5, 0]), np.array([0.5, -1.5, 0]), np.array([0.5, -0.5, 0])).set_fill(BLUE, opacity=0.5)
            )

        # Labels for octagon area
        octagon_area_text = Text("7 square cm", font_size=24, color=BLUE).next_to(octagon, DOWN)

        # # Add octagon to the scene
        self.play(Write(heading))
        self.play(Create(grid))
        self.play(Create(octagon))
        self.play(Write(octagon_area_text))

        # Final explanation for octagon area
        octagon_explanation = Text(
            "The area of the octagon is 7 square cm.\n"
            "It is made up of 5 whole squares (5 sq cm) and 4 half squares(2 sq cm).",
            font_size=24
        ).next_to(octagon_area_text,DOWN)
        self.play(Write(octagon_explanation))
        self.wait(2)

    def Anim3(self):
        heading = Text("Area of Different Shapes - Square", font_size=36).to_edge(UP)

        # Create the 2x2 grid
        grid = VGroup()
        for x in range(3):
            grid.add(Line(np.array([x-1, -1, 0]), np.array([x-1, 1, 0]), color=WHITE))
            grid.add(Line(np.array([-1, x-1, 0]), np.array([1, x-1, 0]), color=WHITE))

        # Add heading and grid to the scene
        self.play(Write(heading))
        self.play(Create(grid))
        self.wait(2)

        # Create the squares making up the larger square
        squares = VGroup(
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([0.5, 0.5, 0])),
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([-0.5, 0.5, 0])),
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([-0.5, -0.5, 0])),
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([0.5, -0.5, 0]))
        )

        # Add squares and area text to the scene
        self.play(Create(squares))
        square_area_text = Text("4 square cm", font_size=24, color=BLUE).next_to(squares, DOWN)
        self.play(Write(square_area_text))

        # Explanation text
        square_explanation = Text(
            "The area of the square is 4 square cm.\n"
            "It is made up of 4 whole squares (4 sq cm).",
            font_size=24
        ).next_to(square_area_text, DOWN)

        self.play(Write(square_explanation))
        self.wait(2)

    def Anim4(self):
        heading = Text("Area of Different Shapes - Rectangle", font_size=36).to_edge(UP)

        # Create the 4x8 grid
        grid = VGroup()
        for x in range(9):  # 8 vertical lines for the grid
            grid.add(Line(np.array([x-4, -2, 0]), np.array([x-4, 2, 0]), color=WHITE))
        for y in range(5):  # 4 horizontal lines for the grid
            grid.add(Line(np.array([-4, y-2, 0]), np.array([4, y-2, 0]), color=WHITE))

        # Add heading and grid to the scene
        self.play(Write(heading))
        self.play(Create(grid))
        self.wait(2)

        # Create the 2x6 rectangle within the grid
        rectangle = VGroup(
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([-2.5, 0.5, 0])),
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([-1.5, 0.5, 0])),
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([-0.5, 0.5, 0])),
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([0.5, 0.5, 0])),
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([1.5, 0.5, 0])),
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([2.5, 0.5, 0])),
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([-2.5, -0.5, 0])),
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([-1.5, -0.5, 0])),
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([-0.5, -0.5, 0])),
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([0.5, -0.5, 0])),
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([1.5, -0.5, 0])),
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([2.5, -0.5, 0]))
        )

        # Add rectangle to the scene
        self.play(Create(rectangle))

        # Add area text
        rectangle_area_text = Text("12 square cm", font_size=24, color=BLUE).next_to(rectangle, 5 * DOWN)
        self.play(Write(rectangle_area_text))

        # Explanation text
        rectangle_explanation = Text(
            "The area of the rectangle is 12 square cm.\n"
            "It is made up of 12 whole squares (12 sq cm).",
            font_size=24
        ).next_to(rectangle_area_text, DOWN)
        self.play(Write(rectangle_explanation))
        self.wait(2)

        # Divide the rectangle into 2 equal rectangles
        dividing_line = Line(np.array([0, 1, 0]), np.array([0, -1, 0]), color=WHITE)
        self.play(Create(dividing_line))

        # Update area text for the divided rectangles
        divided_area_text = Text("Each rectangle: 6 square cm", font_size=24, color=BLUE).next_to(dividing_line, 5 * DOWN)
        self.play(Transform(rectangle_area_text, divided_area_text))

        # Update explanation text
        divided_explanation = Text(
            "The rectangle is divided into two equal parts.\n"
            "Each part has an area of 6 square cm.",
            font_size=24
        ).next_to(divided_area_text, DOWN)
        

        # Animate the separation of the two equal rectangles
        left_rectangle = VGroup(
            *[rect for rect in rectangle if rect.get_center()[0] < 0]
        )
        right_rectangle = VGroup(
            *[rect for rect in rectangle if rect.get_center()[0] >= 0]
        )

        self.play(
            left_rectangle.animate.shift(LEFT ),
            right_rectangle.animate.shift(RIGHT)
        )
        self.wait(2)
        self.play(Transform(rectangle_explanation, divided_explanation))
        self.wait(2)

    def Anim5(self):
        heading = Text("Area of a Rectangle", font_size=36).to_edge(UP)
        
        # Create the 4x8 grid
        grid = VGroup()
        for x in range(9):  # 8 vertical lines for the grid
            grid.add(Line(np.array([x-4, -2, 0]), np.array([x-4, 2, 0]), color=WHITE))
        for y in range(5):  # 4 horizontal lines for the grid
            grid.add(Line(np.array([-4, y-2, 0]), np.array([4, y-2, 0]), color=WHITE))

        # Add heading and grid to the scene
        self.play(Write(heading))
        self.play(Create(grid))
        self.wait(2)

        # Create the 2x6 rectangle within the grid
        rectangle = VGroup(
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([-2.5, 0.5, 0])),
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([-1.5, 0.5, 0])),
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([-0.5, 0.5, 0])),
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([0.5, 0.5, 0])),
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([1.5, 0.5, 0])),
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([2.5, 0.5, 0])),
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([-2.5, -0.5, 0])),
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([-1.5, -0.5, 0])),
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([-0.5, -0.5, 0])),
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([0.5, -0.5, 0])),
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([1.5, -0.5, 0])),
            Square(side_length=1, fill_color=BLUE, fill_opacity=0.5).move_to(np.array([2.5, -0.5, 0]))
        )

        # Add rectangle to the scene
        self.play(Create(rectangle))

        # Add area text
        rectangle_area_text = Text("12 square cm", font_size=24, color=BLUE).next_to(rectangle, 5 * DOWN)
        self.play(Write(rectangle_area_text))
        self.wait(2)

        # Highlight the width by counting each square
        for i, square in enumerate(rectangle[:6]):
            count_text = Text(str(i+1), font_size=24, color=YELLOW).move_to(square)
            self.play(Indicate(square), Write(count_text))
            self.wait(0.5)
            self.remove(count_text)

        width_text = Text("Width = 6 squares", font_size=24, color=YELLOW).next_to(rectangle_area_text, DOWN)
        self.play(Write(width_text))
        self.wait(1)

        # Highlight the height by counting each square
        for i, square in enumerate([rectangle[0], rectangle[6]]):
            count_text = Text(str(i+1), font_size=24, color=YELLOW).move_to(square.get_center())
            self.play(Indicate(square), Write(count_text))
            self.wait(0.5)
            self.remove(count_text)

        height_text = Text("Height = 2 squares", font_size=24, color=YELLOW).next_to(width_text, DOWN)
        self.play(Write(height_text))
        self.wait(1)

        self.play(FadeOut(width_text), FadeOut(height_text))

        # Show the multiplication to find the area
        multiplication_text = Text("Area = Length × Width", font_size=24, color=GREEN).next_to(rectangle_area_text, DOWN)
        self.play(Write(multiplication_text))
        self.wait(1)

        multiplication_example = Text("Area = 6 × 2 = 12 units", font_size=24, color=GREEN).next_to(multiplication_text, DOWN)
        self.play(Write(multiplication_example))
        self.wait(2)

            

            
               
if __name__ == "__main__":
    scene = Chap8G5_SandB_2()
    scene.render()
    