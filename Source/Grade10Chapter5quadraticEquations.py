# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla
import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo
class quadraticAnim(AbstractAnim):
     # use the appropriate method based on how the data is stored
    def construct(self):
           self.RenderSkillbancLogo()
           self.constructDataByCVO()
           self.fadeOutCurrentScene()
           self.quad111()
           self.fadeOutCurrentScene()
           self.quad1122()
           self.fadeOutCurrentScene() 
           self.quad1133()
           self.fadeOutCurrentScene()
         #self.quad1144()
         # self.fadeOutCurrentScene()
           self.quad1155()
           self.fadeOutCurrentScene() 
           self.quad1166()
           self.fadeOutCurrentScene()
           self.RenderEquality1()
           self.fadeOutCurrentScene()
           self.tryfile()
           self.fadeOutCurrentScene()
           self.GithubSourceCodeReference()


# render using CVO data object
# render using CVO data object
    def constructDataByCVO(self):
    # Assuming this sets some property related to circle positions
         self.setNumberOfCirclePositions(4)
    
    # Create content objects with positions and set circle size
         p10 = cvo.CVO().CreateCVO("quadratic equations", "").setPosition([-4, 2, 0])
         p11 = cvo.CVO().CreateCVO("Standard form", "$ax^2 + bx + c = 0$").setPosition([0, 2, 0]).setangle(-TAU/4)
         p12 = cvo.CVO().CreateCVO("real numbers", "a, b, c are real numbers").setPosition([-2, -2, 0]).setangle(-TAU/4)
         p13 = cvo.CVO().CreateCVO("here", "$a \\neq 0$").setPosition([2, -2, 0]).setangle(-TAU/4)


         p11.setcircleradius(1.5)
         p12.setcircleradius(1.5)
    
    
    # Append content objects to p10
         p10.cvolist.append(p11)
         p11.cvolist.append(p12)
         p11.cvolist.append(p13)

    # Assuming this method exists to handle further construction or processing
         self.construct1(p10, p10)  # Passing p10 twice as arguments, adjust if needed

    

     
    def quad111(self):
        

   
        self.setNumberOfCirclePositions(6)
        self.isRandom=False
     
        p20=cvo.CVO().CreateCVO("equation","$3x^2-5x+7 = 0$").setPosition([-4,2,0])
        p21=cvo.CVO().CreateCVO("variable a","3").setPosition([0,-2.5,0]).setangle(-TAU/4)
        p22=cvo.CVO().CreateCVO("variable b","-5").setPosition([0,2,0]).setangle(-TAU/4)
        p23=cvo.CVO().CreateCVO("variable c","7").setPosition([-4,-2,0]).setangle(-TAU/4)
        p24=cvo.CVO().CreateCVO("nature of roots","imaginary roots").setPosition([4,2,0]).setangle(-TAU/4)
        p25=cvo.CVO().CreateCVO("formula to find the roots","$b^2-4ac$").setPosition([4,-2,0]).setangle(-TAU/4)


        p20.cvolist.append(p21)
        p20.cvolist.append(p22)
        p20.cvolist.append(p23)
        p20.cvolist.append(p24)
        p20.cvolist.append(p25)

        
       
       
        self.construct1(p20,p20)   

# To render the scene, use the following command in your terminal:
# manim -pql circle_diagram.py CircleDiagram

    def quad1122(self):
         self.setNumberOfCirclePositions(5)
         self.isRandom=False

         p30=cvo.CVO().CreateCVO("$ax^2+bx+c = 0$","$2x^2+5x+47 = 0$")
         p31=cvo.CVO().CreateCVO("degree","2").setPosition([3,-2,0]).setangle(-TAU/4)
         p32=cvo.CVO().CreateCVO("constant","47").setPosition([0,2,0]).setangle(-TAU/4)
         p33=cvo.CVO().CreateCVO("roots","$1,47/2$").setPosition([3,2,0]).setangle(-TAU/4)
         p34=cvo.CVO().CreateCVO("nature of roots","imaginary roots").setPosition([-2,2,0]).setangle(-TAU/4)

        

         p30.cvolist.append(p31)
         p30.cvolist.append(p32)
         p30.cvolist.append(p33)
         p30.cvolist.append(p34)
    
        
       
       
         self.construct1(p30,p30)


    def quad1133(self):
       
    
        # Title
        title = Text("Checking if the Equation is Quadratic").scale(0.8).to_edge(UP)
        self.play(Write(title))

        # Equations
        equation = MathTex("x(2x + 3) = x^2 + 1").scale(1.2).next_to(title, DOWN, buff=0.5)
        self.play(Write(equation))

        # Explanation text
        explanation = Text("Let's simplify and check if it's quadratic...").scale(0.6).next_to(equation, DOWN, buff=0.5)
        self.play(Write(explanation))

        # Simplification steps
        steps = VGroup(
            MathTex("x(2x + 3)", "=", "x^2 + 1").scale(0.8),
            MathTex("2x^2 + 3x", "=", "x^2 + 1").scale(0.8),
            MathTex("2x^2 + 3x - x^2", "=", "1").scale(0.8),
            MathTex("x^2 + 3x", "=", "1").scale(0.8)
        ).arrange(DOWN, buff=0.3).next_to(explanation, DOWN, buff=0.5)
        
        for step in steps:
            self.play(Write(step))

        # Conclusion
        conclusion = Text("The equation is quadratic.").scale(0.8).next_to(steps, DOWN, buff=0.5)
        self.play(Write(conclusion))

        self.wait(2)



    def quad1155(self):
   
        # Title that remains visible till the end
        title = Text("Finding Roots of Equation by Factorisation", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Display the introductory text with reduced font size
        intro_text = Text("The given equation is", font_size=24)
        equation = MathTex("2x^2 + 5x - 3 = 0")
        
        # Group them together and position them side by side
        intro_group = VGroup(intro_text, equation).arrange(RIGHT, buff=0.5)
        intro_group.next_to(title, DOWN)

        self.play(Write(intro_group))
        self.wait(1)
        
        # Factorization steps
        step1 = MathTex("2x^2 + 6x - x - 3 = 0")
        step2 = MathTex("(2x^2 + 6x) + (-x - 3) = 0")
        step3 = MathTex("2x(x + 3) - 1(x + 3) = 0")
        step4 = MathTex("(2x - 1)(x + 3) = 0")
        
        steps = VGroup(step1, step2, step3, step4).arrange(DOWN, buff=0.5)
        steps.next_to(intro_group, DOWN, buff=0.5)  # Ensure no overlap with intro_text
        
        for step in steps:
            self.play(Write(step))
            self.wait(1)
        
        # Display step 5 and the concluding text on the same line
        step5 = MathTex("x = \\frac{1}{2} \\text{ or } x = -3")
        concluding_text = Text("are the roots of the given equation", font_size=24)
        
        step5_group = VGroup(step5, concluding_text).arrange(RIGHT, buff=0.5)
        step5_group.next_to(steps, DOWN, buff=0.5)

        self.play(Write(step5_group))
        self.wait(2)

        # Ensure the texts remain visible till the end
        self.wait(2)




    def quad1166(self):

      self.setNumberOfCirclePositions(7)
      self.isRandom = False

# Create circles and set their positions and angles
      p70 = cvo.CVO().CreateCVO("example", "solution of equation by completing the square").setPosition([-5, 1, 0])   
      p71 = cvo.CVO().CreateCVO("equation", "$ax^2 + bx + c = 0$").setPosition([-2, 0, 0]).setangle(-TAU / 4)
      p72 = cvo.CVO().CreateCVO("step 1", "divide each side by a").setPosition([1, 2.5, 0]).setangle(-TAU / 4)
      p73 = cvo.CVO().CreateCVO("step 2", "take c/a on RHS").setPosition([2.5, 1.5, 0]).setangle(-TAU / 4)
      p74 = cvo.CVO().CreateCVO("step 3", "$add [1/2(b/a)]^2$").setPosition([4, 0, 0]).setangle(-TAU / 6)
      p75 = cvo.CVO().CreateCVO("step 4", "square LHS and simplify RHS").setPosition([5, -1.5, 0]).setangle(-TAU / 4)
      p76 = cvo.CVO().CreateCVO("step 5", "solve").setPosition([4, -3, 0]).setangle(-TAU / 4)

# Append circles to create the hierarchy 

      p70.cvolist.append(p71)
      p71.cvolist.append(p72)
      p71.cvolist.append(p73)
      p71.cvolist.append(p74)
      p71.cvolist.append(p75)
      p71.cvolist.append(p76)

# Construct the diagram with the given layout
      self.construct1(p70, p70)

    def RenderEquality1(self):
  
        # Title
        title = Text("Example: Finding Roots by Completing the Square Method").scale(0.8).to_edge(UP, buff=0.5)
        self.play(Write(title))

        # Given quadratic equation
        equation = MathTex("4x^2 + 3x + 5 = 0").scale(1.2).move_to(LEFT * 3 + UP * 2)
        self.play(Write(equation))

        self.wait(1)

        # Step 1: Divide each term by 4
        step1_text = MathTex("x^2 + \\frac{3}{4}x + \\frac{5}{4} = 0").scale(0.8).next_to(equation, DOWN, buff=0.5).align_to(equation, LEFT)
        self.play(Write(step1_text))

        self.wait(1)

        # Step 2: Move constant term to the right side
        step2_text = MathTex("x^2 + \\frac{3}{4}x = -\\frac{5}{4}").scale(0.8).next_to(step1_text, DOWN, buff=0.5).align_to(step1_text, LEFT)
        self.play(Write(step2_text))

        self.wait(1)

        # Step 3: Complete the square on the left side
        step3_text = MathTex("x^2 + \\frac{3}{4}x + \\left(\\frac{3}{8}\\right)^2 = -\\frac{5}{4} + \\left(\\frac{3}{8}\\right)^2").scale(0.8).next_to(step2_text, DOWN, buff=0.5).align_to(step2_text, LEFT)
        self.play(Write(step3_text))

        self.wait(1)

        # Step 4: Solve for (x + 3/8)^2
        step4_text = MathTex("\\left(x + \\frac{3}{8}\\right)^2 = -\\frac{71}{64}<0").scale(0.8).next_to(step3_text, DOWN, buff=0.5).align_to(step3_text, LEFT)
        self.play(Write(step4_text))

        self.wait(1)

        # Step 5: Evaluate the discriminant
        step5_text = MathTex("\\left(x + \\frac{3}{8}\\right)^2 = -\\frac{71}{64}").scale(0.8).next_to(step4_text, DOWN, buff=0.5).align_to(step4_text, LEFT)
        self.play(Write(step5_text))

        self.wait(1)

        # Conclusion
        conclusion_text = Text("The equation has no real roots").scale(0.6).to_edge(RIGHT, buff=1).shift(DOWN)
        self.play(Write(conclusion_text))

        self.wait(2)











    def tryfile(self):
        # Title
        title = Text("Solving for the sides of a right-angled triangle").to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Define the hypotenuse and the difference in lengths of the other two sides
        hypotenuse = 25
        difference = 5

        # Create the initial text and equation
        equation_text = MathTex(
            r"\text{Let the length of the smaller side be } x \text{ cm}",
            r"\text{Then length of the longer side } = (x + 5) \text{ cm}",
            r"\text{Given length of the hypotenuse } = 25 \text{ cm}"
        ).scale(0.7).arrange(DOWN, buff=0.5).to_edge(LEFT)
        self.play(Write(equation_text))
        self.wait(1)

        # Add text to explain steps
        steps_text = MathTex(
            r"\text{In a right-angled triangle, } c^2 = a^2 + b^2",
            r"\text{So, } x^2 + (x + 5)^2 = 25^2",
            r"x^2 + x^2 + 10x + 25 = 625",
            r"2x^2 + 10x - 600 = 0",
            r"x^2 + 5x - 300 = 0"
        ).scale(0.7).arrange(DOWN, buff=0.3).next_to(equation_text, DOWN, buff=0.5).to_edge(LEFT)
        self.play(Write(steps_text))
        self.wait(2)

        # Move equation and steps up
        self.play(
            equation_text.animate.to_edge(LEFT).shift(UP),
            steps_text.animate.to_edge(LEFT).shift(UP)
        )
        
        # Create triangle figure
        A = ORIGIN
        B = RIGHT * 4
        C = ORIGIN + UP * 3
        triangle = Polygon(A, B, C, color=BLUE, fill_opacity=0.5)
        hyp_line = Line(A, B, color=RED)

        # Create side labels
        side_label_x = MathTex("x", color=WHITE).next_to(A, DOWN)
        side_label_x_plus_5 = MathTex("x + 5 \, {cm}", color=WHITE).next_to(C, LEFT)
        hyp_label = MathTex("25 \, {cm}", color=WHITE).next_to(triangle.get_center(), RIGHT, buff=0.25)
        
        # Display triangle and labels
        triangle_group = VGroup(triangle, hyp_line, side_label_x, side_label_x_plus_5, hyp_label)
        triangle_group.scale(0.9).move_to([3, 0, 0])  # Move to middle right of the page
        
        self.play(Create(triangle), Create(hyp_line))
        self.play(Write(side_label_x), Write(side_label_x_plus_5), Write(hyp_label))
        self.wait(2)
        
        # Final conclusion text
        conclusion_text = Text(
            "Value of x from the above equation\n"
            "will give the possible length\n"
            "of the sides of the triangle.\n"
        ).scale(0.6).next_to(triangle_group, DOWN, buff=0.6)
        
        self.play(Write(conclusion_text))
        self.wait(2)



    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="quadratic equations.py"

        
    def SetDeveloperList(self):  
        self.DeveloperList="Habeeb Unissa"

if __name__ == "__main__":
    scene = quadraticAnim()
    scene.render()