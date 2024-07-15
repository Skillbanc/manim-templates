from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo

class symmetry6thgrade(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.symmetry1()
        self.fadeOutCurrentScene()
        self.symmetry2()
        self.fadeOutCurrentScene()
        self.symmetry3()
        self.fadeOutCurrentScene()
        self.symmetry4()
        self.fadeOutCurrentScene()
        self.symmetry5()
        self.fadeOutCurrentScene()
        self.symmetry6()
        self.fadeOutCurrentScene()
        self.symmetry7()
        self.fadeOutCurrentScene()
        self.symmetry8()
        self.fadeOutCurrentScene()
        self.symmetry9()
        self.fadeOutCurrentScene()
        self.symmetry10()
        self.fadeOutCurrentScene()
        self.symmetry11()
        self.fadeOutCurrentScene()
        self.symmetry12()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
    
    
    def symmetry1(self):
        self.isRandom = False
        self.angleChoice = [TAU/4,TAU/4,-TAU/4,-TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Symmetry","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("definition", " Balanced, mirrored, harmonious, equal, reflection").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("ETI", "balanced arrangement of shapes, objects, or patterns").setPosition([2,-3,0])
        p13=cvo.CVO().CreateCVO("Types", "").setPosition([-4,3,0])
        p14=cvo.CVO().CreateCVO("", "line symmetry ").setPosition([-4,1,0])
        p15=cvo.CVO().CreateCVO("", "multiple line of symmetry").setPosition([-4,-3,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p13.cvolist.append(p14)
        p13.cvolist.append(p15)
        self.construct1(p10,p10)


    def symmetry2(self):
        # Example 1: Circle (Point Symmetry)
        circle = Circle(radius=2, color=BLUE)
        circle_label = Tex("Circle", color=WHITE).next_to(circle, DOWN)
        self.play(Create(circle), Write(circle_label))
        self.wait(1)

        # Add a point of symmetry to the circle (center)
        circle_symmetry_point = Dot(circle.get_center(), color=RED)
        self.play(Create(circle_symmetry_point))

        self.wait(1)
        self.play(FadeOut(circle), FadeOut(circle_label), FadeOut(circle_symmetry_point))

        # Example 2: Square (Line Symmetry)
        square = Square(side_length=2, color=GREEN)
        square_label = Tex("Square", color=WHITE).next_to(square, DOWN)
        self.play(Create(square), Write(square_label))
        self.wait(1)

        # Add a line of symmetry to the square
        square_symmetry_line = Line(square.get_center(), square.get_center() + UP*2, color=RED)
        self.play(Create(square_symmetry_line))

        self.wait(1)
        self.play(FadeOut(square), FadeOut(square_label), FadeOut(square_symmetry_line))


    def symmetry3(self):
        self.isRandom = False
        self.angleChoice = [TAU/4,TAU/3,-TAU/4]
        p10=cvo.CVO().CreateCVO("line symmetry","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("definition", "").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("", "a line that divides a shape into two identical halves").setPosition([0,-2.5,0])
        p13=cvo.CVO().CreateCVO("Example", "square has 4(i.e Dia) and circle has infinite through center").setPosition([-4,1,0])

        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.construct1(p10,p10)

    def symmetry4(self):
        # Create a dictionary to store the symmetry types
        symmetry_types = {
        
            'A': 'Vertical',
            'B': 'Both',
            'C': 'Horizontal',
            'D': 'Horizontal',
            'E': 'Horizontal',
            'F': 'No',
            'G': 'No',
            'H': 'Both',
            'I': 'Both',
            'J': 'No',
            'K': 'Horizontal',
            'L': 'No',
            'M': 'Vertical',
            'N': 'Vertical',
            'O': 'Both',
            'P': 'No',
            'Q': 'No',
            'R': 'No',
            'S': 'Horizontal',
            'T': 'Vertical',
            'U': 'Vertical',
            'V': 'Vertical',
            'W': 'Vertical',
            'X': 'Both',
            'Y': 'No',
            'Z': 'Horizontal'
        
        }
        alphabets = [chr(i) for i in range(65, 91)]

        # Create a VGroup to store the alphabet TextMobjects
        alphabet_group = VGroup()

        # Create the animation
        for alphabet in alphabets:
            text = Text(alphabet, font_size=48)
            text.move_to(ORIGIN)
            alphabet_group.add(text)

            

            # Add the line of symmetry
            if symmetry_types[alphabet] == 'Vertical':
                line = Line(UP, DOWN, color=YELLOW)
                line.next_to(text, RIGHT)
                alphabet_group.add(line)
            elif symmetry_types[alphabet] == 'Horizontal':
                line = Line(LEFT, RIGHT, color=YELLOW)
                line.next_to(text, UP)
                alphabet_group.add(line)
            elif symmetry_types[alphabet] == 'Both':
                line1 = Line(UP, DOWN, color=YELLOW)
                line1.next_to(text, RIGHT)
                alphabet_group.add(line1)
                line2 = Line(LEFT, RIGHT, color=YELLOW)
                line2.next_to(text, UP)
                alphabet_group.add(line2)
            
             # Add the symmetry type
            symmetry_text = Text(f"Symmetry: {symmetry_types[alphabet]}", font_size=24)
            symmetry_text.next_to(text, DOWN)
            alphabet_group.add(symmetry_text)


        # Fade out each alphabet smoothly
        for alphabet in alphabet_group:
            self.play(FadeOut(alphabet))
            self.wait(0.2)  # Adjust the duration as needed

    def symmetry5(self):
        p10=cvo.CVO().CreateCVO("line symmetry","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("", "of Circle").setPosition([4,2,0])
        
        p10.cvolist.append(p11)
        self.construct1(p10,p10)
    
    
    def symmetry6(self):
        # Create a circle
        circle = Circle(radius=2)

        # Create a line of symmetry
        line_of_symmetry = Line(start=circle.get_center(), end=circle.get_center() + RIGHT * 4)

        # Create a dashed line to indicate the line of symmetry
        dashed_line = DashedLine(start=line_of_symmetry.get_start(), end=line_of_symmetry.get_end(), dash_length=0.1)

        # Add the circle and dashed line to the scene
        self.add(circle, dashed_line)

        # Animate the circle to move along the line of symmetry
        self.play(MoveAlongPath(circle, line_of_symmetry), run_time=3)

        # Add a text label to indicate the line of symmetry
        text = Text("How to draw a line of symmetry for circle", font_size=24)
        text.next_to(line_of_symmetry, UP)
        self.add(text)

        # Fade out the text
        self.play(FadeOut(text))
    
    
    def symmetry7(self):
        self.isRandom = False
        self.angleChoice = [TAU/4,-TAU/3]
        p10=cvo.CVO().CreateCVO("Multiple line of symmetry","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("definition", " more than one line of symmetry").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("Example", "Rectangle,Triangle(equi),Circle").setPosition([0,-2.5,0])
       
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)

 
    def symmetry8(self):
        p10=cvo.CVO().CreateCVO("KITE","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("", " 2 identical set squares").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("LOS", "One line,runs along the center of the kite").setPosition([0,-2.5,0]).setangle(-TAU/3)
       
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        
        
        
        
    def symmetry9(self):
        # Create a title
        title = Title("Symmetry of a Kite")
        self.add(title)

        # Create a kite shape
        kite = Polygon(
            ORIGIN,  # bottom left
            UP * 2,  # top
            RIGHT * 2 + UP,  # top right
            RIGHT * 2,  # bottom right
            color=BLUE,
            fill_opacity=0.5
        )

        # Create a line of symmetry
        line_of_symmetry = Line(start=kite.get_bottom(), end=kite.get_top())

        # Create a dashed line to indicate the line of symmetry
        dashed_line = DashedLine(start=line_of_symmetry.get_start(), end=line_of_symmetry.get_end(), dash_length=0.1)

        # Add the kite and dashed line to the scene
        self.add(kite, dashed_line)

        # Animate the kite to reflect across the line of symmetry
        self.play(
            kite.animate.apply_function(lambda p: line_of_symmetry.get_start() + (p - line_of_symmetry.get_start()) * [-1, 1, 1]),
            run_time=2
        )

        # Add a text label to indicate the line of symmetry
        text = Text("Line of Symmetry", font_size=24)
        text.next_to(line_of_symmetry, UP)
        self.add(text)

        # Wait for a moment before ending the scene
        self.wait()
        
        
    def symmetry10(self):
        self.isRandom = False
        self.angleChoice = [TAU/4,-TAU/3]
        p10=cvo.CVO().CreateCVO("Rectangle","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("", "consist of length'l' and breadth'b'").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("LOS", "one passing through l and another through b ").setPosition([0,-2.5,0])
       
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
    
    def symmetry11(self):
        # Create a title
        title = Title("Symmetry of a Rectangle")
        self.add(title)

        # Create a rectangle shape
        rectangle = Rectangle(width=4, height=2, color=BLUE, fill_opacity=0.5)

        # Create two lines of symmetry
        line_of_symmetry_1 = Line(start=rectangle.get_left(), end=rectangle.get_right())
        line_of_symmetry_2 = Line(start=rectangle.get_bottom(), end=rectangle.get_top())

        # Create dashed lines to indicate the lines of symmetry
        dashed_line_1 = DashedLine(start=line_of_symmetry_1.get_start(), end=line_of_symmetry_1.get_end(), dash_length=0.1)
        dashed_line_2 = DashedLine(start=line_of_symmetry_2.get_start(), end=line_of_symmetry_2.get_end(), dash_length=0.1)

        # Add the rectangle, dashed lines, and title to the scene
        self.add(rectangle, dashed_line_1, dashed_line_2, title)

        # Animate the rectangle to reflect across the lines of symmetry
        self.play(
            rectangle.animate.apply_function(lambda p: line_of_symmetry_1.get_start() + (p - line_of_symmetry_1.get_start()) * [-1, 1, 1]),
            rectangle.animate.apply_function(lambda p: line_of_symmetry_2.get_start() + (p - line_of_symmetry_2.get_start()) * [1, -1, 1]),
            run_time=2
        )

        # Add a text label to indicate the lines of symmetry
        text_1 = Text("Line of Symmetry", font_size=24)
        text_1.next_to(line_of_symmetry_1, UP, buff=0.5)  # Move text 1 up a bit
        text_2 = Text("Line of Symmetry", font_size=24)
        text_2.next_to(line_of_symmetry_2, LEFT, buff=0.5)  # Move text 2 left a bit
        self.add(text_1, text_2)

        # Wait for a moment before ending the scene
        self.wait()

    def symmetry12(self):
        # Title of the animation
        title = Text("How to Draw a Symmetric Figure").to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))  # Fade out the title after displaying

        # Step 1: Draw the first line of symmetry
        line_m = Line(UP*2, DOWN*2).shift(LEFT)
        step1_text = Text("(i) Draw the first line of symmetry (m).").to_edge(UP).scale(0.5)
        self.play(Write(step1_text))
        self.play(Create(line_m))
        self.wait(1)
        self.play(FadeOut(step1_text))

        # Step 2: Draw the initial curve
        start_anchor = LEFT*2
        start_handle = LEFT*2 + UP
        end_handle = LEFT + UP*2
        end_anchor = ORIGIN
        curve = CubicBezier(start_anchor=start_anchor, start_handle=start_handle, end_handle=end_handle, end_anchor=end_anchor)
        step2_text = Text("(ii) Draw an initial curve.").to_edge(UP).scale(0.5)
        self.play(Write(step2_text))
        self.play(Create(curve))
        self.wait(1)
        self.play(FadeOut(step2_text))

        # Step 3: Draw the second line of symmetry
        line_A = Line(LEFT*3, RIGHT*3)
        step3_text = Text("(iii) Draw the second line of symmetry (A).").to_edge(UP).scale(0.5)
        self.play(Write(step3_text))
        self.play(Create(line_A))
        self.wait(1)
        self.play(FadeOut(step3_text))

        # Step 4: Draw the mirror image of the curve
        mirror_curve = curve.copy()
        mirror_curve.flip(axis=line_m.get_vector())
        step4_text = Text("(iv) Draw a mirror image of the curve across line m.").to_edge(UP).scale(0.5)
        self.play(Write(step4_text))
        self.play(Transform(curve, mirror_curve))
        self.wait(1)
        self.play(FadeOut(step4_text))

        # Final step: Show the complete symmetric figure
        final_step_text = Text("Complete symmetric figure with lines A and m.").to_edge(UP).scale(0.5)
        self.play(Write(final_step_text))
        self.play(Create(line_m), Create(line_A), Create(curve), Create(mirror_curve))
        self.wait(2)

         # Clear the screen
        self.play(FadeOut(line_m), FadeOut(line_A), FadeOut(curve), FadeOut(mirror_curve), FadeOut(final_step_text))

    def SetDeveloperList(self): 
       self.DeveloperList="dhanushofc" 
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Class6Ch12Symmetry.py"    


    
if __name__ == "__main__":
    scene = symmetry6thgrade()
    scene.render()