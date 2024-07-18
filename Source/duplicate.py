from manim import *
import cvo
from AbstractAnim import AbstractAnim

class TableScene(AbstractAnim):
    def construct(self):
        #self.Patternsinthecalender()
        self.introduction()
        #self.SquareandSquareroot_table()


    def introduction(self):
        self.setNumberOfCirclePositions(5)
        #self.angleChoice = [0,0,0]
        self.angleChoice = [TAU/4,TAU/4,TAU/4,TAU/4]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Patterns","Patterns are recurring sequences that can be observed in various contexts.").setPosition([-3,2.5,0])
        p11=cvo.CVO().CreateCVO("Types of Patterns","").setPosition([-2.25,-1,0])
        p12=cvo.CVO().CreateCVO("Patterns in numbers","").setPosition([2.75,2.1,0])
        p13=cvo.CVO().CreateCVO("Patterns with turns","").setPosition([4.25,-0.2,0])
        p14=cvo.CVO().CreateCVO("Patterns in the calendar","").setPosition([3.4,-3,0])

        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
        p11.cvolist.append(p14)  

        self.construct1(p10,p10)



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

    
    def SquareandSquareroot_table(self):

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
            h_buff=0.8,
            v_buff=0.3
        )
        

        # Change the color of the table lines to blue
        table.get_horizontal_lines().set_color(BLUE)
        table.get_vertical_lines().set_color(BLUE)

        # Change the color of the headings to pink
        table.get_entries((1, 1)).set_color(PINK)
        table.get_entries((1, 2)).set_color(PINK)
        table.get_entries((1, 3)).set_color(PINK)
        table.get_entries((1, 4)).set_color(PINK)
        table.get_entries((1, 5)).set_color(PINK)
        table.get_entries((1, 6)).set_color(PINK)
        table.get_entries((1, 7)).set_color(PINK)


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

        self.wait(2)




if __name__ == "__main__":
    scene = TableScene()
    scene.render()
