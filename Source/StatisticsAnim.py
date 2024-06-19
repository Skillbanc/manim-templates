import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class StatisticsAnim(AbstractAnim):

    
    def construct(self):
        
        
        self.RenderSkillbancLogo()
        self.Statistics()
        self.Mean()
        self.Direct()
        self.Direct1()
        self.Assumed()
        self.Assumed1()
        self.Step()
        self.Self2()
        self.Mode()
        self.Mode1()
        self.Mode2()
        self.Median()
        self.Median1()
        self.Median2()
        self.Median3()
        self.Median4()
        
        # self.fadeOut()
        # self.constructDataByJSON()
        # self.fadeOut()
    

    def Statistics(self):
        p10=cvo.CVO().CreateCVO("Statistics", "").setPosition([-4,0,0])
        p11=cvo.CVO().CreateCVO("Mean", "").setPosition([1,2.5,0]).setangle(-TAU/4)
        p12=cvo.CVO().CreateCVO("Median", "").setPosition([2,0,0]).setangle(-TAU/4)
        p13=cvo.CVO().CreateCVO("Mode", "").setPosition([1,-2.5,0]).setangle(-TAU/4)
        
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        
        self.setNumberOfCirclePositions(4)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Mean(self):
        p10=cvo.CVO().CreateCVO("Mean", "").setPosition([-4,0,0])
        p11=cvo.CVO().CreateCVO("Direct Method", "").setPosition([1,2.5,0]).setangle(-TAU/4)
        
        p12=cvo.CVO().CreateCVO("Assumed Mean Method", "").setPosition([1,0,0]).setangle(-TAU/4)
        p13=cvo.CVO().CreateCVO("Step Deviation Method", "").setPosition([1,-2.5,0]).setangle(-TAU/4)

        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        

        self.setNumberOfCirclePositions(5)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
    
   
    def Direct(self):

        title = Text("MEAN : Direct Method", font_size=48, color=BLUE)
        title.to_edge(UP)
        
        mean_formula = MathTex(
            r"\text{Mean } (\bar{x}) = \frac{\sum f_i x_i}{\sum f_i}", 
            font_size=36, color=YELLOW
            )
        mean_formula.next_to(title, DOWN, buff=1)

        

        self.play(Write(title))
        self.wait(1)
        self.play(Write(mean_formula))
        self.wait(1)
        self.fadeOutCurrentScene()

    def Direct1(self):

        title = Text( "Direct Method Example", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        
        xi = [11, 14, 17, 20]
        fi = [3, 6, 8, 7]
       
        # Create a table to display the data
        table = Table(
            [["xi", "fi", "fixi"],
             *[[str(x), str(f), str(f * x)] for x, f in zip(xi, fi)]],
            include_outer_lines=True
        )
        table.scale(0.4)
        table.shift(LEFT,UP)
        self.play(Write(table)) 
        self.wait(2)
        # Display the formula and calculations step by step
        formula_steps = [
            MathTex(r"\text{Mean } (\bar{x}) = \frac{\sum f_i x_i}{\sum f_i}", font_size=36, color=YELLOW).shift(DOWN*1),
            
            MathTex(r"\sum fi = 24, \sum fixi = 393",font_size=30,color=GREEN).shift(DOWN*2),
            MathTex(r"\text{Mean} = \frac{393}{24} = 16.38",font_size=30,color=GREEN).shift(DOWN*3)
        ]

        # Show the steps one by one
        for step in formula_steps:
            self.play(Write(step))
            self.wait(2)

        self.fadeOutCurrentScene()    
             

    def Assumed(self):

        title = Text("MEAN : Assumed Mean Method", font_size=48, color=BLUE)
        title.to_edge(UP)
       
        formula = MathTex(
            r"\text{Mean } (\bar{x}) = a + \frac{\sum f_i d_i}{\sum f_i}", font_size=36, color=YELLOW
        )
        formula.next_to(title, DOWN, buff=0.5)
        
        a_def1 = Tex(r"$a =$ assumed mean",font_size=34)
        a_def1.next_to(formula, DOWN, buff=0.5)
        a_def2 = Tex(r"$d_i = x_i - a =$ deviation of $i$-th class",font_size=34)
        a_def2.next_to(a_def1, DOWN, buff=0.25)
        a_def3 = Tex(r"$x_i =$ class mark $= \frac{\text{upper class limit} + \text{lower class limit}}{2}$",font_size=34)
        a_def3.next_to(a_def2, DOWN, buff=0.25)

        self.play(Write(title))
        self.wait(2)
        self.play(Write(formula))
        self.wait(2)
        self.play(Write(a_def1))
        self.wait(1)
        self.play(Write(a_def2))
        self.wait(1)
        self.play(Write(a_def3))
        self.wait(2)
        self.fadeOutCurrentScene()
    
    def Assumed1(self):
        title = Text("Assumed Mean Method Example", font_size=40, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(2)

        classes = ["0-10", "10-20", "20-30", "30-40", "40-50"]
        frequencies = [12, 28, 32, 25, 13]
        class_marks = [5, 15, 25, 35, 45]
        assumed_mean = 25

        # Calculate deviations and fi*di
        deviations = [xi - assumed_mean for xi in class_marks]
        fi_di = [fi * di for fi, di in zip(frequencies, deviations)]

        # Calculate the total frequency and sum of fi*di
        total_frequency = sum(frequencies)
        sum_fi_di = sum(fi_di)

        # Calculate the mean using the assumed mean method
        mean = assumed_mean + sum_fi_di / total_frequency

        # Create a table to display the data
        table = Table(
            [["Class (CI)", "Frequency (fi)", "Class mark (xi)", "di = xi - a", "fidi"],
             *[[ci, str(fi), str(xi), str(di), str(fidi)] for ci, fi, xi, di, fidi in zip(classes, frequencies, class_marks, deviations, fi_di)]],
            include_outer_lines=True
        )
        table.scale(0.4)
        table.shift(LEFT,UP)
        self.play(Write(table))
        self.wait(2)
       
        # Display the assumed mean formula and calculations step by step
        formula_steps = [
            MathTex(r"\text{Mean} = a + \frac{\sum f_i \cdot d_i}{\sum f_i}",font_size=30,color=YELLOW).shift(RIGHT*5),
            
            MathTex(r"\sum f_i = 110, \sum f_i d_i = -10",font_size=25,color=GREEN).shift(DOWN),
            MathTex(r"\text{Mean} = 25 + \frac{-10}{110}",font_size=25,color=GREEN).shift(DOWN * 2),
            MathTex(r"\text{Mean} = 25 - \frac{1}{11}",font_size=25,color=GREEN).shift(DOWN * 3),
            MathTex(r"\text{Mean} = \frac{275 - 1}{11}",font_size=25,color=GREEN).shift(RIGHT*3,DOWN * 2),
            MathTex(r"\text{Mean} = 24.9",font_size=25,color=GREEN).shift(RIGHT*3,DOWN * 3)
        ] 

        # Show the steps one by one
        for step in formula_steps:
            self.play(Write(step))
            self.wait(2)
        
        self.fadeOutCurrentScene()

    def Step(self):

        title = Text("MEAN : Step - Deviation Method", font_size=48,color=BLUE).to_edge(UP)

        formula = MathTex(
            r"\text{Mean } (\bar{x}) = a + h \left[ \frac{\sum u_i f_i}{\sum f_i} \right]",
            font_size=36,color=YELLOW 
             
        ).next_to(title, DOWN, buff=0.5)

        a_text = MathTex(r"a = \text{assumed mean}", font_size=36).next_to(formula, DOWN, buff=0.5)
        h_text = MathTex(r"h = \text{size of class}", font_size=36).next_to(a_text, DOWN, buff=0.25)
        ui_text = MathTex(r"u_i = \frac{x_i - a}{h}", font_size=36).next_to(h_text, DOWN, buff=0.25)

        self.play(Write(title))
        self.wait(1)
        self.play(Write(formula))
        self.wait(1)
        self.play(Write(a_text))
        self.wait(1)
        self.play(Write(h_text))
        self.wait(1)
        self.play(Write(ui_text))
        self.wait(1)

        self.wait(2)
        self.fadeOutCurrentScene()

    def Self2(self):
        title = Text("Step Deviation Method Example", font_size=38, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(2)

        class_intervals = ["50-70", "70-90", "90-110", "110-130", "130-150", "150-170"]
        fi = [15, 10, 20, 22, 16, 17]
        xi = [60, 80, 100, 120, 140, 160]
        A = 50
        h = 20

        # Calculate ui and fixi
        ui = [(x - A) / h for x in xi]
        fixi = [f * ui_val for f, ui_val in zip(fi, ui)]

        # Calculate the sum of fi and fixi
        sum_fi = sum(fi)
        sum_fixi = sum(fixi)

        # Calculate the step deviation mean
        step_deviation_mean = A + h * (sum_fixi / sum_fi)

        # Create a table to display the data
        table = Table(
            [["Class Interval", "fi", "xi", "ui", "fiui", "fixi",],
             *[[interval, str(f), str(x), str(u), str(f * u), str(f * ui_val)] for interval, f, x, u, ui_val, fixi_val in zip(class_intervals, fi, xi, ui, ui, fixi)]],
            include_outer_lines=True
        )
        table.scale(0.4)
        table.shift(LEFT,UP)
        self.play(Write(table))
        self.wait(2)

        # Display the formula and calculations step by step
        formula_steps = [
            MathTex(r"\text{Step Deviation Mean} = A + h \left( \frac{\sum u_i f_i}{\sum f_i} \right)",font_size=30,color=YELLOW).shift(LEFT*4,DOWN * 1.5),
            
            MathTex(r"A = 50, h = 20, \sum fi = 100",font_size=25,color=GREEN).shift(RIGHT,DOWN * 1.5),
            MathTex(r"\sum u_i f_i = 65, \sum fixi = 1000",font_size=25,color=GREEN).shift(RIGHT,DOWN * 2.5),
            MathTex(r"\text{Step Deviation Mean} = 50 + 20 \left( \frac{65}{100} \right) = 113",font_size=25,color=GREEN).shift(RIGHT,DOWN * 3.5)
        ]

        # Show the steps one by one
        for step in formula_steps:
            self.play(Write(step))
            self.wait(2)
        
        self.fadeOutCurrentScene()

    def Mode(self):
        
        p10=cvo.CVO().CreateCVO("Mode", "").setPosition([-3,0,0])
        p11=cvo.CVO().CreateCVO("Formula", "l + ((f1 - f0) / ((2 * f1) - f0 - f2)) * h\n").setPosition([3,2,0]).setangle(-TAU/4)
        
        p10.cvolist.append(p11)

        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
    
    def Mode1(self):
        title = Text("Mode",font_size=48, color=BLUE).scale(0.7).to_edge(UP)
        self.play(Write(title))

        formula_text = MathTex(r"\begin{array}{l}Mode = l + \left ( \frac{f_{1}-f_{0}}{2f_{1}-f_{0}-f_{2}} \right )\times h\end{array}",font_size=36, color=YELLOW).next_to(title, DOWN)
        self.play(Write(formula_text))

        explanation_text = Text(
            "where,\n\n"
            
            "l = lower boundary of the modal class,\n"
            "h = size of the modal class interval,\n"
            "f1 = frequency of the modal class,\n"
            "f0 = frequency of the class preceding the modal class,\n"
            "f2 = frequency of the class succeeding the modal class"
        ).scale(0.6).next_to(formula_text, DOWN, buff=0.5)
        self.play(Write(explanation_text))

        
        self.wait(4)    
        self.fadeOutCurrentScene()

    def Mode2(self):
        title = Text("Mode Example", font_size=38, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(2)

        class_intervals = ["10-20", "20-30", "30-40", "40-50", "50-60", "60-70"]
        fi = [7, 14, 13, 12, 20, 11]
        
        

    

        # Create a table to display the data
        table = Table(
            [["Class Interval", "fi"],
             *[[interval, str(f), ] for interval, f, in zip(class_intervals, fi,)]],
            include_outer_lines=True
        )
        table.scale(0.4)
        table.shift(LEFT*3,UP)
        self.play(Write(table))
        self.wait(2)

        # Display the formula and calculations step by step
        formula_steps = [
            MathTex( r"\text{Mode} = l + \left(\frac{f_1 - f_0}{2f_1 - f_0 - f_2}\right) \times h",font_size=30,color=YELLOW).shift(LEFT*3,DOWN*2.5),
        ]
        for step in formula_steps:
            self.play(Write(step))
            self.wait(2) 

        title =  MathTex(r"l = 50, h = 10",font_size=30).shift(RIGHT*4,UP)
        self.play(Write(title))
        
        title1 = MathTex(r"f_0 = 12, f_1 = 20, f_2 = 11",font_size=30).next_to( title, DOWN)
        self.play(Write(title1))
       
       
        title2 = MathTex(r"\text{Mode} = 50 + \left(\frac{20 - 12}{2*20 - 12 - 11}\right) \times 10",font_size=30).next_to( title1, DOWN)
        self.play(Write(title2))

        title3 = MathTex(r"= 50 + \left(\frac{8}{40 - 23}\right) \times 10",font_size=30).next_to( title2, DOWN)
        self.play(Write(title3))
            
        title4 = MathTex(r"= 50 + \left(\frac{8}{17}\right) \times 10",font_size=30).next_to( title3, DOWN)
        self.play(Write(title4))
       
        title5 = MathTex(r"= 50 + 4.706",font_size=30).next_to( title4, DOWN)
        self.play(Write(title5))

        title6 = MathTex(r"= 54.706",font_size=30).next_to( title5, DOWN)
        self.play(Write(title6))

        self.wait(3)
        self.fadeOutCurrentScene()

    def Median(self):

        p10=cvo.CVO().CreateCVO("Median", "").setPosition([-4,0,0])
        p11=cvo.CVO().CreateCVO("Formula", "").setPosition([-1.5,0,0]).setangle(-TAU/6)
        p12=cvo.CVO().CreateCVO("n=odd", "M = (n + 1) / 2 th term\n").setPosition([3,2,0]).setangle(-TAU/6)
        p13=cvo.CVO().CreateCVO("n=even", "M = [(n / 2) + 1) th term + (n / 2) th term] / 2\n").setPosition([3,-2,0]).setangle(-TAU/6)
        
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)

        p12.setcircleradius(1.5)
        p13.setcircleradius(1.5)
        

        self.setNumberOfCirclePositions(4)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Median1(self):
        title = Text("Median", font_size=48, color=BLUE).scale(0.7).to_edge(UP)
        self.play(Write(title))

        # Odd case formula
        odd_formula = MathTex(r"\text{If } n \text{ is odd: } M = \frac{n+1}{2}\text{th term}",font_size=36, color=YELLOW).scale(0.6).next_to(title, DOWN, buff=0.8)
        self.play(Write(odd_formula))

        # Even case formula
        even_formula = MathTex(r"\text{If } n \text{ is even: } M = \frac{\left(\frac{n}{2} + 1\right)\text{th term} + \left(\frac{n}{2}\right)\text{th term}}{2}",font_size=36, color=YELLOW).scale(0.6).next_to(odd_formula, DOWN, aligned_edge=LEFT)
        self.play(Write(even_formula))

        # Variables explanation
        variables_text = Text("where, M = Median, n = Number of observations",font_size=36).scale(0.6).next_to(even_formula, DOWN, buff=0.8)
        self.play(Write(variables_text))

        # Hold the final view
        self.wait(3)
        self.fadeOutCurrentScene()

    def Median2(self):
        title = Text("Median",font_size=40,color=BLUE).scale(0.7).to_edge(UP)
        self.play(Write(title))


        title1 = Text("Original set: {42, 40, 50, 60, 35, 58, 32}",font_size=34, color=RED).next_to(title, DOWN*2)
        self.play(Write(title1))

        
        title2 = Text("Ordered Set: {32, 35, 40, 42, 50, 58, 60}",font_size=32).next_to(title1, DOWN)
        self.play(Write(title2))
        self.wait(1)
        
        title3 = Text("n = 7 (odd)",font_size=34, color=GREEN_C).next_to(title2, DOWN*2)
        self.play(Write(title3))

        title4 =  MathTex(r"\text{If } n \text{ is odd: } M = \frac{n+1}{2}\text{th term}",font_size=32).next_to(title3, DOWN*2)
        self.play(Write(title4))
        
        title5 = MathTex(r"\text M = \frac{7+1}{2}\text{th term}",font_size=32).next_to( title4, DOWN)
        self.play(Write(title5))
       
        title6 = MathTex(r"\text M = {4}\text{th term}",font_size=32).next_to( title5, DOWN)
        self.play(Write(title6))

        title7 = MathTex(r"\text Median = 42",font_size=32).next_to( title6, DOWN)
        self.play(Write(title7))

        self.wait(2)
        self.fadeOutCurrentScene()

    def Median3(self):
        title = Text("Median",font_size=40,color=BLUE).scale(0.7).to_edge(UP)
        self.play(Write(title))


        title1 = Text("Original set: {42, 40, 50, 60, 35, 58, 32 ,72}",font_size=34, color=RED).next_to(title, DOWN*2)
        self.play(Write(title1))

        
        title2 = Text("Ordered Set: {32, 35, 40, 42, 50, 58, 60, 72}",font_size=32).next_to(title1, DOWN)
        self.play(Write(title2))
        self.wait(1)
        
        title3 = Text("n = 8 (even)",font_size=34, color=GREEN_C).next_to(title2, DOWN*2)
        self.play(Write(title3))

        title4 =  MathTex(r"\text{If } n \text{ is even: } M = \frac{\left(\frac{n}{2} + 1\right)\text{th term} + \left(\frac{n}{2}\right)\text{th term}}{2}",font_size=32).next_to(title3, DOWN*2)
        self.play(Write(title4))
        
        title5 = MathTex(r"\text M = \frac{\left(\frac{8}{2} + 1\right)\text{th term} + \left(\frac{8}{2}\right)\text{th term}}{2}",font_size=32).next_to( title4, DOWN)
        self.play(Write(title5))
       
        title6 = MathTex(r"M = \frac{\text{5th term} + \text{4th term}}{2}",font_size=32).next_to( title5, DOWN)
        self.play(Write(title6))

        title7 = MathTex(r"\text Median = \frac{50+42}{2}",font_size=32).next_to( title6, RIGHT)
        self.play(Write(title7))

        title8 = MathTex(r"\text Median = \frac{92}{2}",font_size=32).next_to( title6,DOWN)
        self.play(Write(title8))
        
        title9 = MathTex(r"\text Median = 46",font_size=32).next_to( title8, RIGHT)
        self.play(Write(title9))

        self.wait(2)
        self.fadeOutCurrentScene()

    def Median4(self):

        title = Text("Graphical Rrepresentation of Cummulative Frequency Distribution", font_size=30, color=BLUE)
        self.play(Write(title))
        self.fadeOutCurrentScene()

        axes = Axes(
            x_range=[0, 100, 10],
            y_range=[0, 60, 10],
            x_length=7,
            y_length=5,
            axis_config={"color": BLUE},
            x_axis_config={
                "numbers_to_include": np.arange(0, 101, 20),
                "label_direction": DOWN,
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 61, 10),
                "label_direction": LEFT,
            },
        )
        labels = axes.get_axis_labels(x_label="Upper limits", y_label="Cumulative frequency")
        
        # Data points
        data_points = [
            (10, 2), (20, 4), (30, 7), (40, 12), 
            (50, 20), (60, 30), (70, 38), (80, 45), (90, 48), (100, 50)
        ]
        
        # Convert data points to graph coordinates
        graph_points = [axes.coords_to_point(x, y) for x, y in data_points]
        
        # Create dots at each data point
        dots = VGroup(*[Dot(point, color=RED) for point in graph_points])
        
        # Create lines connecting the dots
        lines = VGroup()
        for i in range(len(graph_points) - 1):
            lines.add(Line(graph_points[i], graph_points[i + 1], color=BLUE))
        
        # Median line
        median_value = 66.4
        median_point = axes.coords_to_point(median_value, 30)
        median_line = DashedLine(start=axes.c2p(median_value, 0), end=median_point, color=YELLOW)
        median_text = Text("Median (66.4)").next_to(median_line, RIGHT)
        
        # Create the graph and animate
        self.play(Create(axes), Write(labels))
        self.wait(1)
        self.play(Create(dots))
        self.wait(1)
        self.play(Create(lines))
        self.wait(3)
        self.play(Create(median_line), Write(median_text))
        self.wait(1)
        
        # Animation for the dots and lines
        self.play(*[FadeIn(dot) for dot in dots], run_time=2)
        self.wait(1)
        self.play(Create(lines), run_time=2)
        self.wait()
        self.fadeOutCurrentScene()
        
if __name__ == "__main__":
    scene = StatisticsAnim()
    scene.render()