from manim import *
from AbstractAnim import AbstractAnim
import cvo
class DirectProportionGraph(Scene):
    def construct(self):
        
        axes = Axes(
            x_range=[0, 10, 1],  
            y_range=[0, 10, 1], 
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": np.arange(0, 11, 1)},
            y_axis_config={"numbers_to_include": np.arange(0, 11, 1)},
        )
        
        
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
       
        def direct_proportion(x):
            return 0.5 * x  # k = 0.5
        
       
        graph = axes.plot(direct_proportion, color=RED)
        
       
        dot = Dot(axes.c2p(0, 0), color=YELLOW)
        
        
        tracing_line = always_redraw(lambda: Line(axes.c2p(0, 0), dot.get_center(), color=YELLOW))
        
       
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(graph), run_time=2)
        
        
        self.play(MoveAlongPath(dot, graph), run_time=4, rate_func=linear)
        

        self.add(tracing_line)
        

        self.wait(2)

if __name__ == "__main__":
    from manim import *
    scene = DirectProportionGraph()
    scene.render()

