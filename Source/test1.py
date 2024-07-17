from manim import *
from AbstractAnim import AbstractAnim
import cvo

class test1(AbstractAnim):

    def construct(self):
      
        self.topic1()

    def topic1(self):
        operations = [
            ("addition", 2, 3),
            ("subtraction", 5, 2),
            ("multiplication", 2, 3),
        ]
        for operation, a, b in operations:
            self.clear()
            number_line = self.create_number_line()
            self.play(Create(number_line))
            self.perform_operation(number_line, a, b, operation)
            self.wait()
        self.fadeOutCurrentScene()

    def create_number_line(self):
        return NumberLine(
            x_range=[-10, 10, 1],
            length=12,
            color=BLUE,
            include_numbers=True,
            label_direction=DOWN,
        )

    def create_jump_path(self, start, end):
        control_point = start + (end - start) / 2 + UP * 0.5
        path = CubicBezier(start, control_point, control_point, end)
        dashed_path = DashedVMobject(path, num_dashes=15, color=YELLOW)
        return path, dashed_path

    def perform_operation(self, number_line, a, b, operation):
        colors = {"addition": RED, "subtraction": BLUE, "multiplication": GREEN}
        dot = Dot(color=colors[operation]).scale(1.5)
        title = Text(f"{operation.capitalize()} Jumps", font_size=48).to_edge(UP)
        underline = Line(
            start=title.get_left() + DOWN * 0.3,
            end=title.get_right() + DOWN * 0.3,
            color=YELLOW
        )
        self.play(Write(title), Create(underline))
        self.wait(1)

        if operation == "addition":
            dot.move_to(number_line.number_to_point(a))
            explanation = f"A dot starts at {a} and jumps forward {b} times."
            jumps = b
            step = 1
        elif operation == "subtraction":
            dot.move_to(number_line.number_to_point(a))
            explanation = f"A dot starts at {a} and jumps backward {b} times."
            jumps = b
            step = -1
        elif operation == "multiplication":
            dot.move_to(number_line.number_to_point(0))
            explanation = f"A dot jumps {a} steps in a single jump. It jumps {b} times."
            jumps = b
            step = a

        explanation_text = Tex(explanation, font_size=35).next_to(number_line, DOWN, buff=1)
        self.play(Write(explanation_text))
        self.wait(1)
        self.play(FadeIn(dot))

        for i in range(jumps):
            start_position = number_line.number_to_point(a + i * step if operation != "multiplication" else i * step)
            end_position = number_line.number_to_point(a + (i + 1) * step if operation != "multiplication" else (i + 1) * step)
            jump_path, dashed_jump_path = self.create_jump_path(start_position, end_position)
            
            self.play(Create(dashed_jump_path), run_time=0.3)
            self.play(MoveAlongPath(dot, jump_path), run_time=0.3)
            self.wait(0.2)

        result_text = self.get_result_text(a, b, operation)
        result = Tex(result_text, font_size=35).next_to(explanation_text, DOWN, buff=0.6)
        self.play(Write(result))
        self.wait(2)
        self.play(FadeOut(dot, title, underline, explanation_text, result))
        self.wait(1)

    def get_result_text(self, a, b, operation):
        if operation == "addition":
            return f"So the dot jumped a total of {a} + {b} = {a+b} steps"
        elif operation == "subtraction":
            return f"So the dot jumped a total of {a} - {b} = {a-b} steps"
        elif operation == "multiplication":
            return f"So the dot jumped a total of {a} * {b} = {a*b} steps"

    def fadeOutCurrentScene(self):
        self.play(*[FadeOut(mob) for mob in self.mobjects])



   
if __name__ == "__main__":
    scene = test1()
    scene.render()