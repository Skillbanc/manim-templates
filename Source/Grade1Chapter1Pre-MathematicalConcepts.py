from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class Grade1Chapter1(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.premath()
        self.GithubSourceCodeReference()
        self.SubscribeYoutube()
        self.fadeOutCurrentScene()

    def premath(self):
        text=Text("Pre-Mathematical Concepts",font_size=60)
        self.play(Write(text))
        self.wait(1)
        self.fadeOutCurrentScene()

        small_bottle = Text("🍼", font_size=96).shift(LEFT*3)
        large_bottle = Text("🍼", font_size=192).shift(RIGHT*2)
        self.play(Write(small_bottle,run_time=2))
        self.play(Write(large_bottle,run_time=2))
        question = Text("Which is smaller?", color=YELLOW).to_edge(UP)
        self.play(Write(question))
        self.wait(3)
        small_label = Text("This bottle is smaller").next_to(small_bottle, DOWN)
        large_label = Text("Large bottle",font_size=40).next_to(large_bottle, DOWN)
        self.play(Write(small_label))
        self.play(Write(large_label))
        highlight = SurroundingRectangle(small_bottle, color=BLUE, buff=0.1)
        self.play(Create(highlight))
        self.wait(2)
        self.fadeOutCurrentScene()

        parrot = Text("🦜", font_size=96,color=GREEN).shift(LEFT*3)
        bin = Text("🗑️", font_size=192,color=GREY).shift(RIGHT*2)
        self.play(Write(parrot), Write(bin))
        # parrot_label = Text("Parrot").next_to(parrot, DOWN)
        # cage_label = Text("Cage").next_to(cage, DOWN)
        # self.play(Write(parrot_label), Write(cage_label))
        question = Text("Is the parrot inside or outside the bin?", color=RED).to_edge(UP)
        self.play(Write(question))
        self.wait(3)
        self.play(parrot.animate.move_to(bin.get_center()))
        inside_label = Text("Inside").next_to(parrot, UP*3)
        self.play(Write(inside_label))
        self.wait(2)
        self.play(FadeOut(inside_label))
        self.play(parrot.animate.shift(LEFT*4))
        outside_label = Text("Outside").next_to(parrot, UP)
        self.play(Write(outside_label))
        self.wait(2)
        self.fadeOutCurrentScene()

        table=Text("🛏️",font_size=200,color=WHITE)
        ball=Text("⚽",font_size=50,color=BLUE).next_to(table,DOWN,buff=0.5)
        doll=Text("🧸",font_size=50,color=LIGHT_BROWN).next_to(table,UP,buff=0.2)
        self.play(Write(table),Write(ball),Write(doll))
        question = Text("Which object is under the bed?", color=RED).to_edge(UP)
        self.play(Write(question))
        self.wait(4)
        highlight = SurroundingRectangle(ball, color=YELLOW, buff=0.3)
        self.play(Create(highlight))
        self.wait(2)
        text=Text("The ball is under the bed",font_size=30).next_to(ball,RIGHT,buff=0.5)
        self.play(Write(text))
        self.wait(2)
        self.fadeOutCurrentScene()

        chairs1=Text("🪑 🪑 🪑 🪑 🪑 🪑",font_size=60,color=LIGHT_BROWN)
        chairs1.arrange_in_grid(rows=2, cols=3, buff=0.4).shift(LEFT * 3)
        chairs1.add(SurroundingRectangle(chairs1,color=YELLOW))
        self.play(Write(chairs1))
        chairs2=Text("🪑 🪑 🪑 ",font_size=60,color=LIGHT_BROWN)
        chairs2.arrange_in_grid(rows=1, cols=3, buff=0.4).shift(RIGHT * 3)
        chairs2.add(SurroundingRectangle(chairs2,color=YELLOW))
        self.play(Write(chairs2))
        question = Text("Which group has more chairs?", color=RED).to_edge(UP)
        self.play(Write(question))
        self.wait(4)
        highlight = SurroundingRectangle(chairs1, color=BLUE, buff=0.2)
        self.play(Create(highlight))
        text=Text("This group has more chairs",font_size=40).next_to(chairs1,DOWN,buff=1)
        self.play(Write(text))
        self.wait(2)
        self.fadeOutCurrentScene()

        question = Text("Draw the picture of a chocolate, which is bigger than the given one here.", color=BLUE_B,font_size=30).to_edge(UP)
        self.play(Write(question))
        candy=Text("🍬",font_size=80,color=ORANGE).shift(LEFT*4)
        self.play(Write(candy))
        self.wait(4)
        candy1=Text("🍬",font_size=300,color=ORANGE).shift(RIGHT*3)
        self.play(Write(candy1))
        self.wait(2)
        self.fadeOutCurrentScene()

    def SetDeveloperList(self):
        self.DeveloperList="Srujan"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade1Chapter1Pre-MathematicalConcepts.py"

        
if __name__ == "__main__":
    scene = Grade1Chapter1()
    scene.render()