from AbstractAnim import AbstractAnim
from manim import *


class duplicate(AbstractAnim):
    def construct(self):

        # Title
        title = Text("Places Table", font_size=24)
        title.to_edge(UP)
        self.play(Write(title))

        # Table data
        headers = ["Places", "Ten Crores\n(T. Cr)", "Crores\n(Cr)", "Ten Lakhs\n(T. La)", "Lakhs\n(La)", "Ten Thousands\n(T. Th.)", "Thousands\n(Th.)", "Hundreds\n(H)", "Tens\n(T)", "Ones\n(O)"]
        row1 = ["Number", "10,00,00,000", "1,00,00,000", "10,00,000", "1,00,000", "10,000", "1,000", "100", "10", "1"]
        row2 = ["No. of Digits", "9", "8", "7", "6", "5", "4", "3", "2", "1"]

        # Combine headers and rows
        table_data = [headers, row1, row2]

if __name__ == "__main__":
    from manim import *
    scene = duplicate()
    scene.render()