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
        self.GithubSourceCodeReference()
        

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
         
        p1=cvo.CVO().CreateCVO("Arithmetic Mean","Sum of observations divided by no.of observations").setPosition([-3,0,0])
        p2=cvo.CVO().CreateCVO("Sum  of  Observations","x_1+x_2+x_3+x_4........+x_n").setPosition([0,2,0])
        p3=cvo.CVO().CreateCVO("No.of observations","N(1 to n)").setPosition([0,-2,0])
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
        text=Text("Median",font_size=60)
        text.to_edge(UP)
        self.play(Write(text))
 
        text = Tex(
            r"When $n$ is odd, $\left( \frac{n+1}{2} \right)^{\text{th}}$ observation is the median."
        )
        text.scale(0.75)
        self.play(Write(text))
        self.play(text.animate.shift(UP * 1))
        text = Tex(
            r"""
            \begin{itemize}
            \item When $n$ is even, arithmetic mean of $\left( \frac{n}{2} \right)^{\text{th}}$ and $\left( \frac{n}{2} + 1 \right)^{\text{th}}$ is the median.
            \end{itemize}
            """
        )
        text.scale(0.7)
        self.play(Write(text))
        self.play(text.animate.shift(DOWN *1))
        self.wait(2)
          

    def mode(self):
        self.isRandom=False
         
        p1=cvo.CVO().CreateCVO("Mode","").setPosition([0,2,0])
        p2=cvo.CVO().CreateCVO("Definition","The most frequently occurring value").setPosition([-3,0,0])  
        p3=cvo.CVO().CreateCVO("Note:","There may be 2 or 3 or many modes for the same data.").setPosition([3,-1.5,0])
    
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
        p1=cvo.CVO().CreateCVO("Grouped Frequency Distribution","").setPosition([-2,2,0])
        p2=cvo.CVO().CreateCVO("Class Intervals","").setPosition([-2,0,0])
        p3=cvo.CVO().CreateCVO("Upper Limit","Highest value included in a class interval").setPosition([-5,-1,0])
        p4=cvo.CVO().CreateCVO("Lower Limit","Lowest value included in a class interval").setPosition([-3,-3,0])
        p1.cvolist.append(p2)
        p2.cvolist.append(p3)
        p2.cvolist.append(p4)
        self.construct1(p1,p1)
        data = [
            ["Sl. No", "Marks", "No of Students"],
            ["1", "0 - 5", "5"],
            ["2", "5 - 10", "7"],
            ["3", "10 - 15", "10"],
            ["4", "15 - 20", "6"],
            ["5", "20 - 25", "2"],
        ]
        table = Table(
            data,
            include_outer_lines=True,
            line_config={"stroke_color": PINK, "stroke_width": 2},
        )
        table.scale(0.6)
        
        self.play(Create(table))
        self.play(table.animate.shift(RIGHT * 3))
        self.wait(2)
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
        table_data = [
            ["Inclusive classes", "Lower limit", "Upper limit", "Lower boundary", "Upper boundary"],
            ["1-10", "1", "10", "0.5", "10.5"],
            ["11-20", "11", "20", "10.5", "20.5"],
            ["21-30", "21", "30", "20.5", "30.5"]
        ]
        table = Table(
            table_data,
            include_outer_lines=True
        )
        table.scale(0.5)
        self.play(Create(table))
        self.wait(2)
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
        p10.onameList.append("5.U.boundary of a C.I is the avg of its \\\\  U.limit and L.limit of next C.I.")
        p10.onameList.append("6.In exclusive C.I, limits and boundaries are equal;\\\\ in inclusive C.I, they differ.")
        p10.onameList.append("7.Length of class : upper - lower boundary")
        p10.onameList.append("8.Class mark = Avg of upper and lower boundaries of a C.I")
      
       
        
        self.construct2(p10,p10)
        self.fadeOutCurrentScene()

    def cf(self):
        self.isRandom=False
        p1=cvo.CVO().CreateCVO("Cumulative Frequency","").setPosition([0,2.5,0])
        p2=cvo.CVO().CreateCVO("Less than C.F","Adding the frequencies from top").setPosition([-3,0,0])
        p3=cvo.CVO().CreateCVO("Greater than C.F","Adding the frequencies from the bottom").setPosition([3,0,0])
        p1.cvolist.append(p2)
        p1.cvolist.append(p3)
        self.construct1(p1,p1)
        self.fadeOutCurrentScene()
        original_table_data = [
            ["Class Interval\n(Marks)", "UB", "No of\nCandidates\nfrequency"],
            ["0 - 5", "5", "7"],
            ["5 - 10", "10", "10"],
            ["10 - 15", "15", "15"],
            ["15 - 20", "20", "8"],
            ["20 - 25", "25", "3"]
        ]
        original_table = Table(
            original_table_data,
            include_outer_lines=True,
            line_config={"color": WHITE, "stroke_width": 1},
            element_to_mobject_config={"font_size": 36}
        ).scale(0.5)
        self.play(Create(original_table))
        self.play(original_table.animate.shift(LEFT * 4.5))
        self.wait(1)
        less_than_cumulative_data = [
            ["Class Interval\n(Marks)", "Less than\ncumulative\nfrequency"],
            ["0 - 5", "7"],
            ["5 - 10", "17"],
            ["10 - 15", "32"],
            ["15 - 20", "40"],
            ["20 - 25", "43"]
        ]
        less_than_cumulative_table = Table(
            less_than_cumulative_data,
            include_outer_lines=True,
            line_config={"color": WHITE, "stroke_width": 1},
            element_to_mobject_config={"font_size": 36}
        ).scale(0.5)
        less_than_cumulative_table.next_to(original_table, RIGHT, buff=0.6)

        self.play(Create(less_than_cumulative_table))
        self.wait(1)

        greater_than_cumulative_data = [
            ["Class Interval\n(Marks)", "Greater than\ncumulative\nfrequency"],
            ["0 - 5", "43"],
            ["5 - 10", "36"],
            ["10 - 15", "26"],
            ["15 - 20", "11"],
            ["20 - 25", "3"]
        ]
        greater_than_cumulative_table = Table(
            greater_than_cumulative_data,
            include_outer_lines=True,
            line_config={"color": WHITE, "stroke_width": 1},
            element_to_mobject_config={"font_size": 36}
        ).scale(0.5)
        greater_than_cumulative_table.next_to(less_than_cumulative_table, RIGHT, buff=0.6)
        self.play(Create(greater_than_cumulative_table))
        self.wait(2)
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

        values = [4, 7, 1, 8, 5]
        bar_labels = ["A", "B", "C", "D", "E"]
        bar_chart = BarChart(
            values=values,
            bar_names=bar_labels,
            bar_width=0.5,
            bar_colors=[BLUE, GREEN, RED, YELLOW, ORANGE],
            y_range=[0, 10, 2],  
            x_axis_config={"font_size": 24},  
            y_axis_config={"font_size": 24}, 
            
        )
        title = Text("Vertical Bar Graph", font_size=48)
        title.to_edge(UP)
        self.add(bar_chart, title)
        self.play(Create(bar_chart))
        self.wait(3)

        self.fadeOutCurrentScene()

        values = [4, 7, 1, 8, 5]
        bar_labels = ["A", "B", "C", "D", "E"]
        bar_chart = BarChart(
            values=values,
            bar_names=bar_labels,
            bar_width=0.5,
            bar_colors=[BLUE, GREEN, RED, YELLOW, ORANGE],
            y_range=[0, 10, 2], 
            x_axis_config={"font_size": 24},  
            y_axis_config={"font_size": 24},  
            
        )
        bar_chart.rotate(PI / 2)
        title = Text("Horizontal Bar Graph", font_size=48)
        title.to_edge(UP)
        title.shift(DOWN)
        self.add(bar_chart, title)
        self.play(Create(bar_chart))
        self.wait(3)
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

    def SetDeveloperList(self):
        self.DeveloperList="Srujan"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade8CH7FrequencyDistribution.py"

        

   
if __name__ == "__main__":
    scene = FrequencyDistribution()
    scene.render()