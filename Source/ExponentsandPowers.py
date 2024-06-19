# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License

import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class PowerAnim(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.constructDataByCVO()   
        self.fadeOutCurrentScene()
        self.LawsofExponents()
        self.fadeOutCurrentScene()
        self.Samebase()
        self.fadeOutCurrentScene()
        self.Exponentofexponent()
        self.fadeOutCurrentScene()
        self.Exponentofproduct()
        self.fadeOutCurrentScene()
        self.Zeroexponent()
        self.fadeOutCurrentScene()
        self.Divofsamebase()
        self.fadeOutCurrentScene()
        self.Divofsameexp()
        self.fadeOutCurrentScene()
        self.additional()
        self.fadeOutCurrentScene()
        self.Example()
        self.fadeOutCurrentScene()
        self.Example2()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        
    def constructDataByCVO(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Term","$5^3$")
        p11=cvo.CVO().CreateCVO("Base", "5")
        p12=cvo.CVO().CreateCVO("Expononet", "3")
        p13=cvo.CVO().CreateCVO("Read as", "5 to the power of 3")
        p14=cvo.CVO().CreateCVO("Expand", "5*5*5")
        
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        
        self.setNumberOfCirclePositions(5)
        self.construct1(p10,p10)

    def LawsofExponents(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Laws of Exponents","7 laws").setPosition([4,2,0])
        p11=cvo.CVO().CreateCVO("Same base", "$a^m*a^n=a^{m+n}$").setPosition([5,-2,0])
        p12=cvo.CVO().CreateCVO("Exponent of exponent", "$(a^m)^n=a^{m*n}$").setPosition([-4,3,0])
        p13=cvo.CVO().CreateCVO("Exponent of product", "$a^m*b^m=(a*b)^m$").setPosition([-4,1,0])
        p14=cvo.CVO().CreateCVO("Zero exponent", "$a^0=1$").setPosition([-4,-1,0])
        p15=cvo.CVO().CreateCVO("Division with same base", "$a^m/a^n=a^{m-n}$").setPosition([-4,-3,0])
        p16=cvo.CVO().CreateCVO("Division with same exponent", "$(a/b)^m=a^m/b^m$").setPosition([0,0,0])
           
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        p10.cvolist.append(p16)
        self.setNumberOfCirclePositions(7)
        self.construct1(p10,p10)

    def Samebase(self):
       p10 = cvo.CVO().CreateCVO("Same base", "")
           
       p10.onameList.append("Same base ")
       p10.onameList.append("$a^m * a^n = a^{m+n}$")
       p10.onameList.append("Example")
       p10.onameList.append("$ 2^4 * 2^3 = 2^7 $")
       p10.onameList.append("$3^2 * 3^5 = 3^7$")
       p10.onameList.append("$4^5 * 4^6 = 4^{11}$")
       p10.onameList.append("$6^4 * 6^9 = 6^{13}$")   
       
       self.construct2(p10, p10)

    def Exponentofexponent(self):
       self.isRandom = False

       p10 = cvo.CVO().CreateCVO("Same base", "")
       p10.onameList.append("Exponent of Exponent")
       p10.onameList.append("$(a^m)^n=a^{m*n}$")   
       p10.onameList.append("Example")
       p10.onameList.append("$(3^2)^3=3^6$")
       p10.onameList.append("$(5^4)^2=5^8$")
       p10.onameList.append("$(2^2)^5=2^{10}$")
       p10.onameList.append("$(9^5)^3=9^{15}$")
         
       
       self.construct2(p10, p10)
        
    def Exponentofproduct(self):
       self.isRandom = False

       p10 = cvo.CVO().CreateCVO("Same base", "")
       p10.onameList.append("Exponent of Product")
       p10.onameList.append("$a^m*b^m=(a*b)^m$")   
       p10.onameList.append("Example")
       p10.onameList.append("$3^5*4^5=(3*4)^5=12^5$")
       p10.onameList.append("$3^6*4^6=(3*6)^6=18^6$")
       p10.onameList.append("$5^2*2^2=(5*2)^2=10^2$")
       p10.onameList.append("$8^7*3^7=(8*3)^7=24^7$")

       self.construct2(p10, p10)
         
    def Zeroexponent(self):
       self.isRandom = False
       p10 = cvo.CVO().CreateCVO("Same base", "")
       p10.onameList.append("Zero Exponent")
       p10.onameList.append("$a^0=1$")   
       p10.onameList.append("Example")
       p10.onameList.append("$5^0=1$")
       p10.onameList.append("$20^0=1$")
       p10.onameList.append("$99^0=1$")
       p10.onameList.append("$31^0=1$")

       self.construct2(p10, p10)
       
    def Divofsamebase(self):
       self.isRandom = False
       p10 = cvo.CVO().CreateCVO("Same base", "")
       p10.onameList.append("Division with same base")
       p10.onameList.append("$a^m/a^n=a^{m-n}$")   
       p10.onameList.append("Example")
       p10.onameList.append("$3^8/3^3=3^{8-3}=3^5$")
       p10.onameList.append("$2^9/2^2=2^{9-2}=2^7$")
       p10.onameList.append("$5^8/5^5=5^{8-5}=5^3$")
       p10.onameList.append("$7^{12}/7^5=7^{12-5}=7^7$")
       self.construct2(p10, p10)
       
    def Divofsameexp(self):
       self.isRandom = False

       p10 = cvo.CVO().CreateCVO("Same base", "")
       p10.onameList.append("Division with same exponent")
       p10.onameList.append("$(a/b)^m=a^m/b^m$")   
       p10.onameList.append("Example")
       p10.onameList.append("$(7/5)^3=7^3/5^3$")
       p10.onameList.append("$(4/9)^5=4^5/9^5$")
       p10.onameList.append("$(6/5)^3=6^2/5^2$")
       p10.onameList.append("$(5/9)^2=5^2/9^2$")
       self.construct2(p10, p10)
       
    def additional(self):
       self.isRandom = False
       p10=cvo.CVO().CreateCVO("Additional Information", "")
       p11=cvo.CVO().CreateCVO("Negative Exponent", "$a^{-m}=1/a^m$")
       p12=cvo.CVO().CreateCVO("Negative Base", "$(-a)^m$")
       p13=cvo.CVO().CreateCVO("if m is odd", "$-a^m $")
       p14=cvo.CVO().CreateCVO("if m is even", "$a^m $")

       p10.cvolist.append(p11)
       p10.cvolist.append(p12)
       p12.cvolist.append(p13)
       p12.cvolist.append(p14)
       
       self.setNumberOfCirclePositions(5)
       self.construct1(p10,p10)


    def Example(self):
       self.isRandom = False

       p10 = cvo.CVO().CreateCVO("Same base", "")
       p10.onameList.append("Negative Exponent")
       p10.onameList.append("$a^{-m}=1/a^m$")   
       p10.onameList.append("Example")
       p10.onameList.append("$5^{-3}=1/5^3$")
       p10.onameList.append("$2^{-6}=1/2^6$")
       p10.onameList.append("$7^{-4}=1/7^4$")       
       self.construct2(p10, p10)
       
    def Example2(self):
       self.isRandom = False

       p10 = cvo.CVO().CreateCVO("Same base", "")
       p10.onameList.append("Negative Base")
       p10.onameList.append("$(-a)^m$")  
       p10.onameList.append("$-a^m \\text{ if } m \\text{ is odd}$")
       p10.onameList.append("$a^m \\text{ if } m \\text{ is even}$") 
       p10.onameList.append("Example")
       p10.onameList.append("$(-5)^4=5^4$")
       p10.onameList.append("$(-3)^3=-3^3$")
       self.construct2(p10, p10)
       

    def SetDeveloperList(self): 
       self.DeveloperList="Khanak Gupta" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="ExponentsandPowers.py"
      

if __name__ == "__main__":
    scene = PowerAnim()
    scene.render()