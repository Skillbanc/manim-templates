from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo

class Grade6Chapter12Symmetry(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.symmetry1()
        self.fadeOutCurrentScene()
        
        self.symmetry3()
        self.fadeOutCurrentScene()
        self.symmetry2()
        self.fadeOutCurrentScene()
        
        self.symmetry7()
        self.fadeOutCurrentScene()
        self.symmetry4()
        self.fadeOutCurrentScene()
        self.symmetry9()
        self.fadeOutCurrentScene()
        
        
        
        self.GithubSourceCodeReference()
    
    
    def symmetry1(self):
        self.isRandom = False
        self.angleChoice = [TAU/4,TAU/4,-TAU/4,-TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Symmetry","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Definition", " Balanced, mirrored, harmonious, equal, reflection").setPosition([4,2,0])
       
        p13=cvo.CVO().CreateCVO("Types", "").setPosition([5,-2,0])
        p14=cvo.CVO().CreateCVO("line symmetry ", "").setPosition([-4,2,0])
        p15=cvo.CVO().CreateCVO("multiple line of symmetry", "").setPosition([-4,0,0])
        p10.cvolist.append(p11)
        
        p10.cvolist.append(p13)
        p13.cvolist.append(p14)
        p13.cvolist.append(p15)
        self.construct1(p10,p10)


    


    def symmetry3(self):
        self.isRandom = False
        self.angleChoice = [TAU/4,TAU/4,-TAU/4]
        p10=cvo.CVO().CreateCVO("Line symmetry","").setPosition([0,2.5,0])
        
        p12=cvo.CVO().CreateCVO("Definition", "a line that divides a shape into two halves").setPosition([0,-2.5,0])
        p13=cvo.CVO().CreateCVO("Example", "square has 4(i.e Dia) and circle has infinite through center").setPosition([-4,0,0])

        
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.construct1(p10,p10)
    
    def symmetry2(self):
        # Create a heading
        heading = Text("EXAMPLE OF LINE OF SYMMETRY: Square", font_size=36)
        heading.to_edge(UP, buff=0.5)
        
        # Create a square
        square = Square(side_length=4, color=BLUE)
        
        # Label the vertices
        labels = VGroup()
        vertices = square.get_vertices()
        for i, point in enumerate(vertices):
            label = Text(f"V{i+1}", font_size=24)
            label.next_to(point, direction=point - square.get_center(), buff=0.2)
            labels.add(label)
        
        # Create the symmetry line
        symmetry_line = Line(
            start=square.get_top(),
            end=square.get_bottom(),
            color=RED
        )
        
        # Create a label for the symmetry line
        sym_label = Text("Line of Symmetry", font_size=24, color=RED)
        sym_label.next_to(symmetry_line, RIGHT, buff=0.5)
        
        # Group square and labels
        square_group = VGroup(square, labels)
        square_group.next_to(heading, DOWN, buff=0.5)
        
        # Adjust symmetry line and label positions
        symmetry_line.move_to(square_group)
        sym_label.next_to(symmetry_line, RIGHT, buff=0.5)
        
        # Animations
        self.play(Write(heading))
        self.play(Create(square))
        self.play(Write(labels))
        self.wait(1)
        
        self.play(
            Create(symmetry_line),
            Write(sym_label)
        )
        self.wait(1)
        
        # Rotate the square to show symmetry
        self.play(
            Rotate(
                square_group,
                angle=PI,
                about_point=square_group.get_center(),
                rate_func=there_and_back,
                run_time=3
            )
        )
        self.wait(1)
        
        # Fade out everything
        self.play(
            FadeOut(heading),
            FadeOut(square_group),
            FadeOut(symmetry_line),
            FadeOut(sym_label)
        )

    
    
    
    
    
    
    def symmetry7(self):
        self.isRandom = False
        self.angleChoice = [TAU/4,-TAU/3]
        p10=cvo.CVO().CreateCVO("Multiple line of symmetry","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Definition", " more than one line of symmetry").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("Example", "Rectangle,Triangle(equi),Circle").setPosition([0,-2.5,0])
       
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
    
    def symmetry4(self):
        # Title
        title = Text("Examples of Multiple Lines of Symmetry", font_size=36)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))

        # Rectangle
        self.animate_shape("Rectangle", 4, 2.5, BLUE, ["A", "B", "C", "D"])

        # Transition
        self.play(title.animate.shift(UP * 0.5))
        transition_text = Text("Next: Kite", font_size=30).next_to(title, DOWN)
        self.play(Write(transition_text))
        self.wait(1)
        self.play(FadeOut(transition_text))

        # Kite
        self.animate_shape("Kite", 3, 4, YELLOW, ["P", "Q", "R", "S"], is_kite=True)

        self.wait(2)

    def animate_shape(self, shape_name, width, height, color, vertex_labels, is_kite=False):
        # Create shape
        if is_kite:
            shape = self.create_kite(width, height, color)
        else:
            shape = Rectangle(width=width, height=height, color=color)
        
        shape_label = Text(shape_name, font_size=28).next_to(shape, DOWN, buff=0.5)

        # Create vertices
        vertices = VGroup()
        points = shape.get_vertices()
        for point, label in zip(points, vertex_labels):
            dot = Dot(point, color=WHITE)
            text = Text(label, font_size=20).next_to(dot, direction=normalize(point - shape.get_center()), buff=0.1)
            vertices.add(VGroup(dot, text))

        # Create symmetry lines
        v_line = DashedLine(start=shape.get_top(), end=shape.get_bottom(), color=RED)
        h_line = DashedLine(start=shape.get_left(), end=shape.get_right(), color=GREEN)

        # Animations
        self.play(Create(shape), Write(shape_label))
        self.play(Create(vertices))
        self.wait(1)

        # Vertical symmetry
        self.play(Create(v_line))
        self.play(Rotate(shape, PI, about_point=shape.get_center()), Rotate(vertices, PI, about_point=shape.get_center()), run_time=2)
        self.wait(1)
        self.play(FadeOut(v_line))

        # Horizontal symmetry
        if is_kite:
            d_line = DashedLine(start=points[0], end=points[2], color=GREEN)
            self.play(Create(d_line))
            self.play(Rotate(shape, PI, axis=UP, about_point=shape.get_center()), 
                      Rotate(vertices, PI, axis=UP, about_point=shape.get_center()), run_time=2)
            self.wait(1)
            self.play(FadeOut(d_line))
        else:
            self.play(Create(h_line))
            self.play(Rotate(shape, PI, axis=RIGHT, about_point=shape.get_center()),
                      Rotate(vertices, PI, axis=RIGHT, about_point=shape.get_center()), run_time=2)
            self.wait(1)
            self.play(FadeOut(h_line))

        self.play(FadeOut(shape), FadeOut(vertices), FadeOut(shape_label))

    def create_kite(self, width, height, color):
        points = [
            [0, height/2, 0],
            [width/2, 0, 0],
            [0, -height/4, 0],
            [-width/2, 0, 0]
        ]
        return Polygon(*points, color=color)

 
    
    
    def symmetry9(self):
        sections = [
            self.introduction,
            self.mirror_reflection,
            self.line_symmetry,
            self.multiple_lines_of_symmetry,
            
            self.symmetry_in_alphabets,
            self.symmetry_in_shapes,
            self.drawing_symmetric_figures,
            self.conclusion
        ]
        for section in sections:
            section()
            self.clear()
            self.wait(0.5)

    def introduction(self):
        title = Text("Symmetry", font_size=72, color=BLUE_E)
        self.play(Write(title))
        self.wait(2)

    def mirror_reflection(self):
        subtitle = Text("Mirror Reflection", font_size=48, color=BLUE_D)
        self.play(Write(subtitle))
        self.wait(1)
        self.play(subtitle.animate.to_edge(UP))

        wow_text = Text("WOW", font_size=144, color=RED)
        mirror_line = Line(start=LEFT * 4, end=RIGHT * 4, color=BLUE)
        
        self.play(Write(wow_text))
        self.wait(1)
        self.play(Create(mirror_line))
        self.wait(1)

        reflected_wow = wow_text.copy().flip().set_color(GREEN)
        self.play(
            wow_text.animate.shift(UP * 1.5),
            reflected_wow.animate.shift(DOWN * 1.5),
            run_time=2
        )
        self.wait(2)

    def line_symmetry(self):
        subtitle = Text("Line Symmetry", font_size=48, color=BLUE_D)
        self.play(Write(subtitle))
        self.wait(1)
        self.play(subtitle.animate.to_edge(UP))

        shapes = [
            (RegularPolygon(n=3, color=RED).scale(2), "Triangle"),
            (Square(color=GREEN).scale(2), "Square"),
            (RegularPolygon(n=5, color=BLUE).scale(2), "Pentagon")
        ]

        for shape, name in shapes:
            shape_label = Text(name, font_size=36, color=WHITE).next_to(shape, DOWN)
            self.play(Create(shape), Write(shape_label))
            self.wait(1)

            sym_line = Line(shape.get_top(), shape.get_bottom(), color=YELLOW)
            self.play(Create(sym_line))
            self.wait(1)
            self.play(FadeOut(sym_line))

            self.play(FadeOut(shape), FadeOut(shape_label))
            self.wait(0.5)

    def multiple_lines_of_symmetry(self):
        subtitle = Text("Multiple Lines of Symmetry", font_size=48, color=BLUE_D)
        self.play(Write(subtitle))
        self.wait(1)
        self.play(subtitle.animate.to_edge(UP))

        square = Square(side_length=4, color=PURPLE)
        square_label = Text("Square", font_size=36, color=WHITE).next_to(square, DOWN)
        self.play(Create(square), Write(square_label))
        self.wait(1)

        lines = VGroup(
            Line(square.get_top(), square.get_bottom(), color=RED),
            Line(square.get_left(), square.get_right(), color=BLUE),
            Line(square.get_corner(UL), square.get_corner(DR), color=GREEN),
            Line(square.get_corner(UR), square.get_corner(DL), color=YELLOW)
        )

        for line in lines:
            self.play(Create(line))
            self.wait(0.5)

        self.wait(2)

    
    def symmetry_in_alphabets(self):
        subtitle = Text("Symmetry in Alphabets", font_size=48, color=BLUE_D)
        self.play(Write(subtitle))
        self.wait(1)
        self.play(subtitle.animate.to_edge(UP))

        alphabets = [
            ("A", RED, "Vertical symmetry"),
            ("B", GREEN, "Horizontal symmetry"),
            ("C", BLUE, "No line symmetry"),
            ("D", YELLOW, "Vertical symmetry")
        ]

        for letter, color, sym_type in alphabets:
            text = Text(letter, font_size=144, color=color)
            sym_text = Text(sym_type, font_size=36, color=WHITE).next_to(text, DOWN)
            self.play(Write(text), Write(sym_text))
            self.wait(1)

            if sym_type != "No line symmetry":
                sym_line = Line(text.get_top(), text.get_bottom(), color=PURPLE) if "Vertical" in sym_type else Line(text.get_left(), text.get_right(), color=PURPLE)
                self.play(Create(sym_line))
                self.wait(1)
                self.play(FadeOut(sym_line))

            self.play(FadeOut(text), FadeOut(sym_text))
            self.wait(0.5)

    def symmetry_in_shapes(self):
        subtitle = Text("Symmetry in Shapes", font_size=48, color=BLUE_D)
        self.play(Write(subtitle))
        self.wait(1)
        self.play(subtitle.animate.to_edge(UP))

        shapes = [
            (Triangle(color=RED).scale(2), "Triangle"),
            (Square(color=GREEN).scale(2), "Square"),
            (RegularPolygon(6, color=BLUE).scale(2), "Hexagon"),
            (Circle(color=YELLOW).scale(2), "Circle")
        ]

        for shape, name in shapes:
            shape_label = Text(name, font_size=36, color=WHITE).next_to(shape, DOWN)
            self.play(Create(shape), Write(shape_label))
            self.wait(1)

            if isinstance(shape, (Triangle, RegularPolygon)):
                num_sides = 3 if isinstance(shape, Triangle) else 6
                for i in range(num_sides):
                    line = Line(shape.get_center(), shape.get_vertices()[i], color=WHITE)
                    self.play(Create(line))
                    self.wait(0.5)
                    self.play(FadeOut(line))
            elif isinstance(shape, Square):
                lines = VGroup(
                    Line(shape.get_top(), shape.get_bottom(), color=WHITE),
                    Line(shape.get_left(), shape.get_right(), color=WHITE),
                    Line(shape.get_corner(UL), shape.get_corner(DR), color=WHITE),
                    Line(shape.get_corner(UR), shape.get_corner(DL), color=WHITE)
                )
                self.play(Create(lines))
                self.wait(1)
                self.play(FadeOut(lines))
            else:  # Circle
                infinite_text = Text("Infinite lines of symmetry", font_size=24, color=PURPLE)
                infinite_text.next_to(shape, DOWN, buff=0.5)  # Increased buffer
                shape_label.next_to(infinite_text, DOWN, buff=0.2)  # Move shape label below
                self.play(Write(infinite_text))
                self.wait(1)
                self.play(FadeOut(infinite_text))

            self.play(FadeOut(shape), FadeOut(shape_label))
            self.wait(0.5)

    def drawing_symmetric_figures(self):
        subtitle = Text("Drawing Symmetric Figures", font_size=48, color=BLUE_D)
        self.play(Write(subtitle))
        self.wait(1)
        self.play(subtitle.animate.to_edge(UP))

        half_flower = VGroup(
            Arc(1.5, 0, PI, color=RED),
            Arc(1.5, 0, PI, color=GREEN).rotate(PI/3),
            Arc(1.5, 0, PI, color=BLUE).rotate(-PI/3)
        ).scale(1.5)

        half_flower_label = Text("Half Flower", font_size=36, color=WHITE).next_to(half_flower, DOWN)
        self.play(Create(half_flower), Write(half_flower_label))
        self.wait(1)

        mirror_line = Line(DOWN * 3, UP * 3, color=YELLOW)
        self.play(Create(mirror_line))
        self.wait(1)

        full_flower = VGroup(
            half_flower.copy(),
            half_flower.copy().flip(RIGHT)
        )
        full_flower_label = Text("Full Symmetric Flower", font_size=36, color=WHITE).next_to(full_flower, DOWN)

        self.play(
            Transform(half_flower, full_flower),
            Transform(half_flower_label, full_flower_label),
            FadeOut(mirror_line)
        )
        self.wait(2)

    def conclusion(self):
        conclusion = Text("Symmetry in Daily Life", font_size=48, color=BLUE_E)
        self.play(Write(conclusion))
        self.wait(1)
        self.play(conclusion.animate.to_edge(UP))

        examples = VGroup(
            Text("Architecture", font_size=36, color=RED),
            Text("Nature", font_size=36, color=GREEN),
            Text("Art", font_size=36, color=BLUE),
            Text("Technology", font_size=36, color=YELLOW)
        ).arrange(DOWN, buff=0.5)  # Arrange vertically with buffer

        examples.next_to(conclusion, DOWN, buff=1)  # Position the group below the title

        for example in examples:
            self.play(Write(example))
            self.wait(0.5)

        self.wait(2)
        
        
        
        
    
        
        
    
    
    

    

    def SetDeveloperList(self): 
       self.DeveloperList="dhanushofc" 
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade6Chapter12Symmetry.py"    


    
if __name__ == "__main__":
    scene = Grade6Chapter12Symmetry()
    scene.render()