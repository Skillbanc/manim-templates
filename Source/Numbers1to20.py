from manim import *
from AbstractAnim import AbstractAnim
import cvo

class numbers(AbstractAnim):

    def construct(self):
        #self.RenderSkillbancLogo()
        #self.fadeOutCurrentScene()
        #self.six()
        #self.fadeOutCurrentScene()
        self.eight()
        self.fadeOutCurrentScene()


    def six(self):

        text =  Text("Look at the picture given below. Answer the following questions.",color=RED)
        text.scale(0.5)
        text.to_edge(UP)
        self.play(Write(text))
        self.wait(2)
        
        names = ["Ranga", "John", "Latha", "Basha", "Rama", "Uma"]
        
        # Define the starting position and spacing
        start_pos = LEFT * 5 + UP * 1.5
        spacing = RIGHT * 2
        
        # Create circles with text
        circles = []
        for i, name in enumerate(names):
            pos = start_pos + i * spacing
            circle = Circle(radius=1, color=WHITE).move_to(pos)
            text = Text(name).scale(0.5).move_to(pos)
            circles.append(VGroup(circle, text))
        
        # Add the circles to the scene
        for circle in circles:
            self.play(Create(circle))
        
        # Hold the final frame
        self.wait(2)


        text1 = Text("1. Who is the third student? .....Latha\n\n2. Who is the fifth student? .....Rama\n\n3. What is the ordinal number of Basha? .....Forth(4th)\n\n4. What is the ordinal number of Uma? .....Sixth(6th)", color=BLUE)
        text1.scale(0.5)
        text1.shift(DOWN  * 2)
        self.play(Write(text1))
        self.wait(3)


    def eight(self):
        
        text =  Text("Look at the picture given below. Write the ordinal number of the student shown.",color=RED)
        text.scale(0.5)
        text.to_edge(UP)
        self.play(Write(text))
        self.wait(2)

        names = ["Sita", "Hari", "Ramaa", "Giri", "Latha", "Uma", "Shiva", "Usha"]
        
        # Define the starting position and spacing
        start_pos = LEFT * 5.5 + UP * 1.5  # Move circles up by 1 unit and shift to the left
        spacing = RIGHT * 1.5
        
        # Create circles with text
        circles = []
        for i, name in enumerate(names):
            pos = start_pos + i * spacing
            circle = Circle(radius=0.7, color=WHITE).move_to(pos)
            text = Text(name).scale(0.5).move_to(pos)
            circles.append(VGroup(circle, text))
        
        # Add the circles to the scene
        for circle in circles:
            self.play(Create(circle))
        
        # Hold the final frame
        self.wait(2)


        text1 = Text("What is the ordinal number of Latha ? (Fifth5th)\n\nWhat is the ordinal number of Hari ?  Second(2nd)\n\nWhat is the ordinal number of Uma ?  Sixth(6th)\n\nWhat is the ordinal number of Giri ? Forth(4th)\n\nWhat is the ordinal number of Rama ?  Third(3rd)\n\nWhat is the ordinal number of Shiva ? seventh(7th)\n\nWhat is the ordinal number of Usha ?  Eighth(8th)")
        text1.scale(0.4)
        text1.shift(DOWN*2)
        self.play(Write(text1))
        self.wait(3)

if __name__ == "__main__":
    scene = numbers()
    scene.render()