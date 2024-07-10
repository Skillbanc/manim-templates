from AbstractAnim import AbstractAnim
from manim import *

class KnowingNumbers(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.Extra_text()
        self.fadeOutCurrentScene()
        self.finding_largest_smallestNumbers()
        self.fadeOutCurrentScene()
        self.ascendinganddescendingorder()
        self.fadeOutCurrentScene()
        self.RoundoffNumbers()
        self.fadeOutCurrentScene()
        self.REVISIONOFPLACEVALUE()
        self.fadeOutCurrentScene()
        self.Placevalueoflargernumbers()
        self.fadeOutCurrentScene()
        self.comparisionofindianinternationalsystems()
        self.fadeOutCurrentScene()
        self.largeNumbersUsedInDailyLifeSituations()
        self.fadeOutCurrentScene()  
        self.GithubSourceCodeReference()



    def Extra_text(self):
        title = Text("Chapter1 : Knowing our Numbers", font_size=48)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))




    def finding_largest_smallestNumbers(self):

        union = Text("1.1  Estimating and Comparing Numbers",color=PURPLE_B,font_size=37).to_edge(UP*1)
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
        self.play(Create(table))
        self.wait(3)
        self.play(Write(sub_title2))
        self.wait(2)
        self.play(Write(sub_title3))
        self.wait(2)
        self.play(Write(sub_title4))
        self.wait(2)
        

        self.play(FadeOut(sub_title2),FadeOut(sub_title1), FadeOut(sub_title4), FadeOut(sub_title3),FadeOut(table), FadeOut(union))



        heading = MarkupText(
            "<span foreground='PURPLE'>Example :</span>         585 , 9535 , 9678 , 44",
            font_size=34
        ).to_edge(UP*1+LEFT * 1)
        sub_title1 = Text("For finding largest number with equal number of digits  there are two cases :",font_size=29).to_edge(UP*2.75+LEFT *1)
        sub_title2 = MarkupText(
            "<span foreground='yellow'>Case 1 :</span>  if the numbers of digits of a given numbers are same (9535 , 9678)",
            font_size=29
        ).to_edge(UP*4.75+LEFT*1)
        sub_title3 = Text("then start comparing first digit from left side of a given numbers .",font_size=29).to_edge(UP*6.25+LEFT *2)
        sub_title4 = Text("from numbers 9535 and 9635 comparing first digit from left 9 = 9",font_size=29).to_edge(UP*7.75+LEFT *2)
        sub_title5 = MarkupText(
            "<span foreground='yellow'>Case 2 :</span>  if the first digit from left side are same then compare the next place",
            font_size=29
        ).to_edge(UP*9.25+LEFT * 1)
        sub_title6 = Text("from numbers 9535 and 9635 comparing second digit from left 5 < 6",font_size=29).to_edge(UP*10.75+LEFT *2)
        sub_title7 = Text("so the number 9535 < 9635. so the greatest nuber is 9635.",font_size=29).to_edge(UP*12.25+LEFT * 2)
        sub_title8 = Text("next step we can arrange these numbers in a Assending and Descending order.",font_size=29,color=GRAY).to_edge(UP*14+LEFT * 0.6)
        


        self.play(Write(heading))
        self.wait(1)
        self.play(Write(sub_title1))
        self.wait(2)
        self.play(Write(sub_title2))
        self.wait(3)
        self.play(Write(sub_title3))
        self.wait(3)
        self.play(Write(sub_title4))
        self.wait(3)
        self.play(Write(sub_title5))
        self.wait(3)
        self.play(Write(sub_title6))
        self.wait(3)
        self.play(Write(sub_title7))
        self.wait(3)
        self.play(Write(sub_title8))
        self.wait(3)

        self.play(FadeOut(sub_title8), FadeOut(sub_title7), FadeOut(sub_title6), FadeOut(sub_title5), FadeOut(sub_title4), FadeOut(sub_title3), FadeOut(sub_title2), FadeOut(sub_title1),FadeOut(heading))


    def ascendinganddescendingorder(self):  

        heading = Text("Ascending  order :",color=DARK_BROWN,font_size=37).to_edge(UP*1.25+LEFT * 1)
        sub_title1 = Text("Ascending order is the arrangement of elements from smallest to largest.",font_size=29).to_edge(UP*3)
        sub_title2 = Text("for the previous example:  585 , 9535 , 9678 , 44 ",font_size=29).to_edge(UP*4.75)
        sub_title3 = Text("Ascending  order is     44 , 585 , 9535 , 9678",font_size=29).to_edge(UP*6.6)
        heading2 = Text("Descending order :",color=PINK,font_size=37).to_edge(UP*9+LEFT * 1)
        sub_title5 = Text("Descending order is the arrangement of elements from largest to smallest.",font_size=29).to_edge(UP*10.5)
        sub_title6 = Text("for the above example:   585 , 9535 , 9678 , 44 ",font_size=29).to_edge(UP*12)
        sub_title7 = Text("Descending order is     9678 , 9535 , 585 , 44",font_size=29).to_edge(UP*13.5)
        
        self.play(Write(heading))
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


    def RoundoffNumbers(self):

        union = Text("1.2  Estimating And Rounding Off Numbers ", color=DARK_BROWN, font_size=37).to_edge(UP*1)
        sub_title1 = Text("We usually round off the numbers to the nearest 10's(Tens),", font_size=29).to_edge(UP*3)
        sub_title2 = Text("100's(Hundreds), 1000's (Thousands), 10000's (Ten Thousands)... etc.", font_size=29).to_edge(UP*4.75)
        sub_title3 = Text("Rounding off the numbers to the nearest tens:", font_size=30, color=GREY).to_edge(UP*6.5+LEFT *1)
        sub_title4 = Text("82 is near to 80 than 90, and 87 is near to 90 than 80.", font_size=29).to_edge(UP*13)
        sub_title5 = Text("85 is at equal distance from 80 and 90.", font_size=29).to_edge(UP*14)
        
        

        # Create number line from 80 to 90 with slower playback speed
        number_line = NumberLine(
            x_range=[80, 90, 1],
            length=10,
            include_numbers=True,
            label_direction=UP
        ).to_edge(UP*9)

        # Create circles for the numbers to be rounded
        circle_82 = Circle(radius=0.5, color=BLUE).move_to(number_line.n2p(82) + UP * 0.3)
        circle_85 = Circle(radius=0.5, color=BLUE).move_to(number_line.n2p(85) + UP * 0.2)
        circle_87 = Circle(radius=0.5, color=BLUE).move_to(number_line.n2p(87) + UP * 0.3)

        # Create curved arrows for rounding off 82 to 80
        arrow_82_to_80 = ArcBetweenPoints(
            start=circle_82.get_center() + UP * 0.5,
            end=number_line.n2p(80),
            angle=TAU / 4,
            color=PINK
        ).add_tip(tip_length=0.2)

        # Create curved arrows for rounding off 87 to 90
        arrow_87_to_90 = ArcBetweenPoints(
            start=circle_87.get_center() + UP * 0.5,
            end=number_line.n2p(90),
            angle=-TAU / 4,
            color=PINK
        ).add_tip(tip_length=0.2)

        # Create curved arrows for rounding off 85 to 80 and 90 (pointing downwards)
        arrow_85_to_80 = ArcBetweenPoints(
            start=circle_85.get_center() + DOWN * 0.5,
            end=number_line.n2p(80),
            angle=-TAU / 4,
            color=PINK
        ).add_tip(tip_length=0.2)

        arrow_85_to_90 = ArcBetweenPoints(
            start=circle_85.get_center() + DOWN * 0.5,
            end=number_line.n2p(90),
            angle=TAU / 4,
            color=PINK
        ).add_tip(tip_length=0.2)

        


        self.play(Write(union))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)
        self.play(Write(sub_title3))
        self.wait(1)
        self.play(Create(number_line), run_time=3)  # Adjust run_time as needed
        self.wait(1)
        self.play(Create(circle_82))
        self.play(Create(circle_85))
        self.play(Create(circle_87))
        self.wait(1)
        self.play(Write(sub_title4))
        self.wait(1)
        self.play(Create(arrow_82_to_80))
        self.wait(1)
        self.play(Create(arrow_87_to_90))
        self.wait(1)
        self.play(Write(sub_title5))
        self.wait(1)
        self.play(Create(arrow_85_to_80))
        self.play(Create(arrow_85_to_90))

        # Wait before ending the scene
        self.wait(2)

        # Fade out everything before ending the scene
        self.play(FadeOut(VGroup(union, sub_title1, sub_title2, sub_title3, sub_title4, sub_title5, 
                                 number_line, circle_82, circle_85, circle_87, 
                                 arrow_82_to_80, arrow_87_to_90, arrow_85_to_80, arrow_85_to_90)))

        self.wait(2)

    
     

        union = Text("Rounding off the numbers to nearest hundreds : ", color=ORANGE, font_size=31).to_edge(UP*1+LEFT*1)
        sub_title1 = Text("220 is nearer to 200 than 300, so 220 is rounded off to 200.", font_size=29).to_edge(UP*6)
        sub_title2 = Text("280 is nearer to 300 than 200, so it is rounded off to 300.", font_size=29).to_edge(UP*7.5)
        sub_title3 = MarkupText(
            "<span foreground='grey'>Compare the last digit rule:</span>   If the last digit is 5 or greater, we round up.",
            font_size=29
        ).to_edge(UP*9+LEFT *1)
        sub_title4 = Text("If it's less than 5, we round down.", font_size=29).to_edge(UP*10.5+LEFT*10)
        sub_title5 = Text("Since the tens digit(250) is exactly 5, we round up to the next hundred.", font_size=29).to_edge(UP*12)
        sub_title6 = Text("Therefore, 250 is rounded off to 300 ", font_size=29).to_edge(UP*13.5)


        # Create number line from 200 to 300
        number_line = NumberLine(
            x_range=[200, 300, 10],
            length=10,
            include_numbers=True,
            label_direction=UP
        ).to_edge(UP*3.5)  # Adjusted to fit well within the scene

        # Create circles for the numbers to be rounded
        circle_220 = Circle(radius=0.5, color=BLUE).move_to(number_line.n2p(220) + UP * 0.3)
        circle_250 = Circle(radius=0.5, color=BLUE).move_to(number_line.n2p(250) + UP * 0.3)
        circle_280 = Circle(radius=0.5, color=BLUE).move_to(number_line.n2p(280) + UP * 0.3)

        # Create curved arrows for rounding off 220 to 200
        arrow_220_to_200 = ArcBetweenPoints(
            start=circle_220.get_center() + UP * 0.5,
            end=number_line.n2p(200),
            angle=TAU / 4,
            color=PINK
        ).add_tip(tip_length=0.2)

        # Create curved arrows for rounding off 280 to 300
        arrow_280_to_300 = ArcBetweenPoints(
            start=circle_280.get_center() + UP * 0.5,
            end=number_line.n2p(300),
            angle=-TAU / 4,
            color=PINK
        ).add_tip(tip_length=0.2)

        # Create curved arrows for rounding off 280 to 300
        arrow_250_to_300 = ArcBetweenPoints(
            start=circle_250.get_center() + UP * 0.5,
            end=number_line.n2p(300),
            angle=-TAU / 4,
            color=PINK
        ).add_tip(tip_length=0.2)


        self.play(Write(union))

        # Add all elements to the scene with adjusted run_time
        self.play(Create(number_line), run_time=3)  # Adjust run_time as needed
        self.wait(1)
        self.play(Create(circle_220))
        self.play(Create(circle_250))
        self.play(Create(circle_280))
        self.wait(1)
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Create(arrow_220_to_200))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)
        self.play(Create(arrow_280_to_300))
        self.wait(1)
        self.play(Write(sub_title3))
        self.wait(1)
        self.play(Write(sub_title4))
        self.wait(1)
        self.play(Write(sub_title5))
        self.wait(1)
        self.play(Write(sub_title6))
        self.wait(1)
        self.play(Create(arrow_250_to_300))
        self.wait(1)




        # Fade out everything before ending the scene
        self.play(*[FadeOut(mob) for mob in self.mobjects])



    def REVISIONOFPLACEVALUE(self):
        # Title
        title = Text("1.3  REVISION OF PLACE VALUE", font_size=30,color=BLUE).to_edge(UP * 1)
        sub_title1 = Text("expanding a two digit, three digit, four digit and five digit number :",font_size=29).to_edge(UP*2.75+LEFT*1)

        sub_title2 = Text("1. Expand  64                =",font_size=27).to_edge(UP* 4.5+LEFT*1)
        sub_title3 = Text("=                     (6 × 10) + (4 × 1)",font_size=29).to_edge(UP* 7 +RIGHT * 9.25)
        sub_title4 = Text("=                    60 + 4",font_size=29).to_edge(UP*8.5+RIGHT* 13)

        # Table data
        data = [
            ["Tens" ,"Ones"],
            ["6","4"]
        ]

        # Create the table
        table = Table(
            data,
            include_outer_lines=True,
            h_buff=3,
            v_buff=1,
        )

        # Scale the table and adjust position if needed
        table.scale(0.35).to_edge(UP * 4.5 + RIGHT * 8.75)

        
        self.play(Create(title))
        self.wait(4)
        self.play(Write(sub_title1))
        self.wait(2)
        self.play(Write(sub_title2))
        self.wait(2)
        self.play(Create(table))
        self.wait(2)
        self.play(Write(sub_title3))
        self.wait(2)
        self.play(Write(sub_title4))

        sub_title5 = Text("2. Expand  325             =",font_size=27).to_edge(UP* 10.25+LEFT *1)
        sub_title6 = Text("=                    (3 × 100) + (2 × 10) + (5 × 1)",font_size=29).to_edge(UP* 13 +RIGHT * 5.5)
        sub_title7 = Text("=                    300 + 20 + 5",font_size=29).to_edge(UP*15+RIGHT* 10.8)

        

        # Table data
        data = [
            ["Hundreds","Tens" ,"Ones"],
            ["3","2","5"]
        ]

        # Create the table
        table_1 = Table(
            data,
            include_outer_lines=True,
            h_buff=4,
            v_buff=1,
        )

        # Scale the table and adjust position if needed
        table_1.scale(0.35).to_edge(UP * 10.25 + RIGHT * 3)

        
        self.play(Create(sub_title5))
        self.wait(3)
        self.play(Create(table_1))
        self.wait(2)
        self.play(Write(sub_title6))
        self.wait(2)
        self.play(Write(sub_title7))
        self.wait(2)


        self.play(FadeOut(table_1), FadeOut(sub_title7), FadeOut(sub_title6), FadeOut(sub_title5), FadeOut(sub_title4), FadeOut(sub_title3),FadeOut(table), FadeOut(sub_title2), FadeOut(sub_title1),FadeOut(title))

                
    

        sub_title2 = Text("3. Expand    5078            =",font_size=27).to_edge(UP* 1.25+LEFT*1)
        sub_title3 = Text("=                (5 × 1000) + (0 × 100) + (7 × 10) + (8 × 1)",font_size=29).to_edge(UP* 4 +RIGHT * 1)
        sub_title4 = Text("=                5000 + 0 + 70 + 8",font_size=29).to_edge(UP*5.75+RIGHT* 9.1)
        sub_title = Text("=                 5000 + 70 + 8",font_size=29).to_edge(UP*7.25+RIGHT* 10.2)

        # Table data
        data = [
            ["Thousands","Hundreds","Tens" ,"Ones"],
            ["5","0","7","8"]
        ]

        # Create the table
        table = Table(
            data,
            include_outer_lines=True,
            h_buff=2,
            v_buff=1,
        )

        # Scale the table and adjust position if needed
        table.scale(0.35).to_edge(UP * 1.1 + RIGHT * 5)

        

        self.play(Write(sub_title2))
        self.wait(2)
        self.play(Create(table))
        self.wait(2)
        self.play(Write(sub_title3))
        self.wait(2)
        self.play(Write(sub_title4))
        self.wait(2)
        self.play(Write(sub_title))
        self.wait(2)

        sub_title5 = Text("4. Expand  29500             =",font_size=27).to_edge(UP* 9.25+LEFT *1)
        sub_title6 = Text("=    (2 × 10000) + (9 × 1000) + (5 × 100) + (0 × 10) + (0 × 1)",font_size=23).to_edge(UP* 12 +RIGHT * 1.25)
        sub_title7 = Text("=                20000 + 9000 + 500 + 0 + 0",font_size=29).to_edge(UP*13.5+RIGHT* 4.79)
        sub_title8 = Text("=                20000 + 9000 + 500",font_size=29).to_edge(UP*15+RIGHT* 7.6)

        

        

        # Table data
        data = [
            ["Ten Thousands","Thousands","Hundreds","Tens" ,"Ones"],
            ["2","9","5","0","0"]
        ]

        # Create the table
        table_1 = Table(
            data,
            include_outer_lines=True,
            h_buff=1.2,
            v_buff=1,
        )

        # Scale the table and adjust position if needed
        table_1.scale(0.35).to_edge(UP * 9.05 + RIGHT * 3)

        
        self.play(Create(sub_title5))
        self.wait(3)
        self.play(Create(table_1))
        self.wait(2)
        self.play(Write(sub_title6))
        self.wait(2)
        self.play(Write(sub_title7))
        self.wait(2)
        self.play(Write(sub_title8))
        self.wait(2)

        self.play(FadeOut(table_1), FadeOut(sub_title8), FadeOut(sub_title7), FadeOut(sub_title6), FadeOut(sub_title5),FadeOut(sub_title), FadeOut(sub_title4), FadeOut(sub_title3),FadeOut(table), FadeOut(sub_title2))











    def Placevalueoflargernumbers(self):
        # Title
        title = Text("1.4  Place value of larger numbers", font_size=30,color=BLUE).to_edge(UP * 1)
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

        self.play(FadeOut(sub_title2),FadeOut(sub_title1), FadeOut(sub_title4), FadeOut(sub_title3),FadeOut(table), FadeOut(title))





        # Title
        title = Text("Example :", font_size=30,color=BLUE).to_edge(UP * 1+LEFT*1)
        sub_title1 = Text("Expansion of 41430495   = ",font_size=29).to_edge(UP*3+LEFT*1)
        sub_title2 = Text("So the number has 8 digits expansion start from crore :",font_size=27).to_edge(UP*8.75+LEFT*0.7)
        sub_title3 = Text("4,14,30,495  =  (4 × 10000000) + (1 × 1000000) + (4 × 100000) + (3 × 10000) + ",font_size=27).to_edge(UP*10.25+LEFT*0.8)
        sub_title4 = Text("    (0 × 1000) + (4 × 100) + (9 × 10) + (5 × 1)",font_size=29).to_edge(UP* 11.75+  LEFT *6.75)
        sub_title5 = MarkupText(
            "<span foreground='yellow'>Read as:</span> Four crore fourteen lakh thirty thousand four hundred ninety five",
            font_size=29
        ).to_edge(UP*14 + LEFT*1)

    
        # Table data
        headers = ["Places", "T. Cr", "Cr", "T. La", "La", "T. Th.", "Th.", "H", "T", "O"]
        row1 = ["No. of Digits", "9", "8", "7", "6", "5", "4", "3", "2", "1"]
        row2 = ["Number\n(41430495)", "-", "4", "1", "4", "3", "0", "4", "9", "5"]

        # Combine headers and rows
        table_data = [headers, row1, row2]

        # Create the table
        table = Table(
            table_data,
            include_outer_lines=True,
            h_buff=1,
            v_buff=2.3,
            line_config={"stroke_width": 2}
        )

        # Scale the table and adjust position if needed
        table.scale(0.35).to_edge(UP*1.4+LEFT*12)



        self.play(Create(title))
        self.wait(2)
        self.play(Write(sub_title1))
        self.wait(2)
        self.play(Create(table))
        self.wait(4)
        self.play(Write(sub_title2))
        self.wait(2)
        self.play(Write(sub_title3))
        self.wait(2)
        self.play(Write(sub_title4))
        self.wait(3)
        self.play(Write(sub_title5))
        self.wait(1)

        self.play(FadeOut(sub_title5),FadeOut(sub_title4), FadeOut(sub_title3), FadeOut(sub_title2), FadeOut(sub_title1),FadeOut(table), FadeOut(title))    
       




    def comparisionofindianinternationalsystems(self):
        # Title
        title = Text("1.5  Comparison of Indian and International Numeration Systems", font_size=30,color=BLUE).to_edge(UP * 1)
        sub_title1 = Text("Let us compare the places in both the systems :",font_size=29).to_edge(UP*2.75+LEFT*1)

        sub_title2 = Text("From the above table, the relation between these systems understood as follows:",font_size=27).to_edge(UP* 9+LEFT*1)
        sub_title3 = Text("10 lakhs   =   1 million",font_size=29).to_edge(UP*10.5+LEFT*8)
        sub_title4 = Text("1 crore     =   10 million",font_size=29).to_edge(UP*12+LEFT*8)
        sub_title5 = Text("10 crore   =   100 million",font_size=29).to_edge(UP*13.5+LEFT*8)
        sub_title6 = Text("100 crore =   1 billion",font_size=29).to_edge(UP*14.75+LEFT*8)


        # Group subtitles 4, 5, and 6
        group_subtitles = VGroup(sub_title3, sub_title4, sub_title5, sub_title6)
        
        # Create one surrounding rectangle for the grouped subtitles with increased padding
        rect = SurroundingRectangle(group_subtitles, color=GREEN_B, buff=0.25)
        
        
        self.play(Write(title))
        self.wait(2)
        self.play(Write(sub_title1))
        self.wait(1)
        
        # Table data
        data = [
            ["Indian System", "H.Cr.", "Ten.Cr.", "Crore", "Ten.La.", "Lakh", "Ten Th.", "Thousand", "Hundred", "Tens", "Ones"],
            ["International System", "Billion", "Hund. Million", "Ten Million", "Million", "Hund. Th.", "Ten Th.", "Thousand", "Hundred", "Tens", "Ones"]
        ]

        # Create the table
        table = Table(
            data,
            include_outer_lines=True,
            h_buff=0.7,
            v_buff=2,
        )

        # Scale the table and adjust position if needed
        table.scale(0.35).to_edge(UP * 4.5)

        # Draw the table
        self.play(Create(table))
        self.wait(4)

        self.play(Write(sub_title2))
        self.wait(2)
        self.play(Write(sub_title3))
        self.wait(2)
        self.play(Write(sub_title4))
        self.wait(2)
        self.play(Write(sub_title5))
        self.wait(2)
        self.play(Write(sub_title6))
        
        self.play(Create(rect))
        self.wait(1.5)

        self.play(FadeOut(rect),FadeOut(table), FadeOut(sub_title6), FadeOut(sub_title5), FadeOut(sub_title4), FadeOut(sub_title3), FadeOut(sub_title2), FadeOut(sub_title1),FadeOut(title))



        sub_title3 = Text("Usage of commas :",font_size=29,color=PINK).to_edge(UP*1+LEFT*0.73)
        sub_title4 = Text("The first comma comes after hundred place(i.e. three digits from the right)",font_size=27).to_edge(UP*2.5+LEFT*0.73)

        # Heading with highlighted part
        heading_part1 = Text("Indian System:", font_size=27, t2c={"Indian System": YELLOW}).to_edge(UP*4.25 + LEFT * 0.73)
        heading_part2 = Text("Second Comma is placed every two digits from the right.", font_size=27).next_to(heading_part1, RIGHT)
        heading = VGroup(heading_part1, heading_part2)

        # Subtitle with highlighted part
        sub_title1_part1 = Text("International System:", font_size=27, t2c={"International System": YELLOW}).to_edge(UP*5.75+ LEFT * 0.73)
        sub_title1_part2 = Text("Second Comma is placed every three digits from the right.", font_size=27).next_to(sub_title1_part1, RIGHT)
        sub_title1 = VGroup(sub_title1_part1, sub_title1_part2)

        # Subtitle about the number
        sub_title2 = Text("Suppose the number is  45690255 ", font_size=27).to_edge(UP*7.5 + LEFT * 0.73)

        # Play animations to display the headings and subtitles
        self.play(Write(sub_title3))
        self.wait(2)
        self.play(Write(sub_title4))
        self.wait(2)
        
        self.play(Write(heading))
        self.wait(2)
        self.play(Write(sub_title1))
        self.wait(2)
        self.play(Write(sub_title2))
        self.wait(1)
       
        

        # Table data          
        data = [
            ["4,56,90,255"  , "45,690,255"],
            ["Four crore fifty six lakhs ninety thousand two hundred and fifty five.",
             "Forty five million six hundred ninety thousand two hundred fifty five."]
        ]

        # Create the table with custom font sizes
        table = Table(
            data,
            include_outer_lines=True,
            h_buff=1.2,
            v_buff=2.8,
            col_labels=[Text("Indian system of numeration"), Text("International system of numeration")],
        )

        # Increase font size for rows 1 and 2
        table.get_rows()[0].scale(1.2)  # Increase font size for the first row
        table.get_rows()[1].scale(1.2)  # Increase font size for the second row

        # Scale the table and adjust position if needed
        table.scale(0.3).to_edge(UP*9)

        # Draw the table
        self.play(Create(table))
        self.wait(2)





    def largeNumbersUsedInDailyLifeSituations(self):
        # Title
        title = Text("1.7  LARGE NUMBERS USED IN DAILY LIFE SITUATIONS", font_size=30, color=BLUE).to_edge(UP * 1)
        sub_title1 = Text("We use meter (m) as a unit of length, kilogram (kg) as a unit of weight", font_size=29).to_edge(UP * 3)
        sub_title2 = Text("Litre (l) as a unit of volume and second (s) as a unit of time.", font_size=27).to_edge(UP * 5)
        sub_title3 = Text("Since there is a relationship between all of them:", font_size=29).to_edge(UP * 7.25 + LEFT * 1)
        sub_title4 = Text("10 millimeters      =  1 centimeter", font_size=29).to_edge(UP * 9.5+LEFT*8)
        sub_title5 = Text("100 centimeters  =  1 meter", font_size=29).to_edge(UP * 11.25+LEFT*8)
        sub_title6 = Text("1000 meters         =  1 kilometer", font_size=29).to_edge(UP * 13+LEFT*8)

        # Group subtitles 4, 5, and 6
        group_subtitles = VGroup(sub_title4, sub_title5, sub_title6)
        
        # Create one surrounding rectangle for the grouped subtitles with increased padding
        rect = SurroundingRectangle(group_subtitles, color=DARK_BROWN, buff=0.5)

        self.play(Write(title))
        self.wait(2)
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(2)
        self.play(Write(sub_title3))
        self.wait(2)
        self.play(Write(sub_title4), Write(sub_title5), Write(sub_title6), Create(rect))
        self.wait(2)
        
        self.play(FadeOut(sub_title6), FadeOut(sub_title5), FadeOut(sub_title4), FadeOut(rect), FadeOut(sub_title3), FadeOut(sub_title2), FadeOut(sub_title1), FadeOut(title))
        

        # Title
        title = Text("We can calculate the number of millimeters in 1 kilomete :", font_size=30, color=BLUE).to_edge(UP * 1+LEFT*1)
        sub_title1 = Text(" 1km   =  1000m", font_size=29).to_edge(UP * 2.5+LEFT*6)
        sub_title2 = Text("=  1000 × 100 cm", font_size=27).to_edge(UP * 3.75+LEFT*8)
        sub_title3 = Text("=  1000 × 100 × 10 mm", font_size=29).to_edge(UP * 5.25+LEFT*8)
        sub_title4 = Text("=  10,00,000 mm", font_size=29).to_edge(UP * 6.75+LEFT*8)
        sub_title5 = Text("calculating the number of milligrams in 1 kilogram :", font_size=29, color=GRAY).to_edge(UP * 8+LEFT*1)
        sub_title6 = Text("1kg    =  1000g", font_size=29).to_edge(UP * 9.25+LEFT*6)
        sub_title7 = Text("=  1000g × 1000mg/g = 1,000,000mg", font_size=29).to_edge(UP * 10.5+LEFT*8)
        sub_title8 = Text("similarly, calculating the number of  milli litres in 1 killo litre :", font_size=29, color=PURPLE).to_edge(UP * 12+LEFT *1)
        sub_title9 = Text("1kL   =  1000L", font_size=29).to_edge(UP * 13.25+LEFT*6)
        sub_title10 = Text("= 1000L × 1000mL/L = 1,000,000mL", font_size=29).to_edge(UP * 14.5+LEFT*7.8)

        self.play(Write(title))
        self.wait(2)
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(2)
        self.play(Write(sub_title3))
        self.wait(2)
        self.play(Write(sub_title4))
        self.wait(2)
        self.play(Write(sub_title5))
        self.wait(2)
        self.play(Write(sub_title6))
        self.wait(2)
        self.play(Write(sub_title7))
        self.wait(2)
        self.play(Write(sub_title8))
        self.wait(2)
        self.play(Write(sub_title9))
        self.wait(2)
        self.play(Write(sub_title10))
        
        self.play(FadeOut(sub_title10),FadeOut(sub_title9),FadeOut(sub_title8),FadeOut(sub_title7),FadeOut(sub_title6), FadeOut(sub_title5), FadeOut(sub_title4), FadeOut(sub_title3), FadeOut(sub_title2), FadeOut(sub_title1), FadeOut(title))


        #title
        title = Text("Example : ", font_size=30, color=BLUE).to_edge(UP * 1+LEFT*1)
        sub_title1 = Text("A hotel has 15 litres milk. 25ml of milk is required to prepare a cup of tea.", font_size=29).to_edge(UP * 2.5+LEFT*1)
        sub_title2 = Text("How many cups of tea can be made with the milk ?", font_size=27).to_edge(UP * 4+LEFT*1)
        sub_title3 = Text("Solution:    Quantity of milk in the hotel    =  15 litre", font_size=29).to_edge(UP * 6.25+LEFT *1)
        sub_title4 = Text("=   15 × 1000", font_size=29).to_edge(UP * 7.75+LEFT *16)
        sub_title5 = Text("=  15000 ml.", font_size=29).to_edge(UP * 9.25+LEFT*16)
        sub_title6 = Text("Since 25ml. of milk is required for each cup of tea", font_size=29).to_edge(UP * 10.75 + LEFT* 1.5)
        sub_title7 = Text("number of cups of tea that can be made = 15000 ÷ 25", font_size=29).to_edge(UP * 12.25+LEFT *1.5)
        sub_title8 = Text("=    600 cups.", font_size=29).to_edge(UP * 14+LEFT *16.25)


        self.play(Write(title))
        self.wait(2)
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(2)
        self.play(Write(sub_title3))
        self.wait(2)
        self.play(Write(sub_title4))
        self.wait(2)
        self.play(Write(sub_title5))
        self.wait(2)
        self.play(Write(sub_title6))
        self.wait(2)
        self.play(Write(sub_title7))
        self.wait(2)
        self.play(Write(sub_title8))
        self.wait(2)
    
        self.play(FadeOut(sub_title8),FadeOut(sub_title7),FadeOut(sub_title6), FadeOut(sub_title5), FadeOut(sub_title4), FadeOut(sub_title3), FadeOut(sub_title2), FadeOut(sub_title1), FadeOut(title))


    def SetDeveloperList(self):  
        self.DeveloperList="Raghu"

        
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="KnowingourNumbers.py"







if __name__ == "__main__":
    scene = KnowingNumbers()
    scene.render()
