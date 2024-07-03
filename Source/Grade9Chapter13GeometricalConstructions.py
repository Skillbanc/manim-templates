
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class GeometricalConstructions3(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.constructDataByCVO()
        self.fadeOutCurrentScene()
        self.PerpenBi()
        self.fadeOutCurrentScene()
        self.AngularBi()
        self.fadeOutCurrentScene()
        self.Angle60()
        self.fadeOutCurrentScene()
        self.ConstOfTriangles()
        self.fadeOutCurrentScene()
        self.BBAS2()
        self.fadeOutCurrentScene()
        self.BBAD2()
        self.fadeOutCurrentScene()
        self.P2BA()
        self.fadeOutCurrentScene()
        self.SpecialCase()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        self.fadeOutCurrentScene()
        # self.constructDataByJSON()
        # self.fadeOut()
    # render using CVO data object
    def constructDataByCVO(self):
        p10=cvo.CVO().CreateCVO("Basic Constructions","").setPosition([-3.5,0,0])
        p11=cvo.CVO().CreateCVO("perpendicular bisector","").setPosition([3.5,2.5,0]).setangle([-TAU/4])
        p13=cvo.CVO().CreateCVO("Bisector of angle","").setPosition([3.5,0,0]).setangle([-TAU/4])
        p12=cvo.CVO().CreateCVO("60 degrees angle","").setPosition([3.5,-2.5,0]).setangle([-TAU/4])
        p10.cvolist.append(p11)
        p10.cvolist.append(p13)
        p10.cvolist.append(p12)
        self.isRandom=False       
        self.setNumberOfCirclePositions(4)
        self.construct1(p10,p10)
    def PerpenBi(self):
        p11=cvo.CVO().CreateCVO("perpendicular bisector","").setPosition([-2,0,0])
        p12=cvo.CVO().CreateCVO("Construction Steps","").setPosition([2,0,0]).setangle([-TAU/4])
        p12onamelist=["Draw line AB","From A,draw arc with  more than 1/2 AB radius","same as A for B","Mark as P and Q and join"]
        p12.extendOname(p12onamelist)
        p12.circle_radius=2
        p11.cvolist.append(p12)
        self.isRandom=False
        self.setNumberOfCirclePositions(2)
        self.construct1(p11,p11)
    def AngularBi(self):
        p11=cvo.CVO().CreateCVO("Angle bisector","").setPosition([-2,0,0])
        p12=cvo.CVO().CreateCVO("Construction Steps","").setPosition([2,0,0]).setangle([-TAU/4])
        p12onamelist=["Draw an angle","From B,draw arc with any radius","from intersection points, draw two arcs","from B, join F"]
        p12.extendOname(p12onamelist)
        p12.circle_radius=2
        p11.cvolist.append(p12)
        self.isRandom=False   
        self.setNumberOfCirclePositions(2)
        self.construct1(p11,p11)
    def Angle60(self):
        p11=cvo.CVO().CreateCVO("60 degrees Angle","").setPosition([-2,0,0])
        p12=cvo.CVO().CreateCVO("Construction Steps","").setPosition([2,0,0]).setangle([-TAU/4])
        p12onamelist=["Draw a ray","From A,draw arc with any radius","from D, draw arc with same radius","join E and A"]
        p12.extendOname(p12onamelist)
        p12.circle_radius=2
        p11.cvolist.append(p12)
        self.isRandom=False
        self.setNumberOfCirclePositions(2)
        self.construct1(p11,p11)
    def ConstOfTriangles(self):
        p10=cvo.CVO().CreateCVO("Construction of Triangles","").setPosition([-3.5,0,0])
        p11=cvo.CVO().CreateCVO("given base, base angle, \\\\sum of 2 sides","").setPosition([3.5,2.5,0]).setangle([-TAU/4])
        p13=cvo.CVO().CreateCVO("given base,base angle,\\\\difference of 2 sides","").setPosition([3.5,0,0]).setangle([-TAU/4])
        p12=cvo.CVO().CreateCVO("given perimeter, \\\\2 base angles","").setPosition([3.5,-2.5,0]).setangle([-TAU/4])
        p10.cvolist.append(p11)
        p10.cvolist.append(p13)
        p10.cvolist.append(p12)
        self.isRandom=False        
        self.setNumberOfCirclePositions(4)
        self.construct1(p10,p10)
    def BBAS2(self):
        p11=cvo.CVO().CreateCVO("given base, base angle, \\\\sum of 2 sides","").setPosition([-2,0,0])
        p12=cvo.CVO().CreateCVO("Construction Steps","").setPosition([2,0,0]).setangle([-TAU/4])
        p12onamelist=["Draw base and angle","From B and sum,draw arc","join C and D and draw perpendicular bisector","join A,C for triangle"]
        p12.extendOname(p12onamelist)
        p11.cvolist.append(p12)
        p12.circle_radius=2
        self.isRandom=False    
        self.setNumberOfCirclePositions(2)
        self.construct1(p11,p11)    
    def BBAD2(self):
        p11=cvo.CVO().CreateCVO("given base, base angle,\\\\ difference of 2 sides","").setPosition([-2,0,0])
        p12=cvo.CVO().CreateCVO("Construction Steps","").setPosition([2,0,0]).setangle([-TAU/4])
        p12onamelist=["Draw BCD triangle using SAS","draw perpendicular bisector of CD","join C and A for triangle"]
        p12.extendOname(p12onamelist)
        p12.circle_radius=2
        
        p11.cvolist.append(p12)   
        self.isRandom=False 
        self.setNumberOfCirclePositions(2)
        self.construct1(p11,p11)
    def P2BA(self):
        p11=cvo.CVO().CreateCVO("given perimeter and \\\\2 base angles","").setPosition([-2,0,0])
        p12=cvo.CVO().CreateCVO("Construction Steps","").setPosition([2,0,0]).setangle([-TAU/4])
        p12onamelist=["Draw line with perimeter","draw angles,bisectors for them","join intersection point","draw bisectors and join"]
        p12.extendOname(p12onamelist)
        p12.circle_radius=2
        p11.cvolist.append(p12) 
        self.isRandom=False
        self.setNumberOfCirclePositions(2)
        self.construct1(p11,p11)
    def SpecialCase(self):
        p11=cvo.CVO().CreateCVO("Special Case","Cirlce segement\\\\for given chord and angle").setPosition([-2,0,0])
        p12=cvo.CVO().CreateCVO("Construction Steps","").setPosition([2,0,0]).setangle([-TAU/4])
        p12onamelist=["Draw line and angles","with intersection point, draw circle","Mark C and join ",]
        p12.extendOname(p12onamelist)
        p11.cvolist.append(p12)   
        self.isRandom=False 
        self.setNumberOfCirclePositions(2)
        self.construct1(p11,p11)   
    def SetDeveloperList(self): 
       self.DeveloperList="Preetham" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade7Chapter15Symmetry.py"     
if __name__ == "__main__":
    scene = GeometricalConstructions3()
    scene.render()