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

# Configure Manim to allow more cached files
config.max_files_cached = 300  # Change this number to your desired value

class AlgebraicAnim3(AbstractAnim):
    def construct(self):
        self.Introduction()
        self.fadeOutCurrentScene()
        self.Types()
        self.fadeOutCurrentScene()
        self.Polynomials()
        self.fadeOutCurrentScene()
        self.Relations()
        self.fadeOutCurrentScene()
        self.addition()
        self.fadeOutCurrentScene()
        self.substraction()
        self.fadeOutCurrentScene()
        self.multiplication()
        self.fadeOutCurrentScene()
        self.identities()
        self.fadeOutCurrentScene()
        
    def Introduction(self):
        # p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
        self.setNumberOfCirclePositions(3)
        self.isRandom = False
        p10 = cvo.CVO().CreateCVO("algebraic expression", "ax+by+c=0")
        p12 = cvo.CVO().CreateCVO("like terms", "3x,3y")
        p13 = cvo.CVO().CreateCVO("unlike term", "3xy,7yz")
        
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        
        self.construct1(p10, p10)
        
    def Types(self):
        self.setNumberOfCirclePositions(5)
        p10 = cvo.CVO().CreateCVO("types", "4").setPosition([0, 2.5, 0])
        p11 = cvo.CVO().CreateCVO("monomial", "2x,3x").setPosition([4, 2, 0])
        p12 = cvo.CVO().CreateCVO("binomial", "3x + 2, 4x^2 - 9").setPosition([5, -2, 0])
        p12.SetIsMathText(True)
        p13 = cvo.CVO().CreateCVO("trinomial", "x^2 + 3x + 2, 2a^3 - 3a + 5").setPosition([-4, 2, 0])
        p13.SetIsMathText(True)
        p14 = cvo.CVO().CreateCVO("polynomial", "4x^3 + 3x^2 - x + 7, x^4 - 2x^3 + x - 1").setPosition([-4, -2, 0])
        p14.SetIsMathText(True)
        
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        
        self.construct1(p10, p10)
         
    def Polynomials(self):
        
     
        self.setNumberOfCirclePositions(7)
        p10 = cvo.CVO().CreateCVO("polynomials", "types").setPosition([0, 2.5, 0])
        p11 = cvo.CVO().CreateCVO("1", "Linear Polynomial\n(e.g., 2x + 3)").setPosition([4, 2, 0])
        p11.SetIsMathText(True)
        p12 = cvo.CVO().CreateCVO("2", "Quadratic Polynomial\n(e.g., 3x^2 + 2x + 1)").setPosition([5, -2, 0])
        p12.SetIsMathText(True)
        p13 = cvo.CVO().CreateCVO("3", "Cubic Polynomial\n(e.g., x^3 - 3x^2 + 2)").setPosition([-4, 2, 0])
        p13.SetIsMathText(True)
        p14 = cvo.CVO().CreateCVO("4", "Quartic Polynomial\n(e.g., 2x^4 - x^3 + 3x^2 - x + 1)").setPosition([-4, 0, 0])
        p14.SetIsMathText(True)
        p15 = cvo.CVO().CreateCVO("5", "Quintic Polynomia\n (e.g., x^5 + 2x^4 - 5x^3 + x^2 - x + 4)").setPosition([-4, -2, 0])
        p15.SetIsMathText(True)
        p16 = cvo.CVO().CreateCVO("6", "Sextic Polynomial\n(e.g., 3x^6 - x^5 + 4x^4 - x^3 + 2x^2 - x + 1)").setPosition([0, -2.5, 0])
        p16.SetIsMathText(True)
    
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        p10.cvolist.append(p16)
   
        self.construct1(p10, p10)
    
        
    def Relations(self):
        self.setNumberOfCirclePositions(5)
        # self.isRandom = False
        p10 = cvo.CVO().CreateCVO("algebraic expression", "ax+by+c=0").setPosition([0, 2.5, 0])
        p11 = cvo.CVO().CreateCVO("algebraic expression", "operations").setPosition([4, 2, 0])
        p12 = cvo.CVO().CreateCVO("1", "addition").setPosition([5, -2, 0])
        p13 = cvo.CVO().CreateCVO("2", "substraction").setPosition([-4, 2, 0])
        p14 = cvo.CVO().CreateCVO("3", "multiplication").setPosition([-4, -2, 0])
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
        p11.cvolist.append(p14)
        
        p10.cvolist.append(p11)
        
        self.construct1(p10, p10)
    
    def addition(self):
        self.setNumberOfCirclePositions(2)
        self.isRandom = False
        p10 = cvo.CVO().CreateCVO("addition", "+")
        p11 = cvo.CVO().CreateCVO("example", "2x+4x=6x")
        
        p10.cvolist.append(p11)
        
        self.construct1(p10, p10)
        
    def substraction(self):
        self.setNumberOfCirclePositions(2)
        self.isRandom = False
        p10 = cvo.CVO().CreateCVO("substraction", "-")
        p11 = cvo.CVO().CreateCVO("example", "2x-4x=-2x")
        
        p10.cvolist.append(p11)
        
        self.construct1(p10, p10)
        
    def multiplication(self):
        self.setNumberOfCirclePositions(2)
        self.isRandom = False
        p10 = cvo.CVO().CreateCVO("multiplication", "*")
        p11 = cvo.CVO().CreateCVO("example", "2x*4y=8xy")
    
        p10.cvolist.append(p11)
        
        self.construct1(p10, p10)
        
    def identities(self):
        self.setNumberOfCirclePositions(5)
        self.isRandom = False
        p10 = cvo.CVO().CreateCVO("identities", "")
        p11 = cvo.CVO().CreateCVO("(a+b)^2", "a^2+b^2+2ab")
        p11.SetIsMathText(True)
        p12 = cvo.CVO().CreateCVO("(a-b)^2", "a^2+b^2-2ab")
        p12.SetIsMathText(True)
        p13 = cvo.CVO().CreateCVO("(a+b)(a-b)", "a^2-b^2")
        p13.SetIsMathText(True)
        p14 = cvo.CVO().CreateCVO("(x+a)(x+b)", "x^2+(a+b)x+ab")
        p14.SetIsMathText(True)
        
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        
        self.construct1(p10, p10)

if __name__ == "__main__":
    scene = AlgebraicAnim3()
    scene.render()
