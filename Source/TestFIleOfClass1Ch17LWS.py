from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo

class LengthWeightSizeClass1(AbstractAnim):

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
        self.topic7()
        self.fadeOutCurrentScene()
        self.topic8()
        self.fadeOutCurrentScene
        self.PurchaseSkillbancSubscription
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        self.SubscribeYoutube
        
    
    def topic1(self):
        p10=cvo.CVO().CreateCVO("length-weight-size","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("def", "").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("length", "how long something is").setPosition([5,-2,0])
        p13=cvo.CVO().CreateCVO("weight", "how heavy something is").setPosition([-4,3,0]).setangle(-TAU/4)
        p14=cvo.CVO().CreateCVO("size", "how big or small something is").setPosition([-4,1,0]).setangle(-TAU/4)
        
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
        p11.cvolist.append(p14)
        
        self.construct1(p10,p10)
    
    def topic2(self):
        p10=cvo.CVO().CreateCVO("Measuring tools","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Standard measuring tools", "official tools we use to measure").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("Non-standard measuring tools", "everyday things we use to measure").setPosition([5,-2,0])
        p13=cvo.CVO().CreateCVO("eg", "rulers ,tapes,meter sticks").setPosition([-4,3,0]).setangle(-TAU/4)
        p14=cvo.CVO().CreateCVO("eg", "body parts,ojects").setPosition([-4,1,0]).setangle(-TAU/4)
    
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p11.cvolist.append(p13)
        p12.cvolist.append(p14)
        self.construct1(p10,p10)
    
    
    def topic3(self):
        p10=cvo.CVO().CreateCVO("Non-standard measuring tools","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("using body parts", "").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("Hand-breadth", "equal to width of 4 fingers").setPosition([5,-2,0])
        p13=cvo.CVO().CreateCVO("Hand-span", "btw the little finger and thumb of hand").setPosition([-4,3,0]).setangle(-TAU/4)
        p14=cvo.CVO().CreateCVO("cubit", "btw the elbow and tip of the fingers").setPosition([-4,1,0]).setangle(-TAU/4)
        p15=cvo.CVO().CreateCVO("foot", "btw the sole and the toes").setPosition([-4,-1,0]).setangle(-TAU/4)
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
        p11.cvolist.append(p14)
        p11.cvolist.append(p15)
        self.construct1(p10,p10)
        
    def topic4(self):
        # Create a colorful background
        background = Rectangle(width=14, height=8, fill_color="#E6F3FF", fill_opacity=1)
        self.add(background)

        # Title
        title = Text("Non-standard measuring", font_size=48, color=BLUE_E).to_edge(UP)
        self.play(Write(title))

        # Create a simple arm using shapes
        arm = self.create_arm()
        self.play(Create(arm))

        measurements = [
            ("Hand Breadth", 0.5, BLUE),
            ("Hand Span", 1.5, GREEN),
            ("Cubit", 3, RED),
            ("Foot", 2, YELLOW)
        ]

        for name, length, color in measurements:
            # Create measurement object
            measure = Rectangle(width=length, height=0.5, fill_color=color, fill_opacity=0.8)
            measure.next_to(arm, RIGHT, buff=0.5)
            
            # Create label
            label = Text(name, font_size=36, color=BLACK).next_to(measure, UP)
            
            # Show measurement and label
            self.play(GrowFromCenter(measure), Write(label))
            
            # Show dotted lines connecting arm to measurement
            lines = DashedLine(arm.get_right(), measure.get_left(), dash_length=0.1)
            self.play(Create(lines))
            
            # Add a fun fact
            fact = Text(f"We can measure with our {name.lower()}!", 
                        font_size=24, color=DARK_BROWN).to_edge(DOWN)
            self.play(Write(fact))
            
            self.wait(2)
            
            # Clear for next measurement
            self.play(FadeOut(measure), FadeOut(label), FadeOut(lines), FadeOut(fact))

        # Conclusion
        conclusion = Text("Using our body parts", font_size=48, color=BLUE_E)
        self.play(Write(conclusion))
        self.wait(2)

    def create_arm(self):
        # Create a simple arm using rectangles and circles
        upper_arm = Rectangle(width=0.8, height=2, fill_color=LIGHT_BROWN, fill_opacity=1)
        elbow = Circle(radius=0.4, fill_color=LIGHT_BROWN, fill_opacity=1)
        forearm = Rectangle(width=0.7, height=1.8, fill_color=LIGHT_BROWN, fill_opacity=1)
        hand = Circle(radius=0.5, fill_color=LIGHT_BROWN, fill_opacity=1)

        elbow.next_to(upper_arm, DOWN, buff=0)
        forearm.next_to(elbow, DOWN, buff=0)
        hand.next_to(forearm, DOWN, buff=0)

        arm = VGroup(upper_arm, elbow, forearm, hand)
        arm.to_edge(LEFT)
        return arm

    
    def topic5(self):
        p10=cvo.CVO().CreateCVO("Length","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Taller", "Something that is higher up or has more height").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("Shorter", "Something that doesn't reach as high or has less height").setPosition([5,-2,0])
        
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        
        self.construct1(p10,p10)
        
    def topic6(self):
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
        # Background
        background = Rectangle(width=14, height=8, fill_color="#E6F3FF", fill_opacity=1)
        self.add(background)

        # Title
        title = Text("About Measurements!", font_size=42, color=BLUE_E).to_edge(UP)
        self.play(Write(title))

        # Length
        self.show_length()
        
        # Weight
        self.show_weight()
        
        # Size
        self.show_size()

        # Conclusion
        conclusion = Text("Measuring", font_size=48, color=BLUE_E)
        self.play(Write(conclusion))
        self.wait(2)

    def show_length(self):
        subtitle = Text("Length", font_size=36, color=GREEN).next_to(self.camera.frame_center, UP)
        self.play(Write(subtitle))

        long_line = Line(LEFT * 3, RIGHT * 3, color=YELLOW)
        short_line = Line(LEFT, RIGHT, color=RED)
        
        long_label = Text("Long", font_size=28, color=BLUE).next_to(long_line, UP)
        short_label = Text("Short", font_size=24, color=RED).next_to(short_line, DOWN)

        self.play(Create(long_line), Write(long_label))
        self.play(Create(short_line), Write(short_label))
        self.wait(2)
        self.play(FadeOut(subtitle), FadeOut(long_line), FadeOut(short_line), 
                  FadeOut(long_label), FadeOut(short_label))

    def show_weight(self):
        subtitle = Text("Weight", font_size=36, color=GREEN).next_to(self.camera.frame_center, UP)
        self.play(Write(subtitle))

        heavy_box = Square(side_length=2, fill_color=BLUE, fill_opacity=0.8)
        light_box = Square(side_length=1, fill_color=RED, fill_opacity=0.8)
        
        heavy_label = Text("Heavy", font_size=24, color=BLUE).next_to(heavy_box, UP)
        light_label = Text("Light", font_size=24, color=RED).next_to(light_box, UP)

        heavy_box.shift(LEFT * 2)
        light_box.shift(RIGHT * 2)

        self.play(Create(heavy_box), Write(heavy_label))
        self.play(Create(light_box), Write(light_label))
        self.wait(2)
        self.play(FadeOut(subtitle), FadeOut(heavy_box), FadeOut(light_box), 
                  FadeOut(heavy_label), FadeOut(light_label))

    def show_size(self):
        subtitle = Text("Size", font_size=36, color=GREEN).next_to(self.camera.frame_center, UP)
        self.play(Write(subtitle))

        big_circle = Circle(radius=2, fill_color=BLUE, fill_opacity=0.8)
        small_circle = Circle(radius=0.5, fill_color=RED, fill_opacity=0.8)
        
        big_label = Text("Big", font_size=24, color=BLUE).next_to(big_circle, UP)
        small_label = Text("Small", font_size=24, color=RED).next_to(small_circle, DOWN)

        big_circle.shift(LEFT * 2)
        small_circle.shift(RIGHT * 2)

        self.play(Create(big_circle), Write(big_label))
        self.play(Create(small_circle), Write(small_label))
        self.wait(2)
        self.play(FadeOut(subtitle), FadeOut(big_circle), FadeOut(small_circle), 
                  FadeOut(big_label), FadeOut(small_label))
    
    
    def SetDeveloperList(self): 
       self.DeveloperList="Dhanush" 
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="LengthWeightSizeClass1.py"    

    
    
    
    
if __name__ == "__main__":
    scene = LengthWeightSizeClass1()
    scene.render()