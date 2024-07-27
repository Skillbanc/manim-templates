from manim import *
from AbstractAnim import AbstractAnim
import cvo


class Grade8Chapter10DirectAndInverseProportion(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.direct()
        self.fadeOutCurrentScene()
        self.DirectProportionProperties()
        self.fadeOutCurrentScene()
        self.DirectProportionProblem()
        self.fadeOutCurrentScene()
        self.direct_graph()
        self.fadeOutCurrentScene()
        self.inverse()
        self.fadeOutCurrentScene()
        self.InverseProportionProperties()
        self.fadeOutCurrentScene()
        self.InverseProportionProblem()
        self.fadeOutCurrentScene()
        self.inverse_graph()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
     

    def Introduction(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [-TAU/4]
        self.isRandom = False
        p10 = cvo.CVO().CreateCVO("PROPORTIONS", "")
        p11 = cvo.CVO().CreateCVO("TYPES", "")
        p11.extendOname(["DIRECT", "INVERSE"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10, p10)

    def direct(self):
        # Title and Definition
        title = Text("Direct Proportion").set_color(BLUE).to_edge(UP)
        definition = MathTex(
            r"\text{If } y \text{ is directly proportional to } x, \text{ then } y = kx, \text{ where } k \text{ is a constant.}"
        ).scale(0.8).to_edge(UP, buff=1.5)

        # Formula
        formula_title = Text("Formula").set_color(ORANGE).next_to(definition, DOWN, buff=0.5)
        formula = MathTex(r"y = kx").next_to(formula_title, DOWN, buff=0.3)

        # Example with numbers
        example_title = Text("Example").set_color(GREEN).next_to(formula, DOWN, buff=0.5)
        example_text = MathTex(
            r"\text{If } x = 2 \text{ and } y = 6 \text{, then } k = \frac{y}{x} = \frac{6}{2} = 3."
        ).next_to(example_title, DOWN, buff=0.3)

        # Group all elements for better placement
        definition_group = VGroup(title, definition)
        formula_group = VGroup(formula_title, formula)
        example_group = VGroup(example_title, example_text)

        # Arrange the groups vertically
        definition_group.to_edge(UP, buff=1.5)
        formula_group.next_to(definition_group, DOWN, buff=0.7)
        example_group.next_to(formula_group, DOWN, buff=0.7)

        # Display the elements
        self.play(Write(title))
        self.play(Write(definition))
        self.play(Write(formula_title), Write(formula))
        self.play(Write(example_title), Write(example_text))

        self.wait(5)

    def DirectProportionProperties(self):
         
        title = Text("Properties of Direct Proportion").set_color(BLUE).to_edge(UP, buff=1.5)
        
        properties = [
            r"\text{1. The ratio } \frac{y}{x} \text{ is constant.}",
            r"\text{2. A graph of } y \text{ against } x \text{ is a straight line through the origin.}",
            r"\text{3. If } x_1 \text{ and } y_1 \text{ are proportional to } x_2 \text{ and } y_2 \text{ respectively, then } \frac{y_1}{x_1} = \frac{y_2}{x_2}.",
            r"\text{4. If } x \text{ increases, } y \text{ increases proportionally and vice versa.}"
        ]

        # Create the title
        self.play(Write(title))

        # Display the properties
        for i, prop in enumerate(properties):
            prop_text = MathTex(prop, font_size=36).next_to(title, DOWN, buff=0.5).shift(DOWN * i * 1.2)
            self.play(Write(prop_text))

        # Pause before ending
        self.wait(5)

    def DirectProportionProblem(self):
         # Title and Problem Statement
        title = Text("Problem on Direct Proportion").set_color(BLUE).to_edge(UP, buff=0.5)
        problem_text = MathTex(
            r"\text{If } y \text{ is directly proportional to } x, \text{ and } y = 10 \text{ when } x = 5, \text{ find } y \text{ when } x = 8."
        ).scale(0.8).next_to(title, DOWN, buff=0.5)

        # Display the problem
        self.play(Write(title))
        self.play(Write(problem_text))

        # Define the constant of proportionality
        k_text = MathTex(
            r"\text{Given } y = kx, \text{ with } y = 10 \text{ when } x = 5."
        ).next_to(problem_text, DOWN, buff=0.5)
        k_calculation = MathTex(
            r"k = \frac{y}{x} = \frac{10}{5} = 2."
        ).next_to(k_text, DOWN, buff=0.5)

        # Display constant of proportionality calculation
        self.play(Write(k_text))
        self.play(Write(k_calculation))

        # Solve for new value
        new_value_text = MathTex(
            r"\text{Find } y \text{ when } x = 8."
        ).next_to(k_calculation, DOWN, buff=0.5)
        solution_text = MathTex(
            r"y = kx = 2 \times 8 = 16."
        ).next_to(new_value_text, DOWN, buff=0.5)

        # Display the solution
        self.play(Write(new_value_text))
        self.play(Write(solution_text))

        # Additional row showing y = 16
        final_result_text = MathTex(
            r"\text{Thus, } y = 16."
        ).next_to(solution_text, DOWN, buff=0.5)

        # Display the final result
        self.play(Write(final_result_text))

        # Pause to view the result
        self.wait(5)


    def direct_graph(self):
        text = Text("Graph for Direct Proportion")
        text.scale(1)
        text.to_edge(UP)
        self.play(Write(text))
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

    def inverse(self):
         # Title and Definition
        title = Text("Inverse Proportion").set_color(BLUE).to_edge(UP, buff=1)
        definition = MathTex(
            r"\text{If } y \text{ is inversely proportional to } x, \text{ then } y = \frac{k}{x}, \text{ where } k \text{ is a constant.}"
        ).scale(0.8).next_to(title, DOWN, buff=0.5)

        # Formula
        formula_title = Text("Formula").set_color(ORANGE).next_to(definition, DOWN, buff=0.5)
        formula = MathTex(r"y = \frac{k}{x}").next_to(formula_title, DOWN, buff=0.3)

        # Example with numbers
        example_title = Text("Example").set_color(GREEN).next_to(formula, DOWN, buff=0.5)
        example_text = MathTex(
            r"\text{If } x = 4 \text{ and } y = 3 \text{, then } k = xy = 4 \times 3 = 12."
        ).next_to(example_title, DOWN, buff=0.3)

        # Group all elements for better placement
        definition_group = VGroup(title, definition)
        formula_group = VGroup(formula_title, formula)
        example_group = VGroup(example_title, example_text)

        # Arrange the groups vertically with title slightly upward
        definition_group.to_edge(UP, buff=0.7)
        formula_group.next_to(definition_group, DOWN, buff=0.7)
        example_group.next_to(formula_group, DOWN, buff=0.7)

        # Display the elements
        self.play(Write(title))
        self.play(Write(definition))
        self.play(Write(formula_title), Write(formula))
        self.play(Write(example_title), Write(example_text))

        self.wait(5) 


    def InverseProportionProperties(self):
        title = Text("Properties of Inverse Proportion").set_color(BLUE).to_edge(UP, buff=1.5)
        
        properties = [
            r"\text{1. The product } xy \text{ is constant.}",
            r"\text{2. A graph of } y \text{ against } x \text{ is a hyperbola.}",
            r"\text{3. If } x_1 \text{ and } y_1 \text{ are inversely proportional to } x_2 \text{ and } y_2 \text{ respectively, then } x_1 y_1 = x_2 y_2.",
            r"\text{4. If } x \text{ increases, } y \text{ decreases proportionally and vice versa.}"
        ]

        # Create the title
        self.play(Write(title))

        # Display the properties
        for i, prop in enumerate(properties):
            prop_text = MathTex(prop, font_size=36).next_to(title, DOWN, buff=0.5).shift(DOWN * i * 1.2)
            self.play(Write(prop_text))

        # Pause before ending
        self.wait(5)

    def InverseProportionProblem(self):
         # Title and Problem Statement
        title = Text("Problem on Inverse Proportion").set_color(BLUE).to_edge(UP, buff=0.35)
        problem_text = MathTex(
            r"\text{If } y \text{ is inversely proportional to } x, \text{ and } y = 12 \text{ when } x = 4, \text{ find } y \text{ when } x = 6."
        ).scale(0.8).next_to(title, DOWN, buff=0.35)

        # Display the problem
        self.play(Write(title))
        self.play(Write(problem_text))

        # Define the constant of proportionality
        k_text = MathTex(
            r"\text{Given } y = \frac{k}{x}, \text{ with } y = 12 \text{ when } x = 4."
        ).next_to(problem_text, DOWN, buff=0.35)
        k_calculation = MathTex(
            r"k = y \cdot x = 12 \times 4 = 48."
        ).next_to(k_text, DOWN, buff=0.35)

        # Display constant of proportionality calculation
        self.play(Write(k_text))
        self.play(Write(k_calculation))

        # Solve for new value
        new_value_text = MathTex(
            r"\text{Find } y \text{ when } x = 6."
        ).next_to(k_calculation, DOWN, buff=0.35)
        solution_text = MathTex(
            r"y = \frac{k}{x} = \frac{48}{6} = 8."
        ).next_to(new_value_text, DOWN, buff=0.35)

        # Display the solution
        self.play(Write(new_value_text))
        self.play(Write(solution_text))

        # Additional row showing y = 8
        final_result_text = MathTex(
            r"\text{Thus, } y = 8."
        ).next_to(solution_text, DOWN, buff=0.35)

        # Display the final result
        self.play(Write(final_result_text))

        # Pause to view the result
        self.wait(5)

    def inverse_graph(self):
        text = Text("Graph for Inverse Proportion")
        text.scale(1)
        text.to_edge(UP)
        self.play(Write(text))
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
        
    def SetDeveloperList(self): 
       self.DeveloperList="Snehith" 
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="DirectAndInverseProportion.py"

   

if __name__ == "__main__":
    scene = Grade8Chapter10DirectAndInverseProportion()
    scene.render()