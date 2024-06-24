from manim import *
from AbstractAnim import AbstractAnim
import cvo

class LinearEq2var(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.Terms()
        self.fadeOutCurrentScene()
        self.Variable()
        self.fadeOutCurrentScene()
        self.Homogenity()
        self.fadeOutCurrentScene()
        self.Example()
        self.fadeOutCurrentScene()
        self.Example1()
        self.fadeOutCurrentScene()
        self.graph1()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()








    def Introduction(self):
        self.setNumberOfCirclePositions(3)
        self.angleChoice = [TAU/4,TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Linear Equation In two Variables","")
        p11=cvo.CVO().CreateCVO("Notation","ax+by=c")
        p12=cvo.CVO().CreateCVO("Example", "5x+4y=9")
        p10.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)



    def Terms(self):
        self.setNumberOfCirclePositions(3)
        self.angleChoice = [TAU/4,TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("ax+by=c","")
        p11=cvo.CVO().CreateCVO("Variable terms","")
        p12=cvo.CVO().CreateCVO("Constant terms", "c")
        p11.extendOname([" ax","by"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)


    def Variable(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Variable term ","")
        p11=cvo.CVO().CreateCVO("Properties", "")
        p11.extendOname(["a,b!=0"," degree of x\&y=1"])
        p11.SetIsMathText(True)
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)



    def Homogenity(self):
        self.setNumberOfCirclePositions(3)
        self.angleChoice = [TAU/4,TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Homogenity","")
        p11=cvo.CVO().CreateCVO("Homogenous", "c=0")
        p12=cvo.CVO().CreateCVO(" Non-Homogenous", "c!=0")
        
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)



    def Example(self):
       
           # Title
        title = Text("Solution of Linear Equation in Two Variables", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Consider the equation
        text1 = Text("Consider the equation 3x - 2y = 5.", font_size=24,color=YELLOW)
        text1.next_to(title, DOWN, buff=0.5)
        self.play(Write(text1))
        self.wait(1)

        # Can x = 3 be a solution?
        text2 = Text("Given x = 3 is a solution of this equation", font_size=24,color=YELLOW)
        text2.next_to(text1, DOWN, buff=0.5)
        self.play(Write(text2))
        self.wait(1)

        # Substitute x = 3
        text3 = Text("substitute x = 3 in the equation:", font_size=24)
        text3.next_to(text2, DOWN, buff=1)
        equation1 = MathTex("3(3) - 2y = 5", font_size=36)
        equation1.next_to(text3, DOWN, buff=0.5)
        equation2 = MathTex("9 - 2y = 5", font_size=36)
        equation2.next_to(equation1, DOWN, buff=0.5)
        self.play(Write(text3))
        self.play(Write(equation1))
        self.play(Write(equation2))
        self.wait(2)

        # Fade out everything except title and text1
        self.play( FadeOut(text3), FadeOut(equation1), FadeOut(equation2))
        self.wait(1)

        equation5 = MathTex("9 - 2y = 5", font_size=36)
        equation5.next_to(text2, DOWN, buff=0.5)

        # Find y from the equation
        text6 = Text("We can get the value of y from the equation", font_size=24)
        text6.next_to(equation5, DOWN, buff=0.5)
        equation3 = MathTex("2y = 4", font_size=36)
        equation3.next_to(text6, DOWN, buff=0.5)
        equation4 = MathTex("y = 2", font_size=36)
        equation4.next_to(equation3, DOWN, buff=0.5)
        #self.play(Write(equation5),Write(text6), Write(equation3), Write(equation4))
        self.play(Write(equation5))
        self.play(Write(text6))
        self.play(Write(equation3))
        self.play(Write(equation4))
        self.wait(2)

        # Conclusion
        text7 = Text("The values of x and y which satisfy the equation 3x - 2y = 5, are (3,2).", font_size=24)
        text7.next_to(equation4, DOWN, buff=0.5)
        # text8 = Text("This solution is written as an ordered pair (3, 2).", font_size=24)
        # text8.next_to(text7, DOWN, buff=0.5)
        self.play(Write(text7))
        self.wait(2)

        # Fade out
        #self.play(FadeOut(text6), FadeOut(equation3), FadeOut(equation4), FadeOut(text7), FadeOut(equation2))
        self.play(FadeOut(title), FadeOut(text2), FadeOut(text1), FadeOut(equation5), FadeOut(text6), FadeOut(equation3), FadeOut(equation4), FadeOut(text7))
        self.wait(1)
        
    

    def Example1(self):
        # Title
        title = Text("Find the Solutions of linear equation 4x + y = 9", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Equation
        equation = MathTex("Equation : 4x + y = 9", font_size=36,color=YELLOW)
        equation.next_to(title,DOWN, buff=1)
        self.play(Write(equation))
        self.wait(1)

        # Solution 1: x = 0
        solution1_text = Text(" substituting  x=0:", font_size=24)
        solution1_text.next_to(equation, DOWN, buff=0.5)
        self.play(Write(solution1_text))
        self.wait(1)

        equation1 = MathTex("4(0) + y = 9", font_size=36)
        equation1.next_to(solution1_text, DOWN, buff=0.5)
        equation2 = MathTex("y = 9", font_size=36)
        equation2.next_to(equation1, DOWN, buff=0.5)
        self.play(Write(equation1))
        self.wait(1)
        self.play(Write(equation2))
        self.wait(1)

        solution1 = MathTex("(0, 9)", font_size=36, color=YELLOW).next_to(equation2, DOWN, buff=0.5)
        self.play(Write(solution1))
        self.wait(2)

        conclusion1 = Text("(0,9) is one solution linear equation of 4x + y = 9 ", font_size=24)
        conclusion1.next_to(solution1, DOWN, buff=0.5)
        self.play(Write(conclusion1))
        self.wait(2)


        self.play(FadeOut(conclusion1),FadeOut(solution1), FadeOut(equation2), FadeOut(equation1), FadeOut(solution1_text))

        # Solution 2: x = 1
        solution2_text = Text("Now, substituting x=1:", font_size=24)
        solution2_text.next_to(equation, DOWN, buff=0.5)
        self.play(Write(solution2_text))
        self.wait(1)

        equation3 = MathTex("4(1) + y = 9", font_size=36)
        equation3.next_to(solution2_text, DOWN, buff=0.5)
        equation4 = MathTex("4 + y = 9", font_size=36)
        equation4.next_to(equation3, DOWN, buff=0.5)
        equation5 = MathTex("y = 5", font_size=36)
        equation5.next_to(equation4, DOWN, buff=0.5)
        self.play(Write(equation3))
        self.wait(1)
        self.play(Write(equation4))
        self.wait(1)
        self.play(Write(equation5))
        self.wait(1)

        solution2 = MathTex("(1, 5)", font_size=36, color=YELLOW).next_to(equation5, DOWN, buff=0.5)
        self.play(Write(solution2))
        self.wait(2)

        # Conclusion
        conclusion = Text("(0,9) and (1,5) satisfy the linear equation of 4x + y = 9 ", font_size=24)
        conclusion.next_to(solution2, DOWN, buff=0.5)
        self.play(Write(conclusion))
        self.wait(2)

        # Fade out
        self.play(FadeOut(title), FadeOut(equation), FadeOut(solution2_text), FadeOut(equation3),
                  FadeOut(equation4), FadeOut(equation5), FadeOut(solution2), FadeOut(conclusion))
        



    def graph1(self):
        # Create title text
        title = Text("Graph of linear equation in two variables").scale(0.75)
        
        # Display title
        self.play(Write(title))
        self.wait(2)  # Pause to display the title

        # Fade out the title
        self.play(FadeOut(title))

        # Create axes with numbered ticks
        axes = Axes(
            x_range=[-10, 10, 1],
            y_range=[-8, 8, 1],
            axis_config={"color": BLUE, "include_numbers": True},
            tips=False,
            
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        # Define the linear equation
        def linear_function(x):
            return 2 * x + 1

        # Create the graph of the linear equation
        graph = axes.plot(linear_function, color=RED)
        graph_label = axes.get_graph_label(graph, label='y=2x+1', x_val=2, direction=RIGHT)

        # # Create dot for intercept
        # intercept_dot = Dot(axes.coords_to_point(0, 1), color=YELLOW)
        # intercept_label = MathTex("(0, 1)").next_to(intercept_dot,RIGHT)

        # Add the axes, graph, and labels to the scene
        # self.play(Create(axes), Write(labels))
        # self.play(Create(graph), Write(graph_label))
        # self.play(Create(intercept_dot), Write(intercept_label))

         # Intercepts
        intercepts = [(0, 1), (-3,-5), (3,7)]

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

        # Clear the scene
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # Create title text for x-axis parallel line
        title_x = Text("Line Parallel to x-axis: y = 3").scale(0.75)
        
        # Display title
        self.play(Write(title_x))
        self.wait(2)  # Pause to display the title

        # Fade out the title
        self.play(FadeOut(title_x))

        # Create axes with numbered ticks
        axes = Axes(
            x_range=[-8, 8, 1],
            y_range=[-5, 5, 1],
            axis_config={"color": BLUE, "include_numbers": True},
            tips=False
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        # Define the line parallel to the x-axis
        x_parallel_line = axes.plot(lambda x: 3, color=RED)
        x_parallel_label = axes.get_graph_label(x_parallel_line, label='y=3', x_val=2, direction=UP)
        
        # intercept_dot = Dot(axes.coords_to_point(0, 3), color=YELLOW)
        # intercept_label = MathTex("(0, 3)").next_to(intercept_dot,UP)

        # Add the axes, graph, and labels to the scene
        self.play(Create(axes), Write(labels))
        self.play(Create(x_parallel_line), Write(x_parallel_label))
        # self.play(Create(intercept_dot), Write(intercept_label))

        # Pause to display
        self.wait(2)

        # Clear the scene
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # Title
        title = Text(" Line Parallel to Y-Axis: x = 3").scale(0.75)

        self.play(Write(title))
        self.wait(2)  # Pause to display the title

        # Fade out the title
        self.play(FadeOut(title))
        
        # Set up the axes
        axes = Axes(
            x_range=[-8, 8, 1],  # X-axis range from -10 to 10 with a step of 1
            y_range=[-5, 5, 1],  # Y-axis range from -10 to 10 with a step of 1
            axis_config={"color": BLUE, "include_numbers": True},
            tips=False # Include numbers on the axes
        ).add_coordinates()
        
        # Create a vertical line at x = 3
        x_value = 3
        vertical_line = Line(start=axes.c2p(x_value, -10), end=axes.c2p(x_value, 10), color=RED)
        
        # Add x=3 label
        label_x_3 = Tex(f"x = {x_value}").next_to(axes.coords_to_point(x_value, 0), UP+RIGHT)
        
        # Add labels
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        
        # Display the title
        
        
        # Display the axes, line, labels, and x=3 label
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(vertical_line), Write(label_x_3))
        self.wait(2)

    def SetDeveloperList(self):  
        self.DeveloperList="Agraz Gopu"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="LinearEq2var.py"


if __name__ == "__main__":
     scene = LinearEq2var()
     scene.render()

     
    