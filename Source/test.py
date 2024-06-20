from AbstractAnim import AbstractAnim
import cvo
from manim import *

class MoveImageeee(AbstractAnim):
    def construct(self):
        self.construct2()
        
    def construct2(self):
        self.isRandom = False
        self.angleChoice=[TAU/2]
        p10=cvo.CVO().CreateCVO("Diagonals", "").setPosition([-3,2,0])
        p11=cvo.CVO().CreateCVO("Definition", "Line segment joining opposite vertices").setPosition([-3,-2,0])
        p10.cvolist.append(p11)
        
        diagonalline = Line(start=[-1,0.5,0], end=[2,1.5,0], color = RED )
        diagonalline.shift(RIGHT * 2)
        diaglabel=Tex("Diagonal").next_to(diagonalline, LEFT, buff=0.1).set_color(RED).scale(0.5).shift(RIGHT*1.8)
        
        Quadrilaterals = Polygon([-1, 0.5, 0], [1, 0.5, 0], [2, 1.5, 0], [-2,1.5,0], color=BLUE)
        Quadrilaterals.shift(RIGHT * 2 )
        quadlabel=Tex("Quadrilateral").next_to(Quadrilaterals, DOWN, buff = 0.1)
        
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        self.play(Create(Quadrilaterals),Create(quadlabel))
        self.play(Create(diagonalline),Create(diaglabel))
        self.wait(3)
        self.fadeOutCurrentScene()

# To render the scene
if __name__ == "__main__":
    from manim import *
    scene = MoveImageeee()
    scene.render()
