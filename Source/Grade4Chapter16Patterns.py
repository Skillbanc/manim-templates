from manim import *
from AbstractAnim import AbstractAnim
import cvo
class PatternAnimation(AbstractAnim):
    def construct(self):

        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.introduction()
        self.fadeOutCurrentScene()
        self.Patternsinnumbers()
        self.fadeOutCurrentScene()
        self.Patternswithturns()
        self.fadeOutCurrentScene()
        self.fadeOutCurrentScene()
        self.Patternsinthecalender()  
        self.fadeOutCurrentScene() 
        self.GithubSourceCodeReference()


        


    def introduction(self):
        self.setNumberOfCirclePositions(5)
        #self.angleChoice = [0,0,0]
        self.angleChoice = [TAU/4,TAU/4,TAU/4,TAU/4]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Patterns","Patterns are recurring sequences that can be observed in various contexts.").setPosition([-3,2.5,0])
        p11=cvo.CVO().CreateCVO("Types of Patterns","").setPosition([-2.25,-1,0])
        p12=cvo.CVO().CreateCVO("Patterns in numbers","").setPosition([2.75,1.8,0])
        p13=cvo.CVO().CreateCVO("Patterns with turns","").setPosition([4.5,-0.1,0])
        p14=cvo.CVO().CreateCVO("Patterns in the calendar","").setPosition([4,-3,0])

        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
        p11.cvolist.append(p14)  

        self.construct1(p10,p10)





    def Patternsinnumbers(self):

        heading = Text("Patterns in numbers",color=PINK,font_size=37).to_edge(UP*1.25)
        sub_title1 = Text("Recurring sequences or relationships observed in numerical data.",font_size=29).to_edge(UP*3)
        sub_title2 = Text("Identify the patterns in the series of numbers given below. ",font_size=29).to_edge(UP*5+LEFT*1)
        sub_title3 = Text("1.  What will be the next three numbers in these series of numbers ?",font_size=29).to_edge(UP*7+LEFT*1)
        heading2 = Text("(a)   2,  4,  6,  8, _____________",font_size=30).to_edge(UP*9+LEFT * 4)
        sub_title5 = Text("(b)   3,  6,  9,  12, _____________",font_size=30).to_edge(UP*10.75+LEFT * 4)
        sub_title6 = Text("(c)   11, 15, 19, 23, ____________ ",font_size=30).to_edge(UP*12.5+LEFT * 4)
        sub_title7 = Text("(d)  15, 13, 11, 9, _____________",font_size=30).to_edge(UP*13.75+LEFT * 4)
        sub_title8 = Text("10,  12,  14",font_size=30,color=BLUE).to_edge(UP*9+LEFT * 10)
        sub_title9 = Text("15,  18,  21",font_size=30,color=BLUE).to_edge(UP*10.75+LEFT * 10.5)
        sub_title10 = Text("27,  31,  35",font_size=30,color=BLUE).to_edge(UP*12.5+LEFT * 11)
        sub_title11 = Text("7,  5,  3",font_size=30,color=BLUE).to_edge(UP*13.75+LEFT * 10.75)
        
        self.play(Write(heading))
        self.wait(0.6)
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)
        self.play(Write(sub_title3))
        self.wait(1)
        self.play(Write(heading2))
        self.wait(1)
        self.play(Write(sub_title5))
        self.wait(1)
        self.play(Write(sub_title6))
        self.wait(1)
        self.play(Write(sub_title7))
        self.wait(1)
        self.play(Write(sub_title8))
        self.wait(2)
        self.play(Write(sub_title9))
        self.wait(2)
        self.play(Write(sub_title10))
        self.wait(2)
        self.play(Write(sub_title11))

         # Fade out all text objects
        self.play(FadeOut(heading),
                  FadeOut(sub_title1),
                  FadeOut(sub_title2),
                  FadeOut(sub_title3),
                  FadeOut(heading2),
                  FadeOut(sub_title5),
                  FadeOut(sub_title6),
                  FadeOut(sub_title7),
                  FadeOut(sub_title8),
                  FadeOut(sub_title9),
                  FadeOut(sub_title10),
                  FadeOut(sub_title11))
        self.wait(1)


        sub_title1 = Text("(e)   40,  35,  30,  25, _____________", font_size=29).to_edge(UP * 1.5 + LEFT * 4)
        sub_title2 = Text("(f)   3,  6, 10,  15, _____________", font_size=29).to_edge(UP * 3.25 + LEFT * 4)
        sub_title3 = Text("(g)   8,  16,  24,  32, _____________", font_size=29).to_edge(UP * 5 + LEFT * 4)
        heading2 = Text("(h)   49,  42,  35,  28, _____________", font_size=30).to_edge(UP * 6.75 + LEFT * 4)
        sub_title5 = Text("(i)   70,  60,  50,  40, _____________", font_size=30).to_edge(UP * 8.5 + LEFT * 4)
        sub_title6 = Text("(j)   9,  19,  29,  39, _____________", font_size=30).to_edge(UP * 10.25 + LEFT * 4)
        sub_title7 = Text("(k)   4,  8,  16,  32, _____________", font_size=30).to_edge(UP * 12 + LEFT * 4)
        sub_title8 = Text("(l)   36,  45,  54,  63, _____________", font_size=30).to_edge(UP * 13.75 + LEFT * 4)
        sub_title9 = Text("20,  15,  10", font_size=30, color=BLUE).to_edge(UP * 1.5 + LEFT * 11.9)
        sub_title10 = Text("21,  28,  36", font_size=30, color=BLUE).to_edge(UP * 3.25 + LEFT * 10.5)
        sub_title11 = Text("40,  48,  56", font_size=30, color=BLUE).to_edge(UP * 5 + LEFT * 11.4)
        sub_title12 = Text("21,  14,  7", font_size=30, color=BLUE).to_edge(UP * 6.75 + LEFT * 12.25)
        sub_title13 = Text("30,  20,  10", font_size=30, color=BLUE).to_edge(UP * 8.5 + LEFT * 11.85)
        sub_title14 = Text("49,  59,  69", font_size=30, color=BLUE).to_edge(UP * 10.25 + LEFT * 11.45)
        sub_title15 = Text("64,  128,  256", font_size=30, color=BLUE).to_edge(UP * 12 + LEFT * 11.2)
        sub_title16 = Text("72,  81,  90", font_size=30, color=BLUE).to_edge(UP * 13.75 + LEFT * 11.85)

        # List of all text objects
        texts_to_fade_out = [
            sub_title1, sub_title2, sub_title3, heading2, sub_title5,
            sub_title6, sub_title7, sub_title8, sub_title9, sub_title10,
            sub_title11, sub_title12, sub_title13, sub_title14, sub_title15, sub_title16
        ]

        # Write all text objects
        for text in texts_to_fade_out:
            self.play(Write(text))
            self.wait(1)

        self.wait(2)

        # Fade out all text objects
        self.play(*[FadeOut(text) for text in texts_to_fade_out])
        self.wait(1)





    def Patternswithturns(self):

        heading = Text("Patterns with turns",color=PINK,font_size=37).to_edge(UP*1.25)
        sub_title1 = Text("Patterns in turns involve identifying sequences and rules in the ",font_size=29).to_edge(UP*3)
        sub_title2 = Text("rotational movement of shapes or objects.",font_size=29).to_edge(UP*5+LEFT*5)
        sub_title3 = Text("1.   Carry forward these patterns.",font_size=29).to_edge(UP*7+LEFT*1)
        heading2 = Text("(a)",font_size=30).to_edge(UP*10.25 +LEFT*1)
        
        self.play(Write(heading))
        self.wait(0.6)
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)
        self.play(Write(sub_title3))
        self.wait(1)
        
 
        # Create four triangles with increased gap
        triangle1 = Polygon(UP, DOWN + LEFT, DOWN + RIGHT).to_edge(UP*9+LEFT*4)
        triangle2 = triangle1.copy().shift(RIGHT * 3.5).to_edge(UP*9+LEFT*9)
        triangle3 = triangle1.copy().shift(RIGHT * 7).to_edge(UP*9+LEFT*16)
        triangle4 = triangle1.copy().shift(RIGHT * 10.5).to_edge(UP*9+LEFT*22)

        # Create small dots with slight offset for triangles 2 and 3
        dot1 = Dot(triangle1.get_vertices()[0] + UP * 0.3)
        dot2 = Dot(triangle2.get_vertices()[2] + RIGHT * 0.6 + DOWN * 0.2 + LEFT * 0.4)
        dot3 = Dot(triangle3.get_vertices()[1] + LEFT * 0.6 + DOWN * 0.2 + RIGHT * 0.4)
        dot4 = Dot(triangle4.get_vertices()[0] + UP * 0.3)

        # Animation sequence
        self.play(FadeIn(triangle1), FadeIn(dot1))
        self.wait(0.5)
        self.play(FadeIn(triangle2), FadeIn(dot2))
        self.wait(2)
        self.play(FadeIn(triangle3), FadeIn(dot3))
        self.wait(1)
        self.play(FadeIn(triangle4), FadeIn(dot4))
        self.wait(1)
        self.play(FadeOut(triangle1, dot1, triangle2, dot2, triangle3, dot3, triangle4, dot4,sub_title1, heading2,sub_title3,sub_title2,sub_title1,heading))


       
        sub_title1 = Text("(b)", font_size=29).to_edge(UP*3+LEFT*1)
        self.play(Write(sub_title1))
        self.wait(1)
        

        up_arrow = Arrow(start=DOWN, end=UP,color=PINK)
        down_arrow = Arrow(start=UP, end=DOWN,color=PINK)

        # Position arrows
        first_arrow = up_arrow.copy().to_edge(UP*3 +LEFT*5.5)
        second_arrow = down_arrow.copy().next_to(first_arrow, RIGHT, buff=1)
        third_arrow = up_arrow.copy().next_to(second_arrow, RIGHT, buff=1)
        fourth_arrow = down_arrow.copy().next_to(third_arrow, RIGHT, buff=1)

        # Create animation
        self.play(FadeIn(first_arrow))
        self.wait(0.5)
        self.play(FadeIn(second_arrow))
        self.wait(2)
        self.play(FadeIn(third_arrow))
        self.wait(1)
        self.play(FadeIn(fourth_arrow))
        self.wait(1)
        self.play(FadeOut(first_arrow, second_arrow, third_arrow, fourth_arrow,sub_title1))

    



        sub_title2 = Text("(C)", font_size=29).to_edge(UP*9+LEFT*1)
        self.play(Write(sub_title2))
        self.wait(1)

        circle = Circle(color=BLUE)
        circle1 = circle.copy().to_edge(UP*9+LEFT*4.5)  
        circle2 = circle.copy().to_edge(UP*9+LEFT*10.5)  
        circle3 = circle.copy().shift(RIGHT * 2.25).to_edge(UP*9+LEFT*17)  
        circle4 = circle.copy().shift(RIGHT * 4.5).to_edge(UP*9+LEFT*23)    

        up_arrow = Arrow(circle1.get_center(), circle1.get_top(), buff=0)
        right_arrow = Arrow(circle2.get_center(), circle2.get_right(), buff=0)
        down_arrow = Arrow(circle3.get_center(), circle3.get_bottom(), buff=0)
        left_arrow = Arrow(circle4.get_center(), circle4.get_left(), buff=0)

        pattern_f = VGroup(circle1, up_arrow)
        pattern_s = VGroup(circle2, right_arrow)
        pattern_t = VGroup(circle3, down_arrow)
        pattern_fo = VGroup(circle4, left_arrow)

        self.play(FadeIn(pattern_f))
        self.wait(1)

        self.play(FadeIn(pattern_s))
        self.wait(1)

        self.play(FadeIn(pattern_t))
        self.wait(1)

        self.play(FadeIn(pattern_fo))
        self.wait(1)

        self.play(FadeOut(pattern_f, pattern_s, pattern_t, pattern_fo,sub_title2))
        self.play(FadeOut(first_arrow, second_arrow, third_arrow, fourth_arrow,sub_title1))
        self.wait(1)

    
    def Patternsinthecalender(self):
        heading = Text("Patterns in the calendar",color=PINK,font_size=37).to_edge(UP*1)
        sub_title1 = Text("Patterns in calendars are recurring cycles of days, weeks,",font_size=28).to_edge(UP*3)
        sub_title2 = Text(" months, and years used to track time.",font_size=28).to_edge(UP*4.5)
        sub_title3 = Text("example:",font_size=28,color=BLUE).to_edge(UP*7+LEFT*1)
        sub_title4 = Text("Choose any 5 numbers as shown in the calendar",font_size=28).to_edge(UP*8.5+LEFT*1.2)
        sub_title5 = Text("What is their sum?",font_size=28).to_edge(UP*10+LEFT*2.25)
        sub_title6 = Text("2 + 9 + 16 + 23 + 30 = 80",font_size=28).to_edge(UP*11.5+LEFT*2.25)
        sub_title7 = Text("we can do it faster by simply multiply the middle",font_size=28).to_edge(UP*13+LEFT*1.2)
        sub_title8 = Text("number by 9 and get the answer- 9 x 21 = 189",font_size=28).to_edge(UP*14.5+LEFT*1.2)

        self.play(Write(heading))
        self.wait(0.8)
        self.play(Write(sub_title1))
        self.wait(0.5)
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
        self.wait(0.5)
        self.play(Write(sub_title8))
        self.wait(1)


        table_data = [
            ["S", "M", "T", "W", "Th", "F", "Sa"],
            ["", "", "", "1", "2", "3", "4"],
            ["5", "6", "7", "8", "9", "10", "11"],
            ["12", "13", "14", "15", "16", "17", "18"],
            ["19", "20", "21", "22", "23", "24", "25"],
            ["26", "27", "28", "29", "30", "31", ""], 
        ]

        # Create the table with the title
        table = Table(
            table_data,
            include_outer_lines=True,
            h_buff=0.35,
            v_buff=0.3
        )
    
        # Change the color of the table lines to blue
        table.get_horizontal_lines().set_color(BLUE)
        table.get_vertical_lines().set_color(BLUE)

        # Change the color of the headings to pink
        for i in range(1, 8):
            table.get_entries((1, i)).set_color(PINK)

        # Position the table at the specific location
        table.scale(0.6)
        table.to_edge(UP*7.5 + RIGHT*3)

        # Play the title and table together
        self.play(Create(table.get_horizontal_lines()), Create(table.get_vertical_lines()))
        self.wait(1)

        # Sequentially play each cell in the table
        for row in table.get_entries():
            for cell in row:
                self.play(FadeIn(cell))
                self.wait(0.004)

        self.wait(2)

        # Create and add a surrounding rectangle for the specific entries
        entries_to_highlight = [(2, 5), (3, 5), (4, 5), (5, 5), (6, 5)]
        cells = VGroup(*[table.get_entries(entry) for entry in entries_to_highlight])
        combined_rect = SurroundingRectangle(cells, color=YELLOW, buff=0.12)
        self.play(Create(combined_rect))
  
        self.wait(2)

        

    
    
        self.wait(2)
    def SetDeveloperList(self): 
       self.DeveloperList="Raghu" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade4Chapter16Patterns.py" 
    
    
    

if __name__ == "__main__":
    scene = PatternAnimation()
    scene.render()
