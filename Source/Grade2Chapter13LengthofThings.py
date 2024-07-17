from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo

class Grade2Chapter13LengthofThings(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        
        self.topic1()
        self.fadeOutCurrentScene()
        self.topic2()
        self.fadeOutCurrentScene()
        self.topic3()
        self.fadeOutCurrentScene()
        self.topic4()
        self.fadeOutCurrentScene()
        self.topic5()
        self.fadeOutCurrentScene()
        self.topic6()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        
        
    
    def topic1(self):
        self.isRandom = False
        self.angleChoice = [TAU/4]
        p10=cvo.CVO().CreateCVO("Length","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Definition", "how long something is").setPosition([4,2,0])
        

        p10.cvolist.append(p11)
        

        self.construct1(p10,p10)

    def topic2(self):
        self.isRandom = False
        self.angleChoice = [TAU/4,-TAU/2,-TAU/4,-TAU/2]
        p10=cvo.CVO().CreateCVO("Measuring tools","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Standard measuring tools", "official tools we use to measure").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("Non-standard measuring tools", "everyday things we use to measure").setPosition([-4,2,0])
        p13=cvo.CVO().CreateCVO("Examples", "rulers ,tapes,meter sticks").setPosition([5,-2,0])
        p14=cvo.CVO().CreateCVO("Examples", "body parts").setPosition([-4,0,0])

        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p11.cvolist.append(p13)
        p12.cvolist.append(p14)
        self.construct1(p10,p10)
    
    def topic3(self):
        self.isRandom = False
        self.angleChoice = [TAU/4,-TAU/4,-TAU/4]
        p10=cvo.CVO().CreateCVO("Standard measuring tools","").setPosition([0,2.5,0])
        
        p12=cvo.CVO().CreateCVO("Ruler", " helps measure lengths").setPosition([5,-2,0])
        p13=cvo.CVO().CreateCVO("Tapes", "measure distances ").setPosition([-4,1,0])
       

        
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        
        self.construct1(p10,p10)
        


   
    def topic4(self):
    # Title
        #title_emoji = Text("👨‍🔬").scale(2.5)
        title_text = Text("Standard Measuring Tools", font_size=48, color=BLUE)
        title = VGroup( title_text).arrange(RIGHT, buff=0.5).to_edge(UP)
        self.play(FadeIn(title))

        tools = [
            ("📏", "Ruler", "Measures length in cm and inches", BLUE),
            ("🧵", "Measuring Tape", "Flexible for curved surfaces", GREEN),
           
            
        ]

        for emoji, name, description, color in tools:
            # Create tool representation
            tool_emoji = Text(emoji).scale(3.5)
            tool_name = Text(name, font_size=36, color=color)
            tool_group = VGroup(tool_emoji, tool_name).arrange(DOWN, buff=0.4)
            tool_group.to_edge(LEFT, buff=1.5)

            # Show tool
            self.play(FadeIn(tool_group))

            # Create description text
            desc_text = Text(description, font_size=28, color=WHITE)
            desc_text.next_to(tool_group, RIGHT, buff=1.2)

            # Show description
            self.play(Write(desc_text))

            

            self.wait(2)

            # Clear for next tool
            self.play(FadeOut(tool_group), FadeOut(desc_text))
            


        self.wait(2)

    
    def topic5(self):
        self.isRandom = False
        self.angleChoice = [TAU/4,-TAU/4,-TAU/4,-TAU/4,-TAU/4]
        p10=cvo.CVO().CreateCVO("Non-standard measuring tools","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("using body parts", "").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("Hand-breadth", "equal to width of 4 fingers").setPosition([5,-2,0])
        p13=cvo.CVO().CreateCVO("Hand-span", "btw the little finger and thumb of hand").setPosition([-4,2,0])
        p14=cvo.CVO().CreateCVO("Cubit", "btw the elbow and tip of the fingers").setPosition([-4,0,0])
        p15=cvo.CVO().CreateCVO("Foot", "btw the sole and the toes").setPosition([-4,-2,0])
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
        p11.cvolist.append(p14)
        p11.cvolist.append(p15)
        self.construct1(p10,p10)

    
    def topic6(self):
        # Title
        title_text = Text("Non-standard measuring", font_size=48, color=BLUE)
        title = title_text.to_edge(UP)
        self.play(FadeIn(title))

        # Introduction
        intro_emoji = Text("🚶‍♀️‍➡️").scale(2.5)
        intro_text = Text("Using our body parts", font_size=36, color=BLUE)
        intro = VGroup(intro_emoji, intro_text).arrange(RIGHT, buff=0.5)
        intro.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(intro))
        
        self.wait(2)
        
        self.play(FadeOut(intro))

        measurements = [
            ("🖐️", "Hand Breadth", "Width of palm", BLUE, 1.5),
            ("🤚", "Hand Span", "Thumb to pinky when stretched", GREEN, 2.5),
            ("💪", "Cubit", "Elbow to middle fingertip", RED, 3),
            ("🦶", "Foot", "Heel to toe", YELLOW, 2)
        ]

        for emoji, name, description, color, arrow_length in measurements:
            # Create measurement representation
            measure_emoji = Text(emoji).scale(3.5)
            measure_name = Text(name, font_size=36, color=color)
            measure_group = VGroup(measure_emoji, measure_name).arrange(DOWN, buff=0.4)
            measure_group.to_edge(LEFT, buff=1.5)

            # Show measurement
            self.play(FadeIn(measure_group))

            # Create arrow
            arrow = Arrow(start=LEFT, end=RIGHT, color=color, buff=0)
            arrow.set_length(arrow_length)
            arrow.next_to(measure_group, RIGHT, buff=0.5)

            # Create description text
            desc_text = Text(description, font_size=28, color=WHITE)
            desc_text.next_to(arrow, RIGHT, buff=0.5)

            # Show arrow and description
            self.play(GrowArrow(arrow), Write(desc_text))

            

            self.wait(2)

            # Clear for next measurement
            self.play(FadeOut(measure_group), FadeOut(arrow), FadeOut(desc_text))

        self.wait(2)



    def SetDeveloperList(self): 
       self.DeveloperList="Medha Masanam" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade2Chapter13LengthofThings.py"



if __name__ == "__main__":
    scene = Grade2Chapter13LengthofThings()
    scene.render()