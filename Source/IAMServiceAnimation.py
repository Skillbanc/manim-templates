import json

from manim import *
import random

from AbstractAnim import AbstractAnim

import cvo

class IAMServiceAnimation(AbstractAnim):
    
   # Implement construct method to render
    def construct(self):
        self.isRandom = False
        
        self.RenderLOGO().fadeOut()
        # self.RenderMovieTitles().fadeOut()
        # self.RenderAboutMe().fadeOut()
        # self.displayIAMServiceLevelRelationshipsPart1()
        # self.displayUserPerspectiveRelationsPart2()
        # self.displayUserGroupPerspectiveRelationsPart3()
        #self.displayIAMPolicyPerspectiveRelationsPart4()
        
    
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
            self.positionChoice = [[-6,-2,0],[6,-2,0],[0,3,0],[-6,2,0],[6,2,0]]
            self.angleChoice = [TAU/4,TAU/4,TAU/4,TAU/4]#,-TAU/4]
            
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
        
    def RenderLOGO(self):
        # Define colors for dots and circles
        dot_colors = [ORANGE, BLUE, GREEN]
        circle_colors = [ORANGE, DARK_BLUE, GREEN]

        # Create multiple dots appearing randomly from the edges
        num_dots = 100
        dots = VGroup(*[Dot(color=random.choice(dot_colors)) for _ in range(num_dots)])
        self.play(Create(dots))

        # Define animations for random movement of dots
        animations = []
        for _ in range(180):  # 180 frames at 30 fps = 6 seconds
            for dot in dots:
                start_point = random.choice([
                    LEFT * 7 + random.uniform(-3, 3) * UP,
                    RIGHT * 7 + random.uniform(-3, 3) * DOWN,
                    UP * 4 + random.uniform(-5, 5) * RIGHT,
                    DOWN * 4 + random.uniform(-5, 5) * LEFT
                ])
                end_point = random.uniform(-3, 3) * RIGHT + random.uniform(-3, 3) * UP
                animations.append(dot.animate.shift(start_point - dot.get_center()))
                animations.append(dot.animate.shift(end_point - start_point))

        # Play animations for 6 seconds
        self.play(AnimationGroup(*animations))

        # Create circles with different colors
        circles = VGroup(*[Circle(radius=0.5, color=color, fill_color=color, fill_opacity=1) for color in circle_colors])
        circles.arrange(RIGHT, buff=1)
        self.play(Transform(dots, circles))
        # self.play(Transform(circles, dots ))
        # self.play(Transform(dots, circles))
        
        # Define arrow animations with start and end points on the surface of circles
        arrows = VGroup(
            Arrow(circles[0].get_right(), circles[1].get_left(), buff=0.1),
            Arrow(circles[1].get_right(), circles[2].get_left(), buff=0.1),
            CurvedArrow(circles[0].get_top(), circles[2].get_top(), angle=-TAU/4),
            CurvedArrow(circles[0].get_bottom(), circles[2].get_bottom(), angle=TAU/4)
        )

        # Play arrow animations sequentially
        self.play(Create(arrows[0]))
        self.play(Create(arrows[1]))
        self.play(Create(arrows[2]))
        self.play(Create(arrows[3]))
        self.wait(2)
        return self
    
     # render using CVO data object
    def RenderMovieTitles(self):
        self.positionChoice = [[-6,-2,0],[6,-2,0],[0,3,0],[-6,2,0],[6,2,0],[0,-3,0]]
        self.angleChoice = [TAU/4,-TAU/4,TAU/4,-TAU/4,TAU/4,-TAU/4]
        count = 0
        p10=cvo.CVO().CreateCVO("Today's Topic","Git Version Control")
        count += 1
        
        p11=cvo.CVO().CreateCVO("Directed By","Sudhakar Moparthy")
        count += 1
        p10.cvolist.append(p11)
        
        p12=cvo.CVO().CreateCVO("Produced By","Skillbanc.com, Inc.")
        count += 1
        p10.cvolist.append(p12)
        
        p13=cvo.CVO().CreateCVO("Animated By","Rohit Vailla")
        count += 1
        p10.cvolist.append(p13)
        
        p14=cvo.CVO().CreateCVO("Distributed By","Skillbanc YouTube Channel")
        count += 1
        p10.cvolist.append(p14)
        
        p15=cvo.CVO().CreateCVO("Sponsered By", "Skillbanc.com, Inc.")
        count += 1
        p10.cvolist.append(p15)
        

        self.construct1(p10,p10)
        return self
     # render using CVO data object
    def RenderAboutMe(self):
        
        self.angleChoice = [TAU/4,-TAU/4,TAU/4,-TAU/4,TAU/4,-TAU/4]
        
        count = 0
        # starting object
        p10=cvo.CVO().CreateCVO("My Name","Vailla Rohit")
        count += 1
        
        # Level 1 First c2 object
        p11=cvo.CVO().CreateCVO("College","IFHE")
        count += 1
        # Level 2 
        p14=cvo.CVO().CreateCVO("Location","Hyderabad")
        count += 1
        p11.cvolist.append(p14)
        
        p10.cvolist.append(p11)
            
        # 2nd c2 object
        p12=cvo.CVO().CreateCVO("Company","Skillbanc.com.Inc, USA")
        count += 1
        # Level 2
        p13=cvo.CVO().CreateCVO("Project","Manim-Templates")
        count += 1
        p12.cvolist.append(p13)
        
        p10.cvolist.append(p12)
        
        self.setNumberOfClasses(count)
       
       
        self.construct1(p10,p10)
        return self
    
if __name__ == "__main__":
    
    scene = IAMServiceAnimation()
    scene.render()
    