from manim import *

class AdditionFrac2(Scene):
    def construct(self):
        self.AddCircel1()
        self.AdditionSymbol()
        self.AddCircel2()
        self.EquallSymbol()
        self.AddCircleFinal()
    def AddCircel1(self):
        # Define the radius of the circle
        radius = 1
        
        # Create a circle with the specified radius
        circle = Circle(radius=radius, color=WHITE, stroke_width=2)
        
        # Create a horizontal line from the center
        horizontal_line = Line(start=[-radius, 0, 0], end=[radius, 0, 0], color=WHITE)
        
        # Group all elements together
        group = VGroup(circle, horizontal_line)
        
        # Create a semicircle to shade (for example, the upper semicircle)
        shaded_area = Sector(
            outer_radius=radius,
            start_angle=180*DEGREES,
            angle=180 * DEGREES,
            fill_opacity=0.5,
            fill_color=BLUE
        )
        
        # Add shaded area to the group
        group.add(shaded_area)
        
        # Shift circle and horizontal line to their positions
        group.shift(LEFT*4)
        
        # Add everything to the scene
        self.play(Create(circle), Create(horizontal_line), Create(shaded_area))
        text1 = Tex(r"$\frac{1}{2}$")
        text1.shift(DOWN * 2 + LEFT * 4)
        
        # Add text1 to the scene
        self.play(Write(text1))
    def AdditionSymbol(self):
        equals_signs = Tex("+").scale(1.5).shift(UP*0.1+LEFT*2.5)
        self.play(Write(equals_signs))
    def AddCircel2(self):
        # Define the radius of the circle
        radius = 1
        
        # Create a circle with the specified radius
        circle = Circle(radius=radius, color=WHITE, stroke_width=2)
        
        # Create a horizontal line from the center
        horizontal_line = Line(start=[-radius, 0, 0], end=[radius, 0, 0], color=WHITE)
        
        # Group all elements together
        group = VGroup(circle, horizontal_line)
        
        # Create a semicircle to shade (for example, the upper semicircle)
        shaded_area = Sector(
            outer_radius=radius,
            start_angle=0,
            angle=180 * DEGREES,
            fill_opacity=0.5,
            fill_color=BLUE
        )
        
        # Add shaded area to the group
        group.add(shaded_area)
        
        # Shift circle and horizontal line to their positions
        group.shift(LEFT*1)
        
        # Add everything to the scene
        self.play(Create(circle), Create(horizontal_line), Create(shaded_area))
        text1 = Tex(r"$\frac{1}{2}$")
        text1.shift(DOWN * 2 + LEFT * 1)
        
        # Add text1 to the scene
        self.play(Write(text1))

    def EquallSymbol(self):
        equals_signs = Tex("=").scale(1.5).shift(UP*0.1+RIGHT*1)
        self.play(Write(equals_signs))

    def AddCircleFinal(self):
        radius = 1
        
        # Create a circle with the specified radius
        circle = Circle(radius=radius, fill_color=BLUE,fill_opacity=0.5, stroke_width=2).shift(RIGHT * 3)
        
        # Create the text "1/2" and position it relative to the circle
        text1 = Tex(r"$\frac{2}{2}$")
        text1.next_to( DOWN * 2 + RIGHT * 3)
        
        # Add the circle and text to the scene
        self.play(Create(circle), Write(text1))
if __name__ == "__main__":
    scene = AdditionFrac2()
    scene.render()