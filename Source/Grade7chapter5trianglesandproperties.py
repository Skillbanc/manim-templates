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

class trianglesAnim(AbstractAnim):
     # use the appropriate method based on how the data is stored
    def construct(self):
         self.RenderSkillbancLogo()
         self.constructDataByCVO()
         self.fadeOutCurrentScene() 
        #  self.trianglepqr()
        #  self.fadeOutCurrentScene() 
        #  self.triangles()
        #  self.fadeOutCurrentScene() 
        #  self.type1()
        #  self.fadeOutCurrentScene()
        #  self.type2()
        #  self.fadeOutCurrentScene()
        #  self.type3()
        #  self.fadeOutCurrentScene()
        #  self.triangles111()
        #  self.fadeOutCurrentScene() 
        #  self.type11()
        #  self.fadeOutCurrentScene() 
        #  self.triangles1155()
        #  self.fadeOutCurrentScene()
       
        #  self.triangles1122()
        #  self.fadeOutCurrentScene()
        #  self.triangles1133()
        #  self.fadeOutCurrentScene()
        #  self.triangles1144()
        #  self.fadeOutCurrentScene() 
        #  self.exteriorangle()
        #  self.fadeOutCurrentScene() 
        #  self.GithubSourceCodeReference()


# render using CVO data object
    def constructDataByCVO(self):
        p10=cvo.CVO().CreateCVO("Triangles and its properties","").setangle(-TAU/4)
        p11=cvo.CVO().CreateCVO("Sides","PQ,QR,RP").setangle(-TAU/4)
        p12=cvo.CVO().CreateCVO("Angles","angle Q,angle p,angle R").setangle(-TAU/4)
        p13=cvo.CVO().CreateCVO("Vertices","p,q,r").setangle(-TAU/4)
        
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)

        self.setNumberOfCirclePositions(4)

        self.construct1(p10,p10)
  


    def trianglepqr(self):
        # Define the vertices of the triangle
        P = [1, 2, 0]
        Q = [-2, -1, 0]
        R = [3, -1, 0]
        
        # Create the triangle
        triangle = Polygon(P, Q, R, color=BLUE)
        
        # Label the vertices
        labels = VGroup(
            MathTex("P").next_to(P, UP),
            MathTex("Q").next_to(Q, LEFT),
            MathTex("R").next_to(R, RIGHT)
        )
        
        # Animations
        self.play(Create(triangle))
        self.play(Write(labels))

        self.wait(3)




    def triangles(self):
        p20=cvo.CVO().CreateCVO("triangles","based on sides")
        p21=cvo.CVO().CreateCVO("isoseles","PQ=QR!=RP")
        p22=cvo.CVO().CreateCVO("scalar","PQ!=QR!=RP")
        p23=cvo.CVO().CreateCVO("equilateral","pq=qr=rp")

        p20.cvolist.append(p21)
        p20.cvolist.append(p22)
        p20.cvolist.append(p23)

        self.setNumberOfCirclePositions(4)
       
        self.construct1(p20,p20)

    def type1(self):
        triangle = Polygon([-3, 0, 0], [3, 0, 0], [0, 4, 0], color=BLUE)
        label = Tex("Isosceles Triangle").next_to(triangle, DOWN)

        self.play(Create(triangle), Write(label))
        self.wait(1)

    def type2(self):
   
        triangle = Polygon([-2, 0, 0], [4, 0, 0], [0, 3, 0], color=RED)
        label = Tex("Scalar Triangle").next_to(triangle, DOWN)

        self.play(Create(triangle), Write(label))
        self.wait(1)

    def type3(self):
        triangle = Polygon([-2, 0, 0], [2, 0, 0], [0, 2*np.sqrt(3), 0], color=GREEN)
        label = Tex("Equilateral Triangle").next_to(triangle, DOWN)

        self.play(Create(triangle), Write(label))
        self.wait(1)

    def triangles111(self):
        p24=cvo.CVO().CreateCVO("triangles","based on angles ")
        p25=cvo.CVO().CreateCVO("acute angled triangle","angle ($A= B=C>90$)")
        p26=cvo.CVO().CreateCVO("right angled triangle ","angle(A/B/C=90")
        p27=cvo.CVO().CreateCVO("obtuse angled triangle","angle ($A=B=C<90$)")

        p24.cvolist.append(p25)
        p24.cvolist.append(p26)
        p24.cvolist.append(p27)

        self.setNumberOfCirclePositions(4)

        self.construct1(p24,p24)

    def type11(self):
       
        right_triangle = Polygon(
            ORIGIN, 
            RIGHT*3, 
            UP*4, 
            stroke_color=BLUE, 
            fill_color=BLUE, 
            fill_opacity=0.5
        )
        right_triangle_label = Tex("Right-angled").next_to(right_triangle, DOWN)
       
        obtuse_triangle = Polygon(
            LEFT*3, 
            RIGHT*3, 
            [0, 4, 0], 
            stroke_color=RED, 
            fill_color=RED, 
            fill_opacity=0.5
        )
        obtuse_triangle_label = Tex("Obtuse-angled").next_to(obtuse_triangle, DOWN)
       
        acute_triangle = Polygon(
            LEFT*3, 
            RIGHT*2, 
            UP*2, 
            stroke_color=GREEN, 
            fill_color=GREEN, 
            fill_opacity=0.5
        )
        acute_triangle_label = Tex("Acute-angled").next_to(acute_triangle, DOWN)
      


        self.play(Create(right_triangle), Write(right_triangle_label))
        self.wait(3)
        self.play(FadeOut (right_triangle),FadeOut(right_triangle_label))
        self.play(Create(obtuse_triangle), Write(obtuse_triangle_label))
        self.wait(3)
        self.play(FadeOut (obtuse_triangle),FadeOut(obtuse_triangle_label))
        self.play(Create(acute_triangle), Write(acute_triangle_label))
        self.wait(3)
        self.play(FadeOut (acute_triangle),FadeOut(acute_triangle_label))
       

    def triangles1155(self):
        p50=cvo.CVO().CreateCVO("triangle","median of a triangle")
        p51=cvo.CVO().CreateCVO("A triangle has 3 medians","line segmet joining mid point of the opposite side")
        p52=cvo.CVO().CreateCVO("x","x is the median of side AB")

        p50.cvolist.append(p51)
        p50.cvolist.append(p52)
        
        self.setNumberOfCirclePositions(3)

        self.construct1(p50,p50)


    def triangles1122(self):
        p30=cvo.CVO().CreateCVO("relationship between sides of triangles","a,b,c")
        p31=cvo.CVO().CreateCVO("sum","a+b,b+c,c+a")
        p32=cvo.CVO().CreateCVO("condition","$sum>c,diff<c$")
        p33=cvo.CVO().CreateCVO("difference","a-b,b-c,c-a")

        p30.cvolist.append(p31)
        p30.cvolist.append(p32)
        p30.cvolist.append(p33)

        self.setNumberOfCirclePositions(4)
       
        self.construct1(p30,p30)

    def triangles1133(self):
        p40=cvo.CVO().CreateCVO("angle sum property of a triangle","angle a+b+c=180")
        p41=cvo.CVO().CreateCVO("finding an angle","angle c=?")
        p42=cvo.CVO().CreateCVO("required angle c","angle c=180-(angle a + angle b)")
       
        p40.cvolist.append(p41)
        p40.cvolist.append(p42)
        
        self.setNumberOfCirclePositions(3)
       
        self.construct1(p40,p40)

    def triangles1144(self):
        p50=cvo.CVO().CreateCVO("exterior angle property","sum of interior opposite angles of a triangle")
        p51=cvo.CVO().CreateCVO("In triangle ABC","angle A and B are interior angles")
        p52=cvo.CVO().CreateCVO("In triangle ABC","Angle C is the exterior angle")
        p53=cvo.CVO().CreateCVO("E.A=sum of interior angles","angle C= angle A+ angle B")

        p50.cvolist.append(p51)
        p50.cvolist.append(p52)
        p50.cvolist.append(p53)

        self.setNumberOfCirclePositions(4)

        self.construct1(p50,p50)
   

    def exteriorangle(self):
      
        # Create the triangle
        triangle = Polygon(
            [1, 1, 0],  # A
            [-1, -1, 0],  # B
            [3, -1, 0],  # C
            color=BLUE
        )
        
        # Label the vertices
        labels = VGroup(
            MathTex("A").next_to(triangle.get_vertices()[0], UP),
            MathTex("B").next_to(triangle.get_vertices()[1], DOWN),
            MathTex("C").next_to(triangle.get_vertices()[2], DOWN)
        )
        
        # Extend the line BC to form the exterior angle at C
        extended_line = Line(triangle.get_vertices()[2], triangle.get_vertices()[2] + 4 * (triangle.get_vertices()[2] - triangle.get_vertices()[1]), color=GREEN)
        
        # Calculate angles
        line_BC_angle = Line(triangle.get_vertices()[1], triangle.get_vertices()[2]).get_angle()
        line_CA_angle = Line(triangle.get_vertices()[2], triangle.get_vertices()[0]).get_angle()
        exterior_angle = (PI - abs(line_BC_angle - line_CA_angle))
        
        # Create the exterior angle arc
        exterior_angle_arc = Arc(
            start_angle=line_BC_angle,
            angle=PI - exterior_angle,
            radius=0.5,
            color=RED
        ).shift(triangle.get_vertices()[2])
        
        # Create the interior angle arc
        interior_angle_arc = Arc(
            start_angle=line_CA_angle,
            angle=exterior_angle,
            radius=0.5,
            color=YELLOW
        ).shift(triangle.get_vertices()[2])
        
        # Label the exterior angle
        exterior_angle_label = MathTex(r"\theta_{\text{ext}}").next_to(exterior_angle_arc, RIGHT)
        
        # Label the interior angle
        interior_angle_label = MathTex(r"\theta_{\text{int}}").next_to(interior_angle_arc, UP)
        
        # Animations
        self.play(Create(triangle))
        self.play(Write(labels))
        self.play(Create(extended_line))
        self.play(Create(exterior_angle_arc), Write(exterior_angle_label))
        self.play(Create(interior_angle_arc), Write(interior_angle_label))

        # Indicating the relationship
        relation = MathTex(r"\theta_{\text{ext}} = 180^\circ - \theta_{\text{int}}").to_edge(UP)
        self.play(Write(relation))

        self.wait(3)
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="trianglesandproperties.py"

        
    def SetDeveloperList(self):  
        self.DeveloperList="Habeeb unissa"
        
if __name__ == "__main__":
    scene = trianglesAnim()
    scene.render()