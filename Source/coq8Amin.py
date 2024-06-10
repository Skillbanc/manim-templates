from manim import *

class coq7Anim(Scene):
    def construct(self):
        # Title of the animation
        title = Text("Quadrilateral Construction").to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Step 1: Draw the first side with a ruler
        step1_text = Text("Step 1: Draw the first side with a ruler").next_to(title, DOWN)
        self.play(Write(step1_text))
        side1 = Line(LEFT, RIGHT)
        self.play(Create(side1))
        self.wait(1)
        self.play(FadeOut(side1), FadeOut(step1_text))

        # Step 2: Draw the second side with a set square
        step2_text = Text("Step 2: Draw the second side with a set square").next_to(title, DOWN)
        self.play(Write(step2_text))
        side2 = Line(side1.get_end(), side1.get_end() + UP*2)
        self.play(Create(side2))
        self.wait(1)
        self.play(FadeOut(side2), FadeOut(step2_text))

        # Step 3: Draw the third side with a ruler
        step3_text = Text("Step 3: Draw the third side with a ruler").next_to(title, DOWN)
        self.play(Write(step3_text))
        side3 = Line(side2.get_end(), side2.get_end() + LEFT*3)
        self.play(Create(side3))
        self.wait(1)
        self.play(FadeOut(side3), FadeOut(step3_text))

        # Step 4: Draw the fourth side with a compass
        step4_text = Text("Step 4: Draw the fourth side with a compass").next_to(title, DOWN)
        self.play(Write(step4_text))
        side4 = Line(side3.get_end(), side1.get_start())
        self.play(Create(side4))
        self.wait(1)
        self.play(FadeOut(side4), FadeOut(step4_text))

        # Step 5: Show the completed quadrilateral
        step5_text = Text("Step 5: Show the completed quadrilateral").next_to(title, DOWN)
        self.play(Write(step5_text))
        quadrilateral = Polygon(side1.get_start(), side1.get_end(), side2.get_end(), side3.get_end())
        self.play(Create(quadrilateral))
        self.wait(2)
        self.play(FadeOut(quadrilateral), FadeOut(step5_text))

        # Fade out the title at the end
        self.play(FadeOut(title))

# To render the scene, use the following command in your terminal:
# manim -pql quadrilateral_construction.py Coq8Anim




if __name__ == "__main__":
    scene = coq7Anim()
    scene.render()