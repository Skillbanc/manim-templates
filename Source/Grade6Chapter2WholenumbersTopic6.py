from manim import *
from AbstractAnim import AbstractAnim
import cvo

class Grade6Chapter2WholenumbersTopic6(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        
      
    def Introduction(self):
        self.show_title()
        self.show_dot_patterns()
        self.show_rectangle_patterns()
        self.show_square_patterns()
        self.show_triangle_patterns()
        self.show_multiplication_patterns()
    

    def show_title(self):
        title = Text("Patterns in Whole Numbers", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

    def show_dot_patterns(self):
        subtitle = Text("Dot Patterns", font_size=36)
        self.play(Write(subtitle))
        self.play(subtitle.animate.to_edge(UP))

        patterns = VGroup(
            VGroup(*[Dot() for _ in range(2)]).arrange(RIGHT, buff=0.2),
            VGroup(*[Dot() for _ in range(3)]).arrange(RIGHT, buff=0.2),
            VGroup(*[Dot() for _ in range(4)]).arrange(RIGHT, buff=0.2)
        ).arrange(DOWN, buff=0.5)

        labels = VGroup(
            Text("2 dots", font_size=24),
            Text("3 dots", font_size=24),
            Text("4 dots", font_size=24)
        ).arrange(DOWN, buff=0.7)
        labels.next_to(patterns, RIGHT)

        self.play(Create(patterns), Write(labels))
        self.wait(2)
        self.play(FadeOut(VGroup(subtitle, patterns, labels)))

    def show_rectangle_patterns(self):
        subtitle = Text("Rectangle Patterns", font_size=36)
        self.play(Write(subtitle))
        self.play(subtitle.animate.to_edge(UP))

        rectangle = VGroup(*[Dot() for _ in range(6)]).arrange_in_grid(rows=2, cols=3, buff=0.2)
        label = Text("6 can be shown as 2 rows and 3 columns", font_size=24).next_to(rectangle, DOWN)

        self.play(Create(rectangle), Write(label))
        self.wait(2)
        self.play(FadeOut(VGroup(subtitle, rectangle, label)))

    def show_square_patterns(self):
        subtitle = Text("Square Patterns", font_size=36)
        self.play(Write(subtitle))
        self.play(subtitle.animate.to_edge(UP))

        squares = VGroup(
            VGroup(*[Dot() for _ in range(4)]).arrange_in_grid(rows=2, cols=2, buff=0.2),
            VGroup(*[Dot() for _ in range(9)]).arrange_in_grid(rows=3, cols=3, buff=0.2)
        ).arrange(RIGHT, buff=1)

        labels = VGroup(
            Text("2²=4", font_size=24),
            Text("3²=9", font_size=24)
        ).arrange(RIGHT, buff=1.5)
        labels.next_to(squares, DOWN)

        self.play(Create(squares), Write(labels))
        self.wait(2)
        self.play(FadeOut(VGroup(subtitle, squares, labels)))

    def show_triangle_patterns(self):
        subtitle = Text("Triangle Patterns", font_size=36)
        self.play(Write(subtitle))
        self.play(subtitle.animate.to_edge(UP))

        def create_triangle(n):
            dots = VGroup(*[Dot() for _ in range(sum(range(1, n+1)))])
            for i in range(n):
                dots[sum(range(i)):sum(range(i+1))].arrange(RIGHT, buff=0.2)
                dots[sum(range(i)):sum(range(i+1))].shift(DOWN * i * 0.3 + LEFT * i * 0.1)
            return dots

        triangles = VGroup(*[create_triangle(i) for i in range(1, 5)]).arrange(RIGHT, buff=1)
        labels = VGroup(*[Text(f"T{i}", font_size=24) for i in range(1, 5)]).arrange(RIGHT, buff=1.2)
        labels.next_to(triangles, DOWN)

        self.play(Create(triangles), Write(labels))
        self.wait(2)
        self.play(FadeOut(VGroup(subtitle, triangles, labels)))

    

    def show_multiplication_patterns(self):
        subtitle = Text("Multiplication Patterns", font_size=36)
        self.play(Write(subtitle))
        self.play(subtitle.animate.to_edge(UP))

        patterns = VGroup(
            Text("256 × 9 = 256 × 10 - 256 = 2560 - 256 = 2304", font_size=24),
            Text("256 × 99 = 256 × 100 - 256 = 25600 - 256 = 25344", font_size=24),
            Text("256 × 999 = 256 × 1000 - 256 = 256000 - 256 = 255744", font_size=24)
        ).arrange(DOWN, buff=0.5)

        self.play(Write(patterns))
        self.wait(2)
        self.play(FadeOut(VGroup(subtitle, patterns)))

    def SetDeveloperList(self): 
       self.DeveloperList="Medha Masanam" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade6Chapter2WholenumbersTopic6.py"

if __name__ == "__main__":
    scene = Grade6Chapter2WholenumbersTopic6()
    scene.render()