from manim import *

class NumerationSystemTable(Scene):
    def construct(self):

        """# Title
        title = Text(" Place value of larger numbers", font_size=30,color=BLUE).to_edge(UP * 1)
        sub_title1 = Text("we can extend numbers upto lakhs and crores as seen in the following table:",font_size=29).to_edge(UP*2.75+LEFT*0.8)
        sub_title2 = Text("From the above table, the relation between numbers understood as follows:",font_size=27).to_edge(UP*11.25+LEFT*0.7)
        sub_title3 = Text("1 crore = 100 lakhs                           1 lakh = 100 thousands",font_size=27).to_edge(UP*13+LEFT*1.15)
        sub_title4 = Text("        =  10,000 thousands                     = 1000 hundreds",font_size=29).to_edge(UP* 14.5+  LEFT *3.5)
        

    
        # Table data
        headers = ["Places", "Ten Crores\n(T. Cr)", "Crores\n(Cr)", "Ten Lakhs\n(T. La)", "Lakhs\n(La)", "Ten Thousands\n(T. Th.)", "Thousands\n(Th.)", "Hundreds\n(H)", "Tens\n(T)", "Ones\n(O)"]
        row1 = ["Number", "10,00,00,000", "1,00,00,000", "10,00,000", "1,00,000", "10,000", "1,000", "100", "10", "1"]
        row2 = ["No. of Digits", "9", "8", "7", "6", "5", "4", "3", "2", "1"]

        # Combine headers and rows
        table_data = [headers, row1, row2]

        # Create the table
        table = Table(
            table_data,
            include_outer_lines=True,
            h_buff=0.8,
            v_buff=2.07,
            line_config={"stroke_width": 2}
        )

        # Scale the table and adjust position if needed
        table.scale(0.35).to_edge(UP* 4.1)



        self.play(Create(title))
        self.wait(2)
        self.play(Write(sub_title1))
        self.wait(2)
        self.play(Create(table))
        self.wait(4)
        self.play(Write(sub_title2))
        self.wait(2)
        self.play(Write(sub_title3))
        self.wait(3)
        self.play(Write(sub_title4))
        self.wait(3)
        
        



        self.play(FadeOut(sub_title2),FadeOut(sub_title1), FadeOut(sub_title4), FadeOut(sub_title3),FadeOut(table), FadeOut(title))"""

        
       

        

    
        # Table data
        headers = ["Number", "T. Cr", "Cr.", "T. La", "La", "T. Th","Th.", "H", "T", "O"]
        row1 = ["41430495", "-", "4", "1", "4", "3", "0", "4", "9", "5"]
       
        # Combine headers and rows
        table_data = [headers, row1]

        # Create the table
        table = Table(
            table_data,
            include_outer_lines=True,
            h_buff=0.8,
            v_buff=0.6,
            line_config={"stroke_width": 2}
        )

        # Scale the table and adjust position if needed
        table.scale(0.35).to_edge(UP* 4.1)



        """self.play(Create(title))
        self.wait(2)
        self.play(Write(sub_title1))
        self.wait(2)"""
        self.play(Create(table))
        """self.wait(4)
        self.play(Write(sub_title2))
        self.wait(2)
        self.play(Write(sub_title3))
        self.wait(3)
        self.play(Write(sub_title4))
        self.wait(3)"""
        
        



        """self.play(FadeOut(sub_title2),FadeOut(sub_title1), FadeOut(sub_title4), FadeOut(sub_title3),FadeOut(table), FadeOut(title)) """  
       
        

if __name__ == "__main__":
    scene = NumerationSystemTable()
    scene.render()