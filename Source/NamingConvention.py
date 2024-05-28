from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo


class NamingConvention(AbstractAnim):
    
    
    def construct(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("S3 Bucket","my-bucket").setPosition([0,2.5,0])
         p11=cvo.CVO().CreateCVO("Naming Convention","").setPosition([5,2,0])
         p12=cvo.CVO().CreateCVO("Is No Upper Case","YES").setPosition([5,-2,0])
         p13=cvo.CVO().CreateCVO("Is No Underscore","YES").setPosition([-4,3,0]).setangle(-TAU/4)
         p14=cvo.CVO().CreateCVO("Is 3-63 char long","YES").setPosition([-4,1,0]).setangle(-TAU/4)
         p15=cvo.CVO().CreateCVO("Is Not starting with prefix xn--","YES").setPosition([-4,-1,0]).setangle(-TAU/4)
         p16=cvo.CVO().CreateCVO("Is Not ending with suffix -s3alias","YES").setPosition([-4,-3,0]).setangle(TAU/4)

         p10.cvolist.append(p11)
         
         p11.cvolist.append(p12)
         p11.cvolist.append(p13)
         p11.cvolist.append(p14)
         p11.cvolist.append(p15)
         p11.cvolist.append(p16)
         
         self.construct1(p10,p10)
         

      
if __name__ == "__main__":
    scene = NamingConvention()
    scene.render()