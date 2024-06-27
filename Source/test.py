from AbstractAnim import AbstractAnim
import cvo
from manim import *

class MoveImageeee(AbstractAnim):
    def construct(self):
        self.construct1()

        
    def construct1(self):
        title = Text("Find the Distance Between Buildings A and C", font_size=48).to_edge(UP)
        self.play(Write(title))

        # Define scale factor for visualization
        scale_factor = 0.05  # Adjusted to keep all buildings on screen

        # Define building parameters
        building_height_m = 20
        building_width_m = 10
        building_color = BLUE

        def create_building(height, width, color, label):
            building = Rectangle(height=height * scale_factor, width=width * scale_factor, color=color, fill_opacity=1)
            windows = VGroup()
            for y in range(0, height, 2):  # Windows every 2 meters
                for x in range(-width // 2 + 1, width // 2):
                    window = Rectangle(height=1 * scale_factor, width=1 * scale_factor, color=WHITE, fill_opacity=0.7)
                    window.move_to(building.get_bottom() + UP * (y * scale_factor + 1 * scale_factor) + RIGHT * (x * scale_factor))
                    windows.add(window)
            building_label = Text(label, font_size=24).next_to(building, DOWN)
            return VGroup(building, windows, building_label)

        # Create buildings with windows
        building_left = create_building(building_height_m, building_width_m, building_color, "A")
        building_middle = create_building(building_height_m, building_width_m, building_color, "B")
        building_right = create_building(building_height_m, building_width_m, building_color, "C")

        # Position buildings
        building_middle.move_to(ORIGIN)
        building_left.next_to(building_middle, LEFT*0.7, buff=9.0)  # Adjusted buffer to keep left building on screen
        building_right.next_to(building_middle, RIGHT*0.5, buff=7.5)  # 150 m distance

        # Animate buildings appearing
        self.play(FadeIn(building_left), FadeIn(building_middle), FadeIn(building_right))
        self.wait(1)

        # Create distance labels
        distance_450m = Tex("450 m", font_size=24).move_to(midpoint(building_left[0].get_right(), building_middle[0].get_left())).shift(UP * 0.5)
        distance_150m = Tex("150 m", font_size=24).move_to(midpoint(building_middle[0].get_right(), building_right[0].get_left())).shift(UP * 0.5)

        # Create distance lines
        distance_line_450m = Line(start=building_left[0].get_right(), end=building_middle[0].get_left())
        distance_line_150m = Line(start=building_middle[0].get_right(), end=building_right[0].get_left())

        # Animate distance labels and lines
        self.play(Create(distance_line_450m), Write(distance_450m))
        self.wait(1)
        self.play(Create(distance_line_150m), Write(distance_150m))
        self.wait(1)

        # Create and show the addition
        addition_450 = Tex("450 m", font_size=36).to_edge(LEFT).shift(DOWN * 2)
        plus_sign = Tex("+", font_size=36).next_to(addition_450, RIGHT, buff=0.5)
        addition_150 = Tex("150 m", font_size=36).next_to(plus_sign, RIGHT, buff=0.5)
        equals_sign = Tex("=", font_size=36).next_to(addition_150, RIGHT, buff=0.5)
        result_600 = Tex("600 m", font_size=36).next_to(equals_sign, RIGHT, buff=0.5)
        self.play(Write(addition_450), Write(plus_sign), Write(addition_150), Write(equals_sign), Write(result_600))
        self.wait(2)

        # Create the total distance line
        total_distance_line = Line(start=building_left.get_left(), end=building_right.get_right()).next_to(equals_sign,DOWN)
        total_distance_label = Tex("600 m", font_size=24).next_to(total_distance_line, DOWN, buff=0.1)

        # Animate the total distance line
        self.play(Create(total_distance_line), Write(total_distance_label))
        self.wait(2)

        # Fade out all elements
        all_elements = VGroup(addition_450, plus_sign, addition_150, equals_sign, result_600, total_distance_line, total_distance_label,total_distance_label, total_distance_line)
        self.play(FadeOut(all_elements))
        self.wait(1)

def midpoint(p1, p2):
    return (p1 + p2) / 2

# To render the scene
if __name__ == "__main__":
    scene = MoveImageeee()
    scene.render()
