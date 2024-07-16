from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
from scipy.interpolate import make_interp_spline


import cvo

class FrequencyDistributionTandG(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.central_tendency_measure()
        self.fadeOutCurrentScene()
        self.mean()
        self.fadeOutCurrentScene()
        self.median()
        self.medani()
        self.fadeOutCurrentScene()
        self.mode()
        self.modani()
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
        self.SubscribeYoutube()
        self.fadeOutCurrentScene()
                

    def central_tendency_measure(self):
        text=Text("""Frequency Distribution
                  Tables and Graphs""",font_size=40,color=WHITE)
        self.play(Write(text))
        self.wait(2)
        self.fadeOutCurrentScene()
        self.isRandom=False
        self.angleChoice=[-TAU/3,TAU/5,TAU/3]
        p1=cvo.CVO().CreateCVO("Basic Measures Of Central Tendency","").setPosition([0,2.5,0])
        p2=cvo.CVO().CreateCVO("Arithmetic Mean","").setPosition([-5,0,0])
        p3=cvo.CVO().CreateCVO("Median","").setPosition([0,-2,0])
        p4=cvo.CVO().CreateCVO("Mode","").setPosition([5,0,0])
        p1.cvolist.append(p2)
        p1.cvolist.append(p3)
        p1.cvolist.append(p4)        
        self.construct1(p1,p1)


    def mean(self):
        self.isRandom=False
        p1=cvo.CVO().CreateCVO("Arithmetic Mean","").setPosition([-5,2.5,0])
        p2=cvo.CVO().CreateCVO("Definition","Sum of observations divided by no.of observations").setPosition([-4,-2,0])
        p3=cvo.CVO().CreateCVO("Sum  of  Observations","x_1+x_2+x_3+x_4........+x_n").setPosition([1,2,0])
        p4=cvo.CVO().CreateCVO("No.of observations","N").setPosition([1,-2,0])
        p5=cvo.CVO().CreateCVO("Formula","(x_1+x_2+x_3+x_4+........+x_n)/N").setPosition([4,0,0])
        p1.cvolist.append(p2)
        p1.cvolist.append(p3)
        p1.cvolist.append(p4)
        p3.SetIsMathText(True)
        p5.SetIsMathText(True)
        self.construct1(p1,p1)
        self.construct1(p5,p5)
        self.play(Create(CurvedArrow(p3.pos,p5.pos)),Create(CurvedArrow(p4.pos,p5.pos)))


    def median(self):
        self.isRandom=False
        self.positionChoice = [[0,2.5,0],[-4,0,0],[0,-2,0],[4,0,0],[4,-3,0]]

        p1=cvo.CVO().CreateCVO("Median","")
        p2=cvo.CVO().CreateCVO("Formulae","N is even, N is odd")
        p2.setcircleradius(1.5)
        p3=cvo.CVO().CreateCVO("Odd","(N+1)/2 th term")
        p4=cvo.CVO().CreateCVO("Even","((N+1/2) th term + N/2 th term)/2").SetIsMathText(True)
        p4.setcircleradius(1.5)
        p1.cvolist.append(p2)
        p2.cvolist.append(p3)
        p2.cvolist.append(p4)
        self.construct1(p1,p1)
        self.fadeOutCurrentScene()

    def medani(self):
        title=Text("Median for even number of observations:").to_edge(UP)
        title.add(Underline(title, buff=0.1))
        dataset = [26, 35, 15, 70]
        dataset_text = MathTex(r"\text{observations: } \{26, 35, 15, 70\}")
        dataset_text.next_to(title,DOWN)
        obs1=Text("number of observations(n)=4").next_to(dataset_text,DOWN, buff=0.5)

        sorted_dataset = sorted(dataset)
        sorted_text = MathTex(r"\text{Sorted in ascending order: }").next_to(obs1, DOWN)
        sorted_elements = VGroup(
            *[MathTex(f"{x}, " if i < len(sorted_dataset) - 1 else f"{x}").set_color(WHITE) for i, x in enumerate(sorted_dataset)]
        ).arrange(RIGHT, buff=0.2).next_to(sorted_text, DOWN)
        sorted_group = VGroup(sorted_text, sorted_elements)
        median_index1 = len(sorted_dataset) // 2
        median = (sorted_dataset[median_index1 - 1] + sorted_dataset[median_index1]) / 2
        median_text = MathTex(r"\text{Median} = \frac{\frac{n^{\text{th term}}}{2} + (\frac{n}{2} + 1)^{\text{th term}}}{2}").next_to(sorted_group, DOWN)
        subsi=MathTex(r"=\frac{2^{nd term}+3^{rd term}}{2}=").next_to(median_text,DOWN)
        subs=MathTex(r"=\frac{26+35}{2}=").next_to(subsi,RIGHT)
        median_value = MathTex(str(median)).next_to(subs, RIGHT)
        self.play(Write(title))
        self.play(Write(dataset_text,run_time=4))
        self.play(Write(obs1))
        self.wait(1)
        self.play(Write(sorted_group, run_time=5))
        self.play(
            sorted_elements[median_index1 - 1].animate.set_color(YELLOW), 
            sorted_elements[median_index1].animate.set_color(YELLOW)
        )
        self.play(Write(median_text))
        self.play(Write(subsi))
        self.play(Write(subs))
        self.wait(2)
        self.play(Write(median_value))
        self.wait(2)
        self.fadeOutCurrentScene()

        # Second dataset with an odd number of observations
        title2 = Text("Median for odd number of observations:").to_edge(UP)
        title2.add(Underline(title2, buff=0.1))
        dataset2 = [10, 45, 36, 11, 25]
        dataset_text2 = MathTex(r"\text{observations: } \{10, 45, 36, 11, 25\}")
        dataset_text2.next_to(title2, DOWN)
        obs2 = Text("number of observations (n) = 5", font_size=24).next_to(dataset_text2, DOWN, buff=0.5)
        sorted_dataset2 = sorted(dataset2)
        sorted_text2 = MathTex(r"\text{Sorted in ascending order: }").next_to(obs2, DOWN)
        sorted_elements2 = VGroup(
            *[MathTex(f"{x}, " if i < len(sorted_dataset2) - 1 else f"{x}").set_color(WHITE) for i, x in enumerate(sorted_dataset2)]
        ).arrange(RIGHT, buff=0.2).next_to(sorted_text2, DOWN)
        sorted_group2 = VGroup(sorted_text2, sorted_elements2)
        median_index2 = len(sorted_dataset2) // 2
        median2 = sorted_dataset2[median_index2]
        median_text2 = MathTex(r"\text{Median} = ").next_to(sorted_group2, DOWN)
        medform2 = MathTex(r"\frac{n+1}{2}^{\text{th term}}").next_to(median_text2, RIGHT)
        medsub=MathTex(r"=\frac{5+1}{2}^{\text{th term}} = 3^{rd term} ").next_to(medform2, DOWN)
        median_value2 = MathTex("=",str(median2)).next_to(medsub, DOWN)
        median_text2.shift(LEFT * 1)
        medform2.shift(LEFT * 1)
        medform2.shift(DOWN * 0.2)
        median_value2.shift(DOWN * 0.2)
        median_value2.shift(LEFT * 1)
        self.play(Write(title2))
        self.play(Write(dataset_text2))
        self.wait(1)
        self.play(Write(obs2))
        self.play(Write(sorted_group2, run_time=6))
        self.wait(1)
        self.play(Write(median_text2))
        self.play(Write(medform2))
        self.wait(2)
        self.play(Write(medsub))
        self.play(Write(median_value2))
        self.play(
            sorted_elements2[median_index2].animate.set_color(YELLOW)
        )
        self.wait(4)

    def mode(self):
        self.isRandom=False
        self.positionChoice =[[-4,2,0],[4,2,0],[-4,-2,0],[4,-2,0],[0,-1,0]]
        p10=cvo.CVO().CreateCVO("Mode","")
        p11=cvo.CVO().CreateCVO("Definition","The most frequent value in a dataset")
        p10.cvolist.append(p11)
        p12=cvo.CVO().CreateCVO("Sample Data","40,50,69,50")
        p121=cvo.CVO().CreateCVO("Mode","50")
        p12.cvolist.append(p121)
        p13=cvo.CVO().CreateCVO("Bimodal Data","values which occur more and equal number of times")
        p10.cvolist.append(p13)
        self.construct1(p10,p10)
        self.construct1(p12,p12)
        self.fadeOutCurrentScene()

    def modani(self):
        title = Text("Mode").to_edge(UP)
        dataset = [3,3,2,6,7,4,8,9,2,5,6,2]
        dataset_text = Text(f"Example data : {dataset}", font_size=36).next_to(title, DOWN)
        self.play(Write(title))
        self.play(Write(dataset_text))
        self.wait(1)

        mode_value = max(set(dataset), key=dataset.count)
        mode_text = Text(f"Mode= {mode_value}", font_size=36).next_to(dataset_text, DOWN, buff=1.0)

        highlighted_dataset = VGroup()
        for i, value in enumerate(dataset):
            text_value = Text(f"{value}," if i < len(dataset) - 1 else str(value), font_size=36)
            if value == mode_value:
                text_value.set_color(YELLOW)
            highlighted_dataset.add(text_value)
        highlighted_dataset.arrange(RIGHT, buff=0.2).next_to(dataset_text, DOWN)
        
        self.play(Write(highlighted_dataset))
        self.wait(4)

        self.play(Write(mode_text))
        self.wait(3)


    def org_of_gd(self):
        self.isRandom=False
        self.angleChoice=[TAU/2,TAU/2,-TAU/5,TAU/5]
        p1=cvo.CVO().CreateCVO("Organisation of Grouped Data","").setPosition([-4.5,2.5,0])
        p2=cvo.CVO().CreateCVO("Grouped Frequency Distribution","").setPosition([-4,0,0])
        p3=cvo.CVO().CreateCVO("Limits and Boundaries","").setPosition([-4,-2,0])
        p4=cvo.CVO().CreateCVO("Construction of Grouped Frequency Distribution","").setPosition([2.5,-2,0])
        p5=cvo.CVO().CreateCVO("Characteristics of Grouped Frequency Distribution","").setPosition([2.5,1.5,0])
        p1.cvolist.append(p2)
        p2.cvolist.append(p3)
        p2.cvolist.append(p4)
        p2.cvolist.append(p5)
        self.construct1(p1,p1)
        self.fadeOutCurrentScene()

    def GroupedFD(self):
        self.isRandom=False
        self.angleChoice=[TAU/4,-TAU/4,TAU/4]
        p1=cvo.CVO().CreateCVO("Grouped Frequency Distribution","").setPosition([-4,-2.5,0])
        p2=cvo.CVO().CreateCVO("Class Intervals","").setPosition([-3,0,0])
        p3=cvo.CVO().CreateCVO("Upper Limit","").setPosition([-5,2.5,0])
        p4=cvo.CVO().CreateCVO("Lower Limit","").setPosition([-2.5,2.5,0])
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
        table.move_to(RIGHT*3)
        self.play(Create(table))
        text=Text("""   Here, in the marks column the 
            left and right side values are 
            lower and upper limits respectively""",font_size=25,color=WHITE)
        text.next_to(table,UP,buff=0.4)
        self.play(Write(text))
        self.wait(3)
        self.fadeOutCurrentScene()

    def LAB(self):
        self.isRandom=False
        self.angleChoice=[TAU/4,-TAU/4,TAU/4,-TAU/4,-TAU/4,TAU/4]
        p1=cvo.CVO().CreateCVO("Limits and Boundaries","").setPosition([0,2.5,0])
        p2=cvo.CVO().CreateCVO("Limits","").setPosition([-3.5,1.5,0])
        p3=cvo.CVO().CreateCVO("Boundaries","").setPosition([3.5,1.5,0])
        p4=cvo.CVO().CreateCVO("Upper limit","").setPosition([-6,-2,0])
        p5=cvo.CVO().CreateCVO("Lower limit","").setPosition([-1.5,-2,0])
        p6=cvo.CVO().CreateCVO("Upper boundary","").setPosition([1.5,-2,0])
        p7=cvo.CVO().CreateCVO("Lower boundary","").setPosition([5.5,-2,0])
        p1.cvolist.append(p2)
        p1.cvolist.append(p3)
        p2.cvolist.append(p4)
        p2.cvolist.append(p5)
        p3.cvolist.append(p6)
        p3.cvolist.append(p7)
        self.construct1(p1,p1)
        self.fadeOutCurrentScene()
        text1=Text("Limits and Boundaries (for inclusive class intervals)",font_size=40)
        text1.to_edge(UP)
        self.play(Write(text1))
        text2=Text("Upper Limit: Highest value included in a class interval",font_size=25)
        text2.next_to(text1,DOWN,buff=0.2)
        self.play(Write(text2))
        text3=Text("Lower Limit: Lowest value included in a class interval",font_size=25)
        text3.next_to(text2,DOWN,buff=0.2)
        self.play(Write(text3))
        text4=Text("Upper Boundary: value marking the end of C.I, adding  0.5 to the upper limit.",font_size=25)
        text4.next_to(text3,DOWN,buff=0.2)
        self.play(Write(text4))
        text5=Text("Lower Boundary: value marking the end of C.I, subtracting 0.5 to the lower limit.",font_size=25)
        text5.next_to(text4,DOWN,buff=0.2)
        self.play(Write(text5))
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
        table.next_to(text5,DOWN,buff=0.5)
        self.play(Create(table,run_time=6))
        self.wait(2)
        self.fadeOutCurrentScene()

    def con_GFD(self):
        self.isRandom=False
        title = Text("Construction of GFD").to_edge(UP)
        self.play(Write(title))
        title1 = Text("""Consider the marks of 50 students in Mathematics secured in Summative assessment I as
                    31, 14, 0, 12, 20, 23, 26, 36, 33,41, 37,25, 22, 14,3, 25, 
                    27, 34, 38, 43, 32, 22, 28, 18, 7, 21, 20, 35, 36, 45, 9, 19, 29,
                    25, 33, 47, 35, 38, 25, 34, 38, 24, 39, 1, 10, 24, 27, 25, 18, 8.""").next_to(title,DOWN,buff=0.5).scale(0.5)
        self.play(Write(title1))
        self.wait(2)

        step1 = Text("Step 1: Find the range of the data").scale(0.6)
        range_formula = MathTex(r"\text{Range} = \text{Maximum value} - \text{Minimum value}", r"= 47 - 0 = 47").scale(0.6).next_to(step1, DOWN)
        self.play(Write(step1))
        self.play(Write(range_formula))
        self.wait(2)
        self.fadeOutCurrentScene()

        step2 = Text("Step 2: Decide the number of class intervals").scale(0.6)
        class_intervals = MathTex(r"\text{If no of class intervals} = 6", r"\Rightarrow \text{Length of the class interval} = \frac{47}{6} \approx 8").scale(0.6).next_to(step2, DOWN)
        self.play(Write(step2))
        self.play(Write(class_intervals))
        self.wait(2)
        self.fadeOutCurrentScene()

        step3 = Text("Step 3: Write inclusive class intervals").scale(0.6)
        intervals_text = Text("0-7, 8-15, 16-23, 24-31, 32-39, 40-47").scale(0.6).next_to(step3, DOWN)
        self.play(Write(step3))
        self.play(Write(intervals_text))
        self.wait(2)
        self.fadeOutCurrentScene()

        step4 = Text("Step 4: Distribute the observations into class intervals").scale(0.6).to_edge(UP)
        tally_table = Table(
            [["0-7", "4"], ["8-15", "6"], ["16-23", "9"], ["24-31", "13"], ["32-39", "14"], ["40-47", "4"]],
            col_labels=[Text("Intervals (Marks)"), Text("No of students")],
            row_labels=[Text("1"), Text("2"), Text("3"), Text("4"), Text("5"), Text("6")],
            top_left_entry=Text("No")
        ).scale(0.6).next_to(step4, DOWN)
        self.play(Write(step4))
        self.play(Create(tally_table,run_time=8))
        self.wait(2)
        self.fadeOutCurrentScene()

        step5 = Text("Step 5: Count the tally marks and write the frequencies").scale(0.6)
        self.play(Write(step5))
        self.wait(2)
        self.fadeOutCurrentScene()

        headers = ["Intervals (Marks)","Tally Marks", "No of students"]
        header_texts = [Text(header, font_size=40) for header in headers]
        
        data = [
            ["0-7","||||", "4"],
            ["8-15","||||\ |", "6"],
            ["16-23","||||\ ||||", "9"],
            ["24-31","||||\ ||||\ |||", "13"],
            ["32-39","||||\ ||||\ ||||", "14"],
            ["40-47","||||", "4"]
        ]
        
        table = Table(
            data,
            col_labels=[Text(headers[0], font_size=40), Text(headers[1], font_size=40), Text(headers[2], font_size=40)],
            top_left_entry=Text("", font_size=24),
            line_config={"stroke_width": 1, "color": WHITE}
        ).scale(0.5).next_to(title, DOWN)
        self.play(Create(table,run_time=8))
        self.wait(2)
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
        p10.onameList.append("6.Length of class : upper - lower boundary")
        p10.onameList.append("7.In exclusive C.I, limits and boundaries are equal;\\\\ in inclusive C.I, they differ.")
        p10.onameList.append("8.Class mark = Avg of upper and lower boundaries of a C.I")
      
       
        
        self.construct2(p10,p10)
        self.fadeOutCurrentScene()

    def cf(self):
        self.isRandom=False
        self.angleChoice=[-TAU/4,TAU/4]
        p1=cvo.CVO().CreateCVO("Cumulative Frequency","").setPosition([0,2.5,0])
        p2=cvo.CVO().CreateCVO("Less than C.F","").setPosition([-3,0,0])
        p3=cvo.CVO().CreateCVO("Greater than C.F","").setPosition([3,0,0])
        p1.cvolist.append(p2)
        p1.cvolist.append(p3)
        self.construct1(p1,p1)
        self.fadeOutCurrentScene()
        text=Text("L.C.F and G.C.F",font_size=40)
        text.to_edge(UP)
        self.play(Write(text))
        text1=Text("Less than Cumulative Frequency : Adding the frequencies from top",font_size=20)
        text1.next_to(text,DOWN,buff=0.3)
        self.play(Write(text1))
        text2=Text("Greater than Cumulative Frequency : Adding the frequencies from the bottom",font_size=20)
        text2.next_to(text1,DOWN,buff=0.3)
        self.play(Write(text2))
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
        original_table.shift(LEFT * 4.5,DOWN * 0.5)
        self.play(Create(original_table,run_time=5))
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
        less_than_cumulative_table.next_to(original_table, RIGHT, buff=0.5)

        self.play(Create(less_than_cumulative_table,run_time=5))
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
        greater_than_cumulative_table.next_to(less_than_cumulative_table, RIGHT, buff=0.4)
        self.play(Create(greater_than_cumulative_table,run_time=5))
        lcf_additions = [less_than_cumulative_table.get_entries((2, 2)), less_than_cumulative_table.get_entries((3, 2)), less_than_cumulative_table.get_entries((4, 2)), less_than_cumulative_table.get_entries((5, 2)), less_than_cumulative_table.get_entries((6, 2))]
        lcf_texts = ["7", "10 + 7", "15 + 17", "8 + 32", "3 + 40"]
        
        for i, lcf in enumerate(lcf_additions):
            self.play(lcf.animate.set_color(YELLOW))
            self.play(Transform(lcf, Text(lcf_texts[i], font_size=18).move_to(lcf)))
            self.wait(1)
            self.play(lcf.animate.set_color(BLUE))
    
        gcf_additions = [greater_than_cumulative_table.get_entries((6, 2)), greater_than_cumulative_table.get_entries((5, 2)), greater_than_cumulative_table.get_entries((4, 2)), greater_than_cumulative_table.get_entries((3, 2)), greater_than_cumulative_table.get_entries((2, 2))]
        gcf_texts = ["3", "3 + 8", "11 + 15", "26 + 10", "36 + 7"]
        
        for i, gcf in enumerate(gcf_additions):
            self.play(gcf.animate.set_color(YELLOW))
            self.play(Transform(gcf, Text(gcf_texts[i], font_size=18).move_to(gcf)))
            self.wait(1)
            self.play(gcf.animate.set_color(BLUE))

        self.wait(3)
        self.fadeOutCurrentScene()

    def graph_rep_data(self):
        self.isRandom=False
        self.angleChoice=[TAU/4,-TAU/4,TAU/4]
        p1=cvo.CVO().CreateCVO("Graphical representation of Data","").setPosition([-4,2.5,0])
        p2=cvo.CVO().CreateCVO("BAR GRAPHS","").setPosition([1,2,0])
        p3=cvo.CVO().CreateCVO("Vertical Bars","Bars are parallel to y-axis").setPosition([-3,-1,0])
        p4=cvo.CVO().CreateCVO("Horizontal Bars","Bars are parallel to x-axis").setPosition([3,-1,0])
        p1.cvolist.append(p2)
        p2.cvolist.append(p3)
        p2.cvolist.append(p4)
        self.construct1(p1,p1)
        self.fadeOutCurrentScene()

        text=Text("Vertical Bar Graph",font_size=40)
        text.to_edge(UP)
        self.play(Write(text))

        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            axis_config={"include_tip": True},
            x_axis_config={
                "numbers_to_include": np.arange(0, 10, 1),
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 10, 1),
            },
        ).scale(0.6)
        x_label = axes.get_x_axis_label(Tex("X-Axis"), edge=DOWN, direction=DOWN, buff=0.5)
        y_label = axes.get_y_axis_label(Tex("Y-Axis"), edge=LEFT, direction=LEFT, buff=0.5)
        bars = VGroup()
        data = [2, 5, 3, 8, 6]
        for i, height in enumerate(data):
            bar = Rectangle(
                width=0.8, 
                height=height, 
                fill_color=BLUE, 
                fill_opacity=0.7
            ).scale(0.5)
            bar.move_to(axes.c2p(i + 1, 0), aligned_edge=DOWN)
            bars.add(bar)
        self.play(Create(axes,run_time=4), Write(x_label), Write(y_label))

        for bar in bars:
            self.play(FadeIn(bar, shift=DOWN))
            self.wait(0.5)
        self.wait(2)
        self.fadeOutCurrentScene()

        text=Text("Horizontal Bar Graph",font_size=40)
        text.to_edge(UP)
        self.play(Write(text))
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 6, 1],
            axis_config={"include_tip": True},
            x_axis_config={
                "numbers_to_include": np.arange(0, 10, 1),
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 6, 1),
            },
        ).scale(0.5)
        x_label = axes.get_x_axis_label(Tex("X-Axis"), edge=DOWN, direction=DOWN, buff=0.5)
        y_label = axes.get_y_axis_label(Tex("Y-Axis"), edge=LEFT, direction=LEFT, buff=0.5)
        bars = VGroup()
        data = [2, 5, 3, 8, 6]
        for i, width in enumerate(data):
            bar = Rectangle(
                width=width, 
                height=0.8, 
                fill_color=BLUE, 
                fill_opacity=0.7
            ).scale(0.5)
            bar.move_to(axes.c2p(0, i + 1), aligned_edge=LEFT)
            bars.add(bar)
        self.play(Create(axes), Write(x_label), Write(y_label))
        for bar in bars:
            self.play(FadeIn(bar, shift=LEFT))
            self.wait(0.5)
        self.wait(2)
        self.fadeOutCurrentScene()
   
         
    def graph_rep_gfd(self):
        self.isRandom=False
        self.angleChoice=[-TAU/4,-TAU/4,TAU/4,TAU/4,TAU/4]
        p1=cvo.CVO().CreateCVO("Graphical Rep. of Grouped Frequency Distribution","").setPosition([0,2.5,0])
        p2=cvo.CVO().CreateCVO("Histogram","").setPosition([-5,1,0])
        p3=cvo.CVO().CreateCVO("Histogram with varying base widths","").setPosition([-4,-2,0])
        p4=cvo.CVO().CreateCVO("Frequency Polygon","").setPosition([0,-2.5,0])
        p5=cvo.CVO().CreateCVO("Frequency Curve","").setPosition([4,-2,0])
        p6=cvo.CVO().CreateCVO("Graph of Cumulative Frequency Distribution","").setPosition([3,0,0])
        p1.cvolist.append(p2)
        p2.cvolist.append(p3)
        p1.cvolist.append(p4)
        p1.cvolist.append(p5)
        p1.cvolist.append(p6)
        self.construct1(p1,p1)
        self.fadeOutCurrentScene()

        text=Text("Histogram",font_size=40)
        text.to_edge(UP)
        self.play(Write(text))
        text1=Text("Graphical representation of grouped frequency distributions of continuous series",font_size=20)
        text1.next_to(text,DOWN,buff=0.3)
        self.play(Write(text1))

        axes = Axes(
                x_range=[0, 10, 1],
                y_range=[0, 10, 1],
                axis_config={"include_tip": True},
                x_axis_config={
                    "numbers_to_include": np.arange(0, 10, 1),
                },
                y_axis_config={
                    "numbers_to_include": np.arange(0, 10, 1),
                },
            ).scale(0.5)
        x_label = axes.get_x_axis_label(Tex("Class Intervals"), edge=DOWN, direction=DOWN, buff=0.5)
        y_label = axes.get_y_axis_label(Tex("Frequency"), edge=LEFT, direction=LEFT, buff=0.5)

        data = np.random.normal(5, 2, 100)
        bins = np.arange(0, 10, 1)
        hist, bin_edges = np.histogram(data, bins=bins)
        max_height = 5
        max_hist_value = max(hist)
        normalized_hist = (hist / max_hist_value) * max_height


        bars = VGroup()
        for i in range(len(hist)):
            bar = Rectangle(
                width=bin_edges[i + 1] - bin_edges[i], 
                height=normalized_hist[i], 
                fill_color=BLUE, 
                fill_opacity=0.7
            ).scale(0.55)
            bar.move_to(axes.c2p(bin_edges[i] + (bin_edges[i + 1] - bin_edges[i]) / 2, 0), aligned_edge=DOWN)
            bars.add(bar)
        self.play(Create(axes,run_time=4), Write(x_label), Write(y_label))

        for bar in bars:
            self.play(FadeIn(bar, shift=DOWN))
            self.wait(0.5)
        self.wait(2)
        self.fadeOutCurrentScene()  

        text=Text("Histogram with varying base widths",font_size=40)
        text.to_edge(UP)
        self.play(Write(text)) 
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            axis_config={"include_tip": True},
            x_axis_config={
                "numbers_to_include": np.arange(0, 10, 1),
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 10, 1),
            },
        ).scale(0.5)
        x_label = axes.get_x_axis_label(Tex("Class Intervals"), edge=DOWN, direction=DOWN, buff=0.5)
        y_label = axes.get_y_axis_label(Tex("Frequency"), edge=LEFT, direction=LEFT, buff=0.5)
        data = np.random.normal(5, 2, 100)  
        bins = [0, 1, 3, 4, 6, 9]  
        hist, bin_edges = np.histogram(data, bins=bins)
        max_height = 5
        max_hist_value = max(hist)
        normalized_hist = (hist / max_hist_value) * max_height
        bars = VGroup()
        for i in range(len(normalized_hist)):
            bar_width = bin_edges[i + 1] - bin_edges[i]
            bar = Rectangle(
                width=bar_width, 
                height=normalized_hist[i], 
                fill_color=BLUE, 
                fill_opacity=0.7
            ).scale(0.58)
            bar.move_to(axes.c2p(bin_edges[i] + bar_width / 2, 0), aligned_edge=DOWN)
            bars.add(bar)
        self.play(Create(axes), Write(x_label), Write(y_label))
        for bar in bars:
            self.play(FadeIn(bar, shift=DOWN))
            self.wait(0.5)

        self.wait(2)
        self.fadeOutCurrentScene()

        text=Text("Frequency Polygon (with histogram)",font_size=40)
        text.to_edge(UP)
        self.play(Write(text)) 
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            axis_config={"include_tip": True},
            x_axis_config={
                "numbers_to_include": np.arange(0, 10, 1),
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 10, 1),
            },
        ).scale(0.5)
        x_label = axes.get_x_axis_label(Tex("Bins"), edge=DOWN, direction=DOWN, buff=0.5)
        y_label = axes.get_y_axis_label(Tex("Frequency"), edge=LEFT, direction=LEFT, buff=0.5)
        data = np.random.normal(5, 2, 100)  
        bins = np.arange(0, 10, 1)  
        hist, bin_edges = np.histogram(data, bins=bins)
        max_height = 5
        max_hist_value = max(hist)
        normalized_hist = (hist / max_hist_value) * max_height

        bars = VGroup()
        for i in range(len(normalized_hist)):
            bar = Rectangle(
                width=bin_edges[i + 1] - bin_edges[i], 
                height=normalized_hist[i], 
                fill_color=BLUE, 
                fill_opacity=0.7
            ).scale(0.58)
            bar.move_to(axes.c2p(bin_edges[i] + (bin_edges[i + 1] - bin_edges[i]) / 2, 0), aligned_edge=DOWN)
            bars.add(bar)
        points = [axes.c2p(bin_edges[0], 0)]  
        for i in range(len(normalized_hist)):
            midpoint = axes.c2p(bin_edges[i] + (bin_edges[i + 1] - bin_edges[i]) / 2, normalized_hist[i])
            points.append(midpoint)
        points.append(axes.c2p(bin_edges[-1], 0))  

        frequency_polygon = VMobject()
        frequency_polygon.set_points_as_corners(points)
        frequency_polygon.set_stroke(color=RED, width=4)

        self.play(Create(axes,run_time=3), Write(x_label), Write(y_label))
        for bar in bars:
            self.play(FadeIn(bar, shift=DOWN))
            self.wait(0.5)
        self.play(Create(frequency_polygon))
        self.wait(2)
        self.fadeOutCurrentScene()

        text=Text("Frequency Polygon (without histogram)",font_size=40)
        text.to_edge(UP)
        self.play(Write(text))
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            axis_config={"include_tip": True},
            x_axis_config={
                "numbers_to_include": np.arange(0, 10, 1),
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 10, 1),
            },
        ).scale(0.5)
        x_label = axes.get_x_axis_label(Tex("Class Intervals"), edge=DOWN, direction=DOWN, buff=0.5)
        y_label = axes.get_y_axis_label(Tex("Frequency"), edge=LEFT, direction=LEFT, buff=0.5)
        data = np.random.normal(5, 2, 100)  
        bins = np.arange(0, 10, 1)  
        hist, bin_edges = np.histogram(data, bins=bins)
        max_height = 5
        max_hist_value = max(hist)
        normalized_hist = (hist / max_hist_value) * max_height
        points = [axes.c2p(bin_edges[0], 0)]  
        for i in range(len(normalized_hist)):
            midpoint = axes.c2p(bin_edges[i] + (bin_edges[i + 1] - bin_edges[i]) / 2, normalized_hist[i])
            points.append(midpoint)
        points.append(axes.c2p(bin_edges[-1], 0)) 

        frequency_polygon = VMobject()
        frequency_polygon.set_points_as_corners(points)
        frequency_polygon.set_stroke(color=RED, width=4)
        self.play(Create(axes,run_time=3), Write(x_label), Write(y_label))
        self.play(Create(frequency_polygon,run_time=4)) 
        self.wait(2)
        self.fadeOutCurrentScene()

        text=Text("Frequency Curve",font_size=40)
        text.to_edge(UP)
        self.play(Write(text))
        axes = Axes(
            x_range=[0, 100, 10],
            y_range=[0, 20, 2],
            axis_config={"include_tip": True},
            x_axis_config={
                "numbers_to_include": np.arange(0, 101, 10),
                "label_direction": DOWN,
                "include_ticks": True,
                "include_numbers": True
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 21, 2),
                "label_direction": LEFT,
                "include_ticks": True,
                "include_numbers": True
            },
            tips=False
        ).scale(0.5)
        x_label = axes.get_x_axis_label(Tex("Ages (in years)"), edge=DOWN, direction=DOWN, buff=0.5)
        y_label = axes.get_y_axis_label(Tex("No. of Patients"), edge=LEFT, direction=LEFT, buff=0.5)
        data_points = [(5, 2), (15, 5), (25, 10), (35, 18), (45, 16), (55, 12), (65, 5), (75, 3), (85, 1), (95, 0)]
        points = [axes.c2p(x, y) for x, y in data_points]
        frequency_curve = VMobject()
        frequency_curve.set_points_as_corners(points)
        frequency_curve.make_smooth()
        self.play(Create(axes,run_time=2), Write(x_label), Write(y_label))
        self.play(Create(frequency_curve,run_time=3))
        dots = VGroup(*[Dot(axes.c2p(x, y), color=RED) for x, y in data_points])
        self.play(Create(dots))
        self.wait(2)
        self.fadeOutCurrentScene()

        text=Text("Graph of Cumulative Frequency Distribution",font_size=40)
        text.to_edge(UP)
        self.play(Write(text))
        axes = Axes(
            x_range=[0, 24, 4],
            y_range=[0, 36, 2],
            axis_config={"include_tip": True},
            x_axis_config={
                "numbers_to_include": np.arange(0, 25, 4),
                "label_direction": DOWN,
                "include_ticks": True,
                "include_numbers": True
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 37, 2),
                "label_direction": LEFT,
                "include_ticks": True,
                "include_numbers": True
            },
            tips=False
        ).scale(0.7)
        x_label = axes.get_x_axis_label(Tex("No.of days"), edge=DOWN, direction=DOWN, buff=0.5)
        y_label = axes.get_y_axis_label(Tex("No. of Tenders"), edge=LEFT, direction=LEFT, buff=0.5)
        y_label.rotate(PI/2)
        data_points = [(0,0),(4,2),(8,7),(12,19),(16,29),(20,32)]
        points = [axes.c2p(x, y) for x, y in data_points]
        frequency_curve = VMobject()
        frequency_curve.set_points_as_corners(points)
        frequency_curve.make_smooth()
        self.play(Create(axes,run_time=2), Write(x_label), Write(y_label))
        self.play(Create(frequency_curve,run_time=3))
        dots = VGroup(*[Dot(axes.c2p(x, y), color=RED) for x, y in data_points])
        self.play(Create(dots))
        self.wait(2)
        self.fadeOutCurrentScene()



    def SetDeveloperList(self):
        self.DeveloperList="Srujan"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade8Chapter7FrequencyDistribution.py"
   
if __name__ == "__main__":
    scene = FrequencyDistributionTandG()
    scene.render()