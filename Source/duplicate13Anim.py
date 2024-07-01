from manim import *

class duplicate13(Scene):
    def construct(self):

        circle1 = Text("Circle",font_size=40).to_edge(UP*1)
        sub_title1 = Text("A circle is a shape consisting of all points in a plane that are",font_size=29).to_edge(UP*3.0)
        sub_title2 = Text("equidistant from a fixed point called the center"'.',font_size=29).to_edge(UP*4.5)

        self.play(Write(circle1))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)
        self.play(FadeOut(circle1), FadeOut(sub_title1), FadeOut(sub_title2))


        # Draw the circle
        circle = Circle()
        self.play(Create(circle))
        self.wait(1)



        center = Text("Center",font_size=40).to_edge(UP*1)
        sub_title1 = Text("The center of a circle is a point that is equidistant from all points on the circle"'.',font_size=29).to_edge(UP*3.0)

        self.play(Write(center))
        self.play(Write(sub_title1))
        self.wait(1)


        # Show center
        center_dot = Dot(circle.get_center(), color=YELLOW)
        center_label = Text("Center",font_size=30).next_to(center_dot, DOWN)
        self.play(FadeIn(center_dot), Write(center_label))
        self.wait(1)
        self.play(FadeOut(center_dot), FadeOut(center_label))
        self.play(FadeOut(center), FadeOut(sub_title1))


        radius = Text("Radius",font_size=40).to_edge(UP*1)
        sub_title1 = Text("The distance from the center to any point on the circle is called the radius"'.',font_size=29).to_edge(UP*3.0)
        

        self.play(Write(radius))
        self.play(Write(sub_title1))
        self.wait(1)

        
        # Show radius
        radius_line = Line(circle.get_center(), circle.get_right(), color=BLUE)
        radius_label = Text("Radius",font_size=30).next_to(radius_line, UP)
        self.play(Create(radius_line), Write(radius_label))
        self.wait(1)
        self.play(FadeOut(radius_line), FadeOut(radius_label))
        self.play(FadeOut(radius), FadeOut(sub_title1))


        diameter = Text("Diameter",font_size=40).to_edge(UP*1)
        sub_title1 = Text("The diameter of a circle is the straight line distance that passes through",font_size=29).to_edge(UP*3.0)
        sub_title2 = Text("the center of the circle, connecting two points on its circumference"'.',font_size=29).to_edge(UP*4.5)
        

        self.play(Write(diameter))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)


        
        # Show diameter
        diameter_line = Line(circle.get_left(), circle.get_right(), color=RED)
        diameter_label = Text("Diameter",font_size=30).next_to(diameter_line, DOWN)
        self.play(Create(diameter_line), Write(diameter_label))
        self.wait(1)
        self.play(FadeOut(diameter_line), FadeOut(diameter_label))
        self.play(FadeOut(diameter), FadeOut(sub_title1), FadeOut(sub_title2))


        circumference = Text("Circumference",font_size=40).to_edge(UP*1)
        sub_title1 = Text("The circumference of a circle is the total distance around the circle"'.',font_size=29).to_edge(UP*3.0)
        sub_title2 = Text("It is the circle's perimeter"'.',font_size=29).to_edge(UP*4.5)
        

        self.play(Write(circumference))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)



        # Create the circumference label
        circumference_label = Text("Circumference",font_size=40).next_to(circle, RIGHT)
        self.play(Write(circumference_label))
        self.wait(1)
        self.play(FadeOut(circumference_label))
        self.play(FadeOut(circumference), FadeOut(sub_title1), FadeOut(sub_title2))

        
        chord = Text("Chord",font_size=40).to_edge(UP*1)
        sub_title1 = Text("A chord of a circle is a straight line segment whose endpoints both lie",font_size=29).to_edge(UP*3.0)
        sub_title2 = Text("on the circumference of the circle"'.',font_size=29).to_edge(UP*4.5)
        
        self.play(Write(chord))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)


        # Show chord
        chord_line = Line(circle.point_at_angle(PI/4), circle.point_at_angle(3*PI/4), color=GREEN)
        chord_label = Text("Chord",font_size=30).next_to(chord_line, UP)
        self.play(Create(chord_line), Write(chord_label))
        self.wait(1)
        self.play(FadeOut(chord_line), FadeOut(chord_label))
        self.play(FadeOut(chord), FadeOut(sub_title1), FadeOut(sub_title2))


        sector1 = Text("Sector",font_size=40).to_edge(UP*1)
        sub_title1 = Text("A sector of a circle is a region bounded by two radii of the circle and",font_size=29).to_edge(UP*3.0)
        sub_title2 = Text("the arc between their endpoints"'.',font_size=29).to_edge(UP*4.5)
        
        self.play(Write(sector1))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)

        
        # Show sector
        sector = Sector(angle=PI/4, color=PURPLE, arc_center=circle.get_center())
        sector_label = Text("Sector",font_size=30).next_to(sector, DOWN)
        self.play(FadeIn(sector), Write(sector_label))
        self.wait(1)
        self.play(FadeOut(sector), FadeOut(sector_label))
        self.play(FadeOut(sector1), FadeOut(sub_title1), FadeOut(sub_title2))


        segment1 = Text("Segment",font_size=40).to_edge(UP*1)
        sub_title1 = Text("A segment of a circle is a region bounded by a chord and",font_size=29).to_edge(UP*3.0)
        sub_title2 = Text("the arc that the chord subtends"'.',font_size=29).to_edge(UP*4.5)
        
        self.play(Write(segment1))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)


        # Show segment
        segment = Polygon(circle.get_center(), circle.point_at_angle(PI/4), circle.point_at_angle(3*PI/4), color=ORANGE)
        segment_label = Text("Segment",font_size=30).next_to(segment, DOWN)
        self.play(Create(segment), Write(segment_label))
        self.wait(1)
        self.play(FadeOut(segment), FadeOut(segment_label))
        self.play(FadeOut(segment1), FadeOut(sub_title1), FadeOut(sub_title2))

        
        semicircularregion = Text("semi-circular region",font_size=40).to_edge(UP*1)
        sub_title1 = Text("A semi-circular region is half of a circle, bounded by a diameter and the arc",font_size=29).to_edge(UP*3.0)
        sub_title2 = Text("connecting the endpoints of the diameter"'.',font_size=29).to_edge(UP*4.5)
        
        self.play(Write(semicircularregion))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)


        
        # Show semi-circular region
        semicircle = Arc(arc_center=circle.get_center(), radius=1, start_angle=0, angle=PI, color=TEAL)
        semicircle_label = Text("Semi-circular Region",font_size=30).next_to(semicircle, DOWN)
        self.play(Create(semicircle), Write(semicircle_label))
        self.wait(1)
        self.play(FadeOut(semicircle), FadeOut(semicircle_label))
        self.play(FadeOut(semicircularregion), FadeOut(sub_title1), FadeOut(sub_title2))
        self.play(FadeOut(circle))


if __name__ == "__main__":
    from manim import *
    scene = duplicate13()
    scene.render()