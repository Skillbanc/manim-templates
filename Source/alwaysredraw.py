from manim import *

class AlwaysRedraw(Scene):
    def construct(self):
        cir = Circle(radius=3,color=GOLD)

        text = always_redraw(lambda: MathTex("Circle").move_to(cir.get_center()))

        self.add(cir, text)

        self.play(cir.animate.scale(0.5).to_edge(DL), run_time=3)
        self.wait()

        text.clear_updaters()

        self.play(cir.animate.to_edge(UR), run_time=3)

        self.wait()
if __name__=="__main__":
    vt=AlwaysRedraw()
    vt.render()