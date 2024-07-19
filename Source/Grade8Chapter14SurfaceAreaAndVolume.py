from manim import *
from AbstractAnim import AbstractAnim
import cvo

class SAV(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.cube()
        self.fadeOutCurrentScene()
        self.areacube()
        self.fadeOutCurrentScene()
        self.cuboidarea()
        self.fadeOutCurrentScene()
        self.tsacuboid()
        self.fadeOutCurrentScene()
        self.lsacuboid()
        self.fadeOutCurrentScene()
        self.cubearea()
        self.fadeOutCurrentScene()
        self.tsacube()
        self.fadeOutCurrentScene()
        self.lsacube()
        self.fadeOutCurrentScene()
        self.cuboidvolume()
        self.fadeOutCurrentScene()
        self.volumecuboid()
        self.fadeOutCurrentScene()
        self.cubevolume()
        self.fadeOutCurrentScene()
        self.volumecube()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
         

    def Introduction(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [-TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("SURFACE AREA AND VOLUME","")
        p11=cvo.CVO().CreateCVO("SHAPES", "")
        p11.extendOname(["CUBE","CUBOID"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def cube(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [-TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("CUBE AND CUBOID","")
        p11=cvo.CVO().CreateCVO("Operations", "")
        p11.extendOname(["AREA","VOLUME"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def areacube(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [-TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("AREA","")
        p11=cvo.CVO().CreateCVO("AREA TYPES", "")
        p11.extendOname(["LSA","TSA"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def cuboidarea(self):

        title = Text("AREA OF CUBOID", color=RED, weight=BOLD)
        title.move_to([0, 3, 0])

        self.play(Write(title))
        self.wait()

        # Cuboid Animation (Scaled down and positioned to the left)
        scale_factor = 0.7  # Adjust as needed
        a = ((-1*scale_factor, -2.25*scale_factor, 0), (-7*scale_factor, -2.25*scale_factor, 0),
             (-8*scale_factor, -2.75*scale_factor, 0), (-2*scale_factor, -2.75*scale_factor, 0), (-1*scale_factor, -2.25*scale_factor, 0))
        base = Polygon(*a, stroke_width=3, color=WHITE)

        b = ((-1*scale_factor, 0.75*scale_factor, 0), (-7*scale_factor, 0.75*scale_factor, 0),
             (-8*scale_factor, 0.25*scale_factor, 0), (-2*scale_factor, 0.25*scale_factor, 0), (-1*scale_factor, 0.75*scale_factor, 0))
        top = Polygon(*b, stroke_width=3, color=WHITE)

        c = ((-0.9*scale_factor, 0.75*scale_factor, 0), (-0.9*scale_factor, -2.25*scale_factor, 0),
             (-2*scale_factor, -2.75*scale_factor, 0), (-2*scale_factor, 0.25*scale_factor, 0), (-1*scale_factor, 0.75*scale_factor, 0))
        face1 = Polygon(*c, stroke_width=3, color=WHITE)

        d = ((-1*scale_factor, 0.75*scale_factor, 0), (-7*scale_factor, 0.75*scale_factor, 0),
             (-7*scale_factor, -2.25*scale_factor, 0), (-0.9*scale_factor, -2.25*scale_factor, 0), (-0.9*scale_factor, 0.75*scale_factor, 0))
        face2 = Polygon(*d, stroke_width=3, color=WHITE)

        e = ((-7*scale_factor, 0.75*scale_factor, 0), (-7*scale_factor, -2.25*scale_factor, 0),
             (-8*scale_factor, -2.75*scale_factor, 0), (-8*scale_factor, 0.25*scale_factor, 0), (-7*scale_factor, 0.75*scale_factor, 0))
        face3 = Polygon(*e, stroke_width=3, color=WHITE)

        f = ((-2*scale_factor, 0.25*scale_factor, 0), (-2*scale_factor, -2.75*scale_factor, 0),
             (-8*scale_factor, -2.75*scale_factor, 0), (-8*scale_factor, 0.25*scale_factor, 0), (-2*scale_factor, 0.25*scale_factor, 0))
        face4 = Polygon(*f, stroke_width=3, color=WHITE)

        # Labels for dimensions
        l_label = Text("l", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        l_label.next_to(base.get_edge_center(DOWN), DOWN)
        b_label = Text("b", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        b_label.next_to(base.get_edge_center(RIGHT), DOWN)
        h_label = Text("h", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        h_label.next_to(top.get_edge_center(RIGHT), RIGHT)

        cuboid_group = VGroup(base, top, face1, face2, face3, face4, l_label, b_label, h_label)
        cuboid_group.move_to([-2, 0, 0])

        self.play(Create(cuboid_group))
        self.wait()


        # LSA of Cuboid (Blue color)
        lsa_text = Text("LSA = 2h(l+b)", color="#ffb3b3", weight=BOLD,font_size=30)
        lsa_text.next_to(cuboid_group, RIGHT*2, buff=1)
        self.play(Write(lsa_text))
        face1.set_fill("#ffb3b3", opacity=0.5)
        self.wait(1)
        face2.set_fill("#ffb3b3", opacity=0.5)
        self.wait(1)
        face3.set_fill("#ffb3b3", opacity=0.5)
        self.wait(1)
        face4.set_fill("#ffb3b3", opacity=0.5)
        self.wait(1)
        


        # Formulas beside the cuboid
        # TSA of Cuboid (Yellow color)
        tsa_text = Text("TSA = 2(lb+bh+hl)", color="#80ff80", weight=BOLD,font_size=30)
        tsa_text.next_to(lsa_text, DOWN)
        self.play(Write(tsa_text))
        face1.set_fill("#80ff80", opacity=0.5)
        self.wait(1)
        face2.set_fill("#80ff80", opacity=0.5)
        self.wait(1)
        face3.set_fill("#80ff80", opacity=0.5)
        self.wait(1)
        face4.set_fill("#80ff80", opacity=0.5)
        self.wait(1)
        top.set_fill("#80ff80", opacity=0.5)
        self.wait(1)
        base.set_fill("#80ff80", opacity=0.5)
        self.wait(1)
        self.wait(2)


    def tsacuboid(self):
        self.setNumberOfCirclePositions(5)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Total surface area of cuboid","2(lb+lh+bh)").setPosition([-4,0,0])
        p11=cvo.CVO().CreateCVO("h variable ","6").setPosition([0,2.5,0])
        p12=cvo.CVO().CreateCVO("l variable","2").setPosition([0,-2.5,0])
        p14=cvo.CVO().CreateCVO("b variable", "4").setPosition([0,0,0])
        p13=cvo.CVO().CreateCVO("TSA OF CUBOID","88").setPosition([4,0,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p14)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)),Create(CurvedArrow(p14.pos,p13.pos)))

    def lsacuboid(self):
        self.setNumberOfCirclePositions(5)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Lateral surface area of cuboid","2h(l+b)").setPosition([-4,0,0])
        p11=cvo.CVO().CreateCVO("h variable ","6").setPosition([0,2.5,0])
        p12=cvo.CVO().CreateCVO("l variable","2").setPosition([0,-2.5,0])
        p14=cvo.CVO().CreateCVO("b variable", "4").setPosition([0,0,0])
        p13=cvo.CVO().CreateCVO("LSA OF CUBOID","72").setPosition([4,0,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p14)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)),Create(CurvedArrow(p14.pos,p13.pos)))



    def cubearea(self):

        title = Text("AREA OF CUBE", color=RED, weight=BOLD)
        title.move_to([0, 3, 0])

        self.play(Write(title))
        self.wait()

        # Coordinates for the cuboid centered around the origin with increased height
        a = ((-1, -0.75, 0), (1, -0.75, 0), (2, -1.25, 0), (0, -1.25, 0), (-1, -0.75, 0))
        base = Polygon(*a, stroke_width=5, color=WHITE)

        # Adjusted y-coordinates for the top to increase height
        b = ((-1, 1.0, 0), (1, 1.0, 0), (2, 0.5, 0), (0, 0.5, 0), (-1, 1.0, 0))
        top = Polygon(*b, stroke_width=5, color=WHITE)

        c = ((-1.1, 1.0, 0), (-1.1, -0.75, 0), (0, -1.25, 0), (0, 0.5, 0), (-1, 1.0, 0))
        face1 = Polygon(*c, stroke_width=5, color=WHITE)

        d = ((-1, 1.0, 0), (1, 1.0, 0), (1, -0.75, 0), (-1.1, -0.75, 0), (-1.1, 1.0, 0))
        face2 = Polygon(*d, stroke_width=5, color=WHITE)

        e = ((1, 1.0, 0), (1, -0.75, 0), (2.1, -1.25, 0), (2.1, 0.5, 0), (1, 1.0, 0))
        face3 = Polygon(*e, stroke_width=5, color=WHITE)

        f = ((0, 0.5, 0), (0, -1.25, 0), (2.1, -1.25, 0), (2.1, 0.5, 0), (0, 0.5, 0))
        face4 = Polygon(*f, stroke_width=5, color=WHITE)

        # Labels for dimensions
        l_label = Text("a", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        l_label.next_to(base.get_edge_center(DOWN), DOWN)
        b_label = Text("a", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        b_label.next_to(base.get_edge_center(LEFT), DOWN)
        h_label = Text("a", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        h_label.next_to(base.get_edge_center(RIGHT * 0.5), UP * 2)

        cube_group = VGroup(base, top, face1, face2, face3, face4, l_label, b_label, h_label)
        cube_group.move_to([-2, 0, 0])  # Move the cube towards the left

        self.play(Create(cube_group))
        # self.play(Write(l_label))
        # self.play(Write(b_label))
        # self.play(Write(h_label))
        self.wait()

        # LSA of Cube (Light Pink color)
        lsa_text = MathTex(r"\mathbf{LSA = 4a^2}", color="#ffb3b3", font_size=40)
        lsa_text.next_to(cube_group, RIGHT * 2, buff=1)
        self.play(Write(lsa_text))
        face1.set_fill("#ffb3b3", opacity=0.5)
        self.wait(1)
        face2.set_fill("#ffb3b3", opacity=0.5)
        self.wait(1)
        face3.set_fill("#ffb3b3", opacity=0.5)
        self.wait(1)
        face4.set_fill("#ffb3b3", opacity=0.5)
        self.wait(1)

        # TSA of Cube (Light Green color)
        tsa_text = MathTex(r"\mathbf{TSA = 6a^2}", color="#80ff80", font_size=40)
        tsa_text.next_to(lsa_text, DOWN)
        self.play(Write(tsa_text))
        face1.set_fill("#80ff80", opacity=0.5)
        self.wait(1)
        face2.set_fill("#80ff80", opacity=0.5)
        self.wait(1)
        face3.set_fill("#80ff80", opacity=0.5)
        self.wait(1)
        face4.set_fill("#80ff80", opacity=0.5)
        self.wait(1)
        top.set_fill("#80ff80", opacity=0.5)
        self.wait(1)
        base.set_fill("#80ff80", opacity=0.5)
        self.wait(1)



    def tsacube(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("total surface area of cube","6a^{2}").setPosition([-4,0,0])
        p11=cvo.CVO().CreateCVO("Constant faces","6").setPosition([0,2,0])
        p12=cvo.CVO().CreateCVO("a variable","2").setPosition([0,-2,0])
        p13=cvo.CVO().CreateCVO("TSA OF CUBE", "24").setPosition([4,0,0])
        p10.SetIsMathText(True)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))

    def lsacube(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("lateral surface area of cube","4a^{2}").setPosition([-4,0,0])
        p11=cvo.CVO().CreateCVO("Constant faces","4").setPosition([0,2,0])
        p12=cvo.CVO().CreateCVO("a variable","2").setPosition([0,-2,0])
        p13=cvo.CVO().CreateCVO("LSA OF CUBE", "16").setPosition([4,0,0])
        p10.SetIsMathText(True)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))


    def cuboidvolume(self):

        title = Text("VOLUME OF CUBOID", color=RED, weight=BOLD)
        title.move_to([0, 3, 0])

        self.play(Write(title))
        self.wait()

        # Cuboid Animation (Scaled down and positioned to the left)
        scale_factor = 0.7  # Adjust as needed
        a = ((-1*scale_factor, -2.25*scale_factor, 0), (-7*scale_factor, -2.25*scale_factor, 0),
             (-8*scale_factor, -2.75*scale_factor, 0), (-2*scale_factor, -2.75*scale_factor, 0), (-1*scale_factor, -2.25*scale_factor, 0))
        base = Polygon(*a, stroke_width=3, color=WHITE)

        b = ((-1*scale_factor, 0.75*scale_factor, 0), (-7*scale_factor, 0.75*scale_factor, 0),
             (-8*scale_factor, 0.25*scale_factor, 0), (-2*scale_factor, 0.25*scale_factor, 0), (-1*scale_factor, 0.75*scale_factor, 0))
        top = Polygon(*b, stroke_width=3, color=WHITE)

        c = ((-0.9*scale_factor, 0.75*scale_factor, 0), (-0.9*scale_factor, -2.25*scale_factor, 0),
             (-2*scale_factor, -2.75*scale_factor, 0), (-2*scale_factor, 0.25*scale_factor, 0), (-1*scale_factor, 0.75*scale_factor, 0))
        face1 = Polygon(*c, stroke_width=3, color=WHITE)

        d = ((-1*scale_factor, 0.75*scale_factor, 0), (-7*scale_factor, 0.75*scale_factor, 0),
             (-7*scale_factor, -2.25*scale_factor, 0), (-0.9*scale_factor, -2.25*scale_factor, 0), (-0.9*scale_factor, 0.75*scale_factor, 0))
        face2 = Polygon(*d, stroke_width=3, color=WHITE)

        e = ((-7*scale_factor, 0.75*scale_factor, 0), (-7*scale_factor, -2.25*scale_factor, 0),
             (-8*scale_factor, -2.75*scale_factor, 0), (-8*scale_factor, 0.25*scale_factor, 0), (-7*scale_factor, 0.75*scale_factor, 0))
        face3 = Polygon(*e, stroke_width=3, color=WHITE)

        f = ((-2*scale_factor, 0.25*scale_factor, 0), (-2*scale_factor, -2.75*scale_factor, 0),
             (-8*scale_factor, -2.75*scale_factor, 0), (-8*scale_factor, 0.25*scale_factor, 0), (-2*scale_factor, 0.25*scale_factor, 0))
        face4 = Polygon(*f, stroke_width=3, color=WHITE)

        # Labels for dimensions
        l_label = Text("l", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        l_label.next_to(base.get_edge_center(DOWN), DOWN)
        b_label = Text("b", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        b_label.next_to(base.get_edge_center(RIGHT), DOWN)
        h_label = Text("h", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        h_label.next_to(top.get_edge_center(RIGHT), RIGHT)

        cuboid_group = VGroup(base, top, face1, face2, face3, face4, l_label, b_label, h_label)
        cuboid_group.move_to([-2, 0, 0])

        self.play(Create(cuboid_group))
        self.wait()

        # Volume of Cuboid (Red color)
        volume_text = Text("Volume = lbh", color="#99ffff", weight=BOLD,font_size=30)
        volume_text.shift(RIGHT * 3)
        self.play(Write(volume_text))
        face1.set_fill("#99ffff", opacity=0.5)
        face2.set_fill("#99ffff", opacity=0.5)
        face3.set_fill("#99ffff", opacity=0.5)
        face4.set_fill("#99ffff", opacity=0.5)
        base.set_fill("#99ffff", opacity=0.5)
        top.set_fill("#99ffff", opacity=0.5)
        self.wait(3)

    def volumecuboid(self):
        self.setNumberOfCirclePositions(5)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("volume of cuboid","l.b.h").setPosition([-4,0,0])
        p11=cvo.CVO().CreateCVO("h variable ","6").setPosition([0,2.5,0])
        p12=cvo.CVO().CreateCVO("l variable","2").setPosition([0,-2.5,0])
        p14=cvo.CVO().CreateCVO("b variable", "4").setPosition([0,0,0])
        p13=cvo.CVO().CreateCVO("VOLUME OF CUBOID","48").setPosition([4,0,0])
        p10.SetIsMathText(True)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p14)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)),Create(CurvedArrow(p14.pos,p13.pos)))



    def cubevolume(self):

        # Title
        title = Text("VOLUME OF CUBE", color=RED, weight=BOLD)
        title.move_to([0, 3, 0])

        self.play(Write(title))
        self.wait()

        # Coordinates for the cuboid centered around the origin with increased height
        a = ((-1, -0.75, 0), (1, -0.75, 0), (2, -1.25, 0), (0, -1.25, 0), (-1, -0.75, 0))
        base = Polygon(*a, stroke_width=5, color=WHITE)

        # Adjusted y-coordinates for the top to increase height
        b = ((-1, 1.0, 0), (1, 1.0, 0), (2, 0.5, 0), (0, 0.5, 0), (-1, 1.0, 0))
        top = Polygon(*b, stroke_width=5, color=WHITE)

        c = ((-1.1, 1.0, 0), (-1.1, -0.75, 0), (0, -1.25, 0), (0, 0.5, 0), (-1, 1.0, 0))
        face1 = Polygon(*c, stroke_width=5, color=WHITE)

        d = ((-1, 1.0, 0), (1, 1.0, 0), (1, -0.75, 0), (-1.1, -0.75, 0), (-1.1, 1.0, 0))
        face2 = Polygon(*d, stroke_width=5, color=WHITE)

        e = ((1, 1.0, 0), (1, -0.75, 0), (2.1, -1.25, 0), (2.1, 0.5, 0), (1, 1.0, 0))
        face3 = Polygon(*e, stroke_width=5, color=WHITE)

        f = ((0, 0.5, 0), (0, -1.25, 0), (2.1, -1.25, 0), (2.1, 0.5, 0), (0, 0.5, 0))
        face4 = Polygon(*f, stroke_width=5, color=WHITE)

        # Labels for dimensions
        l_label = Text("a", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        l_label.next_to(base.get_edge_center(DOWN), DOWN)
        b_label = Text("a", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        b_label.next_to(base.get_edge_center(LEFT), DOWN)
        h_label = Text("a", font="Comic Sans MS", color=WHITE, weight=BOLD).scale(0.5)
        h_label.next_to(base.get_edge_center(RIGHT * 0.5), UP * 2)

        cube_group = VGroup(base, top, face1, face2, face3, face4, l_label, b_label, h_label)
        cube_group.move_to([-2, 0, 0])  # Move the cube towards the left

        self.play(Create(cube_group))
        # self.play(Write(l_label))
        # self.play(Write(b_label))
        # self.play(Write(h_label))
        self.wait()

        # Volume of Cube (Light Blue color)
        volume_text = MathTex(r"\mathbf{Volume = a^3}", color="#99ffff", font_size=40)
        volume_text.shift(RIGHT * 2)
        self.play(Write(volume_text))
        face1.set_fill("#99ffff", opacity=0.5)
        face2.set_fill("#99ffff", opacity=0.5)
        face3.set_fill("#99ffff", opacity=0.5)
        face4.set_fill("#99ffff", opacity=0.5)
        base.set_fill("#99ffff", opacity=0.5)
        top.set_fill("#99ffff", opacity=0.5)
        self.wait(3)

    def volumecube(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("volume of cube","a^{3}").setPosition([-4,0,0])
        p12=cvo.CVO().CreateCVO("a variable","2").setPosition([0,2.5,0])
        p13=cvo.CVO().CreateCVO("VOLUME OF CUBE", "8").setPosition([4,0,0])
        p10.cvolist.append(p12)
        p10.SetIsMathText(True)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p12.pos,p13.pos)))

    def SetDeveloperList(self):
        self.DeveloperList="SURADHYA REDDY"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade8Chapter14SurfaceAreaAndVolume.py"

if __name__ == "__main__":
    scene = SAV()
    scene.render()
