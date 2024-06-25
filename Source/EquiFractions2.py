from manim import *

class EquiFractions2(Scene):
    def construct(self):
        self.EquiExp()
        self.Example1()
        self.Equall1()
        self.Example2()
        self.Equall2()
        self.Example3()
        self.Equall3()
        self.Example4()
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
        self.play(Create(square1), Create(vertical_line1), Create(horizontal_line1), Create(shaded_area1))
        
        # Create the text "1/4" and position it below square1
        text1 = Tex(r"$\frac{1}{4}$")
        text1.shift(DOWN * 2 + LEFT * 4)
        
        # Add text1 to the scene
        self.play(Write(text1))
    def Equall1(self):
        equals_signs = Tex("=").scale(1.5).shift(UP*0.1+LEFT*2.5)
        self.play(Write(equals_signs))

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
        self.play(Create(vertical_lines2), Create(horizontal_line2))
        
        # Play each shaded area separately for square2
        self.play(FadeIn(shaded_area2_1))
        self.play(FadeIn(shaded_area2_2))
        
        # Create the text "2/8" and position it below square2
        text2 = Tex(r"$\frac{2}{8}$")
        text2.shift(DOWN * 2 + LEFT * 1)

        # Add text2 to the scene
        self.play(Write(text2))
    def Equall2(self):
        equals_signs = Tex("=").scale(1.5).shift(UP*0.1+RIGHT*0.4)
        self.play(Write(equals_signs))


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
        self.play(Create(vertical_lines3), Create(horizontal_line3))
        
        # Play each shaded area separately for square3
        self.play(FadeIn(shaded_area3_1))
        self.play(FadeIn(shaded_area3_2))
        self.play(FadeIn(shaded_area3_3))
        
        # Create the text "3/12" and position it below square3
        text3 = Tex(r"$\frac{3}{12}$")
        text3.shift(DOWN * 2 + RIGHT * 2)  # Adjusted position

        # Add text3 to the scene
        self.play(Write(text3))

    def Equall3(self):
        equals_signs = Tex("=").scale(1.5).shift(UP*0.1+RIGHT*3.5)
        self.play(Write(equals_signs))

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
        self.play(Create(vertical_lines4), Create(horizontal_lines4))
        
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

if __name__ == "__main__":
    scene = EquiFractions2()
    scene.render()
