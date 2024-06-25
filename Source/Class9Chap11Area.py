import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class Areas(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.constructDataByCVO()   
        self.fadeOutCurrentScene()
        self.Properties()
        self.fadeOutCurrentScene()
        self.Theorem1()
        self.fadeOutCurrentScene()
        self.Theorem2()
        self.fadeOutCurrentScene() 
        self.Area1()
        self.fadeOutCurrentScene()
        self.Area2()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
    
    def constructDataByCVO(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Areas","")
        p11=cvo.CVO().CreateCVO("Defination","Measure or magnitude of planer region")
        self.setNumberOfCirclePositions(2)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def Properties(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("General Properties","")
        p11=cvo.CVO().CreateCVO("Property 1", "Two congruent figures have equal areas.")
        p12=cvo.CVO().CreateCVO("Property 2", "If X is formed by two planer regions of figures P and Q, \nthen ar(X)  = ar(P) + ar(Q)").setPosition([-3,2,0])
        p13=cvo.CVO().CreateCVO("Property 3", "Median of Triangle divides it into two equal parts").setPosition([4,2,0])  
        p14=cvo.CVO().CreateCVO("Property 4", "Diagonal of parallelogram divides it into two equal parts").setPosition([1,-1,0])     
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)        
        p11.setcircleradius(1.5)
        p12.setcircleradius(1.5)
        p13.setcircleradius(1.5)
        p14.setcircleradius(1.5)
        self.setNumberOfCirclePositions(4)
        self.construct1(p10,p10)

    def Theorem1(self):
        self.isRandom = False
       
        A = [-2, -1, 0]
        B = [2, -1, 0]
        C = [3, 1, 0]
        D = [-1, 1, 0]
        P = [-3,1,0]
        Q = [1,1,0]

        parallelogram = Polygon(A, B, C, D, color=WHITE)
        parallelogram2 = Polygon(A,P,Q,B)
        label_A = Text("A").next_to(A, DOWN)
        label_B = Text("B").next_to(B, DOWN)
        label_C = Text("C").next_to(C, UP)
        label_D = Text("D").next_to(D, UP)
        label_P = Text("P",color=BLUE).next_to(P, UP)
        label_Q = Text("Q",color=BLUE).next_to(Q, UP)
        
        self.play(Create(parallelogram),Create(parallelogram2),Write(label_A), Write(label_B), Write(label_C), Write(label_D))
        self.play(Create(label_P),Create(label_Q))
                
        parallelogram.shift(4 * RIGHT)
        parallelogram2.shift(4 * RIGHT)
        label_A.shift(4 * RIGHT)
        label_B.shift(4 * RIGHT)
        label_C.shift(4 * RIGHT)
        label_D.shift(4 * RIGHT)
        label_P.shift(4 * RIGHT)
        label_Q.shift(4 * RIGHT)
        
        text = Text("Theorem",color=YELLOW)
        text.to_edge(UP) 
        text.shift(LEFT * (text.get_width() / 2))
        text2 = Text("Parallelograms on the \nsame base and between\nthe same parallels are \nequal in area", color=PURPLE)
        text2.next_to(parallelogram,LEFT, buff=0.9)
        text2.align_to(parallelogram, UP)

        self.add(text,text2)
        self.wait(5)

    def Theorem2(self):
        self.isRandom = False
                  
        A = [-2, -1, 0]
        B = [2, -1, 0]
        C = [3, 1, 0]
        D = [-1, 1, 0]

        parallelogram = Polygon(A, B, C, D, color=WHITE)
        label_A = Text("A").next_to(A, DOWN)
        label_B = Text("B").next_to(B, DOWN)
        label_C = Text("C").next_to(C, UP)
        label_D = Text("D").next_to(D, UP)
        diagonal = Line(A, C, color=YELLOW)
        diagonal2 = Line(D, B, color=YELLOW)
        line_BC = Line(A, B)
        D_proj = line_BC.get_projection(D)
        altitude_DP = DashedLine(D, D_proj, color=BLUE)
        label_P = Text("P").next_to(D_proj, DOWN)

        self.play(Create(parallelogram),Write(label_A), Write(label_B), Write(label_C), Write(label_D))
        self.play(Create(diagonal),Create(diagonal2),Create(altitude_DP), Write(label_P))
        
        parallelogram.shift(4 * RIGHT)
        label_A.shift(4 * RIGHT)
        label_B.shift(4 * RIGHT)
        label_C.shift(4 * RIGHT)
        label_D.shift(4 * RIGHT)
        diagonal.shift(4 * RIGHT)
        diagonal2.shift(4 * RIGHT)
        altitude_DP.shift(4 * RIGHT)
        label_P.shift(4 * RIGHT)

        triangle_ABC = Polygon(A, B, C, color=BLUE, fill_opacity=0.5)
        triangle_ADC = Polygon(A, D, B, color=BLUE, fill_opacity=0.5)
        triangle_ADC.shift(4 * RIGHT)
        triangle_ABC.shift(4 * RIGHT)
       
        text = Text("Theorem", color=YELLOW)
        text.to_edge(UP) 
        text.shift(LEFT * (text.get_width() / 2))
        text2 = Text("Two triangles having the \nsame base  and lie between\nthe same parallels have\nequal areas ", color= PURPLE)
        text2.next_to(parallelogram,LEFT, buff=0.5)
        text2.align_to(parallelogram, UP)
        self.add(text,text2)
        self.play(FadeIn(triangle_ABC), FadeIn(triangle_ADC))
        self.wait(5)
 
    def Area1(self):
        self.isRandom = False
       
        p10=cvo.CVO().CreateCVO("Parallelogram","")
        p11=cvo.CVO().CreateCVO("Area", "product of its base and the corresponding altitude.").setPosition([0,0,0])
        p12=cvo.CVO().CreateCVO("Example", "ABCD is parallelogram").setPosition([-4,2,0])
        p13=cvo.CVO().CreateCVO("", "AB is base and DP is altitude").setPosition([2,3,0])
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        
        A = [-2, -1, 0]
        B = [2, -1, 0]
        C = [3, 1, 0]
        D = [-1, 1, 0]

        parallelogram = Polygon(A, B, C, D, color=WHITE)
                
        label_A = Text("A").next_to(A, DOWN)
        label_B = Text("B").next_to(B, DOWN)
        label_C = Text("C").next_to(C, UP)
        label_D = Text("D").next_to(D, UP)
        diagonal = Line(A, C, color=YELLOW)
        diagonal2 = Line(D, B, color=YELLOW)
        line_BC = Line(A, B)
        D_proj = line_BC.get_projection(D)
        altitude_DP = DashedLine(D, D_proj, color=BLUE)
        label_P = Text("P").next_to(D_proj, DOWN)
        self.play(Create(parallelogram),Write(label_A), Write(label_B), Write(label_C), Write(label_D))
        self.play(Create(diagonal),Create(diagonal2),Create(altitude_DP), Write(label_P))
        
        parallelogram.shift(4 * RIGHT)
        label_A.shift(4 * RIGHT)
        label_B.shift(4 * RIGHT)
        label_C.shift(4 * RIGHT)
        label_D.shift(4 * RIGHT)
        diagonal.shift(4 * RIGHT)
        diagonal2.shift(4 * RIGHT)
        altitude_DP.shift(4 * RIGHT)
        label_P.shift(4 * RIGHT)
        
        self.setNumberOfCirclePositions(4)
        self.construct1(p10,p10)


    def Area2(self):
        self.isRandom = False
       
        p10=cvo.CVO().CreateCVO("Triangle", "same base and between the same parallels of parallelogram")
        p11=cvo.CVO().CreateCVO("Area", "half the area of the parallelogram").setPosition([1,2,0])
        p12=cvo.CVO().CreateCVO("Example", "ADB and ACB are triangles on same base").setPosition([1,-2,0])
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)

        A = [-2, -1, 0]
        B = [2, -1, 0]
        C = [3, 1, 0]
        D = [-1, 1, 0]

        parallelogram = Polygon(A, B, C, D, color=WHITE)
        self.play(Create(parallelogram))
        
        label_A = Text("A").next_to(A, DOWN)
        label_B = Text("B").next_to(B, DOWN)
        label_C = Text("C").next_to(C, UP)
        label_D = Text("D").next_to(D, UP)
        self.play(Write(label_A), Write(label_B), Write(label_C), Write(label_D))
        
        diagonal = Line(A, C, color=YELLOW)
        self.play(Create(diagonal))
        diagonal2 = Line(D, B, color=YELLOW)
        self.play(Create(diagonal2))
   
        line_BC = Line(A, B)
        D_proj = line_BC.get_projection(D)
        altitude_DP = DashedLine(D, D_proj, color=BLUE)
        label_P = Text("P").next_to(D_proj, DOWN)
        self.play(Create(altitude_DP), Write(label_P))
       
        triangle_ABC = Polygon(A, B, C, color=BLUE, fill_opacity=0.5)
        triangle_ADC = Polygon(A, D, B, color=BLUE, fill_opacity=0.5)
        triangle_ADC.shift(4 * RIGHT)
        triangle_ABC.shift(4 * RIGHT)

        parallelogram.shift(4 * RIGHT)
        label_A.shift(4 * RIGHT)
        label_B.shift(4 * RIGHT)
        label_C.shift(4 * RIGHT)
        label_D.shift(4 * RIGHT)
        diagonal.shift(4 * RIGHT)
        diagonal2.shift(4 * RIGHT)
        altitude_DP.shift(4 * RIGHT)
        label_P.shift(4 * RIGHT)
        self.play(FadeIn(triangle_ABC), FadeIn(triangle_ADC))
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)
 
    def SetDeveloperList(self): 
       self.DeveloperList="Khanak Gupta" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Areas.py"


if __name__ == "__main__":
    scene = Areas()
    scene.render()