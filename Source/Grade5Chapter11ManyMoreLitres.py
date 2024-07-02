import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class Litres(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.Litre()
        self.fadeOutCurrentScene()
        self.Example()
        self.fadeOutCurrentScene()
        self.Qustion()
        self.fadeOutCurrentScene()
        self.Qustion2()
        self.fadeOutCurrentScene()
        self.Qustion3()
        self.fadeOutCurrentScene()
        self.Qustion4()
        self.fadeOutCurrentScene()
        self.Qustion5()
        self.fadeOutCurrentScene()
        self.Qustion6()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()        
        


    def Litre(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Litre","1").setPosition([-4,0,0])
        p11=cvo.CVO().CreateCVO("Conversion", "1000 ml").setPosition([3,2,0])
        p12=cvo.CVO().CreateCVO("Written as", "L or l").setPosition([3,-2,0])
      
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
       
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)


    def Example(self):
        text = Text("Example", color=YELLOW).scale(1)
        text.center()
        text.shift(UP * 3)
        self.play(Write(text))
        text2 =Text("Question :Amar wants to paint his home.The details of the\n                     quantity of each paint he bought are given below",color=GREEN).scale(0.65)
        text2.shift(UP *1.5,LEFT )
        self.play(Write(text2))

      
        table_content = [
            ["Color", "Capacity ", "No. of cans", "Cost per litre"],
            ["Yellow", "50 ml", "3", "Rs.400"],
            ["Green", "100 ml", "2", "Rs.500"],
            ["Red", "200 ml", "3", "Rs.500"],
            ["White", "10 L", "4", "Rs.120"],
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
        table_with_lines.shift(DOWN * 2)
        self.add(table_with_lines)

        table = VGroup(*[
            VGroup(*[
                Tex(content, color=BLUE if j == 0 else LIGHT_PINK).move_to(start_position + np.array([i * cell_width, -j * cell_height, 0]))
                for i, content in enumerate(row)
            ])
            for j, row in enumerate(table_content)
        ])
        table.shift(LEFT * 5 + DOWN * 2)
        self.play(Create(table))
        self.wait(0.5)
        
        self.wait(5)
        
        

    def Qustion(self):
        
        text2 =Text("(a).How many litres of paint did Amar buy in all?",color=GREEN).scale(0.8)
        text2.center()
        text2.shift(UP * 2,LEFT)
        self.play(Write(text2))
        text = Text("50ml * 3 = 150ml\n100ml * 2 = 200ml \n200ml * 3 = 600ml\n 10L * 4 = 40L").scale(0.7)
        text.center()
        text.shift(LEFT * 3,UP * 1.5)
        text3 =Text("150ml + 200ml + 600ml + 40L = 40L 950ml").scale(0.7)
        text.center()
        text3.shift(DOWN * 2)
        self.play(Write(text))
        self.play(Write(text3))
        self.wait(3)

    def Qustion2(self):
        
        text2 =Text("(b).How much would one 100 ml can of green paint cost? \n       How much money did Amar spend on green paint?",color=GREEN).scale(0.7)
        text2.center()
        text2.shift(UP * 2,LEFT)
        self.play(Write(text2))
        text = Text("1000 ml = Rs.500 \n100ml = Rs.50 ").scale(0.7)
        text.center()
        text.shift(LEFT * 3,UP * 1.5)
        text3 =Text("For 2 cans : Rs.50 * 2 = Rs.100").scale(0.7)
        text.center()
        text3.shift(DOWN * 2)
        self.play(Write(text))
        self.play(Write(text3))
        self.wait(3)

    def Qustion3(self):
        
        text2 =Text("(c).How much would one 100 ml can of red paint cost? \n       How much money did Amar spend on red paint?",color=GREEN).scale(0.7)
        text2.center()
        text2.shift(UP * 2,LEFT)
        self.play(Write(text2))
        text = Text("1000 ml = Rs.500 \n200ml = Rs.100 ").scale(0.7)
        text.center()
        text.shift(LEFT * 3,UP * 1.5)
        text3 =Text("For 3 cans : Rs.100 * 3 = Rs.300").scale(0.7)
        text.center()
        text3.shift(DOWN * 2)
        self.play(Write(text))
        self.play(Write(text3))
        self.wait(3)
    
    def Qustion4(self):
        
        text2 =Text("(d).How much would one 100 ml can of yellow paint cost? \n       How much money did Amar spend on yellow paint?",color=GREEN).scale(0.7)
        text2.center()
        text2.shift(UP * 2,LEFT)
        self.play(Write(text2))
        text = Text("1000 ml = Rs.400 \n50ml = Rs.20 ").scale(0.7)
        text.center()
        text.shift(LEFT * 3,UP * 1.5)
        text3 =Text("For 3 cans : Rs.20 * 3 = Rs.60").scale(0.7)
        text.center()
        text3.shift(DOWN * 2)
        self.play(Write(text))
        self.play(Write(text3))
        self.wait(3)

    def Qustion5 (self):
        
        text2 =Text("(e).How much would one 100 ml can of white paint cost? \n       How much money did Amar spend on white paint?",color=GREEN).scale(0.7)
        text2.center()
        text2.shift(UP * 2,LEFT)
        self.play(Write(text2))
        text = Text("1 L = Rs.120 \n10 L = Rs.1200 ").scale(0.7)
        text.center()
        text.shift(LEFT * 3,UP * 1.5)
        text3 =Text("For 4 cans : Rs.1200 * 4 = Rs.4800").scale(0.7)
        text.center()
        text3.shift(DOWN * 2)
        self.play(Write(text))
        self.play(Write(text3))
        self.wait(3)

    def Qustion6(self):
        
        text2 =Text("(f). What is the total amount that Amar spent on paint?",color=GREEN).scale(0.7)
        text2.center()
        text2.shift(UP * 2,LEFT)
        self.play(Write(text2))
        text = Text("Rs.60 + Rs.100 + Rs.300 + Rs.4800 = Rs.5260").scale(0.7)
        text.center()
        self.play(Write(text))
        
        self.wait(3)

    def SetDeveloperList(self): 
       self.DeveloperList="Khanak Gupta" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade5Chapter11ManyMoreLitres.py"

if __name__ == "__main__":
    scene = Litres()
    scene.render()

    