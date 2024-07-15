from manim import *
from AbstractAnim import AbstractAnim
import cvo


class AnglesInSurroundings(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.figure1()
        self.fadeOutCurrentScene()
        self.ClockHands()
        self.fadeOutCurrentScene()
        self.angletypes()
        self.fadeOutCurrentScene()
        self.rightangle()
        self.fadeOutCurrentScene()
        self.rightanglesin()
        self.fadeOutCurrentScene()
        self.lessrightangle()
        self.fadeOutCurrentScene()
        self.morerightangle()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()






    def Introduction(self):
        self.setNumberOfCirclePositions(3)
        self.angleChoice = [TAU/4,TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Angle","")
        p11=cvo.CVO().CreateCVO("Definition", "The figure formed by two rays which \n are sharing a common vertex").setPosition([3,2,0])
        p12=cvo.CVO().CreateCVO("Units", "Degrees^{0} ").setPosition([3,-2,0])
        p12.SetIsMathText(True)

        
        p10.setcircleradius(1)
        p11.setcircleradius(2)
        p12.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)

    def figure1(self):

        title=Text("What is an Angle?", font_size=36).to_edge(UP)
        underline = Line(
            start=title.get_left() + DOWN * 0.3,
            end=title.get_right() + DOWN * 0.3,
            color=YELLOW
        )
        
        self.play(Write(title), Create(underline))

        #self.play(Write(title))

         # Create rays
        vertex = np.array([-2, -1, 0])
        ray1 = Line(start=vertex, end=vertex + np.array([2, 3, 0]), color=BLUE)
        ray2 = Line(start=vertex, end=vertex + np.array([4, 0, 0]), color=BLUE)

        arrow1 = Arrow(ray1.get_start(), ray1.get_end(), buff=0)
        arrow2 = Arrow(ray2.get_start(), ray2.get_end(), buff=0)


        # Create angle arc
        angle = ray1.get_angle() - ray2.get_angle()
        arc = Arc(start_angle=ray2.get_angle(), angle=angle, radius=0.5, color=BLUE, arc_center=vertex)
        
        # Create angle label
        angle_label = MathTex(r"\theta^{0}", color=BLUE).next_to(arc.point_from_proportion(0.5), direction=arc.get_center() - vertex, buff=0.1)

        # Create vertex point
        vertex_point = Dot(vertex, color=RED)
        vertex_label = MathTex("A", color=RED).next_to(vertex_point, DOWN+LEFT*0.1, buff=0.1)


        # Angle definition text (adjusted for fitting)
        definition_text = """
        An angle is the figure formed by two rays, which are sharing a common vertex."""
        definition_label = Text(definition_text, font_size=28).to_edge(DOWN, buff=2)

        # Display everything
        #self.play(Create(ray1), Create(ray2))
        self.play(GrowArrow(arrow1), GrowArrow(arrow2))
        self.play(Create(arc), Write(angle_label), Create(vertex_point),Create(vertex_label))
        self.wait(1)
        self.play(Write(definition_label))
        self.wait(3)

    def ClockHands(self):

        title1 = Text("Angles In Our Surroundings").scale(0.75)
        
        # Display title
        self.play(Write(title1))
        self.wait(2)  # Pause to display the title

        # Fade out the title
        self.play(FadeOut(title1))
        

        # Title text with underline
        title = Text("Hands of a Clock", font_size=36).to_edge(UP)
        underline = Line(
            start=title.get_left() + DOWN * 0.3,
            end=title.get_right() + DOWN * 0.3,
            color=YELLOW
        )
        
        self.play(Write(title), Create(underline))

        # Create initial clock face (circle)
        clock_face = Circle(radius=1.75, color=WHITE, fill_opacity=0)
        
        # Create the hour markers
        hour_12 = Text("12", font_size=30).move_to(clock_face.point_at_angle(PI / 2))
        hour_3 = Text("3", font_size=30).move_to(clock_face.point_at_angle(0))
        hour_6 = Text("6", font_size=30).move_to(clock_face.point_at_angle(-PI / 2))
        hour_9 = Text("9", font_size=30).move_to(clock_face.point_at_angle(PI))

        # Adjust the position of the hour markers slightly inward
        for hour_marker in [hour_12, hour_3, hour_6, hour_9]:
            hour_marker.shift(0.3 * hour_marker.get_center() / np.linalg.norm(hour_marker.get_center()))

        # Animate clock face drawing and adding hour markers
        self.play(Create(clock_face), run_time=2)
        self.play(Write(hour_12), Write(hour_3), Write(hour_6), Write(hour_9))
        self.wait()

        # Create hour and minute hands for different times
        def create_hands(hour_angle, minute_angle):
            hour_hand = Arrow(
                start=clock_face.get_center(), 
                end=clock_face.get_center() + 1.0 * np.array([np.cos(hour_angle), np.sin(hour_angle), 0]), 
                buff=0, 
                color=BLUE
            )
            minute_hand = Arrow(
                start=clock_face.get_center(), 
                end=clock_face.get_center() + 1.5 * np.array([np.cos(minute_angle), np.sin(minute_angle), 0]), 
                buff=0, 
                color=GREEN
            )
            return hour_hand, minute_hand

        # Angles in radians for the minute hand (stationary at 12 o'clock)
        minute_angle = 90 * DEGREES  # -90 degrees to point to 12 o'clock

        # Angles in radians for the hour hand
        angle_3 = 0 * DEGREES      # 3 o'clock
        angle_4 = -30 * DEGREES    # 4 o'clock
        angle_6 = -90 * DEGREES    # 6 o'clock

        # Hands at 3 o'clock
        hour_hand_3, minute_hand_3 = create_hands(angle_3, minute_angle)  # 3 o'clock, minute hand fixed
        arc_3 = Arc(angle=PI/2, radius=0.5, color=RED, arc_center=clock_face.get_center(), start_angle=0)
        text_label_3 = Text("At 3 o'clock", font_size=30).next_to(clock_face, LEFT, buff=1)

        # Hands at 4 o'clock
        hour_hand_4, minute_hand_4 = create_hands(angle_4, minute_angle)  # 4 o'clock, minute hand fixed
        arc_4 = Arc(angle=2*PI/3, radius=0.5, color=RED, arc_center=clock_face.get_center(), start_angle=-PI/6)
        text_label_4 = Text("At 4 o'clock", font_size=30).next_to(clock_face, LEFT, buff=1)

        # Hands at 6 o'clock
        hour_hand_6, minute_hand_6 = create_hands(angle_6, minute_angle)  # 6 o'clock, minute hand fixed
        arc_6 = Arc(angle=PI, radius=0.5, color=RED, arc_center=clock_face.get_center(), start_angle=-PI/2)
        text_label_6 = Text("At 6 o'clock", font_size=30).next_to(clock_face, LEFT, buff=1)

        # Additional text after displaying 6 o'clock
        #additional_text = Text("The hands of a clock form different angles at different timings", font_size=32).next_to(clock_face, DOWN, buff=0.75)
        additional_text = Text("The hands of a clock form different angles at different timings", font_size=32).to_edge(DOWN, buff=1.25)

        # Animate hour and minute hands at 3 o'clock
        self.play(Write(text_label_3), run_time=1)
        self.play(Create(hour_hand_3), Create(minute_hand_3), run_time=2)
        self.play(Create(arc_3), run_time=2)
        self.wait(1)

        self.play(Write(additional_text))
        

        # Transition to hour and minute hands at 4 o'clock
        self.play(Transform(hour_hand_3, hour_hand_4), 
                  Transform(minute_hand_3, minute_hand_4), 
                  Transform(arc_3, arc_4), 
                  Transform(text_label_3, text_label_4), run_time=2)
        self.wait(2)

        # Transition to hour and minute hands at 6 o'clock
        self.play(Transform(hour_hand_3, hour_hand_6), 
                  Transform(minute_hand_3, minute_hand_6), 
                  Transform(arc_3, arc_6),  
                  Transform(text_label_3, text_label_6), run_time=2)
        self.wait(1)

        # Display additional text
        # self.play(Write(additional_text), run_time=2)
        # self.wait(2)

    def angletypes(self):
        self.setNumberOfCirclePositions(4)
        self.isRandom = False
        self.angleChoice = [TAU/4,TAU/4,TAU/4]

        p10=cvo.CVO().CreateCVO("Angles ","").setPosition([-2,0,0])
        p11=cvo.CVO().CreateCVO("Right Angle","Degree=90^{0}").setPosition([2,2,0])
        p12=cvo.CVO().CreateCVO("Acute Angle","Degree<90^{0}").setPosition([3,0,0])
        p13=cvo.CVO().CreateCVO("Obtuse Angle","Degree>90^{0}").setPosition([2,-2.5,0])
        p11.SetIsMathText(True)
        p12.SetIsMathText(True)
        p13.SetIsMathText(True)
         
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.construct1(p10,p10)

    def rightangle(self):
        title = Text("Right Angle").to_edge(UP)
        underline = Line(
            start=title.get_left() + DOWN * 0.3,
            end=title.get_right() + DOWN * 0.3,
            color=YELLOW
        )
        
        self.play(Write(title), Create(underline))

        
        # Define the vertex and create two rays forming a right angle
        vertex = np.array([-1, -1, 0])
        ray1 = Line(start=vertex, end=vertex + np.array([0, 3, 0]), color=WHITE)
        ray2 = Line(start=vertex, end=vertex + np.array([3, 0, 0]), color=WHITE)
        
        # Add arrow tips to the rays
        arrow1 = Arrow(ray1.get_start(), ray1.get_end(), buff=0)
        arrow2 = Arrow(ray2.get_start(), ray2.get_end(), buff=0)
        
        # Create a square arc to represent the 90-degree angle
        square_arc = Square(side_length=0.5).move_to(vertex+np.array([0.25, 0.25, 0])).set_fill(opacity=0).set_stroke(width=2)
        
        # Add a label for the angle
        #angle_label = MathTex("90^\circ").next_to(square_arc, UR, buff=0.1)
        angle_label = MathTex(r"\theta",color=BLUE).next_to(square_arc, UR, buff=0.1)
        angle_label1 = MathTex(r"\theta=90^\circ", color=BLUE, font_size=40).to_edge(RIGHT, buff=4)
        
        # Create the definition text
        definition = Text("A right angle is an angle of exactly 90 degrees.", font_size=30).to_edge(DOWN, buff=2)

        
        # Add the title, rays, square arc, angle label, and definition to the scene
        #self.play(Write(title))
        self.play(GrowArrow(arrow1), GrowArrow(arrow2))
        self.play(Create(square_arc))
        self.play(Write(angle_label))
        self.wait(1)
        self.play(Write(definition))
        self.play(Write(angle_label1))
        self.wait()

    def rightanglesin(self):
        title = Text("Right Angles in Square and Circle").to_edge(UP)
        underline = Line(
            start=title.get_left() + DOWN * 0.3,
            end=title.get_right() + DOWN * 0.3,
            color=YELLOW
        )
        
        self.play(Write(title), Create(underline))


        # Square with right angles at corners
        square = Square(side_length=3).shift(LEFT * 3)
        
        square_right_angles1 = Square(side_length=0.5).move_to(square.get_corner(UL) + np.array([0.25, -0.25, 0])).set_fill(opacity=0).set_stroke(width=2)
        square_right_angles2 = Square(side_length=0.5).move_to(square.get_corner(UR) + np.array([-0.25, -0.25, 0])).set_fill(opacity=0).set_stroke(width=2)
        square_right_angles3 = Square(side_length=0.5).move_to(square.get_corner(DL) + np.array([0.25, 0.25, 0])).set_fill(opacity=0).set_stroke(width=2)
        square_right_angles4 = Square(side_length=0.5).move_to(square.get_corner(DR) + np.array([-0.25, 0.25, 0])).set_fill(opacity=0).set_stroke(width=2)
        
        # Circle divided into quarters
        circle = Circle(radius=2).shift(RIGHT * 3)
        square_arc = Square(side_length=0.5).move_to(circle.get_center() +np.array([0.25, 0.25, 0])).set_fill(opacity=0).set_stroke(width=2)
        
        #quarter_arc = Arc(start_angle=0, angle=PI/2, radius=0.5, color=BLUE).shift(RIGHT * 3)
        radius1 = Line(start=circle.get_center(), end=circle.get_center() + 2 * RIGHT, color=WHITE)
        radius2 = Line(start=circle.get_center(), end=circle.get_center() + 2 * UP, color=WHITE)
        radius3 = Line(start=circle.get_center(), end=circle.get_center() + 2 * LEFT, color=WHITE)
        radius4 = Line(start=circle.get_center(), end=circle.get_center() + 2 * DOWN, color=WHITE)

        #arc_3 = Arc(angle=PI/2, radius=0.5, color=RED, arc_center=circle.get_center(), start_angle=0)
        
        # Angle label for circle
        angle_label = MathTex("90^\circ", color=BLUE).next_to(square_right_angles3, UP+ 1 * RIGHT, buff=0.1)
        angle_label1 = MathTex("90^\circ", color=BLUE).next_to(square_arc, UR, buff=0.1)

        # Definition text
        definition = Text("A right angle is formed at every corner of square and every quarter of circle.", font_size=30).to_edge(DOWN, buff=1)

        # Add all elements to the scene
       
        
        # Square and its right angles
        self.play(Create(square))
        self.play(Create(square_right_angles1), Create(square_right_angles2), Create(square_right_angles3), Create(square_right_angles4))
        self.play(Write(angle_label))
        # Circle and its components
        self.play(Create(circle))
        
        self.play(Create(radius1), Create(radius2),Create(radius3),Create(radius4),Create(square_arc))
        
       
        self.play(Write(angle_label1))

        # Definition text
        self.wait(1)
        self.play(Write(definition))
        self.wait()


    def lessrightangle(self):
        title = Text(" Acute Angle").to_edge(UP)
        underline = Line(
            start=title.get_left() + DOWN * 0.3,
            end=title.get_right() + DOWN * 0.3,
            color=YELLOW
        )
        
        self.play(Write(title), Create(underline))

        
        # Define the vertex and create two rays forming an angle less than 90 degrees
        vertex = np.array([-2, -1, 0])
        ray1 = Line(start=vertex, end=vertex + np.array([2,3,0]), color=WHITE)
        ray2 = Line(start=vertex, end=vertex + np.array([3,0,0]), color=WHITE)
        
        # Add arrow tips to the rays
        arrow1 = Arrow(ray1.get_start(), ray1.get_end(), buff=0)
        arrow2 = Arrow(ray2.get_start(), ray2.get_end(), buff=0)

        angle = ray1.get_angle() - ray2.get_angle()
        arc = Arc(start_angle=ray2.get_angle(), angle=angle, radius=0.5, color=BLUE, arc_center=vertex)
        
        # Create angle label
        angle_label = MathTex(r"\theta", color=BLUE).next_to(arc.point_from_proportion(0.5), direction=arc.get_center() - vertex, buff=0.1)

        angle_label1 = MathTex(r"\theta<90^\circ", color=BLUE, font_size=40).to_edge(RIGHT, buff=4)
        
        # Create an arc to represent the angle less than 90 degrees
        # arc = Arc(radius=0.5, angle=ray2.get_angle() - ray1.get_angle(), start_angle=ray1.get_angle(), color=BLUE)
        
        # # Add a label for the angle
        # angle_label = MathTex("\\theta").next_to(arc, UR, buff=0.1)
        
        # Create the definition text
        definition = Text("An angle less than 90 degrees is called an acute angle.", font_size=30).to_edge(DOWN, buff=2)
        
        # Add the title, rays, arc, angle label, and definition to the scene
        #self.play(Write(title))
        self.play(GrowArrow(arrow1), GrowArrow(arrow2))
        self.play(Create(arc))
        self.play(Write(angle_label))
        self.wait(1)
        self.play(Write(definition))
        self.play(Write(angle_label1))
        self.wait()

    def morerightangle(self):
        title = Text("Obtuse Angle").to_edge(UP)
        underline = Line(
            start=title.get_left() + DOWN * 0.3,
            end=title.get_right() + DOWN * 0.3,
            color=YELLOW
        )
        
        self.play(Write(title), Create(underline))

        
        # Define the vertex and create two rays forming an angle less than 90 degrees
        vertex = np.array([-1, -1, 0])
        ray1 = Line(start=vertex, end=vertex + np.array([-2,3,0]), color=WHITE)
        ray2 = Line(start=vertex, end=vertex + np.array([3,0,0]), color=WHITE)
        
        # Add arrow tips to the rays
        arrow1 = Arrow(ray1.get_start(), ray1.get_end(), buff=0)
        arrow2 = Arrow(ray2.get_start(), ray2.get_end(), buff=0)

        angle = ray1.get_angle() - ray2.get_angle()
        arc = Arc(start_angle=ray2.get_angle(), angle=angle, radius=0.5, color=BLUE, arc_center=vertex)
        
        # Create angle label
        angle_label = MathTex(r"\theta", color=BLUE).next_to(arc.point_from_proportion(0.5), direction=arc.get_center() - vertex, buff=0.1)

        angle_label1 = MathTex(r"\theta>90^\circ", color=BLUE, font_size=40).to_edge(RIGHT, buff=4)
        
        # Create an arc to represent the angle less than 90 degrees
        # arc = Arc(radius=0.5, angle=ray2.get_angle() - ray1.get_angle(), start_angle=ray1.get_angle(), color=BLUE)
        
        # # Add a label for the angle
        # angle_label = MathTex("\\theta").next_to(arc, UR, buff=0.1)
        
        # Create the definition text
        definition = Text("An angle more than 90 degrees is called an obtuse angle.", font_size=30).to_edge(DOWN, buff=2)
        
        # Add the title, rays, arc, angle label, and definition to the scene
        #self.play(Write(title))
        self.play(GrowArrow(arrow1), GrowArrow(arrow2))
        self.play(Create(arc))
        self.play(Write(angle_label))
        self.wait(1)
        self.play(Write(definition))
        self.play(Write(angle_label1))
        self.wait()



    def SetDeveloperList(self):  
        self.DeveloperList="Agraz Gopu"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade5Chapter6AnglesInSurroundings.py"


if __name__ == "__main__":
     scene =AnglesInSurroundings()
     scene.render()
