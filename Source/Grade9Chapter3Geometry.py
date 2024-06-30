from manim import *
from numpy import size
from AbstractAnim import AbstractAnim


import cvo

class geometry(AbstractAnim):  
    def construct(self):
        self.RenderSkillbancLogo()
        self.geo()
        self.Axiom()
        self.postulate()
        self.GithubSourceCodeReference()
        

    def geo(self):

        self.isRandom=False

        p1=cvo.CVO().CreateCVO("Building Blocks of Geometry","").setPosition([0,2.5,0])

        p2=cvo.CVO().CreateCVO("point","").setPosition([-4,1,0])
        p1.cvolist.append(p2)

        p3=cvo.CVO().CreateCVO("line","").setPosition([4,1,0])
        p1.cvolist.append(p3)

        p4=cvo.CVO().CreateCVO("Stright line","").setPosition([-4,-1,0])
        p1.cvolist.append(p4)

        p5=cvo.CVO().CreateCVO("surface","").setPosition([4,-1,0])
        p1.cvolist.append(p5)

        p6=cvo.CVO().CreateCVO("plane surface","").setPosition([0,-3,0])
        p1.cvolist.append(p6)

        self.construct1(p1,p1)

        self.fadeOutCurrentScene()

    def Axiom(self):
        self.isRandom = False

        p1 = cvo.CVO().CreateCVO("Axioms discovered by", "EUCLID")
        p1.setPosition([0, 2.5, 0])

        p2 = cvo.CVO().CreateCVO("Axiom: 1", "Things which are equal to the same things are equal to one another")
        p2.setPosition([-4,0.5, 0])
        p1.cvolist.append(p2)

        p3 = cvo.CVO().CreateCVO("Axiom: 2", "If equals are added to equals, the wholes are also equal")
        p3.setPosition([-4, -1, 0])
        p1.cvolist.append(p3)

        p4 = cvo.CVO().CreateCVO("Axiom: 3", "If equals are subtracted from equals, the remainders are also equal.")
        p4.setPosition([-4, -3, 0])
        p1.cvolist.append(p4)

        p5 = cvo.CVO().CreateCVO("Axiom: 4", "Things which coincide with one another are equal to one another")
        p5.setPosition([4, 0.5, 0])
        p1.cvolist.append(p5)

        p6 = cvo.CVO().CreateCVO("Axiom: 5", "Things which are double of the same things are equal to one another")
        p6.setPosition([4, -1, 0])
        p1.cvolist.append(p6)

        p7 = cvo.CVO().CreateCVO("Axiom: 6", "Things which are halves of the same things are equal to one another")
        p7.setPosition([4, -3, 0])
        p1.cvolist.append(p7)

        self.construct1(p1,p1)
     
        self.fadeOutCurrentScene()

    def postulate(self):
         
        self.isRandom=False

        p11=cvo.CVO().CreateCVO("postulates","Euclid has given 5 postulates")
        p11.setPosition([0,3,0])

        p12=cvo.CVO().CreateCVO("postulate-1","There is a unique line that passes through the given two distinct points.").setPosition([-4,1,0])
        p11.cvolist.append(p12)

        p13=cvo.CVO().CreateCVO("postulate-2","A line segment can be extended on either side to form a line.").setPosition([-4,-1,0])
        p11.cvolist.append(p13)

        p14=cvo.CVO().CreateCVO("postulate-3","We can describe a circle with any centre and radius.").setPosition([0,-3,0])
        p11.cvolist.append(p14)

        p15=cvo.CVO().CreateCVO("postulate-4","All right angles are equal to one another").setPosition([4,1,0])
        p11.cvolist.append(p15)

        p16=cvo.CVO().CreateCVO("postulate-5","If a line passes through two intersecting straight lines then the sum of internal agles on that side is less than 180 degrees").setPosition([4,-1,0])
        p11.cvolist.append(p16)

        self.construct1(p11,p11)
        self.fadeOutCurrentScene()

    def SetDeveloperList(self):
        self.DeveloperList="Bhaskar"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade9Chapter3Geometry.py"
      
if __name__ == "__main__":
    scene = geometry()
    scene.render()