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

        bucket = SVGMobject(emoji1_path).scale(2).move_to(LEFT)
        glass = SVGMobject(emoji2_path).scale(2).next_to(bucket,RIGHT)
        text = Text("Bucket holds more Water than a Glass").next_to(bucket,DOWN).scale(1)
    
        self.play(Create(bucket))
        self.wait(1)
        self.play(Create(glass))
        self.wait(1.5)
        self.play(Write(text))
        self.wait(0.5)
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

        text1 = Text("rankings the vessels according to the" ).move_to([0,2.5,0]).scale(1)
        text6 = Text(" quantity of water each can hold").next_to(text1,DOWN).scale(1)

        text2 = Text("Bucket: 1").scale(0.5).next_to(bucket,DOWN)
        text3 = Text("pot: 2").scale(0.5).next_to(pot,DOWN)
        text4 = Text("jug: 3").scale(0.5).next_to(jug,DOWN)
        text5 = Text("glass: 4").scale(0.5).next_to(glass,DOWN)

        self.play(Write(text1),Write(text6))
        self.play(Create(bucket))
        self.play(Create(pot))
        self.play(Create(jug))
        self.play(Create(glass))
        self.wait(2)
        self.play(Write(text2),Write(text3),Write(text4),Write(text5))
        self.fadeOutCurrentScene()

    def SetDeveloperList(self):
        self.DeveloperList="Bhaskar"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade2Chapter15Volumes.py"

        

if __name__ == "__main__":
    scene = Volume()
    scene.render()
    

        
