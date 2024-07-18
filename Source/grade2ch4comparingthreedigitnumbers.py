from manim import *
from AbstractAnim import AbstractAnim

import cvo

class comparingthreedigitnumbers(AbstractAnim):

    def construct(self):
        # p1=cvo.CVO().CreateCVO("cname","oname")
        #self.RenderSkillbancLogo()
        #self.fadeOutCurrentScene()
        self.introduction()
        self.fadeOutCurrentScene()
        #self.addition_1()
        #self.fadeOutCurrentScene()
        #self.Addition()
        #self.fadeOutCurrentScene()
        #self.comparing()
        #self.fadeOutCurrentScene()
        #self.comparing1()
        #self.fadeOutCurrentScene()
        #self.comparing2()
        #self.fadeOutCurrentScene()
        #self.compare()
        #self.fadeOutCurrentScene()
        #self.compare1()
        #self.fadeOutCurrentScene()
        #self.compare2()
        #self.fadeOutCurrentScene()
        #self.GithubSourceCodeReference()

    def introduction(self):
        # p1=cvo.CVO().CreateCVO("cname","oname")
        
        p10=cvo.CVO().CreateCVO("Comparing Three-Digit Numbers", "").setPosition([-3,-1,0])
        p11=cvo.CVO().CreateCVO("For comparing Three-Digit Numbers",">,<,=").setPosition([-4,2,0])
        p12=cvo.CVO().CreateCVO("Greater Than",">").setPosition([0,2.5,0])
        p13=cvo.CVO().CreateCVO("Equals to","=").setPosition([3,1.5,0])
        p14=cvo.CVO().CreateCVO("Less than","<").setPosition([4,-1,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
         
        self.construct1(p10,p10)


    def addition_1(self):
        # Display the title
        number = Text("Comparing Three-Digit Numbers", font_size=40, color=BLUE).to_edge(UP * 1)
        self.play(Write(number))
        
        # Explain Place Values
        place_value_text = Text("First, let's recall place values:", font_size=30).shift(UP * 2)
        self.play(Write(place_value_text))
        self.wait(2)

        # Example Number 1
        number1 = 456
        number1_text = Text(f"Number: {number1}", font_size=35).shift(UP * 1)
        self.play(Write(number1_text))
        self.wait(1)

        # Breakdown of Number 1
        hundreds1 = number1 // 100
        tens1 = (number1 // 10) % 10
        ones1 = number1 % 10

        hundreds1_text = Text(f"Hundreds place: {hundreds1}", font_size=29).shift(LEFT * 3.5)
        tens1_text = Text(f"Tens place: {tens1}", font_size=29)
        ones1_text = Text(f"Ones place: {ones1}", font_size=29).shift(RIGHT * 3)

        # Display the place values in sequence
        self.play(Write(hundreds1_text))
        self.wait(1)
        self.play(Write(tens1_text))
        self.wait(1)
        self.play(Write(ones1_text))
        self.wait(2)

        # Fade out all elements
        self.play(
            FadeOut(hundreds1_text),
            FadeOut(tens1_text),
            FadeOut(ones1_text),
            FadeOut(number1_text),
            FadeOut(place_value_text),
            FadeOut(number)
        )


    def Addition(self):

        sub_title1 = Text("For comparing three digit numbers there are three conditions:",font_size=29, color=BLUE).to_edge(UP*1.5 + LEFT * 1)       
        sub_title2 = MarkupText("<span foreground='PURPLE'>condition-1:</span>  In 3-digit numbers, if the hundreds are not equal,",font_size=29).to_edge(UP*3.5 + LEFT * 1)
        sub_title3 = Text("the one with more hundreds is bigger"'.',font_size=29).to_edge(UP*5 + LEFT * 5.5)
        sub_title4 = MarkupText("<span foreground='PURPLE'>condition-2:</span> In 3-digit numbers, if the hundreds are equal,",font_size=29).to_edge(UP*7 + LEFT * 1)
        sub_title5 = Text("the one with more tens is bigger"'.',font_size=29).to_edge(UP*8.5 + LEFT * 5.5)
        sub_title6 = MarkupText("<span foreground='PURPLE'>condition-3:</span> In 3-digit numbers, if the hundreds and tens are equal,",font_size=29).to_edge(UP*10.5 + LEFT * 1)
        sub_title7 = Text("the one with more ones is bigger"'.',font_size=29).to_edge(UP*12+ LEFT * 5.5)


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
    

    def comparing(self):
         Example = MarkupText("<span foreground='PURPLE'>Example1:</span> One day two friends sold vegetables at the weekly market.",font_size=30).to_edge(UP*1.25 + LEFT * 1)
         Radha = Text("Radha Earned 452",font_size=30).to_edge(UP*4 + LEFT * 1)
         Sita = Text("Sita earned 381",font_size=30).to_edge(UP*4 + RIGHT * 4)       
         sub_title2 = Text("In 452, there are 4 hundreds"'.',font_size=29).to_edge(UP*5.5 + LEFT * 1)
         sub_title3 = Text("In 381, there are 3 hundreds"'.',font_size=29).to_edge(UP*5.5 + RIGHT * 1)
         sub_title4 = Text("Rs.300 is less than Rs.400, It means Radha earned more",font_size=29).to_edge(UP*7)
         sub_title5 = Text("Rs.452 is greater than Rs.381, that is 452 > 381",font_size=29).to_edge(UP*8.5)
         sub_title6 = Text("or",font_size=29).to_edge(UP*10)
         sub_title7 = Text("Rs.381 is less than Rs.452, that is 381 < 452",font_size=29).to_edge(UP*11.5)
         
         self.play(Write(Example))
         self.wait(1)
         self.play(Write(Radha))
         self.play(Write(Sita))
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


    def comparing1(self):
         Example = MarkupText("<span foreground='PURPLE'>Example2:</span> Another day two friends sold vegetables at the weekly market.",font_size=30).to_edge(UP*1.25 + LEFT * 1)
         Radha = Text("Radha Earned 216",font_size=30).to_edge(UP*4 + LEFT * 1)
         Sita = Text("Sita earned 216",font_size=30).to_edge(UP*4 + RIGHT * 4)       
         sub_title2 = Text("In both cases hundreds,tens and onces are equal"'.',font_size=29).to_edge(UP*5.5)
         sub_title3 = Text("It means they earned equally",font_size=29).to_edge(UP*7)
         sub_title4 = Text("216 = 216",font_size=29).to_edge(UP*8.5)
         
         self.play(Write(Example))
         self.wait(1)
         self.play(Write(Radha))
         self.play(Write(Sita))
         self.wait(1)
         self.play(Write(sub_title2))
         self.wait(1)
         self.play(Write(sub_title3))
         self.wait(1)
         self.play(Write(sub_title4))
         self.wait(1)
    

    def comparing2(self):
         Example = MarkupText("<span foreground='PURPLE'>Example3:</span> Another day two friends sold vegetables at the weekly market.",font_size=30).to_edge(UP*1.25 + LEFT * 1)
         Radha = Text("Radha Earned 381",font_size=30).to_edge(UP*4 + LEFT * 1)
         Sita = Text("Sita earned 452",font_size=30).to_edge(UP*4 + RIGHT * 4)       
         sub_title2 = Text("In 381, there are 3 hundreds"'.',font_size=29).to_edge(UP*5.5 + LEFT * 1)
         sub_title3 = Text("In 452, there are 4 hundreds"'.',font_size=29).to_edge(UP*5.5 + RIGHT * 1)
         sub_title4 = Text("Rs.300 is less than Rs.400, It means Sita earned more",font_size=29).to_edge(UP*7)
         sub_title5 = Text("Rs.381 is less than Rs.452, that is 381 < 452",font_size=29).to_edge(UP*8.5)
         sub_title6 = Text("or",font_size=29).to_edge(UP*10)
         sub_title7 = Text("Rs.452 is greater than Rs.381, that is 452 > 381",font_size=29).to_edge(UP*11.5)
         
         self.play(Write(Example))
         self.wait(1)
         self.play(Write(Radha))
         self.play(Write(Sita))
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

    
    def compare(self):
        # Title
        title = Text("Select the appropriate symbol: <, >, =", font_size=36,color=BLUE).to_edge(UP * 1)
        self.play(Write(title))
        self.wait(1)


        # Comparison problems and results
        problems = [
            (620, 580),   # (A)
            (937, 975),   # (B)
            (520, 520),   # (E)
            (987, 965),   # (F)
            (736, 746),   # (G)
            (864, 864),   # (H)
        ]

        results = [
            ">",  # (A)
            "<",  # (B)
            "=",  # (E)
            ">",  # (F)
            "<",  # (G)
            "=",  # (H)
        ]

        # Positioning
        start_y = 2  # Adjusted start_y to move everything down
        offset_y = -1
        x_positions = [-3, 0, 3]

        for i, (nums, result) in enumerate(zip(problems, results)):
            # Create texts
            num1_text = Text(str(nums[0]), font_size=36).move_to(x_positions[0] * RIGHT + start_y * UP + i * offset_y * UP)
            num2_text = Text(str(nums[1]), font_size=36).move_to(x_positions[2] * RIGHT + start_y * UP + i * offset_y * UP)
            result_text = Text(result, font_size=36)
            
            # Create a box for the result symbol
            box = SurroundingRectangle(result_text, color=BLUE, buff=0.2)

            # Position result text and box
            result_text.move_to(x_positions[1] * RIGHT + start_y * UP + i * offset_y * UP)
            box.move_to(result_text.get_center())

            # Animate texts and boxes
            self.play(Write(num1_text))
            self.play(Write(num2_text))
            self.wait(0.5)
            self.play(Create(box))
            self.wait(2)
            self.play(Write(result_text))
            self.wait(0.5)

        self.wait(2)

        # Render the scene
        config.pixel_height = 1080
        config.pixel_width = 1920
        config.frame_height = 8.0
        config.frame_width = 14.0


    def compare1(self):  

        heading = Text("Ascending  order :",color=DARK_BROWN,font_size=37).to_edge(UP*1.25+LEFT * 1)
        sub_title1 = Text("Ascending order is the arrangement of elements from smallest to largest.",font_size=29).to_edge(UP*3)
        sub_title2 = Text("example:  58 , 95 , 96 , 44 ",font_size=29).to_edge(UP*4.75)
        sub_title3 = Text("Ascending  order is     44 , 58 , 95 , 96",font_size=29).to_edge(UP*6.6)
        heading2 = Text("Descending order :",color=PINK,font_size=37).to_edge(UP*9+LEFT * 1)
        sub_title5 = Text("Descending order is the arrangement of elements from largest to smallest.",font_size=29).to_edge(UP*10.5)
        sub_title6 = Text("example:   58 , 95 , 96 , 44 ",font_size=29).to_edge(UP*12)
        sub_title7 = Text("Descending order is     96 , 95 , 58 , 44",font_size=29).to_edge(UP*13.5)
        
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
    
    def compare2(self):
        # Title
        title = Text("The three-Digit Numbers using 7, 8, and 9", font_size=36).to_edge(UP*1.2)
        self.play(Write(title))
        self.wait(1)

        # Digits to use
        digits = [7, 8, 9]
        
        # Calculate all permutations of three-digit numbers
        permutations = []
        for i in digits:
            for j in digits:
                for k in digits:
                    permutations.append(f"{i}{j}{k}")

        # Positioning
        start_y = 2  # Adjusted start_y to move everything down
        start_x = -6
        offset_y = -1
        offset_x = 2

        # Display the numbers
        for index, number in enumerate(permutations):
            num_text = Text(number, font_size=24).shift(UP*1)
            num_text.move_to(start_x * RIGHT + (start_y + (index // 8) * offset_y) * UP + (index % 8) * offset_x * RIGHT)
            box = SurroundingRectangle(num_text, color=BLUE, buff=0.2)
            self.play(Write(num_text), Create(box))
            self.wait(0.2)
        
        self.wait(2)

        # Render the scene
        config.pixel_height = 1080
        config.pixel_width = 1920
        config.frame_height = 8.0
        config.frame_width = 14.0 

    def SetDeveloperList(self):  
        self.DeveloperList="Akshitha"

        
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="comparingthreedigitnumbers.py"
        
if __name__ == "__main__":
    scene = comparingthreedigitnumbers()
    scene.render()