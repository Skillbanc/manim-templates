from manim import *
import random

class SBLogoV1(Scene):
    def construct(self):
        self.RenderLOGO()
        
    def RenderLOGO(self):
        # Define colors for dots and circles
        dot_colors = [ORANGE, BLUE, GREEN]
        circle_colors = [ORANGE, DARK_BLUE, GREEN]

        # Create multiple dots appearing randomly from the edges
        num_dots = 100
        dots = VGroup(*[Dot(color=random.choice(dot_colors)) for _ in range(num_dots)])
        self.play(Create(dots))

        # Define animations for random movement of dots
        animations = []
        for _ in range(180):  # 180 frames at 30 fps = 6 seconds
            for dot in dots:
                start_point = random.choice([
                    LEFT * 7 + random.uniform(-3, 3) * UP,
                    RIGHT * 7 + random.uniform(-3, 3) * DOWN,
                    UP * 4 + random.uniform(-5, 5) * RIGHT,
                    DOWN * 4 + random.uniform(-5, 5) * LEFT
                ])
                end_point = random.uniform(-3, 3) * RIGHT + random.uniform(-3, 3) * UP
                animations.append(dot.animate.shift(start_point - dot.get_center()))
                animations.append(dot.animate.shift(end_point - start_point))

        # Play animations for 6 seconds
        self.play(AnimationGroup(*animations))

        # Create circles with different colors
        circles = VGroup(*[Circle(radius=0.5, color=color, fill_color=color, fill_opacity=1) for color in circle_colors])
        circles.arrange(RIGHT, buff=1)
        self.play(Transform(dots, circles))
        # self.play(Transform(circles, dots ))
        # self.play(Transform(dots, circles))
        
        # Define arrow animations with start and end points on the surface of circles
        arrows = VGroup(
            Arrow(circles[0].get_right(), circles[1].get_left(), buff=0.1),
            Arrow(circles[1].get_right(), circles[2].get_left(), buff=0.1),
            CurvedArrow(circles[0].get_top(), circles[2].get_top(), angle=-TAU/4),
            CurvedArrow(circles[0].get_bottom(), circles[2].get_bottom(), angle=TAU/4)
        )

        # Play arrow animations sequentially
        self.play(Create(arrows[0]))
        self.play(Create(arrows[1]))
        self.play(Create(arrows[2]))
        self.play(Create(arrows[3]))
        self.wait(2)

if __name__ == "__main__":
    scene = SBLogoV1()
    scene.render()
