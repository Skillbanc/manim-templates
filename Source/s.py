from manim import *
from AbstractAnim import AbstractAnim
import cvo

class my(AbstractAnim):

    def construct(self):
        self.GithubSourceCodeReference()

if __name__ == "__main__":
    scene = my()
    scene.render()