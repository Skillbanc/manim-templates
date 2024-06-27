from manim import *
from AbstractAnim import AbstractAnim
import cvo

class Realnumbersanim(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction1()
        self.fadeOutCurrentScene()
        self.Naturalnumbers()
        self.fadeOutCurrentScene()
        self.Wholenumbers()
        self.fadeOutCurrentScene()
        self.Integers()
        self.fadeOutCurrentScene()
        self.Rationalnumbers()
        self.fadeOutCurrentScene()
        self.rationalising()
        self.fadeOutCurrentScene()
        self.IrrationalNumbers()
        self.fadeOutCurrentScene()
        self.LawsOfExponents()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

    def Introduction1(self):
        self.setNumberOfCirclePositions(2)
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Numbers","")
        p11 = cvo.CVO().CreateCVO("Types of numbers", "")
        p11.extendOname(["Natural numbers", "Whole numbers", "Integers", "Rational numbers","Irrational numbers"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10, p10)


    def Naturalnumbers(self):
        self.setNumberOfCirclePositions(2)
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Numbers", "")
        p11 = cvo.CVO().CreateCVO("Natural numbers", "$1, 2, 3, \\ldots, \\infty$")
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10, p10)
        self.fadeOutCurrentScene()

        title = Text("Natural Numbers (N)").to_edge(UP)
        description = Text("All positive numbers starting from 1 ", font_size=24).next_to(title, DOWN)

        self.play(Write(title), Write(description))

        number_line = NumberLine(
            x_range=[1, 11, 1],  # x_range=[start, end, step]
            length=10,  # length of the number line
            color=BLUE,  # color of the number line
            include_numbers=True,  # include numbers on the line
            label_direction=UP,  # position of the labels
        )

        self.play(Create(number_line))
        self.wait(3)

    def Wholenumbers(self):
        self.setNumberOfCirclePositions(2)
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Numbers","")
        p11 = cvo.CVO().CreateCVO("Whole  numbers", "$0,1,2,3, \\ldots, \\infty$")
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10, p10)
        self.fadeOutCurrentScene()


        title = Text("Whole Numbers(W)").to_edge(UP)
        description = Text("0 and all the natural numbers", font_size=24).next_to(title, DOWN)

        self.play(Write(title), Write(description))

        number_line = NumberLine(
            x_range=[0, 10, 1],  
            length=10,  
            color=BLUE, 
            include_numbers=True,
            label_direction=UP,  
        )

        self.play(Create(number_line))
        self.wait(3) 

    def Integers(self):
        self.setNumberOfCirclePositions(2)
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Numbers","")
        p11 = cvo.CVO().CreateCVO("Integers", "$-\\infty,\\ldots,-3,-2,-1,0,1,2,3,\\ldots, \\infty$")
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10, p10)
        self.fadeOutCurrentScene()
        title = Text("Integers(Z)").to_edge(UP)
        description = Text("All positive and negative numbers", font_size=24).next_to(title, DOWN)

        self.play(Write(title), Write(description))

        number_line = NumberLine(
            x_range=[-5, 5, 1],  
            length=10, 
            color=BLUE,  
            include_numbers=True,  
            label_direction=UP,  
        )

        self.play(Create(number_line))
        self.wait(3) 


    def Rationalnumbers(self):
        self.positionChoice=[[-4,0,0],[0,0,0],[4,0,0]]        
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Numbers","")
        p11 = cvo.CVO().CreateCVO("Rational numbers", "")
        p12 = cvo.CVO().CreateCVO("Properties", "")
        p12.extendOname(["Expressed in p/q form","$q\\neq0$","numerator =integer","denominator=integer","Is repeating"])
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        self.construct1(p10, p10)
        self.fadeOutCurrentScene()

        title = Text("Representing 3/4").to_edge(UP)
        self.play(Write(title))

        # Circle representation
        circle = Circle(radius=2, color=BLUE)
        self.play(Create(circle))

        # Add segments to the circle
        circle_segments = VGroup(
            Sector(inner_radius=0, outer_radius=2, angle=PI/2, start_angle=0, color=ORANGE).set_fill(ORANGE, opacity=0.5),
            Sector(inner_radius=0, outer_radius=2, angle=PI/2, start_angle=PI/2, color=ORANGE).set_fill(ORANGE, opacity=0.5),
            Sector(inner_radius=0, outer_radius=2, angle=PI/2, start_angle=PI, color=ORANGE).set_fill(ORANGE, opacity=0.5),
            Sector(inner_radius=0, outer_radius=2, angle=PI/2, start_angle=3*PI/2, color=WHITE).set_fill(WHITE, opacity=0.5),
        )

        # Create the circle segments
        self.play(*[Create(segment) for segment in circle_segments])
        circle_label1 = MathTex(r"\frac{3}{4}",color=ORANGE).next_to(circle, LEFT, buff=0.5)
        circle_label2 = MathTex(r"\frac{1}{4}",color=WHITE).next_to(circle, RIGHT, buff=0.5)
        self.play(Write(circle_label1),Write(circle_label2))

        self.fadeOutCurrentScene()

        title = Text("Rational Numbers").to_edge(UP)
        description = Text("Any number that can be expressed in the form p/q where q ≠ 0", font_size=24).next_to(title, DOWN)

        self.play(Write(title), Write(description))

        number_line = NumberLine(
            x_range=[-0.5, 0.5, 0.1],  
            length=10, 
            color=BLUE,  
            include_numbers=True,  
            label_direction=UP,  
        )
        self.play(Create(number_line))

        rational_numbers = [
            (-0.5, r"-\frac{5}{10}"),
            (-0.4, r"-\frac{4}{10}"),
            (-0.3, r"-\frac{3}{10}"),
            (-0.2, r"-\frac{2}{10}"),
            (-0.1, r"-\frac{1}{10}"),            
            (0, r"\frac{0}{1}"),
            (0.1, r"\frac{1}{10}"),
            (0.2, r"\frac{2}{10}"),
            (0.3, r"\frac{3}{10}"),
            (0.4, r"\frac{4}{10}"),
            (0.5, r"\frac{5}{10}"),
        ]
        for num, label in rational_numbers:
            dot = Dot(point=number_line.number_to_point(num), color=RED)
            label_tex = MathTex(label, font_size=24).next_to(dot, DOWN)
            self.play(FadeIn(dot), Write(label_tex), run_time=0.5)

        self.wait(3)
        self.fadeOutCurrentScene()
        title = MathTex(r"\text{Properties of Square Roots}").to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Define the properties
        properties = [
            r"\text{(i)} \quad \sqrt{a \cdot b} = \sqrt{a} \cdot \sqrt{b}",
            r"\text{(ii)} \quad \sqrt{\frac{a}{b}} = \frac{\sqrt{a}}{\sqrt{b}}, \quad \text{if } b \neq 0",
            r"\text{(iii)} \quad \sqrt{(a + b)(a - b)} = \sqrt{a^2 - b^2}",
            r"\text{(iv)} \quad \sqrt{(a + b)^2} = |a + b|",
            r"\text{(v)} \quad \sqrt{(a + b + c + d)^2} = a + b + c + d",
            r"\text{(vi)} \quad \sqrt{a + 2\sqrt{ab} + b} = \sqrt{a} + \sqrt{b}",
            r"\text{(vii)} \quad \sqrt{a} + \sqrt{b} = \sqrt{a + b + 2\sqrt{ab}}"
        ]

        # Create a VGroup to hold the properties
        props = VGroup(*[MathTex(prop, font_size=24) for prop in properties]).arrange(DOWN, aligned_edge=LEFT).next_to(title, DOWN)

        # Animate each property sequentially
        for prop in props:
            self.play(Write(prop))
            self.wait(4)

    def rationalising(self):
        title = Text("Rationalizing the Denominator", font_size=36).to_edge(UP)
        description = Text("To rationalise we need to multiply and divide the denominator ", font_size=24).next_to(title, DOWN)

        self.play(Write(title), Write(description))


        example = MathTex(r"\frac{1}{\sqrt{2}} \times \frac{\sqrt{2}}{\sqrt{2}} = \frac{\sqrt{2}}{2}").scale(1.5)

        self.play(Write(example))
        self.wait(3)

    def IrrationalNumbers(self):
        self.positionChoice=[[-4,0,0],[0,0,0],[4,0,0]]        
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Numbers","")
        p11 = cvo.CVO().CreateCVO("Irrational", "")
        p12 = cvo.CVO().CreateCVO("Properties", "")
        p12.extendOname(["Cannot expressed in p/q form","$q\\neq0$","numerator =integer","denominator=integer","Is not repeating"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        self.construct1(p10, p10)
        self.fadeOutCurrentScene()
        title = Text("Irrational Numbers on a Number Line",font_size= 36).to_edge(UP)
        description = Text("Any number that cannot be expressed in the form p/q where q ≠ 0", font_size=24).next_to(title, DOWN)
        
        self.play(Write(title), Write(description))

        number_line = NumberLine(
            x_range=[-1, 4, 1],  
            length=10,  
            color=BLUE,  
            include_numbers=True,  
            label_direction=UP, 
        )
        self.play(Create(number_line))

        irrationals = [
            (np.sqrt(2), r"\sqrt{2}"),
            (np.pi, r"\pi"),
            (np.e, r"e"),
        ]

        for value, label in irrationals:
            dot = Dot(point=number_line.number_to_point(value), color=RED)
            label_tex = MathTex(label).next_to(dot, UP)
            self.play(FadeIn(dot), Write(label_tex), run_time=0.5)

        self.wait(3) 
        self.fadeOutCurrentScene()
        title = MathTex("\\text {Locating} \\sqrt{2} \\text{ on the Number Line}").to_edge(UP)
        self.play(Write(title))

        # Number Line
        number_line = NumberLine(
            x_range=[-1,2,1],
            length=4,
            color=BLUE,
            include_numbers=True,
            label_direction=DOWN,
        )
        number_line.move_to(LEFT*3)
        self.play(Create(number_line))

        # Unit Square
        O = Dot(number_line.number_to_point(0), color=RED)
        A = Dot(number_line.number_to_point(1), color=RED)
        C = Dot(O.get_center() + UP, color=RED)
        B = Dot(A.get_center() + UP, color=RED)
        unit_square = Polygon(A.get_center(), B.get_center(), C.get_center(), O.get_center())
        unit_square.set_fill(TEAL, opacity=0.5)
        
        self.play(Create(unit_square))
        self.play(Create(O), Create(B), Create(A), Create(C))

        # Labels for square vertices
        label_o = MathTex("O").next_to(O, DL)
        label_c = MathTex("C").next_to(C, UL)
        label_b = MathTex("B").next_to(B, UR)
        label_a = MathTex("A").next_to(A, DR)
        self.play(Write(label_o), Write(label_a), Write(label_b), Write(label_c))

        # Hypotenuse OB
        hypotenuse = Line(O.get_center(), B.get_center(), color=YELLOW)
        self.play(Create(hypotenuse))

        # Distance OB label directly on hypotenuse
        ob_length = MathTex("\\sqrt{2}")
        ob_length.move_to(hypotenuse.get_center())
        self.play(Write(ob_length))

        # Arc from O to sqrt(2)
        arc = Arc(
            radius=hypotenuse.get_length(),
            start_angle=PI / 2,
            angle=-PI / 2,
            arc_center=O.get_center(),
            color=GREEN,
        )
        self.play(Create(arc))

        # Point on number line
        #sqrt2_point = Dot(number_line.number_to_point(np.sqrt(2)), color=YELLOW)
        #sqrt2_label = MathTex("\\sqrt{2}").next_to(sqrt2_point, DOWN)
        #self.play(Create(sqrt2_point), Write(sqrt2_label))

        # Explanation of Pythagorean Theorem
        explanation_text = VGroup(
            MathTex("Using\\ Pythagorean\\ Theorem:").set_color(YELLOW),
            MathTex("OB^2 = OA^2 + AB^2").set_color(WHITE),
            MathTex("\\Rightarrow 1^2 + 1^2").set_color(WHITE),
            MathTex("OB^2 \\Rightarrow 2").set_color(WHITE),
            MathTex("OB = \\sqrt{2}").set_color(WHITE)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(number_line, RIGHT)
        self.play(Write(explanation_text))

        self.wait(3)

        # Fade out current scene and show steps
        self.fadeOutCurrentScene()
        title = MathTex("\\text{Steps to locate} \\sqrt{2} \\text{ on the Number Line}").to_edge(UP)
        self.play(Write(title))
        Steps = [
            r"\text{1. Draw a unit square } OABC \text{ with side length 1 starting from 0 on the number line.}",
            r"\text{2. Draw the diagonal } OB \text{ of the square.}",
            r"\text{3. By the Pythagorean theorem, the length of } OB \text{ is } \sqrt{2}.",
            r"\text{4. Draw an arc with radius } OB \text{ centered at } O \text{.}",
            r"\text{5. The intersection of the arc with the number line gives the point } \sqrt{2}."
        ]
        Steps = VGroup(*[MathTex(text, font_size=30) for text in Steps]).arrange(DOWN, aligned_edge=LEFT).next_to(title, DOWN)
        self.play(Write(Steps))

        self.wait(3)
        self.fadeOutCurrentScene()

    def LawsOfExponents(self):
        self.positionChoice=[[-4,0,0],[4,2,0],[2,2,0],[2,-2,0],[4,-2,0],[4,0,0]]        
        self.isRandom = False
        self.angleChoice = [TAU/4,TAU/4,TAU/4,TAU/4,TAU/4]


        p10 = cvo.CVO().CreateCVO("Laws of Exponents", "Properties")
        p11 = cvo.CVO().CreateCVO("Property", "$a^m \\cdot a^n = a^{m+n}$")
        p12 = cvo.CVO().CreateCVO("Property", "$(a^m)^n = a^{mn}$")
        p13 = cvo.CVO().CreateCVO("Property", "$a^0 = 1$")
        p14 = cvo.CVO().CreateCVO("Property", "$a^{-n} = \\frac{1}{a^n}$")
        p15 = cvo.CVO().CreateCVO("Property", "$\\frac{a^m}{a^n} = a^{m-n}$")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        self.construct1(p10, p10)
        self.fadeOutCurrentScene()
        
        title = Text("Exponentials").to_edge(UP)
        self.play(Write(title))

        examples = [
            r"a^m \cdot a^n = a^{m+n} \quad \text{example:} \quad 2^3 \cdot 2^4 = 2^{3+4} = 2^7 = 128",
            r"\frac{a^m}{a^n} = a^{m-n} \quad \text{example:} \frac{2^5}{2^2} = 2^{5-2} = 2^3 = 8",
            r"(a^m)^n = a^{m \cdot n} \quad \text{example:} (2^3)^2 = 2^{3 \cdot 2} = 2^6 = 64",
            r"a^{-n} = \frac{1}{a^n} \quad \text{example:}2^{-3} = \frac{1}{2^3} = \frac{1}{8}",
            r"a^0 = 1 \quad \text{example:} 2^0 = 1",
        ]

        # Create and position each example individually
        example1 = MathTex(examples[0]).scale(0.8).next_to(title, DOWN, buff=1)
        example2 = MathTex(examples[1]).scale(0.8).next_to(example1, DOWN, aligned_edge=LEFT, buff=0.5)
        example3 = MathTex(examples[2]).scale(0.8).next_to(example2, DOWN, aligned_edge=LEFT, buff=0.5)
        example4 = MathTex(examples[3]).scale(0.8).next_to(example3, DOWN, aligned_edge=LEFT, buff=0.5)
        example5 = MathTex(examples[4]).scale(0.8).next_to(example4, DOWN, aligned_edge=LEFT, buff=0.5)


        self.play(Write(example1),Write(example2),Write(example3),Write(example4),Write(example5))
        
        self.wait(5)

    def SetDeveloperList(self):  
        self.DeveloperList="Shanmukha Priya"
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade9Chapter1RealNumbers.py"


if __name__ == "__main__":
    scene = Realnumbersanim()
    scene.render()