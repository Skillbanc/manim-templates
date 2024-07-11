import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class DataHandling(AbstractAnim):
    def construct(self):
       self.RenderSkillbancLogo()
       self.Data()
       self.fadeOutCurrentScene()
       self.Table()
       self.fadeOutCurrentScene()
       self.Q1()
       self.fadeOutCurrentScene()
       self.Example()
       self.fadeOutCurrentScene()
       self.Qustion()
       self.fadeOutCurrentScene()
       self.Qustion2()
       self.fadeOutCurrentScene()
       self.GithubSourceCodeReference()
             
  
    def Data(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Data Handling ","").setPosition([-3,0,0])
        p11=cvo.CVO().CreateCVO("Representation of Data", "").setPosition([3,0,0])
        p10.cvolist.append(p11)
        self.construct1(p10,p10)  

    def Example(self):
        text = Text("Example", color=YELLOW).scale(0.9)
        text.center()
        text.shift(UP * 3)
        self.play(Write(text))

      
        table_content = [
            ["Class", "Total Students", "Present", "Absent"],
            ["Class 1", "32", "25", "7"],
            ["Class 2", "40", "37", "3"],
            ["Class 3", "45", "44", "1"],
            ["Class 4", "48", "42", "6"],
            ["Class 5", "55", "53", "2"],
            ["Total", "220", "201", "19"]
        ]
        cell_height = 0.8
        cell_width = 3.3
      
        start_position = ORIGIN + UP * (len(table_content) * cell_height / 2)

        
        h_lines = VGroup(*[
            Line(
                start=start_position + np.array([-cell_width / 2, -j * cell_height - cell_height / 2, 0]),
                end=start_position + np.array([(len(table_content[0])) * cell_width - cell_width / 2, -j * cell_height - cell_height / 2, 0])
            )
            for j in range(len(table_content) + 1)
        ])

        extra_h_line_top = Line(
            start=start_position + np.array([-cell_width / 2, cell_height / 2, 0]),
            end=start_position + np.array([(len(table_content[0])) * cell_width - cell_width / 2, cell_height / 2, 0])
        )

        v_lines = VGroup(*[
            Line(
                start=start_position + np.array([i * cell_width - cell_width / 2, cell_height / 2, 0]),
                end=start_position + np.array([i * cell_width - cell_width / 2, -(len(table_content)) * cell_height + cell_height / 2, 0])
            )
            for i in range(len(table_content[0]) + 1)
        ])

        table_with_lines = VGroup( h_lines, v_lines, extra_h_line_top)
        table_with_lines.shift(LEFT * 5)
        table_with_lines.shift(DOWN)
        self.add(table_with_lines)

        table = VGroup(*[
            VGroup(*[
                Tex(content, color=BLUE if j == 0 or i == 0 else LIGHT_PINK).move_to(start_position + np.array([i * cell_width, -j * cell_height, 0]))
                for i, content in enumerate(row)
            ])
            for j, row in enumerate(table_content)
        ])
        table.shift(LEFT * 5 + DOWN )
        self.play(Create(table))
        self.wait(1)
        
        self.wait(5)

        self.wait(7)

    def Qustion2(self):
        text = Text("Question and Answers", color=YELLOW).scale(0.9)
        text.center()
        text.shift(UP * 3)
        self.play(Write(text))
        
        text2 =Text("(d). How many students were absent in class 1?",color=BLUE).scale(0.7)
        text2.center()
        text2.shift(UP * 2,LEFT)
        self.play(Write(text2))
        text2a =Text("Ans. 42",color=GREEN).scale(0.7)
        text2a.center()
        text2a.shift(UP ,LEFT * 5)
        self.play(Write(text2a))

        text = Text("(e).  How many students are absent in all classes?", color=BLUE).scale(0.7)
        text.center()
        text.shift(LEFT)
        texta = Text("Ans. 19 Students", color=GREEN).scale(0.7)
        texta.center()
        texta.shift(DOWN, LEFT * 4)
     
        text3 =Text("(f). How many students are present in all classes?", color=BLUE).scale(0.7)
        text3.shift(DOWN * 2)
        text3.shift(LEFT)
        text3a =Text("Ans. 201 Students", color=GREEN).scale(0.7)
        text3a.shift(DOWN * 3,LEFT * 4)
        self.play(Write(text))
        self.play(Write(texta))
        self.play(Write(text3))
        self.play(Write(text3a))
        self.wait(7)

    def Qustion(self):
        text = Text("Question and Answers", color=YELLOW).scale(0.9)
        text.center()
        text.shift(UP * 3)
        self.play(Write(text))
        
        text2 =Text("(a). How many students are present in class 4?",color=BLUE).scale(0.7)
        text2.center()
        text2.shift(UP * 2,LEFT)
        self.play(Write(text2))
        text2a =Text("Ans. 7",color=GREEN).scale(0.7)
        text2a.center()
        text2a.shift(UP ,LEFT * 5)
        self.play(Write(text2a))

        text = Text("   (b). Which class has the highest number of absent students?", color=BLUE).scale(0.7)
        text.center()
        texta = Text("Ans. Class 1 - 7 Students", color=GREEN).scale(0.7)
        texta.center()
        texta.shift(DOWN, LEFT * 3)
     
        text3 =Text("(c). Which class has the least number of absent students?", color=BLUE).scale(0.7)
        text3.shift(DOWN * 2)
        text3a =Text("Ans. Class 3 - 1 Student", color=GREEN).scale(0.7)
        text3a.shift(DOWN * 3,LEFT * 3)
        self.play(Write(text))
        self.play(Write(texta))
        self.play(Write(text3))
        self.play(Write(text3a))
        self.wait(7)

    def Table(self):
        text = Text("Example", color=YELLOW).scale(0.9)
        text.center()
        text.to_edge(UP)
        self.play(Write(text))

        circles = [Circle(radius=0.4, color=BLUE, fill_opacity =0.5) for _ in range(5)]
        squares = [Square(side_length=0.8, color=GREEN,fill_opacity =0.5) for _ in range(3)]
        triangles = [Polygon(
            np.array([0, 0.4, 0]), 
            np.array([-0.4, -0.4, 0]), 
            np.array([0.4, -0.4, 0]),
            color=RED,fill_opacity =0.5
        ) for _ in range(6)]
        stars = [Star(n=5, outer_radius=0.4, color=PURPLE,fill_opacity =0.5) for _ in range(7)]

        circ =VGroup(*circles).arrange_in_grid(cols=5, buff=0.3)
        sq = VGroup(*squares).arrange_in_grid(cols=3, buff=0.3)
        tri = VGroup(*triangles).arrange_in_grid(cols=6, buff=0.3)
        star = VGroup(*stars).arrange_in_grid(cols=7, buff=0.3)
        circ.center()
        circ.shift(UP )
        sq.center()
        sq.shift(DOWN * 0.5)
        tri.center()
        tri.shift(DOWN * 1.7)
        star.center()
        star.shift(DOWN *3)
        circ_title = Text("Circle").scale(0.7)
        sq_title = Text("Square").scale(0.7)
        tri_title = Text("Triangle").scale(0.7)
        star_title = Text("Star").scale(0.7)
        circ_title.center()
        sq_title.center()
        tri_title.center()
        star_title.center()
        circ_title.shift(UP,LEFT * 5.4)
        sq_title.shift(DOWN *0.4,LEFT * 5.4)
        tri_title.shift(DOWN * 1.7,LEFT * 5.4)
        star_title.shift(DOWN * 2.9,LEFT * 5.4)
        title=Text("Shapes").scale(0.7)
        title.center()
        title.shift(UP * 2.1,LEFT * 5.4)
        title2=Text("No. of  Shapes").scale(0.7)
        title2.center()
        title2.shift(UP * 2.1,RIGHT )

        start_point = np.array([0,2.5, 0])
        end_point = np.array([0,-3.7, 0])
        horizontal_line = Line(start=LEFT*7, end=RIGHT*5, color=WHITE, stroke_width=4)
        horizontal_line.shift(UP *1.7)
        h2 = Line(start=LEFT*7, end=RIGHT*5, color=WHITE, stroke_width=4)
        h2.shift(UP *2.5)
        vertical_line = Line(start=start_point, end=end_point, color=WHITE, stroke_width=4)
        vertical_line.shift(LEFT * 4)
        v2 = Line(start=start_point, end=end_point, color=WHITE, stroke_width=4)
        v2.shift(LEFT * 7)
        v3= Line(start=start_point, end=end_point, color=WHITE, stroke_width=4)
        v3.shift(RIGHT * 5)
        h3 = Line(start=LEFT*7, end=RIGHT*5, color=WHITE, stroke_width=4)
        h3.shift(DOWN * 3.7)

        self.play(Create(vertical_line),Create(horizontal_line),Create(h2),Create(v2),Create(v3),Create(h3))
        self.play(Write(title),Write(title2))
        self.play(Write(circ_title),Write(sq_title),Write(tri_title),Write(star_title),)
        self.play(Write(circ))
        self.play(Write(sq))
        self.play(Write(tri))
        self.play(Write(star))

        self.wait(7)

    def Q1(self):
        text = Text("Question and Answers", color=YELLOW).scale(0.9)
        text.center()
        text.shift(UP * 3)
        self.play(Write(text))
        text2 =Text("(a). Which Shape is more in number the following table?",color=BLUE).scale(0.7)
        text2.center()
        text2.shift(UP * 2)
        self.play(Write(text2))
        text2a =Text("Ans. Star - 7",color=GREEN).scale(0.7)
        text2a.center()
        text2a.shift(UP ,LEFT * 4)
        self.play(Write(text2a))

        text = Text("(b).Which Shape is more in number - Circle or Triangle?", color=BLUE).scale(0.7)
        text.center()
        texta = Text("Ans. Triangle - 6", color=GREEN).scale(0.7)
        texta.center()
        texta.shift(DOWN, LEFT * 4)
     
        text3 =Text("(c). Which shape is the least in number?", color=BLUE).scale(0.7)
        text3.shift(DOWN * 2,LEFT * 1.5)
        text3a =Text("Ans. Square - 3", color=GREEN).scale(0.7)
        text3a.shift(DOWN * 3,LEFT * 4)
        self.play(Write(text))
        self.play(Write(texta))
        self.play(Write(text3))
        self.play(Write(text3a))
        self.wait(7)

        

        
    def SetDeveloperList(self): 
       self.DeveloperList="Khanak Gupta" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade3Chapter11DataHandling.py"

if __name__ == "__main__":
    scene = DataHandling()
    scene.render()