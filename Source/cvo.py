# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla

from cloup import Color


class CVO:
  
  def setPosition(self,pos):
    self.pos = pos
    return self
  
  def CreateCVO(self,cname,oname):
    
    self.oname = oname
    self.cname = cname
    self.circle_radius=1
    self.circle_color = Color.blue
    self.cvolist = []
    self.pos = [0,0,0]
    return self

  