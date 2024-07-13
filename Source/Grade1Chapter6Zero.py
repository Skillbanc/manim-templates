
import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo

class ZeroAnim(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.Zero()
        self.fadeOutCurrentScene()
        self.emoji_anim()
        self.fadeOutCurrentScene()
        self.emoji_anim2()
        self.fadeOutCurrentScene()
        self.emoji_anim3()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        
    def SetDeveloperList(self):  
        self.DeveloperList = "Mukthanand Reddy"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName = "Grade1Chapter6Zero.py"
            

    def emoji_anim(self):
        # Paths to your emoji SVG files (adjust paths as needed)
        emoji1_path = "media/images/emoji1.svg"
        emoji2_path = "media/images/emoji1.svg"
        emoji3_path = "media/images/emoji1.svg"

        Example_heading = MathTex("Example 1: ", font_size=50).to_edge(UP*1 + LEFT)
        self.play(Write(Example_heading))

        # Radius for scaling the emojis
        radius = 0.5
        
        # Create 3 emojis with the same radius
        emojis_3 = [SVGMobject(emoji1_path).scale(radius) for _ in range(3)]
        
        # Position emojis_3 in a horizontal line shifted to the left and up
        for i, emoji in enumerate(emojis_3):
            emoji.move_to(2 * RIGHT + i * 1.5 * LEFT).shift(LEFT * 3 + UP * 2)
        
        # Show emojis_3
        self.play(*[Create(emoji) for emoji in emojis_3])
        
        # Create arrow and text "3"
        arrow_start_3 = emojis_3[0].get_left() + 1.5 * RIGHT
        arrow_end_3 = emojis_3[0].get_center() + 5 * RIGHT
        arrow_3 = Arrow(start=arrow_start_3, end=arrow_end_3, buff=0, color=YELLOW)
        text_3 = Text("3 Dogs", font_size=48, color=WHITE).next_to(arrow_3, RIGHT, buff=0.1)
        
        # Show arrow and text "3"
        self.play(Create(arrow_3), Write(text_3))
        
        self.wait(1.5)
        
        # Create 2 emojis with the same radius below the 3 emojis
        emojis_2 = [SVGMobject(emoji2_path).scale(radius) for _ in range(2)]
        
        # Position emojis_2 in a horizontal line below the 3 emojis
        for i, emoji in enumerate(emojis_2):
            emoji.move_to(2 * RIGHT + i * 1.5 * LEFT).shift(LEFT * 3 + UP * 0.2)
        
        # Show emojis_2
        self.play(*[Create(emoji) for emoji in emojis_2])
        
        # Create arrow and text "2"
        arrow_start_2 = emojis_2[0].get_left() + 1.5 * RIGHT
        arrow_end_2 = emojis_2[0].get_center() + 5 * RIGHT
        arrow_2 = Arrow(start=arrow_start_2, end=arrow_end_2, buff=0, color=YELLOW)
        text_2 = Text("2 Dogs", font_size=48, color=WHITE).next_to(arrow_2, RIGHT, buff=0.1)
        
        # Show arrow and text "2"
        self.play(Create(arrow_2), Write(text_2))
        
        self.wait(1.5)
        
        # Create 1 emoji with the same radius below the 2 emojis
        emoji_1 = SVGMobject(emoji3_path).scale(radius)
        
        # Position emoji_1 below the 2 emojis
        emoji_1.move_to(2 * RIGHT + LEFT * 1.5).shift(LEFT * 1.3 + DOWN * 1.5)
        
        # Show emoji_1
        self.play(Create(emoji_1))
        
        # Create arrow and text "1"
        arrow_start_1 = emoji_1.get_left() + 1.5 * RIGHT
        arrow_end_1 = emoji_1.get_center() + 5 * RIGHT
        arrow_1 = Arrow(start=arrow_start_1, end=arrow_end_1, buff=0, color=YELLOW)
        text_1 = Text("1 Dog", font_size=48, color=WHITE).next_to(arrow_1, RIGHT, buff=0.1)
        
        # Show arrow and text "1"
        self.play(Create(arrow_1), Write(text_1))
        
        self.wait(1.5)
        
        # Create horizontal line below the last emoji
        #line_last = Line(start=LEFT * 5 + DOWN * 3.1, end=LEFT * 0.1 + DOWN * 3.1, stroke_width=8, color=WHITE).shift(UP*0.38)
        
        # Show the horizontal line
        #self.play(Create(line_last))
        
        # Create arrow and text "0"
        arrow_last_start = LEFT * 0.1 + DOWN * 3.2
        arrow_last_end = RIGHT * 4 + DOWN * 3.2
        arrow_last = Arrow(start=arrow_last_start, end=arrow_last_end, buff=0, color=YELLOW).shift(UP*0.4)
        text_last = Text("0 Dogs ", font_size=48, color=WHITE).next_to(arrow_last, RIGHT, buff=0.1).shift(UP*0)
        
        # Show arrow and text "0"
        self.play(Create(arrow_last))
        self.play(Write(text_last))

        # Zoom in and then zoom out the text "0"
        self.play(text_last.animate.scale(2))  # Zoom in
        self.wait(1)
        self.play(text_last.animate.scale(0.5))  # Zoom out

        self.wait(2)

    def emoji_anim2(self):
        # Paths to your emoji SVG files (adjust paths as needed)
        emoji1_path = "media/images/emoji2.svg"
        emoji2_path = "media/images/emoji2.svg"
        emoji3_path = "media/images/emoji2.svg"

        Example_heading = MathTex("Example 2: ", font_size=50).to_edge(UP*1 + LEFT)
        self.play(Write(Example_heading))

        # Radius for scaling the emojis
        radius = 0.5
        
        # Create 3 emojis with the same radius
        emojis_3 = [SVGMobject(emoji1_path).scale(radius) for _ in range(3)]
        
        # Position emojis_3 in a horizontal line shifted to the left and up
        for i, emoji in enumerate(emojis_3):
            emoji.move_to(2 * RIGHT + i * 1.5 * LEFT).shift(LEFT * 3 + UP * 2)
        
        # Show emojis_3
        self.play(*[Create(emoji) for emoji in emojis_3])
        
        # Create arrow and text "3"
        arrow_start_3 = emojis_3[0].get_left() + 1.5 * RIGHT
        arrow_end_3 = emojis_3[0].get_center() + 5 * RIGHT
        arrow_3 = Arrow(start=arrow_start_3, end=arrow_end_3, buff=0, color=YELLOW)
        text_3 = Text("3 Chicks", font_size=48, color=WHITE).next_to(arrow_3, RIGHT, buff=0.1)
        
        # Show arrow and text "3"
        self.play(Create(arrow_3), Write(text_3))
        
        self.wait(1)
        
        # Create 2 emojis with the same radius below the 3 emojis
        emojis_2 = [SVGMobject(emoji2_path).scale(radius) for _ in range(2)]
        
        # Position emojis_2 in a horizontal line below the 3 emojis
        for i, emoji in enumerate(emojis_2):
            emoji.move_to(2 * RIGHT + i * 1.5 * LEFT).shift(LEFT * 3 + UP * 0.2)
        
        # Show emojis_2
        self.play(*[Create(emoji) for emoji in emojis_2])
        
        # Create arrow and text "2"
        arrow_start_2 = emojis_2[0].get_left() + 1.5 * RIGHT
        arrow_end_2 = emojis_2[0].get_center() + 5 * RIGHT
        arrow_2 = Arrow(start=arrow_start_2, end=arrow_end_2, buff=0, color=YELLOW)
        text_2 = Text("2 Chicks", font_size=48, color=WHITE).next_to(arrow_2, RIGHT, buff=0.1)
        
        # Show arrow and text "2"
        self.play(Create(arrow_2), Write(text_2))
        
        self.wait(1)
        
        # Create 1 emoji with the same radius below the 2 emojis
        emoji_1 = SVGMobject(emoji3_path).scale(radius)
        
        # Position emoji_1 below the 2 emojis
        emoji_1.move_to(2 * RIGHT + LEFT * 1.5).shift(LEFT * 1.3 + DOWN * 1.5)
        
        # Show emoji_1
        self.play(Create(emoji_1))
        
        # Create arrow and text "1"
        arrow_start_1 = emoji_1.get_left() + 1.5 * RIGHT
        arrow_end_1 = emoji_1.get_center() + 5 * RIGHT
        arrow_1 = Arrow(start=arrow_start_1, end=arrow_end_1, buff=0, color=YELLOW)
        text_1 = Text("1 Chick", font_size=48, color=WHITE).next_to(arrow_1, RIGHT, buff=0.1)
        
        # Show arrow and text "1"
        self.play(Create(arrow_1), Write(text_1))
        
        self.wait(1)
        
        # Create horizontal line below the last emoji
        #line_last = Line(start=LEFT * 5 + DOWN * 3.1, end=LEFT * 0.1 + DOWN * 3.1, stroke_width=8, color=WHITE).shift(UP*0.38)
        
        # Show the horizontal line
        #self.play(Create(line_last))
        
        # Create arrow and text "0"
        arrow_last_start = LEFT * 0.1 + DOWN * 3.2
        arrow_last_end = RIGHT * 4 + DOWN * 3.2
        arrow_last = Arrow(start=arrow_last_start, end=arrow_last_end, buff=0, color=YELLOW).shift(UP*0.4)
        text_last = Text("0 Chicks", font_size=48, color=WHITE).next_to(arrow_last, RIGHT, buff=0.1).shift(UP*0)
        
        # Show arrow and text "0"
        self.play(Create(arrow_last))
        self.play(Write(text_last))

        # Zoom in and then zoom out the text "0"
        self.play(text_last.animate.scale(2))  # Zoom in
        self.wait(1)
        self.play(text_last.animate.scale(0.5))  # Zoom out

        self.wait(2)

    def emoji_anim3(self):
        # Paths to your emoji SVG files (adjust paths as needed)
        emoji1_path = "media/images/emoji3.svg"
        emoji2_path = "media/images/emoji3.svg"
        emoji3_path = "media/images/emoji3.svg"

        Example_heading = MathTex("Example 3: ", font_size=50).to_edge(UP*1 + LEFT)
        self.play(Write(Example_heading))

        # Radius for scaling the emojis
        radius = 0.5
        
        # Create 3 emojis with the same radius
        emojis_3 = [SVGMobject(emoji1_path).scale(radius) for _ in range(3)]
        
        # Position emojis_3 in a horizontal line shifted to the left and up
        for i, emoji in enumerate(emojis_3):
            emoji.move_to(2 * RIGHT + i * 1.5 * LEFT).shift(LEFT * 3 + UP * 2)
        
        # Show emojis_3
        self.play(*[Create(emoji) for emoji in emojis_3])
        
        # Create arrow and text "3"
        arrow_start_3 = emojis_3[0].get_left() + 1.5 * RIGHT
        arrow_end_3 = emojis_3[0].get_center() + 5 * RIGHT
        arrow_3 = Arrow(start=arrow_start_3, end=arrow_end_3, buff=0, color=YELLOW)
        text_3 = Text("3 Balloons.", font_size=43, color=WHITE).next_to(arrow_3, RIGHT, buff=0.1)
        
        # Show arrow and text "3"
        self.play(Create(arrow_3), Write(text_3))
        
        self.wait(1)
        
        # Create 2 emojis with the same radius below the 3 emojis
        emojis_2 = [SVGMobject(emoji2_path).scale(radius) for _ in range(2)]
        
        # Position emojis_2 in a horizontal line below the 3 emojis
        for i, emoji in enumerate(emojis_2):
            emoji.move_to(2 * RIGHT + i * 1.5 * LEFT).shift(LEFT * 3 + UP * 0.2)
        
        # Show emojis_2
        self.play(*[Create(emoji) for emoji in emojis_2])
        
        # Create arrow and text "2"
        arrow_start_2 = emojis_2[0].get_left() + 1.5 * RIGHT
        arrow_end_2 = emojis_2[0].get_center() + 5 * RIGHT
        arrow_2 = Arrow(start=arrow_start_2, end=arrow_end_2, buff=0, color=YELLOW)
        text_2 = Text("2 Balloons.", font_size=43, color=WHITE).next_to(arrow_2, RIGHT, buff=0.1)
        
        # Show arrow and text "2"
        self.play(Create(arrow_2), Write(text_2))
        
        self.wait(1)
        
        # Create 1 emoji with the same radius below the 2 emojis
        emoji_1 = SVGMobject(emoji3_path).scale(radius)
        
        # Position emoji_1 below the 2 emojis
        emoji_1.move_to(2 * RIGHT + LEFT * 1.5).shift(LEFT * 1.3 + DOWN * 1.5)
        
        # Show emoji_1
        self.play(Create(emoji_1))
        
        # Create arrow and text "1"
        arrow_start_1 = emoji_1.get_left() + 1.5 * RIGHT
        arrow_end_1 = emoji_1.get_center() + 5 * RIGHT
        arrow_1 = Arrow(start=arrow_start_1, end=arrow_end_1, buff=0, color=YELLOW)
        text_1 = Text("1 Balloon.", font_size=43, color=WHITE).next_to(arrow_1, RIGHT, buff=0.1)
        
        # Show arrow and text "1"
        self.play(Create(arrow_1), Write(text_1))
        
        self.wait(1)
        
        # Create horizontal line below the last emoji
        #line_last = Line(start=LEFT * 5 + DOWN * 3.1, end=LEFT * 0.1 + DOWN * 3.1, stroke_width=8, color=WHITE).shift(UP*0.38)
        
        # Show the horizontal line
        #self.play(Create(line_last))
        
        # Create arrow and text "0"
        arrow_last_start = LEFT * 0.1 + DOWN * 3.2
        arrow_last_end = RIGHT * 4 + DOWN * 3.2
        arrow_last = Arrow(start=arrow_last_start, end=arrow_last_end, buff=0, color=YELLOW).shift(UP*0.4)
        text_last = Text("0  Balloons", font_size=43, color=WHITE).next_to(arrow_last, RIGHT, buff=0.1).shift(UP*0)
        
        # Show arrow and text "0"
        self.play(Create(arrow_last))
        self.play(Write(text_last))

        # Zoom in and then zoom out the text "0"
        self.play(text_last.animate.scale(2))  # Zoom in
        self.wait(1)
        self.play(text_last.animate.scale(0.5))  # Zoom out

        self.wait(2)

    def Zero(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Zero","$0$").setPosition([-4,0,0]).setangle(-TAU/4)
        p11=cvo.CVO().CreateCVO("Definition" ,"The absence of quantity" ).setPosition([4,0,0]).setangle(-TAU/4)
        p11.setcircleradius(2)
        p10.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    
if __name__ == "__main__":
    scene = ZeroAnim()
    scene.render()
