from manim import *

class GraphLinearEquation(Scene):
    def construct(self):
        # Set up the axes with labels
        axes = Axes(
            x_range=[-10, 10, 1],  # X-axis range from -10 to 10 with a step of 1
            y_range=[-10, 10, 1],  # Y-axis range from -10 to 10 with a step of 1
            axis_config={"include_numbers": True},  # Include numbers on the axes
        )
        
        # Labels for the axes
        x_label = axes.get_x_axis_label(Tex("x"))
        y_label = axes.get_y_axis_label(Tex("y"))

        # The linear function y = 2x + 1
        linear_function = axes.plot(lambda x: 2 * x + 1, color=BLUE)
        
        # Label for the function
        function_label = axes.get_graph_label(
            linear_function, 
            label=Tex("y = 2x + 1"), 
            x_val=3, 
            direction=UP
        )

        # Add all the elements to the scene
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(linear_function), Write(function_label))
        self.wait(2)

if __name__ == "__main__":
    scene = GraphLinearEquation()
    scene.render()
