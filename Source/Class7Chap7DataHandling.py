import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo


class DataHandling(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()  
        # self.observations()  
        self.Organising()
        self.mean()
        self.meanani()
        self.fadeOutCurrentScene()
        self.median()
        self.medani()
        self.fadeOutCurrentScene()
        self.mode()
        self.modani()
        self.fadeOutCurrentScene()
        self.Representation()
        self.bargraph()
        self.fadeOutCurrentScene()
        self.piechart()
        self.fadeOutCurrentScene()
        self.dblgrph()
        self.GithubSourceCodeReference()
        self.fadeOutCurrentScene()
    # render using CVO data object
    def Representation(self):
        self.positionChoice = [[-3,0,0],[3,0,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("DataHandling","")
        p11=cvo.CVO().CreateCVO("representation of data","")
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p11namelist=["Bar Graph","DoubleBar graph","Pie Chart"]
        p11.extendOname(p11namelist)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    # def bargraphs(self):
    #     self.isRandom = False
    #     self.positionChoice=[[-3,2,0],[3,2,0]]
    #     p10=cvo.CVO().CreateCVO("","BarGraph")
    #     p11=cvo.CVO().CreateCVO("co-ordinate axis","")
    #     p11namelist=["x-axis","y-axis"]
    #     p11.extendOname(p11namelist)
    #     p10.cvolist.append(p11)
    #     self.construct1(p10,p10)
    #     self.fadeOutCurrentScene()

    def dblgrph(self):
        self.isRandom = False
        self.positionChoice=[[-3,0,0]]
        p10=cvo.CVO().CreateCVO("doublebargraph","similar as bar graph but has 2 columns attached for each element of y axis")
        p10.setcircleradius(2)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    # def piechart(self):
    #     self.isRandom = False
    #     self.positionChoice=[]
    #     p10=cvo.CVO().CreateCVO("Pie Chart","data represented in form of slices in a pie")
    #     self.setNumberOfCirclePositions(1)
    #     self.construct1(p10,p10)
    #     self.fadeOutCurrentScene()
    
    def observations(self):
        self.isRandom = False
        self.positionChoice=[[-3,0,0],[3,0,0]]
        p10=cvo.CVO().CreateCVO("Observations","")
        p11=cvo.CVO().CreateCVO("definition","The numerical entries in the data ")
        p10.cvolist.append(p11)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Organising(self):
        self.isRandom = False
        self.positionChoice=[[-3,0,0],[-3,0,0]]
        
        p10=cvo.CVO().CreateCVO("Organising Data","")
        p11=cvo.CVO().CreateCVO("3 forms","")
        p10.cvolist.append(p11)
        p11onamelist=["mean","median","mode"]
        p11.extendOname(p11onamelist)

        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
    def mean(self):
        self.isRandom = False
        
        p10=cvo.CVO().CreateCVO("Mean","").setPosition([-5,2,0])
        p11=cvo.CVO().CreateCVO("formula","sum of observations/no. of observations").setPosition([-5,-2,0])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p12=cvo.CVO().CreateCVO("Data","20,35,20,50").setPosition([-2,-2,0])
        p121=cvo.CVO().CreateCVO("sum of observations","145").setPosition([1,0,0])
        p122=cvo.CVO().CreateCVO("no of observations","4").setPosition([1,-3,0])
        p12.cvolist.append(p121)
        p12.cvolist.append(p122)
        p1223=cvo.CVO().CreateCVO("mean","145/4=36.5").setPosition([4,2,0])
        self.construct1(p10,p10)
        self.construct1(p12,p12)
        self.play(Create(CurvedArrow(p122.pos,p1223.pos)),Create(CurvedArrow(p121.pos,p1223.pos)))
        self.construct1(p1223,p1223)
        self.fadeOutCurrentScene()

    def meanani(self):
        n=[20, 35, 20, 50]
        mean_value = sum(n) / len(n)
        title=Text("Mean")
        title.to_edge(UP)
        self.play(Write(title))
        sample_text = Text("Example data: " + ", ".join(map(str, n))).next_to(title, DOWN)
        self.play(Write(sample_text))
        mean_formula = MathTex(r"mean=\frac{sum of observations}{number of observations} ").next_to(sample_text, DOWN)
        self.play(Write(mean_formula,run_time=4))
        adding_text=MathTex(r"= \frac{20+35+20+50}{4}")
        self.play(Write(adding_text,run_time=4))
        mean_value_text = Text("Mean = {:.2f}".format(mean_value)).next_to(adding_text, DOWN)
        self.play(Write(mean_value_text))
        self.wait(3)

    def median(self):
        self.isRandom=False
        self.positionChoice = [[0,2.5,0],[-4,0,0],[0,-2,0],[4,0,0],[4,-3,0]]

        p10=cvo.CVO().CreateCVO("Median","")
        p11=cvo.CVO().CreateCVO("Formulae","odd no. of observations, even no. of observations")
        p11.setcircleradius(1.5)
        p1111=cvo.CVO().CreateCVO("odd","(n+1)/2 th term,")
        p1112=cvo.CVO().CreateCVO("even","((N/2)+1^th term + N/2^th term)/2").SetIsMathText(True)
        p1112.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p11.cvolist.append(p1111)
        p11.cvolist.append(p1112)
        
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
    
    def medani(self):
        title=Text("Median for even number of observations:").to_edge(UP)
        title.add(Underline(title, buff=0.1))
        dataset = [20, 35, 20, 50]
        dataset_text = MathTex(r"\text{observations: } \{20, 35, 20, 50\}")
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
        subs=MathTex(r"=\frac{20+35}{2}=").next_to(subsi,RIGHT)
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
        
        dataset2 = [15, 40, 35, 10, 25]
        dataset_text2 = MathTex(r"\text{observations: } \{15, 40, 35, 10, 25\}")
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
        dataset = [4, 1, 2, 2, 3, 5, 4, 2, 6, 4, 4]
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

    def piechart(self):
        data = [20, 30, 25, 25]
        labels = ["Category A", "Category B", "Category C", "Category D"]
        colors = [RED, GREEN, BLUE, YELLOW]

        # Total sum of data
        total = sum(data)

        # Angles for each segment
        angles = [d / total * 360 for d in data]

        # Create pie chart
        start_angle = 0
        radius = 2
        segments = []

        title = Text("Pie Chart Example", font_size=36).to_edge(UP)
        self.play(Write(title,run_time=4))
        self.wait(2)
        for i, angle in enumerate(angles):
            segment = Sector(
                start_angle=start_angle * DEGREES,
                angle=angle * DEGREES,
                color=colors[i],
                outer_radius=radius,
                inner_radius=0,
                fill_opacity=0.8
            )
            start_angle += angle
            segments.append(segment)
            self.play(Create(segment))

        # Add labels
        for i, segment in enumerate(segments):
            label = Text(labels[i], font_size=24, color=BLACK).move_to(segment.get_center())
            self.play(Write(label))

    def bargraph(self):
        data = [0, 6, 3, 5]
        labels = ["0", "A", "B", "C"]
        colors = [RED, GREEN, BLUE, YELLOW]

        # Create axes
        axes = Axes(
            x_range=[0, len(data), 1],
            y_range=[0, max(data) + 2, 1],
            axis_config={"color": WHITE},
            tips=False,
        ).add_coordinates()

        # Manually add labels for axes
        x_axis_label = Text("x-axis", font_size=16, color=WHITE).next_to(axes.x_axis.get_end(), DOWN)
        y_axis_label = Text("y-axis", font_size=16, color=WHITE).next_to(axes.y_axis.get_end(), LEFT)
        yaxislabel = Text("values", font_size=16, color=WHITE).next_to(axes.y_axis.get_center(), LEFT)
        xaxislabel = Text("categories", font_size=16, color=WHITE).next_to(axes.x_axis.get_center(), DOWN)

        y_axis_label.shift(LEFT*0.25)
        xaxislabel.shift(DOWN*0.1)
        # Create bars and labels
        bars = VGroup()
        bar_labels = VGroup()

        for i, value in enumerate(data):
            bar = Rectangle(
                width=0.8,
                height=value,
                fill_color=colors[i],
                fill_opacity=0.8,
                stroke_width=0
            ).move_to(axes.c2p(i, 0), aligned_edge=DOWN)
            bars.add(bar)

            # Label for each bar
            bar_label = Text(labels[i], font_size=16, color=WHITE).next_to(bar, UP)
            bar_labels.add(bar_label)

        # Add a title
        title = Text("Bar Graph Example", font_size=24).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Display elements
        self.play(Create(axes), Write(x_axis_label), Write(y_axis_label))
        self.play(*[Create(bar) for bar in bars])
        self.play(*[Write(label) for label in bar_labels])
        self.play(Write(xaxislabel),Write(yaxislabel))
        
        self.wait(2)

    def SetDeveloperList(self): 
       self.DeveloperList="T Sai Rohith Reddy" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Class7Chap7DataHandling.py" 

if __name__ == "__main__":
    scene = DataHandling()
    scene.render()