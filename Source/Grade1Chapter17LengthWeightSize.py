from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo

class Grade1Chapter17LengthWeightSize(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.topic1()
        self.fadeOutCurrentScene()
        
        
        self.topic10()
        self.fadeOutCurrentScene()
        self.topic11()
        self.fadeOutCurrentScene()
        self.topic2()
        self.fadeOutCurrentScene()
        self.topic12()
        self.fadeOutCurrentScene()
        self.topic13()
        self.fadeOutCurrentScene()
        self.topic3()
        self.fadeOutCurrentScene()
        self.topic4()
        self.fadeOutCurrentScene()
        self.topic5()
        self.fadeOutCurrentScene()
        self.topic6()
        self.fadeOutCurrentScene()
        self.topic7()
        self.fadeOutCurrentScene()
        self.topic8()
        self.fadeOutCurrentScene()
        
        
        self.GithubSourceCodeReference()
        


    def topic1(self):
        self.isRandom = False
        self.angleChoice = [TAU/4]
        p10=cvo.CVO().CreateCVO("Length","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Definition", "how long something is").setPosition([4,2,0])
        

        p10.cvolist.append(p11)
        

        self.construct1(p10,p10)
        
    
        
    def topic10(self):
        self.isRandom = False
        self.angleChoice = [TAU/4]
        p10=cvo.CVO().CreateCVO("Weight","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Definition", "how heavy something is").setPosition([4,2,0])
        

        p10.cvolist.append(p11)
        

        self.construct1(p10,p10)
    
    def topic11(self):
        self.isRandom = False
        self.angleChoice = [TAU/4]
        p10=cvo.CVO().CreateCVO("Size","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Definition", "how big or small something is").setPosition([4,2,0])
        

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
    
    def topic12(self):
        self.isRandom = False
        self.angleChoice = [TAU/4,-TAU/4,-TAU/4]
        p10=cvo.CVO().CreateCVO("Standard measuring tools","").setPosition([0,2.5,0])
        
        p12=cvo.CVO().CreateCVO("Ruler", " helps measure lengths").setPosition([5,-2,0])
        p13=cvo.CVO().CreateCVO("Tapes", "measure distances ").setPosition([-4,1,0])
       

        
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        
        self.construct1(p10,p10)
        
    
    def topic13(self):
    # Title
        #title_emoji = Text("👨‍🔬").scale(2.5)
        title_text = Text("Standard Measuring Tools", font_size=48, color=BLUE)
        title = VGroup( title_text).arrange(RIGHT, buff=0.5).to_edge(UP)
        self.play(FadeIn(title))

        tools = [
            ("📏", "Ruler", "Measures length in cm and inches", BLUE),
            ("🧵", "Measuring Tape", "Flexible for curved surfaces", GREEN),
            ("⚖️", "Scale", "Measures weight or mass", RED),
            ("🧪", "Measuring Cup", "For volume in cooking", YELLOW),
            ("🌡️", "Thermometer", "Measures temperature", PURPLE)
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
    

    def topic3(self):
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

    
    def topic4(self):
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

      


    def topic5(self):
        p10=cvo.CVO().CreateCVO("Length","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Taller", "Something that is higher up or has more height").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("Shorter", "Something that doesn't reach as high or has less height").setPosition([5,-2,0])

        p10.cvolist.append(p11)
        p10.cvolist.append(p12)

        self.construct1(p10,p10)

    def topic6(self):
        self.isRandom = False
        self.angleChoice = [TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Weight","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Light", "Something that feels easy to pick up").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("Heavy", "Something that feels hard to pick up").setPosition([5,-2,0])

        p10.cvolist.append(p11)
        p10.cvolist.append(p12)

        self.construct1(p10,p10)

    def topic7(self):
        
        p10=cvo.CVO().CreateCVO("Size","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Big", "Something that takes up a lot of space").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("Small", "Something that takes up little space").setPosition([5,-2,0])

        p10.cvolist.append(p11)
        p10.cvolist.append(p12)

        self.construct1(p10,p10)

    def topic8(self):
        # Title
        title_emoji = Text("📐", color=YELLOW).scale(2)
        title_text = Text("About Measurements!", font_size=48, color=BLUE_E, weight=BOLD)
        title = VGroup(title_emoji, title_text).arrange(RIGHT, buff=0.5).to_edge(UP)
        self.play(FadeIn(title))
        
        self.wait(1)
        self.play(FadeOut(title))

        # Measurements
        self.show_measurement("Length", "🚂", "Train", "🐛", "Caterpillar", "Long", "Short", ORANGE, PURPLE)
        self.show_measurement("Weight", "🐘", "Elephant", "🪶", "Feather", "Heavy", "Light", TEAL, PINK)
        self.show_measurement("Size", "🏔️", "Mountain", "🐜", "Ant", "Big", "Small", GOLD, MAROON)

        # Conclusion
        
        self.wait(2)

    def show_measurement(self, title, emoji1, emoji_name1, emoji2, emoji_name2, label1, label2, color1, color2):
        subtitle = Text(title, font_size=40, color=GREEN, weight=BOLD).to_edge(UP)
        self.play(Write(subtitle))

        emoji_1 = Text(emoji1).scale(2)
        emoji_2 = Text(emoji2).scale(2)

        emoji_name_1 = Text(emoji_name1, font_size=24, color=GRAY).next_to(emoji_1, DOWN, buff=0.2)
        emoji_name_2 = Text(emoji_name2, font_size=24, color=GRAY).next_to(emoji_2, DOWN, buff=0.2)

        label_1 = Text(label1, font_size=32, color=color1, weight=BOLD).next_to(emoji_name_1, DOWN, buff=0.2)
        label_2 = Text(label2, font_size=32, color=color2, weight=BOLD).next_to(emoji_name_2, DOWN, buff=0.2)

        group_1 = VGroup(emoji_1, emoji_name_1, label_1).arrange(DOWN, buff=0.2).shift(LEFT * 3)
        group_2 = VGroup(emoji_2, emoji_name_2, label_2).arrange(DOWN, buff=0.2).shift(RIGHT * 3)

        category = Text(f"Category: {title} Measurement", font_size=36, color=WHITE, weight=BOLD).to_edge(DOWN)

        comparison = Text("vs", font_size=48, color=RED, weight=BOLD)

        self.play(
            FadeIn(group_1, shift=LEFT),
            FadeIn(group_2, shift=RIGHT),
            FadeIn(category, shift=UP),
            Write(comparison)
        )
        self.wait(2)

        self.play(
            FadeOut(subtitle),
            FadeOut(group_1, shift=LEFT),
            FadeOut(group_2, shift=RIGHT),
            FadeOut(category, shift=DOWN),
            FadeOut(comparison)
        )
    


    def SetDeveloperList(self): 
       self.DeveloperList="dhanushofc" 

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade1Chapter17LengthWeightSize.py"    





if __name__ == "__main__":
    scene = Grade1Chapter17LengthWeightSize()
    scene.render()