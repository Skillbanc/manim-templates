from manim import *

class EquiFractions(Scene):
    def construct(self):
        self.Example1()
        self.Example2()
        self.Example3()
        self.Example4()

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
        group1.shift(UP*2 + LEFT * 3)

        # Add group1 to the scene
        self.play(Create(square1), Create(vertical_line1), Create(horizontal_line1), Create(shaded_area1))
        
        # Create the text "1/4" and position it below square1
        text1 = Tex(r"$\frac{1}{4}$").next_to(square1, DOWN)
        text1.shift(DOWN*1 + LEFT * 3)
        
        # Add text1 to the scene
        self.play(Write(text1))

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
        group2.shift(UP*2 + RIGHT * 3)

        # Add group2 to the scene
        self.play(Create(square2))
        self.play(Create(vertical_lines2), Create(horizontal_line2))
        
        # Play each shaded area separately for square2
        self.play(FadeIn(shaded_area2_1))
        self.play(FadeIn(shaded_area2_2))
        
        # Create the text "1/4" and position it below square2
        text2 = Tex(r"$\frac{1}{4}$").next_to(square2, DOWN)
        text2.shift(DOWN*1 + RIGHT * 3)

        # Add text2 to the scene
        self.play(Write(text2))

    def Example3(self):
        # Define the radius of the square
        radius = 1
        
        # Create a square with the specified radius (side length will be 2 * radius)
        side_length = radius * 2
        square3 = Square(side_length=side_length)
        
        # Create vertical and horizontal lines matching the radius of the square
        vertical_lines3 = VGroup(
            Line(start=[-radius / 2, -radius, 0], end=[-radius / 2, radius, 0]),
            Line(start=[0, -radius, 0], end=[0, radius, 0]),
            Line(start=[radius / 2, -radius, 0], end=[radius / 2, radius, 0])
        )
        horizontal_line3 = Line(start=[-radius, 0, 0], end=[radius, 0, 0])

        # Group all elements of square3
        group3 = VGroup(square3, vertical_lines3, horizontal_line3)

        # Create polygons to shade two quarters of square3
        shaded_area3_1 = Polygon(
            [0, 0, 0], [0, radius, 0], [radius / 2, radius, 0], [radius / 2, 0, 0],
            fill_opacity=0.5, fill_color=BLUE
        )
        shaded_area3_2 = Polygon(
            [0, 0, 0], [0, -radius, 0], [radius / 2, -radius, 0], [radius / 2, 0, 0],
            fill_opacity=0.5, fill_color=BLUE
        )

        # Add shaded areas to group3
        group3.add(shaded_area3_1, shaded_area3_2)
        
        # Shift square3 to its position
        group3.shift(DOWN*2 + LEFT * 3)

        # Add group3 to the scene
        self.play(Create(square3))
        self.play(Create(vertical_lines3), Create(horizontal_line3))
        
        # Play each shaded area separately for square3
        self.play(FadeIn(shaded_area3_1))
        self.play(FadeIn(shaded_area3_2))
        
        # Create the text "1/4" and position it below square3
        text3 = Tex(r"$\frac{1}{4}$").next_to(square3, DOWN)
        text3.shift(DOWN*1 + LEFT * 3)

        # Add text3 to the scene
        self.play(Write(text3))

    def Example4(self):
        # Define the radius of the square
        radius = 1
        
        # Create a square with the specified radius (side length will be 2 * radius)
        side_length = radius * 2
        square4 = Square(side_length=side_length)
        
        # Create vertical and horizontal lines matching the radius of the square
        vertical_lines4 = VGroup(
            Line(start=[-radius / 2, -radius, 0], end=[-radius / 2, radius, 0]),
            Line(start=[0, -radius, 0], end=[0, radius, 0]),
            Line(start=[radius / 2, -radius, 0], end=[radius / 2, radius, 0])
        )
        horizontal_line4 = Line(start=[-radius, 0, 0], end=[radius, 0, 0])

        # Group all elements of square4
        group4 = VGroup(square4, vertical_lines4, horizontal_line4)

        # Create polygons to shade two quarters of square4
        shaded_area4_1 = Polygon(
            [0, 0, 0], [0, radius, 0], [radius / 2, radius, 0], [radius / 2, 0, 0],
            fill_opacity=0.5, fill_color=BLUE
        )
        shaded_area4_2 = Polygon(
            [0, 0, 0], [0, -radius, 0], [radius / 2, -radius, 0], [radius / 2, 0, 0],
            fill_opacity=0.5, fill_color=BLUE
        )

        # Add shaded areas to group4
        group4.add(shaded_area4_1, shaded_area4_2)
        
        # Shift square4 to its position
        group4.shift(DOWN*2 + RIGHT * 3)

        # Add group4 to the scene
        self.play(Create(square4))
        self.play(Create(vertical_lines4), Create(horizontal_line4))
        
        # Play each shaded area separately for square4
        self.play(FadeIn(shaded_area4_1))
        self.play(FadeIn(shaded_area4_2))
        
if __name__ == "__main__":
    scene = EquiFractions()
    scene.render()