from manim import *
import cvo
from AbstractAnim import AbstractAnim

class TableExamples(Scene):
    def construct(self):
        t0 = Table(
            [["2", "12"],
            ["2", "6"],
            ["3","3"],
            ["","1"]])

        t1 = Table(
            [["2","30"],
            ["3","15"],
            ["5","5"],
            ["","1"]])

        t2 = Table(
            [["3","36"],
            ["3","12"],
            ["2","4"],
            ["2","2"],
            ["","1"]]
        )
        
        g = Group(
            t0,t1,t2
        ).scale(0.6).arrange_in_grid(buff=1)
        self.add(g)

if __name__ == "__main__":
    scene = TableExamples()
    scene.render()