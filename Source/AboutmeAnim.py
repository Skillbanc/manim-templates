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

class Rohit(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.constructDataByCVO()
        # self.fadeOut()
        # self.constructDataByJSON()
        # self.fadeOut()
        
    # render using CVO data object
    def constructDataByCVO(self):
        p10=cvo.CVO().CreateCVO("Person","Vailla Rohit")
        p11=cvo.CVO().CreateCVO("College","IFHE")
        p12=cvo.CVO().CreateCVO("Company","Skillbanc.com")
        p13=cvo.CVO().CreateCVO("Project","Manim-Templates")
        p14=cvo.CVO().CreateCVO("Location","Hyderabad")
        p15=cvo.CVO().CreateCVO("Location","USA")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p14)
        p12.cvolist.append(p13)
        p12.cvolist.append(p15)
        
        self.construct1(p10,p10)
    # render using a json string
    def constructDataByJSON(self):
        # The json string containing data, sample 1 string
        json_string1 = '''
                    {
                       "Person": "John Doe"
                    }
                    '''     
        # sample 2 string
        json_string2 = '''
                    {
                        "Task App": {
                            "Task": [
                                "Task 1",
                                "Task 2"
                            ],
                            "Name": "John Doe Task App"
      
                                    }
                    }
                    '''     
        try:
            data = json.loads(json_string1)
            for key, value in data.items():
                
                if isinstance(value, str):
                    p10=cvo.CVO().CreateCVO(key,value)
                    self.p10=p10
                else:
                    p10=cvo.CVO().CreateCVO(key,"")
                    self.p10=p10                
                    self.parsejson(value,p10)
                
                break
            
        except json.JSONDecodeError:
            print("Invalid JSON format.")
         
        self.construct1(self.p10,self.p10)
        
        
      
if __name__ == "__main__":
    scene = Rohit()
    scene.render()
    