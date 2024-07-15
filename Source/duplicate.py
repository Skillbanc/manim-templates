from manim import *

class TableScene(Scene):
    def construct(self):
        self.Factorisation_by_grouping_the_terms()

    
       
    def Factorisation_by_grouping_the_terms(self):
        
        union = Text("Factorisation using identities:",color=DARK_BROWN).to_edge(UP*1.25)
        sub_title1 = Text("(a+b)² = a² + b² + 2ab",font_size=30).to_edge(UP*4.5)
        sub_title2 = Text("(a-b)² = a² + b² - 2ab",font_size=30).to_edge(UP*7.5)
        sub_title3 = Text("(a+b) (a-b) = a² - b²",font_size=30).to_edge(UP*10)
        sub_title4 = Text("We can use these identities for factorisation, if the given",font_size=30).to_edge(UP*12.75)
        sub_title5 = Text("given is in the form of RHS (RightHand Side) of the particular identity.",font_size=30).to_edge(UP*14.5+LEFT*1.25)

        # Create a surrounding rectangle for the subtitle and formula
        rect = SurroundingRectangle(VGroup(sub_title1, sub_title2,sub_title3), color=BLUE, buff=0.3)
        

        self.play(Write(union))
        self.wait(2)
        self.play(Write(sub_title1))
        self.wait(2)
        self.play(Write(sub_title2))
        self.wait(2)
        self.play(Write(sub_title3))
        self.wait(2)  
        self.play(Create(rect))
        self.wait(1)
        self.play(Write(sub_title4))
        self.wait(2)
        self.play(Write(sub_title5))
        self.wait(2)

        elements_to_fade = VGroup(sub_title1, sub_title2, sub_title3, sub_title4, sub_title5)
        self.play(FadeOut(elements_to_fade))
        self.wait(1)

        # Subtitles
        sub_title1 = Text("Example:", font_size=29, color=PINK).to_edge(UP + LEFT)
        sub_title2 = Text("Factorise 6ab - b² - 2bc + 12ac", font_size=27).next_to(sub_title1, RIGHT)
        sub_title3 = Text("Step 1: Check whether there are any common factors for all terms. Obviously none.", font_size=26).to_edge(UP*3 + LEFT)
        sub_title4 = Text("Step 2: On regrouping the first two terms we have", font_size=26).to_edge(UP*4.5 + LEFT)
        sub_title5 = Text("6ab - b² = b(6a - b) .............I", font_size=26).to_edge(UP*6 )
        sub_title6 = Text("We need to change the order of the last two terms in the expression", font_size=26).to_edge(UP*7.5 + LEFT*4)
        sub_title7 = Text("12ac - 2bc = 2c(6a - b) ............II", font_size=26).to_edge(UP*9)
        sub_title8 = Text("Step 3: Combining I and II together", font_size=26).to_edge(UP*10.5 + LEFT)
        sub_title9 = Text("6ab - b² - 2bc + 12ac = b(6a - b) + 2c(6a - b)", font_size=26).to_edge(UP*12 )
        sub_title10 = Text("(6a - b)(b + 2c)", font_size=26).to_edge(UP*13.5)
        sub_title11 = Text("Hence the factors of 6ab - b² - 2bc + 12ac are (6a - b) and (b + 2c)", font_size=26).to_edge(UP*14.8)

        # Set color for step numbers
        sub_title3[0:6].set_color(GREEN)  # Color "Step 1:" in green
        sub_title4[0:6].set_color(GREEN)  # Color "Step 2:" in green
        sub_title8[0:6].set_color(GREEN)  # Color "Step 3:" in green

        # Animation sequence

        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)
        self.play(Write(sub_title3))
        self.wait(1)
        self.play(Write(sub_title4))
        self.wait(1)
        self.play(Write(sub_title5))
        self.wait(1)
        self.play(Write(sub_title6))
        self.wait(1)
        self.play(Write(sub_title7))
        self.wait(1)
        self.play(Write(sub_title8))
        self.wait(1)
        self.play(Write(sub_title9))
        self.wait(1)
        self.play(Write(sub_title10))
        self.wait(1)
        self.play(Write(sub_title11))
        self.wait(2)

        # Fade out all elements
        elements_to_fade = VGroup(sub_title1, sub_title2, sub_title3, sub_title4, sub_title5, sub_title6, sub_title7, sub_title8, sub_title9, sub_title10, sub_title11)
        self.play(FadeOut(elements_to_fade))
        self.wait(1)






if __name__ == "__main__":
    scene = TableScene()
    scene.render()
