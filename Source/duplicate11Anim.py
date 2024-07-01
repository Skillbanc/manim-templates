from AbstractAnim import AbstractAnim
from manim import *


class duplicate11(AbstractAnim):
    def construct(self):

        point = Text("Angle").to_edge(UP*1)
        sub_title1 = Text("Angles are made when corners are formed"'.',font_size=29).to_edge(UP*3.0).shift(LEFT * 3)
        sub_title2 = Text("In the figure imagine two rays say OA and OB"'.',font_size=29).to_edge(UP*4.5).shift(LEFT * 2.7)
        sub_title3 = Text("These two rays have a common end point at O"'.',font_size=29).to_edge(UP*6).shift(LEFT * 2.7)
        sub_title4 = Text("The two rays here are said to form an angle"'.',font_size=29).to_edge(UP*7.5).shift(LEFT * 3)
        sub_title5 = Text("The two rays forming an angle are called the arms"'.',font_size=29).to_edge(UP*9).shift(LEFT * 2.5)
        sub_title6 = Text("Here the two rays OA and OB are two arms"'.',font_size=29).to_edge(UP*10.5).shift(LEFT * 3)
        sub_title7 = Text("O is the vertex of the angle"'.',font_size=29).to_edge(UP*12).shift(LEFT * 4.4)
        sub_title8 = Text("we read it as angle AOB or angle BOA"'.',font_size=29).to_edge(UP*13.5).shift(LEFT * 3.5)
        sub_title9 = Text("it is denoted by ∠AOB or ∠BOA or  simply ∠O"'.',font_size=29).to_edge(UP*15).shift(LEFT * 2.5)


        self.play(Write(point))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)
        self.play(Write(sub_title3))
        self.wait(1)
        self.play(Write(sub_title4))
        self.wait(1)
        self.play(Write(sub_title5))
        self.wait(1)
        self.play(Write(sub_title6))
        self.wait(1)
        self.play(Write(sub_title7))
        self.wait(1)
        self.play(Write(sub_title8))
        self.wait(1)
        self.play(Write(sub_title9))
        
        



        # Define points
        vertex = ORIGIN
        pointA = [3, 2, 0]
        pointB = [3, -2, 0]

        # Create rays
        ray_OA = Line(vertex, pointA, color=BLUE).shift(RIGHT * 3 )
        ray_OB = Line(vertex, pointB, color=GREEN).shift(RIGHT * 3 )

        # Create labels for the rays
        label_OA = MathTex("OA").next_to(ray_OA, UP).shift(UP * -1)
        label_OB = MathTex("OB").next_to(ray_OB, DOWN).shift(DOWN * -1)
        label_O = MathTex("O").next_to(vertex, LEFT).shift(RIGHT * 3 )

        # Create the angle arc
        angle_arc = Arc(
            radius=1,
            start_angle=ray_OA.get_angle(),
            angle=ray_OB.get_angle() - ray_OA.get_angle(),
            color=YELLOW
        ).shift(RIGHT * 3)

        # Create the angle label
        angle_label = MathTex(r"\theta").move_to(angle_arc.point_from_proportion(0.5) + RIGHT * 0.5)

        # Add the rays, labels, and the angle arc to the scene
        self.play(Create(ray_OA), Write(label_OA))
        self.play(Create(ray_OB), Write(label_OB))
        self.play(Write(label_O))
        self.play(Create(angle_arc), Write(angle_label))
        self.wait(2)

if __name__ == "__main__":
    from manim import *
    scene = duplicate11()
    scene.render()