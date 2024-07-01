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
       self.Property1()
       self.fadeOutCurrentScene()
       self.Property2()
       self.fadeOutCurrentScene()
       self.Property3()
       self.fadeOutCurrentScene()
       self.Property4()
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
        p12=cvo.CVO().CreateCVO("Units","Square Units")
        p13=cvo.CVO().CreateCVO("Example","$cm^2,m^2,km^2$")
        self.setNumberOfCirclePositions(4)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p12.cvolist.append(p13)
        self.construct1(p10,p10)

    def Property1(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("General Properties","").setPosition([-4,-3,0])
        p11=cvo.CVO().CreateCVO("Property 1", "Two congruent figures have equal areas.").setPosition([-4,2,0])
        p10.cvolist.append(p11)
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        triangle1_vert=[[-1.5, 0, 0],[1.5, 0, 0],[0, 2, 0]]
        triangle2_vert=[[-1.5, 0, 0],[1.5, 0, 0],[0, 2, 0]]

        triangle1 = Polygon(*triangle1_vert, color=BLUE, fill_opacity=0.5)
        triangle2 = Polygon(*triangle2_vert, color=GREEN,  fill_opacity=0.5)
        text= Text("Area of Triangle ABC =Area of Triangle PQR").scale(0.6)
        text.center()
        text.shift(DOWN *3, RIGHT * 2)
        triangle1.shift(LEFT)
        triangle2.shift(RIGHT * 3)
        triangle1.shift(DOWN)
        triangle2.shift(DOWN)
        
        label1_A = Text("A").next_to(triangle1.get_vertices()[0], DOWN)
        label1_B = Text("B").next_to(triangle1.get_vertices()[1], DOWN)
        label1_C = Text("C").next_to(triangle1.get_vertices()[2], UP)

        label2_D = Text("P").next_to(triangle2.get_vertices()[0], DOWN)
        label2_E = Text("Q").next_to(triangle2.get_vertices()[1], DOWN)
        label2_F = Text("R").next_to(triangle2.get_vertices()[2], UP)
        
        self.play(Create(triangle1), Create(triangle2))
        self.play(Write(label1_A), Write(label1_B), Write(label1_C), Write(label2_D), Write(label2_E), Write(label2_F))
        self.play(Write(text))
        self.wait(2)
        self.play(
            triangle1.animate.move_to(triangle2.get_center()),
            FadeOut(label1_A),
            FadeOut(label1_B),
            FadeOut(label1_C),
           )

        self.wait(3)

    def Property2(self):
        self.isRandom = False
        cvo_text = (
            "If X is formed by two planar regions of figures P and Q,    \n"
            "\n then ar(X) = ar(P) + ar(Q)"
        )
        p10=cvo.CVO().CreateCVO("General Properties","").setPosition([-4,-3,0])
        p11=cvo.CVO().CreateCVO("Property 2", cvo_text).setPosition([-4,2,0])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)

        triangle1_vert = [[-1.5, 0, 0], [1.5, 0, 0], [0, 2, 0]]
        triangle1 = Polygon(*triangle1_vert, color=BLUE, fill_opacity=0.5)
        square_side_length = 3
        square = Square(side_length=square_side_length, color=GREEN, fill_opacity=0.5)
        triangle_bottom_y = min([v[1] for v in triangle1_vert])
        square.move_to([0, triangle_bottom_y - square_side_length / 2, 0])
        triangle1.shift(UP,RIGHT * 2)
        square.shift(UP,RIGHT * 2)

        label_A = Text("B").next_to(square.get_vertices()[1], LEFT)
        label_B = Text("C").next_to(square.get_vertices()[2],LEFT)
        label_C = Text("D").next_to(square.get_vertices()[3], RIGHT)
        label1_C = Text("A").next_to(triangle1.get_vertices()[2], UP)
        label_D = Text("E").next_to(triangle1.get_vertices()[1], RIGHT)

        text= Text("Area of ABCDE = Area of Triangle ABE + Area of BCDE").scale(0.6)
        text.center()
        text.shift(DOWN *3, RIGHT * 2)
        self.play(Create(triangle1),Create(square))
        self.play( Write(label1_C),Write(label_A), Write(label_B), Write(label_C), Write(label_D))
        self.play(Write(text))
        self.wait(3)
   
    def Property3(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("General Properties","").setPosition([-4,-3,0])
        p11=cvo.CVO().CreateCVO("Property 3", "Median of Triangle divides it into two equal parts").setPosition([-4,2,0])
        p10.cvolist.append(p11)
        p11.setcircleradius(1.5)
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)

        triangle1_vert=[[-2, 0, 0],[2, 0, 0],[0, 3, 0]]
        triangle1 = Polygon(*triangle1_vert, color=BLUE, fill_opacity=0.5)
        triangle1.shift(RIGHT * 2 )
        label1_A = Text("A").next_to(triangle1.get_vertices()[0], DOWN)
        label1_B = Text("B").next_to(triangle1.get_vertices()[1], DOWN)
        label1_C = Text("C").next_to(triangle1.get_vertices()[2], UP)
        text= Text("Area of Triangle ACP = Area of Triangle CPB").scale(0.6)
        text.center()
        text.shift(DOWN *2, RIGHT *2)

        midpoint_BC = (triangle1.get_vertices()[0] + triangle1.get_vertices()[1]) / 2
        P = Dot(midpoint_BC, color=RED) 
        label_P = Text("P").next_to(P, DOWN)

        median_line = Line(triangle1.get_vertices()[2], midpoint_BC, color=YELLOW)

        self.play(Create(triangle1))
        self.play(Write(label1_A), Write(label1_B), Write(label1_C))
        self.play(Create(median_line))
        self.play(Create(P), Write(label_P))
        self.play(Write(text))
        self.wait(3)

    def Property4(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("General Properties","").setPosition([-4,-3,0])
        p11=cvo.CVO().CreateCVO("Property 4", "Diagonal of parallelogram divides it into two equal parts").setPosition([-4,2,0])
        p10.cvolist.append(p11)
        p11.setcircleradius(1.5)
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)  
        
        A = [-2, -1, 0]
        B = [2, -1, 0]
        C = [3, 1, 0]
        D = [-1, 1, 0]
        
        parallelogram = Polygon(A, B, C, D, color=WHITE,fill_opacity=0.5 )
        parallelogram.shift(UP, RIGHT * 2)
        label1_A = Text("A").next_to(parallelogram.get_vertices()[0], DOWN)
        label1_B = Text("B").next_to(parallelogram.get_vertices()[1], DOWN)
        label1_C = Text("C").next_to(parallelogram.get_vertices()[2], UP)
        label1_D = Text("D").next_to(parallelogram.get_vertices()[3], UP)
                          
        diagonal = Line(A, C, color=YELLOW)
        diagonal.shift(UP, RIGHT * 2)

        text= Text("Area of Triangle ADC = Area of Triangle ABC").scale(0.6) 
        text.center()
        text.shift(DOWN *2, RIGHT *2)
       
        self.play(Create(parallelogram),Write(label1_A), Write(label1_B), Write(label1_C), Write(label1_D))
        self.play(Create(diagonal))
        self.play(Write(text))
        self.wait(3)
   
    def Theorem1(self):
        self.isRandom = False
       
        A = [-2, -1, 0]
        B = [2, -1, 0]
        C = [3, 1, 0]
        D = [-1, 1, 0]
        P = [-3,1,0]
        Q = [1,1,0]

        parallelogram = Polygon(A, B, C, D, color=GREEN,fill_opacity=0.5)
        parallelogram2 = Polygon(A,P,Q,B, color = BLUE, fill_opacity=0.5)
        label_A = Text("A").next_to(A, DOWN)
        label_B = Text("B").next_to(B, DOWN)
        label_C = Text("C").next_to(C, UP)
        label_D = Text("D").next_to(D, UP)
        label_P = Text("P",color=BLUE).next_to(P, UP)
        label_Q = Text("Q",color=BLUE).next_to(Q, UP)
                
        parallelogram.shift(4 * RIGHT)
        parallelogram2.shift(4 * RIGHT)
        label_A.shift(4 * RIGHT)
        label_B.shift(4 * RIGHT)
        label_C.shift(4 * RIGHT)
        label_D.shift(4 * RIGHT)
        label_P.shift(4 * RIGHT)
        label_Q.shift(4 * RIGHT)
        
        text = Text("Theorem",color=YELLOW)
        text.center()
        text.to_edge(UP) 
        text2 = Text("Parallelograms on the same base \nand between the same parallels \nare equal in area", color=PURPLE).scale(0.7)
        text2.center()
        text2.shift(LEFT * 3, UP)
        text3 = Text("Area of ABCD = Area of PQAB", color=PURPLE).scale(0.7)
        text3.center()
        text3.shift(LEFT* 3, DOWN)
        
        self.play(Write(text))
        self.play(Create(parallelogram),Create(parallelogram2),Write(label_A), Write(label_B), Write(label_C), Write(label_D))
        self.play(Create(label_P),Create(label_Q))
        self.play(Write(text2),Write(text3))
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

       
        parallelogram.shift(4 * RIGHT ,UP)
        label_A.shift(4 * RIGHT ,UP)
        label_B.shift(4 * RIGHT ,UP)
        label_C.shift(4 * RIGHT ,UP)
        label_D.shift(4 * RIGHT ,UP)
        diagonal.shift(4 * RIGHT ,UP)
        diagonal2.shift(4 * RIGHT ,UP)
        altitude_DP.shift(4 * RIGHT ,UP)
        label_P.shift(4 * RIGHT ,UP)

        triangle_ABC = Polygon(A, B, C, color=BLUE, fill_opacity=0.5)
        triangle_ADC = Polygon(A, D, B, color=BLUE, fill_opacity=0.5)
        triangle_ADC.shift(4 * RIGHT,UP)
        triangle_ABC.shift(4 * RIGHT,UP)
       
        text = Text("Theorem", color=YELLOW)
        text.center()
        text.to_edge(UP) 
        
        text2 = Text("Two triangles having the same \nbase and lie between the same \nparallels have equal areas ", color= PURPLE).scale(0.8)
        text2.center()
        text2.shift(LEFT * 3 , UP) 
        text3 = Text("Area of Triangle ABD = Area of Triangle ABC", color= PURPLE).scale(0.6)
        text3.center()
        text3.shift(LEFT * 2, DOWN * 2)
        self.play(Write(text))
        self.play(Create(parallelogram),Write(label_A), Write(label_B), Write(label_C), Write(label_D))
        self.play(Create(diagonal),Create(diagonal2),Create(altitude_DP), Write(label_P))
        self.play(FadeIn(triangle_ABC), FadeIn(triangle_ADC))
        self.play(Write(text2),Write(text3))
       
        self.wait(5)
 
    def Area1(self):
        self.isRandom = False
       
        p10=cvo.CVO().CreateCVO("Parallelogram","")
        p11=cvo.CVO().CreateCVO("Area", "base * corresponding altitude.").setPosition([-4,2,0])
        p12=cvo.CVO().CreateCVO("Example", "ABCD is parallelogram").setPosition([0,0,0])
        p13=cvo.CVO().CreateCVO("Area", "AB * DP").setPosition([2,2,0])
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
       
        p10=cvo.CVO().CreateCVO("Triangle", "same base and between the same parallels of parallelogram").setPosition([-3,-2,0])
        p11=cvo.CVO().CreateCVO("Area", "half the area of the parallelogram").setPosition([-4,2,0])
        p12=cvo.CVO().CreateCVO("Example", "ADB and ACB are triangles on same base").setPosition([0,0,0])
        p13=cvo.CVO().CreateCVO("Area", "1/2 * AB * DP").setPosition([2,2,0])
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
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
       self.SourceCodeFileName="Grade9Chapter11Areas.py"


if __name__ == "__main__":
    scene = Areas()
    scene.render()