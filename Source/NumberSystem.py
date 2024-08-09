
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class NumberSystemsAnim(AbstractAnim):
    
    def construct(self):
        # self.RenderSkillbancLogo()
        # self.RenderBase()
        self.RenderBase10()
        # self.RenderBase2()
        # self.RenderNumberSystem1()
        
    def RenderBase(self):
        #  p1=cvo.CVO().CreateCVO("cname","oname")
        
        self.isRandom =False
        self.setNumberOfCirclePositions(4)

        p10=cvo.CVO().CreateCVO("Number System","")
         

        p11=cvo.CVO().CreateCVO("Base","Base 10")
         
        p12=cvo.CVO().CreateCVO("Base","Base 2")
       
        p13=cvo.CVO().CreateCVO("Base","Base 16")
        
        p10.extendcvo([p11,p12,p13])
         
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
    
    def RenderBase10(self):
        #  p1=cvo.CVO().CreateCVO("cname","oname")
        
         self.isRandom =False
         self.setNumberOfCirclePositions(7)

         p11=cvo.CVO().CreateCVO("Base","Base 10")
         
         p111 = cvo.CVO().CreateCVO("Symbol List","0,1,2,3,4,5,6,7,8,9")
         p112 = cvo.CVO().CreateCVO("Number System","Decimal Number System")
         
         p11.extendcvo([p111,p112])
         
         p113 = cvo.CVO().CreateCVO("Position 1","10^0")
         p113.SetIsMathText(True)
         
         p114 = cvo.CVO().CreateCVO("Position 2","10^1")
         p114.SetIsMathText(True)
         
         p115 = cvo.CVO().CreateCVO("Position 3","10^2")
         p115.SetIsMathText(True)
         
         p116 = cvo.CVO().CreateCVO("Position 4","10^3")
         p116.SetIsMathText(True)
         
         p11.extendcvo([p113,p114,p115,p116])
         
         self.construct1(p11,p11)
         self.fadeOutCurrentScene()
         
    def RenderBase2(self):
        #  p1=cvo.CVO().CreateCVO("cname","oname")
        
         self.isRandom =False
         self.setNumberOfCirclePositions(7)

         p11=cvo.CVO().CreateCVO("Base","Base 2")
         
         p111 = cvo.CVO().CreateCVO("Symbol List","0,1")
         p112 = cvo.CVO().CreateCVO("Number System","Binary Number System")
         
         p113 = cvo.CVO().CreateCVO("Position 1","2^0")
         p113.SetIsMathText(True)
         
         p114 = cvo.CVO().CreateCVO("Position 2","2^1")
         p114.SetIsMathText(True)
         
         p115 = cvo.CVO().CreateCVO("Position 3","2^2")
         p115.SetIsMathText(True)
         
         p116 = cvo.CVO().CreateCVO("Position 4","2^4")
         p116.SetIsMathText(True)
         
         p11.extendcvo([p111,p112,p113.p114,p115,p116])
         
         self.construct1(p11,p11)
         self.fadeOutCurrentScene()
    
    def RenderNumberSystem1(self):
        
        p10=cvo.CVO().CreateCVO("Number System","Base n")
        p10.SetIsMathText(True)
       
        p10.onameList.append("Base 10")
        p10.onameList.append("10 symbols")
        p10.onameList.append("0 1 2 3 4 5 6 7 8 9")
        p10.onameList.append("Base 10 = Base 10")
        p10.onameList.append("24=2*10^1 + 4*10^0=24")
                             
        
        p10.onameList.append("Base 2")
        p10.onameList.append("2 symbols")
        p10.onameList.append("0 1")
        p10.onameList.append("Base 2 = Base 10")
        p10.onameList.append("10=1*2^1 + 0*2^0=2")
                
        p10.onameList.append("Base 3")
        p10.onameList.append("3 symbols")
        p10.onameList.append("0 1 2")
        p10.onameList.append("Base 2 = Base 10")
        p10.onameList.append("121=1*3^2 + 2*3^1 + 1*3^0=16")
        
        self.construct2(p10,p10)
        
if __name__ == "__main__":
    
    scene = NumberSystemsAnim()
    scene.render()
    