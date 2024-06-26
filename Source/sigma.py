from manim import *

class SummationSymbol(Scene):
    def construct(self):
        # Define the summation symbol with limits
        summation = MathTex(r"\sum_{i=1}^{n} i^2")
        
        # Position the summation symbol at the center
        summation.move_to(ORIGIN)

        # Create the animation
        self.play(Write(summation))
        self.wait(2)

if __name__ == "__main__":
    scene = SummationSymbol()
    scene.render()
# To render the scene, you can use the command:
# manim -pql summation_symbol.py SummationSymbol
