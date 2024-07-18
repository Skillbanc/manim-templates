import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class Grade5Chapter16PatternsAnim(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.intro()
        self.fadeOutCurrentScene()
        self.ex1()
        self.fadeOutCurrentScene()
        self.ex3()
        self.fadeOutCurrentScene()
        self.pat()
        self.fadeOutCurrentScene()
        self.pat1()
        self.fadeOutCurrentScene()
        self.pat2()
        self.fadeOutCurrentScene()
        self.ex4()
        self.fadeOutCurrentScene()
        self.ex5()
        self.fadeOutCurrentScene()
        self.topic1()
        self.fadeOutCurrentScene()
        self.topic2()
        self.fadeOutCurrentScene()
        self.topic3()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        


    def SetDeveloperList(self):
        self.DeveloperList = "Lasya Nannapaneni"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName = "Grade5Chapter16PatternsAnim.py"




    def intro(self):
        
        p10=cvo.CVO().CreateCVO("Patterns","").setPosition([-3,2.5,0])
        p15=cvo.CVO().CreateCVO("A pattern is a sequence that repeats.","").setPosition([3,2.5,0])
        p11=cvo.CVO().CreateCVO("Types of Patterns","").setPosition([-3.5,0.5,0])
        p12=cvo.CVO().CreateCVO("Color Patterns","").setPosition([-5,-1.2,0])
        p13=cvo.CVO().CreateCVO("Shape Patterns","").setPosition([-2.5,-2.3,0])
        p14=cvo.CVO().CreateCVO("Number Patterns","").setPosition([0,-2.7,0])

        p10.cvolist.append(p15)
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
        p11.cvolist.append(p14)  
        
        self.construct1(p10,p10)

        self.fadeOutCurrentScene()

        title = Text("Identifying Patterns",font_size=45,color=BLUE).move_to([-3.5,2.3,0])
        u = Underline(title)
        subtil = Text("Look for the part that repeats.\n\n"
                      "That part is called 'core' of the pattern.",font_size=28).move_to([-2.25,1,0])
        self.play(Write(title))
        self.play(Write(u))
        self.play(Write(subtil,run_time=6))
        self.wait()


    def ex1(self):

        t = Triangle(color=BLUE).scale(0.4).move_to([-3,3,0])
        r =  Square(color=BLUE,side_length=0.66).move_to([-3,2.35,0])
        t1 = Triangle(color=BLUE).scale(0.4).move_to([-3,1.7,0]).rotate(PI)
        s1 = Text("In this pattern,", font_size=28).move_to([-5,2.5,0]) 
        s2 = Text("is repeating itself. Hence it is the core.", font_size=26).move_to([0,2.8,0]) 

        t01 = Triangle(color=BLUE).scale(0.4).move_to([-1.5,-2,0]).rotate(PI)
        r1 =  Square(color=BLUE,side_length=0.66).move_to([-1.5,-1.35,0])
        t11 = Triangle(color=BLUE).scale(0.4).move_to([-1.5,-0.7,0])
        t2 = Triangle(color=BLUE).scale(0.4).move_to([-0.8,-0.7,0])
        r2 =  Square(color=BLUE,side_length=0.66).move_to([-0.8,-1.35,0])
        t12 = Triangle(color=BLUE).scale(0.4).move_to([-0.8,-2,0]).rotate(PI)
        t3 = Triangle(color=BLUE).scale(0.4).move_to([-0.1,-0.7,0])
        r3 =  Square(color=BLUE,side_length=0.66).move_to([-0.1,-1.35,0])
        t4 = Triangle(color=BLUE).scale(0.4).move_to([-0.1,-2,0]).rotate(PI)

           

        t21 = Triangle(color=BLUE).scale(0.4).move_to([2,-2,0]).rotate(PI)
        r21 =  Square(color=BLUE,side_length=0.66).move_to([2,-1.35,0])
        t111 = Triangle(color=BLUE).scale(0.4).move_to([2,-0.7,0])
        t22 = Triangle(color=BLUE).scale(0.4).move_to([1.3,-0.7,0])
        r22 =  Square(color=BLUE,side_length=0.66).move_to([1.3,-1.35,0])
        t122 = Triangle(color=BLUE).scale(0.4).move_to([1.3,-2,0]).rotate(PI)
        t32= Triangle(color=BLUE).scale(0.4).move_to([0.6,-0.7,0])
        r32 =  Square(color=BLUE,side_length=0.66).move_to([0.6,-1.35,0])
        t42= Triangle(color=BLUE).scale(0.4).move_to([0.6,-2,0]).rotate(PI)
  
        tg = Text("Pattern - 1",font_size=28).move_to([-1.8,0.8,0])
        self.play(Write(tg))

        self.play(Write(t01))
        self.play(Write(r1))
        self.play(Write(t11))
        self.play(Write(t2))
        self.play(Write(r2))
        self.play(Write(t12))
        self.play(Write(r3))
        self.play(Write(t3))
        self.play(Write(t4))

        self.play(Write(r32))
        self.play(Write(t32))
        self.play(Write(t42))
        self.play(Write(t22))
        self.play(Write(r22))
        self.play(Write(t122))
        self.play(Write(t111))
        self.play(Write(r21))
        self.play(Write(t21))

        self.play(Write(s1))
        self.play(Write(t))
        self.play(Write(r))
        self.play(Write(t1))
        self.play(Write(s2))

    def ex3(self):
     
        s = Square(color=BLUE,side_length=0.66).rotate(angle= 45* DEGREES).move_to([-4,2.35,0])
        t = Triangle(color=BLUE).scale(0.3).move_to([-2,2.2,0])
        t1 = Triangle(color=BLUE).scale(0.3).move_to([-2,2.7,0]).rotate(PI)
        s1 = Text("Here,", font_size=28).move_to([-5,2.5,0])
        s11 = Text("and", font_size=28).move_to([-3,2.5,0])  
        s2 = Text("are repeating alternately.\n Hence they are the core.", font_size=26).move_to([0.5,2.5,0]) 



        s01 = Square(color=BLUE,side_length=0.66).rotate(angle= 45* DEGREES).move_to([-0.5,-0.45,0])
        t01 = Triangle(color=BLUE).scale(0.3).move_to([-0,-0.2,0]).rotate(PI)
        t00 = Triangle(color=BLUE).scale(0.3).move_to([-0,-0.7,0])
        s10 = Square(color=BLUE,side_length=0.66).rotate(angle= 45* DEGREES).move_to([0.5,-0.45,0])
        t11 = Triangle(color=BLUE).scale(0.3).move_to([1,-0.2,0]).rotate(PI)
        t10 = Triangle(color=BLUE).scale(0.3).move_to([1,-0.7,0])
        s21 = Square(color=BLUE,side_length=0.66).rotate(angle= 45* DEGREES).move_to([1.5,-0.45,0])
        t21 = Triangle(color=BLUE).scale(0.3).move_to([2,-0.2,0]).rotate(PI)
        t20 = Triangle(color=BLUE).scale(0.3).move_to([2,-0.7,0])
        s22 = Square(color=BLUE,side_length=0.66).rotate(angle= 45* DEGREES).move_to([2.5,-0.45,0])
        
        tg = Text("Pattern - 2",font_size=28).move_to([-1.8,0.8,0])
        self.play(Write(tg))

        self.play(Write(s01))  
        self.play(Write(t01))
        self.play(Write(t00))
        self.play(Write(s10))  
        self.play(Write(t11))
        self.play(Write(t10))
        self.play(Write(s21))  
        self.play(Write(t21))
        self.play(Write(t20))
        self.play(Write(s22))

        self.play(Write(s1))
        self.play(Write(s))  
        self.play(Write(s11))
        self.play(Write(t1))
        self.play(Write(t))
        self.play(Write(s2))

    def pat(self):    

        te = Text("Look at this triangles pattern:",font_size=28).move_to([-3,3,0])
        self.play(Write(te))
        triangles = [
            Triangle(color=GREEN, fill_opacity=1).scale(0.5).move_to([-2, 1.5, 0]),
            Triangle(color=GREEN, fill_opacity=1).scale(0.5).move_to([-1, 1.5, 0]).rotate(PI / 2),
            Triangle(color=GREEN, fill_opacity=1).scale(0.5).move_to([0, 1.5, 0]).rotate(PI),
            Triangle(color=GREEN, fill_opacity=1).scale(0.5).move_to([1, 1.5, 0]).rotate(3 * (PI / 2)),
            Triangle(color=GREEN, fill_opacity=1).scale(0.5).move_to([2, 1.5, 0]).rotate(2 * PI)
        ]

        for i, triangle in enumerate(triangles):
            self.play(Write(triangle))
            
            # Get the vertices of the triangle
            vertices = triangle.get_vertices()
            
            # Choose one vertex to place the dot (e.g., the first vertex)
            dot_position = vertices[0]
            dot = Dot(dot_position, color=WHITE)
            self.play(Write(dot))
            
            
            # Add the number under the triangle
            number = Text(str(i + 1), font_size=24)
            number_position = triangle.get_center() + DOWN
            number.move_to([triangle.get_center()[0], number_position[1], 0])
            self.play(Write(number))

        self.wait(2)
        title = Text("Each turn of the shape pattern takes",font_size=28).move_to([-3.5,-1.3,0])
        subtil = Text("1/4th part of circular rotation.",font_size=28).move_to([-2.25,-2,0])
        self.play(Write(title))
        self.play(Write(subtil))
        self.wait()




    def pat1(self):  
        
        te = Text("Now,",font_size=28).move_to([-3,3,0])
        self.play(Write(te))
        triangles = [
            Triangle(color=GREEN, fill_opacity=1).scale(0.5).move_to([-2, 1.5, 0]),
            Triangle(color=GREEN, fill_opacity=1).scale(0.5).move_to([-1, 1.5, 0]).rotate(PI),
            Triangle(color=GREEN, fill_opacity=1).scale(0.5).move_to([0, 1.5, 0]).rotate(3 * (PI / 2)),
            Triangle(color=GREEN, fill_opacity=1).scale(0.5).move_to([1, 1.5, 0]).rotate(2 * PI),
            Triangle(color=GREEN, fill_opacity=1).scale(0.5).move_to([2, 1.5, 0]).rotate(5 * (PI / 2))
        ]

        # Define the vertex offsets (assuming we use the top vertex of the unrotated triangle)
        for i, triangle in enumerate(triangles):
            self.play(Write(triangle))
            
            # Get the vertices of the triangle
            vertices = triangle.get_vertices()
            
            # Choose one vertex to place the dot (e.g., the first vertex)
            dot_position = vertices[0]
            dot = Dot(dot_position, color=WHITE)
            self.play(Write(dot))
            
            # Add the number under the triangle
            number = Text(str(i + 1), font_size=24)
            number_position = triangle.get_center() + DOWN
            number.move_to([triangle.get_center()[0], number_position[1], 0])
            self.play(Write(number))

        self.wait(2)
  

        title = Text("Each turn of the shape pattern takes",font_size=28).move_to([-3.5,-1.3,0])
        subtil = Text("1/2th part of circular rotation.",font_size=28).move_to([-2.25,-2,0])
        self.play(Write(title))
        self.play(Write(subtil))
        self.wait()

       

    def pat2(self):

        te = Text("In this pattern,",font_size=28).move_to([-3,3,0])
        self.play(Write(te))
        triangles = [
            Triangle(color=GREEN, fill_opacity=1).scale(0.5).move_to([-2, 1.5, 0]),
            Triangle(color=GREEN, fill_opacity=1).scale(0.5).move_to([-1, 1.5, 0]).rotate(PI / 8),
            Triangle(color=GREEN, fill_opacity=1).scale(0.5).move_to([0, 1.5, 0]).rotate(PI / 4),
            Triangle(color=GREEN, fill_opacity=1).scale(0.5).move_to([1, 1.5, 0]).rotate(3 * (PI / 8)),
            Triangle(color=GREEN, fill_opacity=1).scale(0.5).move_to([2, 1.5, 0]).rotate(PI / 2)
        ]

        # Add the triangles, dots, and numbers to the scene
        for i, triangle in enumerate(triangles):
            self.play(Write(triangle))
            
            # Get the vertices of the triangle
            vertices = triangle.get_vertices()
            
            # Choose one vertex to place the dot (e.g., the first vertex)
            dot_position = vertices[0]
            dot = Dot(dot_position, color=WHITE)
            self.play(Write(dot))
            
            # Add the number under the triangle
            number = Text(str(i + 1), font_size=24)
            number_position = triangle.get_center() + DOWN
            number.move_to([triangle.get_center()[0], number_position[1], 0])
            self.play(Write(number))

        self.wait(2)
    

        title = Text("Each turn of the shape pattern takes",font_size=28).move_to([-3.5,-1.3,0])
        subtil = Text("1/8th part of circular rotation.",font_size=28).move_to([-2.25,-2,0])
        self.play(Write(title))
        self.play(Write(subtil))
        self.wait()
       
    

    def ex4(self):
         
        t = Text("Some patterns follow Number rules:",font_size=35,color=BLUE).move_to([-3,3,0])

        self.play(Write(t))  
         
        t1 = Text("Now an example,",font_size=28).next_to(t,DOWN)
        self.play(Write(t1)) 

        p1 = Text("5  10  15  20  25").next_to(t1,DOWN)
        self.play(Write(p1))   

        p1 = cvo.CVO().CreateCVO("The rule is either","").setPosition([0,-1,0])
        p2 = cvo.CVO().CreateCVO("multiply 1, 2, 3... by 5","").setPosition([-4,-1,0])
        p3 = cvo.CVO().CreateCVO("add 5 to the number before","").setPosition([4,-1,0])
        
        p1.cvolist.append(p2)
        p1.cvolist.append(p3)
        self.construct1(p1,p1)

    def ex5(self):

        t = Text("Now, let's see how number patterns can \n\n be represented as shape patterns too. ",font_size=35,color=BLUE).move_to([-2.7,2.8,0])
        self.play(Write(t))

        t1 = Text("We could write the rule of 'number pattern 1, 4, 9, 16' as following:",font_size=28).move_to([-1.2,1.5,0])
        self.play(Write(t1)) 


        r =  Square(color=BLUE,side_length=0.5,fill_opacity=1).move_to([-4,-1.5,0])
        self.play(Write(r)) 
        t1 = Text(" 1 ",font_size=30).move_to([-4,-2.1,0])
        self.play(Write(t1))

        i2 = [-2.2, -1.5, 0]  
        s2 = 0.6  
        for i in range(2):  
            for j in range(2):  
            
                x = i2[0] + j * s2
                y = i2[1] + i * s2

                square2 = Square(color=BLUE, side_length=0.5, fill_opacity=1).move_to([x, y, 0])
                self.play(Write(square2))

        t2 = Text(" 1 + 3 = 4 ",font_size=30).move_to([-1.8,-2.1,0])
        self.play(Write(t2))

        i3 = [0.3, -1.5, 0]  
        s3 = 0.6  
        for i in range(3):  
            for j in range(3):  
            
                x = i3[0] + j * s3
                y = i3[1] + i * s3

                square3 = Square(color=BLUE, side_length=0.5, fill_opacity=1).move_to([x, y, 0])
                self.play(Write(square3))

        t3 = Text(" 1 + 3 + 5 = 9 ",font_size=30).move_to([0.8,-2.1,0])
        self.play(Write(t3))


        i4 = [3.5, -1.5, 0]  
        s4 = 0.6  
        for i in range(4):  
            for j in range(4):  
            
                x = i4[0] + j * s4
                y = i4[1] + i * s4

                square4 = Square(color=BLUE, side_length=0.5, fill_opacity=1).move_to([x, y, 0])
                self.play(Write(square4))

        t4 = Text(" 1 + 3 + 5 + 7 = 16 ",font_size=30).move_to([4.7,-2.1,0])
        self.play(Write(t4))
        self.wait()

    def topic1(self): 

        t = Text("TRICK 1").move_to([-4,3,0])
        u = Underline(t)
        self.play(Write(t))
        self.play(Write(u))

        t1 =Text("Write your age ________________",font_size=28).move_to([-1,1.5,0])
        t2 =Text("Add 5 to it ________________",font_size=28).move_to([-1,0.5,0])
        t3 =Text("Multiply the sum by 2 _____________",font_size=28).move_to([-1,-0.5,0])
        t4 =Text("Subtract 10 from it _____________",font_size=28).move_to([-1,-1.5,0])
        t5 =Text("Divide it by 2 _____________",font_size=28).move_to([-1,-2.5,0])


      
        self.play(Write(t1))
        self.play(Write(t2))
        self.play(Write(t3))
        self.play(Write(t4))
        self.play(Write(t5))

        t11 = Text("20",font_size=28).move_to([0,1.6,0])
        t21 = Text("20 + 5 = 25",font_size=28).move_to([0,0.6,0])
        t31 = Text("25 * 2 = 50",font_size=28).move_to([1,-0.4,0])
        t41 = Text("50 - 10 = 40",font_size=28).move_to([0.8,-1.4,0])
        t51 = Text("40 / 2 = 20",font_size=28).move_to([0.4,-2.4,0])
        t6 = Text("You get your age again",font_size=30).move_to([3.5,-3,0])

        self.play(Write(t11))
        self.wait()
        self.play(Write(t21))
        self.wait()
        self.play(Write(t31))
        self.wait()
        self.play(Write(t41))
        self.wait()
        self.play(Write(t51))
        self.wait()
        self.play(Write(t6))



    def topic2(self):
        
        
        t = Text("TRICK 2").move_to([-4,3,0])
        u = Underline(t)
        self.play(Write(t))
        self.play(Write(u))

        t1 =Text("Take a number ________________",font_size=28).move_to([-1,1.5,0])
        t2 =Text("Double it ________________",font_size=28).move_to([-1,0.5,0])
        t3 =Text("Multiply by 5 _____________",font_size=28).move_to([-1,-0.5,0])
        t4 =Text("Divide it by 10 _____________",font_size=28).move_to([-1,-1.5,0])
        


        
        self.play(Write(t1))
        self.play(Write(t2))
        self.play(Write(t3))
        self.play(Write(t4))


        t11 = Text("5",font_size=28).move_to([0,1.6,0])
        t21 = Text("5 * 2 = 10",font_size=28).move_to([0,0.6,0])
        t31 = Text("10 * 5 = 50",font_size=28).move_to([1,-0.4,0])
        t41 = Text("50 / 10 = 5",font_size=28).move_to([0.8,-1.4,0])
        t6 = Text("You get your number again",font_size=30).move_to([3.5,-2,0])

        self.play(Write(t11))
        self.wait()
        self.play(Write(t21))
        self.wait()
        self.play(Write(t31))
        self.wait()
        self.play(Write(t41))
        self.wait()
        self.play(Write(t6))


    def topic3(self):

      

        t = Text("MAGIC SQUARES").move_to([-4,3,0])
        u = Underline(t)
        self.play(Write(t))
        self.play(Write(u)) 

        
        square1 = Square(side_length=3,fill_color=BLUE,fill_opacity=0.7).move_to(LEFT*3)
        l1 = Line(start=[-3.5,1.5,0],end=[-3.5,-1.5,0],color=WHITE)
        l2 = Line(start=[-2.5,1.5,0],end=[-2.5,-1.5,0],color=WHITE)
        l3 = Line(start=[-4.5,0.5,0],end=[-1.5,0.5,0],color=WHITE)
        l4 = Line(start=[-4.5,-0.5,0],end=[-1.5,-0.5,0],color=WHITE)
       
        self.play(Write(square1))
        self.play(Write(l1))
        self.play(Write(l2))
        self.play(Write(l3))
        self.play(Write(l4))

        f1 = Text("6",font_size=30,color=BLACK).move_to([-4,1,0])
        self.play(Write(f1))

        f2 = Text("1",font_size=30,color=BLACK).move_to([-3,1,0])
        self.play(Write(f2))

        f3 = Text("8",font_size=30,color=BLACK).move_to([-2,1,0])
        self.play(Write(f3))

        f4 = Text("7",font_size=30,color=BLACK).move_to([-4,0,0])
        self.play(Write(f4))

        f5 = Text("5",font_size=30,color=BLACK).move_to([-3,0,0])
        self.play(Write(f5))

        f6 = Text("3",font_size=30,color=BLACK).move_to([-2,0,0])
        self.play(Write(f6))

        f7 = Text("2",font_size=30,color=BLACK).move_to([-4,-1,0])
        self.play(Write(f7))

        f8 = Text("9",font_size=30,color=BLACK).move_to([-3,-1,0])
        self.play(Write(f8))

        f9 = Text("4",font_size=30,color=BLACK).move_to([-2,-1,0])
        self.play(Write(f9))


        t1 =Text("Add the numbers in the first row.\n We get 8 + 1 + 6 = 15",font_size=28).move_to([3,2,0])
        t2 =Text("Add the numbers in the last row.\n We get 2 + 9 + 4 = 15",font_size=28).move_to([3,1,0])
        t3 =Text("Add the numbers in the middle column.\n We get 7 + 5 + 3 = 15",font_size=28).move_to([3.5,0,0])
        t4 =Text("Add the numbers on the diagonal.\n We get 6 + 5 + 4 = 15",font_size=28).move_to([3,-1,0])
        t5 = Text("This special number grid is called a magic square.",font_size=30).move_to([-3,-2.3,0])

        
        self.play(Write(t1))
        self.wait()
        self.play(Write(t2))
        self.wait()
        self.play(Write(t3))
        self.wait()
        self.play(Write(t4))
        self.wait()
        self.play(Write(t5))
        self.wait()



       
    
        


       



if __name__ == "__main__":
    scene = Grade5Chapter16PatternsAnim()
    scene.render()