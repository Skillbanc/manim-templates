from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo

class LengthWeightSizeClass1(AbstractAnim):

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
        title_emoji = Text("👨‍🔬").scale(2)
        title_text = Text("Standard Measuring Tools", font_size=48, color=BLUE_E)
        title = VGroup(title_emoji, title_text).arrange(RIGHT, buff=0.5).to_edge(UP)
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
            tool_emoji = Text(emoji).scale(3)  # Large emoji for the tool
            tool_name = Text(name, font_size=36, color=BLACK)
            tool_group = VGroup(tool_emoji, tool_name).arrange(DOWN, buff=0.3)
            tool_group.to_edge(LEFT, buff=1)

            # Show tool
            self.play(FadeIn(tool_group))

            # Create info box
            info_box = Rectangle(width=6, height=2, fill_color=color, fill_opacity=0.1, stroke_color=color)
            info_box.next_to(tool_group, RIGHT, buff=1)

            # Create description text
            desc_text = Text(description, font_size=24, color=DARK_GRAY)
            desc_text.move_to(info_box.get_center())

            # Show info box and description
            self.play(Create(info_box), Write(desc_text))

            # Add a fun fact or usage example
            fact_emoji = Text("💡").scale(2)
            fact_text = Text(f"Used for {name.lower()} measurements!",
                            font_size=24, color=DARK_BROWN)
            fact = VGroup(fact_emoji, fact_text).arrange(RIGHT, buff=0.3).to_edge(DOWN)
            self.play(FadeIn(fact))

            self.wait(2)

            # Clear for next tool
            self.play(FadeOut(tool_group), FadeOut(info_box), FadeOut(desc_text), FadeOut(fact))

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
        title_emoji = Text("📝").scale(2)
        title_text = Text("Non-standard measuring", font_size=48, color=BLUE_E)
        title = VGroup(title_emoji, title_text).arrange(RIGHT, buff=0.5).to_edge(UP)
        self.play(FadeIn(title))

        # Introduction
        intro_emoji = Text("🚶‍♀️‍➡️").scale(2)
        intro_text = Text("Using our body parts", font_size=36, color=BLUE_E)
        intro = VGroup(intro_emoji, intro_text).arrange(RIGHT, buff=0.5)
        intro.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(intro))
        
        self.wait(2)
        
        self.play(FadeOut(intro))

        measurements = [
            ("🖐️", "Hand Breadth", 0.5, BLUE),
            ("🤚", "Hand Span", 1.5, GREEN),
            ("💪", "Cubit", 3, RED),
            ("🦶", "Foot", 2, YELLOW)
        ]

        for emoji, name, length, color in measurements:
            # Create measurement object
            measure = Rectangle(width=length, height=0.5, fill_color=color, fill_opacity=0.1, stroke_color=color)
            measure.to_edge(LEFT, buff=1)

            # Create label with emoji
            emoji_label = Text(emoji).scale(2)
            text_label = Text(name, font_size=36, color=BLACK)
            label = VGroup(emoji_label, text_label).arrange(DOWN, buff=0.3)
            label.next_to(measure, UP, buff=0.5)

            # Show measurement and label
            self.play(GrowFromCenter(measure), FadeIn(label))

            # Add a description
            description = Text(f"Used to measure about {length} units", font_size=24, color=DARK_GRAY)
            description.next_to(measure, RIGHT, buff=1)
            self.play(Write(description))

            # Add a fun fact
            fact_emoji = Text("💡").scale(2)
            fact_text = Text(f"We can measure with our {name.lower()}!",
                            font_size=24, color=DARK_BROWN)
            fact = VGroup(fact_emoji, fact_text).arrange(RIGHT, buff=0.3).to_edge(DOWN)
            self.play(FadeIn(fact))

            self.wait(2)

            # Clear for next measurement
            self.play(FadeOut(measure), FadeOut(label), FadeOut(description), FadeOut(fact))

      


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
        title_emoji = Text("📐").scale(2)
        title_text = Text("About Measurements!", font_size=42, color=BLUE_E)
        title = VGroup(title_emoji, title_text).arrange(RIGHT, buff=0.5).to_edge(UP)
        self.play(FadeIn(title))

        # Length
        self.show_length()

        # Weight
        self.show_weight()

        # Size
        self.show_size()

        # Conclusion
        conclusion_emoji = Text("📏").scale(2)
        conclusion_text = Text("Measuring", font_size=48, color=BLUE_E)
        conclusion = VGroup(conclusion_emoji, conclusion_text).arrange(RIGHT, buff=0.5)
        self.play(FadeIn(conclusion))
        self.wait(2)

    def show_length(self):
        subtitle = Text("Length", font_size=36, color=GREEN).next_to(self.camera.frame_center, UP)
        self.play(Write(subtitle))

        long_emoji = Text("🚂").scale(2)  # Train emoji for long
        short_emoji = Text("🐛").scale(2)  # Bug emoji for short

        long_label = Text("Long", font_size=28, color=BLUE).next_to(long_emoji, DOWN)
        short_label = Text("Short", font_size=24, color=RED).next_to(short_emoji, DOWN)

        long_group = VGroup(long_emoji, long_label).shift(LEFT * 3)
        short_group = VGroup(short_emoji, short_label).shift(RIGHT * 3)

        category = Text("Category: Distance", font_size=24, color=GRAY).to_edge(DOWN)

        self.play(FadeIn(long_group), FadeIn(short_group), FadeIn(category))
        self.wait(2)
        self.play(FadeOut(subtitle), FadeOut(long_group), FadeOut(short_group), FadeOut(category))

    def show_weight(self):
        subtitle = Text("Weight", font_size=36, color=GREEN).next_to(self.camera.frame_center, UP)
        self.play(Write(subtitle))

        heavy_emoji = Text("🐘").scale(2.5)  # Elephant emoji for heavy
        light_emoji = Text("🪶").scale(2)  # Feather emoji for light

        heavy_label = Text("Heavy", font_size=24, color=BLUE).next_to(heavy_emoji, DOWN)
        light_label = Text("Light", font_size=24, color=RED).next_to(light_emoji, DOWN)

        heavy_group = VGroup(heavy_emoji, heavy_label).shift(LEFT * 3)
        light_group = VGroup(light_emoji, light_label).shift(RIGHT * 3)

        category = Text("Category: Mass", font_size=24, color=GRAY).to_edge(DOWN)

        self.play(FadeIn(heavy_group), FadeIn(light_group), FadeIn(category))
        self.wait(2)
        self.play(FadeOut(subtitle), FadeOut(heavy_group), FadeOut(light_group), FadeOut(category))

    def show_size(self):
        subtitle = Text("Size", font_size=36, color=GREEN).next_to(self.camera.frame_center, UP)
        self.play(Write(subtitle))

        big_emoji = Text("🏔️").scale(2.5)  # Mountain emoji for big
        small_emoji = Text("🐜").scale(1.5)  # Ant emoji for small

        big_label = Text("Big", font_size=24, color=BLUE).next_to(big_emoji, DOWN)
        small_label = Text("Small", font_size=24, color=RED).next_to(small_emoji, DOWN)

        big_group = VGroup(big_emoji, big_label).shift(LEFT * 3)
        small_group = VGroup(small_emoji, small_label).shift(RIGHT * 3)

        category = Text("Category: Volume", font_size=24, color=GRAY).to_edge(DOWN)

        self.play(FadeIn(big_group), FadeIn(small_group), FadeIn(category))
        self.wait(2)
        self.play(FadeOut(subtitle), FadeOut(big_group), FadeOut(small_group), FadeOut(category))
    


    def SetDeveloperList(self): 
       self.DeveloperList="dhanushofc" 

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Class1Ch17LengthWeightSize.py"    





if __name__ == "__main__":
    scene = LengthWeightSizeClass1()
    scene.render()