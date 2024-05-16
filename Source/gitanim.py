# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla
from manim import *
from AbstractAnim import AbstractAnim
import cvo

class GitAnim(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        # self.RenderRepository()
        # self.fadeOut()
        self.RenderGitCommands()
        self.fadeOutCurrentScene()
        
    # render using CVO data object
    def RenderRepository(self):
        self.setNumberOfCirclePositions(5)
        p10=cvo.CVO().CreateCVO("Git","")
        
        p11=cvo.CVO().CreateCVO("Repository","manim-templates")
        
        p12=cvo.CVO().CreateCVO("Repository Owner","Skillbanc.com,Inc")
        
        p13=cvo.CVO().CreateCVO("Branch","main")
        p13onnamelist=["Vailla Rohit"]
        p13.extendOname(p13onnamelist)
        
        p11children=[p12,p13]
        p11.extendcvo(p11children)
        
        p10Children = [p11]
        p10.extendcvo(p10Children)
        
        self.construct1(p10,p10)
    
    def RenderGitCommands(self):
        self.setNumberOfCirclePositions(2)
        self.setNumberOfAngleChoices(9)
        p10=cvo.CVO().CreateCVO("Git","")
        p11=cvo.CVO().CreateCVO("Command","")
        p11onamelist=["git pull","git push","git commit","git stage","git stash","git init","git branch","git merge","git add"]

        p10.cvolist.append(p11)
        p11.extendOname(p11onamelist)
        
        
        self.construct1(p10,p10)

      
if __name__ == "__main__":
    scene = GitAnim()
    scene.render()