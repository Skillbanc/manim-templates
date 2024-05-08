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
        p13=cvo.CVO().CreateCVO("Branch","main")
        p14=cvo.CVO().CreateCVO("Branch","Vailla Rohit")
        
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
        p11.cvolist.append(p14)
        
        self.construct1(p10,p10)
    
    def repositorycommands(self):
        p10=cvo.CVO().CreateCVO("Git","")
        p11=cvo.CVO().CreateCVO("Command","git init")
        p12=cvo.CVO().CreateCVO("Command","git add")
        p13=cvo.CVO().CreateCVO("Command","git push")
        p14=cvo.CVO().CreateCVO("Command","git pull")
        p15=cvo.CVO().CreateCVO("Command","git commit")
        p16=cvo.CVO().CreateCVO("Command","git stash")
        p17=cvo.CVO().CreateCVO("Command","git clone")

        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        p10.cvolist.append(p16)
        p10.cvolist.append(p17)
        
        self.construct1(p10,p10)

      
if __name__ == "__main__":
    scene = git()
    scene.render()