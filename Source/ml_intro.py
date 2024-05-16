# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla
from manim import *
from AbstractAnim import AbstractAnim
import cvo

class mlintro(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.mlintro()
        
    # render using CVO data object
    def mlintro(self):
        p10=cvo.CVO().CreateCVO("Machine Learning","")
        p11=cvo.CVO().CreateCVO("Types of ML","")
        p11onnamelist=["Supervised","Unsupervised","Semi-supervised","Reinforced"]
        p11.extendOname(p11onnamelist)
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.setNumberOfClasses(2)
        self.angleChoice = [TAU/4]
        self.colorChoice=[ORANGE,YELLOW]
        self.isRandom = False
        self.construct1(p10,p10)


      
if __name__ == "__main__":
    scene = mlintro()
    scene.render()