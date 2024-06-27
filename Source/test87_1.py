from manim import *

class test87_1(Scene):
    def construct(self):
        # Create a colorful background
        background = Rectangle(width=14, height=8, fill_color="#E6F3FF", fill_opacity=1)
        self.add(background)

        # Title
        title = Text("Non-standard measuring", font_size=48, color=BLUE_E).to_edge(UP)
        self.play(Write(title))

        # Create a simple arm using shapes
        arm = self.create_arm()
        self.play(Create(arm))

        measurements = [
            ("Hand Breadth", 0.5, BLUE),
            ("Hand Span", 1.5, GREEN),
            ("Cubit", 3, RED),
            ("Foot", 2, YELLOW)
        ]

        for name, length, color in measurements:
            # Create measurement object
            measure = Rectangle(width=length, height=0.5, fill_color=color, fill_opacity=0.8)
            measure.next_to(arm, RIGHT, buff=0.5)
            
            # Create label
            label = Text(name, font_size=36, color=BLACK).next_to(measure, UP)
            
            # Show measurement and label
            self.play(GrowFromCenter(measure), Write(label))
            
            # Show dotted lines connecting arm to measurement
            lines = DashedLine(arm.get_right(), measure.get_left(), dash_length=0.1)
            self.play(Create(lines))
            
            # Add a fun fact
            fact = Text(f"We can measure with our {name.lower()}!", 
                        font_size=24, color=DARK_BROWN).to_edge(DOWN)
            self.play(Write(fact))
            
            self.wait(2)
            
            # Clear for next measurement
            self.play(FadeOut(measure), FadeOut(label), FadeOut(lines), FadeOut(fact))

        # Conclusion
        conclusion = Text("Using our body parts", font_size=48, color=BLUE_E)
        self.play(Write(conclusion))
        self.wait(2)

    def create_arm(self):
        # Create a simple arm using rectangles and circles
        upper_arm = Rectangle(width=0.8, height=2, fill_color=LIGHT_BROWN, fill_opacity=1)
        elbow = Circle(radius=0.4, fill_color=LIGHT_BROWN, fill_opacity=1)
        forearm = Rectangle(width=0.7, height=1.8, fill_color=LIGHT_BROWN, fill_opacity=1)
        hand = Circle(radius=0.5, fill_color=LIGHT_BROWN, fill_opacity=1)

        elbow.next_to(upper_arm, DOWN, buff=0)
        forearm.next_to(elbow, DOWN, buff=0)
        hand.next_to(forearm, DOWN, buff=0)

        arm = VGroup(upper_arm, elbow, forearm, hand)
        arm.to_edge(LEFT)
        return arm
        
if __name__ == "__main__":
    scene = test87_1()
    scene.render()