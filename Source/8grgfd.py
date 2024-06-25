
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class graphrep_gfd(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.constructDataByCVO()
        self.GitHubSourceCodeReference()
    def constructDataByCVO(self):
        self.isRandom=False
        p1=cvo.CVO().CreateCVO("Graphical Rep. of Grouped Frequency Distribution","").setPosition([0,2.5,0])
        p2=cvo.CVO().CreateCVO("Histogram","Representation of continuous C.I").setPosition([-3,1,0])
        p3=cvo.CVO().CreateCVO("Frequency Polygon","Like a histogram, but connecting class midpoints with lines").setPosition([-3,-1.5,0])
        p4=cvo.CVO().CreateCVO("Frequency Curve","Like a freqency polygon, but connecting with curved lines ").setPosition([3,-1.5,0])
        p5=cvo.CVO().CreateCVO("Graph of Cumulative Frequency Distribution","Cumulative frequency graph (ogive) visualizes data").setPosition([3,1,0])
        p1.cvolist.append(p2)
        p1.cvolist.append(p3)
        p1.cvolist.append(p4)
        p1.cvolist.append(p5)
       

        self.construct1(p1,p1)
        self.fadeOutCurrentScene()

    def GitHubSourceCodeReference(self):
        
        p1 = cvo.CVO().CreateCVO("SOURCE CODE REFERENCE", ""). setPosition([0,2.5,0])
        p2 = cvo.CVO().CreateCVO("Github URL", "https://github.com/Skillbanc/manim-templates").setPosition([-3,0,0])
        p3 = cvo.CVO().CreateCVO("File Name", "FREQUENCY DISTRIBUTION TABLES AND GRAPHS").setPosition([3,-1.5,0])
        p1.cvolist.append(p2)
        p1.cvolist.append(p3)

        p2.setcircleradius(2)
        p3.setcircleradius(2)
        self.construct1(p1,p1)
      
if __name__ == "__main__":
    scene =graphrep_gfd()
    scene.render()
