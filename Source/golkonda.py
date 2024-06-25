# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla
# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla
import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

from manim import *

class golkonda(AbstractAnim):
    def construct(self):
        # self.heading()
        # self.fadeOutCurrentScene()
        self.introduction()
        
        
    def heading(self):
        title = Text("Trip to the Golkonda Fort", font_size=48, color=PINK)
        
        # Animate the title text
        self.play(Write(title))
        self.wait(2)
        
        # Fade out the title text
        self.play(FadeOut(title)) 
        
    def introduction(self):
        p10=cvo.CVO().CreateCVO("estimation of teacher ","").setPosition([-4,0,0])
        p11=cvo.CVO().CreateCVO("","The Golkonda Fort is about 56 km from our school.\nThe bus agency will charge 24 per km").setPosition([0,2,0])
        p12=cvo.CVO().CreateCVO("","The Golkonda Fort is about 56 km from our school. The bus agency will charge ` 24 per km").setPosition([0,1,0]).setangle(-TAU/4)
        p13=cvo.CVO().CreateCVO(""," 20 per person on the snacks and food.").setPosition([0,-3,0]).setangle(-TAU/4)
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
         
        self.construct1(p10,p10)
               
if __name__ == "__main__":
    scene = golkonda()
    scene.render()
