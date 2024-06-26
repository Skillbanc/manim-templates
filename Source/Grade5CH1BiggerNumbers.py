from manim import *
from AbstractAnim import AbstractAnim
import cvo

class BigNumbers(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.placeValue()
        self.fadeOutCurrentScene()
        self.expansion()
        self.fadeOutCurrentScene()
        self.addingBiggerNumbers()
        self.fadeOutCurrentScene()
        self.subtractingBiggerNumbers()
        self.fadeOutCurrentScene()
        self.comparingBiggerNumbers()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

    def placeValue(self):
        self.setNumberOfCirclePositions(2)
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Place Value", "")
        p11 = cvo.CVO().CreateCVO("Understanding Place Value", "")
        p11.extendOname(["Units", "Tens", "Hundreds", "Thousands", "Ten Thousands", "Lakhs"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10, p10)
        self.fadeOutCurrentScene()

        title = Text("Place Value", font_size=30).to_edge(UP)
        explanation = Text("Understanding the value of digits based on their positions in a number.", font_size=24).next_to(title, DOWN, buff=0.5)
        example = MathTex("2345").scale(2).next_to(explanation, DOWN, buff=1)
        self.play(Write(title), Write(explanation), Write(example))
        self.wait(1)
        
        digits_texts = [
            "\\text{$ 2 \\Rightarrow \\text{Thousands place} $}",
            "\\text{$ 3 \\Rightarrow \\text{Hundreds place} $}",
            "\\text{$ 4 \\Rightarrow \\text{Tens place} $}",
            "\\text{$ 5 \\Rightarrow \\text{Units place} $}",
        ]
        
        digits = VGroup(*[MathTex(text, font_size=30) for text in digits_texts]).arrange(DOWN, aligned_edge=LEFT).next_to(example, DOWN, buff=1)

        self.play(Write(digits))
        self.wait(2)
        

    def expansion(self):
        self.setNumberOfCirclePositions(2)
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Number Expansion", "")
        p11 = cvo.CVO().CreateCVO("Expanded Form", "")
        p11.extendOname(["1234 = 1000 + 200 + 30 + 4", "56789 = 50000 + 6000 + 700 + 80 + 9"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10, p10)
        self.fadeOutCurrentScene()

        title = Text("Expansion", font_size=30).to_edge(UP)
        explanation = Text("Breaking down a number into its place value components.", font_size=24).next_to(title, DOWN, buff=0.5)
    
        example1 = MathTex(
            "4567 &= \\text{Four thousand five hundred and sixty-seven} \\\\",
            "&= 4 \\text{ thousand} + 5 \\text{ hundred} + 6 \\text{ ten} + 7 \\text{ ones} \\\\",
            "&= 4000 + 500 + 60 + 7",
            font_size=35
        ).next_to(explanation, DOWN, buff=1)
        example2 = MathTex(
            "1981 &= \\text{One thousand Nine hundred and eighty one} \\\\",
            "&= 1 \\text{ thousand} + 9 \\text{ hundred} + 8 \\text{ ten} + 1 \\text{ ones} \\\\",
            "&= 1000 + 900 + 80 + 1",
            font_size=35
        ).next_to(example1, DOWN, buff=1)

        self.play(Write(title))
        self.wait(1)
        self.play(Write(explanation))
        self.wait(1)
        self.play(Write(example1))
        self.play(Write(example2))
        self.wait(3)

    def addingBiggerNumbers(self):
        self.positionChoice=[[-4,0,0],[0,0,0],[4,0,0]]        
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Bigger Numbers", "")
        p11 = cvo.CVO().CreateCVO("Addition", "12345+67890")
        p12 = cvo.CVO().CreateCVO("Sum", "80235")
        

        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        self.construct1(p10, p10)
        self.fadeOutCurrentScene()

        title = Text("Adding Bigger Numbers", font_size=30).to_edge(UP)
        explanation = Text("Adding numbers with multiple digits.", font_size=24).next_to(title, DOWN, buff=0.5)
        example = MathTex("2987 + 3451 = 6438", font_size=35).next_to(explanation, DOWN, buff=1)
        self.play(Write(title))
        self.wait(1)
        self.play(Write(explanation))
        self.wait(1)
        self.play(Write(example))

        number1 = Tex("2987")
        number2 = Tex("3451").next_to(number1,DOWN)
        plus_sign = MathTex("+").scale(0.7).next_to(number2,LEFT)
        line = Line(number2.get_left(), number2.get_right()).next_to(number2, DOWN)
        sum_number = Tex("6438").next_to(line,DOWN)
        equals_sign = MathTex("=").scale(0.7).next_to(sum_number,LEFT)

        
        # Create the animation
        self.play(Write(number1))
        self.play(Write(number2))
        self.play(Write(line))  # Adding the line after number2  
        self.play(Write(plus_sign))
        self.wait(1)
        self.play(Write(equals_sign))
        self.play(Write(sum_number))
        self.wait(1)
        self.wait(3)

    def subtractingBiggerNumbers(self):
        self.positionChoice=[[-4,0,0],[0,0,0],[4,0,0]]        
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Bigger Numbers", "")
        p11 = cvo.CVO().CreateCVO("Subtraction", "67890-12345")
        p12 = cvo.CVO().CreateCVO("Difference", "55545")
        

        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        self.construct1(p10, p10)
        self.fadeOutCurrentScene()

        title = Text("Subtracting Bigger Numbers", font_size=30).to_edge(UP)
        explanation = Text("Subtracting numbers with multiple digits.", font_size=24).next_to(title, DOWN, buff=0.5)
        example = MathTex("3451 - 1987 = 1461", font_size=24).next_to(explanation, DOWN, buff=1)

        self.play(Write(title))
        self.wait(1)
        self.play(Write(explanation))
        self.wait(1)
        self.play(Write(example))

        number1 = Tex("3451")
        number2 = Tex("1987").next_to(number1,DOWN)
        minus_sign = Tex("-").scale(0.7).next_to(number2,LEFT)
        line = Line(number2.get_left(), number2.get_right()).next_to(number2, DOWN)
        sum_number = Tex("1461").next_to(line,DOWN)
        equals_sign = Tex("=").scale(0.7).next_to(sum_number,LEFT)

        # Create the animation
        self.play(Write(number1))
        self.play(Write(number2))
        self.play(Write(line))  # Adding the line after number2  
        self.play(Write(minus_sign))
        self.wait(1)
        self.play(Write(equals_sign))
        self.play(Write(sum_number))
        self.wait(3)

    def comparingBiggerNumbers(self):
        title = Text("Steps for Comparing Two Numbers", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        explanation = Text("Compare the digits starting from the leftmost digit.", font_size=24).next_to(title, DOWN, buff=0.5)
        self.play(Write(explanation))
        self.wait(1)

        example = MathTex(r"Compare: 4567 \text{ and } 4568", font_size=30).next_to(explanation, DOWN, buff=0.5)
        self.play(Write(example))
        self.wait(1)

        steps = [
            r"\text{1. Compare the thousands place digits: } 4 \text{ and } 4.",
            r"\text{2. If they are equal, move to the next digit.}",
            r"\text{3. Compare the hundreds place digits: } 5 \text{ and } 5.",
            r"\text{4. If they are equal, move to the next digit.}",
            r"\text{5. Compare the tens place digits: } 6 \text{ and } 6.",
            r"\text{6. If they are equal, move to the next digit.}",
            r"\text{7. Compare the ones place digits: } 7 \text{ and } 8.",
            r"\text{8. Since } 7 < 8, \text{ we conclude that } 4567 < 4568.",
        ]

        steps_group = VGroup(*[MathTex(text, font_size=30) for text in steps]).arrange(DOWN, aligned_edge=LEFT).next_to(example, DOWN)
        self.play(Write(steps_group))
        self.wait(5)
       


    def SetDeveloperList(self):  
        self.DeveloperList="Shanmukha Priya"
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade5CH1BiggerNumbers.py"

if __name__ == "__main__":
     scene = BigNumbers()
     scene.render()
