# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla
import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class CircleAnim(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.Circle()
        self.Circumference()
        self.Diameter()
        self.Arc()
        self.Segment()
        self.Sector()
        self.SectorType()
        self.AngleSubtend()
        self.Theorem1()
        self.Theorem2()
        self.Theorem3()
        self.ArcSubtend()
        self.ArcSubtend2()
        self.ArcSubtend3()
        self.ArcSubtend4()
        self.cyclicQuad()
        self.Quad1()
        self.Quad2()
        # self.fadeOut()
        # self.constructDataByJSON()
        # self.fadeOut()
        
    # render using CVO data object
    def Circle(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Circle","")
        p11=cvo.CVO().CreateCVO("Properties","")
        p11onameList=["No Sides","Centre marked 'O'"]
        p10.setcircleradius(1.5)
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p11.extendOname(p11onameList)
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
        Example= ImageMobject("/Users/hridaybhushan/Downloads/circlebasics.jpg")
        Example.scale(1.5)
        self.add(Example)
        self.fadeOutCurrentScene()
    
    def Circumference(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Circumference", "")
        p11=cvo.CVO().CreateCVO("Definition", "Complete length of a circle")
        p10.setcircleradius(1.5)
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
        Example= ImageMobject("/Users/hridaybhushan/Downloads/circlebasics.jpg")
        Example.scale(1.5)
        self.add(Example)
        self.fadeOutCurrentScene()

    def Diameter(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Chord", "")
        p11=cvo.CVO().CreateCVO("Definition", "Line segment joining two points on a circle")
        p12=cvo.CVO().CreateCVO("Diameter", "Line segment joining two points through center")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
        Example= ImageMobject("/Users/hridaybhushan/Downloads/parts-circle-mathematics-arcradius-sector-260nw-2272566953.jpg")
        Example.scale(2.5)
        self.add(Example)
        self.fadeOutCurrentScene()

    def Arc(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Arc", "")
        p12=cvo.CVO().CreateCVO("Major Arc", "")
        p11=cvo.CVO().CreateCVO("Minor Arc", "")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
        Example= ImageMobject("/Users/hridaybhushan/Downloads/parts-circle-mathematics-arcradius-sector-260nw-2272566953.jpg")
        Example.scale(2.5)
        self.add(Example)
        self.fadeOutCurrentScene()
    
    def Segment(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Segment", "")
        p11=cvo.CVO().CreateCVO("Minor", "")
        p12=cvo.CVO().CreateCVO("Major", "")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
        Example= ImageMobject("/Users/hridaybhushan/Downloads/parts-circle-mathematics-arcradius-sector-260nw-2272566953.jpg")
        Example.scale(2.5)
        self.add(Example)
        self.fadeOutCurrentScene()

    def Sector(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Sector", "")
        p11=cvo.CVO().CreateCVO("Definition", "Region enclosed by an arc and two radii")
        p10.setcircleradius(1.5)
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
    
    def SectorType(self):
        p10=cvo.CVO().CreateCVO("Sector Types", "")
        p11=cvo.CVO().CreateCVO("Minor", "")
        p12=cvo.CVO().CreateCVO("Major", "")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
        Example= ImageMobject("/Users/hridaybhushan/Downloads/parts-circle-mathematics-arcradius-sector-260nw-2272566953.jpg")
        Example.scale(2.5)
        self.add(Example)
        self.fadeOutCurrentScene()
    
    def AngleSubtend(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Angle Subtended by a Chord", "Central Angle created\nafter joining two points").setPosition([-2.5,0,0])
        p10.setcircleradius(1.5)
        Example= ImageMobject("/Users/hridaybhushan/Downloads/anglesubtend.png")
        Example.scale(1.2)
        Example.to_edge(RIGHT, buff=1)
        self.add(Example)
        self.setNumberOfCirclePositions(1)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Theorem1(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Theorem", "Equal chords of a circle\nsubtend equal angles at the centre").setPosition([-2,0,0])
        p10.setcircleradius(1.5)
        Example= ImageMobject("/Users/hridaybhushan/Downloads/equal-chords-subtend-equal-angles.jpg")
        Example.scale(2)
        Example.to_edge(RIGHT, buff=1)
        self.add(Example)
        self.setNumberOfCirclePositions(1)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Theorem2(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Theorem", "Chords are equal if angle\nsubtended at centre are also equal").setPosition([-2,0,0])
        p10.setcircleradius(1.5)
        Example= ImageMobject("/Users/hridaybhushan/Downloads/angles-subtended-by-chords-then-chords-are-also-equal.jpg")
        Example.scale(2)
        Example.to_edge(RIGHT, buff=1)
        self.add(Example)
        self.setNumberOfCirclePositions(1)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
    
    def Theorem3(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Theorem", "Perpendicular from centre\nto a chord bisects the chord").setPosition([-2,0,0])
        p10.setcircleradius(1.5)
        Example= ImageMobject("/Users/hridaybhushan/Downloads/mathematics-questions-answers-perpendicular-centre-chord-q1.png")
        Example.scale(2)
        Example.to_edge(RIGHT, buff=1)
        self.add(Example)
        self.setNumberOfCirclePositions(1)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
    
    def ArcSubtend(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Statement", "Arcs of equal length subtend\nequal angles at centre").setPosition([0,0,0])
        p10.setcircleradius(2)
        p10.setcircleradius(2)
        self.setNumberOfCirclePositions(1)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
    
    def ArcSubtend2(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Theorem", "The angle subtended by an arc at the centre 'O' is twice\nthe angle subtended by it on the remaining arc of the circle").setPosition([-2,0,0])
        p10.setcircleradius(1.5)
        Example= ImageMobject("/Users/hridaybhushan/Desktop/Screenshot 2024-06-10 at 20.05.24.png")
        Example.scale(2)
        Example.to_edge(RIGHT, buff=1)
        self.add(Example)
        self.setNumberOfCirclePositions(1)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def ArcSubtend3(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Theorem", "Angles subtended by an arc\nin the same segment are equal").setPosition([-2,0,0])
        p10.setcircleradius(1.5)
        Example= ImageMobject("/Users/hridaybhushan/Desktop/Screenshot 2024-06-10 at 20.11.22.png")
        Example.scale(2)
        Example.to_edge(RIGHT, buff=1)
        self.add(Example)
        self.setNumberOfCirclePositions(1)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def ArcSubtend4(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Theorem", "Points are concylic if line segment joining two points,\nsubtends equal angles at two other points lying on the same side of the line").setPosition([-2,0,0])
        Example= ImageMobject("/Users/hridaybhushan/Desktop/Screenshot 2024-06-10 at 20.15.18.png")
        Example.scale(2)
        Example.to_edge(RIGHT, buff=1)
        self.add(Example)
        self.setNumberOfCirclePositions(1)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def cyclicQuad(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Cyclic Quadrilateral", "").setPosition([-2,2,0])
        p11=cvo.CVO().CreateCVO("Definition","A quadrilateral with all 4 sides\nand 4 vertices inside the circle").setPosition([-2,-2,0])
        p10.cvolist.append(p11)
        Example= ImageMobject("/Users/hridaybhushan/Desktop/Screenshot 2024-06-10 at 20.19.50.png")
        Example.scale(2)
        Example.to_edge(RIGHT, buff=1)
        self.add(Example)
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
    
    def Quad1(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Theorem", "Opposite angles are supplementary").setPosition([-2,0,0])
        p10.setcircleradius(1.5)
        Example= ImageMobject("/Users/hridaybhushan/Downloads/material-gGbzJs4s-thumb@l.png")
        Example.scale(2)
        Example.to_edge(RIGHT, buff=1)
        self.add(Example)
        self.setNumberOfCirclePositions(1)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Quad2(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Theorem", "If sum of any pair of opposite\nangles are supplementary, it is cyclic").setPosition([-2.8,0,0])
        p10.setcircleradius(1.5)
        Example= ImageMobject("/Users/hridaybhushan/Downloads/material-gGbzJs4s-thumb@l.png")
        Example.scale(2)
        Example.to_edge(RIGHT, buff=1)
        self.add(Example)
        self.setNumberOfCirclePositions(1)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()


    


if __name__ == "__main__":
    scene = CircleAnim()
    scene.render()