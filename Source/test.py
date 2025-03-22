from AbstractAnim import AbstractAnim
import cvo
from manim import *

class photo(AbstractAnim):

    def construct(self):

        self.emoji_anim()

    def emoji_anim(self):
        # Paths to your emoji SVG files (replace with actual paths)
        emoji1_path = "media\images\man1.svg"
        emoji2_path = "media\images\man1.svg"
        emoji3_path = "media\images\man1.svg"
        emoji4_path = "media\images\man1.svg"
        emoji5_path = "media\images\man1.svg"

        

        radius = 1

        emojis_1 = SVGMobject(emoji1_path).scale(radius)
        emojis_2 = SVGMobject(emoji2_path).scale(radius)
        emojis_3 = SVGMobject(emoji3_path).scale(radius)
        emojis_4 = SVGMobject(emoji4_path).scale(radius)
        emojis_5 = SVGMobject(emoji5_path).scale(radius)

        emojis_1.to_edge(LEFT)
        emojis_2.next_to(emojis_1, RIGHT, buff=1)
        emojis_3.next_to(emojis_2, RIGHT, buff=1)
        emojis_4.next_to(emojis_3, RIGHT, buff=1)
        emojis_5.next_to(emojis_4, RIGHT, buff=1)


        self.play(FadeIn(emojis_1), FadeIn(emojis_2), FadeIn(emojis_3), FadeIn(emojis_4), FadeIn(emojis_5))
        self.wait(2)

        # Add text below each image
        text1 = Text("Image 1").next_to(emojis_1, DOWN)
        text2 = Text("Image 2").next_to(emojis_2, DOWN)
        text3 = Text("Image 3").next_to(emojis_3, DOWN)
        text4 = Text("Image 3").next_to(emojis_4, DOWN)
        text5 = Text("Image 3").next_to(emojis_5, DOWN)  # Add text for additional images

        self.play(Write(text1), Write(text2), Write(text3), Write(text4), Write(text5))
        self.wait(2)
    

if __name__ == "__main__":
    scene = photo()
    scene.render()