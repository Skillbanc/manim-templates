from manim import *
from AbstractAnim import AbstractAnim
import cvo

class Grade5Chapter13Fractions(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.Definition()
        self.fadeOutCurrentScene()
        self.Intro()
        self.fadeOutCurrentScene()
        self.add_intro()
        self.fadeOutCurrentScene()
        self.add_types_of_fractions()
        self.fadeOutCurrentScene()
        self. SimplifyingFractions()
        self.fadeOutCurrentScene()

       
        self.add_simplifying_fractions()
        self.fadeOutCurrentScene()
        
        self.add_adding_fractions()
        self.fadeOutCurrentScene()
        self.add_subtracting_fractions()
        self.fadeOutCurrentScene()
        self.add_multiplying_fractions()
        self.fadeOutCurrentScene()
        self.add_dividing_fractions()
        self.fadeOutCurrentScene()
  
        self.add_fractions_of_circles()
        self.fadeOutCurrentScene()
        self.NumberLineAnimation()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

    def Definition(self):
        p10 = cvo.CVO().CreateCVO("Fractions", "").setPosition([-3,-1,0])
        p11 = cvo.CVO().CreateCVO("Definition", "A fraction represents a part of a whole").setPosition([-3,1,0])
        p12 = cvo.CVO().CreateCVO("Fraction Form", r"$\frac{p}{q}$",).setPosition([3,1,0]).setangle(-TAU/4)
        p13 = cvo.CVO().CreateCVO("Numerator", "p").setPosition([6,-2,0]).setangle(-TAU/3)
        p14 = cvo.CVO().CreateCVO("Denominator", "q").setPosition([0,-2,0]).setangle(-TAU/3)
    
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p12.cvolist.append(p13)
        p12.cvolist.append(p14)
        self.construct1(p10, p10)
        
    def Intro(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [-TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Fractions","")
        p11=cvo.CVO().CreateCVO("TYPES Of Fractions", "")
        p11.extendOname(["PROPER","IMPROPER","MIXED"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)


    def add_intro(self):
        title = Text("Example Of Fraction").scale(1.5)
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.to_edge(UP))

       

        fraction_example = Tex(r"$\frac{3}{4}$")
        self.play(Write(fraction_example))
        self.wait(2)

        numerator = Tex(" 3 is Numerator", color=BLUE).next_to(fraction_example, UP)
        denominator = Tex(" 4 is Denominator", color=RED).next_to(fraction_example, DOWN)

        self.play(Write(numerator), Write(denominator))
        self.wait(2) 
        self.play(title.animate.to_edge(UP))

    def add_types_of_fractions(self):
        title = Text("Types of Fractions").scale(1)
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.to_edge(UP))

        # Improper Fraction
        improper = Tex(r"Improper Fraction: Numerator is greater than or equal to the denominator").shift(UP * 2).scale(0.8)
        improper_ex = Tex(r"Ex: $\frac{7}{4}$").next_to(improper, DOWN, buff=0.5).scale(0.8)  # Adjust buff for spacing
        improper[0][0:16].set_color(YELLOW)
        self.play(Write(improper))
        self.play(Write(improper_ex))
        self.wait(2)

        # Proper Fraction
        proper = Tex(r"Proper Fraction: Numerator is less than the denominator").next_to(improper_ex, DOWN, buff=0.5).scale(0.8)
        proper_ex = Tex(r"Ex: $\frac{3}{4}$").next_to(proper, DOWN, buff=0.5).scale(0.8)  # Adjust buff for spacing
        proper[0][0:14].set_color(BLUE)
        self.play(Write(proper))
        self.play(Write(proper_ex))
        self.wait(2)

        # Mixed Number
        mixed = Tex(r"Mixed Number: A whole number and a proper fraction combined").next_to(proper_ex, DOWN, buff=0.5).scale(0.8)
        mixed_ex = Tex(r"Ex: $1\frac{3}{4}$").next_to(mixed, DOWN, buff=0.5).scale(0.8)  # Adjust buff for spacing
        mixed[0][0:11].set_color(GREEN)
        self.play(Write(mixed))
        self.play(Write(mixed_ex))
        self.wait(2)
        self.play(FadeOut(improper, proper, mixed,improper_ex,proper_ex,mixed_ex))
        
    

    def SimplifyingFractions(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [-TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Simplifying Fractions","")
        p11=cvo.CVO().CreateCVO("TYPES", "")
        p11.extendOname(["By Addition","By Subtraction","By multiplication","By Division"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def add_simplifying_fractions(self):
        
        title = Text("Simplifying Fractions").scale(1.2)
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.to_edge(UP))

        # Initial fraction
        fraction = Tex(r"$\frac{8}{12}$")
        self.play(Write(fraction))
        self.wait(2)

     

        # First simplification step
        step1 = Tex(r"$\frac{8 \div 4}{12 \div 4}$").shift(DOWN * 1)
        self.play(Write(step1))
        self.wait(2)


        explanation = Text("We use 4 because it is the greatest common divisor (GCD) of 8 and 12.").scale(0.6).shift(DOWN * 2.5)
        self.play(Write(explanation))
        self.wait(3)

        # Final simplified fraction
        simplified_fraction = Tex(r"$= \frac{2}{3}$").shift(DOWN * 2)
        self.play(Write(simplified_fraction))
        self.wait(2)

        # Animate the movement of the initial fraction and the simplification steps
        self.play(
            fraction.animate.shift(UP * 1),
            step1.animate.shift(UP * 1),
            
            explanation.animate.shift(UP * 1),
            simplified_fraction.animate.shift(UP * 1)
        )
        self.wait(2)
        

    def add_adding_fractions(self):
        title = Text("Adding Fractions").scale(1.5)
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.to_edge(UP))

        # First step: Initial fractions addition
        step1 = Tex(r"$\frac{1}{4} + \frac{1}{4} = \frac{2}{4}$")
        self.play(Write(step1))
        self.wait(2)

        # Second step: Simplified fraction
        step2 = Tex(r"$= \frac{1}{2}$").next_to(step1, DOWN)
        self.play(Write(step2))
        self.wait(2)

        # Optional: Animate the movement of the steps to create more space
        self.play(
            step1.animate.shift(UP * 1),
            step2.animate.shift(UP * 1)
        )
        self.wait(2)
       

    def add_subtracting_fractions(self):
        # Create and display the title
        title = Text("Subtracting Fractions").scale(1.5)
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.to_edge(UP))

        # Display the first step of the subtraction
        step1 = Tex(r"$\frac{3}{4} - \frac{1}{4} = \frac{2}{4}$")
        self.play(Write(step1))
        self.wait(2)

        # Display the simplified result
        step2 = Tex(r"$= \frac{1}{2}$").next_to(step1, DOWN)
        self.play(Write(step2))
        self.wait(2)

        # Optional: Animate the movement of the steps to create more space
        self.play(
            step1.animate.shift(UP * 1),
            step2.animate.shift(UP * 1)
        )
        self.wait(2)

    def add_multiplying_fractions(self):
        # Create and display the title
        title = Text("Multiplying Fractions").scale(1.5)
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.to_edge(UP))

        # Display the first step of the multiplication
        step1 = Tex(r"$\frac{1}{2} \times \frac{3}{4} = \frac{1 \times 3}{2 \times 4}$")
        self.play(Write(step1))
        self.wait(2)

        # Display the simplified result
        step2 = Tex(r"$= \frac{3}{8}$").next_to(step1, DOWN)
        self.play(Write(step2))
        self.wait(2)

        # Optional: Animate the movement of the steps to create more space
        self.play(
            step1.animate.shift(UP * 1),
            step2.animate.shift(UP * 1)
        )
        self.wait(2)

    def add_dividing_fractions(self):
        # Create and display the title
        title = Text("Dividing Fractions").scale(1.5)
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.to_edge(UP))

        # Display the first step of the division
        step1 = Tex(r"$\frac{1}{2} \div \frac{3}{4} = \frac{1}{2} \times \frac{4}{3}$")
        self.play(Write(step1))
        self.wait(2)

        # Display the second step
        step2 = Tex(r"$= \frac{1 \times 4}{2 \times 3}$").next_to(step1, DOWN)
        self.play(Write(step2))
        self.wait(2)

        # Display the final simplified result
        step3 = Tex(r"$= \frac{4}{6} = \frac{2}{3}$").next_to(step2, DOWN)
        self.play(Write(step3))
        self.wait(2)

        # Optional: Animate the movement of the steps to create more space
        self.play(
            step1.animate.shift(UP * 1),
            step2.animate.shift(UP * 1),
            step3.animate.shift(UP * 1)
        )
        self.wait(2)

    def add_fractions_of_circles(self):
        # Create and display the title
        title = Text("Fractions of Circles").scale(1.5)
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.to_edge(UP))

        # Create circles and color parts of them
        circles = VGroup()
        fractions = [("1/4", 0.25), ("1/3", 0.33), ("1/2", 0.5), ("3/4", 0.75)]
        colors = [RED, GREEN, BLUE, YELLOW]
        horizontal_spacing = 2.5  # Adjust this value to control horizontal spacing

        for i, (frac, color) in enumerate(zip(fractions, colors)):
            circle = Circle(radius=1, color=WHITE).shift(UP, LEFT * (4 - i * horizontal_spacing))
            arc = AnnularSector(inner_radius=0, outer_radius=1, angle=TAU * frac[1], color=color, start_angle=0).shift(UP, LEFT * (4 - i * horizontal_spacing))
            circles.add(circle, arc)

        self.play(Create(circles))
        self.wait(1)

        # Label the fractions
        labels = VGroup(
            *[Tex(frac[0]).next_to(circle, DOWN) for frac, circle in zip(fractions, circles[::2])]
        )
        self.play(Write(labels))
        self.wait(1)

        # Determine and highlight the greatest and smallest fractions
        greatest_label = labels[3].copy().set_color(YELLOW)
        smallest_label = labels[0].copy().set_color(RED)

        self.play(Indicate(labels[3], color=YELLOW), Indicate(labels[0], color=RED))
        self.wait(1)

        greatest_text = Tex("Greatest Fraction: $\\frac{3}{4}$").shift(DOWN * 2).set_color(YELLOW)
        smallest_text = Tex("Smallest Fraction: $\\frac{1}{4}$").shift(DOWN * 3).set_color(RED)

        self.play(Write(greatest_text))
        self.wait(1)
        self.play(Write(smallest_text))
        self.wait(2)
        
    

    def NumberLineAnimation(self):
        # Create and display the title
        title = Text("Number Line Animation of 1/10").scale(1.5)
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.to_edge(UP))

        # Create the number line
        number_line = NumberLine(
            x_range=[-0.5, 0.5, 0.1],
            length=10,
            color=BLUE,
            include_numbers=True,
            label_direction=DOWN,
        )

        # Mark the fraction 1/10
        mark_position = 0.1
        mark_label = Tex(r"$\frac{1}{10}$").next_to(number_line.n2p(mark_position), UP)

        # Create a red dot at the position of 1/10
        dot = Dot(color=RED).move_to(number_line.n2p(mark_position))

        # Animation sequence
        self.play(Create(number_line))
        self.wait(1)
        self.play(Write(mark_label))
        self.wait(1)
        self.play(Create(dot))
        self.wait(2)
        
        
    def SetDeveloperList(self): 
       self.DeveloperList="Snehith Chowdary" 
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="DirectAndInverseProportion.py"

   

if __name__ == "__main__":
    scene = Grade5Chapter13Fractions() 
    scene.render() 