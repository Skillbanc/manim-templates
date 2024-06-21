from manim import *
class np(Scene):
    def construct(self):
        self.add(NumberPlane(axis_config={"include_tip":1}))
        
if __name__=="__main__":
    s=np()
    s.render()