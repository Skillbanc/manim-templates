from manim import *
from AbstractAnim import AbstractAnim
import cvo

class InverseProportionGraph(Scene):
    def construct(self):
        
        axes = Axes(
            x_range=[0.1, 10, 1],  
            y_range=[0.1, 10, 1],  
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": np.arange(1, 11, 1)},
            y_axis_config={"numbers_to_include": np.arange(1, 11, 1)},
        )
        
      
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        
        def inverse_proportion(x):
            return 2 / x  # k = 2
        
       
        graph = axes.plot(inverse_proportion, color=RED)
        
       
        dot = Dot(axes.c2p(1, inverse_proportion(1)), color=YELLOW)
       
        tracing_line = always_redraw(lambda: Line(axes.c2p(1, 2), dot.get_center(), color=YELLOW))
        
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(graph), run_time=2)
        
        
        self.play(MoveAlongPath(dot, graph), run_time=4, rate_func=linear)
        
       
        self.add(tracing_line)
        
        
        self.wait(2)

if __name__ == "__main__":
    from manim import *
    scene = InverseProportionGraph()
    scene.render()
