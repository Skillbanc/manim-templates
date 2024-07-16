
from manim import *
from AbstractAnim import AbstractAnim
import cvo


class Grade1chapter4Numbersfrom6to9(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.c1c2()
        self.fadeOutCurrentScene()
        self.WriteNumbersWithWords()
        self.fadeOutCurrentScene()
        self.Matching()
        self.fadeOutCurrentScene()
        self.Same_Number_of_Dots()
        self.fadeOutCurrentScene()
        self.CircleWithTrianglesAndStars()
        self.fadeOutCurrentScene()
        self.MoveImage()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

        
    def c1c2(self):
        self.isRandom = False
        self.positionChoice = [[0, 2.5, 0],[-6,0,0],[-3,-2,0],[3,-2,0], [6, 0, 0]]
        p10 = cvo.CVO().CreateCVO("Numbers from 6 to 9", "Numbers")
        p11 = cvo.CVO().CreateCVO("", "6")
        p12 = cvo.CVO().CreateCVO("", "7")
        p13 = cvo.CVO().CreateCVO("", "8")
        p14 = cvo.CVO().CreateCVO("", "9")

        p10.setcircleradius(1.25)
        p11.setcircleradius(1.25)
        p12.setcircleradius(1.25)
        p13.setcircleradius(1.25)
        p14.setcircleradius(1.25) 
        
        p10.cvolist.append(p11)
        p10.cvolist.append(p12) 
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)

        self.construct1(p10, p10)
        self.wait(1)
        self.fadeOutCurrentScene()

    def WriteNumbersWithWords(self):
        # Define the numbers and their words
        numbers_and_words = [
            ("6", "Six"),
            ("7", "Seven"),
            ("8", "Eight"),
            ("9", "Nine")
        ]

        # Position the numbers and words
        for i, (num, word) in enumerate(numbers_and_words):
            # Create Text objects for numbers and words
            number_text = Text(num, font_size=96, color=BLUE)
            word_text = Text(word, font_size=48, color=GREEN)

            # Position the number and word
            number_text.move_to(UP * 1.5)
            word_text.next_to(number_text, DOWN)

            # Animate the writing of each number and word
            self.play(Write(number_text))
            self.wait(0.5)
            self.play(Write(word_text))
            self.wait(1)  # Pause for a second before moving to the next number

            # Fade out the number and word to make space for the next
            self.play(FadeOut(number_text), FadeOut(word_text))

    def Matching(self):
        self.title()
        self.construct2()
        self.construct3()
        self.construct4()
        self.construct5()
        self.construct6()
        self.construct7()
        self.construct8()
        self.construct9()
        self.add_matching_lines()
  
    def title(self):
        title = Text("Count the pictures on the left.\nMatch them with the same pictures on the right.", font_size=24)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(2)

    def construct2(self):
        self.t2 = Text('🕯️🕯️🕯️🕯️🕯️', font_size=28).move_to([-3, 2, 0])
        self.play(FadeIn(self.t2))

    def construct3(self):
        self.t3 = Text('⚽⚽⚽⚽⚽', font_size=28).move_to([-3, 0.5, 0])
        self.play(FadeIn(self.t3))

    def construct4(self):
        self.t4 = Text('⭐⭐⭐⭐⭐⭐', font_size=28).move_to([-3, -1, 0])
        self.play(FadeIn(self.t4))

    def construct5(self):
        self.t5 = Text('🌹🌹🌹🌹🌹🌹', font_size=28).move_to([-3, -2.5, 0])
        self.play(FadeIn(self.t5))

    def construct6(self):
        self.t6 = Text('⚽⚽⚽⚽⚽', font_size=28).move_to([3, 2, 0])
        self.play(FadeIn(self.t6))

    def construct7(self):
        self.t7 = Text('🕯️🕯️🕯️🕯️🕯️', font_size=28).move_to([3, 0.5, 0])
        self.play(FadeIn(self.t7))

    def construct8(self):
        self.t8 = Text('🌹🌹🌹🌹🌹🌹', font_size=28).move_to([3, -1, 0])
        self.play(FadeIn(self.t8))

    def construct9(self):
        self.t9 = Text('⭐⭐⭐⭐⭐⭐', font_size=28).move_to([3, -2.5, 0])
        self.play(FadeIn(self.t9))

    def add_matching_lines(self):
        # Draw lines to match
        lines = [
            Line(self.t2.get_right(), self.t7.get_left(), color=YELLOW),
            Line(self.t3.get_right(), self.t6.get_left(), color=YELLOW),
            Line(self.t4.get_right(), self.t9.get_left(), color=YELLOW),
            Line(self.t5.get_right(), self.t8.get_left(), color=YELLOW),
        ]

        for line in lines:
            self.play(Create(line))
            self.wait(0.5)  # Pause for a short time to make the animation smoother

    def Same_Number_of_Dots(self):
        self.add_title()
        self.construct10()
        self.construct11()
        self.construct12()
        self.construct13()
        self.construct14()
        self.construct15()
        self.construct16()
        self.construct17()
        self.add_matching_lines()

    def add_title(self):
        title = Text("Count the pictures in each box on the left.\nMatch them with the same number of dots on the right.", font_size=24)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(2)

    def construct10(self):
        self.t2 = Text('🐟🐟🐟🐟🐟🐟', font_size=28).move_to([-3, 2, 0])
        self.play(FadeIn(self.t2))

    def construct11(self):
        self.t3 = Text('🪑🪑🪑🪑🪑🪑🪑', font_size=28).move_to([-3, 0.5, 0])
        self.play(FadeIn(self.t3))

    def construct12(self):
        self.t4 = Text('🕛🕛🕛🕛🕛🕛🕛🕛', font_size=28).move_to([-3, -1, 0])
        self.play(FadeIn(self.t4))

    def construct13(self):
        self.t5 = Text('⚾⚾⚾⚾⚾⚾⚾⚾⚾', font_size=28).move_to([-3, -2.5, 0])
        self.play(FadeIn(self.t5))

    def construct14(self):
        self.t6 = Text('⚪⚪⚪⚪⚪⚪⚪', font_size=28).move_to([3, 2, 0])
        self.play(FadeIn(self.t6))

    def construct15(self):
        self.t7 = Text('⚪⚪⚪⚪⚪⚪', font_size=28).move_to([3, 0.5, 0])
        self.play(FadeIn(self.t7))

    def construct16(self):
        self.t8 = Text('⚪⚪⚪⚪⚪⚪⚪⚪⚪', font_size=28).move_to([3, -1, 0])
        self.play(FadeIn(self.t8))

    def construct17(self):
        self.t9 = Text('⚪⚪⚪⚪⚪⚪⚪⚪', font_size=28).move_to([3, -2.5, 0])
        self.play(FadeIn(self.t9))

    def add_matching_lines(self):
        # Draw lines to match
        lines = [
            Line(self.t2.get_right(), self.t7.get_left(), color=YELLOW),
            Line(self.t3.get_right(), self.t6.get_left(), color=YELLOW),
            Line(self.t4.get_right(), self.t9.get_left(), color=YELLOW),
            Line(self.t5.get_right(), self.t8.get_left(), color=YELLOW),
        ]

        for line in lines:
            self.play(Create(line))
            self.wait(0.5)  # Pause for a short time to make the animation smoother


    def CircleWithTrianglesAndStars(self):
        # Title
        title = Tex("Count the things in each circle in each row. Put a tick mark at the circle where the number of things are different.").scale(0.8).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Create circles for the first row
        circles_row1 = VGroup(
            Circle().set_color(WHITE),
            Circle().set_color(WHITE),
            Circle().set_color(WHITE),
            Circle().set_color(WHITE)
        ).arrange(RIGHT, buff=1.5).shift(UP * 1.2)
        
        # Add triangles to circles in the first row
        triangles_sets = [
            [Triangle().scale(0.2) for _ in range(4)],
            [Triangle().scale(0.2) for _ in range(4)],
            [Triangle().scale(0.2) for _ in range(4)],
            [Triangle().scale(0.2) for _ in range(5)]  # 5 triangles for the fourth circle
        ]
        
        for circle, triangles in zip(circles_row1, triangles_sets):
            for triangle in triangles:
                triangle.move_to(circle.get_center() + triangle.get_center())
            VGroup(*triangles).arrange_in_grid(buff=0.2).move_to(circle)
        
        # Animate the creation of the circles and triangles in the first row
        self.play(*[Create(circle) for circle in circles_row1])
        self.wait(1)
        
        triangle_animations = []
        for triangles in triangles_sets:
            triangle_animations.extend([Create(triangle) for triangle in triangles])
        self.play(*triangle_animations)
        self.wait(1)
        
        # Add a tick mark to the fourth circle in the first row
        tick_mark1 = Tex(r"\checkmark").set_color(GREEN).scale(2).next_to(circles_row1[3], UP, buff=0)
        self.play(Write(tick_mark1))
        self.wait(1)

        # Create circles for the second row
        circles_row2 = VGroup(
            Circle().set_color(WHITE),
            Circle().set_color(WHITE),
            Circle().set_color(WHITE),
            Circle().set_color(WHITE)
        ).arrange(RIGHT, buff=1.5).shift(DOWN * 2)
        
        # Add stars to circles in the second row
        stars_sets = [
            [Star().scale(0.2) for _ in range(6)],
            [Star().scale(0.2) for _ in range(5)],  # 5 stars for the second circle
            [Star().scale(0.2) for _ in range(6)],
            [Star().scale(0.2) for _ in range(6)]
        ]
        
        for circle, stars in zip(circles_row2, stars_sets):
            for star in stars:
                star.move_to(circle.get_center() + star.get_center())
            VGroup(*stars).arrange_in_grid(buff=0.2).move_to(circle)
        
        # Animate the creation of the circles and stars in the second row
        self.play(*[Create(circle) for circle in circles_row2])
        self.wait(1)
        
        star_animations = []
        for stars in stars_sets:
            star_animations.extend([Create(star) for star in stars])
        self.play(*star_animations)
        self.wait(1)
        
        # Add a tick mark to the second circle in the second row
        tick_mark2 = Tex(r"\checkmark").set_color(GREEN).scale(2).next_to(circles_row2[1], UP, buff=0)
        self.play(Write(tick_mark2))
        
        self.wait(3)


    def MoveImage(self):
        # Title
        title = Text("Count the number of images on the left side and write the number of objects \n on the right side").scale(0.6).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        self.construct18()
        self.construct19()
        self.construct20()
        self.construct21()

    def construct18(self):
        t = Text('📱📱📱📱📱📱📱', font_size=30).move_to([-3, 2, 0])
        count = Text('7', font_size=34).move_to([3, 2, 0])
        self.play(FadeIn(t))
        self.play(FadeIn(count))

    def construct19(self):
        t = Text('🦜🦜🦜🦜', font_size=30).move_to([-3, 0.5, 0])
        count = Text('4', font_size=34).move_to([3, 0.5, 0])
        self.play(FadeIn(t))
        self.play(FadeIn(count))

    def construct20(self):
        t = Text('🦋🦋🦋🦋🦋🦋', font_size=30).move_to([-3, -1, 0])
        count = Text('6', font_size=34).move_to([3, -1, 0])
        self.play(FadeIn(t))
        self.play(FadeIn(count))

    def construct21(self):
        t = Text('🐧🐧🐧🐧🐧🐧🐧🐧', font_size=30).move_to([-3, -2.5, 0])
        count = Text('8', font_size=34).move_to([3, -2.5, 0])
        self.play(FadeIn(t))
        self.play(FadeIn(count))

    def SetDeveloperList(self):
        self.DeveloperList = "Bommi Yaswanth"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName = "Grade1chapter4Numbersfrom6to9.py"


if __name__ == "__main__":
    scene = Grade1chapter4Numbersfrom6to9()
    scene.render()