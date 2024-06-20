from manim import *

class LinesAndAnglesIntroduction(Scene):
    def construct(self):
        self.intro_lines()
        self.wait(1)
        self.clear()
        self.intro_angles()
        self.wait(1)

    def intro_lines(self):
        title = Text("Introduction to Lines", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))
        
        # Parallel lines
        parallel_lines = VGroup(
            Line(start=3*LEFT+UP, end=3*RIGHT+UP),
            Line(start=3*LEFT+DOWN, end=3*RIGHT+DOWN)
        ).set_color(BLUE)
        parallel_text = Text("Parallel Lines", font_size=36).next_to(parallel_lines, UP)
        self.play(Write(parallel_text), Create(parallel_lines))
        self.wait(2)
        self.play(FadeOut(parallel_lines), FadeOut(parallel_text))
        
        # Perpendicular lines
        perpendicular_lines = VGroup(
            Line(start=2*LEFT, end=2*RIGHT),
            Line(start=DOWN, end=UP)
        ).set_color(RED)
        perpendicular_lines.arrange(buff=0).shift(DOWN)
        perpendicular_text = Text("Perpendicular Lines", font_size=36).next_to(perpendicular_lines, UP)
        self.play(Write(perpendicular_text), Create(perpendicular_lines))
        self.wait(2)
        self.play(FadeOut(perpendicular_lines), FadeOut(perpendicular_text))

    def intro_angles(self):
        title = Text("Introduction to Angles", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))
        
        # Right angle
        right_angle = VGroup(
            Line(start=ORIGIN, end=3*RIGHT),
            Line(start=ORIGIN, end=3*UP)
        ).set_color(GREEN)
        right_angle_text = Text("Right Angle (90°)", font_size=36).next_to(right_angle, UP)
        self.play(Write(right_angle_text), Create(right_angle))
        self.wait(2)
        self.play(FadeOut(right_angle), FadeOut(right_angle_text))
        
        # Acute angle
        acute_angle = VGroup(
            Line(start=ORIGIN, end=3*RIGHT),
            Line(start=ORIGIN, end=3*UP).rotate(-PI/6, about_point=ORIGIN)
        ).set_color(PURPLE)
        acute_angle_text = Text("Acute Angle (<90°)", font_size=36).next_to(acute_angle, UP)
        self.play(Write(acute_angle_text), Create(acute_angle))
        self.wait(2)
        self.play(FadeOut(acute_angle), FadeOut(acute_angle_text))
        
        # Obtuse angle
        obtuse_angle = VGroup(
            Line(start=ORIGIN, end=3*RIGHT),
            Line(start=ORIGIN, end=3*UP).rotate(PI/6, about_point=ORIGIN)
        ).set_color(ORANGE)
        obtuse_angle_text = Text("Obtuse Angle (>90°)", font_size=36).next_to(obtuse_angle, UP)
        self.play(Write(obtuse_angle_text), Create(obtuse_angle))
        self.wait(2)
        self.play(FadeOut(obtuse_angle), FadeOut(obtuse_angle_text))

if __name__ == "__main__":
    from manim import *
    scene = LinesAndAnglesIntroduction()
    scene.render()
