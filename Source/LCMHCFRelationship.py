from manim import *
from AbstractAnim import AbstractAnim
import cvo

class LCMHCFRelationship(AbstractAnim):
    def construct(self):
        self.isRandom = False
        self.positionChoice = [[0, 2, 0], [-3, -2, 0], [3, -2, 0]]
        
        p10 = cvo.CVO().CreateCVO("Relationship Between LCM and HCF", "").setangle(-TAU / 5)
        
        self.construct1(p10, p10)
        self.wait(1)
        self.clear()

        self.relationship_explanation()
        self.wait(2)
        self.clear()
        self.example_explanation()

    def relationship_explanation(self):
        heading = Text("Relationship Between LCM and HCF", color=DARK_BROWN, font_size=37).to_edge(UP * 1.25 + LEFT * 2)
        formula = MathTex(r"\text{LCM}(a, b) \times \text{HCF}(a, b) = a \times b", font_size=48).move_to([0, 1, 0])
        
        explanation = Text("The Least Common Multiple (LCM) and Highest Common Factor (HCF) of two numbers are related by the formula above.", font_size=29).next_to(formula, DOWN, buff=1)

        self.play(Write(heading))
        self.play(Write(formula))
        self.play(Write(explanation))
        self.wait(2)
        self.play(FadeOut(heading), FadeOut(formula), FadeOut(explanation))

    def example_explanation(self):
        heading = Text("Example", color=DARK_BROWN, font_size=37).to_edge(UP * 1.25 + LEFT * 2)
        sub_title1 = Text("Let's find the LCM and HCF of 8 and 12.", font_size=29).to_edge(UP * 3 + LEFT * 1)
        
        example_steps = [
            "8 = 2^3",
            "12 = 2^2 × 3",
            "HCF(8, 12) = 2^2 = 4",
            "LCM(8, 12) = 2^3 × 3 = 24"
        ]

        example_texts = [Text(step, font_size=29).move_to([0, 1 - i * 0.75, 0]) for i, step in enumerate(example_steps)]
        relationship_formula = MathTex(r"\text{LCM}(8, 12) \times \text{HCF}(8, 12) = 8 \times 12", font_size=48).move_to([0, -2, 0])
        result = MathTex(r"24 \times 4 = 96", font_size=48).move_to([0, -3, 0])

        self.play(Write(heading))
        self.play(Write(sub_title1))
        self.wait(1)

        for example_text in example_texts:
            self.play(Write(example_text))
            self.wait(1)

        self.play(Write(relationship_formula))
        self.wait(1)
        self.play(Write(result))
        self.wait(2)

if __name__ == "__main__":
    scene = LCMHCFRelationship()
    scene.render()