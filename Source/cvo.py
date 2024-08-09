# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla

from manim import*


class CVO:
  
  def setPosition(self,pos):
    self.pos = pos
    return self
  
  def setangle(self,angle):
    self.angle = angle
    return self
  
  def setc1nameposition(self,c1nameposition):
    self.c1nameposition = c1nameposition
    return self
  
  def seto1nameposition(self,o1nameposition):
    self.o1nameposition = o1nameposition
    return self
  
  def setduration(self,duration):
    self.duration = duration
    return self
  
  def appendOname(self,oname):
    self.onameList.append(oname)
    return self
  
  def extendOname(self,oname):
    self.onameList.extend(oname)
    return self
  
  def extendcvo(self,cvoobj):
    self.cvolist.extend(cvoobj)

  def setcircleradius(self,radius):
    self.circle_radius=radius
  
  def SetIsMathText(self,b):
    self.IsMathText = b
    return self
    
  def CreateCVO(self,cname,oname):
    self.c1nameposition = None
    self.o1nameposition = None
    self.oname = oname
    self.cname = cname
    self.circle_radius=1
    self.circle_color = BLUE
    self.cvolist = []
    self.pos = None#[0,0,0]
    self.angle = TAU/4
    self.duration = 1
    self.cnameMObject = None
    self.onameMObject = None
    self.onameList = []
    self.SetIsMathText(False)
    self.speech=""
    self.IsSquare = False
    return self
  

  