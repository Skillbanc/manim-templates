from manim import *

class coq6Amin(Scene):
    def construct(self):
        # Title for the sequence
        title = Text("Quadrilaterals").scale(0.9)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Function to create and fade quadrilaterals with titles and properties
        def create_and_fade(quadrilateral, title_text, properties_text):
            shape_title = Text(title_text).next_to(quadrilateral, UP)
            properties = Text(properties_text, font_size=24).next_to(quadrilateral, DOWN)
            self.play(Create(quadrilateral), Write(shape_title))
            self.play(Write(properties))
            self.wait(1)
            self.play(FadeOut(quadrilateral), FadeOut(shape_title), FadeOut(properties))

        # Trapezium
        trapezium = Polygon([-2, 0, 0], [2, 0, 0], [1, 2, 0], [-1, 2, 0], color=BLUE)
        trapezium_props = "1 pair parallel sides, 1 pair non-parallel sides"
        create_and_fade(trapezium, "Trapezium", trapezium_props)

        # Parallelogram
        parallelogram = Polygon([-1, 0, 0], [2, 0, 0], [3, 2, 0], [0, 2, 0], color=GREEN)
        parallelogram_props = "Opposite sides parallel and equal, opposite angles equal"
        create_and_fade(parallelogram, "Parallelogram", parallelogram_props)

        # Rectangle
        rectangle = Rectangle(width=4, height=2, color=ORANGE)
        rectangle_props = "Opposite sides equal, all angles 90 degrees"
        create_and_fade(rectangle, "Rectangle", rectangle_props)

        # Square
        square = Square(side_length=2, color=PURPLE)
        square_props = "All sides equal, all angles 90 degrees"
        create_and_fade(square, "Square", square_props)

        # Rhombus
        rhombus = Polygon([-1, 0, 0], [1, 0, 0], [1.5, 2, 0], [-1.5, 2, 0], color=RED)
        rhombus_props = "All sides equal, diagonals bisect angles"
        create_and_fade(rhombus, "Rhombus", rhombus_props)

        # Kite
        kite = Polygon([-1, 0, 0], [1, 0, 0], [0, 2, 0], [0, -2, 0], color=YELLOW)
        kite_props = "Two pairs of adjacent sides equal, diagonals intersect at 90 degrees"
        create_and_fade(kite, "Kite", kite_props)

        # Another Trapezium
        another_trapezium = Polygon([-2, 0, 0], [2, 0, 0], [1, 2, 0], [-1, 2, 0], color=BLUE)
        create_and_fade(another_trapezium, "Trapezium", trapezium_props)

# To render the scene, use the following command in your terminal:
# manim -pql quadrilateral_animation.py QuadrilateralAnimation







if __name__ == "__main__":
    scene = coq6Amin()
    scene.render()
