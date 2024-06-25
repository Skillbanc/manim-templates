import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo
class Statistics(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()    
        self.statistics()
        self.fadeOutCurrentScene()
        self.centraltendency()
        self.fadeOutCurrentScene()
        self.mean()
        self.MeanFormula()
        self.median()
        self.MedianFormula()
        self.show_odd_median()
        self.mode()
        self.ModeFindingScene()
    def statistics(self):
        self.isRandom = False
        self.positionChoice = [[-5,0,0],[4,2,0],[4,-2,0]]
        a10=cvo.CVO().CreateCVO("Statistics","")
        a11=cvo.CVO().CreateCVO("Primary Data","")
        a12=cvo.CVO().CreateCVO("Secondary Data","")
        a10.cvolist.append(a11)
        a10.cvolist.append(a12)
        self.construct1(a10,a10)
    def centraltendency(self):
        self.isRandom = False
        self.positionChoice = [[-4,0,0],[4,0,0]]
        p10=cvo.CVO().CreateCVO("Central Tendency","")
        p11=cvo.CVO().CreateCVO("3 Appearances","")
        p10.cvolist.append(p11)
        p11onamelist=["mean","median","mode"]
        p11.extendOname(p11onamelist)
        self.construct1(p10,p10)
        p11.setcircleradius(2)
    def mean(self):
        self.isRandom = False    
        p10=cvo.CVO().CreateCVO("Mean","").setPosition([-5,2,0])
        p11=cvo.CVO().CreateCVO("formula","sum of observations/num of observations").setPosition([-5,-2,0])
        self.wait(2)
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p12=cvo.CVO().CreateCVO("Data","20,35,20,50").setPosition([-2,-2,0])
        p121=cvo.CVO().CreateCVO("sum of observations","145").setPosition([1,0,0])
        p122=cvo.CVO().CreateCVO("num of observations","4").setPosition([1,-3,0])
        p12.cvolist.append(p121)
        p12.cvolist.append(p122)
        p1223=cvo.CVO().CreateCVO("mean","145/4=36.5").setPosition([4,2,0])
        self.construct1(p10,p10)
        self.construct1(p12,p12)
        self.play(Create(CurvedArrow(p122.pos,p1223.pos)),Create(CurvedArrow(p121.pos,p1223.pos)))
        self.construct1(p1223,p1223)
        self.fadeOutCurrentScene()
    def MeanFormula(self):
        Observations=[20, 35, 20, 50]
        mean_value = sum(Observations) / len(Observations)
        sample_text = Text("Observations: " + ", ".join(map(str, Observations)))
        sample_text.to_edge(UP)
        self.play(Write(sample_text))
        mean_formula = MathTex(r"\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i").next_to(sample_text, DOWN)
        self.play(Write(mean_formula))
        adding_text=MathTex(r"= \frac{20+35+20+50}{4}")
        self.play(Write(adding_text,run_time=4))
        adding_text1=MathTex(r"= \frac{125}{4}").next_to(adding_text,DOWN)
        self.play(Write(adding_text1,run_time=4))
        mean_value_text = Text("Mean: {:.2f}".format(mean_value)).next_to(adding_text1, DOWN)
        self.play(Write(mean_value_text))
        self.wait(3)
        self.fadeOutCurrentScene()
    def median(self):
        self.isRandom=False
        self.positionChoice = [[0,2.5,0],[-4,0,0],[0,-2,0],[4,0,0],[4,-3,0]]
        p10=cvo.CVO().CreateCVO("Median","")
        p11=cvo.CVO().CreateCVO("Formulas","odd no. of observations, even no. of observations")
        p11.setcircleradius(1.5)
        p1111=cvo.CVO().CreateCVO("odd","(n+1)/2 th term,")
        p1112=cvo.CVO().CreateCVO("even","((N/2)+1^th term + N/2^th term)/2").SetIsMathText(True)
        p1112.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p11.cvolist.append(p1111)
        p11.cvolist.append(p1112)       
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
    def MedianFormula(self):
        title = Text("Median for even number of observations:").to_edge(UP)
        title.add(Underline(title, buff=0.1))

        dataset = [20, 35, 20, 50]
        dataset_text = MathTex(r"\text{Observations: } \{20, 35, 20, 50\}")
        dataset_text.next_to(title, DOWN)
        obs1 = Text("Number of observations (n) = 4").next_to(dataset_text, DOWN, buff=0.5)

        sorted_dataset = sorted(dataset)
        sorted_text = MathTex(r"\text{Sorted in ascending order: }").next_to(obs1, DOWN)
        sorted_elements = VGroup(
            *[MathTex(f"{x}, " if i < len(sorted_dataset) - 1 else f"{x}").set_color(WHITE) for i, x in enumerate(sorted_dataset)]
        ).arrange(RIGHT, buff=0.2).next_to(sorted_text, DOWN)
        sorted_group = VGroup(sorted_text, sorted_elements)
        
        median_index1 = len(sorted_dataset) // 2
        median = (sorted_dataset[median_index1 - 1] + sorted_dataset[median_index1]) / 2
        median_text = MathTex(r"\text{Median} = \frac{\frac{n}{2}^{\text{th term}} + (\frac{n}{2} + 1)^{\text{th term}}}{2}").next_to(sorted_group, DOWN)
        subs = MathTex(r"= \frac{20+35}{2}").next_to(median_text, DOWN)
        median_value = MathTex(f"= {median}").next_to(subs, RIGHT)

        self.play(Write(title))
        self.play(Write(dataset_text))
        self.play(Write(obs1))
        self.wait(1)
        self.play(Write(sorted_group))
        self.play(
            sorted_elements[median_index1 - 1].animate.set_color(YELLOW), 
            sorted_elements[median_index1].animate.set_color(YELLOW)
        )
        self.play(Write(median_text))
        self.play(Write(subs))
        self.play(Write(median_value))
        self.wait(2)
        self.fadeOutCurrentScene()

    def show_odd_median(self):
        title2 = Text("Median for odd number of observations:").to_edge(UP)
        title2.add(Underline(title2, buff=0.1))

        dataset2 = [15, 40, 35, 10, 25]
        dataset_text2 = MathTex(r"\text{Observations: } \{15, 40, 35, 10, 25\}")
        dataset_text2.next_to(title2, DOWN)
        obs2 = Text("Number of observations (n) = 5").next_to(dataset_text2, DOWN, buff=0.5)

        sorted_dataset2 = sorted(dataset2)
        sorted_text2 = MathTex(r"\text{Sorted in ascending order: }").next_to(obs2, DOWN)
        sorted_elements2 = VGroup(
            *[MathTex(f"{x}, " if i < len(sorted_dataset2) - 1 else f"{x}").set_color(WHITE) for i, x in enumerate(sorted_dataset2)]
        ).arrange(RIGHT, buff=0.2).next_to(sorted_text2, DOWN)
        sorted_group2 = VGroup(sorted_text2, sorted_elements2)

        median_index2 = len(sorted_dataset2) // 2
        median2 = sorted_dataset2[median_index2]
        median_text2 = MathTex(r"\text{Median} = \left(\frac{n+1}{2}\right)^{\text{th term}}").next_to(sorted_group2, DOWN)
        median_value2 = MathTex(f"= {median2}").next_to(median_text2, RIGHT)

        self.play(Write(title2))
        self.play(Write(dataset_text2))
        self.play(Write(obs2))
        self.play(Write(sorted_group2))
        self.play(
            sorted_elements2[median_index2].animate.set_color(YELLOW)
        )
        self.play(Write(median_text2))
        self.play(Write(median_value2))
        self.wait(2)
        self.fadeOutCurrentScene()   
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
    def ModeFindingScene(self):
        title = Text("Mode").to_edge(UP)
        dataset = [4, 3, 2, 2, 3, 5, 5, 2, 6, 3, 4]
        dataset_text = Text(f"Example data: {dataset}", font_size=36).next_to(title, DOWN)
        self.play(Write(title))
        self.play(Write(dataset_text))
        self.wait(1)

        mode_value = max(set(dataset), key=dataset.count)
        mode_text = Text(f"Mode = {mode_value}", font_size=36).next_to(dataset_text, DOWN, buff=1.0)

        highlighted_dataset = VGroup()
        for i, value in enumerate(dataset):
            text_value = Text(f"{value}, " if i < len(dataset) - 1 else f"{value}", font_size=36)
            if value == mode_value:
                text_value.set_color(YELLOW)
            highlighted_dataset.add(text_value)
        highlighted_dataset.arrange(RIGHT, buff=0.2).next_to(dataset_text, DOWN)

        self.play(Write(highlighted_dataset))
        self.wait(4)

        self.play(Write(mode_text))
        self.wait(3)
        self.fadeOutCurrentScene()

if __name__ == "__main__":
     scene = Statistics()
     scene.render()