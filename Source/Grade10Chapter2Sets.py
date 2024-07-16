import json
from manim import *
from AbstractAnim import AbstractAnim
import cvo

class sets(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.Cardinalityofset()
        self.fadeOutCurrentScene()
        self.Formsofset()
        self.fadeOutCurrentScene()
        self.Belongingness()
        self.fadeOutCurrentScene()
        self.Typesofsets()
        self.fadeOutCurrentScene()
        self.EmptySet()
        self.fadeOutCurrentScene()
        self.UniversalSet()
        self.fadeOutCurrentScene()
        self.Subset()
        self.fadeOutCurrentScene()
        self.FiniteSets()
        self.fadeOutCurrentScene()
        self.InifniteSets()
        self.fadeOutCurrentScene()
        self.EqualSets()
        self.fadeOutCurrentScene()
        self.Operationsonset()
        self.fadeOutCurrentScene()
        self.Union()
        self.fadeOutCurrentScene()
        self.Intersection()
        self.fadeOutCurrentScene()
        self.Difference()
        self.fadeOutCurrentScene()
        self.DisjointSets()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

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

    def Cardinalityofset(self):
        self.angleChoice=[TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Cardinality of Set","").setPosition([-3,-1,0])
        p11=cvo.CVO().CreateCVO("Definition","no. of elements in a set").setPosition([3,2,0])
        p11.setcircleradius(2)
        p12=cvo.CVO().CreateCVO("Representation","n(A)").setPosition([3,-2,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
    
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

    def Belongingness(self):
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

    def Typesofsets(self):
        self.angleChoice=[TAU/4,TAU/4,TAU/4,TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Types of Sets","").setPosition([-4,-1,0])
        p11=cvo.CVO().CreateCVO("Empty Set","").setPosition([-1.5,2,0])
        p12=cvo.CVO().CreateCVO("Universal Set","").setPosition([1,2,0])
        p13=cvo.CVO().CreateCVO("Subset","").setPosition([3,2,0])
        p14=cvo.CVO().CreateCVO("Finite Set","").setPosition([4,0,0])
        p15=cvo.CVO().CreateCVO("Infinite Set","").setPosition([3.5,-2.5,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        self.construct1(p10,p10)

    def EmptySet(self):
        self.angleChoice=[TAU/4,TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Empty Set","").setPosition([-3,0,0])
        p11=cvo.CVO().CreateCVO("Definition","Set with no elements").setPosition([-4,2.5,0])
        p11=cvo.CVO().CreateCVO("Notation","$\phi$").setPosition([3,2.5,0])
        p12=cvo.CVO().CreateCVO("Example","A=\{x:x is an odd number divisible by 2\}").setPosition([3,0,0])
        text1 = MathTex("NOTE:\phi \\neq \{\phi\}").scale(0.65).to_edge(DOWN).shift(UP*1)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.play(Write(text1))
        self.wait(2)
        self.fadeOutCurrentScene()

    def UniversalSet(self):
        text1 = Text("Universal set - Set that has all elements considered in the problem").scale(0.5).to_edge(UP)
        text2 = Text("Notation - U").scale(0.6).next_to(text1,DOWN)
        text = Text("Venn Diagram").scale(0.5).next_to(text2,DOWN).shift(DOWN*0.5)
        self.play(FadeIn(text1))
        self.play(FadeIn(text2))
        self.wait(2)
        self.play(FadeIn(text))
        self.twodisjointsets()
        universal_set = Rectangle(height=4.5, width=8, color=RED).shift(DOWN*1)
        label_U = Text("U", font_size=24).move_to(universal_set.get_corner(UR) + LEFT*0.3 + DOWN*0.3)
        self.play(Create(universal_set))
        self.play(Write(label_U))
        self.wait(2)
        self.fadeOutCurrentScene()

    def Subset(self):
        title = Text("Subsets").scale(0.8).to_edge(UP)
        self.play(Write(title))
        text1 = Text("A={1,2,3,4,5,6}\nB={3,4,5}",font_size=24).next_to(title,DOWN,buff=0.5)
        self.play(Write(text1))

        set_A = Circle(radius=2, color=BLUE,fill_opacity=0.5).shift(LEFT*3)
        set_B = Circle(radius=1, color=GREEN,fill_opacity=0.5).shift(LEFT*3)

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

        for elem in elements_A:
            self.play(Write(elem))
        for elem in elements_B:
            self.play(Write(elem))
        
        self.play(Create(set_B), Write(label_B))

        proper_subset_text = MathTex("\\text{Proper Subset - }","\\text{A set that contains only}","\\text{few elements of original set}").scale(0.8).arrange(DOWN,aligned_edge=LEFT).to_edge(RIGHT).shift(UP*1).set_color(GREEN)
        notation1 = Tex("Notation - $ \subset $").scale(0.75).next_to(proper_subset_text,DOWN,buff=0.3)
        proper_subset = Tex("$B \subset A$").scale(0.75).next_to(notation1,DOWN,buff=0.3).set_color(GREEN)
        self.play(FadeIn(proper_subset_text),FadeIn(notation1))
        self.wait(2)
        self.play(Write(proper_subset))
        self.wait(2)
        self.play(FadeOut(proper_subset_text,notation1,proper_subset))

        improper_subset_text =  MathTex("\\text{Improper Subset - }","\\text{A set that contains every }","\\text{element of the original set}").scale(0.8).arrange(DOWN,aligned_edge=LEFT).to_edge(RIGHT).shift(UP*1).set_color(BLUE)
        notation2 = Tex("Notation - $ \subseteq $").scale(0.75).next_to(improper_subset_text,DOWN,buff=0.3)
        improper_subset = Tex("$A \subseteq A$").scale(0.75).next_to(notation2,DOWN,buff=0.3).set_color(BLUE)
        self.play(FadeIn(improper_subset_text),FadeIn(notation2))
        self.wait(2)
        self.play(Write(improper_subset))
        self.wait(2)
        
        text1 = Text("NOTE-\n1. Null set is a subset of Every set\n2. Every set is a subset of itself").scale(0.5).to_edge(DOWN).shift(UP*0.5,RIGHT*3).set_color(YELLOW)
        self.play(Write(text1))
        self.wait(2)

    def FiniteSets(self):
        self.angleChoice=[TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Finite sets","").setPosition([-3,0,0])
        p11=cvo.CVO().CreateCVO("Definiton","Sets that have finite no. of elements").setPosition([2,2,0])
        p12=cvo.CVO().CreateCVO("Example","A=\{x $\in$ N:$0<x<10$\}").setPosition([2,-2,0])
        p12.setcircleradius(2.1)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        p11.setcircleradius(2)
        
    def InifniteSets(self):
        self.angleChoice=[TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Infinite sets","").setPosition([-3,0,0])
        p11=cvo.CVO().CreateCVO("Definiton","Sets that have infinite no. of elements").setPosition([2,2,0])
        p12=cvo.CVO().CreateCVO("Example","A=\{x:x is a Natural number\}").setPosition([2,-2,0])
        p12.setcircleradius(2.1)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)       

    def EqualSets(self):
        self.angleChoice=[TAU/4]
        p10=cvo.CVO().CreateCVO("Equal Sets","").setPosition([-3,0,0])
        p11=cvo.CVO().CreateCVO("Defintion","Sets that have exactly same elements").setPosition([3,0,0])
        p10.cvolist.append(p11)
        self.construct1(p10,p10)
    
    def Operationsonset(self):
        p10=cvo.CVO().CreateCVO("Opeartions on sets","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Union","").setPosition([-3,0,0])
        p12=cvo.CVO().CreateCVO("Intersection","").setPosition([0,-2.5,0])
        p13=cvo.CVO().CreateCVO("Difference","").setPosition([3,0,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.construct1(p10,p10)

    def Union(self):
        text1 = Text("UNION - Set of distinct elements present in both the sets\n").scale(0.5).to_edge(UP)
        text2 = Tex("Notation-$\cup$").scale(0.6).next_to(text1,DOWN)
        text3 = Tex("A=\{1,2,3\} , B=\{3,4,5\}, $A \cup B$=\{1,2,3,4,5\}").scale(0.75).to_edge(DOWN).shift(UP*0.65)
        self.play(FadeIn(text1))
        self.play(FadeIn(text2))
        self.wait(1)
        self.play(FadeIn(text3))
        self.twointersectingsets()
        self.wait(2)
        self.play(FadeOut(text1,text2,text3))

    def Intersection(self):
        text1 = Text("INTERSECTION - Set of common elements of two sets\n").scale(0.5).to_edge(UP)
        text2 = Tex("Notation-$\cap$").scale(0.6).next_to(text1,DOWN)
        text3 = Tex("A=\{1,2,3\} , B=\{3,4,5\}, $A \cap B$=\{3\}").scale(0.75).to_edge(DOWN).shift(UP*0.65)
        self.play(FadeIn(text1))
        self.play(FadeIn(text2))
        self.wait(1)
        self.twointersectingsets()
        self.play(FadeIn(text3))
        self.wait(2)
        self.play(FadeOut(text1,text2,text3))

    def Difference(self):
        text1 = Text("DIFFERENCE- Set of elements which belong to A but not to B\n").scale(0.5).to_edge(UP)
        text2 = Tex("$A$=\{1,2,3\} $B$=\{3,4,5\}").scale(0.6).next_to(text1,DOWN)
        text3 = Tex("$A-B$=\{1,2\}").scale(0.6).to_edge(LEFT).shift(RIGHT*1)
        text4 = Tex("$B-A$=\{4,5\}").scale(0.6).to_edge(RIGHT).shift(LEFT*1)
        text5 = Tex("Note : $A-B$ $\\neq$ $B-A$").scale(0.75).to_edge(DOWN).shift(UP*1)
        self.play(FadeIn(text1))
        self.play(FadeIn(text2))
        self.wait(1)
        self.twointersectingsets()
        self.play(FadeIn(text3))
        self.wait(1)
        self.play(FadeIn(text4))
        self.wait(1)
        self.play(FadeIn(text5))
        self.wait(2)

    def DisjointSets(self):
        text1 = Text("Disjoint Sets - Sets with no common elements").scale(0.5).to_edge(UP)
        self.play(Write(text1))
        text2 = Tex("A=\{1,3,5\}, B=\{2,4,6\}, $A \cap B$=$\phi$").scale(0.75).next_to(text1,DOWN)
        self.play(Write(text2))
        self.twodisjointsets()
        self.wait(2)

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
        self.play(FadeIn(set_A), FadeIn(label_A))
        self.play(FadeIn(set_B), FadeIn(label_B))

        for elem in elements_text_A:
            if elem.text != "3":
                self.play(Write(elem))

        for elem in elements_text_B:
            if elem.text != "3":
                self.play(Write(elem))

        self.play(Write(common_element))

    def twodisjointsets(self):
        set_A = Circle(radius=1.5, color=BLUE,fill_opacity=0.5).shift(LEFT*2,DOWN*1)
        set_B = Circle(radius=1.5, color=GREEN,fill_opacity=0.5).shift(RIGHT*2,DOWN*1)

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
        self.play(FadeIn(set_A), FadeIn(label_A))
        self.play(FadeIn(set_B), FadeIn(label_B))
        for elem in elements_A:
            self.play(Write(elem))

        for elem in elements_B:
            self.play(Write(elem))

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade10Chapter2Sets.py"

    def SetDeveloperList(self):
        self.DeveloperList="Sindhu"
               

if __name__ == "__main__":
    import os
    scene = sets()
    scene.render()
