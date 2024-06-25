from manim import *

class Addition(Scene):
    def construct(self):
        self.AdditionOfFractions()
        self.AddSymbol()
        self.AddOfFractionExp2()
        self.EquallSym()
        self.AddOfFractionExp3()

    def AdditionOfFractions(self):
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
        self.play(Create(square1), Create(vertical_line1), Create(horizontal_line1), Create(shaded_area1))
        
        # Create the text "1/4" and position it below square1
        text1 = Tex(r"$\frac{1}{4}$")
        text1.shift(DOWN * 2 + LEFT * 1)
        # Add text1 to the scene
        self.play(Write(text1))

    def EquallSym(self):
        equals_signs = Tex("=").scale(1.5).shift(UP*0.1+RIGHT*1)
        self.play(Write(equals_signs))
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
        self.play(Create(square1), Create(vertical_line1), Create(horizontal_line1), Create(shaded_area1_1),Create(shaded_area1_2))
        
        # Create the text "1/4" and position it below square1
        text1 = Tex(r"$\frac{1}{2}$")
        text1.shift(DOWN * 2 + RIGHT * 3)
        
        # Add text1 to the scene
        self.play(Write(text1))
    
if __name__ == "__main__":
    scene = Addition()
    scene.render()