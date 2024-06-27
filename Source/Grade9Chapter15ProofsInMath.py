import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class ProofsInMath(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.constructDataByCVO()
        self.fadeOutCurrentScene()
        self.Reasoning()
        self.fadeOutCurrentScene()
        self.Types()
        self.fadeOutCurrentScene()
        self.Proofs()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        self.fadeOutCurrentScene()
        # self.fadeOut()
        # self.constructDataByJSON()
        # self.fadeOut()
        
    # render using CVO data object
    def constructDataByCVO(self):
        p10=cvo.CVO().CreateCVO("Statements","Mathematical Statements").setPosition([0,2,0])
        p11=cvo.CVO().CreateCVO("Hypothesis","Can't be proved by evidence").setPosition([3.5,-2.5,0]).setangle([-TAU/4])
        p12=cvo.CVO().CreateCVO("Example","For every real number x, 3x > x").setPosition([-3.5,-2.5,0]).setangle([-TAU/4])
        p12.SetIsMathText(True)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.isRandom=False
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)
    def Reasoning(self):
        p13=cvo.CVO().CreateCVO("Reasoning","").setPosition([-3.5,2,0])
        p14=cvo.CVO().CreateCVO("Deductive Reasoning\\\\in Hypothesis testing ","").setPosition([-3.5,-2.5,0]).setangle([-TAU/4])
        p15=cvo.CVO().CreateCVO("Deductive Reasoning","").setPosition([3,2,0]).setangle([-TAU/4])
        p16=cvo.CVO().CreateCVO("Definition"," proof is a logical deduction from a set of inputs.").setPosition([3.5,-2.5,0]).setangle([-TAU/4])
        p17=cvo.CVO().CreateCVO("Definition","Results from previous statements using logic").setPosition([0,0,0]).setangle([-TAU/4])
        
        p13.cvolist.append(p14)
        p13.cvolist.append(p15)
        p14.cvolist.append(p16)
        p15.cvolist.append(p17)
        self.isRandom=False
        self.setNumberOfCirclePositions(3)

        self.construct1(p13,p13)
    def Types(self):
        p16=cvo.CVO().CreateCVO("Mathematical Statements","").setPosition([-3.5,-2,0])
        p17=cvo.CVO().CreateCVO("Theorems","Whose truth is established").setPosition([-3.5,2,0]).setangle([-TAU/4])
        p18=cvo.CVO().CreateCVO("Conjectures","Which we believe is true").setPosition([3.5,2,0]).setangle([-TAU/4])
        p19=cvo.CVO().CreateCVO("Inductive reasoning","based on examining various cases").setPosition([3.5,-2,0]).setangle([-TAU/4])
        p20=cvo.CVO().CreateCVO("Axioms","Self evident truths").setPosition([0,0,0]).setangle([-TAU/4])
        
        p16.cvolist.append(p17)
        p16.cvolist.append(p18)
        p18.cvolist.append(p19)
        p16.cvolist.append(p20)
        self.isRandom=False        
        self.setNumberOfCirclePositions(5)
        self.construct1(p16,p16)
    def Proofs(self):
        p13=cvo.CVO().CreateCVO("Mathematical Proofs","").setPosition([-3.5,2,0])
        p15=cvo.CVO().CreateCVO("Definition","process which can establish truth based on logic").setPosition([3.5,2,0]).setangle([-TAU/4])
        p14=cvo.CVO().CreateCVO("To make false ","").setPosition([-3.5,-2,0]).setangle([-TAU/4])
        p16=cvo.CVO().CreateCVO("Condition","Produce single counter example").setPosition([3.5,-2,0]).setangle([-TAU/4])
        p13.cvolist.append(p15)
        p13.cvolist.append(p14)
        p14.cvolist.append(p16)
        self.isRandom=False
        self.setNumberOfCirclePositions(4)

        self.construct1(p13,p13)
    def SetDeveloperList(self): 
       self.DeveloperList="Preetham" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade9Chapter15ProofsInMath.py"
      

if __name__ == "__main__":
    scene = ProofsInMath()
    scene.render()