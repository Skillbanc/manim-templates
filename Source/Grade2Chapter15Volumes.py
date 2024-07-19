from manim import*
from AbstractAnim import AbstractAnim

class Volume(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.heading()
        self.ranking()
        self.GithubSourceCodeReference()


    def heading(self):
        self.isRandom=False

        text = Text("Measure of Liquids")
        self.play(Write(text))
        self.wait(2)
        self.fadeOutCurrentScene()

        emoji1_path = "media/images/bucket.svg"
        emoji2_path = "media/images/glass.svg"

        bucket = SVGMobject(emoji1_path).scale(1).move_to([-2,0,0])
        glass = SVGMobject(emoji2_path).scale(1).move_to([2,0,0])
        text = Text("Which of the following holds more Water ?").scale(1).move_to([0,3,0])
        text1 = Text("Bucket holds more water than Glass").move_to([0,-3,0])
        text2 = Text("Bucket").scale(0.5).next_to(bucket,DOWN)
        text3 = Text("Glass").scale(0.5).next_to(glass,DOWN)

        self.play(Write(text))
        self.wait(0.5)
        self.play(Create(bucket),Write(text2))
        self.wait(1)
        self.play(Create(glass),Write(text3))
        self.wait(1.5)
        self.play(Write(text1))
        self.fadeOutCurrentScene()

    def ranking(self):
        self.isRandom=False

        emoji1_path = "media/images/bucket.svg"
        emoji2_path = "media/images/glass.svg"
        emoji3_path = "media/images/jug.svg"
        emoji4_path = "media/images/pottt.svg"

        bucket = SVGMobject(emoji1_path).scale(1).move_to([-4,0,0])
        glass = SVGMobject(emoji2_path).scale(1).move_to([-1,0,0])
        jug = SVGMobject(emoji3_path).scale(1).move_to([1.5,0,0])
        pot = SVGMobject(emoji4_path).scale(1).move_to([4,0,0])

        text1 = Text("Rank the vessels according to the" ).move_to([0,3,0]).scale(1)
        text6 = Text(" quantity of water each can hold").next_to(text1,DOWN).scale(1)

        text2 = Text("Bucket").scale(0.5).next_to(bucket,DOWN)
        text3 = Text("pot").scale(0.5).next_to(pot,DOWN)
        text4 = Text("jug").scale(0.5).next_to(jug,DOWN)
        text5 = Text("glass").scale(0.5).next_to(glass,DOWN)

        text7 = Text("Rank-1").next_to(text2,DOWN).scale(0.7)
        text8 = Text("Rank-2").next_to(text3,DOWN).scale(0.7)
        text9 = Text("Rank-3").next_to(text4,DOWN).scale(0.7)
        text10 = Text("Rank-4").next_to(text5,DOWN).scale(0.7)

        self.play(Write(text1),Write(text6))
        self.play(Create(bucket),Write(text2))
        self.play(Create(pot),Write(text3))
        self.play(Create(jug),Write(text4))
        self.play(Create(glass),Write(text5))
        self.wait(2)
        self.play(Write(text7),Wait(0.5))
        self.play(Write(text8),Wait(0.5))
        self.play(Write(text9),Wait(0.5))
        self.play(Write(text10),Wait(0.5))
        self.fadeOutCurrentScene()

    def SetDeveloperList(self):
        self.DeveloperList="Bhaskar"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade2Chapter15Volumes.py"

        

if __name__ == "__main__":
    scene = Volume()
    scene.render()
    

        
