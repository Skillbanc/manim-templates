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
        exp = Text("Explanation: If two things (let's call them A and B) are each equal to a third thing (let's call it C),\n\n then A and B are equal to each other.", font_size=22).next_to(description,DOWN)
        eq1 = MathTex("A = C", font_size=36).next_to(exp,DOWN)
        eq2 = MathTex("B = C", font_size=36).next_to(eq1, DOWN)
        conclusion = MathTex("\\therefore A = B", font_size=36).next_to(eq2, DOWN)
        self.play(Write(title))
        self.play(Write(description))
        self.play(Write(exp))
        self.play(Write(eq1), Write(eq2))
        self.play(Write(conclusion))
        self.wait(3)
        self.fadeOutCurrentScene()

    def axiom_2(self):
        title = Text("Axiom 2", font_size=36).to_edge(UP)
        description = Text("If equals are added to equals, the wholes are equal.", font_size=24).next_to(title, DOWN)
        exp = Text("Explanation: If you have two pairs of equal quantities and you add one quantity from each pair together,\n\n the resulting sums will also be equal.", font_size=22).next_to(description,DOWN)
        eq1 = MathTex("A = B", font_size=36).next_to(exp,DOWN)
        eq2 = MathTex("C = D", font_size=36).next_to(eq1,DOWN)
        addition = MathTex("\\therefore A + C = B + D", font_size=36).next_to(eq2, DOWN)
        
        self.play(Write(title))
        self.play(Write(description))
        self.play(Write(exp))
        self.play(Write(eq1), Write(eq2))
        self.play(Write(addition))
        self.wait(3)
        self.fadeOutCurrentScene()

    def axiom_3(self):
        title = Text("Axiom 3", font_size=36).to_edge(UP)
        description = Text("If equals are subtracted from equals, the remainders are equal.", font_size=24).next_to(title, DOWN)
        exp = Text("Explanation: If you have two pairs of equal quantities and you subtract one quantity from each pair,\n\n the resulting differences will also be equal.", font_size=22).next_to(description,DOWN)

        eq1 = MathTex(" A= B", font_size=36).next_to(exp,DOWN)
        eq2 = MathTex("C = D", font_size=36).next_to(eq1,DOWN)
        subtraction = MathTex("A - C = B - D", font_size=36).next_to(eq2, DOWN)
        self.play(Write(title))
        self.play(Write(description))
        self.play(Write(exp))
        self.play(Write(eq1), Write(eq2))
        self.play(Write(subtraction))
        self.wait(3)
        self.fadeOutCurrentScene()

    def axiom_4(self):
        title = Text("Axiom 4", font_size=36).to_edge(UP)
        description = Text("Things which coincide with one another are equal to one another.", font_size=24).next_to(title, DOWN)
        exp = Text("Explanation: If two things perfectly match or overlap each other in all aspects, \n\nthen they are considered equal.", font_size=22).next_to(description,DOWN)

        square1 = Square().move_to([-2,0,0])
        square2 = Square().move_to([2,0,0])
        self.play(Write(title))
        self.play(Write(description))
        self.play(Write(exp))
        self.play(Create(square1), Create(square2))
        self.play(square2.animate.move_to(square1))
        self.wait(3)
        self.fadeOutCurrentScene()

    def axiom_5(self):
        title = Text("Axiom 5", font_size=36).to_edge(UP)
        description = Text("Things which are double of the same things are equal to one another.", font_size=24).next_to(title, DOWN)
        exp = Text("Explanation: If you have two quantities that are each twice as large as the same quantity,\n\n then those two quantities are equal to each other.", font_size=22).next_to(description,DOWN)

        eq1 = MathTex("A = B", font_size=36).next_to(exp,DOWN)
        double = MathTex("2A = 2B", font_size=36).next_to(eq1, DOWN)
        self.play(Write(title))
        self.play(Write(description))
        self.play(Write(exp))
        self.play(Write(eq1))
        self.play(Write(double))
        self.wait(3)
        self.fadeOutCurrentScene()

    def axiom_6(self):
        title = Text("Axiom 6", font_size=36).to_edge(UP)
        description = Text("Things which are halves of the same things are equal to one another.", font_size=24).next_to(title, DOWN)
        exp = Text("Explanation: If you have two quantities that are each half of the same quantity,\n\n then those two quantities are equal to each other.", font_size=22).next_to(description,DOWN)
        eq1 = MathTex("A = B", font_size=36).next_to(exp,DOWN)
        half = MathTex("\\frac{A}{2} = \\frac{B}{2}", font_size=36).next_to(eq1, DOWN)
        self.play(Write(title))
        self.play(Write(description))
        self.play(Write(exp))
        self.play(Write(eq1))
        self.play(Write(half))
        self.wait(3)
        self.fadeOutCurrentScene()

    def postulate_1(self):

        text = Text("Euclid's Postulates").scale(1)
        self.play(Write(text))
        self.fadeOutCurrentScene()

        title = Text("Euclid's First Postulate", font_size=36).to_edge(UP)
        description = Text("There is a unique line that passes through the given two distinct points.", font_size=24).next_to(title, DOWN)
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
        description = Text("A line segment can be extended on either side to form a line.", font_size=24).next_to(title, DOWN)
        point_A = Dot(LEFT)
        point_B = Dot(RIGHT)
        label_A = Text("A", font_size=24).next_to(point_A, DOWN)
        label_B = Text("B", font_size=24).next_to(point_B, DOWN)
        line = Line(point_A, point_B)
        line_1 = Line(point_A,LEFT * 3)
        line_2 = Line(point_B, RIGHT *3)
        self.play(Write(title))
        self.play(Write(description))
        self.wait(1)
        self.play(GrowFromCenter(point_A),GrowFromCenter(point_B))
        self.play(Write(label_A),Write(label_B))
        self.play(Create(line))
        self.wait(1)
        self.play(Create(line_1),Create(line_2))
        self.wait(2)
        self.fadeOutCurrentScene()

    def postulate_3(self):
        title = Text("Euclid's Third Postulate", font_size=36).to_edge(UP)
        description = Text("We can describe a circle with any centre and radius.", font_size=24).next_to(title, DOWN)
        center = Dot(ORIGIN)
        label_center = Text("O", font_size=24).next_to(center, DOWN)
        circle = Circle(radius=2)
        line = Line(center,LEFT * 2)
        label_radius = Text("radius = 2 cm").scale(0.5).next_to(line,UP)
        self.play(Write(title))
        self.play(Write(description))
        self.wait(1)
        self.play(GrowFromCenter(center))
        self.play(Write(label_center))
        self.play(Create(circle))
        self.play(Create(line))
        self.play(Write(label_radius))
        self.wait(2)
        self.fadeOutCurrentScene()

    def postulate_4(self):
        title = Text("Euclid's Fourth Postulate", font_size=36).to_edge(UP)
        description = Text("All right angles are equal to one another.", font_size=24).next_to(title, DOWN)

        line_1 = Line(LEFT * 3, RIGHT * 2)
        line_2 = Line(LEFT * 3 , LEFT*3 + UP*2)

        line_3 = Line(LEFT , RIGHT * 2)
        line_4 = Line(LEFT , LEFT + UP*2)

        lines_a = VGroup(line_1, line_2,).scale(0.8).move_to([-3,0,0])
        lines_b = VGroup(line_3, line_4,).scale(0.8).move_to([3,0,0])

        angles = [
            Angle(line_1, line_2, radius=0.5, quadrant=(1,1), other_angle=False, color=YELLOW),
            Angle(line_3, line_4, radius=0.5, quadrant=(1,1), other_angle=False, color=GREEN)]
        
        labels = [
            MathTex(r"\angle 90").next_to(angles[0].point_from_proportion(0.5), UP +RIGHT*2, buff=0.2),
            MathTex(r"\angle 90").next_to(angles[1].point_from_proportion(0.5), UP+ RIGHT*3, buff=0.2)]

        label = [
            Text("P").next_to(line_2,UP),
            Text("Q").next_to(line_2,DOWN),
            Text("R").next_to(line_1,RIGHT),

            Text("A").next_to(line_4,UP),
            Text("B").next_to(line_4,DOWN),
            Text("C").next_to(line_3,RIGHT)
        ]
        
        end_1 = MathTex(r"\angle PQR").move_to([-1,-3,0])
        end_2 = MathTex(r"=").move_to([0,-3,0])
        end_3 = MathTex(r"\angle ABC").move_to([1,-3,0])
            
        self.play(Write(title))
        self.play(Write(description))
        self.wait(1)
        self.play(Create(lines_a),Create(lines_b))
        self.play(Create(VGroup(*angles, *labels, *label)))
        self.wait(1)
        self.play(Create(end_1))
        self.play(Write(end_2),Create(end_3))
        self.wait(2)
        self.fadeOutCurrentScene()

    def postulate_5(self):
        title = Text("Euclid's Fifth Postulate", font_size=36).to_edge(UP)
        description = Text("If a straight line falling on two straight lines makes the interior angles on the \n\n same side less than two right angles, the two straight lines, if extended indefinitely, meet on that side.", font_size=24).scale(0.7).next_to(title, DOWN)
        

        self.play(Write(title),Write(description))

        line_1 = Line(LEFT * 2, RIGHT * 4)
        line_2 = Line(LEFT * 2 + DOWN , RIGHT * 4 + DOWN * 2)
        transversal = Line(LEFT + DOWN * 2, RIGHT * 2 + UP * 2)

        lines = VGroup(line_1, line_2, transversal).scale(0.8)
        self.play(Create(lines))

        angles = [
            Angle(line_1, transversal, radius=0.5, quadrant=(-1,-1), other_angle=False, color=YELLOW),
            Angle(line_2, transversal, radius=0.5, quadrant=(-1,1), other_angle=True, color=GREEN)]
        
        labels = [
            MathTex(r"\angle 1").next_to(angles[0].point_from_proportion(0.5), UP*2 +LEFT, buff=0.2),
            MathTex(r"\angle 2").next_to(angles[1].point_from_proportion(0.5), DOWN*3+ LEFT*2, buff=0.2)]
        
        extend_1 = DashedLine(line_1, LEFT * 8)
        extend_2 = DashedLine(line_2 , LEFT * 8 + UP * 0.2)
        
        self.play(Create(VGroup(*angles, *labels)))
        self.play(Create(extend_1),Create(extend_2))
        self.wait(2)
        self.fadeOutCurrentScene()

    def SetDeveloperList(self):
        self.DeveloperList="Bhaskar"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade9Chapter3Geometry.py"
      
if __name__ == "__main__":
    scene = geometry()
    scene.render()