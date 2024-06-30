import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class Class2Chap19RecordAnim(AbstractAnim):

    def construct(self):
        self.stars()
        self.fadeOutCurrentScene()
        self.graph()



    def stars(self):
        # self.play(Write(NumberPlane()))

        tex = Text("Let us look at colour of stars and Count them:",font_size=30)
        tex.move_to([-2.5,3.5,0])
        self.play(Write(tex))

        box1 = Rectangle(height=3,width=8)
        box1.move_to([0,1.5,0])
        self.play(Write(box1))

        s1 = Star(fill_opacity=0.5,color=PINK).scale(0.3)
        s1.move_to([-3.5,2.5,0])
        self.play(Write(s1))

        s2 = Star(fill_opacity=0.5,color=GREEN).scale(0.3)
        s2.move_to([-2.5,2.5,0])
        self.play(Write(s2))

        s3 = Star(fill_opacity=0.5,color=ORANGE).scale(0.3)
        s3.move_to([-1.5,2.5,0])
        self.play(Write(s3))

        s4 = Star(fill_opacity=0.5,color=GREEN).scale(0.3)
        s4.move_to([-0.5,2.5,0])
        self.play(Write(s4))

        s5 = Star(fill_opacity=0.5,color=PINK).scale(0.3)
        s5.move_to([0.5,2.5,0])
        self.play(Write(s5))

        s7 = Star(fill_opacity=0.5,color=ORANGE).scale(0.3)
        s7.move_to([2.5,2.5,0])
        self.play(Write(s7))

        s8 = Star(fill_opacity=0.5,color=GREEN).scale(0.3)
        s8.move_to([3.5,2.5,0])
        self.play(Write(s8))


        s11 = Star(fill_opacity=0.5,color=PINK).scale(0.3)
        s11.move_to([3.5,1.5,0])
        self.play(Write(s11))

        s21 = Star(fill_opacity=0.5,color=GREEN).scale(0.3)
        s21.move_to([2.5,1.5,0])
        self.play(Write(s21))

        s31 = Star(fill_opacity=0.5,color=ORANGE).scale(0.3)
        s31.move_to([1.5,1.5,0])
        self.play(Write(s31))

        s41 = Star(fill_opacity=0.5,color=GREEN).scale(0.3)
        s41.move_to([0.5,1.5,0])
        self.play(Write(s41))

        s51 = Star(fill_opacity=0.5,color=PINK).scale(0.3)
        s51.move_to([-0.5,1.5,0])
        self.play(Write(s51))

        s71 = Star(fill_opacity=0.5,color=ORANGE).scale(0.3)
        s71.move_to([-2.5,1.5,0])
        self.play(Write(s71))

        s81 = Star(fill_opacity=0.5,color=GREEN).scale(0.3)
        s81.move_to([-3.5,1.5,0])
        self.play(Write(s81))

        s12 = Star(fill_opacity=0.5,color=PINK).scale(0.3)
        s12.move_to([-3.5,0.5,0])
        self.play(Write(s12))

        s22 = Star(fill_opacity=0.5,color=GREEN).scale(0.3)
        s22.move_to([-2.5,0.5,0])
        self.play(Write(s22))

        s32 = Star(fill_opacity=0.5,color=ORANGE).scale(0.3)
        s32.move_to([-1.5,0.5,0])
        self.play(Write(s32))

        s42 = Star(fill_opacity=0.5,color=GREEN).scale(0.3)
        s42.move_to([-0.5,0.5,0])
        self.play(Write(s42))

        s52 = Star(fill_opacity=0.5,color=PINK).scale(0.3)
        s52.move_to([0.5,0.5,0])
        self.play(Write(s52))

        s62 = Star(fill_opacity=0.5,color=GREEN).scale(0.3)
        s62.move_to([1.5,0.5,0])
        self.play(Write(s62))

        s72 = Star(fill_opacity=0.5,color=ORANGE).scale(0.3)
        s72.move_to([2.5,0.5,0])
        self.play(Write(s72))

        s82 = Star(fill_opacity=0.5,color=GREEN).scale(0.3)
        s82.move_to([3.5,0.5,0])
        self.play(Write(s82))


        tab = Table(
            [["Pink","6"],
            ["Green","10"],["Orange","6"]],
            col_labels=[Text("Colour of the star"), Text("Number of stars")],
            include_outer_lines=True,
            arrange_in_grid_config={"cell_alignment": LEFT})
        tab.move_to([-0,-2,0])
        tab.scale(0.5)
        self.play(Create(tab))
        self.wait(2)

    def graph(self):

        data = [0, 6, 3, 5]
        labels = ["0", "A", "B", "C"]
        colors = [RED, GREEN, BLUE, YELLOW]

        # Create axes
        axes = Axes(
            x_range=[0, len(data), 1],
            y_range=[0, max(data) + 2, 1],
            axis_config={"color": WHITE},
            tips=False,
        ).add_coordinates()

        # Manually add labels for axes
        x_axis_label = Text("x-axis", font_size=16, color=WHITE).next_to(axes.x_axis.get_end(), DOWN)
        y_axis_label = Text("y-axis", font_size=16, color=WHITE).next_to(axes.y_axis.get_end(), LEFT)
        yaxislabel = Text("values", font_size=16, color=WHITE).next_to(axes.y_axis.get_center(), LEFT)
        xaxislabel = Text("categories", font_size=16, color=WHITE).next_to(axes.x_axis.get_center(), DOWN)

        y_axis_label.shift(LEFT*0.25)
        xaxislabel.shift(DOWN*0.1)

        # Create bars and labels
        bars = VGroup()
        bar_labels = VGroup()

        for i, value in enumerate(data):
            bar = Rectangle(
                width=0.8,
                height=value,
                fill_color=colors[i],
                fill_opacity=0.8,
                stroke_width=0
            ).move_to(axes.c2p(i, 0), aligned_edge=DOWN)
            bars.add(bar)

            # Label for each bar
            bar_label = Text(labels[i], font_size=16, color=WHITE).next_to(bar, UP)
            bar_labels.add(bar_label)

        # Add a title
        title = Text("Bar Graph Example", font_size=24).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Display elements
        self.play(Create(axes), Write(x_axis_label), Write(y_axis_label))
        self.play(*[Create(bar) for bar in bars])
        self.play(*[Write(label) for label in bar_labels])
        self.play(Write(xaxislabel),Write(yaxislabel))
        
        self.wait(2)

        








if __name__ == "__main__":
    scene = Class2Chap19RecordAnim()
    scene.render()    