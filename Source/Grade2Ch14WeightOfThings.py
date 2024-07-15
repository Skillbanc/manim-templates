from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo
import random

class WeightOfTHingsClass2(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.topic1()
        self.fadeOutCurrentScene()
        self.topic2()
        self.fadeOutCurrentScene()
        #self.topic3()
        
        self.GithubSourceCodeReference()
    
    def topic1(self):
        self.isRandom = False
        self.angleChoice = [TAU/4,TAU/4,TAU/4]
        
        p10=cvo.CVO().CreateCVO("Weight of Things","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Definition", "how heavy something is").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("Heavy", "Something that feels hard to pick up").setPosition([5,-2,0])
        p13=cvo.CVO().CreateCVO("Light", "Something that feels easy to pick up").setPosition([-4,-1,0])
        
        
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
    
        
        self.construct1(p10,p10)
    

    


    def topic2(self):
        self.setup_scene()
        self.show_heavy_objects()
        self.show_light_objects()
        self.compare_weights()
        self.order_by_weight()

    def setup_scene(self):
        title = Text("Understanding Weight 🏋️", font_size=60, color=BLUE).to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)

    def show_heavy_objects(self):
        heavy_text = Text("Heavy Objects 🦛", font_size=48, color=RED).to_edge(UP, buff=1.5)
        self.play(Write(heavy_text))

        elephant = self.create_animal_with_label("🐘", "Elephant", PURPLE)
        camel = self.create_animal_with_label("🐪", "Camel", ORANGE)
        
        elephant.to_edge(LEFT, buff=1).shift(UP * 0.5)
        camel.to_edge(RIGHT, buff=1).shift(UP * 0.5)

        self.play(FadeIn(elephant), FadeIn(camel))
        self.wait(2)
        self.play(FadeOut(elephant), FadeOut(camel), FadeOut(heavy_text))

    def show_light_objects(self):
        light_text = Text("Light Objects 🍂", font_size=48, color=GREEN).to_edge(UP, buff=1.5)
        self.play(Write(light_text))

        feather = self.create_light_object_with_label("🪶", "Feather", YELLOW)
        leaf = self.create_light_object_with_label("🍃", "Leaf", TEAL)
        
        feather.to_edge(LEFT, buff=1).shift(UP * 0.5)
        leaf.to_edge(RIGHT, buff=1).shift(UP * 0.5)

        self.play(FadeIn(feather), FadeIn(leaf))
        self.wait(2)
        self.play(FadeOut(feather), FadeOut(leaf), FadeOut(light_text))

    def compare_weights(self):
        compare_text = Text("Comparing Weights ⚖️", font_size=48, color=GOLD).to_edge(UP, buff=1.5)
        self.play(Write(compare_text))

        cow = self.create_animal_with_label("🐄", "Cow", MAROON)
        dog = self.create_animal_with_label("🐕", "Dog", PINK)
        
        scale = Text("⚖️", font_size=96).move_to(self.camera.frame_center)
        cow.next_to(scale, LEFT, buff=1)
        dog.next_to(scale, RIGHT, buff=1)

        self.play(FadeIn(scale), FadeIn(cow), FadeIn(dog))
        self.wait(1)

        # Add the new text highlighting the weight difference
        result_text = Text("Cow is heavier than Dog", font_size=36, color=YELLOW)
        result_text.next_to(scale, DOWN, buff=1)

        # Animate the result text with a highlight effect
        self.play(Write(result_text))
        self.play(
            result_text.animate.set_color(RED).scale(1.2),
            run_time=0.5
        )
        self.play(
            result_text.animate.set_color(YELLOW).scale(1/1.2),
            run_time=0.5
        )

        self.wait(2)

        # Fade out all elements
        self.play(
            FadeOut(scale),
            FadeOut(cow),
            FadeOut(dog),
            FadeOut(compare_text),
            FadeOut(result_text)
        )
    """def compare_weights(self):
        compare_text = Text("Comparing Weights ⚖️", font_size=48, color=GOLD).to_edge(UP, buff=1.5)
        self.play(Write(compare_text))

        cow = self.create_animal_with_label("🐄", "Cow", MAROON)
        dog = self.create_animal_with_label("🐕", "Dog", PINK)
        
        scale = Text("⚖️", font_size=96).move_to(self.camera.frame_center)
        cow.next_to(scale, LEFT, buff=1)
        dog.next_to(scale, RIGHT, buff=1)

        self.play(FadeIn(scale), FadeIn(cow), FadeIn(dog))
        self.wait(2)
        self.play(FadeOut(scale), FadeOut(cow), FadeOut(dog), FadeOut(compare_text))"""

    
    def order_by_weight(self):
        # Random order
        random_text = Text("Random Objects 🎲", font_size=48, color=BLUE_D).to_edge(UP, buff=1.5)
        self.play(Write(random_text))

        objects = [
            self.create_object_with_label("🖊️", "Pen", RED_A),
            self.create_object_with_label("📕", "Book", GREEN_A),
            self.create_object_with_label("🪑", "Chair", YELLOW_A),
            self.create_object_with_label("🚗", "Car", PURPLE_A)
        ]
        
        random.shuffle(objects)
        
        object_group = VGroup(*objects).arrange(RIGHT, buff=1.5)
        object_group.next_to(random_text, DOWN, buff=1)

        self.play(FadeIn(object_group))
        self.wait(2)

        # Transition to ordered objects
        order_text = Text("Ordered by Weight 📊", font_size=48, color=BLUE_D).to_edge(UP, buff=1.5)
        self.play(Transform(random_text, order_text))

        ordered_objects = [
            self.create_object_with_label("🖊️", "Pen", RED_A),
            self.create_object_with_label("📕", "Book", GREEN_A),
            self.create_object_with_label("🪑", "Chair", YELLOW_A),
            self.create_object_with_label("🚗", "Car", PURPLE_A)
        ]
        
        ordered_group = VGroup(*ordered_objects).arrange(RIGHT, buff=1.5)
        ordered_group.next_to(order_text, DOWN, buff=1)

        numbers = VGroup(*[Text(str(i), font_size=36, color=BLUE) for i in range(1, 5)])
        for number, obj in zip(numbers, ordered_objects):
            number.next_to(obj, DOWN, buff=0.5)

        self.play(Transform(object_group, ordered_group), Write(numbers))
        self.wait(2)
        self.play(FadeOut(object_group), FadeOut(numbers), FadeOut(random_text))

    """def order_by_weight(self):
        order_text = Text("Ordering by Weight 📊", font_size=48, color=BLUE_D).to_edge(UP, buff=1.5)
        self.play(Write(order_text))

        objects = [
            self.create_object_with_label("🖊️", "Pen", RED_A),
            self.create_object_with_label("📕", "Book", GREEN_A),
            self.create_object_with_label("🪑", "Chair", YELLOW_A),
            self.create_object_with_label("🚗", "Car", PURPLE_A)
        ]
        
        object_group = VGroup(*objects).arrange(RIGHT, buff=1.5)
        object_group.next_to(order_text, DOWN, buff=1)

        numbers = VGroup(*[Text(str(i), font_size=36, color=BLUE) for i in range(1, 5)])
        for number, obj in zip(numbers, objects):
            number.next_to(obj, DOWN, buff=0.5)

        self.play(FadeIn(object_group), Write(numbers))
        self.wait(2)
        self.play(FadeOut(object_group), FadeOut(numbers), FadeOut(order_text))
"""
    def create_animal_with_label(self, emoji, animal_type, color):
        animal = Text(emoji, font_size=96)
        label = Text(animal_type.capitalize(), font_size=36, color=color).next_to(animal, DOWN, buff=0.5)
        return VGroup(animal, label)

    def create_light_object_with_label(self, emoji, obj_type, color):
        light_object = Text(emoji, font_size=96)
        label = Text(obj_type.capitalize(), font_size=36, color=color).next_to(light_object, DOWN, buff=0.5)
        return VGroup(light_object, label)

    def create_object_with_label(self, emoji, obj_type, color):
        obj = Text(emoji, font_size=96)
        label = Text(obj_type.capitalize(), font_size=30, color=color).next_to(obj, DOWN, buff=0.5)
        return VGroup(obj, label)

    """def topic2(self):
        self.setup_scene()
        self.show_heavy_objects()
        self.show_light_objects()
        self.compare_weights()
        self.order_by_weight()
        

    def setup_scene(self):
        title = Text("Understanding Weight", font_size=60).to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)

    def show_heavy_objects(self):
        heavy_text = Text("Heavy Objects", font_size=48).to_edge(UP, buff=1.5)
        self.play(Write(heavy_text))

        elephant = self.create_animal_with_label("🐘", "Elephant")
        camel = self.create_animal_with_label("🐪", "camel")
        
        elephant.to_edge(LEFT, buff=1).shift(UP * 0.5)
        camel.to_edge(RIGHT, buff=1).shift(UP * 0.5)

        self.play(FadeIn(elephant), FadeIn(camel))
        self.wait(2)
        self.play(FadeOut(elephant), FadeOut(camel), FadeOut(heavy_text))

    def show_light_objects(self):
        light_text = Text("Light Objects", font_size=48).to_edge(UP, buff=1.5)
        self.play(Write(light_text))

        feather = self.create_light_object_with_label("🪶", "Feather")
        leaf = self.create_light_object_with_label("🍃", "Leaf")
        
        feather.to_edge(LEFT, buff=1).shift(UP * 0.5)
        leaf.to_edge(RIGHT, buff=1).shift(UP * 0.5)

        self.play(FadeIn(feather), FadeIn(leaf))
        self.wait(2)
        self.play(FadeOut(feather), FadeOut(leaf), FadeOut(light_text))

    def compare_weights(self):
        compare_text = Text("Comparing Weights", font_size=48).to_edge(UP, buff=1.5)
        self.play(Write(compare_text))

        cow = self.create_animal_with_label("🐄", "cow")
        dog = self.create_animal_with_label("🐕", "Dog")
        
        scale = Text("⚖️", font_size=96).move_to(self.camera.frame_center)
        cow.next_to(scale, LEFT, buff=1)
        dog.next_to(scale, RIGHT, buff=1)

        self.play(FadeIn(scale), FadeIn(cow), FadeIn(dog))
        self.wait(2)
        self.play(FadeOut(scale), FadeOut(cow), FadeOut(dog), FadeOut(compare_text))

    def order_by_weight(self):
        order_text = Text("Ordering by Weight", font_size=48).to_edge(UP, buff=1.5)
        self.play(Write(order_text))

        objects = [
            self.create_object_with_label("🖊️", "pen"),
            self.create_object_with_label("📕", "book"),
            self.create_object_with_label("🪑", "table"),
            self.create_object_with_label("🚗", "car")
        ]
        
        object_group = VGroup(*objects).arrange(RIGHT, buff=1.5)
        object_group.next_to(order_text, DOWN, buff=1)

        numbers = VGroup(*[Text(str(i), font_size=36) for i in range(1, 5)])
        for number, obj in zip(numbers, objects):
            number.next_to(obj, DOWN, buff=0.5)

        self.play(FadeIn(object_group), Write(numbers))
        self.wait(2)
        self.play(FadeOut(object_group), FadeOut(numbers), FadeOut(order_text))

    

    def create_animal_with_label(self, emoji, animal_type):
        animal = Text(emoji, font_size=96)
        label = Text(animal_type.capitalize(), font_size=36).next_to(animal, DOWN, buff=0.5)
        return VGroup(animal, label)

    def create_light_object_with_label(self, emoji, obj_type):
        light_object = Text(emoji, font_size=96)
        label = Text(obj_type.capitalize(), font_size=36).next_to(light_object, DOWN, buff=0.5)
        return VGroup(light_object, label)

    def create_object_with_label(self, emoji, obj_type):
        obj = Text(emoji, font_size=96)
        label = Text(obj_type.capitalize(), font_size=30).next_to(obj, DOWN, buff=0.5)
        return VGroup(obj, label)"""
    
    
    
        
    

    def topic3(self):
    # Title
        title_emoji = Text("🐴").scale(2)
        title_text = Text("The Donkey's Lesson", font_size=36, color=WHITE)
        title = VGroup(title_emoji, title_text).arrange(RIGHT, buff=0.5).to_edge(UP)
        self.play(FadeIn(title))

        # Create story elements
        donkey = Text("🐴").scale(3)
        water = Text("💧").scale(3)
        salt = Text("🧂").scale(2)
        cotton = Text("🧶").scale(2)

        # Position elements
        story_elements = VGroup(donkey, water, salt, cotton).arrange(RIGHT, buff=1)
        story_elements.next_to(title, DOWN, buff=1)

        # Narration steps
        steps = [
            ("🖼️", "From pictures"),
            ("🚶‍♂️", "The donkey always going into water"),
            ("🧂💧", "Salt melts in water, weight of load decreases"),
            ("🔄", "The farmer replaced salt with cotton"),
            ("🧶💧", "When cotton soaked in water, it absorbs water"),
            ("⚖️", "The load becomes heavier"),
            ("📚", "By this, donkey learned a lesson"),
            ("🏁", "End of Narration")
        ]

        # Display story elements
        self.play(FadeIn(story_elements))

        # Animation for each step
        for emoji, text in steps:
            step_emoji = Text(emoji).scale(1.5)
            step_text = Text(text, font_size=24, color=WHITE)
            step = VGroup(step_emoji, step_text).arrange(RIGHT, buff=0.5)
            step.next_to(story_elements, DOWN, buff=0.5)

            self.play(FadeIn(step))
            self.wait(2)

            if "salt melts" in text.lower():
                self.play(FadeOut(salt))
            elif "replaced salt with cotton" in text.lower():
                self.play(salt.animate.become(cotton.copy().move_to(salt)))
            elif "cotton soaked" in text.lower():
                self.play(water.animate.set_color(BLUE))
            elif "load becomes heavier" in text.lower():
                self.play(cotton.animate.scale(1.2))

            self.play(FadeOut(step))

        # Fade out all elements
        self.play(FadeOut(title), FadeOut(story_elements))
        self.wait(2)
        
    def SetDeveloperList(self): 
       self.DeveloperList="dhanushofc" 
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Class2Ch14WeightOfThings.py"    

    
    
    
    
if __name__ == "__main__":
    scene = WeightOfTHingsClass2()
    scene.render()