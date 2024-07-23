from manim import *
from AbstractAnim import AbstractAnim

import cvo
import os

class Grade6Chapter8(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.Data_Handling()
        self.introduction()
        self.Recording_of_data()
        self.organising_data()
        self.representation_data()
        self.GithubSourceCodeReference()
        self.SubscribeYoutube()
        self.fadeOutCurrentScene()


    def Data_Handling(self):
        self.angleChoice=[-TAU/4,-TAU/4,TAU/4,TAU/4]
        p1=cvo.CVO().CreateCVO("DATA HANDLING","").setPosition([0,2.5,0])
        p2=cvo.CVO().CreateCVO("Introduction","").setPosition([-4,1,0])
        p3=cvo.CVO().CreateCVO("Recording of Data","").setPosition([-4,-2,0])
        p4=cvo.CVO().CreateCVO("Organisation of Data","").setPosition([4,-2,0])
        p5=cvo.CVO().CreateCVO("Representation of Data","").setPosition([4,1,0])
        p1.cvolist.append(p2)
        p1.cvolist.append(p3)
        p1.cvolist.append(p4)  
        p1.cvolist.append(p5)      
        self.construct1(p1,p1)
        self.fadeOutCurrentScene()

    def introduction(self):
        self.isRandom=False
        text=Text("INTRODUCTION",font_size=40).to_edge(UP)
        self.play(Write(text))
        text1=Text("Data Handling is the process of collecting information and organising it",font_size=30).next_to(text,DOWN,buff=3)
        self.play(Write(text1))
        self.wait(2)
        self.fadeOutCurrentScene()

    def Recording_of_data(self):
        text=Text("Recording of Data",font_size=60).to_corner(UP+LEFT)
        self.play(Write(text))
        text1=Text("An example for recording the data",font_size=30).next_to(text,DOWN,buff=1)
        self.play(Write(text1))
        data = [
            ["Laxmi", "orange"],
            ["Preeti", "guava"],
            ["Radha", "orange"],
            ["Uma", "custard apple"],
            ["Reshma", "guava"],
            ["Mary", "orange"],
            ["Latha", "orange"],
            ["Gouri", "banana"],
            ["Salma", "custard apple"],
            ["Rita", "guava"],
        ]

        
        table = Table(
            data,
            col_labels=[Text("Person"), Text("Like to have")],
            line_config={"stroke_width": 2, "color": WHITE},
            element_to_mobject=Text,
            h_buff=1,
            v_buff=0.5,
            include_outer_lines=True
        ).scale(0.5).shift(RIGHT*3)

        self.play(Create(table,run_time=4))
        self.wait(2)

        text3=Text("Here  orange  came  4  times",font_size=30,color=ORANGE).shift(LEFT*3)
        self.play(Write(text3))
        highlight_color = ORANGE
        # for i in range(1, len(data)):  
        #     if data[i][1].strip().lower() == "orange":
        #         cell = table.get_cell((i+1, 2)) 
        #         cell.set_fill(highlight_color, opacity=0.5)
        text2=Text("'4'  is  called  the  'Frequency'  of  orange",font_size=30,color=ORANGE).next_to(text3,DOWN,buff=1)
        self.play(Write(text2))
        self.wait(2)
        self.fadeOutCurrentScene()

    def organising_data(self):
        p1=cvo.CVO().CreateCVO("Organisation Of Data","").setPosition([-5,2.5,0])
        p2=cvo.CVO().CreateCVO("Tally Marks","").setPosition([-5,0.5,0])
        # p3=cvo.CVO().CreateCVO("Grouped Tally Marks","").setPosition([-5,-1.5,0])
        p1.cvolist.append(p2)
        # p2.cvolist.append(p3)
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
                Tex("Family size"),
                Tex("Tally marks"),
                Tex("Number of families"),
            ],
            include_outer_lines=True
        ).shift(RIGHT*2)
        table.scale(0.5)
        self.play(Create(table,run_time=5))
        self.wait(2)
        self.play(FadeOut(table))

        table_data = [
            ["2", "     ", "6"],
            ["3", "     ", "19"],
            ["4", "     ", "23"],
            ["5", "     ", "5"],
            ["6", "     ", "2"],
        ]
        table = Table(
            table_data,
            col_labels=[
                Tex("Family size"),
                Tex("Tally marks"),
                Tex("Number of families"),
            ],
            include_outer_lines=True
        ).shift(RIGHT*2)
        table.scale(0.6)
        self.play(Create(table,run_time=5))

        tally_6 = Tex('$||||$').shift(RIGHT*0.7,UP*1.1).scale(0.6)
        t2=Tex('$\diagup$').move_to(tally_6).scale(0.6)
        t1=Tex("$|$").next_to(tally_6,RIGHT,buff=0.2).scale(0.6)
        self.add(tally_6,t2,t1)

        tally_19 = Tex('$||||$').next_to(tally_6,DOWN).scale(0.6)
        t12=Tex('$\diagup$').move_to(tally_19).scale(0.6)
        t11=Tex("$||||$").next_to(tally_19,RIGHT,buff=0.2).scale(0.6)
        t123=Tex('$\diagup$').move_to(t11).scale(0.6)
        t113=Tex("$||||$").next_to(t11,RIGHT,buff=0.2).scale(0.6)
        t1234=Tex('$\diagup$').move_to(t113).scale(0.6)
        t1134=Tex("$||||$").next_to(t113,RIGHT,buff=0.2).scale(0.6)
        self.add(tally_19,t12,t11,t123,t113,t1234,t1134)

        tally_23 = Tex('$||||$').next_to(tally_19,DOWN,buff=0.4).scale(0.5)
        t012=Tex('$\diagup$').move_to(tally_23).scale(0.5)
        t011=Tex("$||||$").next_to(tally_23,RIGHT,buff=0.125).scale(0.5)
        t0123=Tex('$\diagup$').move_to(t011).scale(0.5)
        t0113=Tex("$||||$").next_to(t011,RIGHT,buff=0.125).scale(0.5)
        t01234=Tex('$\diagup$').move_to(t0113).scale(0.5)
        t01134=Tex("$||||$").next_to(t0113,RIGHT,buff=0.125).scale(0.5)
        t001234=Tex('$\diagup$').move_to(t01134).scale(0.5)
        t001134=Tex("$|||$").next_to(t01134,RIGHT,buff=0.125).scale(0.5)
        self.add(tally_23,t012,t011,t0123,t0113,t01234,t01134,t001234,t001134)

        tally_5 = Tex('$||||$').next_to(tally_23,DOWN,buff=0.4).scale(0.6)
        t21=Tex('$\diagup$').move_to(tally_5).scale(0.6)
        self.add(tally_5,t21)

        tally_2=Tex('$||$').next_to(tally_5,DOWN,buff=0.4).scale(0.6)
        self.add(tally_2)

        self.wait(3)
    
        self.add(table)
        self.fadeOutCurrentScene()
 
    def representation_data(self):
        text=Text("Representation of Data",font_size=60).to_edge(UP)
        self.play(Write(text))
        text1=Text("Data that has been organised and presented in frequency distribution \n\n tables can also be presented using pictographs and bar graphs",font_size=30).next_to(text,DOWN,buff=2)
        self.play(Write(text1))
        self.wait(4)
        self.fadeOutCurrentScene()
        self.angleChoice=[TAU/4,-TAU/4]
        p1=cvo.CVO().CreateCVO("Representation Of Data","").setPosition([0,2.5,0])
        p2=cvo.CVO().CreateCVO("Pictographs","").setPosition([3,0,0])
        p3=cvo.CVO().CreateCVO("Bar Graphs","").setPosition([-3,0,0])
        p1.cvolist.append(p2)
        p1.cvolist.append(p3)
        self.construct1(p1,p1)
        self.fadeOutCurrentScene()

        text3 = Text("PICTOGRAPH", font_size=60,color=YELLOW).to_edge(UP)
        self.play(Write(text3))
        text2=Text("A pictograph uses pictures or symbols to represent the frequency of the data.",font_size=30).next_to(text3,DOWN,buff=2)
        self.play(Write(text2))
        self.wait(2)
        self.fadeOutCurrentScene()

        text = Text("PICTOGRAPH EXAMPLE", font_size=40,color=BLUE).to_edge(UP)
        self.play(Write(text))
        data = {
            "Apples": 5,
            "Bananas": 3,
            "Cherries": 4,
            "Orange": 2
        }
        start_y = 2
        start_x = -4
        y_spacing = 1.5

        for i, (category, count) in enumerate(data.items()):
            category_text = Text(category).scale(0.8)
            category_text.next_to([start_x, start_y - i * y_spacing, 0], LEFT)
            emoji_text = {
                "Apples": "🍎",
                "Bananas": "🍌",
                "Cherries": "🍒",
                "Orange": "🍊"
            }[category]
            
            emoji_color = {
                "Apples": RED,
                "Bananas": YELLOW,
                "Cherries": PURE_RED,
                "Orange": ORANGE
            }[category]
        
            emojis = VGroup()
            for _ in range(count):
                emoji = Text(emoji_text).scale(1.5).set_color(emoji_color)
                outline = SurroundingRectangle(emoji, color=WHITE, buff=0.1)
                emoji_with_outline = VGroup(emoji, outline)
                emojis.add(emoji_with_outline)
            
            emojis.arrange(RIGHT, buff=0.5)
            emojis.next_to(category_text, RIGHT, buff=1)
        
            self.play(Write(category_text))
            self.play(FadeIn(emojis))
        
        self.wait(2)
        self.fadeOutCurrentScene()
        
        # text=Text("Here the number of fruits of \n each  category  is  represented \n as a PICTOGRAPH",font_size=30).to_edge(RIGHT)
        # self.play(Write(text))
        # self.wait(2)
        # self.fadeOutCurrentScene()

        text10 = Text("BAR GRAPH", font_size=60,color=YELLOW).to_edge(UP)
        self.play(Write(text10))
        text=Text("Bar graphs are used to represent independent observations with frequencies.",font_size=30).next_to(text10,DOWN,buff=2)
        self.play(Write(text))
        self.wait(2)
        self.fadeOutCurrentScene()
        self.angleChoice=[-TAU/4,TAU/4]
        p12=cvo.CVO().CreateCVO("BAR GRAPH","").setPosition([0,2.5,0])
        p13=cvo.CVO().CreateCVO("Vertical Bars","Bars are parallel to y-axis").setPosition([-3,0,0])
        p14=cvo.CVO().CreateCVO("Horizontal Bars","Bars are parallel to x-axis").setPosition([3,0,0])
        p12.cvolist.append(p13)
        p12.cvolist.append(p14)
        self.construct1(p12,p12)
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
        data = [3,6,4,5,2]
        for i, height in enumerate(data):
            bar = Rectangle(
                width=0.8, 
                height=height, 
                fill_color=PURE_GREEN, 
                fill_opacity=0.5
            ).scale(0.5)
            bar.move_to(axes.c2p(i + 1, 0), aligned_edge=DOWN)
            bars.add(bar)
        self.play(Create(axes), Write(x_label), Write(y_label))

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
        data = [5,4,7,3,1]
        for i, width in enumerate(data):
            bar = Rectangle(
                width=width, 
                height=0.7, 
                fill_color=PURE_BLUE, 
                fill_opacity=0.5
            ).scale(0.5)
            bar.move_to(axes.c2p(0, i + 1), aligned_edge=LEFT)
            bars.add(bar)
        self.play(Create(axes), Write(x_label), Write(y_label))
        for bar in bars:
            self.play(FadeIn(bar, shift=LEFT))
            self.wait(0.5)
        self.wait(2)
        self.fadeOutCurrentScene()


    def SetDeveloperList(self):
        self.DeveloperList="Srujan"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade6Chapter8DataHandling.py"



if __name__ == "__main__":
    scene = Grade6Chapter8()
    scene.render()
        
        
        
