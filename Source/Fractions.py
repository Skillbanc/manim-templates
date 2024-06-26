from manim import *
from AbstractAnim import AbstractAnim
import cvo

class FractionsChapter(AbstractAnim):
    def construct(self):
        self.add_intro()
        self.fadeOutCurrentScene()
        self.add_types_of_fractions()
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

    def add_intro(self):
        title = Text("Introduction to Fractions").scale(1.5)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        intro_text = Text("""
        A fraction represents a part of a whole.
        It consists of a numerator and a denominator.
        """)
        self.play(Write(intro_text, run_time=4))
        self.wait(2)
        self.play(FadeOut(intro_text))

        fraction_example = Tex(r"$\frac{3}{4}$")
        self.play(Write(fraction_example))
        self.wait(2)

        numerator = Tex("Numerator", color=BLUE).next_to(fraction_example, UP)
        denominator = Tex("Denominator", color=RED).next_to(fraction_example, DOWN)

        self.play(Write(numerator), Write(denominator))
        self.wait(2)
        self.play(FadeOut(fraction_example, numerator, denominator))

    def add_types_of_fractions(self):
        title = Text("Types of Fractions").scale(1.5)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        improper = Tex(r"Improper Fraction: $\frac{7}{4}$").shift(UP * 2)
        proper = Tex(r"Proper Fraction: $\frac{3}{4}$").shift(UP * 1)
        mixed = Tex(r"Mixed Number: $1\frac{3}{4}$").shift(UP * 0)

        self.play(Write(improper))
        self.wait(1)
        self.play(Write(proper))
        self.wait(1)
        self.play(Write(mixed))
        self.wait(2)
        self.play(FadeOut(improper, proper, mixed))

    def add_simplifying_fractions(self):
        title = Text("Simplifying Fractions").scale(1.5)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        fraction = Tex(r"$\frac{8}{12}$")
        self.play(Write(fraction))
        self.wait(2)

        simplification_steps = VGroup(
            Tex(r"$\frac{8 \div 4}{12 \div 4}$").shift(DOWN * 1),
            Tex(r"$\frac{2}{3}$").shift(DOWN * 2)
        )

        self.play(Transform(fraction, simplification_steps[0]))
        self.wait(2)
        self.play(Transform(fraction, simplification_steps[1]))
        self.wait(2)
        self.play(FadeOut(fraction))

    def add_adding_fractions(self):
        title = Text("Adding Fractions").scale(1.5)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        fractions = VGroup(
            Tex(r"$\frac{1}{4} + \frac{1}{4} = \frac{2}{4}$"),
            Tex(r"$= \frac{1}{2}$").shift(DOWN * 1)
        ).arrange(DOWN)

        self.play(Write(fractions[0]))
        self.wait(2)
        self.play(Transform(fractions[0], fractions[1]))
        self.wait(2)
        self.play(FadeOut(fractions))

    def add_subtracting_fractions(self):
        title = Text("Subtracting Fractions").scale(1.5)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        fractions = VGroup(
            Tex(r"$\frac{3}{4} - \frac{1}{4} = \frac{2}{4}$"),
            Tex(r"$= \frac{1}{2}$").shift(DOWN * 1)
        ).arrange(DOWN)

        self.play(Write(fractions[0]))
        self.wait(2)
        self.play(Transform(fractions[0], fractions[1]))
        self.wait(2)
        self.play(FadeOut(fractions))

    def add_multiplying_fractions(self):
        title = Text("Multiplying Fractions").scale(1.5)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        fractions = VGroup(
            Tex(r"$\frac{1}{2} \times \frac{3}{4} = \frac{1 \times 3}{2 \times 4}$"),
            Tex(r"$= \frac{3}{8}$").shift(DOWN * 1)
        ).arrange(DOWN)

        self.play(Write(fractions[0]))
        self.wait(2)
        self.play(Transform(fractions[0], fractions[1]))
        self.wait(2)
        self.play(FadeOut(fractions))

    def add_dividing_fractions(self):
        title = Text("Dividing Fractions").scale(1.5)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        fractions = VGroup(
            Tex(r"$\frac{1}{2} \div \frac{3}{4} = \frac{1}{2} \times \frac{4}{3}$"),
            Tex(r"$= \frac{1 \times 4}{2 \times 3}$").shift(DOWN * 1),
            Tex(r"$= \frac{4}{6} = \frac{2}{3}$").shift(DOWN * 2)
        ).arrange(DOWN)

        self.play(Write(fractions[0]))
        self.wait(2)
        self.play(Write(fractions[1]))
        self.wait(2)
        self.play(Transform(fractions[1], fractions[2]))
        self.wait(2)
        self.play(FadeOut(fractions))

    def add_fractions_of_circles(self):
        title = Text("Fractions of Circles").scale(1.5)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Create circles and color parts of them
        circles = VGroup()
        fractions = [("1/4", 0.25), ("1/3", 0.33), ("1/2", 0.5), ("3/4", 0.75)]
        colors = [RED, GREEN, BLUE, YELLOW]

        for i, (frac, color) in enumerate(zip(fractions, colors)):
            circle = Circle(radius=1, color=WHITE).shift(UP , LEFT * (4 - i * 2))
            arc = AnnularSector(inner_radius=0, outer_radius=1, angle=TAU * frac[1], color=color, start_angle=0).shift(UP , LEFT * (4 - i * 2))
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

        # Animation sequence
        self.play(Create(number_line))
        self.wait(1)
        self.play(Write(mark_label))
        self.wait(2)
        
        
    def SetDeveloperList(self): 
       self.DeveloperList="Snehith" 
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="DirectAndInverseProportion.py"

   

if __name__ == "__main__":
    scene = FractionsChapter()
    scene.render()
