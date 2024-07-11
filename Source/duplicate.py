from manim import *
from AbstractAnim import AbstractAnim  # Assuming AbstractAnim is a custom module you've defined
import cvo  # Assuming cvo is a module you're importing

class TableScene(AbstractAnim):
    def construct(self):
        self.vertical_addition_exercise_1()
    
    def vertical_addition_exercise_1(self):
        # Create addition animation parts
        addition1 = self.vertical_addition("52", "21", "73")
        addition1.move_to([-5, 1, 0])

        # Animate sequentially
        self.play(Write(addition1[0]))  # Top number
        self.wait(0.5)
        self.play(Write(addition1[1]))  # Bottom number
        self.wait(0.5)
        self.play(Write(addition1[5]))  # Plus symbol
        self.wait(0.5)
        self.play(Write(addition1[2]))  # First underline
        self.wait(0.5)
        self.play(Write(addition1[4]))  # Second underline
        self.wait(0.5)

        # Highlight units place
        self.play(
            addition1[0][1].animate.set_color(YELLOW),
            addition1[1][1].animate.set_color(YELLOW)
        )
        self.wait(0.5)
        
        # Write intermediate result for units place
        unit_result = Tex("3").scale(1.1).next_to(addition1[2], DOWN, buff=0.1).shift(RIGHT * 0.7)
        self.play(Write(unit_result))
        self.wait(0.5)

        # Highlight tens place
        self.play(
            addition1[0][0].animate.set_color(YELLOW),
            addition1[1][0].animate.set_color(YELLOW)
        )
        self.wait(0.5)
        
        # Write intermediate result for tens place
        tens_result = Tex("7").scale(1.1).next_to(unit_result, LEFT, buff=0.2)
        self.play(Write(tens_result))
        self.wait(0.5)

        # Show final result
        self.play(Write(addition1[3]))  # Final result
        self.wait(1.5)

    def vertical_addition(self, top_number, bottom_number, result):
        numbers = VGroup(
            Tex(top_number).scale(1.1),
            Tex(bottom_number).scale(1.1),
            Tex("\\underline{\\phantom{0000}}").scale(2),
            Tex(result).scale(1.1),
            Tex("\\underline{\\phantom{0000}}").scale(2),
            Tex("+").scale(1.1)
        ).arrange(DOWN, buff=0.2)

        # Positioning elements
        numbers[1].next_to(numbers[0], DOWN)
        numbers[5].next_to(numbers[1], LEFT)

        return numbers

if __name__ == "__main__":
    scene = TableScene()
    scene.render()
