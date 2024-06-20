from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo
import numpy as np

class test98(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        # Title of the animation
        title = Text("How to Draw a Symmetric Figure").to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))  # Fade out the title after displaying

        # Step 1: Draw the first line of symmetry
        line_m = Line(UP*2, DOWN*2).shift(LEFT)
        step1_text = Text("(i) Draw the first line of symmetry (m).").to_edge(UP).scale(0.5)
        self.play(Write(step1_text))
        self.play(Create(line_m))
        self.wait(1)
        self.play(FadeOut(step1_text))

        # Step 2: Draw the initial curve
        start_anchor = LEFT*2
        start_handle = LEFT*2 + UP
        end_handle = LEFT + UP*2
        end_anchor = ORIGIN
        curve = CubicBezier(start_anchor=start_anchor, start_handle=start_handle, end_handle=end_handle, end_anchor=end_anchor)
        step2_text = Text("(ii) Draw an initial curve.").to_edge(UP).scale(0.5)
        self.play(Write(step2_text))
        self.play(Create(curve))
        self.wait(1)
        self.play(FadeOut(step2_text))

        # Step 3: Draw the second line of symmetry
        line_A = Line(LEFT*3, RIGHT*3)
        step3_text = Text("(iii) Draw the second line of symmetry (A).").to_edge(UP).scale(0.5)
        self.play(Write(step3_text))
        self.play(Create(line_A))
        self.wait(1)
        self.play(FadeOut(step3_text))

        # Step 4: Draw the mirror image of the curve
        mirror_curve = curve.copy()
        mirror_curve.flip(axis=line_m.get_vector())
        step4_text = Text("(iv) Draw a mirror image of the curve across line m.").to_edge(UP).scale(0.5)
        self.play(Write(step4_text))
        self.play(Transform(curve, mirror_curve))
        self.wait(1)
        self.play(FadeOut(step4_text))

        # Final step: Show the complete symmetric figure
        final_step_text = Text("Complete symmetric figure with lines A and m.").to_edge(UP).scale(0.5)
        self.play(Write(final_step_text))
        self.play(Create(line_m), Create(line_A), Create(curve), Create(mirror_curve))
        self.wait(2)

         # Clear the screen
        self.play(FadeOut(line_m), FadeOut(line_A), FadeOut(curve), FadeOut(mirror_curve), FadeOut(final_step_text))

# To run the scene, use:
# manim -pql draw_symmetric_figure.py DrawSymmetricFigure

if __name__ == "__main__":
    scene = test98()
    scene.render()
