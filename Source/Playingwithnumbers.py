from manim import *

class EmptyTable(Scene):
    def construct(self):
        # Create and display the title
        title = Text("Empty 3x3 Table").scale(0.7).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Create an empty 3x3 table
        table = Table(
            [["", "", ""],
             ["", "", ""],
             ["", "", ""]],
            include_outer_lines=True
        ).shift(DOWN)

        # Animate the creation of the table
        self.play(Create(table))
        self.wait(2)

if __name__ == "__main__":
    scene = EmptyTable()
    scene.render()
