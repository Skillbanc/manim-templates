from manim import *
from AbstractAnim import AbstractAnim
import cvo


class Multiplication(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.example1()
        self.fadeOutCurrentScene()
        self.frog()
        self.fadeOutCurrentScene()
        self.multiplybyzero()
        self.fadeOutCurrentScene()
        self.multiplybyone()
        self.fadeOutCurrentScene()
        self.multiplybignum()
        self.fadeOutCurrentScene()
        self.multiplydaily()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        


        



    def Introduction(self):
        self.setNumberOfCirclePositions(3)
        self.angleChoice = [TAU/4,TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Multiplication","")
        p11=cvo.CVO().CreateCVO("Definition ", "Repeated Addition is called as Multiplication").setPosition([3,2,0])
        p12=cvo.CVO().CreateCVO("Symbol", "\\times").setPosition([3,-2,0])
        p12.SetIsMathText(True)
        p11.setcircleradius(1.5)
        p12.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)

    def example1(self):
        title = Text("What is 5 times 3?", font_size=48).to_edge(UP)
        underline = Line(
            start=title.get_left() + DOWN * 0.3,
            end=title.get_right() + DOWN * 0.3,
            color=YELLOW
        )
        self.play(Write(title))
        #self.play(Create(underline))  
        self.wait(1)

        # Represent 5 times 3 as 5 x 3
        step1 = Text("5 times 3 is represented as", font_size=36).next_to(title, DOWN, buff=1)
        self.play(Write(step1))
        self.wait(1)

        # 5 x 3
        representation = Text("5 x 3", font_size=48)
        representation.next_to(step1, DOWN, buff=1)
        self.play(Write(representation))
        self.wait(1)

        # Arrow to x indicating multiplication
        arrow = Arrow(start=representation[1].get_bottom(), end=representation[1].get_bottom() + DOWN * 1.5, buff=0.1)
        arrow_text = Text("multiplication symbol", font_size=24).next_to(arrow.get_end(), DOWN)
        self.play(Create(arrow), Write(arrow_text))
        self.wait(2)

        # Clear representations
        self.play(FadeOut(step1), FadeOut(representation), FadeOut(arrow), FadeOut(arrow_text))

        # Visualize Multiplication as Repeated Addition
        step2 = Text("5 times 3 means adding 5 three times:", font_size=36).next_to(title, DOWN, buff=1)
        self.play(Write(step2))
        self.wait(1)

        addition_visual = VGroup(
            Text("5", font_size=36),
            Text("+ 5", font_size=36),
            Text("+ 5", font_size=36)
        ).arrange(RIGHT, buff=0.2).next_to(step2, DOWN, buff=1)
        self.play(Write(addition_visual))
        self.wait(1)

        # Show Calculation Process
        calculation = Text("5 x 3 = 5 + 5 + 5", font_size=36).next_to(addition_visual, DOWN, buff=1)
        self.play(Write(calculation))
        self.wait(1)

        # Display the Result
        result = Text("= 15", font_size=48, color=YELLOW).next_to(calculation, DOWN, buff=1)
        self.play(Write(result))
        self.wait(2)

        # Fade out
        self.play(FadeOut(title), FadeOut(step2), FadeOut(addition_visual), FadeOut(calculation), FadeOut(result))


    def frog(self):
        number_line = NumberLine(
            x_range=[0, 18, 1], 
            length=10, 
            color=BLUE, 
            include_numbers=True, 
            label_direction=DOWN
        )
        

        # Create the frog as a Dot
        frog = Dot(color=GREEN).scale(1.5)
        frog.move_to(number_line.n2p(0))  # Start at 0 on the number line

        # Create text for the title
        title = Text("Frogie Jumps", font_size=48).to_edge(UP)
        underline = Line(
            start=title.get_left() + DOWN * 0.3,
            end=title.get_right() + DOWN * 0.3,
            color=YELLOW
        )
        

        # Create text for the multiplication explanation
        explanation = Tex("A frog jumped 3 steps in a single jump. It jumped 6 times.",font_size=35).next_to(number_line, DOWN,buff=1)

        explanation1 = Tex("So the frog jumped a total of 3 x 6 = 18 steps",font_size=35).next_to(explanation, DOWN,buff=0.6)

        # Add number line, texts, and frog to the scene
        #self.add(number_line, frog, title, explanation)
        self.play(Write(title))
        self.play(Create(underline))
        self.wait(1)
        self.play(Create(number_line))
        self.wait(1)
        self.add(frog)
        self.play(Write(explanation))
        self.wait(1)
        

        # Function to create a jumping path with a dashed line
        def create_jump_path(start, end):
            control_point = start + (end - start) / 2 + UP * 1.5  # Control point for the jump
            path = CubicBezier(start, control_point, control_point, end)
            dashed_path = DashedVMobject(path, num_dashes=15, color=GREEN)
            return path, dashed_path

        # Move the frog in steps of 3, six times, with a jumping effect and dashed lines
        for i in range(1, 7):
            start_position = number_line.n2p(3 * (i - 1))
            end_position = number_line.n2p(3 * i)
            jump_path, dashed_jump_path = create_jump_path(start_position, end_position)
            
            self.play(Create(dashed_jump_path), run_time=0.5)
            self.play(MoveAlongPath(frog, jump_path), run_time=0.5)
            self.wait(0.5)
       
        self.play(Write(explanation1))
        self.wait(1)

    def multiplybyzero(self):
        title = Text("Multiplication with Zero", font_size=48).to_edge(UP)
        underline = Line(
            start=title.get_left() + DOWN * 0.3,
            end=title.get_right() + DOWN * 0.3,
            color=YELLOW
        )
        self.play(Write(title))
        self.play(Create(underline))
        self.wait(1)

        # Summary
        summary1 = Text(
            "Multiplying any number by zero always results in zero.",
            font_size=30
        ).next_to(title, DOWN, buff=0.8)
        self.play(Write(summary1))
        self.wait(1)

        # Examples title
        example1 = Text("Examples:", font_size=36).next_to(summary1.get_left(), DOWN+RIGHT*0.1, buff=1)
        self.play(Write(example1))
        self.wait(1)

        # Examples for multiplication with zero
        multiply1 = Text("0 x 1 = 0", font_size=36).next_to(example1, RIGHT, buff=0.5)
        multiply2 = Text("0 x 2 = 0", font_size=36).next_to(multiply1, DOWN, buff=0.3).align_to(multiply1, LEFT)
        multiply3 = Text("0 x 3 = 0", font_size=36).next_to(multiply2, DOWN, buff=0.3).align_to(multiply1, LEFT)
        multiply4 = Text("0 x 4 = 0", font_size=36).next_to(multiply3, DOWN, buff=0.3).align_to(multiply1, LEFT)
        multiply5 = Text("0 x 5 = 0", font_size=36).next_to(multiply4, DOWN, buff=0.3).align_to(multiply1, LEFT)
        multiply6 = Text("0 x 6 = 0", font_size=36).next_to(multiply5, DOWN, buff=0.3).align_to(multiply1, LEFT)

        # Display examples
        self.play(Write(multiply1))
        self.play(Write(multiply2))
        self.play(Write(multiply3))
        self.play(Write(multiply4))
        self.play(Write(multiply5))
        self.play(Write(multiply6))
        self.wait(1)

        # Fade out all elements
        self.play(FadeOut(title, underline, summary1, example1, multiply1, multiply2, multiply3, multiply4, multiply5, multiply6))

        

    def multiplybyone(self):
        title = Text("Multiplication with One", font_size=48).to_edge(UP)
        underline = Line(
            start=title.get_left() + DOWN * 0.3,
            end=title.get_right() + DOWN * 0.3,
            color=YELLOW
        )
        self.play(Write(title))
        self.play(Create(underline))
        self.wait(1)

        summary1 = Text(
            "Multiplying any number by one always results in the same number.",
            font_size=30
        ).next_to(title, DOWN, buff=0.8)
        self.play(Write(summary1))
        self.wait(1)


       
        example1 = Text("Examples :", font_size=36).next_to(summary1.get_left(), DOWN+RIGHT*0.1, buff=1)
        self.play(Write(example1))
        self.wait(1)

        # Repeated Addition Visualization for Example 1
        multiply1 = Text("1 x 1 = 1", font_size=36).next_to(example1,RIGHT, buff=0.5)
        multiply2 = Text("1 x 2 = 1 + 1 = 2", font_size=36).next_to(multiply1, DOWN, buff=0.3).align_to(multiply1, LEFT)
        multiply3 = Text("1 x 3 = 1 + 1 + 1 = 3", font_size=36).next_to(multiply2, DOWN, buff=0.3).align_to(multiply1, LEFT)
        multiply4 = Text("1 x 4 = 1 + 1 + 1 + 1 = 4", font_size=36).next_to(multiply3, DOWN, buff=0.3).align_to(multiply1, LEFT)
        multiply5 = Text("1 x 5 = 1 + 1 + 1 + 1 + 1 = 5", font_size=36).next_to(multiply4, DOWN, buff=0.3).align_to(multiply1, LEFT)
        multiply6 = Text("1 x 6 = 1 + 1 + 1 + 1 + 1 + 1 = 6", font_size=36).next_to(multiply5, DOWN, buff=0.3).align_to(multiply1, LEFT)


        self.play(Write(multiply1))
        self.play(Write(multiply2))
        self.play(Write(multiply3))
        self.play(Write(multiply4))
        self.play(Write(multiply5))
        self.play(Write(multiply6))
        self.wait(1)


    def multiplybignum(self):

         # Title and Underline
        title = Text("Multiplying Bigger Numbers").scale(0.8).to_edge(UP)
        self.play(Write(title))

        
        underline = Line(
            start=title.get_left() + DOWN * 0.3,
            end=title.get_right() + DOWN * 0.3,
            color=YELLOW
        )
       
        self.play(Create(underline))
        self.wait(1)

        # Example description
        example_description = MathTex("\\text{Example 1 : } 21 \\times 3").scale(0.75).next_to(title, DOWN,buff=1).shift(LEFT*3.5)
        self.play(Write(example_description))

        # Initial numbers
        #num1 = MathTex("21").shift(UP*2)
        num1 = MathTex("21").next_to(example_description, DOWN+RIGHT*0.4,buff=1)
        num2 = MathTex("3").next_to(num1, DOWN)
        times_sign = MathTex("\\times").next_to(num2, LEFT)
        underline = Line(num2.get_right(), num2.get_right() + RIGHT * 1.5).shift(DOWN*0.5, LEFT*1)
        #self.play(Write(num1), Write(num2), Write(times_sign), Write(underline))
        self.play(Write(num1))
        self.play(Write(num2))
        self.play(Write(times_sign))
        self.play(Write(underline))


    
        explanation1 = Tex("First multiply 3 with 1 at one's place").scale(0.6).to_edge(RIGHT).shift(UP*1.5)
        self.play(Write(explanation1))
        self.wait(1)

        # Transform to show first multiplication step
        step1_text = MathTex("3 \\times 1 = 3").scale(0.75).next_to(explanation1, DOWN, buff=0.3)
        self.play(Write(step1_text))
        self.wait(1)
       

        # Explanation step 2: Then multiply 3 with 2
        explanation2 = Tex("Then multiply 3 with 2 at ten's place").scale(0.6).next_to(step1_text, DOWN,buff=0.5)
        self.play(Write(explanation2))
        self.wait(1)

        # Transform to show second multiplication step
        step2_text = MathTex("3 \\times 20 = 60").scale(0.75).next_to(explanation2, DOWN, buff=0.3)
        self.play(Write(step2_text))
        self.wait(1)

        # Show total multiplication process
        final_step_text = MathTex("21 \\times 3 = 3 + 60 ").scale(0.75).next_to(step2_text, DOWN, buff=0.3)
        self.play(Write(final_step_text))
        self.wait(1)

        final_step_text1 = MathTex(" = 63 ").scale(0.75).next_to(final_step_text, DOWN, buff=0.3)
        self.play(Write(final_step_text1))
        self.wait(1)

        result_step1 = MathTex("63").next_to(underline, DOWN).set_color(YELLOW)
        self.play(Write(result_step1))
        self.wait(1)

        final_result = MathTex("21 \\times 3 = 63").scale(0.9).next_to(result_step1, DOWN, buff=1).set_color(BLUE)
        self.play(Write(final_result))
        self.wait(2)


        self.play(
            FadeOut(num1), FadeOut(num2), FadeOut(times_sign),
            FadeOut(underline), FadeOut(step1_text), FadeOut(step2_text), FadeOut(final_step_text), FadeOut(final_result),
            FadeOut(final_step_text1),FadeOut(result_step1),FadeOut(explanation1),FadeOut(explanation2)
        )
        self.wait(1)

        example1_description = MathTex("\\text{Example 2: } 36 \\times 4").scale(0.75).next_to(title, DOWN,buff=1).shift(LEFT*3.5)
        self.play(Transform(example_description, example1_description))

        num1 = MathTex("36").next_to(example1_description, DOWN+RIGHT*0.4,buff=1)
        num2 = MathTex("4").next_to(num1, DOWN)
        times_sign = MathTex("\\times").next_to(num2, LEFT)
        underline = Line(num2.get_right(), num2.get_right() + RIGHT * 1.5).shift(DOWN*0.5, LEFT*1)
        #self.play(Write(num1), Write(num2), Write(times_sign), Write(underline))
        self.play(Write(num1))
        self.play(Write(num2))
        self.play(Write(times_sign))
        self.play(Write(underline))

        explanation1 = Tex("First multiply 4 with 6 at one's place").scale(0.6).to_edge(RIGHT).shift(UP*1.5)
        self.play(Write(explanation1))
        self.wait(1)

        # Transform to show first multiplication step
        step1_text = MathTex("4 \\times 6 = 24").scale(0.75).next_to(explanation1, DOWN, buff=0.3)
        self.play(Write(step1_text))
        self.wait(1)
       

        # Explanation step 2: Then multiply 3 with 2
        explanation2 = Tex("Then multiply 4 with 3 at ten's place").scale(0.6).next_to(step1_text, DOWN,buff=0.5)
        self.play(Write(explanation2))
        self.wait(1)

        # Transform to show second multiplication step
        step2_text = MathTex("4 \\times 30 = 120").scale(0.75).next_to(explanation2, DOWN, buff=0.3)
        self.play(Write(step2_text))
        self.wait(1)

        final_step_text = MathTex("36 \\times 4 = 120 + 24 ").scale(0.75).next_to(step2_text, DOWN, buff=0.3)
        self.play(Write(final_step_text))
        self.wait(1)

        final_step_text1 = MathTex(" = 144 ").scale(0.75).next_to(final_step_text, DOWN, buff=0.3)
        self.play(Write(final_step_text1))
        self.wait(1)

        result_step1 = MathTex("144").next_to(underline, DOWN).set_color(YELLOW)
        self.play(Write(result_step1))
        self.wait(1)

        final_result = MathTex("36 \\times 4 = 144").scale(0.9).next_to(result_step1, DOWN, buff=1).set_color(BLUE)
        self.play(Write(final_result))
        self.wait(2)


    def multiplydaily(self):
       
        title = Text("Multiplication in daily life", font_size=48).to_edge(UP)
        self.play(Write(title))
        
        underline = Line(
            start=title.get_left() + DOWN * 0.3,
            end=title.get_right() + DOWN * 0.3,
            color=YELLOW
        )
        
        self.play(Create(underline))
        self.wait(1)

        example1 = Text("Example :", font_size=30).shift(UP*2).to_edge(LEFT)
        self.play(Write(example1))
        self.wait(1)

        # Display the initial statement
        statement1 = Text("Surya's age is twice that of Ramya.", font_size=32).shift(UP*2).next_to(example1,RIGHT)
        self.play(Write(statement1))
        self.wait(1)

        statement2 = Text("Ramya is 9 years. What is Surya's age?", font_size=32).next_to(statement1,DOWN,buff=0.3)
        self.play(Write(statement2))
        self.wait(2) 

        # Centering Calculation steps
        step1 = Tex("Ramya's age = 9 years", font_size=36).shift(UP*0.3)  # Slightly above center
        step2 = Tex("Surya's age = Twice Ramya's age", font_size=36).next_to(step1, DOWN, buff=0.3)
        step3 = Tex("= 2 x Ramya's age", font_size=36).next_to(step2, DOWN, buff=0.3)
        step4 = Tex("= 2 x 9", font_size=36).next_to(step3, DOWN, buff=0.3)
        step5 = Tex("= 18", font_size=36).next_to(step4, DOWN, buff=0.3)

        # Play steps one after another
        self.play(Write(step1))
        self.wait(1)
        self.play(Write(step2))
        self.wait(1)
        self.play(Write(step3))
        self.wait(1)
        self.play(Write(step4))
        self.wait(1)
        self.play(Write(step5))
        self.wait(1)

        # Final answer centered below steps
        answer = Tex("Surya's age is 18 years", font_size=36).next_to(step5, DOWN, buff=0.3)
        self.play(Write(answer))
        self.wait(2)

        #self.play(FadeOut(title, statement1, statement2, step1, step2, step3, step4, step5, answer))


        


    



    def SetDeveloperList(self):  
        self.DeveloperList="Agraz Gopu"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade3Chapter6Multiplication.py"

if __name__ == "__main__":
        scene = Multiplication()  
        scene.render()  
