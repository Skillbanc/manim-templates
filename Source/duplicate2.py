from manim import *
from AbstractAnim import AbstractAnim
import cvo

class SquareVisuals(AbstractAnim):
    def construct(self):
        self.Add()
        self.Anim()  # Call the Anim method after Add
    

    def Add(self):
        self.isRandom = False
        t1 = Text("Addition of Numbers not Exceeding 20", font_size=30)
        t1.move_to([0, 0, 0])
        # Write the text and the underline
        self.play(Write(t1))
        self.wait(2)
        self.play(FadeOut(t1))
        self.wait(1)
        p10 = cvo.CVO().CreateCVO("Addition", "")
        p12 = cvo.CVO().CreateCVO("Definition", "sum of two numbers")
        p11 = cvo.CVO().CreateCVO("Symbol", "+")
        p10.cvolist.append(p12)
        p10.cvolist.append(p11)
        self.setNumberOfCirclePositions(3)
        self.construct1(p10, p10)
        self.wait(2)

    def Anim(self):
        ex = Text("Example", font_size=25)
        ex.move_to([-5, 3, 0])
        self.play(Write(ex))
        self.wait(1)

        problems = [
            (8, 7, 15),
            (10, 8, 18),
            (9, 3, 12)
        ]
    
        def create_chick(chick, row, col):
            chick_text = Text(chick, font_size=30, color=YELLOW)
            x_pos = -6 + col * 1  # Adjust horizontal spacing (1 is an example)
            y_pos = 1 - row * 1   # Adjust vertical spacing (1 is an example)
            chick_text.move_to(np.array([x_pos, y_pos, 0]))
            return chick_text
        
        chick_emoji = "🐤"

        for first_addend, second_addend, result in problems:
            problem_text = Text(f"{first_addend} + {second_addend} = {result}", font_size=40, color=BLUE)
            self.play(Write(problem_text))
            self.wait(1)
            self.play(problem_text.animate.shift(UP * 3.3))
            self.wait(1)
            
            # Create emojis for first addend
            first_addend_chick = VGroup()
            for i in range(first_addend):
                col = i % 5  # Adjust columns as needed
                row = i // 5  # Adjust rows as needed
                chick = create_chick(chick_emoji, row, col)
                first_addend_chick.add(chick)
            
            first_addend_label = Text(f"{first_addend}", font_size=24)
            first_addend_label.next_to(first_addend_chick, DOWN)
            
            self.play(
                FadeIn(first_addend_chick),
                Write(first_addend_label)
            )
            self.wait(2)

            # Animate addition
            plus_text = Text("+", font_size=125, color=BLUE)
            plus_text.next_to(first_addend_chick, RIGHT)
            self.play(Write(plus_text))
            self.wait(1)

            # Create emojis for second addend
            second_addend_chick = VGroup()
            for i in range(second_addend):
                col = i % 4  # Adjust columns as needed
                row = i // 4  # Adjust rows as needed
                chick = create_chick(chick_emoji, row, col)
                second_addend_chick.add(chick)

            second_addend_chick.next_to(plus_text, RIGHT)
            
            second_addend_label = Text(f"{second_addend}", font_size=24)
            second_addend_label.next_to(second_addend_chick, DOWN)
            
            self.play(
                FadeIn(second_addend_chick),
                Write(second_addend_label)
            )
            self.wait(2)

            # Animate equals sign
            equal_text = Text("=", font_size=125, color=BLUE)
            equal_text.next_to(second_addend_chick, RIGHT)
            self.play(Write(equal_text))
            self.wait(1)

            # Create emojis for result
            result_chick = VGroup()
            for i in range(result):
                col = i % 3  # Adjust columns as needed
                row = i // 3  # Adjust rows as needed
                chick = create_chick(chick_emoji, row, col)
                result_chick.add(chick)

            result_chick.next_to(equal_text, RIGHT)
            
            result_label = Text(f"{result}", font_size=24)
            result_label.next_to(result_chick, DOWN)
            
            self.play(
                FadeIn(result_chick),
                Write(result_label)
            )
            self.wait(2)
            
            # Fade out all elements for the current problem
            self.play(
                FadeOut(problem_text),
                FadeOut(first_addend_chick),
                FadeOut(second_addend_chick),
                FadeOut(result_chick),
                FadeOut(first_addend_label),
                FadeOut(second_addend_label),
                FadeOut(result_label),
                FadeOut(plus_text),
                FadeOut(equal_text)
            )
        
        self.wait(2)

# To run the scene
if __name__ == "__main__":
    scene = SquareVisuals()
    scene.render()
