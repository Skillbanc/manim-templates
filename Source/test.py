from manim import *

class MoveImageeee(Scene):
    def construct(self):


        """union = Text("Estimating And Comaring Numbers",color=PURPLE_B,font_size=37).to_edge(UP*1)
        sub_title1 = Text("Identify the greatest and smallest among the following numbers .",font_size=28).to_edge(UP*3+LEFT*1)
        sub_title2 = Text("We can identify them easily by simply counting the digits in the numbers.",font_size=28).to_edge(UP*11+LEFT *1)
        sub_title3 = Text("For example,",font_size=28,color=YELLOW).to_edge(UP*12.5+LEFT*1)
        sub_title4 = Text("The numbers having five digits are greater than numbers having two digit.",font_size=28).to_edge(UP*14+LEFT*1)
        

        
        #We can identify them easily by simply counting the digits in the numbers.



        # Table data
        headers = ["S.No.", "Numbers", "Greatest Number", "Smallest Number"]
        row1 = ["1", " 3845, 485, 34, 13845", " 13845", "34"]
        row2 = ["2", " 856, 1459, 35851, 23", "35851", "23"]
        row3 = ["3", " 39, 748, 19651, 7850", "19651", "39"]

        # Combine headers and rows
        table_data = [headers, row1, row2, row2]

        # Create the table
        table = Table(
            table_data,
            include_outer_lines=True,
            h_buff=1,
            v_buff=1.5,
            line_config={"stroke_width": 2}
        )

        # Scale the table and adjust position if needed
        table.scale(0.35).to_edge(UP* 4.5)


        self.play(Write(union))
        self.wait(2)
        self.play(Write(sub_title1))
        self.wait(2)
        self.play(Write(sub_title2))
        self.wait(2)
        self.play(Write(sub_title3))
        self.wait(2)
        self.play(Write(sub_title4))
        self.wait(2)
        self.play(Create(table))
        self.wait(4)




        self.play(FadeOut(sub_title2),FadeOut(sub_title1), FadeOut(sub_title4), FadeOut(sub_title3),FadeOut(table), FadeOut(union))"""


       

    def difference_scene(self):    
        heading = Text("Example: 585, 9535, 9678, 44",color=DARK_BROWN,font_size=37).to_edge(UP*1.25+LEFT * 2)
        sub_title1 = Text("Step 1: number of digits of given numbers are : 3 , 4, 4, 2 ",font_size=29).to_edge(UP*3+LEFT *1)
        sub_title2 = Text("so the number 44 is smallest number because it has less number of digits(2).",font_size=29).to_edge(UP*4.75)
        sub_title3 = Text("Case 1: if the numbers of digits of a given numbers are same,",font_size=29).to_edge(UP*6.25+LEFT *1)
        sub_title4 = Text("then start comparing first digit from left side of a given numbers",font_size=29).to_edge(UP*8)
        sub_title5 = Text("from numbers 9535 and 9635 comparing first digits from left 9 > 9",font_size=29).to_edge(UP*9.5)
        sub_title6 = Text("Case 2: if the first digit from left side are same then comare with next digit",font_size=29).to_edge(UP*11.25+LEFT * 1)
        sub_title7 = Text("from numbers 9535 and 9635 comparing second digit from left 5 < 6 ",font_size=29).to_edge(UP*12.75)
        sub_title8 = Text("so the number 9535 < 9635. so the greatest nuber is 9635.",font_size=29).to_edge(UP*14.5+LEFT * 1)
       

        self.play(Write(heading))
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
        self.play(FadeOut(sub_title8), FadeOut(sub_title7), FadeOut(sub_title6), FadeOut(sub_title5), FadeOut(sub_title4), FadeOut(sub_title3), FadeOut(sub_title2), FadeOut(sub_title1),FadeOut(heading))










 
# To render the scene
if __name__ == "__main__":
    scene = MoveImageeee()
    scene.render()
