import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class IAMServiceAnimation(AbstractAnim):
    
   # Implement construct method to render
    def construct(self):
        
        # self.displayIAMServiceLevelRelationshipsPart1()
        # self.displayUserPerspectiveRelationsPart2()
        # self.displayUserGroupPerspectiveRelationsPart3()
        self.displayIAMPolicyPerspectiveRelationsPart4()
        
    # render using a json string
    def displayIAMServiceLevelRelationshipsPart1(self):
         
        # IAM Service Concepts
        json_string2 = '''
                    {
                        "IAM Service": {
                            "User": [
                                "John Doe"
                            ],
                            "User Group": [
                                "Marketing Group"
                            ],
                            "IAM Policy": [
                                "Manim Templates Dev Access Policy"
                            ],
                            "Role": [
                                "Admin Role"
                            ]
                            
                                    }
                    }
                    '''     
        try:
            data = json.loads(json_string2)
            for key, value in data.items():
                
                if isinstance(value, str):
                    p10=cvo.CVO().CreateCVO(key,value)
                    self.p10=p10
                else:
                    p10=cvo.CVO().CreateCVO(key,"")
                    self.p10=p10                
                    self.parsejson(value,p10)
                
                break
            
            self.construct1(self.p10,self.p10)
            self.fadeOut()
            
        except json.JSONDecodeError:
            print("Invalid JSON format.")
         
        
        
        # render using a json string
    def displayUserPerspectiveRelationsPart2(self):
         
        # IAM Service Concepts
        json_string2 = '''
                    {
                        "User": {
                            "IAM Policy": [
                                "Project 1 Access Policy"
                            ],
                            "User Group": [
                                "Marketing Group"
                            ]
                                    }
                    }
                    '''     
        try:
            data = json.loads(json_string2)
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
        self.fadeOut()
        
    def displayUserGroupPerspectiveRelationsPart3(self):
         
        # IAM Service Concepts
        json_string2 = '''
                    {
                        "User Group": {
                            "IAM Policy": [
                                "Project 1 Access Policy"
                            ],
                            "User": [
                                "John Doe",
                                "Jane Doe"
                            ]
                                    }
                    }
                    '''     
        try:
            data = json.loads(json_string2)
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
        self.fadeOut()
        
    # render using a json string
    def displayIAMPolicyPerspectiveRelationsPart4(self):
         
        # IAM Service Concepts
        json_string2 = '''
                    {
                        "IAM Policy": {
                            "User": [
                                "John Doe",
                                "Jane Doe"
                            ],
                            "User Group": [
                                "Marketing Group",
                                "Customer Support Group"
                            ]
                            
                                    }
                    }
                    '''     
        try:
            self.positionChoice = [[0,0,0],[-6,-2,0],[6,-2,0],[0,3,0],[-6,2,0],[6,2,0]]
            self.angleChoice = [TAU/4]#,-TAU/4]
            
            data = json.loads(json_string2)
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
        self.fadeOut()
        
   
if __name__ == "__main__":
    
    scene = IAMServiceAnimation()
    scene.render()
    