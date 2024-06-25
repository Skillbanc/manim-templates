import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo

class StandardFormFractions(AbstractAnim):
    def construct(self):
       #self.StanderdForm()
       #self.NonStanderd()
       #self.LikeFractions()
       #self.UnLikeFractions()
       self.AscendingOrder()
       self.fadeOutCurrentScene()
       self.DesendingOrder()
 
    def StanderdForm(self):
        p10 = cvo.CVO().CreateCVO("Standerd Form of Fractions", "").setPosition([3,1,0])
        p11 = cvo.CVO().CreateCVO("Definition", "Fraction with no common factors").setPosition([3,-1,0])
        p12 = cvo.CVO().CreateCVO("Examples ", r"$\frac{1}{3}$").setPosition([-3,1,0]).setangle(-TAU/4)
        p13 = cvo.CVO().CreateCVO("Exp2", r"$\frac{2}{3}$").setPosition([-3,-1,0]).setangle(-TAU/4)
        p14 = cvo.CVO().CreateCVO("Exp3", r"$\frac{3}{11}$").setPosition([0,-2,0])
    
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        self.construct1(p10, p10)

    def NonStanderd(self):
        p10 = cvo.CVO().CreateCVO("Non Standerd Fractions", "").setPosition([3,1,0])
        p11 = cvo.CVO().CreateCVO("Condition","Fraction not in simplest form").setPosition([3,-1,0])
        p12 = cvo.CVO().CreateCVO("Examples ", r"$\frac{5}{10}$").setPosition([-3,1,0]).setangle(-TAU/4)
        p13 = cvo.CVO().CreateCVO("Exp2", r"$\frac{2}{4}$").setPosition([-3,-1,0]).setangle(-TAU/4)
        p14 = cvo.CVO().CreateCVO("Exp3", r"$\frac{16}{36}$").setPosition([0,-2,0])
    
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        self.construct1(p10, p10)
    def LikeFractions(self):
        p10 = cvo.CVO().CreateCVO("Like Fractions", "").setPosition([-2,2.5,0])
        p11 = cvo.CVO().CreateCVO("Defination","Fractions with same denominator.").setPosition([0,1,0])
        p12 = cvo.CVO().CreateCVO("Examples ", r"$\frac{2}{7}$,$\frac{3}{7}$,$\frac{5}{7}$").setPosition([3,0,0]).setangle(-TAU/4)
        p13 = cvo.CVO().CreateCVO("Exp2", r"$\frac{1}{9}$,$\frac{2}{9}$,$\frac{4}{9}$").setPosition([-3,-1.5,0]).setangle(-TAU/4)
       # p14 = cvo.CVO().CreateCVO("Exp3", r"$\frac{16}{36}$").setPosition([0,-2,0])
    
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
        #p10.cvolist.append(p14)
        self.construct1(p10, p10)
    
    def UnLikeFractions(self):
        p10 = cvo.CVO().CreateCVO("UnLike Fractions", "").setPosition([3,1,0])
        p11 = cvo.CVO().CreateCVO("Defination","Fractions with different denominators.").setPosition([3,-1,0])
        p12 = cvo.CVO().CreateCVO("Examples ", r"$\frac{2}{5}$,$\frac{3}{2}$,$\frac{5}{9}$").setPosition([-3,1,0]).setangle(-TAU/4)
        p13 = cvo.CVO().CreateCVO("Exp2", r"$\frac{1}{5}$,$\frac{2}{7}$,$\frac{4}{9}$").setPosition([-3,-1,0]).setangle(-TAU/4)
       # p14 = cvo.CVO().CreateCVO("Exp3", r"$\frac{16}{36}$").setPosition([0,-2,0])
    
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        #p10.cvolist.append(p14)
        self.construct1(p10, p10)
    def AscendingOrder(self):
        p10 = cvo.CVO().CreateCVO("Ascending Order Fractions", "").setPosition([-2,2.5,0])
        p11 = cvo.CVO().CreateCVO("Defination","Fractions arranged smallest to largest").setPosition([0,1,0])
        p12 = cvo.CVO().CreateCVO("Examples", r"$\frac{3}{5} < \frac{7}{5} < \frac{9}{5}$").setPosition([-3, 0, 0]).setangle(-TAU/4)
        p13 = cvo.CVO().CreateCVO("Exp2", r"$\frac{4}{3} < \frac{8}{3} < \frac{10}{3}$").setPosition([3,-1.5, 0]).setangle(-TAU/4)

       
        # p14 = cvo.CVO().CreateCVO("Exp3", r"$\frac{16}{36}$").setPosition([0,-2,0])
    

        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
        #p10.cvolist.append(p14)
        self.construct1(p10, p10)
    
    def DesendingOrder(self):
        p10 = cvo.CVO().CreateCVO("Desending Order Fractions", "").setPosition([3,1,0])
        p11 = cvo.CVO().CreateCVO("Defination","Fractions arranged Largest to Smallest").setPosition([3,-1,0])
        p12 = cvo.CVO().CreateCVO("Examples", r"$\frac{9}{5} > \frac{7}{5} > \frac{3}{5}$").setPosition([-3, 1, 0]).setangle(-TAU/4)
        p13 = cvo.CVO().CreateCVO("Exp2", r"$\frac{10}{3} > \frac{8}{3} > \frac{4}{3}$").setPosition([-3, -1, 0]).setangle(-TAU/4)

        
        # p14 = cvo.CVO().CreateCVO("Exp3", r"$\frac{16}{36}$").setPosition([0,-2,0])
    
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
        #p10.cvolist.append(p14)
        self.construct1(p10, p10)
if __name__ == "__main__":
    scene = StandardFormFractions()
    scene.render()