from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class NUM10to20(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.ten()
        self.above10()
        self.GithubSourceCodeReference()
        self.SubscribeYoutube()
        self.fadeOutCurrentScene()
        
    def ten(self):
        p1=cvo.CVO().CreateCVO("Number:10","").setPosition([0,2.5,0])
        p2=cvo.CVO().CreateCVO("10 is the smallest two digit number","You write the number 10 using the digits 1 and 0").setPosition([0,0,0])
        p1.cvolist.append(p2)
        self.construct1(p1,p1)
        self.wait(1)
        self.fadeOutCurrentScene()

        text = Text("Group of 10 objects", font_size=60,color=ORANGE)
        self.play(Write(text))
        self.play(text.animate.shift(UP * 3))

        text = Text("10 sticks", font_size=40,color=DARK_BROWN)
        self.play(Write(text))
        self.play(text.animate.shift(LEFT * 3))

        text = Text("10 balls", font_size=40,color=YELLOW)
        self.play(Write(text))
        self.play(text.animate.shift(RIGHT * 3))
        
        sticks = VGroup(*[Line(ORIGIN, UP,color=DARK_BROWN).scale(1.5) for _ in range(10)])
        sticks.arrange(RIGHT, buff=0.5)
        bundle = VGroup(*[Line(ORIGIN, UP,color=DARK_BROWN).scale(1.5) for _ in range(10)])
        bundle.arrange(RIGHT, buff=0.2)
        bundle.add(SurroundingRectangle(bundle, color=BLUE))
        
        balls = VGroup(*[Circle(color=YELLOW).scale(0.3) for _ in range(10)])
        balls.arrange_in_grid(rows=2, cols=5, buff=0.5)
        bundle1 = VGroup(*[Circle(color=YELLOW).scale(0.3) for _ in range(10)])
        bundle1.arrange_in_grid(rows=2, cols=5, buff=0.2)
        bundle1.add(SurroundingRectangle(bundle1, color=RED))
        
        sticks_group = VGroup(sticks, bundle).arrange(DOWN, buff=1)
        
        flowers_group = VGroup(balls, bundle1).arrange(DOWN, buff=1)
        all_groups = VGroup(sticks_group, flowers_group).arrange(RIGHT, buff=2)
        
        self.play(LaggedStart(*[Write(stick) for stick in sticks], lag_ratio=0.1))
        self.play(Transform(sticks, bundle))
        
        self.wait(1)
        
        self.play(LaggedStart(*[Write(ball) for ball in balls], lag_ratio=0.1))
        self.play(Transform(balls, bundle1))
        
        self.wait(1)
        self.fadeOutCurrentScene()

    def above10(self):
        text = Text("Numbers above 10", font_size=60)
        self.play(Write(text))
        self.fadeOutCurrentScene()

        text = Text("ELEVEN : 11", font_size=60)
        self.play(Write(text))
        self.play(text.animate.shift(UP * 3))
        ten_circles = VGroup(*[Circle(radius=0.5, color=BLUE).scale(0.5) for _ in range(10)])
        ten_circles.arrange_in_grid(rows=2, cols=5, buff=0.5).shift(LEFT * 3)
        ten_circles.add(SurroundingRectangle(ten_circles,color=YELLOW))
        ten_label = Text("10", font_size=72).next_to(ten_circles, DOWN)
        one_circle = Circle(radius=0.5, color=RED).shift(RIGHT * 5).scale(0.5)
        one_label = Text("1", font_size=72).next_to(one_circle,DOWN)
        eleven_label = Text("11", font_size=72).to_edge(DOWN)
        self.play(LaggedStart(*[Write(circle) for circle in ten_circles], lag_ratio=0.1))
        self.play(Write(ten_label))
        plus_sign = Text("+", font_size=72).next_to(ten_circles, RIGHT, buff=1)
        self.play(Write(plus_sign))
        self.wait(1)
        self.play(Write(one_circle), Write(one_label))
        self.wait(1)
        self.play(Write(eleven_label))
        self.wait(1)
        self.play(Indicate(eleven_label, scale_factor=1.5))
        self.wait(1)
        self.fadeOutCurrentScene()

        text = Text("TWELVE : 12", font_size=60)
        self.play(Write(text))
        self.play(text.animate.shift(UP * 3))
        ten_circles = VGroup(*[Circle(radius=0.5, color=BLUE).scale(0.5) for _ in range(10)])
        ten_circles.arrange_in_grid(rows=2, cols=5, buff=0.5).shift(LEFT * 3)
        ten_circles.add(SurroundingRectangle(ten_circles,color=YELLOW))
        ten_label = Text("10", font_size=72).next_to(ten_circles, DOWN)
        two_circles = VGroup(*[Circle(radius=0.5, color=RED).scale(0.5) for _ in range(2)])
        two_circles.arrange(RIGHT, buff=0.5)
        two_circles.next_to(plus_sign, RIGHT, buff=1)
        two_label = Text("2", font_size=72).move_to(two_circles.get_center() + DOWN * 0.75)
        twelve_label = Text("12", font_size=72).to_edge(DOWN)
        self.play(LaggedStart(*[Write(circle) for circle in ten_circles], lag_ratio=0.1))
        self.play(Write(ten_label))
        plus_sign = Text("+", font_size=72).next_to(ten_circles, RIGHT, buff=1)
        self.play(Write(plus_sign))
        self.wait(1)
        self.play(LaggedStart(*[Write(circle) for circle in two_circles], lag_ratio=0.1))
        self.play(Write(two_label))
        self.wait(1)
        self.play(Write(twelve_label))
        self.wait(1)
        self.play(Indicate(twelve_label, scale_factor=1.5))
        self.wait(1)
        self.fadeOutCurrentScene()

        text = Text("THIRTEEN : 13", font_size=60)
        self.play(Write(text))
        self.play(text.animate.shift(UP * 3))
        ten_circles = VGroup(*[Circle(radius=0.5, color=BLUE).scale(0.5) for _ in range(10)])
        ten_circles.arrange_in_grid(rows=2, cols=5, buff=0.5).shift(LEFT * 3)
        ten_circles.add(SurroundingRectangle(ten_circles,color=YELLOW))
        ten_label = Text("10", font_size=72).next_to(ten_circles, DOWN)
        three_circles = VGroup(*[Circle(radius=0.5, color=RED).scale(0.5) for _ in range(3)])
        three_circles.arrange(RIGHT, buff=0.5)
        three_circles.next_to(plus_sign, RIGHT, buff=1)
        three_label = Text("3", font_size=72).move_to(three_circles.get_center() + DOWN * 0.75)
        thirteen_label = Text("13", font_size=72).to_edge(DOWN)
        self.play(LaggedStart(*[Write(circle) for circle in ten_circles], lag_ratio=0.1))
        self.play(Write(ten_label))
        plus_sign = Text("+", font_size=72).next_to(ten_circles, RIGHT, buff=1)
        self.play(Write(plus_sign))
        self.wait(1)
        self.play(LaggedStart(*[Write(circle) for circle in three_circles], lag_ratio=0.1))
        self.play(Write(three_label))
        self.wait(1)
        self.play(Write(thirteen_label))
        self.wait(1)
        self.play(Indicate(thirteen_label, scale_factor=1.5))
        self.wait(1)
        self.fadeOutCurrentScene()

        text = Text("FOURTEEN : 14 ", font_size=60)
        self.play(Write(text))
        self.play(text.animate.shift(UP * 3))
        ten_circles = VGroup(*[Circle(radius=0.5, color=BLUE).scale(0.5) for _ in range(10)])
        ten_circles.arrange_in_grid(rows=2, cols=5, buff=0.5).shift(LEFT * 3)
        ten_circles.add(SurroundingRectangle(ten_circles,color=YELLOW))
        ten_label = Text("10", font_size=72).next_to(ten_circles, DOWN)
        four_circles = VGroup(*[Circle(radius=0.5, color=RED).scale(0.5) for _ in range(4)])
        four_circles.arrange_in_grid(rows=2, cols=2, buff=0.5)
        four_circles.next_to(plus_sign, RIGHT, buff=1)
        four_label = Text("4", font_size=72).next_to(four_circles, DOWN)
        fourteen_label = Text("14", font_size=72).to_edge(DOWN)
        self.play(LaggedStart(*[Write(circle) for circle in ten_circles], lag_ratio=0.1))
        self.play(Write(ten_label))
        plus_sign = Text("+", font_size=72).next_to(ten_circles, RIGHT, buff=1)
        self.play(Write(plus_sign))
        self.wait(1)
        self.play(LaggedStart(*[Write(circle) for circle in four_circles], lag_ratio=0.1))
        self.play(Write(four_label))
        self.wait(1)
        self.play(Write(fourteen_label))
        self.wait(1)
        self.play(Indicate(fourteen_label, scale_factor=1.5))
        self.wait(1)
        self.fadeOutCurrentScene()
        
        text = Text("FIFTEEN : 15", font_size=60)
        self.play(Write(text))
        self.play(text.animate.shift(UP * 3))
        ten_circles = VGroup(*[Circle(radius=0.5, color=BLUE).scale(0.5) for _ in range(10)])
        ten_circles.arrange_in_grid(rows=2, cols=5, buff=0.5).shift(LEFT * 3)
        ten_circles.add(SurroundingRectangle(ten_circles,color=YELLOW))
        ten_label = Text("10", font_size=72).next_to(ten_circles, DOWN)
        five_circles = VGroup(*[Circle(radius=0.5, color=RED).scale(0.5) for _ in range(5)])
        five_circles.arrange_in_grid(rows=2, cols=3, buff=0.5)
        five_circles.next_to(plus_sign, RIGHT, buff=1)
        five_label = Text("5", font_size=72).next_to(five_circles, DOWN)
        fifteen_label = Text("15", font_size=72).to_edge(DOWN)
        self.play(LaggedStart(*[Write(circle) for circle in ten_circles], lag_ratio=0.1))
        self.play(Write(ten_label))
        plus_sign = Text("+", font_size=72).next_to(ten_circles, RIGHT, buff=1)
        self.play(Write(plus_sign))
        self.wait(1)
        self.play(LaggedStart(*[Write(circle) for circle in five_circles], lag_ratio=0.1))
        self.play(Write(five_label))
        self.wait(1)
        self.play(Write(fifteen_label))
        self.wait(1)
        self.play(Indicate(fifteen_label, scale_factor=1.5))
        self.wait(1)
        self.fadeOutCurrentScene()

        text = Text("SIXTEEN : 16", font_size=60)
        self.play(Write(text))
        self.play(text.animate.shift(UP * 3))
        ten_circles = VGroup(*[Circle(radius=0.5, color=BLUE).scale(0.5) for _ in range(10)])
        ten_circles.arrange_in_grid(rows=2, cols=5, buff=0.5).shift(LEFT * 3)
        ten_circles.add(SurroundingRectangle(ten_circles,color=YELLOW))
        ten_label = Text("10", font_size=72).next_to(ten_circles, DOWN)
        six_circles = VGroup(*[Circle(radius=0.5, color=RED).scale(0.5) for _ in range(6)])
        six_circles.arrange_in_grid(rows=2, cols=3, buff=0.5)
        six_circles.next_to(plus_sign, RIGHT, buff=1)
        six_label = Text("6", font_size=72).next_to(six_circles, DOWN)
        sixteen_label = Text("16", font_size=72).to_edge(DOWN)
        self.play(LaggedStart(*[Write(circle) for circle in ten_circles], lag_ratio=0.1))
        self.play(Write(ten_label))
        plus_sign = Text("+", font_size=72).next_to(ten_circles, RIGHT, buff=1)
        self.play(Write(plus_sign))
        self.wait(1)
        self.play(LaggedStart(*[Write(circle) for circle in six_circles], lag_ratio=0.1))
        self.play(Write(six_label))
        self.wait(1)
        self.play(Write(sixteen_label))
        self.wait(1)
        self.play(Indicate(sixteen_label, scale_factor=1.5))
        self.wait(1)
        self.fadeOutCurrentScene()


        text = Text("SEVENTEEN : 17", font_size=60)
        self.play(Write(text))
        self.play(text.animate.shift(UP * 3))
        ten_circles = VGroup(*[Circle(radius=0.5, color=BLUE).scale(0.5) for _ in range(10)])
        ten_circles.arrange_in_grid(rows=2, cols=5, buff=0.5).shift(LEFT * 3)
        ten_circles.add(SurroundingRectangle(ten_circles,color=YELLOW))
        ten_label = Text("10", font_size=72).next_to(ten_circles, DOWN)
        seven_circles = VGroup(*[Circle(radius=0.5, color=RED).scale(0.5) for _ in range(7)])
        seven_circles.arrange_in_grid(rows=2, cols=4, buff=0.5)
        seven_circles.next_to(plus_sign, RIGHT, buff=1)
        seven_label = Text("7", font_size=72).next_to(seven_circles, DOWN)
        seventeen_label = Text("17", font_size=72).to_edge(DOWN)
        self.play(LaggedStart(*[Write(circle) for circle in ten_circles], lag_ratio=0.1))
        self.play(Write(ten_label))
        plus_sign = Text("+", font_size=72).next_to(ten_circles, RIGHT, buff=1)
        self.play(Write(plus_sign))
        self.wait(1)
        self.play(LaggedStart(*[Write(circle) for circle in seven_circles], lag_ratio=0.1))
        self.play(Write(seven_label))
        self.wait(1)
        self.play(Write(seventeen_label))
        self.wait(1)
        self.play(Indicate(seventeen_label, scale_factor=1.5))
        self.wait(1)
        self.fadeOutCurrentScene()
        

        text = Text("EIGHTEEN : 18", font_size=60)
        self.play(Write(text))
        self.play(text.animate.shift(UP * 3))
        ten_circles = VGroup(*[Circle(radius=0.5, color=BLUE).scale(0.5) for _ in range(10)])
        ten_circles.arrange_in_grid(rows=2, cols=5, buff=0.5).shift(LEFT * 3)
        ten_circles.add(SurroundingRectangle(ten_circles,color=YELLOW))
        ten_label = Text("10", font_size=72).next_to(ten_circles, DOWN)
        eight_circles = VGroup(*[Circle(radius=0.5, color=RED).scale(0.5) for _ in range(8)])
        eight_circles.arrange_in_grid(rows=2, cols=4, buff=0.5)
        eight_circles.next_to(plus_sign, RIGHT, buff=1)
        eight_label = Text("8", font_size=72).next_to(eight_circles, DOWN)
        eighteen_label = Text("18", font_size=72).to_edge(DOWN)
        self.play(LaggedStart(*[Write(circle) for circle in ten_circles], lag_ratio=0.1))
        self.play(Write(ten_label))
        plus_sign = Text("+", font_size=72).next_to(ten_circles, RIGHT, buff=1)
        self.play(Write(plus_sign))
        self.wait(1)
        self.play(LaggedStart(*[Write(circle) for circle in eight_circles], lag_ratio=0.1))
        self.play(Write(eight_label))
        self.wait(1)
        self.play(Write(eighteen_label))
        self.wait(1)
        self.play(Indicate(eighteen_label, scale_factor=1.5))
        self.wait(1)
        self.fadeOutCurrentScene()

        text = Text("NINETEEN : 19", font_size=60)
        self.play(Write(text))
        self.play(text.animate.shift(UP * 3))
        ten_circles = VGroup(*[Circle(radius=0.5, color=BLUE).scale(0.5) for _ in range(10)])
        ten_circles.arrange_in_grid(rows=2, cols=5, buff=0.5).shift(LEFT * 3)
        ten_circles.add(SurroundingRectangle(ten_circles,color=YELLOW))
        ten_label = Text("10", font_size=72).next_to(ten_circles, DOWN)
        nine_circles = VGroup(*[Circle(radius=0.5, color=RED).scale(0.5) for _ in range(9)])
        nine_circles.arrange_in_grid(rows=2, cols=5, buff=0.5)
        nine_circles.next_to(plus_sign, RIGHT, buff=1)
        nine_label = Text("9", font_size=72).next_to(nine_circles, DOWN)
        nineteen_label = Text("19", font_size=72).to_edge(DOWN)
        self.play(LaggedStart(*[Write(circle) for circle in ten_circles], lag_ratio=0.1))
        self.play(Write(ten_label))
        plus_sign = Text("+", font_size=72).next_to(ten_circles, RIGHT, buff=1)
        self.play(Write(plus_sign))
        self.wait(1)
        self.play(LaggedStart(*[Write(circle) for circle in nine_circles], lag_ratio=0.1))
        self.play(Write(nine_label))
        self.wait(1)
        self.play(Write(nineteen_label))
        self.wait(1)
        self.play(Indicate(nineteen_label, scale_factor=1.5))
        self.wait(1)
        self.fadeOutCurrentScene()

        text = Text("TWENTY : 20", font_size=60)
        self.play(Write(text))
        self.play(text.animate.shift(UP * 3))
        ten_circles = VGroup(*[Circle(radius=0.5, color=BLUE).scale(0.5) for _ in range(10)])
        ten_circles.arrange_in_grid(rows=2, cols=5, buff=0.4).shift(LEFT * 3)
        ten_circles.add(SurroundingRectangle(ten_circles,color=YELLOW))
        ten_label = Text("10", font_size=72).next_to(ten_circles, DOWN)
        ten1_circles = VGroup(*[Circle(radius=0.5, color=RED).scale(0.5) for _ in range(10)])
        ten1_circles.arrange_in_grid(rows=2, cols=5, buff=0.4)
        ten1_circles.add(SurroundingRectangle(ten1_circles,color=YELLOW))
        ten1_circles.next_to(plus_sign, RIGHT, buff=0.8)
        ten1_label = Text("10", font_size=72).next_to(ten1_circles, DOWN)
        twenty_label = Text("20", font_size=72).to_edge(DOWN)
        self.play(LaggedStart(*[Write(circle) for circle in ten_circles], lag_ratio=0.1))
        self.play(Write(ten_label))
        plus_sign = Text("+", font_size=72).next_to(ten_circles, RIGHT, buff=1)
        self.play(Write(plus_sign))
        self.wait(1)
        self.play(LaggedStart(*[Write(circle) for circle in ten1_circles], lag_ratio=0.1))
        self.play(Write(ten1_label))
        self.wait(1)
        self.play(Write(twenty_label))
        self.wait(1)
        self.play(Indicate(twenty_label, scale_factor=1.5))
        self.wait(1)
        self.fadeOutCurrentScene()

    def SetDeveloperList(self):
        self.DeveloperList="Srujan"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade1Chapter9NumbersFrom10to20.py"


if __name__ == "__main__":
    scene = NUM10to20()
    scene.render()