from manim import *

class HorizontalSubtraction(Scene):
    def construct(self):
        # Title
        title = Tex("Horizontal Subtraction").to_edge(UP)
        self.play(Write(title))
        
        # Create squares for each number and symbols
        square1 = self.create_square("4")
        symbol1 = Tex("-").scale(2)
        square2 = self.create_square("1")
        symbol2 = Tex("=").scale(2)
        result_square1 = self.create_square("3")

        # Position squares horizontally
        subtraction1 = VGroup(square1, symbol1, square2, symbol2, result_square1)
        subtraction1.arrange(RIGHT, buff=0.5)
        subtraction1.move_to([0,2,0])

        # Create squares for second subtraction
        square3 = self.create_square("5")
        symbol3 = Tex("-").scale(2)
        square4 = self.create_square("3")
        symbol4 = Tex("=").scale(2)
        result_square2 = self.create_square("2")

        # Position squares for second subtraction horizontally
        subtraction2 = VGroup(square3, symbol3, square4, symbol4, result_square2)
        subtraction2.arrange(RIGHT, buff=0.5)
        subtraction2.move_to([0,0,0])

        # Create squares for third subtraction
        square5 = self.create_square("3")
        symbol5 = Tex("-").scale(2)
        square6 = self.create_square("2")
        symbol6 = Tex("=").scale(2)
        result_square3 = self.create_square("1")

        # Position squares for third subtraction horizontally
        subtraction3 = VGroup(square5, symbol5, square6, symbol6, result_square3)
        subtraction3.arrange(RIGHT, buff=0.5)
        subtraction3.move_to([0,-3,0])

        # Animate creation of all examples
        self.play(Create(subtraction1))
        self.play(Create(subtraction2))
        self.play(Create(subtraction3))
        self.wait(2)

    def create_square(self, number):
        # Create a square with a number inside
        square = Square(side_length=2, color=BLUE, fill_opacity=0.5)
        label = Tex(number).scale(1.5)
        label.move_to(square)
        
        return VGroup(square, label)

if __name__ == "__main__":
    scene = HorizontalSubtraction()
    scene.render()
