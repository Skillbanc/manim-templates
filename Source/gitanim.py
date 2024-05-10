# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla
from manim import *
from AbstractAnim import AbstractAnim
import cvo

class git(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.repository()
        self.fadeOut()
        self.repositorycommands()
        # self.fadeOut()
        
    # render using CVO data object
    def repository(self):
        p10=cvo.CVO().CreateCVO("Git","")
        p11=cvo.CVO().CreateCVO("Repository","manim-templates")
        p12=cvo.CVO().CreateCVO("Repository Owner","Skillbanc.com,Inc")
        p13=cvo.CVO().CreateCVO("Branch","")
        p13onnamelist=["main","Vailla Rohit"]
        p13.extendOname(p13onnamelist)
        p11children=[p12,p13]
        p10.cvolist.append(p11)
        p11.extendcvo(p11children)
        
        
        self.construct1(p10,p10)
    
    def repositorycommands(self):
        p10=cvo.CVO().CreateCVO("Git","")
        p11=cvo.CVO().CreateCVO("Command","")
        p11onamelist=["git pull","git push","git commit","git stage","git stash","git init","git branch","git merge","git add"]

        p10.cvolist.append(p11)
        p11.extendOname(p11onamelist)
        
        
        self.construct1(p10,p10)

      
if __name__ == "__main__":
    scene = git()
    scene.render()