from manim import *
from AbstractAnim import AbstractAnim
import cvo

class SAV(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.cube()
        self.fadeOutCurrentScene()
        self.areacube()
        self.fadeOutCurrentScene()
        self.tsacuboid()
        self.fadeOutCurrentScene()
        self.lsacuboid()
        self.fadeOutCurrentScene()
        self.tsacube()
        self.fadeOutCurrentScene()
        self.lsacube()
        self.fadeOutCurrentScene()
        self.volumecuboid()
        self.fadeOutCurrentScene()
        self.volumecube()
        self.fadeOutCurrentScene()
        self.SourceReference()
         

    def Introduction(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [-TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("SURFACE AREA AND VOLUME","")
        p11=cvo.CVO().CreateCVO("SHAPES", "")
        p11.extendOname(["CUBE","CUBOID"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def cube(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [-TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("CUBE AND CUBOID","")
        p11=cvo.CVO().CreateCVO("Operations", "")
        p11.extendOname(["AREA","VOLUME"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def areacube(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [-TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("AREA","")
        p11=cvo.CVO().CreateCVO("AREA TYPES", "")
        p11.extendOname(["LSA","TSA"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def tsacuboid(self):
        self.setNumberOfCirclePositions(5)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("total surface area of cuboid","2(lb+lh+bh)").setPosition([-4,0,0])
        p11=cvo.CVO().CreateCVO("h variable ","6").setPosition([0,2.5,0])
        p12=cvo.CVO().CreateCVO("l variable","2").setPosition([0,0,0])
        p14=cvo.CVO().CreateCVO("b variable", "4").setPosition([0,-2.5,0])
        p13=cvo.CVO().CreateCVO("TSA OF CUBOID","88").setPosition([4,0,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p14)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)),Create(CurvedArrow(p14.pos,p13.pos)))

    def lsacuboid(self):
        self.setNumberOfCirclePositions(5)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Lateral surface area of cuboid","2h(l+b)").setPosition([-4,0,0])
        p11=cvo.CVO().CreateCVO("h variable ","6").setPosition([0,2.5,0])
        p12=cvo.CVO().CreateCVO("l variable","2").setPosition([0,0,0])
        p14=cvo.CVO().CreateCVO("b variable", "4").setPosition([0,-2.5,0])
        p13=cvo.CVO().CreateCVO("LSA OF CUBOID","72").setPosition([4,0,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p14)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)),Create(CurvedArrow(p14.pos,p13.pos)))

    def tsacube(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("total surface area of cube","6a*a").setPosition([-4,0,0])
        p11=cvo.CVO().CreateCVO("Constant sides","6").setPosition([0,2,0])
        p12=cvo.CVO().CreateCVO("a variable","2").setPosition([0,-2,0])
        p13=cvo.CVO().CreateCVO("TSA OF CUBE", "24").setPosition([4,0,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))

    def lsacube(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("lateral surface area of cube","4a*a").setPosition([-4,0,0])
        p11=cvo.CVO().CreateCVO("Constant sides","4").setPosition([0,2,0])
        p12=cvo.CVO().CreateCVO("a variable","2").setPosition([0,-2,0])
        p13=cvo.CVO().CreateCVO("LSA OF CUBE", "16").setPosition([4,0,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))

    def volumecuboid(self):
        self.setNumberOfCirclePositions(5)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("volume of cuboid","l*b*h").setPosition([-4,0,0])
        p11=cvo.CVO().CreateCVO("h variable ","6").setPosition([0,2.5,0])
        p12=cvo.CVO().CreateCVO("l variable","2").setPosition([0,0,0])
        p14=cvo.CVO().CreateCVO("b variable", "4").setPosition([0,-2.5,0])
        p13=cvo.CVO().CreateCVO("VOLUME OF CUBOID","48").setPosition([4,0,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p14)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)),Create(CurvedArrow(p14.pos,p13.pos)))


    def volumecube(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("volume of cube","a*a*a").setPosition([-4,0,0])
        p12=cvo.CVO().CreateCVO("a variable","2").setPosition([0,0,0])
        p13=cvo.CVO().CreateCVO("VOLUME OF CUBE", "8").setPosition([4,0,0])
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p12.pos,p13.pos)))

    def SourceReference(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("SOURCE CODE REFERENCE","").setPosition([0,3,0])
        p12=cvo.CVO().CreateCVO("GITHUB URL","https://github.com/Skillbanc/manim-templates.git").setPosition([4,0,0])
        p13=cvo.CVO().CreateCVO("FILE NAME", "SAVanim.py").setPosition([4,0,0])
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p12.setcircleradius(3)
        p13.setcircleradius(2)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        #self.play(Create(CurvedArrow(p12.pos,p13.pos)))



if __name__ == "__main__":
    scene = SAV()
    scene.render()
