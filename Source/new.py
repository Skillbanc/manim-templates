from manim import *

class ClockHands(Scene):

    def ClockHands(self):

        
        title = Text("Graph of linear equation in two variables").scale(0.75)
        
        # Display title
        self.play(Write(title))
        self.wait(2)  # Pause to display the title

        # Fade out the title
        self.play(FadeOut(title))

        # Create axes with numbered ticks
        axes = Axes(
            x_range=[-10, 10, 1],
            y_range=[-9, 9, 1],
            axis_config={"color": BLUE, "include_numbers": True},
            tips=False,
            
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        # Define the linear equation
        def linear_function(x):
            return 4 * x - 9

        # Create the graph of the linear equation
        graph = axes.plot(linear_function, color=RED)
        graph_label = axes.get_graph_label(graph, label='y=4x-9', x_val=4, direction=RIGHT)

        # # Create dot for intercept
        # intercept_dot = Dot(axes.coords_to_point(0, 1), color=YELLOW)
        # intercept_label = MathTex("(0, 1)").next_to(intercept_dot,RIGHT)

        # Add the axes, graph, and labels to the scene
        # self.play(Create(axes), Write(labels))
        # self.play(Create(graph), Write(graph_label))
        # self.play(Create(intercept_dot), Write(intercept_label))

         # Intercepts
        intercepts = [(0, 9), (1,5)]

        # Create dots and labels for intercepts
        intercept_dots = []
        intercept_dot_labels = []
        for intercept in intercepts:
            dot = Dot(axes.coords_to_point(intercept[0], intercept[1]), color=YELLOW)
            label = MathTex(f"({intercept[0]}, {intercept[1]})").next_to(dot, RIGHT)
            intercept_dots.append(dot)
            intercept_dot_labels.append(label)

        # Add the axes, graph, intercepts, and labels to the scene
        self.play(Create(axes), Write(labels))
        self.play(Create(graph), Write(graph_label))
        self.play(*[Create(dot) for dot in intercept_dots])
        self.play(*[Write(label) for label in intercept_dot_labels])


        # Pause to display
        self.wait(2)

if __name__ == "__main__":
    scene = ClockHands()
    scene.render()
