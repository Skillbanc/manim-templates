from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class FrequencyDistribution(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.central_tendency_measure()
        self.fadeOutCurrentScene()
        self.mean()
        self.fadeOutCurrentScene()
        self.median()
        self.fadeOutCurrentScene()
        self.mode()
        self.fadeOutCurrentScene()
        self.org_of_gd()
        self.GroupedFD()
        self.LAB()
        self.con_GFD()
        self.gfd()
        self.char_GFD()
        self.cf()
        self.graph_rep_data()
        self.graph_rep_gfd()
        self.GitHubSourceCodeReference()

    def central_tendency_measure(self):
        self.isRandom=False
        p1=cvo.CVO().CreateCVO("Basic Measures Of Central Tendency","").setPosition([0,2.5,0])
        p2=cvo.CVO().CreateCVO("Measure 1","Arithmetic Mean").setPosition([-5,0,0])
        p3=cvo.CVO().CreateCVO("Measure 2","Median").setPosition([0,-2,0])
        p4=cvo.CVO().CreateCVO("Measure 3","Mode").setPosition([5,0,0])

        p1.cvolist.append(p2)
        p1.cvolist.append(p3)
        p1.cvolist.append(p4)        

        self.construct1(p1,p1)


    def mean(self):
        self.isRandom=False
         
        p1=cvo.CVO().CreateCVO("Arithmetic Mean","sum of observations divided by no.of observations").setPosition([-3,0,0])
        p2=cvo.CVO().CreateCVO("sum of observations","x_1+x_2+x_3+x_4........+x_n").setPosition([0,2,0])
        p3=cvo.CVO().CreateCVO("no.of observations","N(1 to n)").setPosition([0,-2,0])
        p4=cvo.CVO().CreateCVO("Mean","(x_1+x_2+x_3+x_4+........+x_n)/N").setPosition([5,0,0])
          
        p1.cvolist.append(p2)
         
        p1.cvolist.append(p3)
        p2.SetIsMathText(True)
        p4.SetIsMathText(True)
        self.construct1(p1,p1)
        
        self.construct1(p4,p4)
        self.play(Create(CurvedArrow(p2.pos,p4.pos)),Create(CurvedArrow(p3.pos,p4.pos)))


    def median(self):
        self.isRandom=False
         
        p1=cvo.CVO().CreateCVO("Median","").setPosition([0,2,0])
        p2=cvo.CVO().CreateCVO("case 1: odd no.of observations(n)","median=((n+1)/2)th ").setPosition([-3,0,0])
        p3=cvo.CVO().CreateCVO("case 2: even no.of observations(n)","((n/2)th +((n+1)/2)th )/2 value").setPosition([3,0,0])
          
        p1.cvolist.append(p2)
        p1.cvolist.append(p3)
         
        p2.SetIsMathText(True)
        p3.SetIsMathText(True)
         
        self.construct1(p1,p1)

    def mode(self):
        self.isRandom=False
         
        p1=cvo.CVO().CreateCVO("Mode","").setPosition([0,2,0])
        p2=cvo.CVO().CreateCVO("Definition","The most frequently occurring value").setPosition([-3,0,0])  
        p3=cvo.CVO().CreateCVO("note:","There may be 2 or 3 or many modes for the same data.").setPosition([3,-1.5,0])
    
        p1.cvolist.append(p2)
        p1.cvolist.append(p3)
        self.construct1(p1,p1)

    def org_of_gd(self):
        self.isRandom=False
        p1=cvo.CVO().CreateCVO("Organisation of Grouped Data","").setPosition([0,2.5,0])
        p2=cvo.CVO().CreateCVO("Grouped Frequency Distribution","").setPosition([-4,1,0])
        p3=cvo.CVO().CreateCVO("Limits and Boundaries","").setPosition([-3,-1.5,0])
        p4=cvo.CVO().CreateCVO("Construction of Grouped Frequency Distribution","").setPosition([2,-2,0])
        p5=cvo.CVO().CreateCVO("Characteristics of Grouped Frequency Distribution","").setPosition([3,0.7,0])
        p1.cvolist.append(p2)
        p1.cvolist.append(p3)
        p1.cvolist.append(p4)
        p1.cvolist.append(p5)
        self.construct1(p1,p1)
        self.fadeOutCurrentScene()

    def GroupedFD(self):
        self.isRandom=False
        p1=cvo.CVO().CreateCVO("Grouped Frequency Distribution","").setPosition([0,2,0])
        p2=cvo.CVO().CreateCVO("Class Intervals","").setPosition([0,0,0])
        p3=cvo.CVO().CreateCVO("Upper Limit","Highest value included in a class interval").setPosition([-3,-1,0])
        p4=cvo.CVO().CreateCVO("Lower Limit","Lowest value included in a class interval").setPosition([3,-1,0])
        p1.cvolist.append(p2)
        p2.cvolist.append(p3)
        p2.cvolist.append(p4)
        self.construct1(p1,p1)
        self.fadeOutCurrentScene()

    def LAB(self):
        self.isRandom=False
        p1=cvo.CVO().CreateCVO("Limits and Boundaries","").setPosition([0,2.5,0])
        p2=cvo.CVO().CreateCVO("Limits","").setPosition([-3,1.5,0])
        p3=cvo.CVO().CreateCVO("Boundaries","").setPosition([3,1.5,0])
        p4=cvo.CVO().CreateCVO("Upper limit","Highest value included in a class interval").setPosition([-5,-1,0])
        p5=cvo.CVO().CreateCVO("Lower limit","Lower value included in a class interval").setPosition([-2,-2,0])
        p6=cvo.CVO().CreateCVO("Upper boundary","value marking the end of C.I, adding  0.5 to the upper limit.").setPosition([1,-1,0])
        p7=cvo.CVO().CreateCVO("Lower boundary","value marking the end of C.I, subtracting  0.5 to the lower limit.").setPosition([3,-2.5,0])
        p1.cvolist.append(p2)
        p1.cvolist.append(p3)
        p2.cvolist.append(p4)
        p2.cvolist.append(p5)
        p3.cvolist.append(p6)
        p3.cvolist.append(p7)
        self.construct1(p1,p1)
        self.fadeOutCurrentScene()

    def con_GFD(self):
        self.isRandom=False
        p1=cvo.CVO().CreateCVO("Construction of Grouped Frequency Distribution","").setPosition([0,2.5,0])
        p2=cvo.CVO().CreateCVO("Step 1: Find Range of Data","Range = Max. value-Min value").setPosition([-4,1.5,0])
        p3=cvo.CVO().CreateCVO("Step 2: Decide no.of class intervals(random)","length of class= (max.value)/no.of class intervals").setPosition([-3,-0.5,0])
        p4=cvo.CVO().CreateCVO("Step 3: Write inclusive class intervals","Boundaries are included").setPosition([0,-2.5,0])
        p5=cvo.CVO().CreateCVO("Step 4: ","Distribute the Observations using Tally marks").setPosition([4,-0.5,0])
        p6=cvo.CVO().CreateCVO("Step 5:","Use the Tally marks to write the frequencies in the table").setPosition([4,1.5,0])
        p1.cvolist.append(p2)
        p1.cvolist.append(p3)
        p1.cvolist.append(p4)
        p1.cvolist.append(p5)
        p1.cvolist.append(p6)
        self.construct1(p1,p1)
        self.fadeOutCurrentScene()

    def gfd(self):
        self.isRandom=False

        p1=cvo.CVO().CreateCVO("Characteristics of GFD","").setPosition([-4,-2,0])
        self.construct1(p1,p1)



    def char_GFD(self):
        self.isRandom=False
        
        

        p10=cvo.CVO().CreateCVO("Characteristics of GFD","")
        p10.onameList.append("1.GFD has class intervals")
        p10.onameList.append("2.Class interval has upper and lower limits")
        p10.onameList.append("3.Inclusive C.I : Both the upper and lower limits are included")
        p10.onameList.append("4.Exclusive C.I : The upper limit is excluded")
        p10.onameList.append("5.U.boundary of a C.I is the avg of its \\\\ U.limit and L.limit of next C.I.")
        p10.onameList.append("6.In exclusive C.I, limits and boundaries are equal;\\\\ in inclusive C.I, they differ.")
        p10.onameList.append("7.Length of class : upper - lower boundary")
        p10.onameList.append("8.Class mark = Avg of upper and lower boundaries of a C.I")
      
       
        
        self.construct2(p10,p10)
        self.fadeOutCurrentScene()

    def cf(self):
        self.isRandom=False
        p1=cvo.CVO().CreateCVO("Cumulative Frequency","").setPosition([0,2.5,0])
        p2=cvo.CVO().CreateCVO("Lesser than C.F","Adding the frequencies from bottom").setPosition([-5,0,0])
        p3=cvo.CVO().CreateCVO("Greater than C.F","Adding the frequencies from the top").setPosition([5,0,0])
        p1.cvolist.append(p2)
        p1.cvolist.append(p3)
       

        self.construct1(p1,p1)
        self.fadeOutCurrentScene()

    def graph_rep_data(self):
        self.isRandom=False
        p1=cvo.CVO().CreateCVO("Graphical representation of Data","").setPosition([0,2.5,0])
        p2=cvo.CVO().CreateCVO("BAR GRAPHS","").setPosition([0,0,0])
        p3=cvo.CVO().CreateCVO("Vertical Bars","Bars are parallel to y-axis").setPosition([-3,-1,0])
        p4=cvo.CVO().CreateCVO("Horizontal Bars","Bars are parallel to x-axis").setPosition([3,-1,0])
        p1.cvolist.append(p2)
        p2.cvolist.append(p3)
        p2.cvolist.append(p4)
       

        self.construct1(p1,p1)
        self.fadeOutCurrentScene()
         
    def graph_rep_gfd(self):
        self.isRandom=False
        p1=cvo.CVO().CreateCVO("Graphical Rep. of Grouped Frequency Distribution","").setPosition([0,2.5,0])
        p2=cvo.CVO().CreateCVO("Histogram","Representation of continuous C.I").setPosition([-3,1,0])
        p3=cvo.CVO().CreateCVO("Frequency Polygon","Like a histogram, but connecting class midpoints with lines").setPosition([-3,-1.5,0])
        p4=cvo.CVO().CreateCVO("Frequency Curve","Like a freqency polygon, but connecting with curved lines ").setPosition([3,-1.5,0])
        p5=cvo.CVO().CreateCVO("Graph of Cumulative Frequency Distribution","Cumulative frequency graph (ogive) visualizes data").setPosition([3,1,0])
        p1.cvolist.append(p2)
        p1.cvolist.append(p3)
        p1.cvolist.append(p4)
        p1.cvolist.append(p5)
       

        self.construct1(p1,p1)
        self.fadeOutCurrentScene()

    def GitHubSourceCodeReference(self):
        
        p1 = cvo.CVO().CreateCVO("SOURCE CODE REFERENCE", ""). setPosition([0,2.5,0])
        p2 = cvo.CVO().CreateCVO("Github URL", "https://github.com/Skillbanc/manim-templates").setPosition([-3,0,0])
        p3 = cvo.CVO().CreateCVO("File Name", "FREQUENCY DISTRIBUTION ").setPosition([3,-1.5,0])
        p1.cvolist.append(p2)
        p1.cvolist.append(p3)

        p2.setcircleradius(3)
        p3.setcircleradius(3)
        self.construct1(p1,p1)
         
if __name__ == "__main__":
    scene = FrequencyDistribution()
    scene.render()