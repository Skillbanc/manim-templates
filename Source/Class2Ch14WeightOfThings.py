from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo

class WeightOfTHingsClass2(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.topic1()
        self.fadeOutCurrentScene()
        self.topic2()
        self.fadeOutCurrentScene()
        self.topic3()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
    
    def topic1(self):
        p10=cvo.CVO().CreateCVO("Weight of Things","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("def", "how heavy something is").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("Heavy", "Something that feels hard to pick up").setPosition([5,-2,0])
        p13=cvo.CVO().CreateCVO("Light", "Something that feels easy to pick up").setPosition([-4,3,0]).setangle(-TAU/4)
        
        
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
    
        
        self.construct1(p10,p10)
        
    def topic2(self):
        self.setup_scene()
        self.show_heavy_objects()
        self.show_light_objects()
        self.compare_weights()
        self.order_by_weight()
        self.conclusion()

    def setup_scene(self):
        title = Text("Understanding Weight", font_size=48).to_edge(UP)
        self.play(Write(title))

    def show_heavy_objects(self):
        heavy_text = Text("Heavy Objects", font_size=36).next_to(self.camera.frame_center, UP)
        self.play(Write(heavy_text))

        elephant = self.create_animal("elephant")
        camel = self.create_animal("camel")
        
        elephant.to_edge(LEFT)
        camel.to_edge(RIGHT)

        self.play(Create(elephant), Create(camel))
        self.wait(2)
        self.play(FadeOut(elephant), FadeOut(camel), FadeOut(heavy_text))

    def show_light_objects(self):
        light_text = Text("Light Objects", font_size=36).next_to(self.camera.frame_center, UP)
        self.play(Write(light_text))

        feather = self.create_light_object("feather")
        leaf = self.create_light_object("leaf")
        
        feather.to_edge(LEFT)
        leaf.to_edge(RIGHT)

        self.play(Create(feather), Create(leaf))
        self.wait(2)
        self.play(FadeOut(feather), FadeOut(leaf), FadeOut(light_text))

    def compare_weights(self):
        compare_text = Text("Comparing Weights", font_size=36).next_to(self.camera.frame_center, UP)
        self.play(Write(compare_text))

        cow = self.create_animal("cow")
        dog = self.create_animal("dog")
        
        cow.shift(LEFT * 2)
        dog.shift(RIGHT * 2)

        scale = self.create_scale()
        arrow = Arrow(start=LEFT, end=RIGHT, color=YELLOW)

        self.play(Create(cow), Create(dog), Create(scale), Create(arrow))
        self.wait(2)
        self.play(FadeOut(cow), FadeOut(dog), FadeOut(scale), FadeOut(arrow), FadeOut(compare_text))

    def order_by_weight(self):
        order_text = Text("Ordering by Weight", font_size=36).next_to(self.camera.frame_center, UP)
        self.play(Write(order_text))

        objects = [self.create_object("pen"), self.create_object("book"), 
                   self.create_object("table"), self.create_object("car")]
        object_group = VGroup(*objects).arrange(RIGHT, buff=1)

        numbers = VGroup(*[Text(str(i), font_size=24) for i in range(1, 5)])
        for number, obj in zip(numbers, objects):
            number.next_to(obj, DOWN)

        self.play(Create(object_group), Write(numbers))
        self.wait(2)
        self.play(FadeOut(object_group), FadeOut(numbers), FadeOut(order_text))

    def conclusion(self):
        conclusion_text = Text("Weight helps us compare objects!", font_size=36)
        self.play(Write(conclusion_text))
        self.wait(2)

    def create_animal(self, animal_type):
       if animal_type == "elephant":
        return VGroup(
            Circle(radius=0.5, fill_opacity=0.8, color=GRAY),
            Rectangle(height=0.8, width=0.6, fill_opacity=0.8, color=GRAY).next_to(Circle(radius=0.5), DOWN, buff=0),
            Line(start=LEFT*0.3, end=RIGHT*0.3).next_to(Circle(radius=0.5), DOWN, buff=-0.4)
        )
       elif animal_type in ["camel", "cow"]:
        return VGroup(
            Circle(radius=0.4, fill_opacity=0.8, color=DARK_BROWN),  # Changed BROWN to DARK_BROWN
            Rectangle(height=0.6, width=0.8, fill_opacity=0.8, color=DARK_BROWN).next_to(Circle(radius=0.4), DOWN, buff=0)
        )
       else:  # dog
           return VGroup(
            Circle(radius=0.3, fill_opacity=0.8, color=GOLD),
            Rectangle(height=0.4, width=0.6, fill_opacity=0.8, color=GOLD).next_to(Circle(radius=0.3), DOWN, buff=0)
        )
    def create_light_object(self, obj_type):
        if obj_type == "feather":
            return VGroup(
                Line(start=LEFT*0.5, end=RIGHT*0.5),
                Line(start=LEFT*0.5, end=RIGHT*0.5).rotate(PI/6),
                Line(start=LEFT*0.5, end=RIGHT*0.5).rotate(-PI/6)
            )
        else:  # leaf
            return VGroup(
                Ellipse(width=0.8, height=0.4, fill_opacity=0.8, color=GREEN),
                Line(start=ORIGIN, end=DOWN*0.4)
            )

    def create_scale(self):
        return VGroup(
            Line(start=LEFT, end=RIGHT),
            Triangle().scale(0.2).next_to(Line(start=LEFT, end=RIGHT), DOWN)
        )

    def create_object(self, obj_type):
        if obj_type == "pen":
            return Line(start=ORIGIN, end=UP).scale(0.5)
        elif obj_type == "book":
            return Rectangle(height=0.5, width=0.4)
        elif obj_type == "table":
            return VGroup(
                Rectangle(height=0.1, width=0.8),
                Line(start=LEFT*0.35, end=DOWN*0.4+LEFT*0.35),
                Line(start=RIGHT*0.35, end=DOWN*0.4+RIGHT*0.35)
            )
        else:  # car
            return VGroup(
                Rectangle(height=0.3, width=0.6),
                Circle(radius=0.1).next_to(Rectangle(height=0.3, width=0.6), DOWN, buff=-0.1).shift(LEFT*0.15),
                Circle(radius=0.1).next_to(Rectangle(height=0.3, width=0.6), DOWN, buff=-0.1).shift(RIGHT*0.15)
            )
            
    
    


    def topic3(self):
        # Text narration
        narration = Text("The Donkey's Lesson", font_size=36, color=WHITE)
        narration.to_edge(UP)
        self.play(Write(narration))
        self.wait(2)

        # Create donkey (using a simple shape)
        donkey = Circle(radius=0.5, color=GRAY, fill_opacity=1)
        donkey.next_to(narration, DOWN)
        self.play(Create(donkey))
        self.wait(1)

        # Create water (using a rectangle)
        water = Rectangle(width=6, height=1, color=BLUE, fill_opacity=0.5)
        water.next_to(donkey, DOWN)
        self.play(Create(water))
        self.wait(1)

        # Create salt (using text)
        salt = Text("Salt", font_size=24, color=WHITE).next_to(water, LEFT)
        self.play(Write(salt))
        self.wait(1)

        # Create cotton (using text)
        cotton = Text("Cotton", font_size=24, color=WHITE).next_to(water, RIGHT)
        self.play(Write(cotton))
        self.wait(1)

        # Animation: Salt melts in water
        self.play(FadeOut(salt))
        self.wait(1)

        # Animation: Replace salt with cotton
        self.play(Transform(cotton, donkey))
        self.wait(1)

        # Animation: Cotton absorbs water
        self.play(FadeOut(water))
        self.wait(1)

        # Animation: Load becomes heavier
        heavier_text = Text("Load becomes heavier", font_size=24, color=GREEN).next_to(cotton, DOWN)
        self.play(Write(heavier_text))
        self.wait(2)

        # Animation: Donkey learns a lesson
        lesson_text = Text("Donkey learns a lesson", font_size=24, color=GREEN).next_to(heavier_text, DOWN)
        self.play(Write(lesson_text))
        self.wait(2)

        # End of narration
        self.play(FadeOut(narration), FadeOut(cotton), FadeOut(heavier_text), FadeOut(lesson_text))

    """ def topic3(self):
        
        p10=cvo.CVO().CreateCVO("Narration of the story","").SetIsMathText(True)
        
       
        p10.onameList.append("From pictures")
        p10.onameList.append("The donkey always gng into water")
        p10.onameList.append("since salt melts in water , wt of load decreases")
        p10.onameList.append("The farmer replaced salt with cotton")
        p10.onameList.append("when cotton soaked in water , it absorbs water")
        p10.onameList.append("The load becomes heavier")
        p10.onameList.append("By this donkey learned lesson")
        p10.onameList.append("End of Narration")

        
        
        
        self.construct2(p10,p10)"""
        
    def SetDeveloperList(self): 
       self.DeveloperList="dhanushofc" 
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Class2Ch14WeightOfThings.py"    

    
    
    
    
if __name__ == "__main__":
    scene = WeightOfTHingsClass2()
    scene.render()