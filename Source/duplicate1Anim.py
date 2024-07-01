from manim import *
from AbstractAnim import AbstractAnim

import cvo


class duplicate1(AbstractAnim):

     def construct(self):
        # p1=cvo.CVO().CreateCVO("cname","oname")
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.Addition()
        self.fadeOutCurrentScene() 


     def Addition(self):
        # Create CVO object with mathematical text
        p10 = cvo.CVO().CreateCVO("Sub Topics of  Basic Geometrical Ideas", "").SetIsMathText(True)
        # Append onameList with properly formatted LaTeX strings
        p10.onameList.append("Sub Topics of  Basic Geometrical Ideas")
        p10.onameList.append(r"chapter-4.1: Introduction")
        p10.onameList.append(r"chapter-4.2: Point")
        p10.onameList.append(r"chapter-4.3: Line Segment")
        p10.onameList.append(r"chapter-4.4: Line")
        p10.onameList.append(r"chapter-4.5: Ray")
        p10.onameList.append(r"chapter-4.6: Curve")
        p10.onameList.append(r"chapter-4.7: Angle")
        p10.onameList.append(r"chapter-4.8: Triangle")
        p10.onameList.append(r"chapter-4.9: Quadrilateral")
        p10.onameList.append(r"chapter-4.10: Circle")
        
        # Render the CVO object
        self.construct2(p10, p10)


if __name__ == "__main__":
    scene = duplicate1()
    scene.render()