from manim import *
from AbstractAnim import AbstractAnim
import cvo


class TableScene(AbstractAnim):
    def construct(self):

        self.PurchaseSkillbancSubscription()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        self.SubscribeYoutube()

    


    def SetDeveloperList(self):  
        self.DeveloperList="Raghu"

        
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="SubtractionofNumbersupto9.py"

    


if __name__ == "__main__":
    scene = TableScene()
    scene.render()
