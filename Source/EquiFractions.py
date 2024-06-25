
import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo
from manim import *

class EquiFractions(AbstractAnim):
    def construct(self):
        self.Example()
        self.fadeOutCurrentScene()
        self.Example2()

    def Example(self):
        # Define the radius of the square
        radius = 1  # This makes the radius of the square equal to 2 units
        
        # Create a square with the specified radius (side length will be 2 * radius)
        side_length = radius * 2
        square = Square(side_length=side_length)
        
        # Create vertical and horizontal lines matching the radius of the square
        vertical_line = Line(start=[0, -radius, 0], end=[0, radius, 0])
        horizontal_line = Line(start=[-radius, 0, 0], end=[radius, 0, 0])

        # Group all elements to shift them together
        group = VGroup(square, vertical_line, horizontal_line)

        # Create a polygon to shade one quarter
        shaded_area = Polygon(
            [0, 0, 0], [0, radius, 0], [radius, radius, 0], [radius, 0, 0],
            fill_opacity=0.5, fill_color=BLUE
        )
        
        # Add the shaded area to the group
        group.add(shaded_area)
        
        # Shift the entire group to the left by 5 units
        group.shift(UP*1 + LEFT * 5)
        
        # Add the group to the scene
        self.play(Create(square), Create(vertical_line), Create(horizontal_line), Create(shaded_area))
        text = Tex(r"$\frac{1}{4}$",font_size = 80)
        text.shift(DOWN*1 +LEFT * 5)
        self.play(Write(text))

    def Example2(self):
    
        radius = 1  # This makes the radius of the square equal to 2 units
        
        # Create a square with the specified radius (side length will be 2 * radius)
        side_length = radius * 2
        square = Square(side_length=side_length)
        
        # Create vertical and horizontal lines matching the radius of the square
        vertical_lines = VGroup(
            Line(start=[-radius / 2, -radius, 0], end=[-radius / 2, radius, 0]),
            Line(start=[0, -radius, 0], end=[0, radius, 0]),
            Line(start=[radius / 2, -radius, 0], end=[radius / 2, radius, 0])
        )
        horizontal_line = Line(start=[-radius, 0, 0], end=[radius, 0, 0])

        # Group all elements to shift them together
        group = VGroup(square, vertical_lines, horizontal_line)

        # Create a polygon to shade one quarter
        shaded_area1 = Polygon(
            [0, 0, 0], [0, radius, 0], [radius / 2, radius, 0], [radius / 2, 0, 0],
            fill_opacity=0.5, fill_color=BLUE
        )
        shaded_area2 = Polygon(
            [0, 0, 0], [0, -radius, 0], [radius / 2, -radius, 0], [radius / 2, 0, 0],
            fill_opacity=0.5, fill_color=BLUE
        )
        # Add the shaded area to the group
        group.add(shaded_area1,shaded_area2)
        
        # Shift the entire group to the left by 5 units
        group.shift(LEFT * 2)

        # Add the group to the scene
        self.play(Create(square))
        self.play(Create(vertical_lines), Create(horizontal_line))
        self.play(Create(shaded_area1,shaded_area2))
        
        # Create the text "1/4" and position it below the square
        text = Text("1/4").next_to(square, DOWN)
        
        # Shift the text to the left by 5 units to match the square's position
        text.shift(UP*1 + LEFT * 2 )

        # Add the text to the scene
        self.play(Write(text))

if __name__ == "__main__":
    scene = EquiFractions()
    scene.render()
