from manim import *
from AbstractAnim import AbstractAnim
import cvo

class UsingAdditionsandSubtractions(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.subtraction()
        self.fadeOutCurrentScene()
        self.addition()
        self.fadeOutCurrentScene()
        self.Anim()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

    def subtraction(self):
        self.setNumberOfCirclePositions(2)
        self.isRandom = False
        p10 = cvo.CVO().CreateCVO("Subtraction", "")
        p11 = cvo.CVO().CreateCVO("Symbol", "minus (-)")       
        p10.cvolist.append(p11)   
        self.construct1(p10, p10)
        self.fadeOutCurrentScene()
  
    def addition(self):
        self.setNumberOfCirclePositions(2)
        self.isRandom = False
        p10 = cvo.CVO().CreateCVO("Addition", "")
        p11 = cvo.CVO().CreateCVO("Symbol", "plus (+)")       
        p10.cvolist.append(p11)   
        self.construct1(p10, p10)
        self.fadeOutCurrentScene()

    def Anim(self):

        def create_box_with_symbols(circle_color, num_symbols, number, position):
            box = Square(side_length=2, color=WHITE)
            symbols = VGroup(*[Circle(radius=0.2, color=circle_color) for _ in range(num_symbols)]).arrange_in_grid(rows=2, buff=0.1)
            symbols.move_to(box.get_center())
            number_text = Text(str(number), font_size=36).next_to(box, DOWN)
            group = VGroup(box, symbols, number_text).move_to(position)
            return group

        # Addition Animation
        addition_text = Title("ADDITION", color=RED)
        self.play(Write(addition_text))
        self.wait(1)

        # Create boxes with symbols representing numbers
        box1_group = create_box_with_symbols(GREEN, 3, 3, LEFT)
        self.play(Create(box1_group))

        plus_sign = Text("+", font_size=48)
        self.play(Write(plus_sign.next_to(box1_group, RIGHT, buff=0.5)))

        box2_group = create_box_with_symbols(ORANGE, 5, 5, plus_sign.get_right() + RIGHT)
        self.play(Create(box2_group))

        equals_sign = Text("=", font_size=48)
        self.play(Write(equals_sign.next_to(box2_group, RIGHT, buff=0.5)))

        result_group = create_box_with_symbols(BLUE, 8, 8, equals_sign.get_right() + RIGHT)
        self.play(Create(result_group))
        self.wait(4)

        self.play(FadeOut(VGroup(box1_group, plus_sign, box2_group, equals_sign, result_group)))
        self.play(FadeOut(addition_text))

        # Subtraction Animation
        subtraction_text = Title("SUBTRACTION", color=RED)
        self.play(Write(subtraction_text))
        self.wait(1)

        # Create boxes with symbols representing numbers for subtraction
        box3_group = create_box_with_symbols(BLUE, 8, 8, LEFT)
        self.play(Create(box3_group))

        minus_sign = Text("-", font_size=48)
        self.play(Write(minus_sign.next_to(box3_group, RIGHT, buff=0.5)))

        box4_group = create_box_with_symbols(ORANGE, 5, 5, minus_sign.get_right() + RIGHT)
        self.play(Create(box4_group))

        equals_sign = Text("=", font_size=48)
        self.play(Write(equals_sign.next_to(box4_group, RIGHT, buff=0.5)))

        result_group2 = create_box_with_symbols(GREEN, 3, 3, equals_sign.get_right() + RIGHT)
        self.play(Create(result_group2))
        self.wait(4)

        self.play(FadeOut(VGroup(box3_group, minus_sign, box4_group, equals_sign, result_group2)))
        self.play(FadeOut(subtraction_text))
  

    def SetDeveloperList(self):  
        self.DeveloperList="Gayathri Veeramreddy"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade3Chapter5UsingAdditionsandSubtractions.py"

 

if __name__ == "__main__":
    scene = UsingAdditionsandSubtractions()
    scene.render()
