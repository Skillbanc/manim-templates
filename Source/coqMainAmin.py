from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo

class coqMainAmin(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.quadrilateral()
        self.fadeOutCurrentScene()
        self.toq()
        self.fadeOutCurrentScene()
        self.coq1()
        self.fadeOutCurrentScene()
        self.coq2()
        self.fadeOutCurrentScene()
        self.cospclq()

    def quadrilateral(self):
        
        p10=cvo.CVO().CreateCVO("Quadrilaterals","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("defination", " It consist of 4S,4A").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("ETI", "Latin words “quadri”=“four” and “latus”=“side”").setPosition([0,-2.5,0]).setangle(-TAU/3)
        p13=cvo.CVO().CreateCVO("keypoints", "Vertices\nSides\nDiagonals\nInterior Angles\n").setPosition([-4,3,0]).setangle(-TAU/4)

        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.construct1(p10,p10)

    def toq(self):
        

        p10=cvo.CVO().CreateCVO("Types of quadrilateral","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Trapezium", " one pair of opp S are llel").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("parallelogram", "two pair opp S are equal and llel").setPosition([5,-2,0])
        p13=cvo.CVO().CreateCVO("Rhombus", "ADJs are equal").setPosition([-4,3,0]).setangle(-TAU/4)
        p14=cvo.CVO().CreateCVO("Kite", "2 pairs of AdjS equal  and diagonals intersect at 90 deg").setPosition([-4,1,0]).setangle(-TAU/4)
        p15=cvo.CVO().CreateCVO("Rectangle", "parallelogram with 4 right angles").setPosition([-4,-1,0]).setangle(-TAU/4)
        p16=cvo.CVO().CreateCVO("Square", "rhombus with 4 right angles").setPosition([-4,-3,0]).setangle(-TAU/4)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        p10.cvolist.append(p16)
        self.construct1(p10,p10)

    def coq1(self):
        

        p10=cvo.CVO().CreateCVO("Construction quadrilateral","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Materials needed", "Ruler\n ,Pencil\n,Protractor\n,Compass\n").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("Step:1", "draw rough sketch").setPosition([5,-2,0])
        p13=cvo.CVO().CreateCVO("Step:2", "Analyse the fig and use spcl properties of it").setPosition([-4,3,0]).setangle(-TAU/4)
        p14=cvo.CVO().CreateCVO("Step:3", "use compass and protractor to obtain req fig").setPosition([-4,1,0]).setangle(-TAU/4)
        p15=cvo.CVO().CreateCVO("Step:4", "Join the pt's to complete").setPosition([-4,-1,0]).setangle(-TAU/4)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        self.construct1(p10,p10)

    def coq2(self):
        

        p10=cvo.CVO().CreateCVO("Quadrilateral Meaurements","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("4S AND 1A", "S.S.S.S.A").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("4S AND 1Diag", "S.S.S.S.Diag").setPosition([5,-2,0])
        p13=cvo.CVO().CreateCVO("3S AND 2Diag", "S.S.S.Diag.Diag").setPosition([-4,3,0]).setangle(-TAU/4)
        p14=cvo.CVO().CreateCVO("2AdjS AND 3A", "S.A.S.A.A").setPosition([-4,1,0]).setangle(-TAU/4)
        p15=cvo.CVO().CreateCVO("3S AND 2A", "S.A.S.A.S").setPosition([-4,-1,0]).setangle(-TAU/4)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        self.construct1(p10,p10)

    def cospclq(self):
        

        p10=cvo.CVO().CreateCVO("Spcl quadrilateral","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("rhombus", "").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("square", "").setPosition([5,-2,0])
        p13=cvo.CVO().CreateCVO("Unique quadrilateral", "5 independent measurements req").setPosition([-4,3,0]).setangle(-TAU/4)
        p14=cvo.CVO().CreateCVO("construction", "when 2Diag are given").setPosition([-4,1,0]).setangle(-TAU/4)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.construct1(p10,p10)
        self.construct1(p14,p14)
        self.play(Create(CurvedArrow(p11.pos,p14.pos)),Create(CurvedArrow(p12.pos,p14.pos)))
        #self.play()
        
    


if __name__ == "__main__":
    scene = coqMainAmin()
    scene.render()