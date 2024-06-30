import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class Trigonometry(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.Righttriangle()   
        self.fadeOutCurrentScene()
        self.Ratio()
        self.fadeOutCurrentScene()
        self.Ratio2()
        self.fadeOutCurrentScene()
        self.Ratio2A()
        self.fadeOutCurrentScene()
        self.Ratio3()
        self.fadeOutCurrentScene()
        self.Ratio4()
        self.fadeOutCurrentScene()
        self.Proof()
        self.fadeOutCurrentScene()
        self.Identities()
        self.fadeOutCurrentScene()
        self.Proof2()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
               
    def Righttriangle(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Right angled triangle","")
        p11=cvo.CVO().CreateCVO("Hypotenuse", "AB")
        p12=cvo.CVO().CreateCVO(" Opposite side of angle A", "BC")
        p13=cvo.CVO().CreateCVO("Adjacent side of angle A", "AC")
        
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)

        self.wait(1)
        triangle1_vert = [[-2, 0, 0], [2, 0, 0], [-2, 2, 0]] 
        triangle1 = Polygon(*triangle1_vert, color=GRAY)
        
        label1_A = Text("C", color=BLUE).next_to(triangle1.get_vertices()[0], LEFT).scale(0.75)
        label1_B = Text("A", color=BLUE).next_to(triangle1.get_vertices()[1], RIGHT).scale(0.75)
        label1_C = Text("B", color=BLUE).next_to(triangle1.get_vertices()[2], UP).scale(0.75)
        
        right_angle1 = Square(side_length=0.5).move_to(triangle1.get_vertices()[0] + np.array([0.25, 0.25, 0]))
       
        self.play(Create(triangle1))
        self.play(Write(label1_A), Write(label1_B), Write(label1_C))
        self.play(Create(right_angle1))
       
        self.setNumberOfCirclePositions(4)
        self.construct1(p10,p10)

    def Ratio(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Trigonometric Ratios ","").setPosition([-3,-3,0])
        p11=cvo.CVO().CreateCVO("sinA", "").setPosition([-4,2,0])
        p12=cvo.CVO().CreateCVO(" cosA", "").setPosition([-2,2,0])
        p13=cvo.CVO().CreateCVO("tanA", "").setPosition([0,2,0])
        p14=cvo.CVO().CreateCVO("cosecA", "").setPosition([2,2,0])
        p15=cvo.CVO().CreateCVO("secA", "").setPosition([4,2,0])
        p16=cvo.CVO().CreateCVO("cotA", "").setPosition([4,0,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        p10.cvolist.append(p16)
       
        self.setNumberOfCirclePositions(7)
        self.construct1(p10,p10)  

    def Ratio2(self):
        self.isRandom = False
        
        triangle1_vert = [[-2, 0, 0], [2, 0, 0], [-2, 2, 0]] 
        triangle1 = Polygon(*triangle1_vert, color=BLUE)
        
        label1_A = Text("C", color=BLUE).next_to(triangle1.get_vertices()[0], LEFT).scale(0.75)
        label1_B = Text("A", color=BLUE).next_to(triangle1.get_vertices()[1], RIGHT).scale(0.75)
        label1_C = Text("B", color=BLUE).next_to(triangle1.get_vertices()[2], UP).scale(0.75)
        
        right_angle1 = Square(side_length=0.5).move_to(triangle1.get_vertices()[0] + np.array([0.25, 0.25, 0]))
        hypotenuse = Text("Hypotenuse",color=YELLOW).next_to(Line(triangle1.get_vertices()[1], triangle1.get_vertices()[2]).get_center(), RIGHT).scale(0.4)
        side1 = Text("Opposite",color=YELLOW).next_to(Line(triangle1.get_vertices()[0], triangle1.get_vertices()[2]), LEFT).scale(0.4)
        side2 = Text("Adjacent",color=YELLOW).next_to(Line(triangle1.get_vertices()[0], triangle1.get_vertices()[1]).shift(4 * RIGHT), LEFT).scale(0.4)
        side2.shift(0.5 * DOWN)
        side1.shift(RIGHT)
        hypotenuse.shift(0.5 * UP)
        hypotenuse.shift(2 * LEFT)
     
        triangle1.shift(4 * RIGHT)
        label1_A.shift(4 * RIGHT)
        label1_B.shift(4 * RIGHT)
        label1_C.shift(4 * RIGHT)
        right_angle1.shift(4 * RIGHT)
        hypotenuse.shift(4 * RIGHT)
        side1.shift(4 * RIGHT)
        side2.shift(4 * RIGHT)
        self.wait(2)

        title = Text("Trigonometric Ratios").to_edge(UP)
        underline = Underline(title)

        t1 = MathTex(r"\sin A = \frac{\text{Length of Opposite}}{\text{Length of Hypotenuse}}").scale(0.8)
        t2 = MathTex(r"\cos A = \frac{\text{Length of Adjacent}}{\text{Length of Hypotenuse}}").scale(0.8)
        t3 = MathTex(r"\tan A = \frac{\text{Length of Opposite}}{\text{Length of Adjacent}}").scale(0.8)
        t1.next_to(UP).to_edge(LEFT)
        t2.next_to(t1,DOWN, buff=0.5).to_edge(LEFT)
        t3.next_to(t2, DOWN , buff=0.5).to_edge(LEFT)

        self.play(Write(title))
        self.play(Create(underline))
        self.play(Create(triangle1))
        self.play(Write(label1_A), Write(label1_B), Write(label1_C))
        self.play(Create(right_angle1))
        self.play(Write(hypotenuse), Write(side1),Write(side2))
        self.play(Write(t1))
        self.play(Write(t2))
        self.play(Write(t3))
        self.wait(3)

    def Ratio2A(self):
        self.isRandom = False
        
        triangle1_vert = [[-2, 0, 0], [2, 0, 0], [-2, 2, 0]] 
        triangle1 = Polygon(*triangle1_vert, color=BLUE)
        
        label1_A = Text("C", color=BLUE).next_to(triangle1.get_vertices()[0], LEFT).scale(0.75)
        label1_B = Text("A", color=BLUE).next_to(triangle1.get_vertices()[1], RIGHT).scale(0.75)
        label1_C = Text("B", color=BLUE).next_to(triangle1.get_vertices()[2], UP).scale(0.75)
        
        right_angle1 = Square(side_length=0.5).move_to(triangle1.get_vertices()[0] + np.array([0.25, 0.25, 0]))
        hypotenuse = Text("Hypotenuse",color=YELLOW).next_to(Line(triangle1.get_vertices()[1], triangle1.get_vertices()[2]).get_center(), RIGHT).scale(0.4)
        side1 = Text("Opposite",color=YELLOW).next_to(Line(triangle1.get_vertices()[0], triangle1.get_vertices()[2]), LEFT).scale(0.4)
        side2 = Text("Adjacent",color=YELLOW).next_to(Line(triangle1.get_vertices()[0], triangle1.get_vertices()[1]).shift(4 * RIGHT), LEFT).scale(0.4)
        side2.shift(0.5 * DOWN)
        side1.shift(RIGHT)
        hypotenuse.shift(0.5 * UP)
        hypotenuse.shift(2 * LEFT)
     
        triangle1.shift(4 * RIGHT)
        label1_A.shift(4 * RIGHT)
        label1_B.shift(4 * RIGHT)
        label1_C.shift(4 * RIGHT)
        right_angle1.shift(4 * RIGHT)
        hypotenuse.shift(4 * RIGHT)
        side1.shift(4 * RIGHT)
        side2.shift(4 * RIGHT)
        self.wait(2)

        title = Text("Trigonometric Ratios").to_edge(UP)
        underline = Underline(title)

        t1 = MathTex(r"cosec A = \frac{\text{Length of Hypotenuse}}{\text{Length of Opposite}}").scale(0.8)
        t2 = MathTex(r"\sec A = \frac{\text{Length of Hypotenuse}}{\text{Length of Adjacent}}").scale(0.8)
        t3 = MathTex(r"\cot A = \frac{\text{Length of Adjacent}}{\text{Length of Opposite}}").scale(0.8)
        t1.next_to(UP).to_edge(LEFT)
        t2.next_to(t1,DOWN, buff=0.5).to_edge(LEFT)
        t3.next_to(t2, DOWN , buff=0.5).to_edge(LEFT)

        self.play(Write(title))
        self.play(Create(underline))
        self.play(Create(triangle1))
        self.play(Write(label1_A), Write(label1_B), Write(label1_C))
        self.play(Create(right_angle1))
        self.play(Write(hypotenuse), Write(side1),Write(side2))
        self.play(Write(t1))
        self.play(Write(t2))
        self.play(Write(t3))
        self.wait(3)

    def Ratio3(self):
        text = Text("Trigonometric Ratios for specific angles").scale(0.8)
        text.center()
        text.shift(UP * 3)
        self.play(Write(text))

      
        table_content = [
            ["Angle", "0°", "30°", "45°", "60°", "90°"],
            ["sin", "0", r"$\frac{1}{2}$", r"$\frac{\sqrt{2}}{2}$", r"$\frac{\sqrt{3}}{2}$", "1"],
            ["cos", "1", r"$\frac{\sqrt{3}}{2}$", r"$\frac{\sqrt{2}}{2}$", r"$\frac{1}{2}$", "0"],
            ["tan", "0", r"$\frac{\sqrt{3}}{3}$", "1", r"$\sqrt{3}$", r"$\infty$"],
            ["csc", r"$\infty$", "2", r"$\sqrt{2}$", r"$\frac{2}{\sqrt{3}}$", "1"],
            ["sec", "1", r"$\frac{2}{\sqrt{3}}$", r"$\sqrt{2}$", r"$2$", r"$\infty$"],
            ["cot", r"$\infty$", r"$\sqrt{3}$", "1", r"$\frac{1}{\sqrt{3}}$", "0"]
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

    def Ratio4(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Trigonometric Ratios ","").setPosition([4,2,0])
        p17=cvo.CVO().CreateCVO("Complementary Angles", "").setPosition([5,-2,0])
        p11=cvo.CVO().CreateCVO("", "sin(90 - A)= cos A").setPosition([-4,3,0])
        p12=cvo.CVO().CreateCVO("", "cos(90 - A)= sin A").setPosition([-4,1,0])
        p13=cvo.CVO().CreateCVO("", "tan(90 - A)= cot A").setPosition([-4,-1,0])
        p14=cvo.CVO().CreateCVO("", "cot(90 - A)= tan A").setPosition([-4,-3,0])
        p15=cvo.CVO().CreateCVO("", "sec(90 - A)= cosec A").setPosition([-2,-3,0])
        p16=cvo.CVO().CreateCVO("", "cosec(90 - A)= sec A").setPosition([-2,-1,0])
        
        p10.cvolist.append(p17)
        p17.cvolist.append(p11)
        p17.cvolist.append(p12)
        p17.cvolist.append(p13)
        p17.cvolist.append(p14)
        p17.cvolist.append(p15)
        p17.cvolist.append(p16)
        
        self.setNumberOfCirclePositions(7)
        self.construct1(p10,p10)

    def Proof(self):
        self.isRandom = False
        
        triangle1_vert = [[-2, 0, 0], [2, 0, 0], [-2, 2, 0]] 
        triangle1 = Polygon(*triangle1_vert, color=BLUE)
        
        label1_A = Text("C", color=BLUE).next_to(triangle1.get_vertices()[0], LEFT).scale(0.75)
        label1_B = Text("A", color=BLUE).next_to(triangle1.get_vertices()[1], RIGHT).scale(0.75)
        label1_C = Text("B", color=BLUE).next_to(triangle1.get_vertices()[2], UP).scale(0.75)
        
        right_angle1 = Square(side_length=0.5).move_to(triangle1.get_vertices()[0] + np.array([0.25, 0.25, 0]))
        hypotenuse = Text("Hypotenuse",color=YELLOW).next_to(Line(triangle1.get_vertices()[1], triangle1.get_vertices()[2]).get_center(), RIGHT).scale(0.4)
        side1 = Text("Opposite",color=YELLOW).next_to(Line(triangle1.get_vertices()[0], triangle1.get_vertices()[2]), LEFT).scale(0.4)
        side2 = Text("Adjacent",color=YELLOW).next_to(Line(triangle1.get_vertices()[0], triangle1.get_vertices()[1]).shift(4 * RIGHT), LEFT).scale(0.4)
        side2.shift(0.5 * DOWN)
        side1.shift(RIGHT)
        hypotenuse.shift(0.5 * UP)
        hypotenuse.shift(2 * LEFT)
     
        triangle1.shift(4 * RIGHT)
        label1_A.shift(4 * RIGHT)
        label1_B.shift(4 * RIGHT)
        label1_C.shift(4 * RIGHT)
        right_angle1.shift(4 * RIGHT)
        hypotenuse.shift(4 * RIGHT)
        side1.shift(4 * RIGHT)
        side2.shift(4 * RIGHT)
        self.wait(2)

        title = Text("Proof for Complementary Angles",color= GREEN).to_edge(UP).scale(0.9)
        underline = Underline(title)

        t1 = MathTex(r"\text{Since } \angle C = 90^\circ,  \text{the sum of } \\ \text{the other two angles must be } 90^\circ.").scale(0.8)
        t2 = MathTex(r"\angle A + \angle B = 90^\circ \\ \text{ or } \angle B = 90^\circ - \angle A").scale(0.8)
        t3 = MathTex(r"\text{Thus, } \sin(90^\circ - \angle A) = \frac{\text{AC}}{\text{AB}} =\text{cosA}").scale(0.8)


        t1.next_to(UP).to_edge(LEFT)
        t2.next_to(t1,DOWN, buff=0.5).to_edge(LEFT)
        t3.next_to(t2, DOWN , buff=0.5).to_edge(LEFT)

        self.play(Write(title))
        self.play(Create(underline))
        self.play(Create(triangle1))
        self.play(Write(label1_A), Write(label1_B), Write(label1_C))
        self.play(Create(right_angle1))
        self.play(Write(hypotenuse), Write(side1),Write(side2))
        self.play(Write(t1))
        self.play(Write(t2))
        self.play(Write(t3))
        self.wait(3)

    def Identities(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Identities","")
        p11=cvo.CVO().CreateCVO("", "$cos^2A+sin^2A=1$")
        p12=cvo.CVO().CreateCVO("", "$sec^2A-tan^2A=1$")
        p13=cvo.CVO().CreateCVO("", "$cosec^2A-cot^2A=1$")
        
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)

        self.setNumberOfCirclePositions(4)
        self.construct1(p10,p10)    
        
    def Proof2(self):
        self.isRandom = False
        
        triangle1_vert = [[-2, 0, 0], [2, 0, 0], [-2, 2, 0]] 
        triangle1 = Polygon(*triangle1_vert, color=BLUE)
        
        label1_A = Text("B", color=BLUE).next_to(triangle1.get_vertices()[0], LEFT).scale(0.75)
        label1_B = Text("C", color=BLUE).next_to(triangle1.get_vertices()[1], RIGHT).scale(0.75)
        label1_C = Text("A", color=BLUE).next_to(triangle1.get_vertices()[2], UP).scale(0.75)
        
        right_angle1 = Square(side_length=0.5).move_to(triangle1.get_vertices()[0] + np.array([0.25, 0.25, 0]))
        hypotenuse = Text("Hypotenuse",color=YELLOW).next_to(Line(triangle1.get_vertices()[1], triangle1.get_vertices()[2]).get_center(), RIGHT).scale(0.4)
        side1 = Text("Opposite",color=YELLOW).next_to(Line(triangle1.get_vertices()[0], triangle1.get_vertices()[2]), LEFT).scale(0.4)
        side2 = Text("Adjacent",color=YELLOW).next_to(Line(triangle1.get_vertices()[0], triangle1.get_vertices()[1]).shift(4 * RIGHT), LEFT).scale(0.4)
        side2.shift(0.5 * DOWN)
        side1.shift(RIGHT)
        hypotenuse.shift(0.5 * UP)
        hypotenuse.shift(2 * LEFT)
     
        triangle1.shift(4 * RIGHT)
        label1_A.shift(4 * RIGHT)
        label1_B.shift(4 * RIGHT)
        label1_C.shift(4 * RIGHT)
        right_angle1.shift(4 * RIGHT)
        hypotenuse.shift(4 * RIGHT)
        side1.shift(4 * RIGHT)
        side2.shift(4 * RIGHT)
        self.wait(2)

        title = Text("Proof for Identities",color= GREEN).to_edge(UP).scale(0.9)
        underline = Underline(title)

        t1 = MathTex(r"\text{From Pythagoras theorem, } \\ AB^2 + BC^2 = AC^2").scale(0.8)
        t2 = MathTex(r"\text{Dividing each term by } AC^2").scale(0.8)
        t3 = MathTex(r"\frac{\text{AB}^2}{\text{AC}^2} + \frac{\text{BC}^2}{\text{AC}^2} = \frac{\text{AC}^2}{\text{AC}^2}").scale(0.8)
        t4 = MathTex(r"cosA^2 + sinA^2 = 1")
        t1.next_to(UP * 2).to_edge(LEFT)
        t2.next_to(t1,DOWN, buff=0.5).to_edge(LEFT)
        t3.next_to(t2, DOWN , buff=0.5).to_edge(LEFT)
        t4.next_to(t3, DOWN , buff=0.5).to_edge(LEFT)

        self.play(Write(title))
        self.play(Create(underline))
        self.play(Create(triangle1))
        self.play(Write(label1_A), Write(label1_B), Write(label1_C))
        self.play(Create(right_angle1))
        self.play(Write(hypotenuse), Write(side1),Write(side2))
        self.play(Write(t1))
        self.play(Write(t2))
        self.play(Write(t3))
        self.play(Write(t4))
        self.wait(3)

    def SetDeveloperList(self): 
       self.DeveloperList="Khanak Gupta" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade10Chapter11Trigonometry.py"

if __name__ == "__main__":
    scene = Trigonometry()
    scene.render()