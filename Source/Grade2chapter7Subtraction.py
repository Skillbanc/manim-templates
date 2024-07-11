from manim import *
from AbstractAnim import AbstractAnim
import cvo

class Grade2Chapter7Subtraction(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.c1c2()
        self.fadeOutCurrentScene()
        self.SubtractionUsingExpansion()
        self.fadeOutCurrentScene()
        self.VerticalSubtraction()
        self.fadeOutCurrentScene()
        self.HorizontalSubtraction()
        self.fadeOutCurrentScene()
        self.SymbolFillScene()
        self.fadeOutCurrentScene()
        self.fill_in_the_blanks()
        self.fadeOutCurrentScene()
        self.series_problem()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()


    def c1c2(self):
        self.isRandom = False
        self.positionChoice = [[-3, 0, 0], [3, 2, 0]]
        p10 = cvo.CVO().CreateCVO("Subtraction", "")
        p11 = cvo.CVO().CreateCVO("Symbol Used", "-")

        p10.setcircleradius(1.25)
        p11.setcircleradius(1.25)

        p10.cvolist.append(p11)

        self.construct1(p10, p10)
        self.wait(1)
        self.fadeOutCurrentScene()

    def SubtractionUsingExpansion(self):
        # Title
        title = Text("Subtract numbers using the method of expansion of numbers.", font_size=24)
        title.move_to(UP * 3.5)
        self.play(Write(title))
        self.wait(1)

        # Numbers and breakdowns
        num1 = 65
        num2 = 30

        num1_breakdown = Tex(r"65 = 60 + 5").move_to(UP * 1.2)
        num2_breakdown = Tex(r"30 = 30 + 0").move_to(UP * 0.6)
        self.play(Write(num1_breakdown), Write(num2_breakdown))
        self.wait(1)

        # Perform the subtraction step by step
        sub_step1 = Tex("65 - 30").move_to(UP * 0)
        self.play(Write(sub_step1))
        self.wait(1)

        # Manual calculation steps
        calculation_steps = [
            Tex("65 - 30 = (60 + 5) - 30").move_to(DOWN * 0.5),
            Tex("= 60 + (5 - 30)").move_to(DOWN * 1),
            Tex("= 60 - 25").move_to(DOWN * 1.6),
            Tex("= 35").move_to(DOWN * 2.2),
        ]

        for step in calculation_steps:
            self.play(Write(step))
            self.wait(1)

        self.wait(2)


    def VerticalSubtraction(self):
        # Title
        title = Tex("Subtract the numbers").to_edge(UP)
        self.play(Write(title))
        
        # Subtraction 48 - 26
        subtraction1 = self.vertical_subtraction("48", "26", "22")
        subtraction1.move_to([-4,0,0])

        # Subtraction 59 - 24
        subtraction2 = self.vertical_subtraction("59", "24", "35")
        subtraction2.move_to([-1,0,0])

        # Subtraction 68 - 20
        subtraction3 = self.vertical_subtraction("68", "20", "48")
        subtraction3.move_to([2,0,0])

        # Subtraction 99 - 69
        subtraction4 = self.vertical_subtraction("99", "69", "30")
        subtraction4.move_to([5,0,0])

        # Animate sequentially
        self.play(Create(subtraction1))
        self.wait(1)
        self.play(Create(subtraction2))
        self.wait(1)
        self.play(Create(subtraction3))
        self.wait(1)
        self.play(Create(subtraction4))
        self.wait(1)
        
    def vertical_subtraction(self, top_number, bottom_number, result):
        
        numbers = VGroup(
        Tex(top_number).scale(1.1),
        Tex(bottom_number).scale(1.1), 
        Tex("\\underline{\\phantom{0000}}").scale(2), 
        Tex(result).scale(1.1),               
        Tex("\\underline{\\phantom{0000}}").scale(2), 
        Tex("-").scale(1.1)
        ).arrange(DOWN, buff=0.2) 
    
     
       
        numbers.move_to(ORIGIN)

        numbers[1].next_to(numbers[0],DOWN)
        numbers[5].next_to(numbers[1],LEFT)

        return numbers

    def HorizontalSubtraction(self):
        # Title
        title = Tex("Subtract the numbers given.").to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Subtraction 54 - 31
        subtraction1 = self.horizontal_subtraction("54", "31", "23")
        subtraction1.move_to(UP * 1)

        # Subtraction 35 - 23
        subtraction2 = self.horizontal_subtraction("35", "23", "12")
        subtraction2.move_to(DOWN * 0)

        # Subtraction 65 - 24
        subtraction3 = self.horizontal_subtraction("65", "24", "41")
        subtraction3.move_to(DOWN * 1)

        # Subtraction 76 - 30
        subtraction4 = self.horizontal_subtraction("76", "30", "46")
        subtraction4.move_to(DOWN * 2)

        # Animate sequentially
        self.play(Create(subtraction1))
        self.wait(1)
        self.play(Create(subtraction2))
        self.wait(1)
        self.play(Create(subtraction3))
        self.wait(1)
        self.play(Create(subtraction4))
        self.wait(1)

    def horizontal_subtraction(self, top_number, bottom_number, result):
        numbers = VGroup(
            Tex(top_number).scale(1.5),
            Tex("-").scale(1.5),
            Tex(bottom_number).scale(1.5),
            Tex("=").scale(1.5),
            Tex(result).scale(1.5)
        ).arrange(RIGHT, buff=0.5)

        numbers.move_to(ORIGIN)

        return numbers

    
    def SymbolFillScene(self):
        # Title
        title = Text("Write the correct symbol (+ or -) in the blank boxes.",font_size=26).to_edge(UP)

        # Numbers and boxes for each row
        numbers = [
            ("35", "12", "23", "-"),
            ("47", "13", "60", "+"),
            ("88", "22", "66", "-")
        ]

        # Coordinates for positioning
        x_start = -4
        y_start = 2
        x_gap = 2
        y_gap = 1.5

        # Draw the numbers and boxes
        elements = []
        symbol_boxes = []
        symbols = []
        for i, (left, right, result, symbol) in enumerate(numbers):
            # Left number
            left_text = Text(left).move_to([x_start, y_start - i * y_gap, 0])
            elements.append(left_text)
            
            # Box for symbol
            symbol_box = Square(1).next_to(left_text, RIGHT, buff=0.5)
            elements.append(symbol_box)
            symbol_boxes.append(symbol_box)
            
            # Right number
            right_text = Text(right).next_to(symbol_box, RIGHT, buff=0.5)
            elements.append(right_text)
            
            # Equals sign
            equals_sign = Text("=").next_to(right_text, RIGHT, buff=0.5)
            elements.append(equals_sign)
            
            # Result number
            result_text = Text(result).next_to(equals_sign, RIGHT, buff=0.5)
            elements.append(result_text)

            # Symbol to be filled in the box
            symbol_text = Text(symbol).move_to(symbol_box.get_center())
            symbols.append(symbol_text)

        # Add title to the scene
        self.play(Write(title))
        
        # Animate the elements
        for element in elements:
            self.play(FadeIn(element))
        
        # Animate the symbols filling the boxes
        for symbol_text in symbols:
            self.play(Write(symbol_text))


    def fill_in_the_blanks(self):
        title = Text("Fill in the blank boxes with the correct numbers.", font_size=24)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(2)

        problems = [
            [["3", "6", "1"], ["2", "3"], "3"],
            [["4", "7", "2"], ["2", "5"], "2"],
            [["7", "5", "2"], ["5", "0"], "5"],
            [["6", "8", "3"], ["5", "0"], "8"],
        ]

        positions = [
            LEFT * 4 + UP * 2,
            RIGHT * 2 + UP * 2,
            LEFT * 4 + DOWN * 1,
            RIGHT * 2 + DOWN * 1,
        ]

        for i, (nums, results, box_value) in enumerate(problems):
            pos = positions[i]

            # Display the given numbers in tens and ones place
            num1_tens = Text(nums[0], font_size=24, color=BLUE).move_to(pos)
            num1_ones = Text(nums[1], font_size=24, color=BLUE).next_to(num1_tens, RIGHT, buff=0.5)
            minus_sign = Text("-", font_size=24, color=BLUE).next_to(num1_tens, DOWN * 1.5)
            num2_tens = Text(nums[2], font_size=24, color=BLUE).next_to(minus_sign, RIGHT, buff=0.2)
            box = Square(side_length=0.4, color=PINK).next_to(num2_tens, RIGHT, buff=0.5)
            line = Line(LEFT, RIGHT).next_to(minus_sign, DOWN, buff=0.8).scale(2)
            result_tens = Text(results[0], font_size=24, color=BLUE).next_to(line, DOWN, buff=0.5)
            result_ones = Text(results[1], font_size=24, color=BLUE).next_to(result_tens, RIGHT, buff=0.5)

            self.play(Write(num1_tens), Write(num1_ones))
            self.wait(1)
            self.play(Write(minus_sign), Write(num2_tens), Create(box))
            self.wait(1)
            self.play(Create(line))
            self.wait(1)
            self.play(Write(result_tens), Write(result_ones))
            self.wait(1)

            # Display the box value
            box_value_text = Text(box_value, font_size=24, color=BLUE).move_to(box.get_center())
            self.play(Write(box_value_text))
            self.wait(2)


    def series_problem(self):
        title = Text("Observe the series of numbers. Write the next two numbers in each row.", font_size=24)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(2)

        example = [
            "10", "8", "6", "4", "2"
        ]

        problems = [
            ["9", "7", "5", "", "", "3", "1"],
            ["12", "9", "6", "", "", "3", "0"],
            ["30", "25", "20", "", "", "15", "10"]
        ]

        example_position = LEFT * 3 + UP * 1.5
        positions = [
            LEFT * 3 + UP * 0.5,
            LEFT * 3 + DOWN * 0.5,
            LEFT * 3 + DOWN * 1.5
        ]

        # Example
        example_text = Text("Example:", font_size=24).next_to(example_position, LEFT, buff=0.5)
        self.play(Write(example_text))
        self.wait(1)
        for i, num in enumerate(example):
            pos = example_position + RIGHT * 1.5 * i
            num_text = Text(num, font_size=24)
            self.play(Write(num_text.move_to(pos)))
            self.wait(0.5)

        # Problems
        for i, (nums) in enumerate(problems):
            pos = positions[i]

            problem_label = Text(f"{chr(97 + i)})", font_size=24).next_to(pos, LEFT, buff=0.5)
            self.play(Write(problem_label))
            self.wait(1)
            
            # Display the sequence and underlines
            for j, num in enumerate(nums[:3]):
                num_text = Text(num, font_size=24).move_to(pos + RIGHT * 1.5 * j)
                self.play(Write(num_text))
                self.wait(0.5)
            
            for j in range(3, 5):
                underline = Line(LEFT, RIGHT, color=WHITE).scale(0.4).move_to(pos + RIGHT * 1.5 * j + DOWN * 0.2)
                self.play(Create(underline))
                self.wait(0.5)

            # Display the next two numbers on the underlines
            for j, num in enumerate(nums[5:]):
                num_text = Text(num, font_size=24).move_to(pos + RIGHT * 1.5 * (j + 3))
                self.play(Write(num_text))
                self.wait(0.5)


    def SetDeveloperList(self):
        self.DeveloperList = "Bommi Yaswanth"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName = "Grade2Chapter7Subtraction.py"


if __name__ == "__main__":
    scene = Grade2Chapter7Subtraction()
    scene.render()
