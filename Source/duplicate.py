from manim import *
from AbstractAnim import AbstractAnim
import cvo


class TableScene(AbstractAnim):
    def construct(self):
        self.InterestingPatternsofSquare()
        
    
    
    def InterestingPatternsofSquare(self):

        self.setNumberOfCirclePositions(7)
        self.colorChoice=[RED,BLUE,PURPLE,YELLOW,GREEN,ORANGE,PINK]

        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
        p10=cvo.CVO().CreateCVO("Interesting patterns of Square","Chapter:6.2").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Sum of first n odd numbers = $n^2$","$\sum_{i=1}^{n} (2i-1) = n^2$").setPosition([-4.12,1,0]).setangle(TAU/3)
        p12=cvo.CVO().CreateCVO("Numeric Palindrome","$1111^2$=1234321").setPosition([0,0,0]).setangle(-TAU/4)
        p13=cvo.CVO().CreateCVO("Numbers between sucessive squares","2*Base of the first Number").setPosition([4,1,0]).setangle(-TAU/3)
        p14=cvo.CVO().CreateCVO("Example","1+3+5+7=16=$4^2$").setPosition([-2.25,-2,0])
        p15=cvo.CVO().CreateCVO("Example","$1001^2$=1002001").setPosition([0,-2,0])
        p16=cvo.CVO().CreateCVO("Example","$2^2$=4;$3^2$=9=2*2=4").setPosition([2.25,-2,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p11.cvolist.append(p14)
        p12.cvolist.append(p15)
        p13.cvolist.append(p16)
 
    
        p11.setcircleradius(1.25)
        p12.setcircleradius(1.05)
        p14.setcircleradius(1.25)
        p15.setcircleradius(1.1)
        p16.setcircleradius(1.25)

 
        self.construct1(p10,p10)
        #self.play()


    

    


if __name__ == "__main__":
    scene = TableScene()
    scene.render()
