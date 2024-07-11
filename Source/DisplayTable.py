from manim import *

class DisplayTable(Scene):
    def construct(self):
        # Define the table content
        data = [
            ["2 kg of tamarind", "2 kg"],
            ["1 kg of groundnut", "1 kg"],
            ["3 kg of sugar", "2 kg, 1 kg"],
            ["6 kg of onions", "5 kg, 1 kg"],
            ["7 kg of wheat flour", "5 kg, 2 kg"],
            ["13 kg of rice", "10 kg, 2 kg, 1 kg"]
        ]

        # Create the table with headers
        table = Table(
            [["Articles to buy", "Weights used to weigh"]] + data,
            include_outer_lines=True
        )

        # Scale the table for better visibility
        table.scale(0.6)

        # Create the table header and lines separately
        table_header = Table(
            [["Articles to buy", "Weights used to weigh"]],
            include_outer_lines=True
        )
        table_header.scale(0.6)

        # Create the rest of the table separately
        table_content = Table(
            data,
            include_outer_lines=True
        )
        table_content.scale(0.6)
        table_content.next_to(table_header, DOWN, buff=0.1)

        # Position the table header and content at the center of the scene
        table.move_to(ORIGIN)

        # Play the header first
        self.play(Create(table_header))
        self.wait(1)

        # Sequentially play each cell in the table content
        for row in table_content.get_entries():
            for cell in row:
                self.play(FadeIn(cell))
                self.wait(0.5)

        self.wait(2)

# To run the animation
if __name__ == "__main__":
    scene = DisplayTable()
    scene.render()