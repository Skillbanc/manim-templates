from manim import *
from AbstractAnim import AbstractAnim
import cvo

class Grade1Chapter13Numbersfrom20to100(AbstractAnim):
    
    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.numbersfrom20to100()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()


    def Introduction(self):
        p10 = cvo.CVO().CreateCVO("Numbers", "").setPosition([-3,1,0])
        p11 = cvo.CVO().CreateCVO("Definition", "A symbol representing quantity or amount").setPosition([3,1,0])
        
        p10.cvolist.append(p11)
        self.construct1(p10, p10)

        
    def numbersfrom20to100(self): 
        numbers = list(range(20, 101))

        for number in numbers:
            tens = number // 10
            ones = number % 10

            # Create text to display the number and its tens and ones
            number_text = Text(f"Number: {number}", font_size=36).to_edge(UP)
            tens_text = Text(f"Tens: {tens}", font_size=24).next_to(number_text, DOWN)
            ones_text = Text(f"Ones: {ones}", font_size=24).next_to(tens_text, DOWN)
            sum_text = Text(f"{number} = {tens} tens + {ones} ones = {tens * 10} + {ones} = {number}", font_size=24).next_to(ones_text, DOWN)
            self.play(FadeIn(number_text))
            self.play(FadeIn(tens_text), FadeIn(ones_text))
            self.play(FadeIn(sum_text))

            # Create bundles of sticks (tens) and squares (ones)
            bundles = VGroup(*[Rectangle(width=0.15, height=1.5, color=BLUE) for _ in range(tens)]).arrange(RIGHT, buff=0.2).shift(LEFT*2)
            bundles_text = Text(f"{tens} tens", font_size=24).next_to(bundles, DOWN)

            # Create and position the plus sign
            plus_sign = Text("+", font_size=72).next_to(bundles, RIGHT, buff=1)
            
            # Play animations
            self.play(LaggedStart(*[GrowFromCenter(stick) for stick in bundles], lag_ratio=0.1, run_time=2))
            self.play(FadeIn(bundles_text))
            self.play(FadeIn(plus_sign))

            if number % 10 == 0:
                # Display zero
                zero_text = Text("0", font_size=72, color=RED).next_to(plus_sign, RIGHT, buff=1)
                self.play(FadeIn(zero_text))
            else:
                # Create loose squares
                loose_squares = VGroup()
                for i in range(ones):
                    square = Square(side_length=0.3, color=GREEN)
                    row = i // 5
                    col = i % 5
                    square.shift(RIGHT * (2 + col * 0.5) + DOWN * row * 0.6 + UP * 0.3)  # Shift each square up by 0.6 units
                    loose_squares.add(square)
                self.play(LaggedStart(*[GrowFromCenter(square) for square in loose_squares], lag_ratio=0.1, run_time=2))
                loose_squares_text = Text(f"{ones} ones", font_size=24).next_to(loose_squares, DOWN)
                self.play(FadeIn(loose_squares_text))

            self.wait(1)

            # Fade out everything for the current number
            if number % 10 == 0:
                self.play(FadeOut(number_text), FadeOut(tens_text), FadeOut(ones_text), FadeOut(sum_text), FadeOut(bundles), FadeOut(bundles_text), FadeOut(plus_sign), FadeOut(zero_text))
            else:
                self.play(FadeOut(number_text), FadeOut(tens_text), FadeOut(ones_text), FadeOut(sum_text), FadeOut(bundles), FadeOut(bundles_text), FadeOut(plus_sign), FadeOut(loose_squares), FadeOut(loose_squares_text))

    def SetDeveloperList(self): 
       self.DeveloperList="Snehith" 
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Shapes.py"
 

if __name__ == "__main__":
    scene = Grade1Chapter13Numbersfrom20to100()
    scene.render()
