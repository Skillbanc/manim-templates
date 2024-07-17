from manim import *

class DisplayText(Scene):
    def construct(self):
        # Create all Text objects
        texts = [
            Text("= 30 + 6"),
            Text("= * 3"),
            Text("= 90 + 18"),
            Text("= 90 + 10 + 8"),
            Text("= 100 + 8"),
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
        texts_group.move_to(RIGHT * 4)

        # Display the texts on the screen
        self.play(Write(texts_group))
        self.wait(2)

if __name__ == "__main__":
    scene = DisplayText()
    scene.render()
