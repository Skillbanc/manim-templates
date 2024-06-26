from manim import *

class GraphLinearEquation(Scene):
    
    def construct(self):
        # Set up the axes
        axes = Axes(
            x_range=[-10, 10, 1], 
            y_range=[-10, 10, 1], 
            axis_config={"include_numbers": True}
        )

        # Labels for the axes
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")

        # The linear function y = 2x + 1
        linear_function = axes.get_graph_label(lambda x: 2 * x + 1, color=BLUE)
        function_label = axes.get_graph_label(linear_function, label="y = 2x + 1", x_val=3, direction=UP)

        # Add all the elements to the scene
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(linear_function), Write(function_label))
        self.wait(2)

if __name__ == "__main__":
    scene = GraphLinearEquation()
    scene.render()