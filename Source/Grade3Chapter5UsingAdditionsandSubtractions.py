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
        self.missingnums()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

    def subtraction(self):
        self.setNumberOfCirclePositions(3)
        self.isRandom = False
        p10 = cvo.CVO().CreateCVO("Subtraction", "")
        p11 = cvo.CVO().CreateCVO("Symbol", "minus (-)")  
        p12 = cvo.CVO().CreateCVO("Representation", "9 - 5 = 4") 
        p10.setcircleradius(1.5)
        p11.setcircleradius(1.5)
        p12.setcircleradius(1.5)
        p10.cvolist.append(p11) 
        p10.cvolist.append(p12)  
        self.construct1(p10, p10)
        self.fadeOutCurrentScene()
  
    def addition(self):
        self.setNumberOfCirclePositions(3)
        self.isRandom = False
        p10 = cvo.CVO().CreateCVO("Addition", "")
        p11 = cvo.CVO().CreateCVO("Symbol", "plus (+)")       
        p12 = cvo.CVO().CreateCVO("Representation", "9 + 5 = 14") 
        p10.setcircleradius(1.5)
        p11.setcircleradius(1.5)
        p12.setcircleradius(1.5)
        p10.cvolist.append(p11) 
        p10.cvolist.append(p12)  
        self.construct1(p10, p10)
        self.fadeOutCurrentScene()
  

    def Anim(self):

        def create_box_with_symbols(symbol, num_symbols, number, position):
           box = Square(side_length=2, color=WHITE)
           symbols = VGroup(*[Text(symbol, font_size=24) for _ in range(num_symbols)]).arrange_in_grid(rows=2, buff=0.1)
           symbols.move_to(box.get_center())
           number_text = Text(str(number), font_size=36).next_to(box, DOWN)
           group = VGroup(box, symbols, number_text).move_to(position)
           return group

    # Addition Animation
        addition_text = Title("ADDITION", color=RED).to_edge(UP)
        self.play(Write(addition_text))
        self.wait(1)

    # Create boxes with symbols representing numbers
        box1_group = create_box_with_symbols("🍭", 3, 3, ORIGIN + LEFT * 3)
        self.play(Create(box1_group))
    
        plus_sign = Text("+", font_size=48).next_to(box1_group, RIGHT, buff=0.5)
        self.play(Write(plus_sign))

        box2_group = create_box_with_symbols("🍭", 5, 5, plus_sign.get_right() + RIGHT * 2)
        self.play(Create(box2_group))

        equals_sign = Text("=", font_size=48).next_to(box2_group, RIGHT, buff=0.5)
        self.play(Write(equals_sign))

        result_group = create_box_with_symbols("🍭", 8, 8, equals_sign.get_right() + RIGHT * 2)
        self.play(Create(result_group))
        self.wait(4)

        self.play(FadeOut(VGroup(box1_group, plus_sign, box2_group, equals_sign, result_group)))
        self.play(FadeOut(addition_text))

    # Subtraction Animation
        subtraction_text = Title("SUBTRACTION", color=RED).to_edge(UP)
        self.play(Write(subtraction_text))
        self.wait(1)

    # Create boxes with symbols representing numbers for subtraction
        box3_group = create_box_with_symbols("🍄", 8, 8, ORIGIN + LEFT * 3)
        self.play(Create(box3_group))

        minus_sign = Text("-", font_size=48).next_to(box3_group, RIGHT, buff=0.5)
        self.play(Write(minus_sign))

        box4_group = create_box_with_symbols("🍄", 5, 5, minus_sign.get_right() + RIGHT * 2)
        self.play(Create(box4_group))

        equals_sign = Text("=", font_size=48).next_to(box4_group, RIGHT, buff=0.5)
        self.play(Write(equals_sign))

        result_group2 = create_box_with_symbols("🍄", 3, 3, equals_sign.get_right() + RIGHT * 2)
        self.play(Create(result_group2))
        self.wait(4)

        self.play(FadeOut(VGroup(box3_group, minus_sign, box4_group, equals_sign, result_group2)))
        self.play(FadeOut(subtraction_text))


    def missingnums(self):
        self.create_cross_circles_with_numbers()

    def create_cross_circles_with_numbers(self):
        # Title for the scene
        title = Text("Write Correct Number in the Circle", font_size=32).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Define the positions for the circles
        positions = [
            UP + LEFT * 2,        # Position for blue circle on top-left
            DOWN + LEFT * 2,      # Position for green circle on bottom-left
            UP + RIGHT * 2,       # Position for green circle on top-right
            DOWN + RIGHT * 2,     # Position for blue circle on bottom-right
            ORIGIN                # Position for orange circle at center
        ]
        numbers = [60, 85, None, None, 25]  # Updated numbers
        colors = [BLUE, GREEN, GREEN, BLUE, ORANGE]
        circles = VGroup()
        number_texts = VGroup()

        # Create circles and store numbers separately
        for pos, number, color in zip(positions, numbers, colors):
            circle = Circle(radius=0.5, color=color).move_to(pos)
            circles.add(circle)
            if number is not None:
                number_text = Text(str(number), font_size=24).move_to(pos)
                number_texts.add(number_text)

        # Add circles to the scene
        self.play(Create(circles))
        self.wait(1)

        # Draw lines between the circles
        lines = VGroup(
            Line(positions[0] + RIGHT * 0.5, positions[4] + LEFT * 0.5),  # Top-left to center-left
            Line(positions[1] + RIGHT * 0.5, positions[4] + LEFT * 0.5),  # Bottom-left to center-left
            Line(positions[2] + LEFT * 0.5, positions[4] + RIGHT * 0.5),  # Top-right to center-right
            Line(positions[3] + LEFT * 0.5, positions[4] + RIGHT * 0.5),  # Bottom-right to center-right
        )
        self.play(Create(lines))
        self.wait(1)

        # Add symbols above the lines
        symbol_plus = Tex("+", font_size=24).next_to(lines[0].get_center(), UP)
        symbol_minus = Tex("-", font_size=24).next_to(lines[1].get_center(), UP)
        symbol_equal = Tex("=", font_size=24).next_to(lines[2].get_center(), UP)
        symbol_equal_2 = Tex("=", font_size=24).next_to(lines[3].get_center(), UP)

        # Add numbers inside the circles
        self.play(Write(number_texts))
        self.wait(2)
        
        # Add symbols to the scene
        self.play(Write(symbol_plus), Write(symbol_minus), Write(symbol_equal), Write(symbol_equal_2))
        self.wait(2)

        # Write the result text below the animations
        result_text_1 = Text("60 + 25 = 85", font_size=30,color=BLUE).to_edge(DOWN*1.5, buff=1)
        result_text_2 = Text("85 - 25 = 60", font_size=30,color=GREEN).next_to(result_text_1, DOWN)
        self.play(Write(result_text_1))
        self.play(Write(result_text_2))
        self.wait(2)

        # Add new numbers inside the empty circles
        new_number_texts = VGroup(
            Text("60", font_size=24).move_to(positions[2]),  # Green empty circle on the right side
            Text("85", font_size=24).move_to(positions[3])   # Blue empty circle on the left side
        )
        self.play(Write(new_number_texts))
        self.wait(2)

        # Fade out the circles, lines, symbols, numbers, and result text
        self.play(FadeOut(circles), FadeOut(lines), FadeOut(symbol_plus),
                  FadeOut(symbol_minus), FadeOut(symbol_equal), FadeOut(symbol_equal_2),
                  FadeOut(number_texts), FadeOut(result_text_1), FadeOut(result_text_2),
                  FadeOut(new_number_texts), FadeOut(title))

    def SetDeveloperList(self):  
        self.DeveloperList = "Gayathri Veeramreddy"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName = "Grade3Chapter5UsingAdditionsandSubtractions.py"

if __name__ == "__main__":
    scene = UsingAdditionsandSubtractions()
    scene.render()
