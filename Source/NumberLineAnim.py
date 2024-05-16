
from manim import *

class NumberLineAnim(Scene):
    def construct(self):
        self.RenderNaturalNumbers()
    
    def RenderNaturalNumbers(self):
        number_line = NumberLine()
        pointer = Vector(DOWN)
        label = MathTex("x").add_updater(lambda m: m.next_to(pointer, UP))

        tracker = ValueTracker(1)
        pointer.add_updater(
            lambda m: m.next_to(
                        number_line.n2p(tracker.get_value()),
                        UP
                    )
        )
        self.add(number_line, pointer,label)
        for i in range(1,10):
            self.play(tracker.animate.set_value(i))

if __name__ == "__main__":
    scene = NumberLineAnim()
    scene.render()