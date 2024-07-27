# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla

from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo


class Grade4chapter13Smarttables(AbstractAnim):
    
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.Title()
        self.fadeOutCurrentScene()
        self.t1()
        self.fadeOutCurrentScene()
        self.t2()
        self.fadeOutCurrentScene()
        self.ques1()
        self.fadeOutCurrentScene()        
        self.t3()
        self.fadeOutCurrentScene()
        self.questions()
        self.fadeOutCurrentScene()
        self.t4()
        self.fadeOutCurrentScene()
        self.t5()
        self.fadeOutCurrentScene()
        self.toys()
        self.fadeOutCurrentScene()
        self.question7()
        self.fadeOutCurrentScene()
        self.h1()
        self.fadeOutCurrentScene()
        self.coin()
        self.fadeOutCurrentScene()
        self.question8()
        self.fadeOutCurrentScene()
        self.paddy()
        self.fadeOutCurrentScene()
        self.question5()
        self.fadeOutCurrentScene()
        self.box()
        self.fadeOutCurrentScene()
        self.question()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        







    def Title(self):
        # Title
        title = Text("Smart tables ", font_size=86)
        self.play(Write(title))
        self.wait(4)
        self.play(Unwrite(title))
        self.wait(2)



    
    def t1(self):
        # Create the table
        table = Table(
            [["Akhila", "A", "Sonia", "C","Uday","B","Sarala","A"],
             ["Raju", "A", "Gopi", "B", "Ani", "A", "Urmila", "B"],
             ["Amzad", "C", "Leela", "B", "Deepthi", "B", "Ramesh","B"],
             ["Vinay", "B", "Shameen", "A", "Sruthi", "C", "Srinu", "A"],
             ["Hampi", "A", "Pragna", "C", "Roja", "B", "Prasad", "B"],
             ["Rani", "B", "Fahim", "A", "Mangala", "A", "Kamala", "B"],
             ["Krishna", "A", "Komal", "B", "Kalpana", "B", "John", "C"],             
        #    #  ["+", "", "", "", "", "", "", "", "", "", ""],
        #      ["Table 3", "3", "6", "9", "12", "15", "18", "21", "24", "27", "30"],
        #      ["", "", "", "", "", "", "", "", "", "", ""],
        #      ["Table 5", "5", "10", "15", "20", "25", "30", "35", "40", "45", "50"],
        #      ["Table 1  +", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
        #    #  ["+", "", "", "", "", "", "", "", "", "", ""],
            #   ["Table 6", "6", "12", "18", "24", "30", "36", "42", "48", "54", "60"]
              ],
            include_outer_lines=True
        )
        
        # Style the table
        table.scale(0.5)  # Adjust scale as needed
        table.set_column_colors(BLUE, WHITE, BLUE, WHITE, BLUE, WHITE, BLUE, WHITE, WHITE, WHITE, WHITE)
        
        # Add the title
        title = Text("Class teacher has written the grades of her Class 4 students in the register...", 
                     color=YELLOW).scale(0.63)
        title.next_to(table, UP)

        
        # Create the scene
        self.play(Write(title))
        self.wait(2)
        self.play(Create(table))
        self.wait(15)

    


    def t2(self):
        # Create the table
        table = Table(
            [["Grade", "Tally Marks", "Number of students"],
             ["A", " |||||  |||||", "10"],
             ["B", "|||||  |||||  |||", "13"],
             ["C", "|||||", "5"],
                          
       
              ],
            include_outer_lines=True
        )
        
        # Style the table
        table.scale(0.8)  # Adjust scale as needed
        table.set_row_colors(YELLOW)
        
        # Add the title
        title = Text("The information is written from the given table. ", 
                     color=BLUE).scale(0.9)
        title.next_to(table, UP)

        
        # Create the scene
        self.play(Write(title))
        self.wait(2)
        self.play(Create(table))
        self.wait(5)

    def ques1(self):

         # Add the title
        q1 = Text("(a) How many children got A grade? ",   color=WHITE).scale(0.65)
        q1.to_edge( UP*2.5)

        
        # Create the scene
        self.play(Write(q1))
        self.wait(2)
        
        a = Text("  Answer:   Ten ", color=BLUE).scale(0.7)
        a.to_edge( UP*3.6)

        
        # Create the scene
        self.play(Write(a))
        self.wait(2)
        


         # Add the title
        q2 = Text("(b) How many children got B grade?", color=WHITE).scale(0.65)
        q2.to_edge( UP*7.5)

        
        # Create the scene
        self.play(Write(q2))
        self.wait(2)
        
        a1 = Text("  Answer:   Thirteen ",   color=BLUE).scale(0.7)
        a1.to_edge( UP*8.6)

        
        # Create the scene
        self.play(Write(a1))
        self.wait(2)

 # Add the title
        q3 = Text("(c) How many children got C grade?", color=WHITE).scale(0.65)
        q3.to_edge( UP*11.7)

        
        # Create the scene
        self.play(Write(q3))
        self.wait(2)
        
        a2 = Text("  Answer:   Five ",   color=BLUE).scale(0.7)
        a2.to_edge( UP*12.8)

        
        # Create the scene
        self.play(Write(a2))
        self.wait(2)





    def t3(self):
 
     # Create the table
        table = Table(
            [["Name of game", "Tally Marks", "Total"],
             ["Kabaddi", " |||||  |||||  |||||  |||||", "20"],
             ["Kho-kho", "|||||  |||||  ||", "12"],
             ["Carrom", "||||| ", "5"],
             ["Circket", "|||||  |||||  |||||  |||||  ||", "22"],
             ["Carrom", " ||||", "4"],
             ["Ludo", " || ", "2"],
             ["Volley ball", "|||||  |||||  |||", "13"],
                          
       
              ],
            include_outer_lines=True
        )
        
        # Style the table
        table.scale(0.52)  # Adjust scale as needed
        table.set_row_colors(RED,BLUE,BLUE,BLUE,BLUE,BLUE,BLUE,BLUE)
        
        # Add the title
        title = Text("Which is your favourite game? ",  color=WHITE).scale(0.9)
        title.next_to(table, UP)

        
        # Create the scene
        self.play(Write(title))
        self.wait(2)
        self.play(Create(table))
        self.wait(15) 
        
    def questions(self):

         # Add the title
        q1 = Text("(a) Which is the most popular game among children of your class? ",   color=WHITE).scale(0.65)
        q1.to_edge( UP*2.5)

        
        # Create the scene
        self.play(Write(q1))
        self.wait(2)
        
        a = Text("  Answer:  Circket ", color=BLUE).scale(0.7)
        a.to_edge( UP*3.6+LEFT)

        
        # Create the scene
        self.play(Write(a))
        self.wait(2)
        


         # Add the title
        q2 = Text("(b) Which is the least popular game among children of your class?", color=WHITE).scale(0.65)
        q2.to_edge( UP*7.5)

        
        # Create the scene
        self.play(Write(q2))
        self.wait(2)
        
        a1 = Text("  Answer:   Ludo ",   color=BLUE).scale(0.7)
        a1.to_edge( UP*8.6+LEFT)

        
        # Create the scene
        self.play(Write(a1))
        self.wait(2)

       
    def t4(self):
 
        # Create the table
        table = Table(
            [["Family size","Tally marks"," Number of families"],
             ["7 members and above","|","1"],
             ["6 members", "||", "2"],
             ["5 members", "||||", "4"],
             ["4 members", " |||||  ||", "7"],
             ["3 members", " |||", "3"],
             ["2 members", "|| ", "2"],
             ["1 members", " |", "1"],
                          
       
              ],
            include_outer_lines=True
        )
        
        # Style the table
        table.scale(0.52)  # Adjust scale as needed
        table.set_row_colors(BLUE)
        
        # Add the title
        title = Text("How big are the families that live around you?",  color=ORANGE).scale(0.85)
        title.next_to(table, UP)

        
        # Create the scene
        self.play(Write(title))
        self.wait(2)
        self.play(Create(table))
        self.wait(11)


    def t5(self):
 
        # Create the table
        table = Table(
            [["Types of houses","Tally marks"," No.of houses"],
             ["Apartments","|||||  |","6"],
             ["Villas", "||", "2"],
             ["Bungalows", "|||||", "5"],
          
       
              ],
            include_outer_lines=True
        )
        
        # Style the table
        table.scale(0.52)  # Adjust scale as needed
        table.set_row_colors(BLUE)
        
        # Add the title
        title = Text("Types of houses ",  color=YELLOW).scale(0.85)
        title.to_edge( UP)

        # Create the scene
        self.play(Write(title))
        self.wait(2)
        # Add the title
        title1 = Text("In a small village, there are 3 types of houses. The information has been\n given below. With the help of tally marks fill this tables.",  color=ORANGE).scale(0.57)
        title1.next_to(table, UP)

        # Create the scene
        self.play(Write(title1))
        self.wait(5)
        self.play(Create(table))
        self.wait(5)
        





        
    def toys(self):
    
 
        # Create the table
        table = Table(
            [["Toys","Total"],
            [" car        car       car        car        car        car","6"],
            [" doll       doll       doll       doll","4"],
            [" aeroplane         aeroplane","2"],
            [" bike       bike       bike       bike       bike","5"],
            [" teddy          teddy          teddy          teddy          teddy          teddy          teddy","7"],
            [" bus          bus          bus          bus         bus          bus          bus          bus          bus","9"], 
            [" train        train        train","3"], 
            [" parrot        parrot        parrot        parrot        parrot        parrot","6"],
       
              ],
            include_outer_lines=True
        )
        
        # Style the table
        table.scale(0.5)  # Adjust scale as needed
        table.set_row_colors(ORANGE,BLUE,BLUE,BLUE,BLUE,BLUE,BLUE,BLUE,BLUE)
        
        # Add the title
        title = Text("Picture Tables and Charts of  Toy Shop",  color=YELLOW).scale(0.7)
        title.next_to(table, UP)

        # Create the scene
        self.play(Write(title))
        self.wait(2)
        self.play(Create(table))
        self.wait(4)
        

    def question7(self):
           # Add the title
        q1 = Text("(a) Which toy is the most in stock at the end of the month?",   color=WHITE).scale(0.65)
        q1.to_edge( UP*1.7+LEFT)

        
        # Create the scene
        self.play(Write(q1))
        self.wait(2)
        
        a = Text("  Answer:   Bus", color=BLUE).scale(0.7)
        a.to_edge( UP*2.8+LEFT)

        
        # Create the scene
        self.play(Write(a))
        self.wait(2)
        


         # Add the title
        q2 = Text("(b)  Which toy is the least in stock at the end of the month?", color=WHITE).scale(0.65)
        q2.to_edge( UP*5+LEFT)

        
        # Create the scene
        self.play(Write(q2))
        self.wait(2)
        
        a1 = Text("  Answer:   Aeroplane ",   color=BLUE).scale(0.7)
        a1.to_edge( UP*6.1+LEFT)

        
        # Create the scene
        self.play(Write(a1))
        self.wait(2)

 # Add the title
        q3 = Text("(c)  There were 10 of each of these toys in the beginning of the month\nLooking at the stock of toys in the picture table can you say which \ntoy has been sold the most in the month?", color=WHITE).scale(0.65)
        q3.to_edge( UP*8.3+ LEFT)

        
        # Create the scene
        self.play(Write(q3))
        self.wait(2)
        
        a2 = Text("  Answer:   Aeroplane",   color=BLUE).scale(0.7)
        a2.to_edge( UP*10.9+LEFT)

        
        # Create the scene
        self.play(Write(a2))
        self.wait(2)

# Add the title
        q4 = Text("(d)   Which other toys are popular with children?", color=WHITE).scale(0.65)
        q4.to_edge( UP*12.5+ LEFT)

        
        # Create the scene
        self.play(Write(q4))
        self.wait(2)
        
        a3 = Text("  Answer:    Bike,Car,Doll,Train,Parrot,Teddy ",   color=BLUE).scale(0.7)
        a3.to_edge( UP*13.6+LEFT)

        
        # Create the scene
        self.play(Write(a3))
        self.wait(2)


###
    def h1(self):
           # Add the title
        q1 = Text("Helping Hands!",   color=BLUE).scale(0.82)
        q1.to_edge( UP*1.7+LEFT)

        
        # Create the scene
        self.play(Write(q1))
        self.wait(2)
        
        a = Text(" Class 4 students of Palampet Primary School were given a target of \n\ncollecting300 in a week for an orphanage home. They asked  5 donation\n\n from eachperson they approached.", color=WHITE).scale(0.65)
        a.to_edge( UP*3.7+LEFT)

        
        # Create the scene
        self.play(Write(a))
        self.wait(5)
        
      
 
    def coin(self):
        # Create table
        table = Table(
            [["Day", "Money collected(coins)", "Total money"],
             ["SUN", "5   5   5   5   5   5   5   5   5   5   5   5   5   5 ", "70"],
             ["MON", "5   5   5   5   5   5   5", "35"],
             ["TUE", "5   5   5   5   5   5   5   5", "40"],
             ["WED", "5   5   5   5   5   5", "30"],
             ["THU", "5   5   5   5   5   5   5   5  5 ", "45"],
             ["FRI", "5   5   5   5   5   5", "30"],
             ["SAT", "5   5   5   5   5   5   5   5   5   5   5", "55"]],
            include_outer_lines=True,
            arrange_in_grid_config={"cell_alignment": LEFT}
        )
        table.scale(0.6)
        table.set_row_colors(YELLOW,BLUE,BLUE,BLUE,BLUE,BLUE,BLUE,BLUE,BLUE)

        # # Create coins
        # coin = Circle(radius=0.07, color=BLUE).set_fill(BLUE, opacity=0.8)
        # coin_values = [14, 7, 8, 6, 9, 6, 11]  # Number of coins for each day

        # coin_groups = VGroup(*[
        #     VGroup(*[coin.copy() for _ in range(value)]).arrange(RIGHT*1.8, buff=0.08)
        #     for value in coin_values
        # ])

        # for i, coin_group in enumerate(coin_groups):
        #     coin_group.next_to(table.get_entries((i+2, 1)), RIGHT*1.8, buff=0.6)

        # # Animation
        # self.play(Create(table))

        # for i, coin_group in enumerate(coin_groups):
        #     self.play(
        #         LaggedStartMap(FadeIn, coin_group, lag_ratio=0.1),
        #         run_time=1.2
        #     )
        self.play(Create(table))
        self.wait(5)


    def question8(self):
           # Add the title
        q1 = Text("(a)  On which day was the collection highest?",   color=WHITE).scale(0.65)
        q1.to_edge( UP*1.7+LEFT)

        
        # Create the scene
        self.play(Write(q1))
        self.wait(2)
        
        a = Text("  Answer:   Sunday", color=BLUE).scale(0.7)
        a.to_edge( UP*2.8+LEFT)

        
        # Create the scene
        self.play(Write(a))
        self.wait(2)
        


         # Add the title
        q2 = Text("(b)  On which days did they collect the same amount of money?", color=WHITE).scale(0.65)
        q2.to_edge( UP*5+LEFT)

        
        # Create the scene
        self.play(Write(q2))
        self.wait(2)
        
        a1 = Text("  Answer:   wednesday and  Friday ",   color=BLUE).scale(0.7)
        a1.to_edge( UP*6.1+LEFT)

        
        # Create the scene
        self.play(Write(a1))
        self.wait(2)

 # Add the title
        q3 = Text("(c)   Did the class meet its target?", color=WHITE).scale(0.65)
        q3.to_edge( UP*8.4+ LEFT)

        
        # Create the scene
        self.play(Write(q3))
        self.wait(2)
        
        a2 = Text("  Answer:   yes ",   color=BLUE).scale(0.7)
        a2.to_edge( UP*10.5+LEFT)

        
        # Create the scene
        self.play(Write(a2))
        self.wait(2)







        # ########\
    def paddy(self):
      
        chart = BarChart(
            values=[7, 8, 11, 14],
            bar_names=["2009", "2010", "2011", "2012"],
            y_range=[0,14],
            y_length=7,
            x_length=14,
            x_axis_config={"font_size": 36},
        ).scale(0.8)

        c_bar_lbls = chart.get_bar_labels(font_size=36)
        # Add the title
        title = Text("Bags of paddy(Each bag 50kgs)",  color=WHITE).scale(0.85)
        title.to_edge(UP*0.5)

        
        # Create the scene
        self.play(Write(title))
        self.wait(2)

        self.add(chart, c_bar_lbls)
           # Create title
        title = Text("No.of\nBags", color=WHITE,font_size=24).to_edge(UP*0.9+LEFT*1.8)
        title1 = Text("Years", color=WHITE,font_size=26).to_edge(DOWN*2+RIGHT*0.7)
        self.play(Write(title),Write(title1))
        
        self.wait(8)

    
 
    def question5(self):
           # Add the title
        q1 = Text("(a) In which year the production of paddy is highest? How much?",   color=WHITE).scale(0.65)
        q1.to_edge( UP*1.7+LEFT)

        
        # Create the scene
        self.play(Write(q1))
        self.wait(2)
        
        a = Text("  Answer:   2012 and 14bags(each 50kgs)", color=BLUE).scale(0.7)
        a.to_edge( UP*2.8+LEFT)

        
        # Create the scene
        self.play(Write(a))
        self.wait(2)
        


         # Add the title
        q2 = Text("(b) In which year did the paddy production was double to that of 2009?", color=WHITE).scale(0.65)
        q2.to_edge( UP*5+LEFT)

        
        # Create the scene
        self.play(Write(q2))
        self.wait(2)
        
        a1 = Text("  Answer:   2012 ",   color=BLUE).scale(0.7)
        a1.to_edge( UP*6.1+LEFT)

        
        # Create the scene
        self.play(Write(a1))
        self.wait(2)

 # Add the title
        q3 = Text("(c)   Paddy production has steadily increased over the past four years.\nCan we draw this conclusion from the above picture chart?", color=WHITE).scale(0.65)
        q3.to_edge( UP*8.4+ LEFT)

        
        # Create the scene
        self.play(Write(q3))
        self.wait(2)
        
        a2 = Text("  Answer:   Usage of good fertilizers and multicroping system.",   color=BLUE).scale(0.7)
        a2.to_edge( UP*10.5+LEFT)

        
        # Create the scene
        self.play(Write(a2))
        self.wait(2)


    def box(self):
      
        chart = BarChart(
            values=[2, 6, 5, 7, 6],
            bar_names=["Groundnut oil", "Palmolein oil", "Sunflower oil", "Coconut oil", "Rice bran oil"],
            y_range=[0,7],
            y_length=7,
            x_length=14,
            x_axis_config={"font_size": 36},
        ).scale(0.8)

        c_bar_lbls = chart.get_bar_labels(font_size=36)
        # Add the title
        title = Text("How much oil is in stock?",  color=ORANGE).scale(0.4)
        title.to_edge(UP*0.5)

        
        # Create the scene
        self.play(Write(title))
        self.wait(2)

        self.add(chart, c_bar_lbls)
          # Create title
        title = Text("Stocks\n(liters)", color=WHITE,font_size=24).to_edge(UP*1.0+LEFT*1.5)
        title1 = Text("Name of\n oil", color=WHITE,font_size=24).to_edge(DOWN*1.8+RIGHT*0.5)
        self.play(Write(title),Write(title1))
        
        self.wait(8)
 
    def question(self):
           # Add the title
        q1 = Text("(a) Which oil is lying most in stock?",   color=WHITE).scale(0.65)
        q1.to_edge( UP*1.7+LEFT)

        
        # Create the scene
        self.play(Write(q1))
        self.wait(2)
        
        a = Text("  Answer:   Coconut oil", color=BLUE).scale(0.7)
        a.to_edge( UP*2.8+LEFT)

        
        # Create the scene
        self.play(Write(a))
        self.wait(2)
        


         # Add the title
        q2 = Text("(b) Which oil is lying least in stock?", color=WHITE).scale(0.65)
        q2.to_edge( UP*5+LEFT)

        
        # Create the scene
        self.play(Write(q2))
        self.wait(2)
        
        a1 = Text("  Answer:   Groundnut oil ",   color=BLUE).scale(0.7)
        a1.to_edge( UP*6.1+LEFT)

        
        # Create the scene
        self.play(Write(a1))
        self.wait(2)

 # Add the title
        q3 = Text("(c)  If there were 30 packets of groundnut oil in the \nbeginning of the week then how many have been sold in the week?", color=WHITE).scale(0.65)
        q3.to_edge( UP*8.3+ LEFT)

        
        # Create the scene
        self.play(Write(q3))
        self.wait(2)
        
        a2 = Text("  Answer:   Two",   color=BLUE).scale(0.7)
        a2.to_edge( UP*10.4+LEFT)

        
        # Create the scene
        self.play(Write(a2))
        self.wait(2)

# Add the title
        q4 = Text("(d)   If there were 20 packets of sunflower oil in the \nbeginning of the week then how many have been sold in the week?", color=WHITE).scale(0.65)
        q4.to_edge( UP*11.8+ LEFT)

        
        # Create the scene
        self.play(Write(q4))
        self.wait(2)
        
        a3 = Text("  Answer:    Five ",   color=BLUE).scale(0.7)
        a3.to_edge( UP*13.9+LEFT)

        
        # Create the scene
        self.play(Write(a3))
        self.wait(2)




    def SetDeveloperList(self):
        self.DeveloperList = "Uday Kiran"   

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade4chapter13Smarttables.py"      



        
   # Run the scene
if __name__ == "__main__":
    from manim import config
    config.background_color = BLACK
    Grade4chapter13Smarttables().render()