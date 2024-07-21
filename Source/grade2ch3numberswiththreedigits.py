from AbstractAnim import AbstractAnim
from manim import *
import cvo

class numberswiththreedigits(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.introduction()
        self.fadeOutCurrentScene()
        self.Add()
        self.fadeOutCurrentScene()
        self.expansion()
        self.fadeOutCurrentScene()
        self.numbers()
        self.fadeOutCurrentScene()
        self.game()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()


    def introduction(self):
        self.isRandom = False
        t1 = Text("Chapter 3 : Numbers with three digits", font_size=35)
        t1.move_to([0, 0, 0])
        # Write the text and the underline
        self.play(Write(t1))
        self.wait(2)
        self.play(FadeOut(t1))
        
        p10 = cvo.CVO().CreateCVO("three digit number", "")
        p12 = cvo.CVO().CreateCVO("Definition", "A three-digit number is a number that consists of exactly three digits.").setPosition([0,2.3,0])
        p11 = cvo.CVO().CreateCVO("Range", "It ranges from 100 to 999.").setPosition([3,-1.5,0])
        p10.cvolist.append(p12)
        p10.cvolist.append(p11)
        self.setNumberOfCirclePositions(3)
        self.construct1(p10, p10)
        self.wait(2)
    
    def Add(self):
        title = MarkupText("Observe the place, place value and face value of the digits in 746", font_size=26).to_edge(UP * 1.5 + LEFT * 3)
        
        self.play(Write(title))
        self.wait(1)

        table_data = [
            ["Number",  "7", "4", "6"],
            ["Position", "hundreds", "tens", "ones"],
            ["Place Value", "7 × 100 = 700", "4 × 10 = 40", "6 × 1 = 6"],
            ["Face Value", "7", "4", "6"],
        ]
        
        # Create the table with the title
        table = Table(
            table_data,
            include_outer_lines=True,
            h_buff=1.5,
            v_buff=1
        )
        
        # Change the color of the headings to pink
        for i in range(1, 5):
            table.get_entries((i, 1)).set_color(PINK)

        # Position the table at the center of the scene
        table.scale(0.6)
        table.move_to(ORIGIN)

        # Play the title and table together
        self.play(Create(table.get_horizontal_lines()), Create(table.get_vertical_lines()))
        self.wait(1)

        # Sequentially play each cell in the table
        for row in table.get_entries():
            for cell in row:
                self.play(FadeIn(cell))
                self.wait(0.5)

        self.wait(1)


    def expansion(self):
        table_data =[
            ["Number", "Expansion", "In words"],
            ["175", "100 + 70 + 5", "One hundred seventy-five"],
            ["782", "700 + 80 + 2", "Seven hundred eighty-two"],
            ["986", "900 + 80 + 6", "Nine hundred eighty-six"],
            ["407", "400 + 0 + 7", " Four hundred seven"],
            ["340", "300 + 40 + 0", "Three hundred forty"],
            ["999", "900 + 90 + 9", "Nine hundred ninety-nine"],
        ]

        # Create the table with the title
        table = Table(
            table_data,
            include_outer_lines=True,
            h_buff=1.2,
            v_buff=0.7
        )
        
        # Change the color of the headings to pink
        table.get_entries((1, 1)).set_color(BLUE)
        table.get_entries((1, 2)).set_color(BLUE)
        table.get_entries((1, 3)).set_color(BLUE)

        # Position the table at the center of the scene
        table.scale(0.6)
        table.move_to(ORIGIN)

        # Add the title
        title = Text("Expand the given numbers and write each one in words.", font_size=30,color="")
        title.next_to(table, UP * 1.25)

        # Play the title and table together
        self.play(Write(title), Create(table.get_horizontal_lines()), Create(table.get_vertical_lines()))
        self.wait(1)

        # Sequentially play each cell in the table
        for row in table.get_entries():
            for cell in row:
                self.play(FadeIn(cell))
                self.wait(0.5)

        self.wait(2)

    def numbers(self):
        # Title
        t1 = Text("Observe the numbers and write the next 5 numbers for each series.", font_size=27,color=PINK).to_edge(UP * 1+LEFT*1)
        self.play(Write(t1))
        self.wait(1)

        # Series with blanks
        sub_title1 = Text("100,  200,  300,_____________________ ", font_size=29).to_edge(UP * 3.5 + LEFT * 4)
        sub_title2 = Text("110,  120,  130,______________________  ", font_size=29).to_edge(UP * 5.75 + LEFT * 4)
        sub_title3 = Text("350,  400,  450,_____________________  ", font_size=29).to_edge(UP * 8 + LEFT * 4)
        heading2 = Text("400,  425,  450,_____________________  ", font_size=30).to_edge(UP * 10.25 + LEFT * 4)
        sub_title5 = Text("900,  800,  700,_____________________", font_size=30).to_edge(UP * 12.5 + LEFT * 4)


        # Series with answers (positions adjusted to match underscores)
        sub_title1_answer = Text("400,  500,  600,  700,  800", font_size=29, color=BLUE).to_edge(UP * 3.25 + LEFT * 9.75)
        sub_title2_answer = Text("140,  150,  160,  170,  180", font_size=29, color=BLUE).to_edge(UP * 5.55 + LEFT * 9.65)
        sub_title3_answer = Text("500,  550,  600,  650,  700", font_size=29, color=BLUE).to_edge(UP * 7.75 + LEFT * 9.9)
        heading2_answer = Text("475,  500,  525,  550,  575", font_size=29, color=BLUE).to_edge(UP * 10 + LEFT * 10)
        sub_title5_answer = Text("600,   500,  400,  300,  200", font_size=29, color=BLUE).to_edge(UP * 12.25 + LEFT * 10)

        
        # List of all text objects
        texts_to_write = [
            sub_title1, sub_title2, sub_title3, heading2, sub_title5
        ]
        
        # Write all text objects
        for text in texts_to_write:
            self.play(Write(text))
            self.wait(1)

        self.wait(2)

        # "ADD 100" text positioned to the right of the first series
        add_100_text = Text("Add 100 each time", font_size=22, color=GREEN).next_to(sub_title1, RIGHT*2.5)
        # Write the answers individually
        self.play(Write(add_100_text))
        self.wait(1)
        # Fade out the "ADD 100" text
        self.play(FadeOut(add_100_text))
        self.wait(1)
        # Write the answers individually
        self.play(Write(sub_title1_answer))
        self.wait(1)

        add_100_text1 = Text("Add 10 each time", font_size=22, color=GREEN).next_to(sub_title2, RIGHT*2.5)
        self.play(Write(add_100_text1))
        self.wait(1)
        # Fade out the "ADD 100" text
        self.play(FadeOut(add_100_text1))
        self.wait(1)
        self.play(Write(sub_title2_answer))
        self.wait(1)

        add_100_text2 = Text("Add 50 each time", font_size=22, color=GREEN).next_to(sub_title3, RIGHT*2.5)
        self.play(Write(add_100_text2))
        self.wait(1)
        # Fade out the "ADD 100" text
        self.play(FadeOut(add_100_text2))
        self.wait(1)
        self.play(Write(sub_title3_answer))
        self.wait(1)

        add_100_text3 = Text("Add 25 each time", font_size=22, color=GREEN).next_to(heading2, RIGHT*2.5)
        self.play(Write(add_100_text3))
        self.wait(1)
        # Fade out the "ADD 100" text
        self.play(FadeOut(add_100_text3))
        self.wait(1)
        self.play(Write(heading2_answer))
        self.wait(1)

        add_100_text4 = Text("subtract 100 each time", font_size=22, color=GREEN).next_to(sub_title5, RIGHT*2.5)
        self.play(Write(add_100_text4))
        self.wait(1)
         # Fade out the "ADD 100" text
        self.play(FadeOut(add_100_text4))
        self.wait(1)
        self.play(Write(sub_title5_answer))
        self.wait(1)

    
    def game(self):
        # Title
        title = Text("Play a game with sticks.", font_size=31, color=BLUE).to_edge(UP * 1+LEFT*1)
        sub_title1 = Text("1 long stick        =  100", font_size=26).to_edge(UP * 3+ LEFT*4)
        sub_title2 = Text("1 medium stick  =  10", font_size=26).to_edge(UP * 4.75+ LEFT*4)
        sub_title3 = Text("1 short stick      =  1", font_size=26).to_edge(UP * 6.5 + LEFT*4)


        self.play(Write(title))
        self.wait(2)
    
        # Create vertical lines representing the different stick values
        long_line = Line(start=ORIGIN, end=UP * 2.75, color=PINK).to_edge(RIGHT * 11.5 + UP *2)
        medium_line = Line(start=ORIGIN, end=UP * 1.75, color=GREEN).to_edge(RIGHT * 9.5+ UP *4)
        short_line = Line(start=ORIGIN, end=UP * 0.75, color=RED).to_edge(RIGHT * 7.5+ UP *6)


        # Create labels for the lines
        long_label = Text("100", font_size=24).next_to(long_line, DOWN)
        medium_label = Text("10", font_size=24).next_to(medium_line, DOWN)
        short_label = Text("1", font_size=24).next_to(short_line, DOWN)
   
        # Display the lines and labels

        self.play(Write(sub_title1))
        self.wait(0.7)
        self.play(Create(long_line), Write(long_label))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(0.7)
        self.play(Create(medium_line), Write(medium_label))
        self.wait(1)
        self.play(Write(sub_title3))
        self.wait(0.7)
        self.play(Create(short_line), Write(short_label))
        self.wait(1)


        table_data = [
            ["Big sticks",  "Medium sticks", "Short sticks", "The number formed"],
            ["4", "6", "5", "400 + 60 + 5 = 465"],
            ["7", "8", "2", "700 + 80 + 2 = 782"],
            ["5", "4", "3", "500 + 40 + 3 = 543"],
            ["1", "2", "7", "100 + 20 + 7 = 127"]
        ]
        
        # Create the table with the title
        table = Table(
            table_data,
            include_outer_lines=True,
            h_buff=1.2,
            v_buff=0.4
        )
        
        # Change the color of the headings to pink
        table.get_entries((1, 1)).set_color(GOLD)
        table.get_entries((1, 2)).set_color(GOLD)
        table.get_entries((1, 3)).set_color(GOLD)
        table.get_entries((1, 4)).set_color(GOLD)

        # Position the table at the center of the scene
        table.scale(0.6)
        table.to_edge(UP*9.5, buff=0.5)


        # Play the title and table together
        self.play(Create(table.get_horizontal_lines()), Create(table.get_vertical_lines()))
        self.wait(1)

        # Sequentially play each cell in the table
        for row in table.get_entries():
            for cell in row:
                self.play(FadeIn(cell))
                self.wait(0.5)

        self.wait(2)

    
    def SetDeveloperList(self):  
        self.DeveloperList="Akshitha"

        
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="numberswiththreedigits.py"


if __name__ == "__main__":
    from manim import *
    scene = numberswiththreedigits()
    scene.render()