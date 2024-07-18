from AbstractAnim import AbstractAnim
from manim import *
import cvo


class duplicate(Scene):
    def construct(self):
        # Series with blanks
        sub_title1 = Text("100,  200,  300,_____________________ ", font_size=29).to_edge(UP * 3.5 + LEFT * 4)
        sub_title2 = Text("110,  120,  130,______________________  ", font_size=29).to_edge(UP * 5.75 + LEFT * 4)
        sub_title3 = Text("350,  400,  450,_____________________  ", font_size=29).to_edge(UP * 8 + LEFT * 4)
        heading2 = Text("400,  425,  450,_____________________  ", font_size=30).to_edge(UP * 10.25 + LEFT * 4)
        sub_title5 = Text("900,  800,  700,______________________ ", font_size=30).to_edge(UP * 12.5 + LEFT * 4)


        # Series with answers (positions adjusted to match underscores)
        sub_title1_answer = Text("400,  500,  600,  700,  800", font_size=29, color=BLUE).to_edge(UP * 3.25 + LEFT * 9.75)
        sub_title2_answer = Text("140,  150,  160,  170,  180", font_size=29, color=BLUE).to_edge(UP * 5.55 + LEFT * 9.65)
        sub_title3_answer = Text("500,  550,  600,  650,  700", font_size=29, color=BLUE).to_edge(UP * 7.75 + LEFT * 9.9)
        heading2_answer = Text("475,  500,  525,  550,  575", font_size=29, color=BLUE).to_edge(UP * 10 + LEFT * 10)
        sub_title5_answer = Text("600,   500,  400,  300,  200", font_size=29, color=BLUE).to_edge(UP * 12.25 + LEFT * 10)

        
        # List of all text objects
        texts_to_write = [
            sub_title1, sub_title2, sub_title3, heading2, sub_title5
        ]
        
        # Write all text objects
        for text in texts_to_write:
            self.play(Write(text))
            self.wait(1)

        self.wait(2)

        # "ADD 100" text positioned to the right of the first series
        add_100_text = Text("Add 100", font_size=29, color=GREEN).next_to(sub_title1, RIGHT*2.5)
        # Write the answers individually
        self.play(Write(add_100_text))
        self.wait(1)
        # Fade out the "ADD 100" text
        self.play(FadeOut(add_100_text))
        self.wait(1)
        # Write the answers individually
        self.play(Write(sub_title1_answer))
        self.wait(1)

        add_100_text1 = Text("Add 10", font_size=29, color=GREEN).next_to(sub_title2, RIGHT*2.5)
        self.play(Write(add_100_text1))
        self.wait(1)
        # Fade out the "ADD 100" text
        self.play(FadeOut(add_100_text1))
        self.wait(1)
        self.play(Write(sub_title2_answer))
        self.wait(1)

        add_100_text2 = Text("Add 50", font_size=29, color=GREEN).next_to(sub_title3, RIGHT*2.5)
        self.play(Write(add_100_text2))
        self.wait(1)
        # Fade out the "ADD 100" text
        self.play(FadeOut(add_100_text2))
        self.wait(1)
        self.play(Write(sub_title3_answer))
        self.wait(1)

        add_100_text3 = Text("Add 25", font_size=29, color=GREEN).next_to(heading2, RIGHT*2.5)
        self.play(Write(add_100_text3))
        self.wait(1)
        # Fade out the "ADD 100" text
        self.play(FadeOut(add_100_text3))
        self.wait(1)
        self.play(Write(heading2_answer))
        self.wait(1)

        add_100_text4 = Text("subtract 100", font_size=29, color=GREEN).next_to(sub_title5, RIGHT*2.5)
        self.play(Write(add_100_text4))
        self.wait(1)
         # Fade out the "ADD 100" text
        self.play(FadeOut(add_100_text4))
        self.wait(1)
        self.play(Write(sub_title5_answer))
        self.wait(1)



if __name__ == "__main__":
    from manim import *
    scene = duplicate()
    scene.render()