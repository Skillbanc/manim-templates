from manim import *
from AbstractAnim import AbstractAnim
import cvo
from numpy import size

class multiplication(AbstractAnim):
 
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.show_intromul()
        self.fadeOutCurrentScene()
        self.introc1()
        self.fadeOutCurrentScene()
        self.define_multiplication()
        self.fadeOutCurrentScene()
        self.multiplication_symbol()
        self.fadeOutCurrentScene()
        self.Two()
        self.fadeOutCurrentScene()
        self.multiplicationexample()
        self.fadeOutCurrentScene()
        self.example1()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()


    def show_intromul(self):
        # Title for the scene
        intro_title = Text(" Multiplication of Numbers-1", font_size=60, color=BLUE)
        self.play(Write(intro_title))
        self.wait(2)
        self.play(FadeOut(intro_title))


    

        
    def Two(self):

        title = Text("Multiplication", color=BLUE).scale(0.6).to_edge(UP*0.4)
        # Add title to scene
        self.play(Write(title))
        self.wait(2)


        # title = Text("2", color=WHITE,fill_opacity=0.28).scale(6)
        # # Add title to scene
        # self.play(Write(title))
        # self.wait(2)

        table_data = [
         #  ["Numbr of chains", "A person counted the beads in the chains and \nwrote the numbers as shown below."],
            ["1 X 2", "2", "2"],
            ["2 X 2", "2 + 2", "4"],
            ["3 X 2 ", "2 + 2 + 2", "6"],
            ["4 X 2", "2 + 2 + 2 + 2", "8"],
            ["5 X 2", "2 + 2 + 2 + 2 + 2", "10"],
            ["6 X 2", "2 + 2 + 2 + 2 + 2 + 2", "12"],
            ["7 X 2", "2 + 2 + 2 + 2 + 2 + 2 + 2", "14"],
            ["8 X 2", "2 + 2 + 2 + 2 + 2 + 2 + 2 + 2", "16"],
            ["9 X 2 ", "2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2", "18"],
            ["10 X 2", "2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2", "20"]
        ]
        

        # Create table with custom column widths
        table = Table(
            table_data,
          #  col_labels=[Text("Number of chains"), Text("A person counted the beads in the chains \nand wrote the numbers as shown below.")],
            include_outer_lines=True,
            line_config={"stroke_width": 3, "color": RED},
        ).scale(0.5).set_opacity(20).stretch_to_fit_depth(4).shift(LEFT*2.5)

        # Add table to scene
        self.play(Create(table))
        self.wait(4)

# Create equations for the multiplication table
        equations = VGroup(
            *[MathTex(f"{i}\\times 2 =", i* 2) for i in range(1, 11)]
        ).arrange(DOWN, buff=0.3).shift(RIGHT*5).set_color(YELLOW)

        # Display equations one by one
        for equation in equations:
            self.play(Write(equation))
            self.wait(0.5)

        # Fade out equations
        self.play(FadeOut(equations))
        self.wait()




    def multiplication_symbol(self):
        # Title for the multiplication symbol
        symbol_title = Text("The Symbol of Multiplication", font_size=48, color=YELLOW).to_edge(UP)
        self.play(Write(symbol_title))

        # Multiplication symbol
        symbol = Text("x", font_size=96, color=RED).next_to(symbol_title, DOWN, buff=1)

        # Explanation of the symbol
        symbol_explanation = Text(
            "The symbol for multiplication is ' x '",
            font_size=24
        ).next_to(symbol, DOWN, buff=0.5)

        self.play(Write(symbol))
        self.wait(1)
        self.play(Write(symbol_explanation))
        self.wait(3)
        self.play(FadeOut(symbol_title), FadeOut(symbol), FadeOut(symbol_explanation))


    def multiplicationexample(self):

        # Title
        title = Text("Repeated Addition to Multiplication",color=GOLD_E).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Example
        example_text = MathTex("4 + 4 + 4 + 4 + 4", "=", "5", r"\times", "4", "=", "20")
        example_text.scale(0.8).next_to(title, DOWN, buff=1)
        
        self.play(Write(example_text))
        self.wait(1)
        
        # self.play(Write(example_text[3:]))
        # self.wait(1)
        
        # self.play(example_text.animate.set_color(YELLOW))
        self.wait(1)

        # A) 7 + 7 + 7 + 7
        a_text = MathTex("7 + 7 + 7 + 7", "=", "4", r"\times", "7", "=", "28")
        a_text.scale(0.8).next_to(example_text, DOWN, buff=0.8, aligned_edge=LEFT)
        
        self.play(Write(a_text))
        self.wait(1)
        
        # self.play(Write(a_text[3:]))
        # self.play(a_text.set_color(YELLOW))
        self.wait(1)

        # B) 3 + 3 + 3 + 3 + 3 + 3 + 3
        b_text = MathTex("3 + 3 + 3 + 3 + 3 + 3 + 3", "=", "7", r"\times", "3", "=", "21")
        b_text.scale(0.8).next_to(a_text, DOWN, buff=0.5, aligned_edge=LEFT)
        
        self.play(Write(b_text))
        self.wait(1)
        
        # self.play(Write(b_text[3:]))
        # self.play(b_text.set_color(YELLOW))
        self.wait(1)

        # C) 6 + 6 + 6 + 6 + 6
        c_text = MathTex("6 + 6 + 6 + 6 + 6", "=", "5", r"\times", "6", "=", "30")
        c_text.scale(0.8).next_to(b_text, DOWN, buff=0.5, aligned_edge=LEFT)
        
        self.play(Write(c_text))
        self.wait(1)
        
        # self.play(Write(c_text[3:]))
        # self.play(c_text.set_color(YELLOW))
        self.wait(1)

        # D) 2 + 2 + 2 + 2 + 2 + 2
        d_text = MathTex("2 + 2 + 2 + 2 + 2 + 2", "=", "6", r"\times", "2", "=", "12")
        d_text.scale(0.8).next_to(c_text, DOWN, buff=0.5, aligned_edge=LEFT)
        
        self.play(Write(d_text))
        self.wait(1)
        
        # self.play(Write(d_text[3:]))
        # self.play(d_text.set_color(YELLOW))
        self.wait(1)

        self.wait(2)

# To run the animation, use the following command in your terminal:
# manim -pql your_script.py RepeatedAdditionToMultiplication
    def introc1(self):
         
        self.setNumberOfCirclePositions(3)
        #self.angleChoice = [0,0,0]
        self.isRandom = False
        p8=cvo.CVO().CreateCVO("MULTIPLICATION","")
        p9=cvo.CVO().CreateCVO("Defination","Multiplication is adding a number to itself\na certain number of times.").setPosition([2,2,2])
        p7=cvo.CVO().CreateCVO("Symbol","'X'").setPosition([2,0,2])
        p10=cvo.CVO().CreateCVO("Example","4 X 5=20").setPosition([2,-2.5,2])
        p8.cvolist.append(p9)
        p8.cvolist.append(p7)
        p8.cvolist.append(p10)
        self.construct1(p8,p8)

    def SetDeveloperList(self):
        self.DeveloperList="Sai Krishna Bikkumalla"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade2Ch9Multiplication.py"

    def example1(self):
        # Create the heading "Example"
        heading = Text("Example",color=RED).scale(1.5).to_edge(UP)

        # Create a grid of dots (5 rows, 3 columns) with green color
        rows, cols = 5, 3
        dot_grid = VGroup(*[Dot(color=GREEN) for _ in range(rows * cols)])
        dot_grid.arrange_in_grid(rows=rows, cols=cols, buff=MED_LARGE_BUFF)
        
        # Position the dot grid on the left side
        dot_grid.to_edge(LEFT)
        
        # Create the numbers and the multiplication equation
        number_5 = Text("5 in rows",color=BLUE).next_to(dot_grid, RIGHT, buff=LARGE_BUFF)
        number_3 = Text("3 in columns",color=BLUE).next_to(number_5, RIGHT, buff=LARGE_BUFF)
        multiplication_eq = Text("5 × 3 = 15",color=BLUE).next_to(number_3, RIGHT, buff=LARGE_BUFF)
        
        # Animate the creation of the heading
        self.play(Write(heading))
        
        # Animate the creation of the dot grid
        self.play(Create(dot_grid))
        
        # Wait for a moment
        self.wait(1)
        
        # Animate the appearance of the numbers and the equation
        self.play(Write(number_5))
        self.wait(1)
        self.play(Write(number_3))
        self.wait(1)
        self.play(Write(multiplication_eq))
        
        # Hold the final frame for 2 seconds
        self.wait(2)

# To render the scene, use the following command in your terminal:
# manim -pql multiplication_scene.py MultiplicationScene


    def define_multiplication(self):
        # Title for the definition
        definition_title = Text("What is Multiplication?", font_size=48, color=YELLOW).to_edge(UP)
        self.play(Write(definition_title))

        # Definition of multiplication
        definition = Text(
            "Multiplication is adding a number to itself\na certain number of times.",
            font_size=30
        ).next_to(definition_title, DOWN)

        self.play(Write(definition))
        self.wait(3)

        # Example of multiplication: 3 groups of 2 apples
        example_title = Text("Example: 3 x 2", font_size=36, color=YELLOW).next_to(definition, DOWN*0.5, buff=1)
        self.play(Write(example_title))

        # Illustration of the example
        apples = VGroup(*[SVGMobject("apple.svg").scale(0.5) for _ in range(6)])
        apples.arrange_in_grid(rows=3, cols=2, buff=0.5).next_to(example_title, DOWN*0.5, buff=1)

        self.play(Create(apples))
        self.wait(1)

        # Explanation of the example
        example_explanation = Text(
            "3 groups of 2 apples each.\nSo, 3 x 2 = 6.",
            font_size=24
        ).next_to(apples, DOWN, buff=0.5)
        self.play(Write(example_explanation))
        self.wait(3)

        # Fade out all the elements
        self.play(FadeOut(definition_title), FadeOut(definition), FadeOut(example_title), FadeOut(apples), FadeOut(example_explanation))

# Save this as `apple.svg`
SVG_CODE_APPLE = '''
<svg height="100" width="100" xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="red" />
  <line x1="50" y1="20" x2="50" y2="10" stroke="brown" stroke-width="4" />
  <circle cx="50" cy="8" r="4" fill="green" />
</svg>
'''

with open("apple.svg", "w") as f:
    f.write(SVG_CODE_APPLE)
    
    


if __name__ == "__main__":
    scene = multiplication()
    scene.render()