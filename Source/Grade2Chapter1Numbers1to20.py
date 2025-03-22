from manim import *
from AbstractAnim import AbstractAnim
import cvo

class Grade2Chapter1Numbers1to20(AbstractAnim):

    def construct(self):

        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.numbdef()
        self.fadeOutCurrentScene()
        self.six()
        self.fadeOutCurrentScene()
        self.eight()
        self.fadeOutCurrentScene()
        self.count()
        self.fadeOutCurrentScene()
        self.numb()
        self.fadeOutCurrentScene()
        self.roundnumbers()
        self.fadeOutCurrentScene()
        self.smallbig()
        self.fadeOutCurrentScene() 
        self.GithubSourceCodeReference()


    def numbdef(self):

        p10 = cvo.CVO().CreateCVO("Numbers", "").setPosition([-3,1,0])
        p11 = cvo.CVO().CreateCVO("Definition", "A symbol representing quantity or amount").setPosition([3,1,0])
        p10.cvolist.append(p11)
        self.construct1(p10,p10)


    def six(self):

        text =  Text("Look at the picture given below. Answer the following questions.",color=RED)
        text.scale(0.5)
        text.to_edge(UP)
        self.play(Write(text))
        self.wait(2)
        
        emoji1_path = "media\images\man1.svg"
        emoji2_path = "media\images\man1.svg"
        emoji3_path = "media\images\man1.svg"
        emoji4_path = "media\images\man1.svg"
        emoji5_path = "media\images\man1.svg"
        emoji6_path = "media\images\man1.svg"

        radius = 0.8

        emojis_1 = SVGMobject(emoji1_path).scale(radius)
        emojis_2 = SVGMobject(emoji2_path).scale(radius)
        emojis_3 = SVGMobject(emoji3_path).scale(radius)
        emojis_4 = SVGMobject(emoji4_path).scale(radius)
        emojis_5 = SVGMobject(emoji5_path).scale(radius)
        emojis_6 = SVGMobject(emoji6_path).scale(radius)

        emojis_1.shift(LEFT * 5 + UP * 2)
        emojis_2.next_to(emojis_1, RIGHT, buff=0.7)
        emojis_3.next_to(emojis_2, RIGHT, buff=0.7)
        emojis_4.next_to(emojis_3, RIGHT, buff=0.7)
        emojis_5.next_to(emojis_4, RIGHT, buff=0.7)
        emojis_6.next_to(emojis_5, RIGHT, buff=0.7)


        self.play(FadeIn(emojis_1), FadeIn(emojis_2), FadeIn(emojis_3), FadeIn(emojis_4), FadeIn(emojis_5), FadeIn(emojis_6))
        self.wait(2)

        # Add text below each image
        text1 = Text("Ranga").next_to(emojis_1, DOWN).scale(0.6)
        text2 = Text("John").next_to(emojis_2, DOWN).scale(0.6)
        text3 = Text("Latha").next_to(emojis_3, DOWN).scale(0.6)
        text4 = Text("Basha").next_to(emojis_4, DOWN).scale(0.6)
        text5 = Text("Rama").next_to(emojis_5, DOWN).scale(0.6)
        text6 = Text("Uma").next_to(emojis_6, DOWN).scale(0.6)  # Add text for additional images

        self.play(Write(text1), Write(text2), Write(text3), Write(text4), Write(text5), Write(text6))
        self.wait(2)

        #question1
        textq1 = Text("Question: Who is the third student? ", color=BLUE)
        textq1.scale(0.5)
        textq1.shift(DOWN  * 2)
        self.play(Write(textq1))
        self.wait(1)

        number1 = Text("1").scale(2).next_to(text1, DOWN).scale(0.7)
        number2 = Text("2").scale(2).next_to(text2, DOWN).scale(0.7)
        number3 = Text("3").scale(2).next_to(text3, DOWN).scale(0.7)
        
        
        # Animation sequence
        self.play(FadeIn(number1))
        self.wait(1)
        self.play(FadeIn(number2))
        self.wait(1)
        self.play(FadeIn(number3))
        self.wait(1)

        texta1 = Text("Answer: Latha is the third student")
        texta1.scale(0.5)
        texta1.shift(DOWN  * 3)
        self.play(Write(texta1))
        self.wait(2)



    def eight(self):

        text = Text("Look at the picture given below. Write the ordinal number of the student shown")
        text.scale(0.5)
        text.to_edge(UP)
        self.play(Write(text))
        self.wait(2)
        
        emoji1_path = "media\images\man1.svg"
        emoji2_path = "media\images\man1.svg"
        emoji3_path = "media\images\man1.svg"
        emoji4_path = "media\images\man1.svg"
        emoji5_path = "media\images\man1.svg"
        emoji6_path = "media\images\man1.svg"
        emoji7_path = "media\images\man1.svg"
        emoji8_path = "media\images\man1.svg"

        radius = 0.7

        emojis_1 = SVGMobject(emoji1_path).scale(radius)
        emojis_2 = SVGMobject(emoji2_path).scale(radius)
        emojis_3 = SVGMobject(emoji3_path).scale(radius)
        emojis_4 = SVGMobject(emoji4_path).scale(radius)
        emojis_5 = SVGMobject(emoji5_path).scale(radius)
        emojis_6 = SVGMobject(emoji6_path).scale(radius)
        emojis_7 = SVGMobject(emoji7_path).scale(radius)
        emojis_8 = SVGMobject(emoji8_path).scale(radius)

        emojis_1.shift(LEFT * 5.25 + UP * 2)
        emojis_2.next_to(emojis_1, RIGHT, buff=0.5)
        emojis_3.next_to(emojis_2, RIGHT, buff=0.5)
        emojis_4.next_to(emojis_3, RIGHT, buff=0.5)
        emojis_5.next_to(emojis_4, RIGHT, buff=0.5)
        emojis_6.next_to(emojis_5, RIGHT, buff=0.5)
        emojis_7.next_to(emojis_6, RIGHT, buff=0.5)
        emojis_8.next_to(emojis_7, RIGHT, buff=0.5)


        self.play(FadeIn(emojis_1), FadeIn(emojis_2), FadeIn(emojis_3), FadeIn(emojis_4), FadeIn(emojis_5), FadeIn(emojis_6), FadeIn(emojis_7), FadeIn(emojis_8))
        self.wait(2)

        # Add text below each image
        text1 = Text("Sita").next_to(emojis_1, DOWN).scale(0.5)
        text2 = Text("Hari").next_to(emojis_2, DOWN).scale(0.5)
        text3 = Text("Ramaa").next_to(emojis_3, DOWN).scale(0.5)
        text4 = Text("Giri").next_to(emojis_4, DOWN).scale(0.5)
        text5 = Text("Latha").next_to(emojis_5, DOWN).scale(0.5)
        text6 = Text("Uma").next_to(emojis_6, DOWN).scale(0.5)
        text7 = Text("Shiva").next_to(emojis_7, DOWN).scale(0.5)
        text8 = Text("Usha").next_to(emojis_8, DOWN).scale(0.5)  # Add text for additional images

        self.play(Write(text1), Write(text2), Write(text3), Write(text4), Write(text5), Write(text6), Write(text7), Write(text8))
        self.wait(2)



        textq1 = Text("question: What is the ordinal number of Latha ? ")
        textq1.scale(0.4)
        textq1.shift(DOWN * 2)
        self.play(Write(textq1))
        self.wait(1)

        number1 = Text("1").scale(2).next_to(text1, DOWN).scale(0.7)
        number2 = Text("2").scale(2).next_to(text2, DOWN).scale(0.7)
        number3 = Text("3").scale(2).next_to(text3, DOWN).scale(0.7)
        number4 = Text("4").scale(2).next_to(text4, DOWN).scale(0.7)
        number5 = Text("5").scale(2).next_to(text5, DOWN).scale(0.7)
        
        
        # Animation sequence
        self.play(FadeIn(number1))
        self.wait(1)
        self.play(FadeIn(number2))
        self.wait(1)
        self.play(FadeIn(number3))
        self.wait(1)
        self.play(FadeIn(number4))
        self.wait(1)
        self.play(FadeIn(number5))
        self.wait(1)

        texta1 = Text("Answer: Fifth(5th) is the ordinal number of Latha")
        texta1.scale(0.5)
        texta1.shift(DOWN  * 3)
        self.play(Write(texta1))
        self.wait(3)


    def count(self):

        text =  Text("Count the circles. Circle the correct number.",color=RED)
        text.scale(0.5)
        text.to_edge(UP)
        self.play(Write(text))
        self.wait(2)

        names = ["A", "B", "C", "D", "E", "F", "G", "H"]
        
        # Define the starting position and spacing
        start_pos = LEFT * 5.5 + UP * 1.5  # Move circles up by 1 unit and shift to the left
        spacing = RIGHT * 1.5
        
        # Create circles with text
        circles = []
        for i, name in enumerate(names):
            pos = start_pos + i * spacing
            circle = Circle(radius=0.7, color=WHITE).move_to(pos)
            text = Text(name).scale(0.5).move_to(pos)
            circles.append(VGroup(circle, text))
        
        # Add the circles to the scene
        for circle in circles:
            self.play(Create(circle))
        
        # Hold the final frame
        self.wait(1)


        number_7 = Text("7").shift(LEFT * 2 + DOWN )
        number_8 = Text("8").shift(DOWN)
        number_9 = Text("9").shift(RIGHT * 2 + DOWN )

        # Create a circle to highlight number 8
        circle = Circle(color=RED).surround(number_8)

        # Display the numbers
        self.play(Write(number_7), Write(number_8), Write(number_9))
        self.wait(1)

        # Circle the number 8
        self.play(Create(circle))
        self.wait(3)

    def numb(self):

        text = Text("Write the missing numbers in the sequence")
        text.scale(0.5)
        text.to_edge(UP)
        self.play(Write(text))
        self.wait(2)
        
        numbers = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
        ]

        initial_numbers = {1, 2, 5, 6, 8, 11, 16, 20}
        all_numbers = set(range(1, 21))
        missing_numbers = all_numbers - initial_numbers

        grid = VGroup()
        for row in numbers:
            row_group = VGroup()
            for num in row:
                num_text = Text(str(num))
                if num not in initial_numbers:
                    num_text.set_opacity(0)  # Initially invisible

                box = Square(side_length=1)
                num_text.move_to(box.get_center())
                box_group = VGroup(box, num_text)
                row_group.add(box_group)
            row_group.arrange(RIGHT, buff=0.5)
            grid.add(row_group)

        grid.arrange(DOWN, buff=0.5)

        self.play(FadeIn(grid))
        self.wait(2)

# Animate the missing numbers sequentially
        animations = []
        for i, row in enumerate(numbers):
            for j, num in enumerate(row):
                if num in missing_numbers:
            # Access the correct element in the flattened grid
                    box_group = grid[i][j]  # Get the box_group which contains the Square and Text
                    num_text = box_group[1]  # Get the Text object
                    animations.append(num_text.animate.set_opacity(1).set_color(RED))

# Play animations sequentially
        for anim in animations:
            self.play(anim)
            self.wait(0.5)

        self.wait(2)

    def roundnumbers(self):

        text = Text("Draw a triangle around each number between 10 and 20 and circle around each number less than 10")
        text.scale(0.4)
        text.to_edge(UP)
        self.play(Write(text))
        self.wait(2)

        # Create a matrix of numbers from 1 to 20
        numbers = [[i + j*5 + 1 for i in range(5)] for j in range(4)]
        
        # Create a matrix of MathTex objects
        matrix_tex = [[MathTex(str(number)) for number in row] for row in numbers]
        
        # Create VGroups for each row and then a VGroup for the entire matrix
        rows = [VGroup(*row).arrange(RIGHT, buff=1) for row in matrix_tex]
        matrix = VGroup(*rows).arrange(DOWN, buff=1)
        
        # Center the matrix on the screen
        matrix.move_to(ORIGIN)
        
        # Add the numbers to the scene
        for row in matrix_tex:
            for number in row:
                self.add(number)
        
        self.wait(1)
        
        # Draw triangles around numbers between 10 and 20
        for row in matrix_tex:
            for number in row:
                num = int(number.get_tex_string())
                if 10 < num < 20:
                    triangle = Polygon(
                        number.get_center() + UP * 0.5,
                        number.get_center() + LEFT * 0.5 + DOWN * 0.5,
                        number.get_center() + RIGHT * 0.5 + DOWN * 0.5,
                        color=BLUE
                    )
                    self.play(Create(triangle))
        
        self.wait(1)
        
        # Numbers to circle
        circle_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        # Draw circles around specific numbers
        for row in matrix_tex:
            for number in row:
                num = int(number.get_tex_string())
                if num in circle_numbers:
                    circle = Circle(radius=0.5, color=RED).move_to(number.get_center())
                    self.play(Create(circle))
        
        self.wait(3)


    def smallbig(self):

        text = Text("Write numbers in small to big order and big to small order")
        text.scale(0.5)
        text.to_edge(UP)
        self.play(Write(text))
        self.wait(2)

        text1 = Text("Given Numbers : 6, 0, 8, 3, 5, 2")
        text1.scale(0.75)
        text1.shift(UP)
        self.play(Write(text1))
        self.wait(1)

        text2 = Text("Big to small order : 8, 6, 5, 3, 2, 0")
        text2.scale(0.75)
        #text1.shift(UP)
        self.play(Write(text2))
        self.wait(1)

        text3 = Text("Small To Big order : 0, 2, 3, 5, 6, 8")
        text3.scale(0.75)
        text3.shift(DOWN)
        self.play(Write(text3))
        self.wait(2)




    def SetDeveloperList(self):
        self.DeveloperList="SURADHYA REDDY"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade2Chapter1Numbers1to20.py"



if __name__ == "__main__":
    scene = Grade2Chapter1Numbers1to20()
    scene.render()