import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo

class sets(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.Formsofset()
        self.belongingness()
        self.typesofsets()
        self.operationsonset()

    def Introduction(self):
        self.angleChoice=[TAU/4,TAU/4,TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Sets","").setPosition([-4,2.5,0])
        p11=cvo.CVO().CreateCVO("Definition","collection of similar elements").setPosition([3,2.5,0])
        p12=cvo.CVO().CreateCVO("Example","A=\{1,2,3\}").setPosition([-2.5,0,0])
        p13=cvo.CVO().CreateCVO("Set name","A").setPosition([3,0,0])
        p14=cvo.CVO().CreateCVO("Elements","1,2,3").setPosition([0,-2.5,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p12.cvolist.append(p13)
        p12.cvolist.append(p14)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
    
    def Formsofset(self):
        self.angleChoice=[TAU/4,TAU/4,TAU/4,TAU/4]
        p14=cvo.CVO().CreateCVO("Sets","").setPosition([-4,2.5,0])
        p10=cvo.CVO().CreateCVO("Forms of Set","").setPosition([3,2.5,0])
        p10onamelist=["Roaster Form","set builder Form"]
        p10.setcircleradius(1.5)
        p11=cvo.CVO().CreateCVO("Example","A= Set of all vowels").setPosition([-3,0,0])
        p11.setcircleradius(1.5)
        p12=cvo.CVO().CreateCVO("Roaster form","A=\{a,e,i,o,u\}").setPosition([3,0,0])
        p13=cvo.CVO().CreateCVO("Set builder form","a=\{x:x is a vowel in english alphabets\}").setPosition([0,-2.5,0])
        p14.cvolist.append(p10)
        p10.extendOname(p10onamelist)
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
        self.construct1(p14,p14)
        self.construct1(p11,p11)
        self.fadeOutCurrentScene()

    def belongingness(self):
        self.angleChoice=[TAU/4,TAU/4,TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Belongs Symbol","$\in$").setPosition([-4,2.5,0])
        p11=cvo.CVO().CreateCVO("Doesnot Belong Symbol","$ \\notin $").setPosition([3,2.5,0])
        p12=cvo.CVO().CreateCVO("Set","A=\{1,2,3\}").setPosition([-3,0,0])
        p13=cvo.CVO().CreateCVO("Belongs","$2 \in A$").setPosition([3,0,0])
        p14=cvo.CVO().CreateCVO("Doesnot belong","$4 \\notin A$").setPosition([0,-2.5,0])
        p12.cvolist.append(p13)
        p12.cvolist.append(p14)
        self.construct1(p10,p10)
        self.construct1(p11,p11)
        self.construct1(p12,p12)
        self.fadeOutCurrentScene()

    def typesofsets(self):
        self.angleChoice=[TAU/4,TAU/4,TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Empty Set","").setPosition([-3,0,0])
        p11=cvo.CVO().CreateCVO("Definition","Set with no elements").setPosition([-4,2.5,0])
        p11=cvo.CVO().CreateCVO("Notation","$\phi$").setPosition([3,2.5,0])
        p12=cvo.CVO().CreateCVO("Example","A=\{x:x is an odd number divisible by 2\}").setPosition([3,0,0])
        text1 = MathTex("NOTE:\phi \\neq \{\phi\}").scale(0.65).to_edge(DOWN).shift(UP*1)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.play(Write(text1))
        self.fadeOutCurrentScene()

        text1 = Text("Universal set - Set that has all elements considered in the problem").scale(0.5).to_edge(UP)
        text2 = Text("Notation - U").scale(0.6).next_to(text1,DOWN)
        text = Text("Venn Diagram").scale(0.5).next_to(text2,DOWN).shift(DOWN*0.5)
        self.play(FadeIn(text1))
        self.play(FadeIn(text2))
        self.play(FadeIn(text))
        self.twodisjointsets()
        universal_set = Rectangle(height=4.5, width=8, color=RED).shift(DOWN*1)
        label_U = Text("U", font_size=24).move_to(universal_set.get_corner(UR) + LEFT*0.3 + DOWN*0.3)
        self.play(Create(universal_set))
        self.play(Write(label_U))
        self.wait(2)
        self.fadeOutCurrentScene()
        self.angleChoice=[TAU/4,TAU/4,TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Subset","").setPosition([-4,0,0])
        p11=cvo.CVO().CreateCVO("Proper subset","").setPosition([-3,2.5,0])
        p12=cvo.CVO().CreateCVO("Notation","$A \subset B$").setPosition([3,2.5,0])
        p13=cvo.CVO().CreateCVO("Improper subset","").setPosition([0,-2.5,0])
        p14=cvo.CVO().CreateCVO("Notation","$A \subseteq B$").setPosition([3,0,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p13)
        p11.cvolist.append(p12)
        p13.cvolist.append(p14)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
        text1 = Text("Subsets").scale(0.8).to_edge(UP)
        self.play(Write(text1))
        text2 = Text("A={1,2,3,4,5,6} B={3,4,5}").scale(0.5).next_to(text1,DOWN)
        self.play(Write(text2))
        set_A = Circle(radius=2, color=BLUE)
        set_B = Circle(radius=1, color=GREEN)

        # Add elements to set A
        elements_A = [Text(str(i), font_size=24).move_to(set_A.get_center() + pos)
                      for i, pos in zip([1,2,6], [RIGHT*1.5,LEFT*1.5, DOWN*1.5])]

        # Add elements to set B
        elements_B = [Text(str(i), font_size=24).move_to(set_B.get_center() + pos)
                      for i, pos in zip([3,4,5], [LEFT*0.5, RIGHT*0.5, DOWN*0.5])]

        # Create labels for subsets A and B
        label_A = Text("A", font_size=24).next_to(set_A, UP)
        label_B = Text("B", font_size=24).next_to(set_B, UP)

        # Add everything to the scene
        self.play(Create(set_A), Write(label_A))
        self.play(Create(set_B), Write(label_B))
        for elem in elements_A:
            self.play(Write(elem))
        for elem in elements_B:
            self.play(Write(elem))

        text = Tex("$B \subset A$ , $A \subseteq A$").scale(0.5).to_edge(RIGHT).shift(LEFT*1.5)
        self.play(Write(text))
        text1 = Text("NOTE\n1.Null set is a subset of Every set\n2.Every set is a subset of itself").scale(0.5).to_edge(DOWN).shift(UP*0.5)
        self.play(Write(text1))
        self.fadeOutCurrentScene()        
    
    def operationsonset(self):
        p10=cvo.CVO().CreateCVO("Opeartions on sets","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Union","").setPosition([-3,0,0])
        p12=cvo.CVO().CreateCVO("Intersection","").setPosition([0,-2.5,0])
        p13=cvo.CVO().CreateCVO("Difference","").setPosition([3,0,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
        text1 = Text("UNION - Set of distinct elements present in both the sets\n").scale(0.5).to_edge(UP)
        text2 = Tex("Notation-$\cup$").scale(0.6).next_to(text1,DOWN)
        text3 = Tex("A=\{1,2,3\} , B=\{3,4,5\}, $A \cup B$=\{1,2,3,4,5\}").scale(0.75).to_edge(DOWN).shift(UP*0.65)
        self.play(FadeIn(text1))
        self.play(FadeIn(text2))
        self.play(FadeIn(text3))
        self.twointersectingsets()
        self.wait(2)
        self.play(FadeOut(text1))
        self.play(FadeOut(text2))
        self.play(FadeOut(text3))
        text4 = Text("INTERSECTION - Set of common elements of two sets\n").scale(0.5).to_edge(UP)
        text5 = Tex("Notation-$\cap$").scale(0.6).next_to(text1,DOWN)
        text6 = Tex("A=\{1,2,3\} , B=\{3,4,5\}, $A \cap B$=\{3\}").scale(0.75).to_edge(DOWN).shift(UP*0.65)
        self.play(FadeIn(text4))
        self.play(FadeIn(text5))
        self.play(FadeIn(text6))
        self.wait(2)
        self.play(FadeOut(text4))
        self.play(FadeOut(text5))
        self.play(FadeOut(text6))
        text7 = Text("DIFFERENCE- Set of elements which belong to A but not to B\n").scale(0.5).to_edge(UP)
        text8 = Tex("$A$=\{1,2,3\} $B$=\{3,4,5\}").scale(0.6).next_to(text7,DOWN)
        text10 = Tex("$A-B$=\{1,2\}").scale(0.6).to_edge(LEFT).shift(RIGHT*1)
        text11 = Tex("$B-A$=\{4,5\}").scale(0.6).to_edge(RIGHT).shift(LEFT*1)
        text9 = Tex("Note - $A-B$ $\\neq$ $B-A$").scale(0.75).to_edge(DOWN).shift(UP*1)
        self.play(FadeIn(text7))
        self.play(FadeIn(text8))
        self.play(FadeIn(text10))
        self.play(FadeIn(text11))
        self.play(FadeIn(text9))
        self.wait(2)
        self.fadeOutCurrentScene()
        text1 = Text("Disjoint Sets - Sets with no common elements").scale(0.5).to_edge(UP)
        self.play(Write(text1))
        text2 = Tex("A=\{1,3,5\}, B=\{2,4,6\}, $A \cap B$=$\phi$").scale(0.75).next_to(text1,DOWN)
        self.play(Write(text2))
        self.twodisjointsets()
        self.fadeOutCurrentScene()
        self.angleChoice=[TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Equal Sets","Sets that have exactly same elements").setPosition([-3,0,0])
        p11=cvo.CVO().CreateCVO("Notation","$=$").setPosition([3,0,0])
        p10.cvolist.append(p11)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
        self.angleChoice=[TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Finite sets","Sets that have finite no. of elements").setPosition([-3,2,0])
        p11=cvo.CVO().CreateCVO("Example","A=\{x $\in$ N:$0<x<10$\}").setPosition([3,2,0])
        p11.setcircleradius(2)
        p12=cvo.CVO().CreateCVO("Infinite sets","Sets that have infinite no. of elements").setPosition([-3,-2,0])
        p13=cvo.CVO().CreateCVO("Example","A=\{x:x is a Natural number\}").setPosition([3,-2,0])
        p13.setcircleradius(2.1)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)
        p12.cvolist.append(p13)
        self.construct1(p12,p12)
        self.fadeOutCurrentScene()
        self.angleChoice=[TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Cardinality","").setPosition([-3,-1,0])
        p11=cvo.CVO().CreateCVO("Definition","no. of elements in a set").setPosition([3,2,0])
        p11.setcircleradius(2)
        p12=cvo.CVO().CreateCVO("Representation","n(A)").setPosition([3,-2,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def twointersectingsets(self):
        set_A = Circle(radius=1.5, color=BLUE, fill_opacity=0.5).shift(LEFT)
        set_B = Circle(radius=1.5, color=GREEN, fill_opacity=0.5).shift(RIGHT)
        
        # Create the labels for the sets
        label_A = Text("A", font_size=24).next_to(set_A, UP)
        label_B = Text("B", font_size=24).next_to(set_B, UP)

        # Elements of set A and set B
        elements_A = [1, 2, 3]
        elements_B = [3, 4, 5]

        # Create text objects for the elements and position them
        elements_text_A = [
            Text(str(elem), font_size=24).move_to(set_A.get_center() + pos)
            for elem, pos in zip(elements_A, [UP*0.5, DOWN*1, RIGHT*1.5])
        ]
        elements_text_B = [
            Text(str(elem), font_size=24).move_to(set_B.get_center() + pos)
            for elem, pos in zip(elements_B, [UP*0.5, DOWN*1, RIGHT*1])
        ]

        # Position for the common element
        common_element = Text("3", font_size=24).move_to(ORIGIN)

        # Animate the creation of sets and elements
        self.play(Create(set_A), Write(label_A))
        self.play(Create(set_B), Write(label_B))

        for elem in elements_text_A:
            if elem.text != "3":
                self.play(Write(elem))

        for elem in elements_text_B:
            if elem.text != "3":
                self.play(Write(elem))

        self.play(Write(common_element))

    def twodisjointsets(self):
        set_A = Circle(radius=1.5, color=BLUE).shift(LEFT*2,DOWN*1)
        set_B = Circle(radius=1.5, color=GREEN).shift(RIGHT*2,DOWN*1)

        # Add elements to set A
        elements_A = [Text(str(i), font_size=24).move_to(set_A.get_center() + pos)
                      for i, pos in zip([1, 3, 5], [LEFT*0.5, RIGHT*0.5, DOWN*0.5])]

        # Add elements to set B
        elements_B = [Text(str(i), font_size=24).move_to(set_B.get_center() + pos)
                      for i, pos in zip([2, 4, 6], [LEFT*0.5, RIGHT*0.5, DOWN*0.5])]

        # Create labels for subsets A and B
        label_A = Text("A", font_size=24).next_to(set_A, UP)
        label_B = Text("B", font_size=24).next_to(set_B, UP)

        # Add everything to the scene
        self.play(Create(set_A), Write(label_A))
        self.play(Create(set_B), Write(label_B))
        for elem in elements_A:
            self.play(Write(elem))

        for elem in elements_B:
            self.play(Write(elem))
        
        
        

if __name__ == "__main__":
    import os
    #os.system("manim -pql venn_diagram.py VennDiagram")
    scene = sets()
    scene.render()

