import json
from manim import *
from AbstractAnim import AbstractAnim
import cvo
class weights(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.weight()
        self.measurements()
        self.example()
        self.example2()
        self.GithubSourceCodeReference()
    def weight(self):
        self.isRandom = False
        self.positionChoice = [[-5,0,0],[3,0,0]]
        a=cvo.CVO().CreateCVO("Weights","")
        a1=cvo.CVO().CreateCVO("Definition","The amount of mass or heaviness of an object")
        a.cvolist.append(a1)
        self.construct1(a,a)
        self.fadeOutCurrentScene()
    def measurements(self):
        self.isRandom = False
        self.positionChoice = [[-5,0,0],[3,0,0]]
        p=cvo.CVO().CreateCVO("Measurements","")
        p1=cvo.CVO().CreateCVO("Measured Through","")
        p1.appendOname=["kg","gm"]
        p.cvolist.append(p1)
        p1.extendOname(p1.appendOname)
        self.construct1(p,p)
        self.fadeOutCurrentScene()
    def example(self):
        text = Text("EXAMPLE 1", font_size=22,color=RED)
        text.add(Underline(text, buff=0.1))
        text.to_corner(UP + LEFT)
        self.play(Write(text))
        items = [
            ("Bag", 1.2),
            ("Coffee Cup", 0.3),
            ("TV", 8.0),
            ("Car", 1200),
            ("Bottle", 0.5)
        ]

        item_texts = [
            Text(f"{item}: {weight} kg").scale(0.7).to_edge(UP).shift(DOWN*i)
            for i, (item, weight) in enumerate(items)
        ]

        for item_text in item_texts:
            self.play(Write(item_text))

        least_weight_item = min(items, key=lambda x: x[1])
        least_weight_text = Text(f"Least weight: {least_weight_item[0]} ({least_weight_item[1]} kg)").scale(0.7).set_color(YELLOW).next_to(item_text,DOWN)

        for item_text in item_texts:
            if least_weight_item[0] in item_text.text:
                self.play(item_text.animate.set_color(YELLOW))
        
        self.play(Write(least_weight_text))
        self.fadeOutCurrentScene()
    def example2(self):
        text = Text("EXAMPLE 2", font_size=22,color=ORANGE)
        text.add(Underline(text, buff=0.1))
        text.to_corner(UP + LEFT)
        self.play(Write(text))   
        items = [
            ("Groceries", 5.2),
            ("Eggs", 0.8),
            ("Vegetables", 2.3),
            ("Fruits", 1.7)
        ]

        item_texts = [
            Text(f"{item}: {weight} kg").scale(0.7).to_edge(UP).shift(DOWN*i)
            for i, (item, weight) in enumerate(items)
        ]

        for item_text in item_texts:
            self.play(Write(item_text))

        total_weight = sum(weight for _, weight in items)
        total_weight_text = Text(f"Total weight: {total_weight} kg").scale(0.7).set_color(YELLOW).next_to(item_text,DOWN)

        self.play(Write(total_weight_text))
        self.play(Indicate(total_weight_text, color=GREEN), run_time=2)
        self.fadeOutCurrentScene()
    def SetDeveloperList(self): 
       self.DeveloperList="Abhiram" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Class4Chap9HowMuchDoesItWeigh.py"

if __name__ == "__main__":
    scene = weights()
    scene.render()