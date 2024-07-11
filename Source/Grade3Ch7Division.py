from manim import *
from AbstractAnim import AbstractAnim
import cvo
from numpy import size

class division(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.introc1()
        self.fadeOutCurrentScene()
        self.show_intro()
        self.fadeOutCurrentScene()
        self.define_division()
        self.fadeOutCurrentScene()
        self.exampledivision()
        self.fadeOutCurrentScene()
        self.laddu()
        self.fadeOutCurrentScene()
        self.toffies() 
        self.fadeOutCurrentScene()
        self.example3()
        self.fadeOutCurrentScene()
        self.muldiv()  
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()


    def show_intro(self):
        # Title for the scene
        intro_title = Text("CH-DIVISION", font_size=72, color=BLUE)
        self.play(Write(intro_title))
        self.wait(2)
        self.play(FadeOut(intro_title))

    def introc1(self):
         
        self.setNumberOfCirclePositions(3)
        #self.angleChoice = [0,0,0]
        self.isRandom = False
        p8=cvo.CVO().CreateCVO("DIVISION","")
        p9=cvo.CVO().CreateCVO("Defination","Division is splitting a number into equal parts.\n"
            "It is the process of finding out how many times\n"
            "one number is contained within another number.").setPosition([2,2,2])
        p7=cvo.CVO().CreateCVO("Symbol","'/'").setPosition([2,0,2])
        p10=cvo.CVO().CreateCVO("Example","20/5=4").setPosition([2,-2.5,2])
        p8.cvolist.append(p9)
        p8.cvolist.append(p7)
        p8.cvolist.append(p10)
        self.construct1(p8,p8)

    
    def define_division(self):
        
         # Title for the definition
        definition_title = Text("What is Division?", font_size=55, color=YELLOW).to_edge(UP)
        self.play(Write(definition_title))

        # Definition of division
        definition = Text(
            "Division is splitting a number into equal parts.\n"
            "It is the process of finding out how many times\n"
            "one number is contained within another number.",
            font_size=38
        ).next_to(definition_title, DOWN)

        self.play(Write(definition))
        self.wait(3)

        # Fade out the definition title and text
        self.play(FadeOut(definition_title), FadeOut(definition))

        # Introduce the symbol for division
        symbol_title = Text("The Symbol of Division", font_size=48, color=YELLOW).to_edge(UP)
        self.play(Write(symbol_title))

        # Symbol of division
        symbol = Text("÷", font_size=96, color=RED).next_to(symbol_title, DOWN, buff=1)

        # Explanation of the symbol
        symbol_explanation = Text(
            "The symbol for division is ' ÷ '\n\n \t\t'20 ÷ 4 = 5'",
            
            font_size=24
        ).next_to(symbol, DOWN, buff=0.5)

        self.play(Write(symbol))
        self.wait(1)
        self.play(Write(symbol_explanation))
        self.wait(3)

    def exampledivision(self):
         # Create Text objects
        title = Text("Division: 20 ÷ 4 = 5",color=BLUE).scale(1.5).to_edge(UP)
        explanation = Text("20 divided into 4 equal parts",color=BLUE_A).next_to(title, DOWN)
        
        # Show the title
        self.play(Write(title))
        self.play(Write(explanation))
        self.wait(1)

        # Draw the dividend and divisor
        dividend = Integer(20).shift(LEFT * 2 + UP)
        divisor = Integer(4).shift(RIGHT * 2 + UP)
        
        dividend_label = Text("20 (dividend)").next_to(dividend, DOWN)
        divisor_label = Text("4 (divisor)").next_to(divisor, DOWN)

        self.play(Write(dividend), Write(dividend_label))
        self.play(Write(divisor), Write(divisor_label))
        self.wait(1)
        
        # Explain repeated subtraction
        steps = [
            "20 - 4 = 16",
            "16 - 4 = 12",
            "12 - 4 = 8",
            "8 - 4 = 4",
            "4 - 4 = 0"
        ]
        
        step_texts = [Text(step).scale(0.75) for step in steps]
        for i, step_text in enumerate(step_texts):
            step_text.next_to(dividend).shift(DOWN *0.5* (i+3))
        
        for step_text in step_texts:
            self.play(Write(step_text))
            self.wait(0.5)
        
        # Show the quotient
        quotient = Text("The quotient is 5.'Therefore, 20 ÷ 4 = 5'",color=RED).next_to(step_texts[-1], DOWN * 1)
        self.play(Write(quotient))
        self.wait(2)



    def laddu(self):
        # Title for the scene
        title = Text("Example:Laddoos and Plates",color=BLUE, font_size=36).to_edge(UP)
        self.play(Write(title))

        # Explanation text
        explanation_text = Text("There are 12 laddoos in a plate. Keep them equally in two plates.", font_size=24).next_to(title, DOWN)
        self.play(Write(explanation_text))
        
        # Representing the initial plate with 12 laddoos
        initial_plate = Ellipse(width=4, height=2, color=BLUE).shift(UP * 1.5)
        laddoos = VGroup(*[Circle(radius=0.2, color=YELLOW, fill_opacity=1) for _ in range(12)])
        laddoos.arrange_in_grid(rows=3, cols=4, buff=0.3).move_to(initial_plate.get_center())
        
        # Create the initial plate with laddoos
        self.play(Create(initial_plate), Create(laddoos))
        self.wait(1)
        
        # Text to indicate initial plate
        initial_text = Text("12 Laddoos in one plate  ", font_size=24).next_to(initial_plate, DOWN)
        self.play(Write(initial_text))
        self.wait(1)
        
        # Representing two empty plates
        left_plate = Ellipse(width=3, height=1.5, color=GREEN).shift(DOWN * 1.5 + LEFT * 2.5)
        right_plate = Ellipse(width=3, height=1.5, color=GREEN).shift(DOWN * 1.5 + RIGHT * 2.5)
        
        self.play(Create(left_plate), Create(right_plate))
        self.wait(1)
        
        # Text to indicate the task
        task_text = Text("Distributing the laddoos equally into two plates =12/6\n \t \t \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t=6 in each", font_size=24).next_to(initial_text, DOWN*2.5, buff=1)
        self.play(Write(task_text))
        self.wait(1)

        # Distribute the laddoos into two plates (6 laddoos per plate)
        left_laddoos = laddoos[:6]
        right_laddoos = laddoos[6:]

        for laddoo in left_laddoos:
            self.play(laddoo.animate.move_to(left_plate.get_center() + (0.5 - np.random.rand()) * LEFT * 1 + (0.5 - np.random.rand()) * UP * 0.5))
        for laddoo in right_laddoos:
            self.play(laddoo.animate.move_to(right_plate.get_center() + (0.5 - np.random.rand()) * LEFT * 1 + (0.5 - np.random.rand()) * UP * 0.5))
        
        self.wait(2)
        
        # Text to explain the result
        result_text = Text("Each plate has 6 laddoos.", font_size=24).next_to(task_text, DOWN, buff=1)
        self.play(Write(result_text))
        self.wait(2)
    def toffies(self):
        # Title for the scene
        title = Text("Division of 20 Toffees Among 5 Friends", color=BLUE,font_size=36).to_edge(UP)
        self.play(Write(title))

        # Explanation text - initial
        explanation_text = Text("Let's divide 20 toffees equally among 5 friends.",color=BLUE_A, font_size=24).next_to(title, DOWN)
        self.play(Write(explanation_text))

        # Representing the 20 toffees with dots
        toffees = VGroup(*[Dot() for _ in range(20)])
        toffees.arrange_in_grid(rows=4, buff=0.5).to_edge(LEFT, buff=1)

        # Create the 20 toffees
        self.play(Create(toffees))
        self.wait(1)

        # Text to explain the toffees
        toffee_text = Text("We have 20 toffees.", font_size=24).next_to(toffees, DOWN, buff=1)
        self.play(Write(toffee_text))
        self.wait(1)

        # Text to introduce the division concept
        divide_text = Text("...............................divide them equally among 5 friends. =20/5 = 4 each", font_size=24).next_to(toffee_text, DOWN)
        self.play(Write(divide_text))
        self.wait(2)

        # Representing the 5 friends with square boxes
        friends = VGroup(*[Square(side_length=1) for _ in range(5)])
        friends.arrange(RIGHT, buff=1).to_edge(RIGHT, buff=1)

        # Create the boxes
        self.play(Create(friends))
        self.wait(1)

        # Add labels to the friends
        friend_labels = VGroup(*[Text(f"Friend {i+1}", font_size=24) for i in range(5)])
        for i, label in enumerate(friend_labels):
            label.next_to(friends[i], DOWN)
        
        self.play(Write(friend_labels))
        self.wait(1)

        # Add text to explain the process
        process_text = Text("Distributing the toffees equally...", font_size=24).next_to(divide_text, DOWN)
        self.play(Write(process_text))
        self.wait(1)
        
        # Define positions within a single box for 4 positions
        positions = [
            LEFT + UP, RIGHT + UP, LEFT + DOWN, RIGHT + DOWN
        ]

        # Distribute the toffees into the boxes (each friend gets 4 toffees)
        for i in range(20):
            target_position = friends[i % 5].get_center() + positions[i % 4] * 0.3
            self.play(toffees[i].animate.move_to(target_position))

        self.wait(2)

        # Text to explain the grouping process
        grouping_text = Text("Each friend gets 4 toffees.", font_size=24).next_to(process_text, DOWN, buff=1)
        self.play(Write(grouping_text))
        self.wait(2)

        # Text to explain the result of division
        result_text = Text("Therefore, 20 ÷ 5 = 4.",color=RED_C, font_size=24).next_to(grouping_text, DOWN, buff=1)
        self.play(Write(result_text))
        self.wait(2)

        # Ending text to conclude the explanation
        conclusion_text = Text("Each friend receives 4 toffees.", font_size=24).next_to(result_text, DOWN, buff=1)
        self.play(Write(conclusion_text))
        self.wait(2)
# To render the scene, use the following command in terminal:
# manim -pql division_of_toffees.py DivisionOfToffees

    
    def example3(self):
        # Title for the scene
        # Title for the scene
        title = Text("Repeated Subtraction to Divide Equally",color=RED, font_size=36).to_edge(UP)
        self.play(Write(title))

        # Explanation text - initial
        explanation_text = Text("Distributing 8 balls into equal groups of 4 balls", color=GOLD,font_size=24).next_to(title, DOWN)
        self.play(Write(explanation_text))

        # Representing the 8 balls
        balls = VGroup(*[Circle(radius=0.3, color=BLUE, fill_opacity=1) for _ in range(8)])
        balls.arrange_in_grid(rows=2, cols=4, buff=0.5).to_edge(LEFT, buff=1.5)

        # Create the 8 balls
        self.play(Create(balls))
        self.wait(1)

        # Text to indicate initial state
        initial_text = Text("Total balls are 8", font_size=24).next_to(balls, DOWN, buff=0.5)
        self.play(Write(initial_text))
        self.wait(1)

        # Representing the empty groups/boxes
        left_box = Rectangle(width=2, height=2, color=GREEN).shift(RIGHT * 3.5 + UP * 1.2)
        right_box = Rectangle(width=2, height=2, color=GREEN).shift(RIGHT * 3.5 + DOWN *1)

        self.play(Create(left_box), Create(right_box))
        self.wait(1)

        # Text to explain the first subtraction
        subtract_text1 = Text("First time taking away 4 balls", font_size=24).next_to(initial_text, DOWN, buff=1)
        self.play(Write(subtract_text1))
        self.wait(1)

        # Move first 4 balls to the left box
        for i in range(4):
            self.play(balls[i].animate.move_to(left_box.get_center() + (i % 2 - 0.5) * LEFT + (i // 2 - 0.5) * UP))
        self.wait(1)

        # Text to show the remaining balls
        remaining_text1 = Text("Remaining balls: 4", font_size=24).next_to(subtract_text1, buff=1)
        self.play(Write(remaining_text1))
        self.wait(1) 

        # Transform subtract_text1 to subtract_text2
        subtract_text2 = Text("Second time taking away 4 balls", font_size=24).next_to(explanation_text, DOWN, buff=1)
        self.play(Transform(subtract_text1, subtract_text2))
        self.wait(1)

        self.play(FadeOut(remaining_text1))

        # Move remaining 4 balls to the right box
        for i in range(4, 8):
            self.play(balls[i].animate.move_to(right_box.get_center() + ((i % 4) % 2 - 0.5) * LEFT + ((i % 4) // 2 - 0.5) * UP))
        self.wait(1)

        # Text to show the remaining balls and explain the division result
        remaining_text2 = Text("Remaining balls: 0\n\n8 ÷ 4 = 2\n8 is dividend\n4 is divisor\n2 is quotient\n0 is remainder", font_size=24).next_to(subtract_text2, DOWN, buff=1)
        self.play(Write(remaining_text2))
        self.wait(1)

    def SetDeveloperList(self):
        self.DeveloperList="Sai Krishna Bikkumalla"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade3Ch7Division.py"

# To render the scene, use the following command in terminal:
# manim -pql repeated_subtraction_division.py RepeatedSubtractionDivision
    def muldiv(self):
        
        # Title
        title = Text("Relation between Division and Multiplication",color=RED).scale(0.8)
        title.to_edge(UP)
        
        # Apple groups illustration
        apples = [SVGMobject("apple.svg").scale(0.2) for _ in range(15)]
        apple_group_3x5 = VGroup(*apples).arrange_in_grid(rows=3, cols=5, buff=0.1)
        apple_label = Text("15 apples", font_size=24)
        apple_label.next_to(apple_group_3x5, DOWN)
        
        # Multiplication box
        mult_title = Text("Multiplication", font_size=24, color=BLUE).to_edge(LEFT).to_edge(UP*2.5)
        mult_text1 = Text("3 Groups of 5 make 15", font_size=24)
        mult_text2 = Text("3 x 5 = 15", font_size=24)
        mult_text3 = Text("and also:", font_size=24)
        mult_text4 = Text("5 groups of 3 make 15", font_size=24)
        mult_text5 = Text("5 x 3 = 15", font_size=24)
        
        mult_text1.next_to(mult_title, DOWN, aligned_edge=LEFT)
        mult_text2.next_to(mult_text1, DOWN, aligned_edge=LEFT)
        mult_text3.next_to(mult_text2, DOWN, aligned_edge=LEFT)
        mult_text4.next_to(mult_text3, DOWN, aligned_edge=LEFT)
        mult_text5.next_to(mult_text4, DOWN, aligned_edge=LEFT)
        
        mult_box = VGroup(mult_title, mult_text1, mult_text2, mult_text3, mult_text4, mult_text5)
        
        # Division box
        div_title = Text("Division", font_size=24, color=BLUE).next_to(apple_label,RIGHT,buff=RIGHT).to_edge(UP*2.5)
        div_text1 = Text("So 15 divided by 3 is 5", font_size=24)
        div_text2 = Text("15 ÷ 3 = 5", font_size=24)
        div_text3 = Text("So 15 divided by 5 is 3", font_size=24)
        div_text4 = Text("15 ÷ 5 = 3", font_size=24)
        
        div_text1.next_to(div_title, DOWN, aligned_edge=LEFT)
        div_text2.next_to(div_text1, DOWN, aligned_edge=LEFT)
        div_text3.next_to(div_text2, DOWN, aligned_edge=LEFT)
        div_text4.next_to(div_text3, DOWN, aligned_edge=LEFT)
        
        div_box = VGroup(div_title, div_text1, div_text2, div_text3, div_text4)
        
        # Conclusion text
        conclusion_text = Text("Every multiplication can be written in the form of division and every\n division can be written in the form of a multiplication.", font_size=24)
        conclusion_text.next_to(VGroup(mult_box, div_box), DOWN*2, buff=1)
        
        # Grouping all elements together
        all_elements = VGroup(title, apple_group_3x5, apple_label, mult_box, div_box, conclusion_text)
        self.add(all_elements)
        self.play(FadeIn(all_elements))
        
        # Explanation of Multiplication
        self.play(Indicate(mult_text1, color=YELLOW))
        self.play(Indicate(mult_text2, color=YELLOW))
        
        self.play(Indicate(apple_group_3x5[:5], color=GREEN))
        self.wait(1)
        self.play(Indicate(apple_group_3x5[5:10], color=GREEN))
        self.wait(1)
        self.play(Indicate(apple_group_3x5[10:], color=GREEN))
        self.wait(1)

        self.play(Indicate(mult_text4, color=YELLOW))
        self.play(Indicate(mult_text5, color=YELLOW))
        
        self.play(Indicate(apple_group_3x5[::5], color=GREEN))
        self.wait(1)
        self.play(Indicate(apple_group_3x5[1::5], color=GREEN))
        self.wait(1)
        self.play(Indicate(apple_group_3x5[2::5], color=GREEN))
        self.wait(1)
        self.play(Indicate(apple_group_3x5[3::5], color=GREEN))
        self.wait(1)
        self.play(Indicate(apple_group_3x5[4::5], color=GREEN))
        self.wait(1)
        
        # Explanation of Division
        self.play(Indicate(div_text1, color=YELLOW))
        self.play(Indicate(div_text2, color=YELLOW))
        
        self.play(Indicate(apple_group_3x5, color=BLUE))
        self.wait(1)
        
        self.play(Indicate(div_text3, color=YELLOW))
        self.play(Indicate(div_text4, color=YELLOW))
        
        self.play(Indicate(apple_group_3x5, color=BLUE))
        self.wait(1)
        
        # Emphasize the conclusion
        self.play(Write(conclusion_text))
        
        self.wait(1)

# Save this as `apple.svg`
SVG_CODE = '''
<svg height="100" width="100" xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="red" />
</svg>
'''

with open("apple.svg", "w") as f:
    f.write(SVG_CODE)

if __name__ == "__main__":
        scene = division()
        scene.render()
        
#transorm