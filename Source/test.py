from AbstractAnim import AbstractAnim
import cvo
from manim import *

class MoveImageeee(AbstractAnim):
    def construct(self):
        self.construct1()

        
    def construct1(self):
        self.isRandom=False
        self.setNumberOfCirclePositions(4)
        p10 = cvo.CVO().CreateCVO("Subtraction ", "ab - c")

        # Step 2: Unit Digit Check
        p11 = cvo.CVO().CreateCVO("Unit Digit Check", "Is  b< c?")

        # Step 3: Carry Over
        p12 = cvo.CVO().CreateCVO("Carry Over", "Borrow from next digit(a)")

        # Step 4: Tenth Digit Adjustment
        p13 = cvo.CVO().CreateCVO("Tenth Digit Adjustment", "a becomes a-1,\\\\b becomes 1b")

        # Step 5: Perform Subtraction
        p14 = cvo.CVO().CreateCVO("Perform Subtraction", "ab - c = d")

        # Connect the concepts
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        p13.cvolist.append(p14)

        # Construct the diagram
        self.construct1(p10, p10)
        

# To render the scene
if __name__ == "__main__":
    scene = MoveImageeee()
    scene.render()
