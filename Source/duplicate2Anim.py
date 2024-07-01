from manim import *
from AbstractAnim import AbstractAnim
import cvo

class CircleParts(Scene):
    def curve1(self):
        curve = Text("Curve",font_size=40).to_edge(UP*1)
        sub_title1 = Text("A curve in mathematics is a one-dimensional continuous set of points"'.',font_size=29).to_edge(UP*3.0)
        
        self.play(Write(curve))
        self.play(Write(sub_title1))
        self.wait(1)


        # Define the cosine wave function
        cosine_wave = FunctionGraph(
            lambda x: np.cos(x),
            x_range=[-PI, PI],
            color=BLUE
        )
        
        # Add the cosine wave to the scene
        self.play(Create(cosine_wave))
        self.wait(0)
        self.play(FadeOut(curve))
        self.play(FadeOut(sub_title1))
        self.play(FadeOut(cosine_wave))


        opencurve = Text("Open Curve",font_size=40).to_edge(UP*1)
        sub_title1 = Text("An open curve is a curve that does not form a closed loop"'.',font_size=29).to_edge(UP*3.0)
        
        self.play(Write(opencurve))
        self.play(Write(sub_title1))
        self.wait(1)


        # Define the sine wave function
        sine_wave = FunctionGraph(
            lambda x: np.sin(x),
            x_range=[-PI, PI],
            color=BLUE
        )
        # Add the sine wave to the scene
        self.play(Create(sine_wave))
        self.wait(0)
        self.play(FadeOut(opencurve))
        self.play(FadeOut(sub_title1))
        self.play(FadeOut(sine_wave))
        


        closedcurve = Text("Closed Curve",font_size=40).to_edge(UP*1)
        sub_title1 = Text("A closed curve in mathematics is a curve that forms a loop,",font_size=29).to_edge(UP*3.0)
        sub_title2 = Text("meaning its endpoints meet"'.',font_size=29).to_edge(UP*4.5)

        self.play(Write(closedcurve))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))

        ellipse = Ellipse(width=4.0, height=2.0, color=BLUE).to_edge(UP*8)
        self.play(Create(ellipse))
        self.wait(0)

if __name__ == "__main__":
    scene = CircleParts()
    scene.render()