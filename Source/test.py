from AbstractAnim import AbstractAnim
import cvo
from manim import *

class MoveImageeee(AbstractAnim):
    def construct(self):
        # Title
        title = Text("Cone", color=RED, weight=BOLD)
        title.move_to([0, 3, 0])
        underline = Underline(title)
        self.play(Write(title))
        self.play(Create(underline))
        self.wait()

        # Create the cone
        # self.play(Write(NumberPlane()))
        cone = Polygon(
            [0, 2, 0],  # Top point of the cone
            [-2, -1, 0],  # Bottom left point
            [2, -1, 0],  # Bottom right point
            color=WHITE,
            
        )
        cone.shift([-4, 0, 0])  # Shifted towards the left
        self.play(Create(cone))

        # Create the horizontal ellipse (base)
        base = Ellipse(width=4, height=0.4, color=WHITE)
        base.move_to(cone.get_center() + DOWN * 1.5)  # Positioned below the cone
        self.play(Create(base))

        # Create the vertical line representing the height
        height_line = Line(start=[-4, 2, 0], end=[-4, -1, 0], color=WHITE)  # Shifted towards the left
        self.play(Create(height_line))

        
        # Create the small filled circle at the center of the base
        center_dot = Dot(point=[-4, -1, 0], color=WHITE)  # Shifted towards the left
        self.play(Create(center_dot))

        # Create the labels "h", "l", and "r"
        height_label = Text("h", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        height_label.move_to([-4.2, 0.5, 0])  # Adjusted position
        self.play(Write(height_label))

        slant_label = Text("l", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        slant_label.move_to([-3, 1, 0])  # Shifted towards the left
        self.play(Write(slant_label))

        radius_label = Text("r", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        radius_label.move_to([-3, -1.7, 0])  # Shifted towards the left
        self.play(Write(radius_label))

        # Slant height formula
        slantheight = MathTex ("\\textbf{Slant height } = h^2 + r^2 \\\\ =\\sqrt{h^2 + r^2}", color=WHITE).next_to(cone,RIGHT*2)
        self.play(Write(slantheight))

        cone1 = Polygon(
            [-4, 2, 0],  # Top point of the cone
            [-2, -1, 0],  # Bottom left point
            [-4, -1, 0],  # Bottom right point
            color=WHITE,
            
        )
        
        self.play(Create(cone1))
        cone1.set_fill("#a3a3c2", opacity=0.5)
        base1 = Ellipse(width=4, height=0.4, color=WHITE,fill_opacity=1, fill_color=BLACK)
        base1.move_to(cone.get_center() + DOWN * 1.5)  # Positioned below the cone
        self.play(Create(base1))

        # Create the vertical line representing the height
        height_line1 = Line(start=[-4, 2, 0], end=[-4, -1, 0], color=WHITE)  # Shifted towards the left
        self.play(Create(height_line1))

        # Create the small filled circle at the center of the base
        center_dot1 = Dot(point=[-4, -1, 0], color=WHITE)  # Shifted towards the left
        self.play(Create(center_dot1))
        self.wait()
        L1=Line(start=[-6,-1,0],end=[-2,-1,0])
        self.play(Write(L1))
        self.wait()
        
        slant_height_formula = MathTex("\\textbf{Slant height (l)} = \\sqrt{h^2 + r^2}", color="#a3a3c2")
        slant_height_formula.next_to(slantheight, DOWN,buff=1)
        self.play(Write(slant_height_formula))
        self.play(Uncreate(cone1))
        self.play(FadeOut(slantheight), FadeOut(slant_height_formula))

        # Highlight LSA
        lsaformula = MathTex("\\textbf{LSA} = \\text{Sum of the areas of triangles}\\\\ =\\frac{1}{2}l\\text{(circumference of base of cone)}\\\\ =\\frac{1}{2}l(2\\pi r) \\\\ = \\pi r l", color=WHITE).next_to(cone,RIGHT*2)
        self.play(Create(lsaformula))
        cone.set_fill("#ffb3b3", opacity=0.5)
        
        base1 = Ellipse(width=4, height=0.4, color=WHITE,fill_opacity=1, fill_color=BLACK)
        base1.move_to(cone.get_center() + DOWN * 1.5)  # Positioned below the cone
        self.play(Create(base1))

        # Create the vertical line representing the height
        height_line1 = Line(start=[-4, 2, 0], end=[-4, -1, 0], color=WHITE)  # Shifted towards the left
        self.play(Create(height_line1))

        # Create the small filled circle at the center of the base
        center_dot1 = Dot(point=[-4, -1, 0], color=WHITE)  # Shifted towards the left
        self.play(Create(center_dot1))
        self.wait()
        L1=Line(start=[-6,-1,0],end=[-2,-1,0])
        self.play(Write(L1))
        self.wait()

        lsa_formula = MathTex("\\textbf{LSA} = \\pi r l", color="#ffb3b3")
        lsa_formula.next_to(lsaformula, DOWN)
        self.play(Write(lsa_formula))
        self.play(FadeOut(lsaformula), FadeOut(lsa_formula))

        # Highlight TSA
        tsaformula  = MathTex("\\textbf{TSA} =\\text{LSA + area of its base} \\\\ = \\pi r l + \\pi r^2\\\\= \\pi r (l + r)", color=WHITE).next_to(cone,RIGHT*2)
        self.play(Write(tsaformula))
        cone.set_fill("#80ff80", opacity=1)
        self.wait(1)
        base1.set_fill("#80ff80", opacity=1)
        self.wait(1)
        tsa_formula = MathTex("\\textbf{TSA} = \\pi r (l + r)", color="#80ff80")
        tsa_formula.next_to(tsaformula, DOWN)
        self.play(Write(tsa_formula))
        self.wait(1)
        self.play(FadeOut(tsaformula), FadeOut(tsa_formula))
        
        # Highlight Volume
        volumeformula = MathTex("\\textbf{Volume} = \\frac{1}{3}\\text{volume of cylinder} \\\\ =\\frac{1}{3} \\pi r^2 h", color=WHITE).next_to(cone,RIGHT*2)
        self.play(Write(volumeformula)) 
        cone.set_fill("#99ffff", opacity=1)
        base1.set_fill("#99ffff", opacity=1)
        self.wait(1)                      
        volume_formula = MathTex("\\textbf{Volume} = \\frac{1}{3} \\pi r^2 h", color="#99ffff")
        volume_formula.next_to(volumeformula, DOWN)
        self.play(Write(volume_formula))
        cone.set_fill("#99ffff", opacity=1)
        base1.set_fill("#99ffff", opacity=1)
        self.wait(1)
        

        
        
        
        

# To render the scene
if __name__ == "__main__":
    
    scene = MoveImageeee()
    scene.render()
