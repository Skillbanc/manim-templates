import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class FactorsAnim(AbstractAnim):

    
    def construct(self):
        # self.RenderSkillbancLogo()
        # self.Factors()
        # self.Important()
        # self.Multiples()
        # self.Multiples1()
        self.Multiple()
        # self.Important1()
        # self.Example()
        # self.GithubSourceCodeReference() 

    def Factors(self):
        
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Factors and Multiples", "").setPosition([-4,0,0])
        p11=cvo.CVO().CreateCVO("Multiples", "").setPosition([0,2,0]).setangle(-TAU/4)
        
        p12=cvo.CVO().CreateCVO("Factors", "").setPosition([0,-2,0]).setangle(-TAU/4)
        
        
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        
        

        

        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
    
    def Important(self):
        
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Multiples", "").setPosition([-3,0,0])
        p11=cvo.CVO().CreateCVO("Definition","Numbers you get when you multiply a certain number by an integer.").setPosition([2,2,0]).setangle(-TAU/4)
        
        
       
        
        p10.cvolist.append(p11)
        

        p11.setcircleradius(1.5)
        

        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Multiples(self):
       
        title = Text("Multiples of 2", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Introduction
        intro_text = Text("Numbers that are divisible by 2.",font_size=30, color=BLUE)
        intro_text.next_to(title, DOWN)
        self.play(FadeIn(intro_text))
        self.wait(2)
        self.play(FadeOut(intro_text))

        # Show multiples
        multiples = [2, 4, 6, 8, 10, 12]
        circles = VGroup()

        for i, num in enumerate(multiples):
            circle = Circle(radius=0.5, color=BLUE)
            circle.move_to(2 * RIGHT * i + LEFT * 6)
            number = Text(str(num), font_size=24)
            number.move_to(circle.get_center())
            self.play(FadeIn(circle), Write(number))
            circles.add(circle, number)
            self.wait(0.5)

        # Patterns in multiples
        pattern_text = Text("Multiples of 2 end in 0, 2, 4, 6, or 8.", font_size=24)
        pattern_text.next_to(circles, DOWN)
        self.play(Write(pattern_text))
        self.wait(2)
        self.play(FadeOut(pattern_text), FadeOut(circles))
        self.fadeOutCurrentScene()

    def Multiples1(self):

         # Title
        title = Text("Example : First 6 Multiples of 3", font_size=40, color=BLUE).to_edge(UP)
        self.play(Write(title))

        # Multiplication animations
        equations = []
        for i in range(1, 7):  # 1 to 6
            multiple = 3 * i
            equation = MathTex(f"3 \\times {i} = {multiple}").to_edge(UP).shift(1 * i * DOWN)
            equations.append(equation)

        # Animation
        for equation in equations:
            self.play(Write(equation))
            self.wait(1)

        self.wait(2)
        self.fadeOutCurrentScene()

    def Multiple(self):

        title = Text("Common Multiples", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))

        # Venn Diagram circles
        red_circle = Circle(radius=2, color=RED, fill_opacity=0.5)
        blue_circle = Circle(radius=2, color=BLUE, fill_opacity=0.5)
        yellow_circle = Circle(radius=2, color=YELLOW, fill_opacity=0.5)

        red_circle.shift(LEFT * 2 + DOWN)
        blue_circle.shift(RIGHT * 2 + DOWN)
        yellow_circle.shift(DOWN)

        self.play(FadeIn(red_circle), FadeIn(blue_circle), FadeIn(yellow_circle))

        # Labels for the circles
        red_label = Text("Multiples of 3", font_size=20, color=RED)
        blue_label = Text("Multiples of 5", font_size=20, color=BLUE)
        yellow_label = Text("Common Multiples", font_size=20, color=YELLOW)

        red_label.next_to(red_circle, DOWN)
        blue_label.next_to(blue_circle, DOWN)
        yellow_label.next_to(yellow_circle, UP)

        self.play(Write(red_label), Write(blue_label), Write(yellow_label))

        # Multiples lists
        multiples_of_3 = [3, 6, 9, 12, 18]
        multiples_of_5 = [5, 10, 20, 25]
        common_multiples = [15, 30]

        # Function to place numbers in the circles
        def place_numbers(multiples, circle, color, position_offset=ORIGIN):
          for i, num in enumerate(multiples):
           num_text = Text(str(num), font_size=24, color=color)
           angle = np.pi  # 180 degrees (left side)
           radius = circle.radius * 0.7
           num_text.move_to(circle.get_center() + radius * np.array([np.cos(angle), np.sin(angle), 0]) + position_offset)
           self.play(FadeIn(num_text))

        # Place multiples of 3 in the red circle
        place_numbers(multiples_of_3, red_circle, WHITE)
        
        # Place multiples of 5 in the blue circle
        place_numbers(multiples_of_5, blue_circle, WHITE)
        
        # Place common multiples (15 and 30) in the yellow circle
        place_numbers(common_multiples, yellow_circle, WHITE, position_offset=0.5*UP)

        self.wait(2)
        self.fadeOutCurrentScene()

    def Important1(self):
        
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Factors", "").setPosition([-3,0,0])
        p11=cvo.CVO().CreateCVO("Definition", "Numbers that divide a certain number without leaving a remainder").setPosition([1,2,0]).setangle(-TAU/4)
        
        
       
        
        p10.cvolist.append(p11)
        

        p11.setcircleradius(1.5)
        
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()


    def Example(self):
    
        title = Text("Factors of 12", font_size=48,color=YELLOW).to_edge(UP)
        self.play(Write(title))

        # Introduction
        intro_text = Text("Let's find the factors of 12!", font_size=36)
        self.play(Write(intro_text))
        self.wait(2)
        self.play(FadeOut(intro_text))

        # Dots for Number 12
        num_dots = 12
        dots = VGroup(*[Dot() for _ in range(num_dots)]).arrange_in_grid(rows=1, cols=num_dots, buff=0.2)
        self.play(FadeIn(dots))
        self.wait(1)

        # Grouping by Factors
        factor_groups = [
            (1, 12), # 1 x 12
            (2, 6),  # 2 x 6
            (3, 4),  # 3 x 4
            (4, 3),  # 4 x 3
            (6, 2),  # 6 x 2
            (12, 1)  # 12 x 1
        ]
        
        group_texts = [
            "1 x 12",
            "2 x 6",
            "3 x 4",
            "4 x 3",
            "6 x 2",
            "12 x 1"
        ]

        for i, (rows, cols) in enumerate(factor_groups):
            # Create grid for each factor group
            factor_group = VGroup(*[Dot() for _ in range(num_dots)]).arrange_in_grid(rows=rows, cols=cols, buff=0.2)
            factor_group.shift(DOWN * 1.5)

            # Display factor text
            factor_text = Text(group_texts[i], font_size=26)
            factor_text.next_to(factor_group, UP*2)

            self.play(Transform(dots, factor_group), Write(factor_text))
            self.wait(1.5)
            self.play(FadeOut(factor_text))
            self.remove(dots)
        

        # Conclusion
        conclusion_text = Text("1, 2, 3, 4, 6, 12 are all the factors of 12!", font_size=36)
        self.play(Write(conclusion_text))
        self.wait(2)
        self.play(FadeOut(conclusion_text))

        self.fadeOutCurrentScene()

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade5CHpater14FactorsandMultiples.py"

    def SetDeveloperList(self):  
        self.DeveloperList="Lagichetty Kushal"
    
if __name__ == "__main__":
    scene = FactorsAnim()
    scene.render()