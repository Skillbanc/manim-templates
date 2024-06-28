from manim import *
from AbstractAnim import AbstractAnim
import cvo

class Measurement(AbstractAnim):

        self.isRandom=False
        self.positionChoice = [[-4,-2,0],[4,-2,0],[3,2,0],[-4,2,0],[-3,2,0],[3,-2,0]]
        p10=cvo.CVO().CreateCVO("Measurements","").setangle(-TAU/5)
        p11=cvo.CVO().CreateCVO("Standard Instruments","Scale""Tape")
        p12=cvo.CVO().CreateCVO("Standard Weights","Kilograms")

        p10.setcircleradius(1.25)
        p11.setcircleradius(1.25)
        p12.setcircleradius(1.25)
    
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)

        self.construct(p10,p10)
        self.wait(1)
        self.clear_screen()

        # Create a scale (ruler)
        scale_length = 10
        scale = VGroup()
        for i in range(scale_length + 1):
            if i % 5 == 0:
                tick_length = 0.3
                label = Text(str(i), font_size=24).next_to(Line(ORIGIN, UP * tick_length), DOWN)
                label.shift(RIGHT * i)
                scale.add(label)
            else:
                tick_length = 0.15
            tick = Line(ORIGIN, UP * tick_length).shift(RIGHT * i)
            scale.add(tick)

        scale.shift(LEFT * scale_length / 2)
        
        # Create a measuring tape
        tape_length = 10
        tape_width = 0.5
        tape = Rectangle(width=tape_length, height=tape_width, color=YELLOW, fill_opacity=0.5)
        
        # Adding markings to the measuring tape
        tape_markings = VGroup()
        for i in range(tape_length + 1):
            if i % 5 == 0:
                tick_length = tape_width / 2
                label = Text(str(i), font_size=24).next_to(Line(UP * tape_width / 2, UP * (tape_width / 2 + tick_length)), UP)
                label.shift(RIGHT * i - RIGHT * tape_length / 2)
                tape_markings.add(label)
            else:
                tick_length = tape_width / 4
            tick = Line(UP * tape_width / 2, UP * (tape_width / 2 + tick_length)).shift(RIGHT * i - RIGHT * tape_length / 2)
            tape_markings.add(tick)
        
        # Position the tape below the scale
        tape.shift(DOWN * 2)
        tape_markings.shift(DOWN * 2)

        # Add the scale and tape to the scene
        self.play(Create(scale))
        self.wait(1)
        self.play(Create(tape))
        self.wait(1)
        self.play(Create(tape_markings))
        self.wait(2)

if __name__ == "__main__":
    from manim import *
    scene = Measurement()
    scene.render()