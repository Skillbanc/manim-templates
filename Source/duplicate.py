from manim import *
import cvo
from AbstractAnim import AbstractAnim

class TableScene(AbstractAnim):
    def construct(self):
        self.Subtopics_2()





    def Subtopics_2(self):
        self.isRandom=False
        self.angleChoice = [TAU/4,TAU/4,TAU/4]
        self.setNumberOfCirclePositions(2)
        p10=cvo.CVO().CreateCVO("Knowing our Numbers","").setPosition([-4.3,1.8,0])
        p11=cvo.CVO().CreateCVO("Place value of larger numbers","").setPosition([0,2.4,0])
        p12=cvo.CVO().CreateCVO("Large Numbers Used In Daily Life Situations","").setPosition([2.15,-3,0])
        p13=cvo.CVO().CreateCVO("Indian vs. International Numeration Systems","").setPosition([3,-0.2,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)

        
        self.construct1(p10,p10)





if __name__ == "__main__":
    scene = TableScene()
    scene.render()
