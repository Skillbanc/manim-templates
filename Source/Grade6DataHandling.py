from manim import *
from AbstractAnim import AbstractAnim

import cvo
import os

class DATA_HANDLING(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.Data_Handling()
        self.introduction()
        self.Recording_of_data()
        self.organising_data()
        self.representation_data()
        self.GithubSourceCodeReference()


    def Data_Handling(self):
        text = Text("Data Handling", font_size=60,color=YELLOW,font="Bookman Old Style")
        self.play(Write(text))
        self.play(text.animate.shift(UP * 3))
        
        
        text = Text("1.Introduction", font_size=40,color=BLUE)
        self.play(Write(text))
        self.play(text.animate.shift(UP * 2))
        # self.play(text.animate.shift(LEFT * 4))
        
        text = Text("2.Recording Of Data", font_size=40,color=GREEN)
        self.play(Write(text))
        self.play(text.animate.shift(UP * 1))
        # self.play(text.animate.shift(LEFT * 4))
        
        text = Text("3.Organisation Of Data", font_size=40,color=RED)
        self.play(Write(text))
        self.play(text.animate.shift(UP * 0))
        # self.play(text.animate.shift(LEFT * 4))
        
        text = Text("4.Representation Of Data", font_size=40,color=PURPLE)
        self.play(Write(text))
        self.play(text.animate.shift(DOWN * 1))
        # self.play(text.animate.shift(LEFT * 4))

        self.fadeOutCurrentScene()


    def introduction(self):
        self.isRandom=False
        p1=cvo.CVO().CreateCVO("INTRODUCTION","").setPosition([0,2.5,0])
        self.construct1(p1,p1)
        text=Text("Data Handling is the process of collecting information and organising it",font_size=30)
        self.play(Write(text))
        self.play(text.animate.shift(UP * 0))

        
        self.fadeOutCurrentScene()


    def Recording_of_data(self):
        p1=cvo.CVO().CreateCVO("Recording Of Data","").setPosition([-4,2,0])
        self.construct1(p1,p1)
        text=Text("An example for recording the data",font_size=30)
        self.play(Write(text))
        self.play(text.animate.shift(UP * 3.5))
        data = [
            ["Laxmi", "orange"],
            ["Preeti", "guava"],
            ["Radha", "orange"],
            ["Uma", "custard apple"],
            ["Reshma", "guava"],
            ["Mary", "orange"],
            ["Latha", "orange"],
            ["Gouri", "banana"],
            ["Salma", "custard Apple"],
            ["Rita", "guava"],
        ]

        
        table = Table(
            data,
            col_labels=[Text("Person"), Text("Like to have")],
            line_config={"stroke_width": 1, "color": WHITE},
            element_to_mobject=Text,
            h_buff=1,
            v_buff=0.5,
        ).scale(0.5)

        self.play(Create(table))
        self.play(table.animate.shift(RIGHT * 3))
        self.wait(2)

        # for i, row in enumerate(data[1:], start=1): 
        #     like_to_have = row[1].strip().lower()
        #     if like_to_have == "orange":
        #         self.play(FadeToColor(table.get_rows()[i], color=ORANGE), run_time=1)
        #         self.wait(0.5)

        text=Text("Here  oranges  came  4  times",font_size=30,color=ORANGE)
        self.play(Write(text))
        self.play(text.animate.shift(LEFT * 3))

        text=Text("4  is  called  the  Frequency  of  Orange",font_size=30,color=ORANGE)
        self.play(Write(text))
        self.play(text.animate.shift(LEFT * 3, DOWN * 1))
        self.wait(2)
        self.fadeOutCurrentScene()

    def organising_data(self):
        p1=cvo.CVO().CreateCVO("Organising Of Data","").setPosition([-5,2.5,0])
        p2=cvo.CVO().CreateCVO("Tally Marks","").setPosition([-5,0.5,0])
        p3=cvo.CVO().CreateCVO("Grouped Tally Marks","").setPosition([-5,-1.5,0])
        p1.cvolist.append(p2)
        p2.cvolist.append(p3)
        self.construct1(p1,p1)
        table_data = [
            ["2", "||||||", "6"],
            ["3", "|||||||||||||||||", "19"],
            ["4", "|||||||||||||||||||||||", "23"],
            ["5", "|||||", "5"],
            ["6", "||", "2"],
        ]
        table = Table(
            table_data,
            col_labels=[
                Text("Family size"),
                Text("Tally marks"),
                Text("Number of families"),
            ],
            include_outer_lines=True
        )
        table.scale(0.5)
        self.play(Create(table))
        self.play(table.animate.shift(RIGHT * 2))
        self.wait(2)
        self.play(FadeOut(table))

        table_data = [
            ["2", self.get_tally_marks(6), "6"],
            ["3", self.get_tally_marks(19), "19"],
            ["4", self.get_tally_marks(23), "23"],
            ["5", self.get_tally_marks(5), "5"],
            ["6", self.get_tally_marks(2), "2"],
        ]
        table = Table(
            table_data,
            col_labels=[
                Text("Family size"),
                Text("Tally Marks"),
                Text("Number of families"),
            ],
            include_outer_lines=True
        )
        table.scale(0.5) 
        self.play(Create(table))
        self.play(table.animate.shift(RIGHT * 2))
        self.wait(2)
        self.fadeOutCurrentScene()

    def get_tally_marks(self, number):
        tally_marks = ""
        for i in range(number // 5):
            tally_marks += "||||\\ "
        tally_marks += "|" * (number % 5)
        return tally_marks
    
    
    def representation_data(self):
        text = Text("Representation Of Data", font_size=60,color=YELLOW,font="Bookman Old Style")
        self.play(Write(text))
        self.play(text.animate.shift(UP * 3))
        text=Text("Data that has been organised and presented in frequency distribution \n\n tables can also be presented using pictographs and bar graphs",font_size=30)
        self.play(Write(text))
        self.play(text.animate.shift(UP * 0))
        self.fadeOutCurrentScene()
        p1=cvo.CVO().CreateCVO("Representation Of Data","").setPosition([0,2.5,0])
        p2=cvo.CVO().CreateCVO("Pictographs","").setPosition([3,0,0])
        p3=cvo.CVO().CreateCVO("Bar Graphs","").setPosition([-3,0,0])
        p1.cvolist.append(p2)
        p1.cvolist.append(p3)
        self.construct1(p1,p1)
        self.fadeOutCurrentScene()
        text = Text("PICTOGRAPH", font_size=60,color=YELLOW,font="Bookman Old Style")
        self.play(Write(text))
        self.play(text.animate.shift(UP * 3))
        text=Text("A pictograph uses pictures or symbols to represent the frequency of the data.",font_size=30)
        self.play(Write(text))
        self.play(text.animate.shift(UP * 0))
        self.fadeOutCurrentScene()

        text = Text("PICTOGRAPH EXAMPLE", font_size=40,color=BLUE,font="Bookman Old Style")
        self.play(Write(text))
        self.play(text.animate.shift(UP * 3.5))
        title = Text("Number of books").scale(0.7).to_edge(UP)
        subjects = ["Telugu", "English", "Hindi", "Maths", "Science", "Social"]
        num_books = [4, 3, 4, 6, 5, 4]

        svg_path = os.path.join(os.path.dirname(__file__), "book.svg")

        if not os.path.exists(svg_path):
            raise FileNotFoundError(f"SVG file not found: {svg_path}")
        rows = VGroup()
        for i, (subject, count) in enumerate(zip(subjects, num_books)):
            subject_text = Text(subject).scale(0.7).align_to(title, LEFT)
            books = VGroup(*[SVGMobject(svg_path).scale(0.2) for _ in range(count)])
            books.arrange(RIGHT, buff=0.1)
            row = VGroup(subject_text, books).arrange(RIGHT, buff=1).to_edge(LEFT)
            row.shift(DOWN * (i + 1))
            rows.add(row)
        table = VGroup(title, rows).arrange(DOWN, buff=0.5)
        self.play(FadeIn(table))
        self.wait(2)
        text=Text("Here the number of books of \n each  subject  is  represented \n as a PICTOGRAPH",font_size=20,color=ORANGE)
        self.play(Write(text))
        self.play(text.animate.shift(LEFT * 5))
        self.wait(2)
        self.fadeOutCurrentScene()

        text = Text("BAR GRAPH", font_size=60,color=YELLOW,font="Bookman Old Style")
        self.play(Write(text))
        self.play(text.animate.shift(UP * 3))
        text=Text("Bar graphs are used to represent independent observations with frequencies.",font_size=30)
        self.play(Write(text))
        self.play(text.animate.shift(UP * 0))
        self.fadeOutCurrentScene()
        p12=cvo.CVO().CreateCVO("BAR GRAPH","").setPosition([0,2,0])
        p13=cvo.CVO().CreateCVO("Vertical Bars","Bars are parallel to y-axis").setPosition([-3,0,0])
        p14=cvo.CVO().CreateCVO("Horizontal Bars","Bars are parallel to x-axis").setPosition([3,0,0])
        p12.cvolist.append(p13)
        p12.cvolist.append(p14)
        self.construct1(p12,p12)
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
        text=Text("The length of the bars\n represents the frequency\n of the data items\n\n\n Scale on X axis 1cm=1unit \n Scale on Y axis 1cm=2units",font_size=20,color=WHITE)
        self.play(Write(text))
        self.play(text.animate.shift(LEFT * 5))
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
        self.add(bar_chart, title)
        self.play(Create(bar_chart))
        text=Text(" Scale on X axis 1cm=2units \n Scale on Y axis 1cm=1unit",font_size=20,color=WHITE)
        self.play(Write(text))
        self.play(text.animate.shift(LEFT * 5))
        self.wait(3)
        self.fadeOutCurrentScene()


    def SetDeveloperList(self):
        self.DeveloperList="Srujan"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade6DataHandling.py"



if __name__ == "__main__":
    scene = DATA_HANDLING()
    scene.render()
        
        
        
