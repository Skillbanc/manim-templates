from manim import *
from AbstractAnim import AbstractAnim
import cvo

class SetOperations(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.introduction()
        self.fadeOutCurrentScene()
        self.Settypes()
        self.fadeOutCurrentScene()
        self.typesofsets()
        self.fadeOutCurrentScene()
        self.BasicOperationsonSets()
        self.fadeOutCurrentScene()
        self.union_scene()
        self.fadeOutCurrentScene()
        self.intersection_scene()
        self.fadeOutCurrentScene()
        self.difference_scene()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()


    def introduction(self):
        self.isRandom=False
        self.positionChoice = [[-4,-2,0],[4,-2,0],[3,2,0],[-4,2,0]]
        p10=cvo.CVO().CreateCVO("Set","A set is a well-defined collection of distinct objects.").setangle(-TAU/5)
        p11=cvo.CVO().CreateCVO("Ex 1:Set of Natural Numbers:","{1,2,3,4,5,...}")
        p12=cvo.CVO().CreateCVO("Ex 2:Set of Vowels in English Alphabet:","{a,e,i,o,u}")
        p13=cvo.CVO().CreateCVO("Ex 3:Set of Fruits:","{apple,banana,grape,kiwi}")

        p10.setcircleradius(1.25)
        p11.setcircleradius(1.25)
        p12.setcircleradius(1.25)
        p13.setcircleradius(1.5)
    
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)

        self.construct1(p10,p10)




    def Settypes(self):
        self.isRandom=False
        self.positionChoice = [[0,0,0],[-0.5,2.5,0],[2.5,2,0],[4,0.5,0],[4.5,-2,0],[-4.25,-2.75,0],[-4,-0.5,0],[-3,2,0]]
        p10=cvo.CVO().CreateCVO("Types of sets","").setangle(TAU/2)
        p11=cvo.CVO().CreateCVO("Universal set","")
        p12=cvo.CVO().CreateCVO("Empty set","")
        p13=cvo.CVO().CreateCVO("Subset","")
        p14=cvo.CVO().CreateCVO("Equal set","")
        p15=cvo.CVO().CreateCVO("Disjoint set","")
        p16=cvo.CVO().CreateCVO("Finite set","")
        p17=cvo.CVO().CreateCVO("Infinite set","")

    
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        p10.cvolist.append(p16) 
        p10.cvolist.append(p17)

        self.construct1(p10,p10)   
        

    def typesofsets(self):

        universal = Text("Universal Set",color=DARK_BLUE).to_edge(UP*0.7)
        sub_title1 = Text("A universal set contains all elements relevant to a specific context .",font_size=29).to_edge(UP*2.75)
        sub_title2 = Text("represented as U = {1, 2, 3, 4, 5}",font_size=29).to_edge(UP*4.5)

        # Universal set U
        universal_set = Circle(radius=2, color=GRAY, fill_opacity=0.3).shift(DOWN*1.75)
        label_U = Tex("Universal Set $U$").next_to(universal_set, UP)

        # Numbers for Universal set
        numbers_U = Tex("1, 2, 3, 4, 5").move_to(universal_set)

        self.play(Write(universal))
        self.wait(1)
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)

        self.play(Create(universal_set), Write(label_U))
        self.wait(1)

        self.play(Write(numbers_U))
        self.wait(1)

        self.play(FadeOut(numbers_U), FadeOut(label_U), FadeOut(universal_set), FadeOut(sub_title2), FadeOut(sub_title1), FadeOut(universal))


        Empty_set = Text("Empty Set",color=GRAY).to_edge(UP*0.7)
        sub_title1 = Text("An empty set is a set that contains no elements also known as a null set.",font_size=29).to_edge(UP*2.75)
        sub_title2 = Text("Empty set is denoted by the symbol ∅ or { }",font_size=29).to_edge(UP*4.5)

        # Empty set ∅
        empty_set = Circle(radius=1.5, color=PURPLE, fill_opacity=0.2).shift(DOWN*1.75)
        label_empty = Tex("Empty Set $\\emptyset$",color=PURPLE).next_to(empty_set, UP)

        self.play(Write(Empty_set))
        self.wait(1)
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)

        self.play(Create(empty_set), Write(label_empty))
        self.wait(1)

        self.play(FadeOut(empty_set), FadeOut(label_empty), FadeOut(sub_title2),FadeOut(sub_title1),FadeOut(Empty_set))



        # Subset sets definition
        sub_set = Text("Subset",color=LIGHTER_GREY).to_edge(UP*0.7)
        sub_title1 = Text("If all elements of set B are present in A, then B is said to be subset of A .",font_size=29).to_edge(UP*2.75)
        sub_title2 = Text(" B is subset of A is Represented as B ⊆ A .",font_size=29).to_edge(UP*4.5)
        
        # Set A
        set_A = Circle(radius=2, color=BLUE, fill_opacity=0.3).shift(LEFT*3+DOWN*1.75)
        label_A = Tex("Set $A$", color=BLUE).next_to(set_A, UP)
        numbers_A = Tex("1, 2, 3, 4").move_to(set_A)

        # Set B (subset of A)
        set_B = Circle(radius=1.5, color=PINK, fill_opacity=0.3).shift(RIGHT*3+DOWN*1.75)
        label_B = Tex("Set $B$ (Subset of $A$)", color=PINK).next_to(set_B, UP)
        numbers_B = Tex("2, 4").move_to(set_B)

        arrow = Arrow(set_B, set_A, color=WHITE)

        self.play(Write(sub_set))
        self.wait(1)
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)

        self.play(Create(set_A), Write(label_A))
        self.play(Write(numbers_A))
        self.wait(1)

        self.play(Create(set_B), Write(label_B))
        self.play(Write(numbers_B))
        self.play(Create(arrow))
        self.wait(2)

        self.play(FadeOut(numbers_B), FadeOut(set_B), FadeOut(label_B), FadeOut(arrow), FadeOut(numbers_A), FadeOut(set_A), FadeOut(label_A), FadeOut(sub_title2),FadeOut(sub_title1),FadeOut(sub_set))

        
        # Equal sets definition
        equal_set = Text("Equal Sets :", color=GREEN).to_edge(UP * 1 + LEFT * 2.75)
        equal_sets_desc = Text("Sets with exactly the same elements, regardless of order or repetition.", font_size=29).to_edge(UP * 3)

        # Example of equal sets in roster form
        equal_sets_example = MathTex(r"Example :   \{p, q, r\} = \{q, p, r\}").to_edge(UP * 5 + LEFT * 3.5)

        self.play(Write(equal_set))
        self.wait(1)
        self.play(Write(equal_sets_desc))
        self.wait(1)
        self.play(Write(equal_sets_example))
        self.wait(1)

        # Step 1: Create Sets A and B
        set_A_circle = Circle(radius=1.5, color=BLUE, fill_opacity=0.3).shift(LEFT * 3.5 + DOWN*2)
        set_B_circle = Circle(radius=1.5, color=LIGHT_BROWN, fill_opacity=0.3).shift(RIGHT * 3 + DOWN*2)

        set_A_label = Tex(r"A = \{p, q, r\}").next_to(set_A_circle, UP)
        set_B_label = Tex(r"B = \{q, p, r\}").next_to(set_B_circle, UP)
        
        numbers_A = Tex("p , q , r").move_to(set_A_circle)
        numbers_B = Tex("q , p , r").move_to(set_B_circle)

        self.play(Create(set_A_circle), Write(set_A_label), Write(numbers_A))
        self.play(Create(set_B_circle), Write(set_B_label), Write(numbers_B))

        # Step 2: Show A ⊆ B
        subset_A_B = Tex(r"$A \subseteq B$").shift(LEFT * 0.2+DOWN * 2)
        self.play(Write(subset_A_B))
        self.wait(2)
        self.play(FadeOut(subset_A_B))

        # Step 3: Show B ⊆ A
        subset_B_A = Tex(r"$B \subseteq A$").shift(LEFT * 0.2+DOWN * 2)
        self.play(Write(subset_B_A))
        self.wait(2)
        self.play(FadeOut(subset_B_A))

        # Step 4: Conclude A = B
        equal_sets = Tex(r"$A = B$").shift(LEFT * 0.2+DOWN * 2)
        self.play(Write(equal_sets))

        self.wait(2)

        self.play(FadeOut(equal_sets), FadeOut(numbers_B), FadeOut(set_B_label), FadeOut(set_B_circle), FadeOut(numbers_A), FadeOut(set_A_label), FadeOut(set_A_circle), FadeOut(equal_sets_example), FadeOut(equal_sets_desc), FadeOut(equal_set))





        # Disjoint sets definition
        disjoint_set = Text("Disjoint Sets :", color=PURPLE).to_edge(UP * 1 + LEFT * 2.75)
        disjoint_sets_desc = Text("Sets with no common elements. Then there A ∩ B =  ∅  or { }", font_size=29).to_edge(UP * 3)

        # Example of disjoint sets in roster form
        disjoint_sets_example = MathTex(r"A = \{1, 3, 5, 7\}").to_edge(UP * 5 + LEFT * 3.5)
        disjoint_sets_example2 = MathTex(r"B = \{2, 4, 6, 8\}").to_edge(UP * 5 + RIGHT * 5)

        self.play(Write(disjoint_set))
        self.wait(1)
        self.play(Write(disjoint_sets_desc))
        self.wait(1)
        self.play(Write(disjoint_sets_example))
        self.wait(1)
        self.play(Write(disjoint_sets_example2))
        self.wait(1)

        # Step 1: Create Sets A and B
        set_A_circle = Circle(radius=1.5, color=LIGHT_GREY, fill_opacity=0.3).shift(LEFT * 3.5 + DOWN*2)
        set_B_circle = Circle(radius=1.5, color=LIGHT_BROWN, fill_opacity=0.3).shift(RIGHT * 3 + DOWN*2)

        set_A_label = Tex("A").next_to(set_A_circle, UP)
        set_B_label = Tex("B").next_to(set_B_circle, UP)
        
        numbers_A = Tex("1, 3, 5, 7").move_to(set_A_circle)
        numbers_B = Tex("2, 4, 6, 8").move_to(set_B_circle)

        self.play(Create(set_A_circle), Write(set_A_label), Write(numbers_A))
        self.play(Create(set_B_circle), Write(set_B_label), Write(numbers_B))

        # Display disjoint sets text
        disjoint_text_1 = Text("A ∩ B = ∅",font_size=30  ).shift(LEFT * 0.2+DOWN * 2)
        self.play(Write(disjoint_text_1))
        self.wait(1)

        self.play(FadeOut(disjoint_text_1), FadeOut(numbers_B), FadeOut(set_B_label), FadeOut(set_B_circle), FadeOut(numbers_A), FadeOut(set_A_label), FadeOut(set_A_circle), FadeOut(disjoint_sets_example2), FadeOut(disjoint_sets_example), FadeOut(disjoint_sets_desc), FadeOut(disjoint_set))




        finite = Text("Finite Set :",color=PINK).to_edge(UP*1+LEFT*2.75)
        sub_title1 = Text("A finite set is a set that contains a countable number of elements.",font_size=29).to_edge(UP*3)
        finite_elements1 = Tex(r"Example = \{1, 2, 3, 4, 5\}").shift(LEFT * 3).to_edge(UP*5+LEFT*3)

        # finite set f
        finite_set = Circle(radius=1.8, color=GRAY, fill_opacity=0.3).shift(DOWN*1.75)
        label_f = Tex("Finite set").next_to(finite_set, UP)

        # Numbers for finite set
        numbers_f = Tex("1, 2, 3, 4, 5").move_to(finite_set)
       
        self.play(Write(finite))
        self.wait(1)
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(finite_elements1))
        self.wait(1)

        self.play(Create(finite_set), Write(label_f))
        self.wait(1)

        self.play(Write(numbers_f))
        self.wait(1)

        self.play(FadeOut(numbers_f), FadeOut(label_f), FadeOut(finite_set), FadeOut(finite_elements1), FadeOut(sub_title1), FadeOut(finite))




        Infinite = Text("Infinite Set :",color=BLUE).to_edge(UP*0.8+LEFT*2.75)
        sub_title2 = Text("An infinite set contains an uncountable or endless number of elements.",font_size=27).to_edge(UP*3)
        finite_elements2 = Tex(r"Example :\{1, 2, 3, 4  \ldots\}").to_edge(UP*5+LEFT*3)

        # Infinite set f
        infinite_set = Circle(radius=1.8, color=LIGHT_BROWN, fill_opacity=0.3).shift(DOWN*1.75)
        label_if = Tex("Infinite set").next_to(infinite_set, UP)

        # Numbers for Infinite set
        numbers_if = Tex(r"1, 2, 3, 4,....").move_to(infinite_set)
       
        self.play(Write(Infinite))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)
        self.play(Write(finite_elements2))
        self.wait(1)

        self.play(Create(infinite_set), Write(label_if))
        self.wait(1)

        self.play(Write(numbers_if))
        self.wait(1)

        self.play(FadeOut(numbers_if), FadeOut(label_if), FadeOut(infinite_set), FadeOut(finite_elements2), FadeOut(sub_title2), FadeOut(Infinite))
       




    def BasicOperationsonSets(self):
        # Create the title
        title = Text("Basic Operations on Sets").to_edge(UP)

        # Create the LaTeX strings for operations

        union = Text("Basic Operations on Sets").to_edge(UP*1.25)
        sub_title1 = Text("1. Union of Sets = 'A U B '.",font_size=30).to_edge(UP*4.5)
        sub_title2 = Text("2. Intersection of Sets = ' A ∩ B '",font_size=30).to_edge(UP*7.5)
        sub_title3 = Text("3. Difference of sets = ' A - B '",font_size=30).to_edge(UP*10)

        self.play(Write(union))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)
        self.play(Write(sub_title3))
        
    def union_scene(self):

        union = Text("1. Union of Sets").to_edge(UP*1)
        sub_title1 = Text("Is a set that contains all the elements of set A,B,or both(without repetition).",font_size=29).to_edge(UP*3.5)
        sub_title2 = Text("The union of sets A and B, denoted by 'A U B '.",font_size=29).to_edge(UP*5.5)


        # Define sets
        set_A = {1, 2, 3}
        set_B = {3, 4, 5}

        # Venn diagrams (c1 for set A, c2 for set B)
        c1 = Circle(radius=1.5, color=BLUE, fill_opacity=0.5).shift(LEFT*5,DOWN*2)
        c2 = Circle(radius=1.5, color=RED, fill_opacity=0.5).shift(LEFT*1.5,DOWN*2)

        # Labels for sets
        label_A = Tex("A", color=BLUE).next_to(c1, UP)
        label_B = Tex("B", color=RED).next_to(c2, UP)

        # Union (c1 ∪ c2)
        union_label = Tex("$A \\cup B$", color=GREEN).shift(UP*0,RIGHT*3.5)
        union_c1 = Circle(radius=1.5, color=BLUE, fill_opacity=0.5).shift(RIGHT*2.5,DOWN*2)
        union_c2 = Circle(radius=1.5, color=RED, fill_opacity=0.4).shift(RIGHT*4.5,DOWN*2)

        self.play(Write(union))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))

        # Display initial sets
        self.play(Create(c1), Create(c2), Write(label_A), Write(label_B))
        self.wait(1)

        # Display Union
        self.play(Create(union_c1), Create(union_c2), Write(union_label))
        self.wait(2)

        # Clear previous animations
        self.play(FadeOut(union_c1), FadeOut(union_c2), FadeOut(union_label),FadeOut(label_B),FadeOut(label_A),FadeOut(c2),FadeOut(c1),FadeOut(sub_title2), FadeOut(sub_title1), FadeOut(union))
        self.wait(1)




        heading1= Text("Example :",color=WHITE).to_edge(UP*1+LEFT*2.75)
        sub_title2 = Text(" A = {1 , 2 , 3 , 4}} and B = {2 , 4 , 6 , 8}",font_size=32).to_edge(UP*3)
        finite_elements2 = Text("A U B = {1 , 2 , 3 , 4 , 2 , 4 , 6 , 8}",font_size=32).to_edge(UP*5)
        finite_elements3 = Text("A U B = {1 , 2 , 3 , 4 , 6 , 8}",font_size=32).to_edge(UP*7)
        
        self.play(Write(heading1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)
        self.play(Write(finite_elements2))
        self.wait(1)
        self.play(Write(finite_elements3))
        self.wait(1)

        # Define sets
        set_A = {1,2,3,4}
        set_B = {2,4,6,8}


        # Define circles for sets
        intersection_c1 = Circle(radius=1.5, color=PINK, fill_opacity=0.05).shift(LEFT*1 + DOWN*2)
        label_c1 = Tex("A", color=PINK, font_size=31).next_to(intersection_c1, UP)
        intersection_c2 = Circle(radius=1.5, color=ORANGE, fill_opacity=0.1).shift(RIGHT*1 + DOWN*2)
        label_c2 = Tex("B", color=ORANGE, font_size=31).next_to(intersection_c2, UP)

        # Intersection area
        intersection_area = Intersection(intersection_c1, intersection_c2, color=BLUE, fill_opacity=0.6)
        intersection_numbers = Tex("2, 4", color=BLACK, font_size=34).move_to(intersection_area)
        
        # A - (A ∩ B) area
        only_A_area = Difference(intersection_c1, intersection_area, color=BLUE, fill_opacity=0.4)
        numbers_only_A = Tex("1 , 3", color=WHITE, font_size=32).move_to(only_A_area)
        
        # B - (A ∩ B) area
        only_B_area = Difference(intersection_c2, intersection_area, color=BLUE, fill_opacity=0.4)
        numbers_only_B = Tex("6 , 8", color=WHITE, font_size=32).move_to(only_B_area)

        
        # Display the sets and their differences
        self.play(Create(intersection_c1), Create(label_c1))
        self.play(Create(intersection_c2), Create(label_c2))
        self.play(Create(only_A_area), Write(numbers_only_A))
        self.play(Create(only_B_area), Write(numbers_only_B))
        self.play(Create(intersection_area), Write(intersection_numbers))
        self.wait(2)



    def intersection_scene(self):

        union = Text("2. Intersection of Sets").to_edge(UP*1)
        sub_title1 = Text("Is a set that contains all the elements that are element of both And B.",font_size=29).to_edge(UP*3.5)
        sub_title2 = Text("The intersection of sets A and B, denoted by ' A ∩ B '.",font_size=29).to_edge(UP*5.5)

        self.play(Write(union))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))

        # Define sets
        set_A = {2,4,8,10,12}
        set_B = {3,6,9,12,15}

        # Venn diagrams (c1 for set A, c2 for set B)
        c1 = Circle(radius=1.5, color=BLUE, fill_opacity=0.5).shift(LEFT*5,DOWN*2)
        c2 = Circle(radius=1.5, color=RED, fill_opacity=0.5).shift(LEFT*1.5,DOWN*2)

        # Labels for sets
        label_A = Tex("A", color=BLUE).next_to(c1, UP)
        label_B = Tex("B", color=RED).next_to(c2, UP)

        # Display initial sets
        self.play(Create(c1), Create(c2), Write(label_A), Write(label_B))
        self.wait(1)


        # Define Intersection of A ∩ B
        intersection_c1 = Circle(radius=1.5, color=BLUE, fill_opacity=0.4).shift(RIGHT*2.5,DOWN*2)
        label_c1 = Tex("A", color=BLUE, font_size=31).next_to(intersection_c1, UP)
        intersection_c2 = Circle(radius=1.5, color=RED, fill_opacity=0.4).shift(RIGHT*4.5,DOWN*2)
        label_c2 = Tex("B", color=RED, font_size=31).next_to(intersection_c2, UP)

        # Intersection area
        intersection_area = Intersection(intersection_c1, intersection_c2, color=GRAY, fill_opacity=0.6)
        intersection_label = Tex("$A \\cap B$", color=BLACK,font_size=26).move_to(intersection_area)
        
        # A - (A ∩ B) area
        only_A_area = Difference(intersection_c1, intersection_area, color=BLUE, fill_opacity=0.3)
        
        # B - (A ∩ B) area
        only_B_area = Difference(intersection_c2, intersection_area, color=RED, fill_opacity=0.3)
    

        # Display the sets and their differences
        self.play(Create(intersection_c1), Create(label_c1))
        self.play(Create(intersection_c2), Create(label_c2))
        self.play(Create(only_A_area))
        self.play(Create(only_B_area))
        self.play(Create(intersection_area), Write(intersection_label))
        self.wait(2)

        # Clear previous animations
        self.play(FadeOut(intersection_label),FadeOut(intersection_area),FadeOut(only_B_area), FadeOut(only_A_area), FadeOut(label_c2), FadeOut(intersection_c2), FadeOut(label_c1), FadeOut(intersection_c1),FadeOut(label_B), FadeOut(label_A), FadeOut(c2), FadeOut(c1),FadeOut(sub_title2), FadeOut(sub_title1), FadeOut(union))
        self.wait(1)



        heading1= Text("Example :",color=WHITE).to_edge(UP*1+LEFT*2.75)
        sub_title2 = Text(" A = {2,4,6,8,10,12} and B = {3,6,9,12,15}",font_size=32).to_edge(UP*3)
        finite_elements2 = Text("A ∩ B = {6,12}",font_size=32).to_edge(UP*5)
        
        self.play(Write(heading1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)
        self.play(Write(finite_elements2))
        self.wait(1)

        # Define sets
        set_A = {2,4,8,10,12}
        set_B = {3,6,9,12,15}


        # Define circles for sets
        intersection_c1 = Circle(radius=1.5, color=PURPLE, fill_opacity=0.2).shift(LEFT*1 + DOWN*2)
        label_c1 = Tex("A", color=PURPLE, font_size=31).next_to(intersection_c1, UP)
        intersection_c2 = Circle(radius=1.5, color=BLUE, fill_opacity=0.2).shift(RIGHT*1 + DOWN*2)
        label_c2 = Tex("B", color=BLUE, font_size=31).next_to(intersection_c2, UP)

        # Intersection area
        intersection_area = Intersection(intersection_c1, intersection_c2, color=GRAY, fill_opacity=0.6)
        intersection_numbers = Tex("6, 12", color=BLACK, font_size=34).move_to(intersection_area)
        
        # A - (A ∩ B) area
        only_A_area = Difference(intersection_c1, intersection_area, color=PURPLE, fill_opacity=0.4)
        numbers_only_A = Tex("2,4,8,10", color=WHITE, font_size=32).move_to(only_A_area)
        
        # B - (A ∩ B) area
        only_B_area = Difference(intersection_c2, intersection_area, color=BLUE, fill_opacity=0.3)
        numbers_only_B = Tex("3,9,15", color=WHITE, font_size=32).move_to(only_B_area)

        
        # Display the sets and their differences
        self.play(Create(intersection_c1), Create(label_c1))
        self.play(Create(intersection_c2), Create(label_c2))
        self.play(Create(only_A_area), Write(numbers_only_A))
        self.play(Create(only_B_area), Write(numbers_only_B))
        self.play(Create(intersection_area), Write(intersection_numbers))
        self.wait(2)



    def difference_scene(self):

        union = Text("3. Difference of sets").to_edge(UP*1)
        sub_title1 = Text("Is a set that containing the elements of A that are not in B.",font_size=29).to_edge(UP*3.5)
        sub_title2 = Text("The difference of sets A and B, denoted by 'A - B '.",font_size=29).to_edge(UP*5.5)

        self.play(Write(union))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))

        # Define sets
        set_A = {1, 2, 3}
        set_B = {3, 4, 5}

        # Venn diagrams (c1 for set A, c2 for set B)
        c1 = Circle(radius=1.5, color=BLUE, fill_opacity=0.5).shift(LEFT*5,DOWN*2)
        c2 = Circle(radius=1.5, color=RED, fill_opacity=0.5).shift(LEFT*1.5,DOWN*2)

        # Labels for sets
        label_A = Tex("A", color=BLUE).next_to(c1, UP)
        label_B = Tex("B", color=RED).next_to(c2, UP)

        # Difference (c1 - c2)
        difference_label = Tex("$A - B$", color=ORANGE).shift(RIGHT*4 + DOWN*2.25)
        difference_c1 = Circle(radius=1.5, color=BLUE, fill_opacity=0.5).shift(RIGHT*4 + DOWN*2)
        difference_c2 = Circle(radius=1.5, color=RED, fill_opacity=0).shift(RIGHT*4 + DOWN*2)

        # Display initial sets
        self.play(Create(c1), Create(c2), Write(label_A), Write(label_B))
        self.wait(1)

        # Display Difference
        self.play(Create(difference_c1), Create(difference_c2), Write(difference_label))
        self.wait(2)

        # Clear previous animations
        self.play(FadeOut(difference_c1), FadeOut(difference_c2), FadeOut(difference_label), FadeOut(label_B), FadeOut(label_A), FadeOut(c2), FadeOut(c1), FadeOut(sub_title2), FadeOut(sub_title1), FadeOut(union))
        self.wait(1)
        


        heading1 = Text("Example :", color=WHITE).to_edge(UP * 1 + LEFT * 2.75)
        sub_title2 = Text(" A = {1,2,3,4,5} and B = {4,5,6,7}", font_size=32).to_edge(UP * 3)
        finite_elements2 = Text("A - B = {1,2,3,4,5} - {4,5,6,7}", font_size=32).to_edge(UP * 5 + LEFT * 1)
        finite_elements3 = Text("A - B = {1,2,3}", font_size=32).to_edge(UP * 7 + LEFT * 1)
        
        self.play(Write(heading1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)
        self.play(Write(finite_elements2))
        self.wait(1)
        self.play(Write(finite_elements3))
        self.wait(1)

        # Define sets
        set_A = {1, 2, 3, 4, 5}
        set_B = {4, 5, 6, 7}

        # Define circles for sets
        intersection_c1 = Circle(radius=1.5, color=BLUE, fill_opacity=0.3).shift(LEFT * 4 + DOWN * 2)
        label_c1 = Tex("A", color=BLUE, font_size=31).next_to(intersection_c1, UP)
        intersection_c2 = Circle(radius=1.5, color=GRAY, fill_opacity=0.1).shift(LEFT * 2 + DOWN * 2)
        label_c2 = Tex("B", color=GRAY, font_size=31).next_to(intersection_c2, UP)

        # Intersection area
        intersection_area = Intersection(intersection_c1, intersection_c2, color=GRAY, fill_opacity=0.1)
        intersection_numbers = Tex("4, 5", color=WHITE, font_size=34).move_to(intersection_area)

        # A - (A ∩ B) area
        only_A_area = Difference(intersection_c1, intersection_area, color=BLUE, fill_opacity=0.5)
        numbers_only_A = Tex("1, 2, 3", color=BLACK, font_size=34).move_to(only_A_area)

        # Numbers for intersection_c2
        numbers_c2 = Tex("6, 7", color=WHITE, font_size=32).move_to(intersection_c2)

        # Display the sets and their differences
        self.play(Create(intersection_c1), Create(label_c1))
        self.play(Create(intersection_c2), Create(label_c2))
        self.play(Create(only_A_area), Write(numbers_only_A))
        self.play(Create(intersection_area), Write(intersection_numbers))
        self.play(Write(numbers_c2))
        self.wait(2)

        finite_elements4 = Text("B - A = {4,5,6,7} - {1,2,3,4,5}", font_size=32).to_edge(UP * 5 + RIGHT * 1.5)
        finite_elements5 = Text("B - A = {6,7}", font_size=32).to_edge(UP * 7 + RIGHT* 4.5)

        self.play(Write(finite_elements4))
        self.wait(1)
        self.play(Write(finite_elements5))
        self.wait(1)

        # Define sets
        set_A = {1, 2, 3, 4, 5}
        set_B = {4, 5, 6, 7}

        # Define circles for sets
        intersection_c1 = Circle(radius=1.5, color=BLUE, fill_opacity=0.1).shift(RIGHT * 2.5 + DOWN * 2)
        label_c1 = Tex("A", color=BLUE, font_size=31).next_to(intersection_c1, UP)
        intersection_c2 = Circle(radius=1.5, color=GRAY, fill_opacity=0.2).shift(RIGHT * 4.5 + DOWN * 2)
        label_c2 = Tex("B", color=GRAY, font_size=31).next_to(intersection_c2, UP)

        # Intersection area
        intersection_area = Intersection(intersection_c1, intersection_c2, color=GRAY, fill_opacity=0.1)
        intersection_numbers = Tex("4, 5", color=WHITE, font_size=34).move_to(intersection_area)

        # Numbers for intersection_c1
        numbers_c1 = Tex("1, 2, 3", color=WHITE, font_size=32).move_to(intersection_c1)
        
        # B - (A ∩ B) area
        only_B_area = Difference(intersection_c2, intersection_area, color=GRAY, fill_opacity=0.5)
        numbers_only_B = Tex("6, 7", color=BLACK, font_size=32).move_to(only_B_area)

        # Display the sets and their differences
        self.play(Create(intersection_c1), Create(label_c1))
        self.play(Create(intersection_c2), Create(label_c2))
        self.play(Write(numbers_c1))
        self.play(Create(intersection_area), Write(intersection_numbers))
        self.play(Create(only_B_area), Write(numbers_only_B))
        self.wait(2)

    
    def GithubSourceCodeReference(self):
        self.colorChoice=[BLUE,PURPLE,ORANGE]
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
        p10=cvo.CVO().CreateCVO("Source code reference for the video","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("File Name","setoperations.py").setPosition([3.5,-1,0])
        p12=cvo.CVO().CreateCVO("Git hub URL","https://github.com/Skillbanc/manim-templates").setPosition([-3.5,-1,0]).setangle(-TAU/4)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p11.setcircleradius(1.5)
        p12.setcircleradius(3)
 
        self.construct1(p10,p10)
         
        #self.play()




if __name__ == "__main__":
    scene = SetOperations()
    scene.render()