from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo

class constructionofquadrilateral8thgrade(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.quadrilateral()
        self.fadeOutCurrentScene()
        self.toq()
        self.fadeOutCurrentScene()
        self.coq3()
        self.fadeOutCurrentScene()
        self.coq1()
        self.fadeOutCurrentScene()
        self.coq4()
        self.fadeOutCurrentScene()
        self.coq2()
        self.fadeOutCurrentScene()
        self.cospclq()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
    
    
    def quadrilateral(self):
        self.isRandom = False
        self.angleChoice = [TAU/4,-TAU/3,-TAU/4]
        
        p10=cvo.CVO().CreateCVO("Quadrilaterals","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("definition", " It consist of 4S,4A").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("ETI", "Latin words “quadri”=“four” and “latus”=“side”").setPosition([0,-2.5,0])
        p13=cvo.CVO().CreateCVO("key points", "Vertices\nSides\nDiagonals\nInterior Angles\n").setPosition([-4,3,0])

        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.construct1(p10,p10)

    def toq(self):
        self.isRandom = False
        self.angleChoice = [TAU/4,TAU/4,-TAU/4,-TAU/4,-TAU/4,-TAU/4]
        

        p10=cvo.CVO().CreateCVO("Types of quadrilateral","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Trapezium", " one pair of opp S are llel").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("parallelogram", "two pair opp S are equal and llel").setPosition([5,-2,0])
        p13=cvo.CVO().CreateCVO("Rhombus", "ADJs are equal").setPosition([-4,3,0])
        p14=cvo.CVO().CreateCVO("Kite", "2 pairs of AdjS equal  and diagonals intersect at 90 deg").setPosition([-4,1,0])
        p15=cvo.CVO().CreateCVO("Rectangle", "parallelogram with 4 right angles").setPosition([-4,-1,0])
        p16=cvo.CVO().CreateCVO("Square", "rhombus with 4 right angles").setPosition([-4,-3,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        p10.cvolist.append(p16)
        self.construct1(p10,p10)
    
    
    def coq3(self):
        title = Text("Quadrilaterals").scale(0.9)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Function to create and fade quadrilaterals with titles and properties
        def create_and_fade(quadrilateral, title_text, properties_text):
            shape_title = Text(title_text).next_to(quadrilateral, UP)
            properties = Text(properties_text, font_size=24).next_to(quadrilateral, DOWN)
            self.play(Create(quadrilateral), Write(shape_title))
            self.play(Write(properties))
            self.wait(1)
            self.play(FadeOut(quadrilateral), FadeOut(shape_title), FadeOut(properties))

        # Trapezium
        trapezium = Polygon([-2, 0, 0], [2, 0, 0], [1, 2, 0], [-1, 2, 0], color=BLUE)
        trapezium_props = "1 pair parallel sides, 1 pair non-parallel sides"
        create_and_fade(trapezium, "Trapezium", trapezium_props)

        # Parallelogram
        parallelogram = Polygon([-1, 0, 0], [2, 0, 0], [3, 2, 0], [0, 2, 0], color=GREEN)
        parallelogram_props = "Opposite sides parallel and equal, opposite angles equal"
        create_and_fade(parallelogram, "Parallelogram", parallelogram_props)

        # Rectangle
        rectangle = Rectangle(width=4, height=2, color=ORANGE)
        rectangle_props = "Opposite sides equal, all angles 90 degrees"
        create_and_fade(rectangle, "Rectangle", rectangle_props)

        # Square
        square = Square(side_length=2, color=PURPLE)
        square_props = "All sides equal, all angles 90 degrees"
        create_and_fade(square, "Square", square_props)

        # Rhombus
        rhombus = Polygon([-1, 0, 0], [1, 0, 0], [1.5, 2, 0], [-1.5, 2, 0], color=RED)
        rhombus_props = "All sides equal, diagonals bisect angles"
        create_and_fade(rhombus, "Rhombus", rhombus_props)

        # Kite
        kite = Polygon([-1, 0, 0], [1, 0, 0], [0, 2, 0], [0, -2, 0], color=YELLOW)
        kite_props = "Two pairs of adjacent sides equal, diagonals intersect at 90 degrees"
        create_and_fade(kite, "Kite", kite_props)
    
    
    
    def coq1(self):
        self.isRandom = False
        self.angleChoice = [TAU/4,TAU/4,-TAU/4,-TAU/4,-TAU/4]
        

        p10=cvo.CVO().CreateCVO("Construction quadrilateral","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Materials needed", "Ruler\n ,Pencil\n,Protractor\n,Compass\n").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("Step:1", "draw rough sketch").setPosition([5,-2,0])
        p13=cvo.CVO().CreateCVO("Step:2", "Analyse the fig and use spcl properties of it").setPosition([-4,3,0])
        p14=cvo.CVO().CreateCVO("Step:3", "use compass and protractor to obtain req fig").setPosition([-4,1,0])
        p15=cvo.CVO().CreateCVO("Step:4", "Join the pt's to complete").setPosition([-4,-1,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        self.construct1(p10,p10)
    
    
    
    def coq4(self):
        title = Text("Quadrilateral Construction").to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Initialize an empty list to keep track of the sides
        sides = []

        # Step 1: Draw the first side with a ruler
        step1_text = Text("Step 1: Draw the first side with a ruler").next_to(title, DOWN)
        self.play(Write(step1_text))
        side1 = Line(LEFT, RIGHT)
        self.play(Create(side1))
        sides.append(side1)
        self.wait(1)
        self.play(FadeOut(step1_text))

        # Step 2: Draw the second side with a set square
        step2_text = Text("Step 2: Draw the second side with a set square").next_to(title, DOWN)
        self.play(Write(step2_text))
        side2 = Line(side1.get_end(), side1.get_end() + UP*2)
        self.play(Create(side2))
        sides.append(side2)
        self.wait(1)
        self.play(FadeOut(step2_text))

        # Step 3: Draw the third side with a ruler
        step3_text = Text("Step 3: Draw the third side with a ruler").next_to(title, DOWN)
        self.play(Write(step3_text))
        side3 = Line(side2.get_end(), side2.get_end() + LEFT*3)
        self.play(Create(side3))
        sides.append(side3)
        self.wait(1)
        self.play(FadeOut(step3_text))

        # Step 4: Draw the fourth side with a compass
        step4_text = Text("Step 4: Draw the fourth side with a compass").next_to(title, DOWN)
        self.play(Write(step4_text))
        side4 = Line(side3.get_end(), side1.get_start())
        self.play(Create(side4))
        sides.append(side4)
        self.wait(1)
        self.play(FadeOut(step4_text))

        # Step 5: Show the completed quadrilateral
        step5_text = Text("Step 5: Show the completed quadrilateral").next_to(title, DOWN)
        self.play(Write(step5_text))
        quadrilateral = Polygon(*[side.get_start() for side in sides], side4.get_end())
        self.play(Create(quadrilateral))
        self.wait(2)
        self.play(FadeOut(quadrilateral), FadeOut(step5_text))

        # Fade out the title at the end
        self.play(FadeOut(title))
    
    
    
    def coq2(self):
        self.isRandom = False
        self.angleChoice = [TAU/4,TAU/4,-TAU/4,-TAU/4,-TAU/4]
        

        p10=cvo.CVO().CreateCVO("Quadrilateral Measurements","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("4S AND 1A", "S.S.S.S.A").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("4S AND 1Diag", "S.S.S.S.Diag").setPosition([5,-2,0])
        p13=cvo.CVO().CreateCVO("3S AND 2Diag", "S.S.S.Diag.Diag").setPosition([-4,3,0])
        p14=cvo.CVO().CreateCVO("2AdjS AND 3A", "S.A.S.A.A").setPosition([-4,1,0])
        p15=cvo.CVO().CreateCVO("3S AND 2A", "S.A.S.A.S").setPosition([-4,-1,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        self.construct1(p10,p10)

    def cospclq(self):
        self.isRandom = False
        self.angleChoice = [TAU/4,TAU/4,-TAU/4,-TAU/4]
        

        p10=cvo.CVO().CreateCVO("Spcl quadrilateral","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("rhombus", "").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("square", "").setPosition([5,-2,0])
        p13=cvo.CVO().CreateCVO("Unique quadrilateral", "5 independent measurements req").setPosition([-4,3,0])
        p14=cvo.CVO().CreateCVO("construction", "when 2Diag are given").setPosition([-4,1,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.construct1(p10,p10)
        self.construct1(p14,p14)
        self.play(Create(CurvedArrow(p11.pos,p14.pos)),Create(CurvedArrow(p12.pos,p14.pos)))
        #self.play()
    
    
    def SetDeveloperList(self): 
       self.DeveloperList="dhanushofc" 
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Class8Ch3ConstructionOfQuadrilaterals.py"    


if __name__ == "__main__":
    scene = constructionofquadrilateral8thgrade()
    scene.render()