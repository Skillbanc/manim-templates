from manim import *
from AbstractAnim import AbstractAnim
import cvo

class LinearEq(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Pair()
        self.fadeOutCurrentScene()
        self.solution()
        self.fadeOutCurrentScene()
        self.Methods()
        self.fadeOutCurrentScene()
        self.create_title("Graphical Method of Finding Solution")
        self.fadeOutCurrentScene()
        axes, axes_labels = self.setup_axes()
        self.add(axes, axes_labels)
        self.fadeOutCurrentScene()
        
        # Example usage of plot_line
        self.display_intersecting_lines()
        # self.fadeOutCurrentScene()
        self.display_coincident_lines()
        # self.fadeOutCurrentScene()
        self.display_parallel_lines()
        # self.fadeOutCurrentScene()
        self.coeff()
        self.fadeOutCurrentScene()
        self.consistent1()
        self.fadeOutCurrentScene()
        self.inconsistent1()
        self.fadeOutCurrentScene()
        self.dependent1()
        self.fadeOutCurrentScene()
        self.relation()
        self.fadeOutCurrentScene()
        self.consistent()
        self.fadeOutCurrentScene()
        self.inconsistent()
        self.fadeOutCurrentScene()
        self.dependent()
        self.fadeOutCurrentScene()
        self.Algeb()
        self.fadeOutCurrentScene()
        self.Subs()
        self.example_substitution()
        self.Elim()
        self.solve_example()
        self.GithubSourceCodeReference()


    def Pair(self):
        self.positionChoice=[[-3,-2,0],[-3,2,0],[3,-2,0],[1,0,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Pair of Linear Equations in two variables","")
        p11=cvo.CVO().CreateCVO("Equation 1",r"$a_1x+b_1y+c_1=0$")
        p12=cvo.CVO().CreateCVO("Equation 2",r"$a_2x+b_2y+c_2=0$")
        p13=cvo.CVO().CreateCVO("Real Numbers","$a_1,a_2,b_1,b_2,c_1,c_2$")
        p10.cvolist.append(p11) 
        p10.cvolist.append(p12) 
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))

    def solution(self):
        self.setNumberOfCirclePositions(2)
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Solution","Pair of Linear Equations")
        p11=cvo.CVO().CreateCVO("Property","Pair of values that satisfy both equations")
        # p10=cvo.CVO().CreateCVO("Solution","Pair of Linear Equations")
        p10.setcircleradius(2)        
        p11.setcircleradius(2)        
        p10.cvolist.append(p11) 
        self.construct1(p10, p10)

    def Methods(self):
        self.positionChoice=[[0,2,0],[-4,2,0],[4,2,0],[4,-2,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Methods for Solutions","")
        p11=cvo.CVO().CreateCVO("Model Method","")
        p12=cvo.CVO().CreateCVO("Graphical Method","")
        p13=cvo.CVO().CreateCVO("Algebraic Method","")      
        p10.cvolist.append(p11) 
        p10.cvolist.append(p12) 
        p10.cvolist.append(p13) 
        self.construct1(p10, p10)
    
    def create_title(self, title_text):
        title = Text(title_text, font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        step1_label = Text("1: Intersecting Lines", font_size=24).shift(UP * 2)
        self.play(Write(step1_label))
        step2_label = Text("2: Coinciding Lines", font_size=24).next_to(step1_label, DOWN, buff=0.5)
        self.play(Write(step2_label))
        step3_label = Text("3: Parallel Lines", font_size=24).next_to(step2_label, DOWN, buff=0.5)
        self.play(Write(step3_label))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(step1_label), FadeOut(step2_label), FadeOut(step3_label))

    def setup_axes(self):
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"color": BLUE, "include_numbers": True},
            tips=False
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        return axes, axes_labels

    def plot_line(self, axes, equation, color):
        return axes.plot(equation, color=color)

    def display_intersecting_lines(self):
        axes, axes_labels = self.setup_axes()
        self.play(Create(axes), Write(axes_labels))

        eq1 = lambda x: 2 - x  # Example: x + y = 2
        eq2 = lambda x: 3 - 2 * x  # Example: 2x + y = 3

        graph1 = self.plot_line(axes, eq1, color=GREEN)
        graph2 = self.plot_line(axes, eq2, color=RED)

        label1 = MathTex("x + y = 2", color=GREEN).to_corner(UP+LEFT)
        label2 = MathTex("2x + y = 3", color=RED).next_to(label1, DOWN, buff=0.5)

        self.play(Create(graph1), Write(label1))
        self.play(Create(graph2), Write(label2))

        intersection_point = Dot(axes.coords_to_point(1, 1), color=YELLOW)
        intersection_label = MathTex("(1, 1)").next_to(intersection_point, RIGHT)

        self.play(Create(intersection_point), Write(intersection_label))
        intersecting_text = Text("Intersecting Lines (Unique Solution)", font_size=24).to_corner(UP + RIGHT)
        self.play(Write(intersecting_text))
        self.wait(2)

        self.clear_scene()

    def display_coincident_lines(self):
        axes, axes_labels = self.setup_axes()
        self.play(Create(axes), Write(axes_labels))

        eq = lambda x: 2 * x - 1  # Example: 2x - y = 1

        graph1 = self.plot_line(axes, eq, color=GREEN)
        graph2 = self.plot_line(axes, eq, color=RED)

        label1 = MathTex("2x - y = 1", color=GREEN).to_corner(UP+LEFT)
        label2 = MathTex("4x - 2y = 2", color=RED).next_to(label1, DOWN, buff=0.5)

        self.play(Create(graph1), Write(label1))
        self.play(Create(graph2), Write(label2))

        coincident_text = Text("Coinciding Lines (Infinite Solutions)", font_size=24).to_corner(UP + RIGHT)
        self.play(Write(coincident_text))
        self.wait(2)

        self.clear_scene()

    def display_parallel_lines(self):
        axes, axes_labels = self.setup_axes()
        self.play(Create(axes), Write(axes_labels))

        eq1 = lambda x: 2 * x + 1  # Example: 2x + y = 1
        eq2 = lambda x: 2 * x - 2  # Example: 2x + y = -2

        graph1 = self.plot_line(axes, eq1, color=GREEN)
        graph2 = self.plot_line(axes, eq2, color=RED)

        label1 = MathTex("2x + y = 1", color=GREEN).to_corner(UP+LEFT)
        label2 = MathTex("2x + y = -2", color=RED).next_to(label1, DOWN, buff=0.5)

        self.play(Create(graph1), Write(label1))
        self.play(Create(graph2), Write(label2))

        parallel_text = Text("Parallel Lines (No Solution)", font_size=24).to_corner(UP + RIGHT)
        self.play(Write(parallel_text))
        self.wait(2)

        self.clear_scene()

    def clear_scene(self):
        self.play(*[FadeOut(mob) for mob in self.mobjects])


    def coeff(self):
        self.positionChoice=[[-4,-2,0],[-1,2,0],[4,2,0],[4,-1,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Coefficient Relation","")
        p11=cvo.CVO().CreateCVO("Algebraic Interpretation", "")
        p11.extendOname(["Consistent \& Independent","Inconsistent","Consistent \& Dependent"])
        p11.setcircleradius(1.5)
        p12=cvo.CVO().CreateCVO("Graphical Representation", "")
        p12.extendOname(["Intersecting","Parallel","Coincident"])
        p12.setcircleradius(1.5)
        p13=cvo.CVO().CreateCVO("Solutions", "")
        p13.extendOname(["one","No","Many"])
        p13.setcircleradius(1.5)
        p10.cvolist.append(p11) 
        p10.cvolist.append(p12) 
        p10.cvolist.append(p13)   
        self.construct1(p10, p10)

    def consistent1(self):
        self.positionChoice=[[-4,-2,0],[0,-2,0],[-2,2,0],[4,2,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Consistent \& Independent","")
        p11 = cvo.CVO().CreateCVO("Comparison of ratios", r"$\frac{a_1}{a_2} \neq \frac{b_1}{b_2}$")
        p12=cvo.CVO().CreateCVO("Solution","One")
        p13=cvo.CVO().CreateCVO("Graph","Intersection")
        p10.cvolist.append(p11) 
        p10.cvolist.append(p12) 
        p10.cvolist.append(p13)   
        self.construct1(p10, p10)
 

    def inconsistent1(self):
        self.positionChoice = [[-4, -2, 0], [0, -2, 0], [-2, 2, 0], [4, 2, 0]]
        self.isRandom = False
        p10 = cvo.CVO().CreateCVO("Inconsistent", "")
        p11 = cvo.CVO().CreateCVO("Comparision of ratios", r"$\frac{a_1}{a_2} = \frac{b_1}{b_2} \neq \frac{c_1}{c_2}$")
        p12 = cvo.CVO().CreateCVO("Solution", "No")
        p13 = cvo.CVO().CreateCVO("Graph", "Parallel")
        p10.cvolist.append(p11) 
        p10.cvolist.append(p12) 
        p10.cvolist.append(p13)   
        self.construct1(p10, p10)  # Ensure that construct1 is supposed to be called with (p10, p10)

    def dependent1(self):
        self.positionChoice = [[-4, -2, 0], [0, -2, 0], [-2, 2, 0], [4, 2, 0]]
        self.isRandom = False
        p10 = cvo.CVO().CreateCVO("Consistent \& Dependent", "")
        p11 = cvo.CVO().CreateCVO("Comparision of ratios", r"$\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}$")
        p12 = cvo.CVO().CreateCVO("Solution", "Infinitely many")
        p13 = cvo.CVO().CreateCVO("Graph", "Coincident")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.construct1(p10, p10)  # Ensure construct1 is meant to be called with (p10, p10)


    def relation(self):
        # Title
        self.title = Text("Relationship between Coefficients and System of Equations", font_size=30).to_edge(UP)
        self.play(Write(self.title))

        # Equations Setup
        self.eq1 = MathTex("a_1 x + b_1 y + c_1 = 0", font_size=36).shift(UP * 2)
        self.eq2 = MathTex("a_2 x + b_2 y + c_2 = 0", font_size=36).next_to(self.eq1, DOWN, buff=1)
        self.play(Write(self.eq1), Write(self.eq2))

        self.wait(1)
        
    def consistent(self):
        # Case 1: Consistent (Unique Solution)
        consistent_text = Text("Consistent (Unique Solution)", font_size=24).to_edge(UP)
        condition1 = MathTex("\\frac{a_1}{a_2} \\neq \\frac{b_1}{b_2}", font_size=36).next_to(consistent_text, DOWN, buff=0.5)
        
        # Example Graph for Unique Solution
        axes1 = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": BLUE, "include_numbers": True},
            tips=False
        ).next_to(condition1,DOWN)
        line1 = axes1.plot(lambda x: -0.5 * x + 1, color=GREEN)
        line2 = axes1.plot(lambda x: x - 1, color=RED)

        self.play(Write(consistent_text), Write(condition1))
        self.play(Create(axes1), Create(line1), Create(line2))
        self.wait(2)

    def inconsistent(self):
        # Case 2: Inconsistent (No Solution)
        inconsistent_text = Text("Inconsistent (No Solution)", font_size=24).to_edge(UP)
        condition2 = MathTex("\\frac{a_1}{a_2} = \\frac{b_1}{b_2} \\neq \\frac{c_1}{c_2}", font_size=36).next_to(inconsistent_text, DOWN, buff=0.5)

        # Example Graph for No Solution
        axes2 = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": BLUE},
            tips=False
        ).next_to(condition2,DOWN)
        line3 = axes2.plot(lambda x: x + 1, color=GREEN)
        line4 = axes2.plot(lambda x: x - 1, color=RED)

        self.play(Write(inconsistent_text), Write(condition2))
        self.play(Create(axes2), Create(line3), Create(line4))
        self.wait(2)

    def dependent(self):
        # Case 3: Dependent and Consistent (Infinite Solutions)
        dependent_text = Text("Dependent and Consistent (Infinite Solutions)", font_size=24).to_edge(UP)
        condition3 = MathTex("\\frac{a_1}{a_2} = \\frac{b_1}{b_2} = \\frac{c_1}{c_2}", font_size=36).next_to(dependent_text, DOWN, buff=0.5)

        # Example Graph for Infinite Solutions
        axes3 = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": BLUE},
            tips=False
        ).next_to(condition3,DOWN)
        line5 = axes3.plot(lambda x: 0.5 * x + 1, color=GREEN)
        line6 = axes3.plot(lambda x: 0.5 * x + 1, color=RED)

        self.play(Write(dependent_text), Write(condition3))
        self.play(Create(axes3), Create(line5), Create(line6))

        # Conclusion
        conclusion = Text("The nature of the system of equations is determined by the relationships between their coefficients.", font_size=20).next_to(dependent_text, DOWN, buff=2)
        self.play(Write(conclusion))

        self.wait(2)

    def Algeb(self):
        self.positionChoice=[[-3,-2,0],[3,2,0],[3,-2,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Algebraic Method","")    
        p11=cvo.CVO().CreateCVO("Substitution Method","")    
        p12=cvo.CVO().CreateCVO("Elimination Method","")    
        p10.cvolist.append(p11) 
        p10.cvolist.append(p12)  
        self.construct1(p10, p10)

    def Subs(self):
        title = Text("SUBSTITUTION METHOD").to_edge(UP)
        self.play(Write(title))


        steps = [
            "Step1: Express one variable in terms of other(y in terms x)",
            "Step2: Substitute(y) in the second equation",
            "Step3: Solve for x",
            "Step4: Find y by substituting x",
            "Step5: Verify the solution"
        ]

        step_mobs = VGroup(*[Text(step, font_size=24) for step in steps])
        step_mobs.arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.5)
        step_mobs.next_to(title, DOWN*2, buff=1)

        self.play(Write(step_mobs))
        self.wait(3)
        self.play(FadeOut(title), FadeOut(step_mobs))

    def example_substitution(self):
        eq1 = MathTex("Equation 1 : x + y = 4")
        eq2 = MathTex("Equation 2 : 2x - y = 1")

        equations = VGroup(eq1, eq2).arrange(DOWN, center=False, aligned_edge=LEFT).to_edge(LEFT).shift(UP)

        self.play(Write(eq1))
        self.play(Write(eq2))
        self.wait(2)

        # Step 1: Solve eq1 for y
        step1 = Text("Step 1: Solve the first equation for y", font_size=24).to_edge(UP)
        self.play(Write(step1))
        self.wait(1)
        
        solve_for_y = MathTex("\\implies y = 4 - x").next_to(eq1, RIGHT)
        # self.play(Transform(eq1, solve_for_y))
        self.play(Write(solve_for_y))
        self.wait(2)

        # Step 2: Substitute y in eq2
        step2 = Text("Step 2: Substitute y in the second equation", font_size=24).to_edge(UP)
        self.play(Transform(step1, step2))
        self.wait(1)

        substitute_in_eq2 = MathTex("\\implies 2x - (4 - x) = 1").next_to(eq2, RIGHT)
        # self.play(Transform(eq2, substitute_in_eq2))
        self.play(Write(substitute_in_eq2))
        self.wait(2)

        simplified_eq2 = MathTex("\\implies 3x - 4 = 1").next_to(substitute_in_eq2, DOWN)
        # self.play(Transform(eq2, simplified_eq2))
        self.play(Write(simplified_eq2))
        self.wait(2)

        solved_x = MathTex("\\implies 3x = 5 \\implies x = \\frac{5}{3}").next_to(simplified_eq2, DOWN)
        # self.play(Transform(eq2, solved_x))
        self.play(Write(solved_x))
        self.wait(2)
        self.play(FadeOut(substitute_in_eq2),FadeOut(simplified_eq2),FadeOut(solved_x))

        # Step 3: Solve for y
        step3 = Text("Step 3: Solve for y by substituting x", font_size=24).to_edge(UP)
        self.play(Transform(step1, step3))
        self.wait(1)
        x_val=MathTex("x = \\frac{5}{3}").next_to(eq1, UP * 1.5)
        self.play(Write(x_val))
        self.wait(1)
         
        substitute_x = MathTex("\\implies y = 4 - \\frac{5}{3}").next_to(solve_for_y, RIGHT)
        # self.play(Transform(eq1, substitute_x))
        self.play(Write(substitute_x))
        self.wait(2)

        solved_y = MathTex("y = \\frac{7}{3}").next_to(substitute_x, DOWN)
        # self.play(Transform(eq1, solved_y))
        self.play(Write(solved_y))
        self.wait(2)
        self.play(FadeOut(solve_for_y),FadeOut(substitute_x),solved_y.animate.next_to(x_val, RIGHT))
        # Step 4: Verify the solution
        step4 = Text("Step 4: Verify the solution", font_size=24).to_edge(UP)
        self.play(Transform(step1, step4))
        self.wait(1)


        verification = MathTex(
            "\\text{Check: }",
            "\\left(\\frac{5}{3}, \\frac{7}{3}\\right)"
        ).next_to(eq2, DOWN)
        
        self.play(Write(verification))
        self.wait(1)

        verified_eq1 = MathTex(
            "\\implies \\frac{5}{3} + \\frac{7}{3} = 4"
        ).next_to(eq1, RIGHT)

        verified_eq2 = MathTex(
            "\\implies 2 \\cdot \\frac{5}{3} - \\frac{7}{3} = 1"
        ).next_to(eq2, RIGHT)

        self.play(Write(verified_eq1))
        self.wait(2)
        self.play(Transform(verified_eq1,verified_eq2))
        self.wait(2)

        # Clear Scene
        self.play(FadeOut(step1), FadeOut(eq1), FadeOut(eq2), FadeOut(verification), FadeOut(verified_eq1), FadeOut(verified_eq2),FadeOut(x_val),FadeOut(solved_y))



    def Elim(self):
        title = Text("Elimination Method").to_edge(UP)
        self.play(Write(title))

        steps = [
            "Step1: Write equations in standard form ax+by=c",
            "Step2: Equalize coefficients by multiplying equations",
            "Step3: Eliminate variable by adding or subtracting",
            "Step4: Solve for Remaining variable",
            "Step5: Find Eliminated Variable by substituting"
        ]

        step_mobs = VGroup(*[Text(step, font_size=24) for step in steps])
        step_mobs.arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.5)
        step_mobs.next_to(title, DOWN*2, buff=1)

        self.play(Write(step_mobs))
        self.wait(3)
        self.play(FadeOut(title), FadeOut(step_mobs))

    def solve_example(self):
        step1 = Text("Step 1: Example Equations", font_size=28).to_edge(UP)
        eq1 = MathTex("Equation 1 : 3x + 4y = 20")
        eq2 = MathTex("Equation 2 : 5x - 2y = 10")
        equations = VGroup(eq1, eq2).arrange(DOWN, center=False, aligned_edge=LEFT).to_edge(LEFT).shift(UP)

        self.play(Write(step1))
        self.play(Write(eq1), Write(eq2))
        self.wait(1)

        # Step 2: Equalize coefficients
        step2 = Text("Step 2: Equalize coefficients by multiplying equations", font_size=28).to_edge(UP)
        self.play(ReplacementTransform(step1, step2))

        multiplier1 = MathTex("\\times 2", color=YELLOW).next_to(eq1, RIGHT, buff=0.5).scale(0.8)
        self.play(Write(multiplier1))

        eq1_multiplied = MathTex("\\implies 6x + 8y = 40").next_to(multiplier1, RIGHT).scale(0.8)
        # self.play(Transform(eq1, eq1_multiplied))
        self.play(Write(eq1_multiplied))
        self.wait(1)

        multiplier2 = MathTex("\\times 4", color=YELLOW).next_to(eq2, RIGHT, buff=0.5).scale(0.8)
        self.play(Write(multiplier2))

        eq2_multiplied = MathTex("\\implies 20x - 8y = 40").next_to(multiplier2,RIGHT).scale(0.8)
        # self.play(Transform(eq2, eq2_multiplied))
        self.play(Write(eq2_multiplied))

        self.wait(1)

        # Step 3: Eliminate variable
        step3 = Text("Step 3: Eliminate variable by adding or subtracting", font_size=28).to_edge(UP)
        self.play(ReplacementTransform(step2, step3))

        add_label = MathTex("+").next_to(eq2_multiplied, LEFT + DOWN, buff=0.5).scale(0.8)
        self.play(Write(add_label))
        self.wait(1)
        
        sum_eq = MathTex("\\implies 26x = 80").next_to(eq2_multiplied, DOWN, buff=1).scale(0.8)
        self.play(Write(sum_eq))
        self.wait(1)

        # self.play(FadeOut(step1),FadeOut(eq1),FadeOut(eq2),FadeOut(multiplier1),FadeOut(multiplier2),FadeOut(add_label))

        # Step 4: Solve for remaining variable
        step4 = Text("Step 4: Solve for remaining variable", font_size=28).to_edge(UP)
        self.play(ReplacementTransform(step3, step4))

        solve_x = MathTex("x = \\frac{80}{26} = \\frac{40}{13}").next_to(sum_eq,DOWN)
        self.play(Write(solve_x))
        self.wait(1)
        x_val=MathTex("x = \\frac{40}{13}").next_to(eq1,UP * 0.5)
        self.play(Write(x_val))
        self.wait(1)


        self.play(FadeOut(multiplier1),FadeOut(eq1_multiplied),FadeOut(multiplier2),FadeOut(eq2_multiplied),FadeOut(add_label),FadeOut(sum_eq),FadeOut(solve_x))
        # Step 5: Substitute back
        
        step5 = Text("Step 5: Find eliminated variable by substituting", font_size=28).to_edge(UP)
        self.play(ReplacementTransform(step4, step5))

        substitute_step = Text("Substitute x = 40/13 into 3x + 4y = 20", font_size=24).next_to(step5, DOWN, buff=1).scale(0.8)
        self.play(Write(substitute_step))
        
        substituted_eq = MathTex("\\implies 3 \\times \\frac{40}{13} + 4y = 20").next_to(eq1, RIGHT, buff=1).scale(0.8)
        self.play(Write(substituted_eq))
        self.wait(2)
        
        # self.play(ReplacementTransform(substitute_step, substituted_eq))

        solve_y = MathTex("4y = 20 - \\frac{120}{13}").next_to(substituted_eq, DOWN).scale(0.8)
        simplify_y = MathTex("4y = \\frac{140}{13}").next_to(solve_y, DOWN * 1.5).scale(0.8)
        final_y = MathTex("y = \\frac{35}{13}").next_to(simplify_y, DOWN).scale(0.8)

        self.play(Write(solve_y))
        self.wait(1)
        self.play(Write(simplify_y))
        self.wait(2)
        # self.play(Transform(solve_y, simplify_y))
        self.play(Write(final_y))
        self.wait(1)
        self.play(FadeOut(substitute_step),FadeOut(substituted_eq),FadeOut(solve_x),FadeOut(solve_y),FadeOut(simplify_y),final_y.animate.next_to(x_val,RIGHT))
    # Display the final solution
        final_solution = MathTex("(x, y) = \\left(\\frac{40}{13}, \\frac{35}{13}\\right)").next_to(eq2, DOWN + RIGHT, buff=1).scale(0.8)
        self.play(Write(final_solution))
        self.wait(2)

        # Clear scene
        self.clear_scene()

    def clear_scene(self):
        self.play(*[FadeOut(mob) for mob in self.mobjects])


    def SetDeveloperList(self):  
        self.DeveloperList="Gayathri Veeramreddy"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="LinearEquations.py"

if __name__ == "__main__":
    scene=LinearEq()
    scene.render()