from manim import *

from AbstractAnim import AbstractAnim

class EllipseWithStars(VGroup):
    def __init__(self, num_circles, **kwargs):
        super().__init__(**kwargs)
        self.add(*self.circles)

        

class Skillbanclogo(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        
    
        
if __name__=="__main__":
    s=Skillbanclogo()
    s.render()

