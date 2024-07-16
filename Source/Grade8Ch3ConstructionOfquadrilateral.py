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
        self.coq_2()
        self.fadeOutCurrentScene()
        
        self.GithubSourceCodeReference()
    
    
    def quadrilateral(self):
        self.isRandom = False
        self.angleChoice = [TAU/4,-TAU/3,-TAU/4]
        
        p10=cvo.CVO().CreateCVO("Quadrilaterals","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Definition", " It consist of 4 sides,4 angles").setPosition([4,2,0])
        #p12=cvo.CVO().CreateCVO("ETI", "Latin words “quadri”=“four” and “latus”=“side”").setPosition([0,-2.5,0])
        p13=cvo.CVO().CreateCVO("Key points", "Vertices\nSides\nDiagonals\nInterior Angles\n").setPosition([0,-2.5,0])

        p10.cvolist.append(p11)
        #p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.construct1(p10,p10)

    def toq(self):
        self.isRandom = False
        self.angleChoice = [TAU/4,TAU/4,-TAU/4,-TAU/4,-TAU/4,TAU/4]
        

        p10=cvo.CVO().CreateCVO("Types of quadrilateral","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Trapezium", "").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("Parallelogram", "").setPosition([5,-2,0])
        p13=cvo.CVO().CreateCVO("Rhombus", "").setPosition([-4,2,0])
        p14=cvo.CVO().CreateCVO("Kite", "").setPosition([-4,0,0])
        p15=cvo.CVO().CreateCVO("Rectangle", "").setPosition([-4,-2,0])
        p16=cvo.CVO().CreateCVO("Square", "").setPosition([4,0,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        p10.cvolist.append(p16)
        self.construct1(p10,p10)
    
    
   
 
    
    def coq3(self):
        title = Text("Quadrilaterals").scale(1.2)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        def create_and_fade(quadrilateral, title_text, properties_text, labels, diagonals=None):
            shape_title = Text(title_text, font_size=36).next_to(quadrilateral, UP, buff=0.5)
            properties = Text(properties_text, font_size=24).next_to(quadrilateral, DOWN, buff=0.5)
            
            self.play(Create(quadrilateral), Write(shape_title))
            self.play(Write(properties))
            
            for label in labels:
                self.play(Write(label), run_time=0.5)
            
            if diagonals:
                for diagonal in diagonals:
                    self.play(Create(diagonal), run_time=0.5)
            
            self.wait(2)
            fade_objects = [quadrilateral, shape_title, properties] + labels
            if diagonals:
                fade_objects += diagonals
            self.play(*[FadeOut(mob) for mob in fade_objects], run_time=1.5)

        # Trapezium
        trapezium = Polygon([-2, -1, 0], [2, -1, 0], [1, 1, 0], [-1, 1, 0], color=BLUE)
        trapezium_props = "1 pair of parallel sides (a || b), non-parallel sides (c, d)"
        trapezium_labels = [
            Text("A", font_size=24).next_to(trapezium.get_corner(DL), DL, buff=0.1),
            Text("B", font_size=24).next_to(trapezium.get_corner(DR), DR, buff=0.1),
            Text("C", font_size=24).next_to(trapezium.get_corner(UR), UR, buff=0.1),
            Text("D", font_size=24).next_to(trapezium.get_corner(UL), UL, buff=0.1),
            Text("a", font_size=24).next_to(trapezium.get_bottom(), DOWN, buff=0.1),
            Text("b", font_size=24).next_to(trapezium.get_top(), UP, buff=0.1),
            Text("c", font_size=24).next_to(trapezium.get_left(), LEFT, buff=0.1),
            Text("d", font_size=24).next_to(trapezium.get_right(), RIGHT, buff=0.1),
        ]
        create_and_fade(trapezium, "Trapezium", trapezium_props, trapezium_labels)

        # Parallelogram
        parallelogram = Polygon([-2, -1, 0], [2, -1, 0], [1, 1, 0], [-3, 1, 0], color=GREEN)
        parallelogram_props = "Opposite sides parallel and equal (a || c, b || d)"
        parallelogram_labels = [
            Text("A", font_size=24).next_to(parallelogram.get_corner(DL), DL, buff=0.1),
            Text("B", font_size=24).next_to(parallelogram.get_corner(DR), DR, buff=0.1),
            Text("C", font_size=24).next_to(parallelogram.get_corner(UR), UR, buff=0.1),
            Text("D", font_size=24).next_to(parallelogram.get_corner(UL), UL, buff=0.1),
            Text("a", font_size=24).next_to(parallelogram.get_bottom(), DOWN, buff=0.1),
            Text("b", font_size=24).next_to(parallelogram.get_right(), RIGHT, buff=0.1),
            Text("c", font_size=24).next_to(parallelogram.get_top(), UP, buff=0.1),
            Text("d", font_size=24).next_to(parallelogram.get_left(), LEFT, buff=0.1),
        ]
        create_and_fade(parallelogram, "Parallelogram", parallelogram_props, parallelogram_labels)

        # Rectangle
        rectangle = Rectangle(width=4, height=2, color=ORANGE)
        rectangle_props = "Opposite sides equal (w = w, h = h), all angles 90°"
        rectangle_labels = [
            Text("A", font_size=24).next_to(rectangle.get_corner(DL), DL, buff=0.1),
            Text("B", font_size=24).next_to(rectangle.get_corner(DR), DR, buff=0.1),
            Text("C", font_size=24).next_to(rectangle.get_corner(UR), UR, buff=0.1),
            Text("D", font_size=24).next_to(rectangle.get_corner(UL), UL, buff=0.1),
            Text("w", font_size=24).next_to(rectangle.get_bottom(), DOWN, buff=0.1),
            Text("h", font_size=24).next_to(rectangle.get_left(), LEFT, buff=0.1),
        ]
        rectangle_diagonals = [
            Line(rectangle.get_corner(DL), rectangle.get_corner(UR), color=YELLOW),
            Line(rectangle.get_corner(DR), rectangle.get_corner(UL), color=YELLOW),
        ]
        create_and_fade(rectangle, "Rectangle", rectangle_props, rectangle_labels, rectangle_diagonals)

        # Square
        square = Square(side_length=2, color=PURPLE)
        square_props = "All sides equal (s), all angles 90°"
        square_labels = [
            Text("A", font_size=24).next_to(square.get_corner(DL), DL, buff=0.1),
            Text("B", font_size=24).next_to(square.get_corner(DR), DR, buff=0.1),
            Text("C", font_size=24).next_to(square.get_corner(UR), UR, buff=0.1),
            Text("D", font_size=24).next_to(square.get_corner(UL), UL, buff=0.1),
            Text("s", font_size=24).next_to(square.get_bottom(), DOWN, buff=0.1),
        ]
        square_diagonals = [
            Line(square.get_corner(DL), square.get_corner(UR), color=YELLOW),
            Line(square.get_corner(DR), square.get_corner(UL), color=YELLOW),
        ]
        create_and_fade(square, "Square", square_props, square_labels, square_diagonals)

        # Rhombus
        rhombus = Polygon([-1.5, 0, 0], [0, -2, 0], [1.5, 0, 0], [0, 2, 0], color=RED)
        rhombus_props = "All sides equal (s), diagonals (d1, d2) bisect angles"
        rhombus_labels = [
            Text("A", font_size=24).next_to(rhombus.get_left(), LEFT, buff=0.1),
            Text("B", font_size=24).next_to(rhombus.get_bottom(), DOWN, buff=0.1),
            Text("C", font_size=24).next_to(rhombus.get_right(), RIGHT, buff=0.1),
            Text("D", font_size=24).next_to(rhombus.get_top(), UP, buff=0.1),
            Text("s", font_size=24).next_to(rhombus.get_bottom(), DR, buff=0.1),
            Text("d1", font_size=24).next_to(rhombus.get_center(), UR, buff=0.1),
            Text("d2", font_size=24).next_to(rhombus.get_center(), DL, buff=0.1),
        ]
        rhombus_diagonals = [
            Line(rhombus.get_left(), rhombus.get_right(), color=YELLOW),
            Line(rhombus.get_top(), rhombus.get_bottom(), color=YELLOW),
        ]
        create_and_fade(rhombus, "Rhombus", rhombus_props, rhombus_labels, rhombus_diagonals)

        # Kite
        kite = Polygon([-1, 0, 0], [0, -2, 0], [1, 0, 0], [0, 2, 0], color=YELLOW)
        kite_props = "Two pairs of adjacent sides equal, d1 perpendicular to d2"
        kite_labels = [
            Text("A", font_size=24).next_to(kite.get_left(), LEFT, buff=0.1),
            Text("B", font_size=24).next_to(kite.get_bottom(), DOWN, buff=0.1),
            Text("C", font_size=24).next_to(kite.get_right(), RIGHT, buff=0.1),
            Text("D", font_size=24).next_to(kite.get_top(), UP, buff=0.1),
            Text("d1", font_size=24).next_to(kite.get_center(), UR, buff=0.1),
            Text("d2", font_size=24).next_to(kite.get_center(), DL, buff=0.1),
        ]
        kite_diagonals = [
            Line(kite.get_left(), kite.get_right(), color=YELLOW),
            Line(kite.get_top(), kite.get_bottom(), color=YELLOW),
        ]
        create_and_fade(kite, "Kite", kite_props, kite_labels, kite_diagonals)

        
    
    
    
    def coq1(self):
        self.isRandom = False
        self.angleChoice = [TAU/4,TAU/4,-TAU/4,-TAU/4,-TAU/4]
        

        p10=cvo.CVO().CreateCVO("Construction quadrilateral","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Materials needed", "Ruler\n ,Pencil\n,Protractor\n,Compass\n").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("Step:1", "draw rough sketch").setPosition([5,-2,0])
        p13=cvo.CVO().CreateCVO("Step:2", "Analyse the fig and use spcl properties of it").setPosition([-4,2,0])
        p14=cvo.CVO().CreateCVO("Step:3", "use compass and protractor to obtain req fig").setPosition([-4,0,0])
        p15=cvo.CVO().CreateCVO("Step:4", "Join the pt's to complete").setPosition([-4,-2,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        self.construct1(p10,p10)
    
    
    
  
   
    
    def coq4(self):
        # Title
        title = Text("Quadrilateral Construction", font_size=40).to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)

        # Initialize lists for sides and vertices
        sides = []
        vertices = []

        # Create a group for step texts
        step_text_group = VGroup()

        # Function to create and animate step text
        def show_step_text(step_number, description):
            step_text = Text(f"Step {step_number}: {description}", font_size=28).next_to(title, DOWN, buff=0.5)
            self.play(Write(step_text))
            step_text_group.add(step_text)
            return step_text

        # Function to hide step text
        def hide_step_text():
            self.play(FadeOut(step_text_group))
            step_text_group.remove(*step_text_group)

        # Step 1: Draw the first side (base) with a ruler
        show_step_text(1, "Draw the base (AB)")
        side1 = Line(LEFT*3, RIGHT*3, color=BLUE).shift(DOWN)
        side1_label = Text("AB", font_size=24).next_to(side1, DOWN, buff=0.2)
        self.play(Create(side1), Write(side1_label))
        sides.append(side1)
        vertices.extend([side1.get_start(), side1.get_end()])
        self.wait(1)
        hide_step_text()

        # Step 2: Draw the second side
        show_step_text(2, "Draw BC")
        side2 = Line(side1.get_end(), side1.get_end() + UP*2 + RIGHT*0.5, color=RED)
        side2_label = Text("BC", font_size=24).next_to(side2, RIGHT, buff=0.2)
        self.play(Create(side2), Write(side2_label))
        sides.append(side2)
        vertices.append(side2.get_end())
        self.wait(1)
        hide_step_text()

        # Step 3: Draw the third side
        show_step_text(3, "Draw CD")
        side3 = Line(side2.get_end(), side2.get_end() + LEFT*6 + UP*0.5, color=GREEN)
        side3_label = Text("CD", font_size=24).next_to(side3, UP, buff=0.2)
        self.play(Create(side3), Write(side3_label))
        sides.append(side3)
        vertices.append(side3.get_end())
        self.wait(1)
        hide_step_text()

        # Step 4: Draw the fourth side
        show_step_text(4, "Draw DA")
        side4 = Line(side3.get_end(), side1.get_start(), color=YELLOW)
        side4_label = Text("DA", font_size=24).next_to(side4, LEFT, buff=0.2)
        self.play(Create(side4), Write(side4_label))
        sides.append(side4)
        self.wait(1)
        hide_step_text()

        # Label vertices
        vertex_labels = VGroup(*[
            Text(label, font_size=24).next_to(point, direction, buff=0.2)
            for label, point, direction in zip(
                ["A", "B", "C", "D"],
                vertices,
                [DOWN+LEFT, DOWN+RIGHT, UP+RIGHT, UP+LEFT]
            )
        ])
        self.play(Write(vertex_labels))

        # Step 5: Show the completed quadrilateral
        show_step_text(5, "Completed Quadrilateral ABCD")
        quadrilateral = Polygon(*vertices, color=WHITE, fill_opacity=0.2)
        self.play(Create(quadrilateral))
        self.wait(2)
        hide_step_text()

        # Final display
        final_text = Text("Quadrilateral ABCD", font_size=36).next_to(quadrilateral, DOWN, buff=0.5)
        self.play(Write(final_text))
        self.wait(2)

        # Fade out everything
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=2
        )
    
    
    
    
    
    def coq_2(self):
        self.isRandom = False
        self.angleChoice = [TAU/4,TAU/4,-TAU/4,-TAU/4,-TAU/4]
        

        p10=cvo.CVO().CreateCVO("Quadrilateral Measurements","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("4 sides 1 angle", "").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("4 sides 1 diagonal", "").setPosition([5,-2,0])
        p13=cvo.CVO().CreateCVO("3 sides 2 diagonals", "").setPosition([-4,2,0])
        p14=cvo.CVO().CreateCVO("2 adjacent 3 angles", "").setPosition([-4,0,0])
        p15=cvo.CVO().CreateCVO("3 sides 2 angles", "").setPosition([-4,-2,0])
        
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
       
        self.construct1(p10,p10)

    
    
    def SetDeveloperList(self): 
       self.DeveloperList="dhanushofc" 
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Class8Ch3ConstructionOfQuadrilaterals.py"    


if __name__ == "__main__":
    scene = constructionofquadrilateral8thgrade()
    scene.render()