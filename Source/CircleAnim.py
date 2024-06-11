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
        p10.cvolist.append(p11)
        p11.extendOname(p11onameList)
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
        Example= ImageMobject("/Users/hridaybhushan/Desktop/Screenshot 2024-06-10 at 19.21.49.png")
        Example.scale(2.5)
        self.add(Example)
        self.fadeOutCurrentScene()
    
    def Circumference(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Circumference", "")
        p11=cvo.CVO().CreateCVO("Definition", "Complete length of a circle")
        p10.cvolist.append(p11)
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Diameter(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Chord", "")
        p11=cvo.CVO().CreateCVO("Definition", "Line segment joining two points on a circle")
        p12=cvo.CVO().CreateCVO("Diameter (Special Case)", "Line segment joining two points through center")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
        Example= ImageMobject("/Users/hridaybhushan/Desktop/Screenshot 2024-06-10 at 19.22.16.png")
        Example.scale(2.5)
        self.add(Example)
        self.fadeOutCurrentScene()

    def Arc(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Arc", "Part of circle between two points")
        p12=cvo.CVO().CreateCVO("Major Arc", "Arc larger than Semi-Circle")
        p11=cvo.CVO().CreateCVO("Minor Arc", "Arc smaller than Semi-Circle")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
        Example= ImageMobject("/Users/hridaybhushan/Desktop/Screenshot 2024-06-10 at 19.22.35.png")
        Example.scale(2.5)
        self.add(Example)
        self.fadeOutCurrentScene()
    
    def Segment(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Segment", "Minor and Major")
        p11=cvo.CVO().CreateCVO("Minor", "Region between chord and minor arc")
        p12=cvo.CVO().CreateCVO("Major", "Region between chord and major arc")
        p13=cvo.CVO().CreateCVO("Special Case", "If chord is diameter, circle split equally")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.setNumberOfCirclePositions(4)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
        Example= ImageMobject("/Users/hridaybhushan/Desktop/Screenshot 2024-06-10 at 19.22.42.png")
        Example.scale(2.5)
        self.add(Example)
        self.fadeOutCurrentScene()

    def Sector(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Sector", "Region enclosed by an arc and two radii")
        p11=cvo.CVO().CreateCVO("Minor", "")
        p12=cvo.CVO().CreateCVO("Major", "")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
        Example= ImageMobject("/Users/hridaybhushan/Desktop/Screenshot 2024-06-10 at 19.22.57.png")
        Example.scale(2.5)
        self.add(Example)
        self.fadeOutCurrentScene()
    
    def AngleSubtend(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Angle Subtended by a Chord", "Central Angle created after joining two points").setPosition([-2,0,0])
        Example= ImageMobject("/Users/hridaybhushan/Desktop/Screenshot 2024-06-10 at 19.41.25.png")
        Example.scale(2)
        Example.to_edge(RIGHT, buff=1)
        self.add(Example)
        self.setNumberOfCirclePositions(1)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Theorem1(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Theorem 1", "Equal chords of a circle subtend equal angles at the centre").setPosition([-2,0,0])
        Example= ImageMobject("/Users/hridaybhushan/Desktop/Screenshot 2024-06-10 at 19.48.26.png")
        Example.scale(2)
        Example.to_edge(RIGHT, buff=1)
        self.add(Example)
        self.setNumberOfCirclePositions(1)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Theorem2(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Theorem 2", "Chords are equal if angle subtended at centre are also equal").setPosition([-2,0,0]).setcircleradius(2)
        Example= ImageMobject("/Users/hridaybhushan/Desktop/Screenshot 2024-06-10 at 19.48.34.png")
        Example.scale(2)
        Example.to_edge(RIGHT, buff=1)
        self.add(Example)
        self.setNumberOfCirclePositions(1)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
    
    def Theorem3(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Theorem 3", "Perpendicular from centre to a chord bisects the chord").setPosition([-2,0,0])
        Example= ImageMobject("/Users/hridaybhushan/Desktop/Screenshot 2024-06-10 at 19.54.59.png")
        Example.scale(2)
        Example.to_edge(RIGHT, buff=1)
        self.add(Example)
        self.setNumberOfCirclePositions(1)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
    
    def ArcSubtend(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Statement", "Arcs of equal length subtend equal angles at centre").setPosition([-2,0,0])
        Example= ImageMobject("/Users/hridaybhushan/Desktop/Screenshot 2024-06-10 at 20.02.09.png")
        Example.scale(2)
        Example.to_edge(RIGHT, buff=1)
        self.add(Example)
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
    
    def ArcSubtend2(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Theorem 1", "The angle subtended by an arc at the centre 'O' is twice the angle subtended by it on the remaining arc of the circle").setPosition([-2,0,0])
        Example= ImageMobject("/Users/hridaybhushan/Desktop/Screenshot 2024-06-10 at 20.05.24.png")
        Example.scale(2)
        Example.to_edge(RIGHT, buff=1)
        self.add(Example)
        self.setNumberOfCirclePositions(1)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def ArcSubtend3(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Theorem 2", "Angles subtended by an arc in the same segment are equal").setPosition([-2,0,0])
        Example= ImageMobject("/Users/hridaybhushan/Desktop/Screenshot 2024-06-10 at 20.11.22.png")
        Example.scale(2)
        Example.to_edge(RIGHT, buff=1)
        self.add(Example)
        self.setNumberOfCirclePositions(1)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def ArcSubtend4(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Theorem 3", "Points are concylic if line segment joining two points, subtends equal angles at two other points lying on the same side of the line").setPosition([-2,0,0])
        Example= ImageMobject("/Users/hridaybhushan/Desktop/Screenshot 2024-06-10 at 20.15.18.png")
        Example.scale(2)
        Example.to_edge(RIGHT, buff=1)
        self.add(Example)
        self.setNumberOfCirclePositions(1)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def cyclicQuad(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Cyclic Quadrilateral", "A quadrilateral with all 4 sides and vertices inside the circle").setPosition([-2,0,0])
        Example= ImageMobject("/Users/hridaybhushan/Desktop/Screenshot 2024-06-10 at 20.19.50.png")
        Example.scale(2)
        Example.to_edge(RIGHT, buff=1)
        self.add(Example)
        self.setNumberOfCirclePositions(1)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
    
    def Quad1(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Theorem 1", "Opposite angles are supplementary").setPosition([-2,0,0])
        Example= ImageMobject("/Users/hridaybhushan/Desktop/Screenshot 2024-06-10 at 20.21.32.png")
        Example.scale(2)
        Example.to_edge(RIGHT, buff=1)
        self.add(Example)
        self.setNumberOfCirclePositions(1)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Quad2(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Theorem 2", "If sum of any pair of opposite angles are supplementary, it is cyclic").setPosition([-2,0,0])
        Example= ImageMobject("/Users/hridaybhushan/Desktop/Screenshot 2024-06-10 at 20.24.14.png")
        Example.scale(2)
        Example.to_edge(RIGHT, buff=1)
        self.add(Example)
        self.setNumberOfCirclePositions(1)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()


    


if __name__ == "__main__":
    scene = CircleAnim()
    scene.render()