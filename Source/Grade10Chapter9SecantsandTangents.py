import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo
class secantsandtangents(AbstractAnim):
    def construct(self):      
        self.circles()
        self.fadeOutCurrentScene()
        self.constructionoftangents()
        self.CircleWithTangent()
        self.fadeOutCurrentScene()
        self.tangentexternal()
        self.fadeOutCurrentScene()
        self.secant()
        self.constructionofsecant()
        self.area()
        self.rectangle()
        self.square()
        self.triangle() 
        self.GithubSourceCodeReference()
    def circles(self):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.isRandom = False
        self.positionChoice = [[-5,0,0],[5,2,0],[5,-3,0]]
        p10=cvo.CVO().CreateCVO("Circles","")
        p11=cvo.CVO().CreateCVO("Secants","")
        p12=cvo.CVO().CreateCVO("Tangents","")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
    def constructionoftangents(self):
        self.isRandom = False
        self.positionChoice = [[-6,0,0],[3,0,0]]
        a10=cvo.CVO().CreateCVO("Tangent","")
        a11=cvo.CVO().CreateCVO("Line that intersects Circle at a point","")
        a10.cvolist.append(a11)
        a11.setcircleradius(1.5)
        self.construct1(a10,a10)
        self.fadeOutCurrentScene()
    def CircleWithTangent(self):
        text = Text("Construction of Tangent", font_size=22)
        text.add(Underline(text, buff=0.1))
        text.to_corner(UP)
        self.play(Write(text))

        text6=Text("Steps",font_size=22).to_edge(RIGHT)
        text6.add(Underline(text6,buff=0.1))
        text2=Text("1)Draw a circle", font_size=22).next_to(text6,DOWN)
        text3=Text("2)Take a point ", font_size=22).next_to(text2,DOWN)
        text4=Text("3)Draw a perpendicular line from it", font_size=22).next_to(text3,DOWN)
        text5=Text("4)Tangent is formed", font_size=22).next_to(text4,DOWN)
        
        r1 = 2
        circle = Circle(radius=r1, color=BLUE)
        circle.to_edge(ORIGIN)

        tangent_point = circle.point_at_angle(PI / 4)  
        tangent_line = Line(
            start=tangent_point + UP * 1.5, 
            end=tangent_point + DOWN * 1.5, 
            color=RED
        )
                
        circle.shift(LEFT*2)

        text6.shift(LEFT*1.5)
        text2.shift(LEFT*1.5)
        text3.shift(LEFT*1.25)
        text4.shift(LEFT*1.5)
        text5.shift(LEFT*1.5)
        text6.shift(UP*2)
        text2.shift(UP*2)
        text3.shift(UP*2)
        text4.shift(UP*2)
        text5.shift(UP*2)

        
        tangent_line.rotate(PI / 4, about_point=tangent_point)

       
        tangent_dot = Dot(point=tangent_point, color=YELLOW)
        tangent_dot.shift(LEFT*2)
        tangent_line.shift(LEFT*2)
        self.play(Write(text6))
        self.play(Write(text2))
        self.play(Create(circle,run_time=3))
        self.play(Write(text3))  
        self.play(FadeIn(tangent_dot))
        self.play(Write(text4))  
        self.play(Create(tangent_line,run_time=3))
        self.play(Write(text5))  

        self.wait(2)
    def tangentexternal(self): 
        text = Text("Finding Tangent From External Point", font_size=22)
        underline = Underline(text)
        text = VGroup(text, underline)
        text.to_corner(UP)
        self.add(text)    
        radius = 0.5
        distance_to_external_point = 2
        external_point = RIGHT * distance_to_external_point

        # Create a circle with the specified radius
        circle = Circle(radius=radius, color=BLUE)
        circle.shift(LEFT * (distance_to_external_point - radius))

        # Create a dot at the external point
        external_dot = Dot(point=external_point, color=YELLOW)

        # Calculate the length of the tangent using Pythagorean theorem
        tangent_length = (distance_to_external_point**2 - radius**2)**0.5

        # Define the tangent points on the circle
        tangent_angle = np.arccos(radius / distance_to_external_point)
        tangent_point_1 = circle.point_at_angle(tangent_angle)
        tangent_point_2 = circle.point_at_angle(-tangent_angle)

        # Create the tangent lines
        tangent_line_1 = Line(external_point, tangent_point_1, color=RED)
        tangent_line_2 = Line(external_point, tangent_point_2, color=RED)

        # Create text labels
        radius_label = MathTex("3\\,cm").next_to(circle, DOWN, buff=0.5)
        # external_point_label = MathTex("External Point").next_to(external_dot, UP, buff=0.5)
        tangent_label_1 = MathTex(f"Tangent = {tangent_length:.2f}\\,cm").next_to(tangent_line_1, RIGHT, buff=0.1)
        # tangent_label_2 = MathTex(f"Tangent = {tangent_length:.2f}\\,cm").next_to(tangent_line_2, RIGHT, buff=0.1)
        radius_6cm_label = MathTex("Radius = 6\\,cm").next_to(tangent_line_1.get_center() + DOWN, buff=0.5)
        # Add all elements to the scene
        self.play(Create(circle))  # Animate the drawing of the circle
        self.play(FadeIn(external_dot))  # Animate the appearance of the external point
        self.play(Create(tangent_line_1), Create(tangent_line_2))  # Animate the drawing of the tangent lines
        self.play(Write(tangent_label_1))  # Write the tangent lengths
        self.play(Write(radius_label))  # Write the radius label
        self.play(Write(radius_6cm_label))
        # Use Pythagorean theorem
        theorem = MathTex("a^2 + b^2 = c^2")
        theorem.shift(LEFT * 4)
        # self.Positionchoice = [[-5,1,0]] 
        calculation = MathTex(f"3^2 + b^2 = 6^2")
        calculation.next_to(theorem, DOWN, buff=0.5)
        solution = MathTex(f"b = \\sqrt{{6^2 - 3^2}} = {tangent_length:.2f}\\,cm")
        solution.next_to(calculation, DOWN, buff=0.5)

        self.play(Write(theorem))  # Write the Pythagorean theorem
        self.play(Write(calculation))  # Write the equation with values
        self.play(Write(solution))  # Write the solution

        # Wait for a moment before ending the scene
        self.wait(2)
    def secant(self):
        self.isRandom = False
        self.positionChoice = [[-5,0,0],[3,0,0]]
        s10=cvo.CVO().CreateCVO("Secant","")
        s11=cvo.CVO().CreateCVO("Definition","A straight line that cuts a Circle in two or more parts")
        s10.cvolist.append(s11)
        self.construct1(s10,s10)
        self.fadeOutCurrentScene()
    def constructionofsecant(self):
        text = Text("Construction of Secant", font_size=22)
        text.add(Underline(text, buff=0.1))
        text.to_corner(UP)
        self.play(Write(text))

        text2=Text("1)Draw a circle", font_size=22).to_edge(RIGHT)
        text3=Text("2)Take any two points ", font_size=22).next_to(text2,DOWN)
        text4=Text("3)Draw a perpendicular line from it", font_size=22).next_to(text3,DOWN)
        text5=Text("4)Secant is formed", font_size=22).next_to(text4,DOWN)

        text2.shift(LEFT)
        text3.shift(LEFT)
        text4.shift(LEFT)
        text5.shift(LEFT)
        
        circle = Circle(radius=2, color=BLUE)
        circle.move_to(ORIGIN)
        
        # Create points A and B on the circle
        point_a = Dot(circle.point_at_angle(PI/3), color=RED)
        point_b = Dot(circle.point_at_angle(-PI/4), color=RED)
        
        # Create labels for points A and B
        label_a = Text("A").next_to(point_a, RIGHT)
        label_b = Text("B").next_to(point_b, RIGHT)
        
        # Create secant line AB
        secant_line = Line(point_a.get_center(), point_b.get_center(), color=GREEN)
        
        # Draw the circle
        self.play(Write(text2))
        self.play(Create(circle))
        
        # Draw points A and B
        self.play(Write(text3))
        self.play(FadeIn(point_a), FadeIn(point_b))
        
        # Add labels for points A and B
        self.play(Write(label_a), Write(label_b))
        
        # Draw the secant line
        self.play(Write(text4))
        self.play(Create(secant_line))
        self.play(Write(text5))
        
        # Pause to display the final construction
        self.wait(2)
        self.fadeOutCurrentScene()
    def area(self):
        self.isRandom = False
        self.positionChoice = [[-5,0,0],[5,2,0],[5,0,0],[-5,-3,0]]
        n10=cvo.CVO().CreateCVO("Area","")
        n11=cvo.CVO().CreateCVO("Rectangle","")
        n12=cvo.CVO().CreateCVO("Square","")
        n13=cvo.CVO().CreateCVO("Triangle","")
        n10.cvolist.append(n11)
        n10.cvolist.append(n12)
        n10.cvolist.append(n13)
        self.construct1(n10,n10)
        self.fadeOutCurrentScene()
    def rectangle(self):
        self.isRandom = False
        self.positionChoice = [[-4,-2,0],[4,2,0]]
        r10=cvo.CVO().CreateCVO("Rectangle","")
        r11=cvo.CVO().CreateCVO("Formula","L*B")
        r10.cvolist.append(r11)
        self.construct1(r10,r10)
        self.fadeOutCurrentScene()
        text = Text("Rectangle Example with L=3,B=5", font_size=22)
        underline = Underline(text)
        text = VGroup(text, underline)
        text.to_corner(UP)
        self.add(text)
        text1 = Text("Area=L*B",font_size=22).to_edge(RIGHT)
        adding_text = MathTex(r"3 \times 5 = 15", font_size=48).next_to(text1,DOWN)
        
        text1.shift(LEFT*2)

        rectangle = Rectangle(height=3, width=5, color=BLUE)
        
        # Create braces for length and breadth
        length_brace = Brace(rectangle, direction=DOWN, color=YELLOW)
        breadth_brace = Brace(rectangle, direction=LEFT, color=YELLOW)
        
        # Create labels for length and breadth
        length_label = length_brace.get_text("5 units")
        breadth_label = breadth_brace.get_text("3 units")
        
        adding_text.move_to(rectangle.get_center())
        # Add the rectangle to the scene
        self.play(Create(rectangle))
        
        # Add braces and labels to the scene
        self.play(Create(length_brace), Write(length_label))
        self.play(Create(breadth_brace), Write(breadth_label))
        self.play(Write(text1))
        self.play(Write(adding_text))
        # Pause to display the result
        self.wait(2)
        self.fadeOutCurrentScene()
    def square(self):
        self.isRandom = False
        self.positionChoice = [[-4,-2,0],[4,2,0]]
        s10=cvo.CVO().CreateCVO("Sqaure","")
        s11=cvo.CVO().CreateCVO("Formula","A=S*S")
        s10.cvolist.append(s11)
        self.construct1(s10,s10)
        self.fadeOutCurrentScene()
        text = Text("Sqaure Example", font_size=22)
        underline = Underline(text)
        text = VGroup(text, underline)
        text.to_corner(UP)
        self.add(text)
        square = Square(side_length=2)

        text2 = Text("Area=S*S",font_size=22).to_edge(RIGHT)
        adding_text = MathTex(r"4 \times 4 = 16", font_size=30).next_to(text2,DOWN)
        
        text2.shift(LEFT*2)
        
        # Create the sides of the square (edges)
        top_edge = Line(square.get_corner(UP + LEFT), square.get_corner(UP + RIGHT), color=YELLOW)
        right_edge = Line(square.get_corner(UP + RIGHT), square.get_corner(DOWN + RIGHT), color=YELLOW)
        
        adding_text.move_to(square.get_center())
        # Add the square to the scene
        self.play(Create(square))
        self.wait(1)
        
        # Highlight each side of the square
        self.play(Create(top_edge))
        self.wait(1)
        self.play(Transform(top_edge, right_edge))
        self.wait(1)
        self.play(Write(text2))
        self.play(Write(adding_text))
        
        
        # Wait before ending the scene
        self.wait(2)
        self.fadeOutCurrentScene()
    def triangle(self):
        self.isRandom = False
        self.positionChoice = [[-4,-2,0],[4,2,0]]
        s10=cvo.CVO().CreateCVO("Triangle","")
        s11=cvo.CVO().CreateCVO("Formula","A=1/2L*B")
        s10.cvolist.append(s11)
        self.construct1(s10,s10)
        self.fadeOutCurrentScene()
        text = Text("Triangle Example", font_size=22)
        underline = Underline(text)
        text = VGroup(text, underline)
        text.to_corner(UP)
        self.add(text)
        formula = MathTex(r"\text{Area} = \frac{1}{2} \times \text{base} \times \text{height}", font_size=34)
        text = MathTex(r" = 0.5 \times 2*4 ", font_size=30).next_to(formula,DOWN).next_to(formula,DOWN)
        text1 = MathTex(r"4", font_size=70,color=GREEN)

        formula.shift(LEFT*4)
        text.shift(LEFT*4)
        text1.shift(RIGHT)
        underline = Underline(text1)
        text1 = VGroup(text1, underline)

        A = np.array([-2, -1, 0])
        B = np.array([2, -1, 0])
        C = np.array([2, 2, 0])

        # Create the triangle using Polygon
        triangle = Polygon(A, B, C)
        # triangle.shift(LEFT*1)
        
        # Labels for the vertices
        label_A = MathTex("A").next_to(A, LEFT)
        # label_A.shift(LEFT*1)
        label_B = MathTex("B").next_to(B, RIGHT)
        # label_B.shift(RIGHT*1)
        label_C = MathTex("C").next_to(C, UP)
        # label_C.shift(UP*1)
        # Create side labels
        length_label = MathTex("Length").next_to(Line(A, B).get_center(), DOWN)
        # length_label.shift(DOWN*1)
        breadth_label = MathTex("Breadth").next_to(Line(B, C).get_center(), RIGHT)
        # breadth_label.shift(UP*1)
        # Highlight the length and breadth using different colors
        length_highlight = Line(A, B, color=YELLOW, stroke_width=6)
        breadth_highlight = Line(B, C, color=RED, stroke_width=6)
        # text1.move_to(triangle.get_center())

        # Add the triangle and labels to the scene
        self.play(Create(triangle))
        self.play(Write(label_A), Write(label_B), Write(label_C))
        
        # Highlight the length
        self.play(Create(length_highlight))
        self.play(Write(length_label))

        # Highlight the breadth
        self.play(Create(breadth_highlight))
        self.play(Write(breadth_label))
        self.play(Write(formula))
        self.play(Write(text))
        self.play(Write(text1))

        # Pause for a moment to display the result
        self.wait(2)
        self.fadeOutCurrentScene()
    def SetDeveloperList(self): 
       self.DeveloperList="Abhiram" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Class10Chap9SecantsandTangents"
if __name__ == "__main__":
     scene = secantsandtangents()
     scene.render()
    