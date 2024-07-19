from manim import *
from AbstractAnim import AbstractAnim
import cvo

class numbers(AbstractAnim):

    def construct(self):

        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.six()
        self.fadeOutCurrentScene()
        self.eight()
        self.fadeOutCurrentScene()
        self.count()
        self.fadeOutCurrentScene()


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
        textq1 = Text("1. Who is the third student? ", color=BLUE)
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

        texta1 = Text("Ans: Latha")
        texta1.shift(DOWN  * 3)
        self.play(Write(texta1))
        self.wait(3)



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



        textq1 = Text("What is the ordinal number of Latha ? ")
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

        texta1 = Text("Ans: Fifth(5th)")
        texta1.shift(DOWN  * 3)
        self.play(Write(texta1))
        self.wait(3)


    def count(self):

        text =  Text("Count the pictures. Circle the correct number.",color=RED)
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

    #def number(self):

        



if __name__ == "__main__":
    scene = numbers()
    scene.render()