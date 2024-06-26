from manim import *

class DisplayText(Scene):
    def construct(self):
        heading = Text("multiplication of numbers").scale(1.0)
        heading.move_to(UP * 3 + LEFT * 3)  # Position on the top-left corner
        self.play(Write(heading))
        self.wait(2)
        # Creating the texts with reduced scale
        text_t_o = Text("T O", color=BLUE).scale(1.0)  # Set "T O" in blue
        text_3_6 = Text("3 6").scale(1.0)
        text_star_3 = Text("* 3").scale(1.0)

        # Arranging the texts vertically with reduced buffer and aligning to the left
        texts_group = VGroup(text_t_o, text_3_6, text_star_3).arrange(DOWN, buff=0.4, aligned_edge=LEFT)

        # Creating the lines with reduced spacing
        line1 = Line(color=WHITE).set_width(text_star_3.get_width()).next_to(text_star_3, DOWN, buff=0.3)
        line2 = Line(color=WHITE).set_width(text_star_3.get_width()).next_to(line1, DOWN, buff=0.3)

        # Combine texts and lines
        display_group = VGroup(texts_group, line1, line2)

        # Aligning everything to the left side
        display_group.move_to(LEFT * 4)

        # Displaying the texts and lines on the screen
        self.play(Write(display_group))
        self.wait(2)
        
         # Create all Text objects
        texts = [
            Text("= 6 ones x 3 = 18 ones = 1 ten + 8 ones"),
            Text("= 3 tens x 3           = 9 tens"),
            Text("= 10 tens + 8 ones"),
            Text("= 100 ones + 8 ones"),
            Text("= 108"),
        ]

        # Additional text to be inserted between two lines
        additional_text = Text("30*3 + 6*3")
        additional_text.scale(0.8)  # Scale down the additional text

        # Scale down all texts uniformly
        for text in texts:
            text.scale(0.8)

        # Insert the additional text between the second and third lines
        texts.insert(2, additional_text)

        # Arrange texts vertically with a specific buffer
        texts_group = VGroup(*texts).arrange(DOWN, buff=0.5)

        # Move texts to the right side of the screen
        texts_group.move_to(RIGHT * 2)

        # Display the texts on the screen
        self.play(Write(texts_group))
        self.wait(2)

if __name__ == "__main__":
    scene = DisplayText()
    scene.render()
