import json
from manim import*
from AbstractAnim import AbstractAnim
import cvo

class Playingwithshapes(AbstractAnim):
    def construct(self):
        self.shapes()
        self.fadeOutCurrentScene()
        self.cube()
        self.fadeOutCurrentScene()
        # self.cubani()
        # self.fadeOutCurrentScene()
        self.cubshadow()
        self.fadeOutCurrentScene()
        self.cuboid()
        self.fadeOutCurrentScene()
        self.dicecut()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

    
    def shapes(self):
        self.isRandom= False
        self.setNumberOfAngleChoices(4)
        p10=cvo.CVO().CreateCVO("Shapes","").setPosition([-4,0,0])
        p11=cvo.CVO().CreateCVO("Cube","").setPosition([2,2,0])
        p12=cvo.CVO().CreateCVO("Cuboid","").setPosition([2,0,0])
        p13=cvo.CVO().CreateCVO("Sphere","").setPosition([2,-2,0])

        p10.setangle(-TAU/4)
        p11.setangle(-TAU/4)
        p12.setangle(-TAU/4)
        p13.setangle(-TAU/4)

        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)

        self.construct1(p10,p10)

    def cube(self):
        self.isRandom= False
        self.setNumberOfAngleChoices(3)
        p10=cvo.CVO().CreateCVO("Cube","").setPosition([-4,0,0])
        p11=cvo.CVO().CreateCVO("Faces","6").setPosition([2,2,0])
        p12=cvo.CVO().CreateCVO("Edges","12").setPosition([2,0,0])
        p13=cvo.CVO().CreateCVO("Vertices","8").setPosition([2,-2,0])
        p14=cvo.CVO().CreateCVO("Dimensions","height,width,length are same").setPosition([2,-4,0])
        p14.setcircleradius(1.8)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.construct1(p10,p10)
    
    def cubeani(self):
        text=Text("Cube",font_size=36).to_edge(UP * 0.1)
        text.add(Underline(text, buff=0.1))
        self.play(Write(text))

        vertices = [
             [-1, -1, 0],
            [1, -1, 0], 
            [1, 1, 0],  
            [-1, 1, 0], 
            [-0.5, -0.5, 0],
            [1.5, -0.5, 0], 
            [1.5, 1.5, 0],  
            [-0.5, 1.5, 0]  
        ]


        edges_front = [
            (0, 1), (1, 2), (2, 3), (3, 0)
        ]

        edges_back = [
            (4, 5), (5, 6), (6, 7), (7, 4)
        ]

        edges_connect = [
            (0, 4), (1, 5), (2, 6), (3, 7)  
        ]

        for start, end in edges_front:
            line = Line(start=vertices[start], end=vertices[end], color=BLUE)
            self.play(Create(line))

        for start, end in edges_back:
            line = Line(start=vertices[start], end=vertices[end], color=BLUE)
            self.play(Create(line))

        for start, end in edges_connect:
            line = Line(start=vertices[start], end=vertices[end], color=BLUE)
            self.play(Create(line))

        self.wait(2)

    def cubshadow(self):
        self.isRandom= False
        self.setNumberOfAngleChoices(2)
        p10=cvo.CVO().CreateCVO("Cube","").setPosition([-4,0,0])
        p11=cvo.CVO().CreateCVO("Shadow","Rectangle").setPosition([2,2,0])
        p10.cvolist.append(p11)
        self.construct1(p10,p10)
        


    def cuboid(self):
        self.isRandom= False
        self.setNumberOfAngleChoices(4)
        p10=cvo.CVO().CreateCVO("Cuboid","").setPosition([-4,0,0])
        p11=cvo.CVO().CreateCVO("Faces","6").setPosition([2,2,0])
        p12=cvo.CVO().CreateCVO("Edges","12").setPosition([2,0,0])
        p13=cvo.CVO().CreateCVO("Vertices","8").setPosition([2,-2,0])
        p14=cvo.CVO().CreateCVO("Dimensions","Length, width, height are different")
        p14.setcircleradius(1.9)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)

        self.construct1(p10,p10)

    def cuboshadow(self):
        self.isRandom= False
        self.setNumberOfAngleChoices(2)
        p10=cvo.CVO().CreateCVO("Cuboid","").setPosition([-4,0,0])
        p11=cvo.CVO().CreateCVO("Shadow","Rectangle").setPosition([2,2,0])
        p10.cvolist.append(p11)
        self.construct1(p10,p10)
        

    def sphshadow(self):
        self.isRandom= False
        self.setNumberOfAngleChoices(2)
        p10=cvo.CVO().CreateCVO("Sphere","").setPosition([-4,0,0])
        p11=cvo.CVO().CreateCVO("Shadow","Circle").setPosition([2,2,0])
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def dicecut(self):
        example=Text("Dice Cut-out",color=YELLOW_D).to_edge(UP)
        square_size = 1.5
        dot_radius = 0.09

        # Create smaller squares for each face of the die in their original positions
        face_1 = Square(side_length=square_size).shift(UP * 1.5)         # Top face
        face_2 = Square(side_length=square_size)                           # Center face
        face_3 = Square(side_length=square_size).shift(RIGHT * 1.5)      # Right face
        face_4 = Square(side_length=square_size).shift(LEFT * 1.5)       # Left face
        face_5 = Square(side_length=square_size).shift(DOWN * 1.5)       # Bottom face
        face_6 = Square(side_length=square_size).shift(DOWN * 3)         # Bottom-most face

        # Define dot positions for each face relative to the center of the face
        dots_face_1 = [Dot(radius=dot_radius).move_to(face_1.get_center())]  # 1 dot in the center

        dots_face_2 = [
            Dot(radius=dot_radius).move_to(face_2.get_center()).shift( LEFT*0.2),
            Dot(radius=dot_radius).move_to(face_2.get_center()).shift( RIGHT*0.2),
            Dot(radius=dot_radius).move_to(face_2.get_center()).shift(RIGHT*0.2).shift(UP*0.4),
            Dot(radius=dot_radius).shift(face_2.get_center()).shift(DOWN*0.4).shift(LEFT*0.2),
            Dot(radius=dot_radius).move_to(face_2.get_center()).shift(UP*0.4).shift(LEFT*0.2),
            Dot(radius=dot_radius).move_to(face_2.get_center()).shift(DOWN*0.4).shift(RIGHT*0.2)
        ]

        dots_face_3 = [
            Dot(radius=dot_radius).move_to(face_3.get_center()).shift(UP*0.4).shift(LEFT*0.4),
            Dot(radius=dot_radius).move_to(face_3.get_center()).shift(DOWN*0.4).shift(RIGHT*0.4),
            Dot(radius=dot_radius).move_to(face_3.get_center())
        ]

        dots_face_4 = [
            Dot(radius=dot_radius).move_to(face_4.get_center()).shift(UP*0.2).shift(LEFT*0.2),
            Dot(radius=dot_radius).move_to(face_4.get_center()).shift(DOWN*0.2).shift(RIGHT*0.2)
        ]

        dots_face_5 = [
            Dot(radius=dot_radius).move_to(face_5.get_center()).shift(UP*0.4).shift(LEFT*0.4),
            Dot(radius=dot_radius).move_to(face_5.get_center()).shift(DOWN*0.4).shift(RIGHT*0.4),
            Dot(radius=dot_radius).move_to(face_5.get_center()).shift(RIGHT*0.4).shift(UP*0.4),
            Dot(radius=dot_radius).move_to(face_5.get_center()).shift(DOWN*0.4).shift(LEFT*0.4)
        ]

        dots_face_6 = [
            Dot(radius=dot_radius).move_to(face_6.get_center()).shift(UP*0.4).shift(LEFT*0.4),
            Dot(radius=dot_radius).move_to(face_6.get_center()).shift(DOWN*0.4).shift(RIGHT*0.4),
            Dot(radius=dot_radius).move_to(face_6.get_center()).shift(RIGHT*0.4).shift(UP*0.4),
            Dot(radius=dot_radius).move_to(face_6.get_center()).shift(DOWN*0.4).shift(LEFT*0.4),
            Dot(radius=dot_radius).move_to(face_6.get_center())
        ]

        # Add dots to faces
        for dot in dots_face_1:
            face_1.add(dot)
        for dot in dots_face_2:
            face_2.add(dot)
        for dot in dots_face_3:
            face_3.add(dot)
        for dot in dots_face_4:
            face_4.add(dot)
        for dot in dots_face_5:
            face_5.add(dot)
        for dot in dots_face_6:
            face_6.add(dot)

        # Display the net
        self.play(Write(example))
        self.play(Create(face_1), Create(face_2), Create(face_3),
                  Create(face_4), Create(face_5), Create(face_6))
        self.wait(3)
    
    def SetDeveloperList(self): 
       self.DeveloperList="T Sai Rohith Reddy" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade5Chapter7PlayingWithShapes.py"

if __name__=="__main__":
    Scene=Playingwithshapes()
    Scene.render()