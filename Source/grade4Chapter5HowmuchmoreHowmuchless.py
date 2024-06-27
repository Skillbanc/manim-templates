# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla
import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo

class grade4th(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.constructDataByCVO()
        self.fadeOutCurrentScene()
        #self.constructDataByJSON()
        # self.fadeOut()
        # self.addition()
        # self.fadeOutCurrentScene()
        # self.subtraction()
        # self.fadeOutCurrentScene()
        self.bignoaddition()
        self.fadeOutCurrentScene()
        self.bignosubtraction()
        self.fadeOutCurrentScene()
        # self.table()
        # self.fadeOutCurrentScene
        # self.Question1()
        # self.fadeOutCurrentScene()
        # self.GithubSourceCodeReference()

        # render using CVO data object
    def constructDataByCVO(self):
        p10=cvo.CVO().CreateCVO("grade 4","")
        p11=cvo.CVO().CreateCVO("","how much more -How much less?")

        p10.cvolist.append(p11)
        

        self.setNumberOfCirclePositions(2) 

        self.construct1(p10,p10)

    def addition(self):
        p11=cvo.CVO().CreateCVO("Addition", "of two numbers N1,N2")
        p12=cvo.CVO().CreateCVO("N1+N2", "90+200")
        p13=cvo.CVO().CreateCVO("N1", "90")
        p14=cvo.CVO().CreateCVO("N2", "200")
        p15=cvo.CVO().CreateCVO("result", "290")
       
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
        p11.cvolist.append(p14)
        p11.cvolist.append(p15)
        
        self.setNumberOfCirclePositions(6) 

        self.construct1(p11,p11)


    def subtraction(self):
        p11=cvo.CVO().CreateCVO("Subtraction", "of two numbers N1,N2")
        p12=cvo.CVO().CreateCVO("N1-N2", "300-200")
        p13=cvo.CVO().CreateCVO("N1", "300")
        p14=cvo.CVO().CreateCVO("N2", "200")
        p15=cvo.CVO().CreateCVO("result", "100")
       
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
        p11.cvolist.append(p14)
        p11.cvolist.append(p15)
      

        self.setNumberOfCirclePositions(5) 

        self.construct1(p11,p11)

    def bignoaddition(self):
        p30=cvo.CVO().CreateCVO("Addition", "of bigger numbers N1,N2")
        p31=cvo.CVO().CreateCVO("N1+N2", "332+255")
        p32=cvo.CVO().CreateCVO("Result", "587")
        p33=cvo.CVO().CreateCVO("Hundreds", "500")
        p34=cvo.CVO().CreateCVO("tens", "80")
        p35=cvo.CVO().CreateCVO("ones", "7")
       
        p30.cvolist.append(p31)
        p30.cvolist.append(p32)
        p30.cvolist.append(p33)
        p30.cvolist.append(p34)
        p30.cvolist.append(p35)
      

        self.setNumberOfCirclePositions(6) 

        self.construct1(p30,p30)

    def bignosubtraction(self):
        p40=cvo.CVO().CreateCVO("Subtraction", "of bigger numbers N1,N2")
        p41=cvo.CVO().CreateCVO("N1-N2", "333-222")
        p42=cvo.CVO().CreateCVO("Result", "111")
        p43=cvo.CVO().CreateCVO("Hundreds", "100")
        p44=cvo.CVO().CreateCVO("tens", "10")
        p45=cvo.CVO().CreateCVO("ones", "1")
       
        p40.cvolist.append(p41)
        p40.cvolist.append(p42)
        p40.cvolist.append(p43)
        p40.cvolist.append(p44)
        p40.cvolist.append(p45)

        self.setNumberOfCirclePositions(6) 

        self.construct1(p40,p40)
        self.fadeOutCurrentScene()
   
    def table(self):
        text = Text("London Olympics Medal Winners - 2012").scale(0.8)
        text.center()
        text.shift(UP * 3)
        self.play(Write(text))

      
        table_content = [
            ["country", "gold", "silver", "bronze", "total"],
            ["america", "20", "30", "40", "90"],
            ["china", "10", "20", "30", "60"],
            ["Italy", "50", "30", "10", "90"],
            ["Korea", "13", "8", "12", "33"],
            ["Russia", "40", "30", "20", "90"],
            ["Korea", "33", "22", "11", "66"]
        ]
        cell_height = 0.8
        cell_width = 2
      
        start_position = ORIGIN + UP * (len(table_content) * cell_height / 2)

        table = VGroup(*[
            VGroup(*[
                Tex(content).move_to(start_position + np.array([i * cell_width, -j * cell_height, 0]))
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

        self.wait(5)
        self.fadeOutCurrentScene()

        
    def Question1(self):
        
        text2 =Text("(d).  How many medals did America got more than Italy?",color=GREEN).scale(0.7)
        text2.center()
        text2.shift(UP * 2,LEFT)
        self.play(Write(text2))
        text2a =Text("Ans. 104-90=14",color=PURPLE).scale(0.7)
        text2a.center()
        text2a.shift(UP ,LEFT * 5)
        self.play(Write(text2a))

        text = Text("(e).  How many medals did Korea get less than Russia?", color=GREEN).scale(0.7)
        text.center()
        text.shift(LEFT)
        texta = Text("Ans.90-66=24 less medals", color=PURPLE).scale(0.7)
        texta.center()
        texta.shift(DOWN, LEFT * 4)
     
        text3 =Text("(f). How many more medals does China need to get an equal number of medals as that of America?", color=GREEN).scale(0.7)
        text3.shift(DOWN * 2)
        text3.shift(LEFT)
        text3a =Text("Ans. 30 more medals are required", color=PURPLE).scale(0.7)
        text3a.shift(DOWN * 3,LEFT * 4)
        self.play(Write(text))
        self.play(Write(texta))
        self.play(Write(text3))
        self.play(Write(text3a))
        self.wait(7)











    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="How much more-How much less.py"


    def SetDeveloperList(self):  
        self.DeveloperList="Habeeb Unissa"

if __name__ == "__main__":
    scene = grade4th()
    scene.render()