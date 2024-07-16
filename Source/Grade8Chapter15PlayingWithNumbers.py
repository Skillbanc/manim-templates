# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla

from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo


class Grade8Chapter15PlayingWithNumbersTopic1(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Playing_numbers()
        self.fadeOutCurrentScene()
        self.Expanded_Form()
        self.fadeOutCurrentScene()
        self.create_animation()
        self.fadeOutCurrentScene()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.DivisibilityRule2()
        self.fadeOutCurrentScene()
        self.DivisibilityRule3()
        self.fadeOutCurrentScene()
        self.DivisibilityRule4()
        self.fadeOutCurrentScene()
        self.DivisibilityRule5()
        self.fadeOutCurrentScene()
        self.Introduction1()
        self.fadeOutCurrentScene()
        self.DivisibilityRule6()
        self.fadeOutCurrentScene()
        self.DivisibilityRule7()
        self.fadeOutCurrentScene()
        self.DivisibilityRule8()
        self.fadeOutCurrentScene()
        self.DivisibilityRule9()
        self.fadeOutCurrentScene()
        self.Introduction2()
        self.fadeOutCurrentScene()
        self.DivisibilityRule10()
        self.fadeOutCurrentScene()
        self.DivisibilityRule11()
        self.fadeOutCurrentScene()
        self.DivisibilityRule12()
        self.Introduction3()
        self.fadeOutCurrentScene()
        self.Example()
        self.fadeOutCurrentScene()
        self.fadeOutCurrentScene()
        
        self.GithubSourceCodeReference()
        
    
    
    def Playing_numbers(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("Place Value","").setPosition([0,2.5,0])
         p11=cvo.CVO().CreateCVO("Example","64").setPosition([4,2,0])
         p12=cvo.CVO().CreateCVO("Expansion","$60+4$").setPosition([5,-2,0])
        
         p13=cvo.CVO().CreateCVO("In words","sixty four").setPosition([-4,2,0]).setangle(-TAU/4)
         
         p11.cvolist.append(p12)
         
         p10.cvolist.append(p11)
        
         p11.cvolist.append(p13)
         
         self.construct1(p10,p10)
         

    def Expanded_Form(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("Expanded Form","").setPosition([0,2.5,0])
         p11=cvo.CVO().CreateCVO("Example","64").setPosition([4,2,0])
         p12=cvo.CVO().CreateCVO("Expansion","$60+4$").setPosition([5,-2,0])
        
         p13=cvo.CVO().CreateCVO("Equal to","$(10*6)+(8)$").setPosition([-4,2,0]).setangle(-TAU/4)
         
         p11.cvolist.append(p12)
         
         p10.cvolist.append(p11)
        
         p12.cvolist.append(p13)
         
         self.construct1(p10,p10)


    def create_animation(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("Factors","every number has factors").setPosition([0,2.5,0])
         p11=cvo.CVO().CreateCVO("Type-1","Prime Numbers").setPosition([-4,2,0])
         p12=cvo.CVO().CreateCVO("Type-2","Composite Numbers").setPosition([4,2,0])
        
        
         p13=cvo.CVO().CreateCVO("Example","2,3,5,7").setPosition([-4,-3,0]).setangle(-TAU/4)
         p14=cvo.CVO().CreateCVO("Example","4,6,8,9").setPosition([4,-3,0]).setangle(-TAU/4)
         p15=cvo.CVO().CreateCVO("Defination","having 1 and itself as factors").setPosition([-4,0,0]).setangle(-TAU/4)
         p16=cvo.CVO().CreateCVO("Defination","having factors other than 1 or itself").setPosition([4,0,0]).setangle(-TAU/4)
         p10.cvolist.append(p11)
         
         p10.cvolist.append(p12)
         p11.cvolist.append(p15)
         p15.cvolist.append(p13)
         p12.cvolist.append(p16)
         p16.cvolist.append(p14)
         self.construct1(p10,p10)

    
    def Introduction(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [-TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Playing With Numbers","")
        p11=cvo.CVO().CreateCVO("Divisibility Rules", "")
        p11.extendOname(["2","3","4","5"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def DivisibilityRule2(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Divisibility Rule 2","Units Place-2,4,6,8,0")
        p11=cvo.CVO().CreateCVO("example","28")
        p12=cvo.CVO().CreateCVO("units place","8")
        p13=cvo.CVO().CreateCVO("Divisibility Rule of 2", "satisfied")
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        self.construct1(p10,p10)
        #self.construct1(p13,p13)
        #self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()

    def DivisibilityRule3(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Divisibility Rule 3","sum of digits divisible by 3")
        p11=cvo.CVO().CreateCVO("example","12")
        p12=cvo.CVO().CreateCVO("sum of digits","1+2=3(divisible by 3)")
        p13=cvo.CVO().CreateCVO("Divisibility Rule of 3", "satisfied")
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        self.construct1(p10,p10)
        #self.construct1(p13,p13)
        #self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()

    def DivisibilityRule4(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Divisibility Rule 4","last 2 digits divisible by 4")
        p11=cvo.CVO().CreateCVO("example","116")
        p12=cvo.CVO().CreateCVO("last 2 digits ","16(divisible by 4)")
        p13=cvo.CVO().CreateCVO("Divisibility Rule of 4", "satisfied")
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        self.construct1(p10,p10)
        #self.construct1(p13,p13)
        #self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()

    def DivisibilityRule5(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Divisibility Rule 5","units place- 0 or 5")
        p11=cvo.CVO().CreateCVO("example","45")
        p12=cvo.CVO().CreateCVO("units digit ","5")
        p13=cvo.CVO().CreateCVO("Divisibility Rule of 5", "satisfied")
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        self.construct1(p10,p10)
        #self.construct1(p13,p13)
        #self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()

    def Introduction1(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [-TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Playing With Numbers","")
        p11=cvo.CVO().CreateCVO("Divisibility Rules", "")
        p11.extendOname(["6","7","8","9"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def DivisibilityRule6(self):
        self.setNumberOfCirclePositions(7)
        #self.angleChoice = [0,0,0]
        #self.isRandom = False

        p10=cvo.CVO().CreateCVO("Divisibility Rule 6","divisible by both 2 and 3").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("example","30").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("units place","0").setPosition([4,0,0]).setangle(-TAU/4)
        p13=cvo.CVO().CreateCVO("Divisibility Rule of 2", "satisfied").setPosition([4,-2,0]).setangle(-TAU/4)
        p14=cvo.CVO().CreateCVO("sum of digits ","3+0=3(divisible)").setPosition([-4,2,0]).setangle(-TAU/4)
        p15=cvo.CVO().CreateCVO("Divisibility Rule of 3", "satisfied").setPosition([-4,-2,0]).setangle(-TAU/4)
        p16=cvo.CVO().CreateCVO("Divisibility Rule of 6", "satisfied").setPosition([0,-2.5,0])
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        p11.cvolist.append(p14)
        p14.cvolist.append(p15)
        self.construct1(p10,p10)
        self.construct1(p16,p16)
        self.play(Create(CurvedArrow(p13.pos,p16.pos)),Create(CurvedArrow(p15.pos,p16.pos)))
        #self.play()

    def DivisibilityRule7(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Divisibility Rule 7","$unit digit*2-given number,check if divisible by 7$")
        p11=cvo.CVO().CreateCVO("example","7")
        p12=cvo.CVO().CreateCVO("$unit digit*2-given number$","$7*2=14-7=7(divisible)$")
        p13=cvo.CVO().CreateCVO("Divisibility Rule of 7", "satisfied")
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        self.construct1(p10,p10)
        #self.construct1(p13,p13)
        #self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()

    

    def DivisibilityRule8(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Divisibility Rule 8","last 3 digits divisible by 8")
        p11=cvo.CVO().CreateCVO("example","328")
        p12=cvo.CVO().CreateCVO("last 3 digits ","328(divisble by 8)")
        p13=cvo.CVO().CreateCVO("Divisibility Rule of 8", "satisfied")
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        self.construct1(p10,p10)
        #self.construct1(p13,p13)
        #self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()

        
    def DivisibilityRule9(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Divisibility Rule 9","sum of digits divisible by 9")
        p11=cvo.CVO().CreateCVO("example","27")
        p12=cvo.CVO().CreateCVO("sum of digits","7+2=9(divisible by 9)")
        p13=cvo.CVO().CreateCVO("Divisibility Rule of 9", "satisfied")
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        self.construct1(p10,p10)
        #self.construct1(p13,p13)
        #self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()

    def Introduction2(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [-TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Playing With Numbers","")
        p11=cvo.CVO().CreateCVO("Divisibility Rules", "")
        p11.extendOname(["10","11","12"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)


    def DivisibilityRule10(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Divisibility Rule 10","units place- 0 ")
        p11=cvo.CVO().CreateCVO("example","50")
        p12=cvo.CVO().CreateCVO("units digit ","0")
        p13=cvo.CVO().CreateCVO("Divisibility Rule of 10", "satisfied")
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        self.construct1(p10,p10)
        #self.construct1(p13,p13)
        #self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play() 

    

    def DivisibilityRule11(self):
        self.setNumberOfCirclePositions(5)
        #self.angleChoice = [0,0,0]
        #self.isRandom = False

        p10=cvo.CVO().CreateCVO("Divisibility Rule 11","$sum of odd place-sum of even place =divisible by 11$")
        p11=cvo.CVO().CreateCVO("example","11")
        p12=cvo.CVO().CreateCVO("$sum of odd place-sum of even place$","$1-1=0$")
        p13=cvo.CVO().CreateCVO("Divisibile by 11", "0 is divisble by 11")
        p14=cvo.CVO().CreateCVO("Divisibility Rule of 11", "satisfied")
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        p13.cvolist.append(p14)
        self.construct1(p10,p10)
        #self.construct1(p13,p13)
        #self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()

    def DivisibilityRule12(self):
        self.setNumberOfCirclePositions(7)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Divisibility Rule 12","both by 4 and 3").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("example","24").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("last 2 digits","24(divisible)").setPosition([4,0,0]).setangle(-TAU/4)
        p13=cvo.CVO().CreateCVO("Divisibility Rule of 4", "satisfied").setPosition([4,-2,0]).setangle(-TAU/4)
        p14=cvo.CVO().CreateCVO("sum of digits ","2+4=6").setPosition([-4,2,0]).setangle(-TAU/4)
        p15=cvo.CVO().CreateCVO("Divisibility Rule of 3", "satisfied").setPosition([-4,-2,0]).setangle(-TAU/4)
        p16=cvo.CVO().CreateCVO("Divisibility Rule of 12", "satisfied").setPosition([0,-2.5,0])
        p10.cvolist.append(p11)
        p11.cvolist.append(p14)
        p14.cvolist.append(p15)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        self.construct1(p10,p10)
        self.construct1(p16,p16)
        self.play(Create(CurvedArrow(p13.pos,p16.pos)),Create(CurvedArrow(p15.pos,p16.pos)))
        #self.play()

        
    def Introduction3(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Playing With Numbers","Puzzles with Missing Digits")
        p11=cvo.CVO().CreateCVO("Step 1","Each letter of the puzzle must stand for just one digit")
        p12=cvo.CVO().CreateCVO("Step 2","The digit with highest place value of the number can not be zero")
        p13=cvo.CVO().CreateCVO("Step 3", "Only one solution")
        
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        self.construct1(p10,p10)
        #self.construct1(p13,p13)
        #self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()
    

    def Example(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Example","$17A + 2A4 = 407$")
        p11=cvo.CVO().CreateCVO("Step 1(units place)","$A + 4 = 7$")
        p12=cvo.CVO().CreateCVO("Step 2","$A = 7-4 = 3$")
        p13=cvo.CVO().CreateCVO("Solution", "$173 + 234 = 407$")
        p10.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        self.construct1(p10,p10)
        # self.construct1(p13,p13)
        #self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()
    def SetDeveloperList(self): 
       self.DeveloperList="Medha Masanam" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade8Chapter15PlayingWithNumbersTopic1.py"
  
      
if __name__ == "__main__":
    scene = Grade8Chapter15PlayingWithNumbersTopic1()
    scene.render()