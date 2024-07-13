from AbstractAnim import AbstractAnim
import cvo
from manim import *

class Grade1Chapter15Money(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduce_currency()
        self.Show_coins()
        self.Show_notes()
        self.fadeOutCurrentScene()
        self.Display_currency_relationships()
        self.fadeOutCurrentScene()
        #self.create_equation()
        #self.fadeOutCurrentScene()
        self.Combinations()
        self.fadeOutCurrentScene()
        #self.combined_equation()
        #self.fadeOutCurrentScene()
        self.Pricewithcoins()
        self.fadeOutCurrentScene()
        #self.create_coins()
        #self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

    

    def Introduce_currency(self):
        self.angleChoice=[TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Currency","").setPosition([-3,0,0])
        p11=cvo.CVO().CreateCVO("Coins","").setPosition([0,2,0])
        p12=cvo.CVO().CreateCVO("Notes","").setPosition([0,-2,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
        title = Text("Indian Currency", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

    def Show_coins(self):
        coins = [
            ("₹1", "#C0C0C0", 0.5),
            ("₹2", "#C0C0C0", 0.55),
            ("₹5", "#D4AF37", 0.6),
        ]

        coin_group = VGroup()
        for value, color, size in coins:
            coin = Circle(radius=size, color=color, fill_opacity=0.8)
            text = Text(value, font_size=24).move_to(coin.get_center())
            coin_group.add(VGroup(coin, text))

        coin_group.arrange(RIGHT, buff=0.5)
        coin_title = Text("Coins", font_size=36).next_to(coin_group, UP)
        
        self.play(Write(coin_title))
        self.play(Create(coin_group))
        self.wait(1)
        self.play(FadeOut(coin_title,coin_group))

    def Show_notes(self):
        notes = [
            ("₹10", "#FFA07A", (1.2, 0.6)),
            ("₹20", "#85BB65", (1.2, 0.6)),
            ("₹50", "#87CEEB", (1.2, 0.6)),
            ("₹100", "#E6E6FA", (1.2, 0.6)),
            ("₹500", "#006400", (1.2, 0.6)),
        ]

        note_group = VGroup()
        for value, color, size in notes:
            note = Rectangle(height=size[1], width=size[0], color=color, fill_opacity=0.8)
            text = Text(value, font_size=24).move_to(note.get_center())
            note_group.add(VGroup(note, text))

        note_group.arrange(RIGHT, buff=0.5)
        note_title = Text("Currency Notes", font_size=36).next_to(note_group, UP)
        
        self.play(Write(note_title))
        self.play(Create(note_group))
        self.wait(3)

    def Display_currency_relationships(self):
        title = Text("Equivalent combinations of Currency", font_size=36).set_color(YELLOW).to_edge(UP)
        self.play(Write(title))
        
        # 2 Rupee in Circle = 1 Rupee of two Circles
        equation_1 = self.create_equation("₹2",["₹1","₹1"], use_circle=True)
        self.play(FadeIn(equation_1))
        self.wait(2)
        self.play(FadeOut(equation_1))

        # 5 Rupee in Circle = 1 Rupee of five Circles
        equation_2_1 = self.create_equation("₹5", ["₹1", "₹1","₹1","₹1","₹1"], use_circle=True).shift(UP * 2)
        # 5 Rupee in Circle = 2 Rupee of one Circle + 1 Rupee of three Circles
        equation_2_2 = self.create_equation("₹5", ["₹2", "₹1", "₹1", "₹1"], use_circle=True)
        # 5 Rupee in Circle = 2 Rupee of two Circles + 1 Rupee of one Circle
        equation_2_3 = self.create_equation("₹5", ["₹2", "₹2", "₹1"], use_circle=True).shift(DOWN * 2)
        self.play(FadeIn(equation_2_1))
        self.wait(2)
        self.play(FadeIn(equation_2_2))
        self.wait(2)
        self.play(FadeIn(equation_2_3))
        self.wait(2)
        self.play(FadeOut(equation_2_1), FadeOut(equation_2_2), FadeOut(equation_2_3))

        # 10 Rupee in Rectangle = 5 Rupee of one Circle + 2 Rupee of two Circles + 1 Rupee of one Circle
        high_val_rect = Rectangle(height=0.8, width=1.5, color=BLUE, fill_opacity=0.8)
        high_val_text = Text("₹10", font_size=24).move_to(high_val_rect.get_center())

        # Create circles for lower values
        low_values = [("₹5", 0.55), ("₹2", 0.5), ("₹2", 0.5), ("₹1", 0.4)]
        circles = VGroup()
        
        for val, radius in low_values:
            circle = Circle(radius=radius, color="#C0C0C0", fill_opacity=0.8)
            circle_text = Text(val, font_size=20).move_to(circle.get_center())
            circles.add(VGroup(circle, circle_text))

        # Arrange circles and texts
        circles.arrange(RIGHT, buff=0.5)

        # Combine high value rectangle and circles
        equals = Text("=", font_size=36)
        left = VGroup(high_val_rect, high_val_text)
        right = circles

        equation3 = VGroup(left, equals, right).arrange(RIGHT, buff=0.5)

        # Display equation
        self.play(FadeIn(equation3))
        self.wait(2)
        self.play(FadeOut(equation3))

        # 20 Rupee in Rectangle = 10 Rupee of one Rectangle + 10 Rupee of one Rectangle
        equation_4 = self.create_equation("₹20", ["₹10", "₹10"], use_circle=False)
        self.play(FadeIn(equation_4))
        self.wait(2)
        self.play(FadeOut(equation_4))

        # 50 Rupee in Rectangle = 20 Rupee of two Rectangles + 10 Rupee of one Rectangle
        equation_5 = self.create_equation("₹50", ["₹20", "₹20", "₹10"], use_circle=False)
        self.play(FadeIn(equation_5))
        self.wait(2)
        self.play(FadeOut(equation_5))

        # 100 Rupee in Rectangle = 50 Rupee of two Rectangles (with plus signs)
        equation_6 = self.create_equation("₹100", ["₹50", "₹50"], use_circle=False)
        self.play(FadeIn(equation_6))
        self.wait(2)
        self.play(FadeOut(equation_6))

        # 500 Rupee in Rectangle = 100 Rupee of five Rectangles (with plus signs)
        equation_7 = self.create_equation("₹500", ["₹100", "₹100", "₹100", "₹100", "₹100"], use_circle=False)
        self.play(Create(equation_7))
        self.wait(2)
        self.play(FadeOut(equation_7))

    def create_equation(self, high_val, low_vals, use_circle=False):
        shape = Circle(radius=0.6, color=YELLOW, fill_opacity=0.8) if use_circle else Rectangle(height=0.8, width=1.5, color=BLUE, fill_opacity=0.8)
        left_text = Text(high_val, font_size=24, color=WHITE).move_to(shape)

        equals = Text("=", font_size=36, color=WHITE)

        right_shapes = VGroup(*[Circle(radius=0.4, color="#C0C0C0", fill_opacity=0.8) for _ in low_vals] if use_circle else 
                            [Rectangle(height=0.6, width=1.0, color=GREEN, fill_opacity=0.8) for _ in low_vals])
        right_shapes.arrange(RIGHT, buff=0.2)

        right_text = VGroup(*[Text(val, font_size=20, color=WHITE).move_to(shape.get_center()) for shape, val in zip(right_shapes, low_vals)])

        equation = VGroup(VGroup(shape, left_text), equals, VGroup(right_shapes, right_text)).arrange(RIGHT, buff=0.5)

        return equation

    def Combinations(self):
        text = Text("Look at the coins and add their values",font_size=36).to_edge(UP).set_color(YELLOW)
        self.play(Write(text))
        # Example 1: ₹2 + ₹5 = ₹7
        eq_1 = self.combined_equation(["₹2", "₹1"], 3)
        eq_1.shift(UP * 1)
        self.play(Create(eq_1))
        self.wait(2)

        # Example 2: ₹2 + ₹2 + ₹1 = ₹5
        eq_2 = self.combined_equation(["₹2", "₹5", "₹1"], 8)
        eq_2.shift(DOWN * 1)
        self.play(Create(eq_2))
        self.wait(2)
        self.play(FadeOut(text,eq_1,eq_2))

    def combined_equation(self, coin_values, total_value):
        # Create coin shapes with text inside
        coins_and_texts = VGroup()
        for val in coin_values:
            coin = Circle(radius=0.4, color=GREEN, fill_opacity=0.8)
            coin_text = Text(val, font_size=20, color=WHITE).move_to(coin.get_center())
            coins_and_texts.add(VGroup(coin, coin_text))
            plus_sign = Text("+", font_size=24, color=WHITE)
            coins_and_texts.add(plus_sign)
        coins_and_texts.remove(plus_sign)  # Remove the last unnecessary plus sign
        coins_and_texts.arrange(RIGHT, buff=0.2)

        # Create the box with the total value
        box = Square(side_length=1.0)
        box_text = Text(f"₹{total_value}", font_size=24, color=WHITE).move_to(box)

        # Arrange the equation
        equation = VGroup(
            coins_and_texts,
            Text("=", font_size=36, color=WHITE),
            VGroup(box, box_text)
        ).arrange(RIGHT, buff=0.5)

        return equation

    def Pricewithcoins(self):
        # Example: Pen costing Rs. 6
        example_text = Text("Identify value of coins equal to the price", font_size=36, color=BLUE).to_edge(UP)
        pen_image = Text("✏️").scale(1).shift(LEFT*2,UP*2)
        equals_text = Text("=", font_size=36, color=WHITE).next_to(pen_image, RIGHT, buff=0.5)
        coins_example = self.create_coins(["₹5", "₹1"]).next_to(equals_text,RIGHT,buff=0.5)
        price_example = Text("Rs. 6", font_size=28, color=BLUE).next_to(pen_image, DOWN, buff=0.5)
        imagegroup = VGroup(pen_image, price_example)
        example_group = VGroup(equals_text, coins_example)

        self.play(Create(example_text), Write(imagegroup))
        self.wait(2)
        self.play(Write(example_group))
        # Example: chocolate costing Rs. 10
        chocolate_image = Text("🍫").scale(1).next_to(pen_image,DOWN,buff=1)
        equals_text1 = Text("=", font_size=36, color=WHITE).next_to(chocolate_image, RIGHT, buff=0.5).shift(DOWN*1)
        coins_example1 = self.create_coins(["₹5", "₹5"]).next_to(equals_text1,RIGHT,buff=0.5)
        price_example1 = Text("Rs. 10", font_size=28, color=BLUE).next_to(chocolate_image, DOWN, buff=0.5)
        imagegroup1 = VGroup(chocolate_image, price_example1).shift(DOWN*1)
        example_group1 = VGroup(equals_text1, coins_example1)

        self.play(Write(imagegroup1))
        self.wait(2)
        self.play(Write(example_group1))

    def create_coins(self, values, empty=False):
        coins = VGroup()
        for val in values:
            coin = Circle(radius=0.4, color=GREEN, fill_opacity=0.8)
            if not empty:
                coin_text = Text(val, font_size=20, color=WHITE).move_to(coin.get_center())
                coins.add(VGroup(coin, coin_text))
            else:
                coins.add(coin)
            plus_sign = Text("+", font_size=24, color=WHITE)
            coins.add(plus_sign)
        coins.remove(plus_sign)  # Remove the last unnecessary plus sign
        coins.arrange(RIGHT, buff=0.2)
        return coins
    
    def SetDeveloperList(self): 
       self.DeveloperList="Medha Masanam" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade1Chapter15Money.py"
    


# To render the scene
if __name__ == "__main__":
    scene = Grade1Chapter15Money()
    scene.render()
