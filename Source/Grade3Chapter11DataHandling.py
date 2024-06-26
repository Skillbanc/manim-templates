import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class DataHandling(AbstractAnim):
    def construct(self):
       self.RenderSkillbancLogo()
       self.Clock()
       self.fadeOutCurrentScene()
       self.Example()
       self.fadeOutCurrentScene()
       self.Qustion()
       self.fadeOutCurrentScene()
       self.Qustion2()
       self.fadeOutCurrentScene()
       self.GithubSourceCodeReference()
             
  
    def Clock(self):
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

        table = VGroup(*[
            VGroup(*[
                Tex(content, color=BLUE).move_to(start_position + np.array([i * cell_width, -j * cell_height, 0]))
                for i, content in enumerate(row)
            ])
            for j, row in enumerate(table_content)
        ])

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

        table_with_lines = VGroup(table, h_lines, v_lines, extra_h_line_top)
        table_with_lines.shift(LEFT * 5)
        table_with_lines.shift(DOWN)
        self.play(Create(table_with_lines))

        self.wait(7)

    def Qustion2(self):
        
        text2 =Text("(d). How many students were absent in class 1?",color=GREEN).scale(0.7)
        text2.center()
        text2.shift(UP * 2,LEFT)
        self.play(Write(text2))
        text2a =Text("Ans. 42",color=PURPLE).scale(0.7)
        text2a.center()
        text2a.shift(UP ,LEFT * 5)
        self.play(Write(text2a))

        text = Text("(e).  How many students are absent in all classes?", color=GREEN).scale(0.7)
        text.center()
        text.shift(LEFT)
        texta = Text("Ans. 19 Students", color=PURPLE).scale(0.7)
        texta.center()
        texta.shift(DOWN, LEFT * 4)
     
        text3 =Text("(f). How many students are present in all classes?", color=GREEN).scale(0.7)
        text3.shift(DOWN * 2)
        text3.shift(LEFT)
        text3a =Text("Ans. 201 Students", color=PURPLE).scale(0.7)
        text3a.shift(DOWN * 3,LEFT * 4)
        self.play(Write(text))
        self.play(Write(texta))
        self.play(Write(text3))
        self.play(Write(text3a))
        self.wait(7)

    def Qustion(self):
        
        text2 =Text("(a). How many students are present in class 4?",color=GREEN).scale(0.7)
        text2.center()
        text2.shift(UP * 2,LEFT)
        self.play(Write(text2))
        text2a =Text("Ans. 7",color=PURPLE).scale(0.7)
        text2a.center()
        text2a.shift(UP ,LEFT * 5)
        self.play(Write(text2a))

        text = Text("   (b). Which class has the highest number of absent students?", color=GREEN).scale(0.7)
        text.center()
        texta = Text("Ans. Class 1 - 7 Students", color=PURPLE).scale(0.7)
        texta.center()
        texta.shift(DOWN, LEFT * 3)
     
        text3 =Text("(c). Which class has the least number of absent students?", color=GREEN).scale(0.7)
        text3.shift(DOWN * 2)
        text3a =Text("Ans. Class 3 - 1 Student", color=PURPLE).scale(0.7)
        text3a.shift(DOWN * 3,LEFT * 3)
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