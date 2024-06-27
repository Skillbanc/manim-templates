from AbstractAnim import AbstractAnim
import cvo
from manim import *

class MoveImageeee(AbstractAnim):
    def construct(self):
        # Title
        title = Text("Right Pyramid", color=RED, weight=BOLD)
        title.move_to(UP * 3)  # Center the title at the top
        underline = Underline(title)
        
        # Define the reduced base of the pyramid (square)
        base_points = [(-1, -1, 0), (1, -1, 0), (0.5, -2, 0), (-1.5, -2, 0)]
        base = Polygon(*base_points, stroke_width=5, color=WHITE)

        # Apex of the pyramid
        apex = [0, 1, 0]

        # Faces of the pyramid
        face1 = Polygon(apex, base_points[0], base_points[1], stroke_width=5, color=WHITE)
        face2 = Polygon(apex, base_points[1], base_points[2], stroke_width=5, color=WHITE)
        face3 = Polygon(apex, base_points[2], base_points[3], stroke_width=5, color=WHITE)
        face4 = Polygon(apex, base_points[3], base_points[0], stroke_width=5, color=WHITE)

        # Dotted line for the height
        height_line = DashedLine(start=apex, end=[0, -1.5, 0], color=RED)

        # Dot at the end of the height line
        center_dot = Dot(point=[0, -1.5, 0], color=WHITE)

        # Normal line for slant height
        slant_height_line = Line(start=apex, end=base_points[1], color=RED)

        # Labels
        height_label = Text("height", color=WHITE).scale(0.5)
        slant_height_label = Text("slant height", color=WHITE).scale(0.5)

        # Adjust labels' positions
        height_label.next_to(height_line, LEFT)
        slant_height_label.next_to(slant_height_line, RIGHT)

        # Group all objects to move them together
        group = VGroup(base, face1, face2, face3, face4, height_line, center_dot, height_label, slant_height_line, slant_height_label)
        
        # Shift the group further to the left and a little down
        group.move_to(LEFT * 4 + DOWN * 1) 

        # Animation to display the title and underline
        self.play(Write(title))
        self.play(Write(underline))

        # Animation to display the pyramid
        self.play(Write(group))

        # Formulas
        lsa_formula = MathTex(r"\textbf{LSA} = \frac{1}{2} \times \text{Perimeter of base} \times \text{Slant height}", color="#ffb3b3").move_to(RIGHT * 2 + UP*0.2)
        # lsa_formula.next_to(title, DOWN)
        tsa_formula = MathTex(r"\textbf{TSA} = \text{LSA} + \text{Area of base}", color="#80FF80").move_to(RIGHT * 2)
        volume_formula = MathTex(r"\textbf{Volume} = \frac{1}{3} \times \text{Area of base} \times \text{Height}", color="#99FFFF").move_to(RIGHT * 2 + DOWN * 1)

        # Highlight LSA Formula
        lsa_highlight = MathTex(r"\textbf{LSA} = \frac{1}{2} \times \text{Perimeter of base} \times \text{Slant height}", color="#ffb3b3")
        lsa_highlight.next_to(volume_formula, UP * 3)
        self.play(Write(lsa_highlight))
        face1.set_fill("#ffb3b3", opacity=0.5)
        self.wait(1)
        face2.set_fill("#ffb3b3", opacity=0.5)
        self.wait(1)
        face3.set_fill("#ffb3b3", opacity=0.5)
        self.wait(1)
        face4.set_fill("#ffb3b3", opacity=0.5)
        self.wait(1)
        
        # Highlight TSA Formula
        tsa_highlight = MathTex(r"\textbf{TSA} = \text{LSA} + \text{Area of base}", color="#80FF80")
        tsa_highlight.next_to(lsa_highlight, DOWN)
        self.play(Write(tsa_highlight))
        face1.set_fill("#80FF80", opacity=0.5)
        self.wait(1)
        face2.set_fill("#80FF80", opacity=0.5)
        self.wait(1)
        face3.set_fill("#80FF80", opacity=0.5)
        self.wait(1)
        face4.set_fill("#80FF80", opacity=0.5)
        self.wait(1)
        base.set_fill("#80FF80", opacity=0.5)
        self.wait(1)
        
        # Highlight Volume Formula
        volume_highlight = MathTex(r"\textbf{Volume} = \frac{1}{3} \times \text{Area of base} \times \text{Height}", color="#99FFFF")
        volume_highlight.next_to(tsa_highlight, DOWN)
        self.play(Write(volume_highlight))
        face1.set_fill("#99FFFF", opacity=0.5)
        face2.set_fill("#99FFFF", opacity=0.5)
        face3.set_fill("#99FFFF", opacity=0.5)
        face4.set_fill("#99FFFF", opacity=0.5)
        base.set_fill("#99FFFF", opacity=0.5)
        self.wait(3)  

# To render the scene
if __name__ == "__main__":
    
    scene = MoveImageeee()
    scene.render()
