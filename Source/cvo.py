from cloup import Color


class CVO:
  
  def CreateCVO(self, o1name,o2name,c1name,c2name):
    self.o1name = o1name
    self.o2name = o2name
    self.c1name = c1name
    self.c2name = c2name
    self.circle_radius=1
    self.circle_color = Color.blue
    
    return self

  def setc1o1Name(self,c1name,o1name):
    self.setc1name(c1name)
    self.seto1Name(o1name)
    return self
    
  def setc2o2Name(self,c2name,o2name):
    self.setc2name(c2name)
    self.seto2Name(o2name)
    
  def setc1Name(self,c1name):
    self.c1name = c1name
    return self
    
  def setc2Name(self,c2name):
    self.c2name = c2name
    return self
    
  def seto1Name(self,o1name):
    self.o1name = o1name
    return self
  
  def seto2Name(self,o2name):
    self.o2name = o2name
    return self
  