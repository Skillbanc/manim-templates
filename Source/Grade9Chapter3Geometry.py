from manim import *
from numpy import size
from AbstractAnim import AbstractAnim


import cvo

class geometry(AbstractAnim):  
    def construct(self):
        self.RenderSkillbancLogo()
        self.geo()
        self.axiom_1()
        self.axiom_2()
        self.axiom_3()
        self.axiom_4()
        self.axiom_5()
        self.axiom_6()
        self.postulate_1()
        self.postulate_2()
        self.postulate_3()
        self.postulate_4()
        self.postulate_5()
        self.GithubSourceCodeReference()
        

    def geo(self):

        self.isRandom=False

        p1=cvo.CVO().CreateCVO("Building Blocks of Geometry","").setPosition([0,2.5,0])

        p2=cvo.CVO().CreateCVO("point","").setPosition([-4,1,0])
        p1.cvolist.append(p2)

        p3=cvo.CVO().CreateCVO("line","").setPosition([4,1,0])
        p1.cvolist.append(p3)

        p4=cvo.CVO().CreateCVO("Stright line","").setPosition([-4,-1,0])
        p1.cvolist.append(p4)

        p5=cvo.CVO().CreateCVO("surface","").setPosition([4,-1,0])
        p1.cvolist.append(p5)

        p6=cvo.CVO().CreateCVO("plane surface","").setPosition([0,-3,0])
        p1.cvolist.append(p6)

        self.construct1(p1,p1)

        self.fadeOutCurrentScene()

    def axiom_1(self):

        text = Text("AXIOMS").scale(1)
        self.play(Write(text))
        self.wait(1)
        self.fadeOutCurrentScene()

        title = Text("Axiom 1", font_size=36).to_edge(UP)
        description = Text("Things which are equal to the same thing are equal to one another.", font_size=24).next_to(title, DOWN)
        eq1 = MathTex("a = c", font_size=36).shift(UP)
        eq2 = MathTex("b = c", font_size=36).shift(DOWN)
        conclusion = MathTex("\\therefore a = b", font_size=36).next_to(eq2, DOWN)
        self.play(Write(title), Write(description))
        self.play(Write(eq1), Write(eq2))
        self.play(Write(conclusion))
        self.wait(2)
        self.fadeOutCurrentScene()

    def axiom_2(self):
        title = Text("Axiom 2", font_size=36).to_edge(UP)
        description = Text("If equals are added to equals, the wholes are equal.", font_size=24).next_to(title, DOWN)
        eq1 = MathTex("a = b", font_size=36).shift(UP)
        eq2 = MathTex("c = d", font_size=36).shift(DOWN)
        addition = MathTex("a + c = b + d", font_size=36).next_to(eq2, DOWN)
        self.play(Write(title), Write(description))
        self.play(Write(eq1), Write(eq2))
        self.play(Write(addition))
        self.wait(2)
        self.fadeOutCurrentScene()

    def axiom_3(self):
        title = Text("Axiom 3", font_size=36).to_edge(UP)
        description = Text("If equals are subtracted from equals, the remainders are equal.", font_size=24).next_to(title, DOWN)
        eq1 = MathTex("a = b", font_size=36).shift(UP)
        eq2 = MathTex("c = d", font_size=36).shift(DOWN)
        subtraction = MathTex("a - c = b - d", font_size=36).next_to(eq2, DOWN)
        self.play(Write(title), Write(description))
        self.play(Write(eq1), Write(eq2))
        self.play(Write(subtraction))
        self.wait(2)
        self.fadeOutCurrentScene()

    def axiom_4(self):
        title = Text("Axiom 4", font_size=36).to_edge(UP)
        description = Text("Things which coincide with one another are equal to one another.", font_size=24).next_to(title, DOWN)
        square1 = Square().move_to([-2,0,0])
        square2 = Square().move_to([2,0,0])
        self.play(Write(title), Write(description))
        self.play(Create(square1), Create(square2))
        self.play(square2.animate.move_to(square1))
        self.wait(2)
        self.fadeOutCurrentScene()

    def axiom_5(self):
        title = Text("Axiom 5", font_size=36).to_edge(UP)
        description = Text("Things which are double of the same things are equal to one another.", font_size=24).next_to(title, DOWN)
        eq1 = MathTex("a = b", font_size=36).shift(UP)
        double = MathTex("2a = 2b", font_size=36).next_to(eq1, DOWN)
        self.play(Write(title), Write(description))
        self.play(Write(eq1))
        self.play(Write(double))
        self.wait(2)
        self.fadeOutCurrentScene()

    def axiom_6(self):
        title = Text("Axiom 6", font_size=36).to_edge(UP)
        description = Text("Things which are halves of the same things are equal to one another.", font_size=24).next_to(title, DOWN)
        eq1 = MathTex("a = b", font_size=36).shift(UP)
        half = MathTex("\\frac{a}{2} = \\frac{b}{2}", font_size=36).next_to(eq1, DOWN)
        self.play(Write(title), Write(description))
        self.play(Write(eq1))
        self.play(Write(half))
        self.wait(2)
        self.fadeOutCurrentScene()

    def postulate_1(self):

        text = Text("Euclid's Postulates").scale(1)
        self.play(Write(text))
        self.fadeOutCurrentScene()

        title = Text("Euclid's First Postulate", font_size=36).to_edge(UP)
        description = Text("A straight line segment can be drawn joining any two points.", font_size=24).next_to(title, DOWN)
        point_A = Dot(LEFT * 2)
        point_B = Dot(RIGHT * 2)
        label_A = Text("A", font_size=24).next_to(point_A, DOWN)
        label_B = Text("B", font_size=24).next_to(point_B, DOWN)
        line_AB = Line(point_A.get_center(), point_B.get_center())
        self.play(Write(title), Write(description))
        self.wait(1)
        self.play(GrowFromCenter(point_A), GrowFromCenter(point_B))
        self.play(Write(label_A), Write(label_B))
        self.play(Create(line_AB))
        self.wait(2)
        self.fadeOutCurrentScene()

    def postulate_2(self):
        title = Text("Euclid's Second Postulate", font_size=36).to_edge(UP)
        description = Text("A line segment can be extended indefinitely in both directions.", font_size=24).next_to(title, DOWN)
        point_A = Dot(ORIGIN)
        point_B = Dot(RIGHT*2)
        label_A = Text("A", font_size=24).next_to(point_A, DOWN)
        label_B = Text("B", font_size=24).next_to(point_B, DOWN)
        line = Line(LEFT * 4, RIGHT * 4)
        self.play(Write(title), Write(description))
        self.wait(1)
        self.play(GrowFromCenter(point_A),GrowFromCenter(point_B))
        self.play(Write(label_A),Write(label_B))
        self.play(Create(line))
        self.wait(2)
        self.fadeOutCurrentScene()

    def postulate_3(self):
        title = Text("Euclid's Third Postulate", font_size=36).to_edge(UP)
        description = Text("A circle can be drawn with any center and radius.", font_size=24).next_to(title, DOWN)
        center = Dot(ORIGIN)
        label_center = Text("O", font_size=24).next_to(center, DOWN)
        circle = Circle(radius=2)
        self.play(Write(title), Write(description))
        self.wait(1)
        self.play(GrowFromCenter(center))
        self.play(Write(label_center))
        self.play(Create(circle))
        self.wait(2)
        self.fadeOutCurrentScene()

    def postulate_4(self):
        title = Text("Euclid's Fourth Postulate", font_size=36).to_edge(UP)
        description = Text("All right angles are equal to each other.", font_size=24).next_to(title, DOWN)
        right_angle_1 = VGroup(Line(LEFT, RIGHT), Line(LEFT, LEFT + UP)).move_to(LEFT * 2)
        right_angle_2 = VGroup(Line(LEFT, RIGHT), Line(LEFT, LEFT + UP*2)).move_to(RIGHT * 2)
        self.play(Write(title), Write(description))
        self.wait(1)
        self.play(Create(right_angle_1))
        self.play(Create(right_angle_2))
        self.wait(2)
        self.fadeOutCurrentScene()

    def postulate_5(self):
        title = Text("Euclid's Fifth Postulate", font_size=36).to_edge(UP)
        description = Text("If a straight line falling on two straight lines makes the interior angles on the \n\n same side less than two right angles, the two straight lines, if extended indefinitely, meet on that side.", font_size=24).scale(0.7).next_to(title, DOWN)
        

        self.play(Write(title),Write(description))

        line_1 = Line(LEFT * 3, RIGHT * 3)
        line_2 = Line(LEFT * 3 + DOWN , RIGHT * 3 + DOWN * 2)
        transversal = Line(LEFT + DOWN * 2, RIGHT + UP * 2)

        lines = VGroup(line_1, line_2, transversal).scale(0.8)
        self.play(Create(lines))

        angles = [
            Angle(line_1, transversal, radius=0.5, quadrant=(-1,-1), other_angle=False, color=YELLOW),
            Angle(line_2, transversal, radius=0.5, quadrant=(-1,1), other_angle=True, color=GREEN)]
        
        labels = [
            MathTex(r"\angle 1").next_to(angles[0].point_from_proportion(0.5), UP*2 +LEFT, buff=0.2),
            MathTex(r"\angle 2").next_to(angles[1].point_from_proportion(0.5), DOWN*3+ LEFT*2, buff=0.2)]
        
        self.play(Create(VGroup(*angles, *labels)))
        self.wait(2)
        self.fadeOutCurrentScene()

    def SetDeveloperList(self):
        self.DeveloperList="Bhaskar"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade9Chapter3Geometry.py"
      
if __name__ == "__main__":
    scene = geometry()
    scene.render()