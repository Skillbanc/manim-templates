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
        self.Combinations()
        self.fadeOutCurrentScene()
        self.Pricewithcoins()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

    def Introduce_currency(self):
        self.angleChoice=[TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Currency","").setPosition([-3,0,0])
        p11=cvo.CVO().CreateCVO("Coins","").setPosition([1,2,0])
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
        
        # 2 Rupee coin
        two_rupee = self.create_equation("₹2", [], use_circle=True)
        self.play(FadeIn(two_rupee))
        self.wait(2)
        self.play(FadeOut(two_rupee))
        
        one_rupees = self.create_equation("₹2", ["₹1", "₹1"], use_circle=True)
        self.play(FadeIn(one_rupees))
        
        explanation = Text("Two Rupee coin is equivalent to two one rupee coins", font_size=24).set_color(BLUE).next_to(one_rupees, DOWN)
        self.play(Write(explanation))
        self.wait(2)
        self.play( FadeOut(one_rupees), FadeOut(explanation))

        # 5 Rupee coin representations
        five_rupee = self.create_equation("₹5", [], use_circle=True)
        self.play(FadeIn(five_rupee))
        self.wait(2)
        self.play(FadeOut(five_rupee))

        # First representation: 5 one-rupee coins
        eq_1 = self.create_equation("₹5", ["₹1", "₹1", "₹1", "₹1", "₹1"], use_circle=True)
        exp_1 = Text("Five Rupee coin is equivalent to five one rupee coins", font_size=24).set_color(BLUE).next_to(eq_1, DOWN)
        self.play(FadeIn(eq_1), Write(exp_1))
        self.wait(2)
        self.play(FadeOut(eq_1), FadeOut(exp_1))
        self.play(FadeIn(five_rupee))
        self.wait(2)
        self.play(FadeOut(five_rupee))

        # Second representation: 2 two-rupee coins + 1 one-rupee coin
        eq_2 = self.create_equation("₹5", ["₹2", "₹2", "₹1"], use_circle=True)
        exp_2 = Text("Five Rupee coin is equivalent to two two-rupee coins and one one-rupee coin", font_size=24).set_color(BLUE).next_to(eq_2, DOWN)
        self.play(FadeIn(eq_2), Write(exp_2))
        self.wait(2)
        self.play(FadeOut(eq_2), FadeOut(exp_2))
        self.play(FadeIn(five_rupee))
        self.wait(2)
        self.play(FadeOut(five_rupee))

        # Third representation: 1 two-rupee coin + 3 one-rupee coins
        eq_3 = self.create_equation("₹5", ["₹2", "₹1", "₹1", "₹1"], use_circle=True)
        exp_3 = Text("Five Rupee coin is equivalent to one two-rupee coin and three one-rupee coins", font_size=24).set_color(BLUE).next_to(eq_3, DOWN)
        self.play(FadeIn(eq_3), Write(exp_3))
        self.wait(2)
        self.play( FadeOut(eq_3), FadeOut(exp_3))
       
        # 10 Rupee note
        ten_rupee = self.create_equation("₹10", [], use_circle=False)
        self.play(FadeIn(ten_rupee))
        self.wait(2)
        self.play(FadeOut(ten_rupee))

        eq_10 = self.create_equation("₹10", ["₹5", "₹2", "₹2", "₹1"], use_circle=True)
        exp_10 = Text("Ten Rupee note is equivalent to one 5-rupee coin, two 2-rupee coins, and one 1-rupee coin", font_size=24).set_color(BLUE).next_to(eq_10, DOWN)
        self.play(FadeIn(eq_10), Write(exp_10))
        self.wait(2)
        self.play( FadeOut(eq_10), FadeOut(exp_10))

        # 20 Rupee note
        twenty_rupee = self.create_equation("₹20", [], use_circle=False)
        self.play(FadeIn(twenty_rupee))
        self.wait(2)
        self.play(FadeOut(twenty_rupee))

        eq_20 = self.create_equation("₹20", ["₹10", "₹10"], use_circle=False)
        exp_20 = Text("Twenty Rupee note is equivalent to two ten-rupee notes", font_size=24).set_color(BLUE).next_to(eq_20, DOWN)
        self.play(FadeIn(eq_20), Write(exp_20))
        self.wait(2)
        self.play(FadeOut(eq_20), FadeOut(exp_20))

        # 50 Rupee note
        fifty_rupee = self.create_equation("₹50", [], use_circle=False)
        self.play(FadeIn(fifty_rupee))
        self.wait(2)
        self.play(FadeOut(fifty_rupee))

        eq_50 = self.create_equation("₹50", ["₹20", "₹20", "₹10"], use_circle=False)
        exp_50 = Text("Fifty Rupee note is equivalent to two twenty-rupee notes and one ten-rupee note", font_size=24).set_color(BLUE).next_to(eq_50, DOWN)
        self.play(FadeIn(eq_50), Write(exp_50))
        self.wait(2)
        self.play( FadeOut(eq_50), FadeOut(exp_50))

        # 100 Rupee note
        hundred_rupee = self.create_equation("₹100", [], use_circle=False)
        self.play(FadeIn(hundred_rupee))
        self.wait(2)
        self.play(FadeOut(hundred_rupee))

        eq_100 = self.create_equation("₹100", ["₹50", "₹50"], use_circle=False)
        exp_100 = Text("Hundred Rupee note is equivalent to two fifty-rupee notes", font_size=24).set_color(BLUE).next_to(eq_100, DOWN)
        self.play(FadeIn(eq_100), Write(exp_100))
        self.wait(2)
        self.play(FadeOut(eq_100), FadeOut(exp_100))

        # 500 Rupee note
        five_hundred_rupee = self.create_equation("₹500", [], use_circle=False)
        self.play(FadeIn(five_hundred_rupee))
        self.wait(2)
        self.play(FadeOut(five_hundred_rupee))

        eq_500 = self.create_equation("₹500", ["₹100", "₹100", "₹100", "₹100", "₹100"], use_circle=False)
        exp_500 = Text("Five Hundred Rupee note is equivalent to five hundred-rupee notes", font_size=24).set_color(BLUE).next_to(eq_500, DOWN)
        self.play(FadeIn(eq_500), Write(exp_500))
        self.wait(2)
        self.play( FadeOut(eq_500), FadeOut(exp_500))

        self.play(FadeOut(title))

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
        text = Text("Look at the coins and add their values", font_size=36).to_edge(UP).set_color(YELLOW)
        self.play(Write(text))
        # Create 2 rupee and 1 rupee coins
        two_rupee = self.create_coin("₹2")
        one_rupee = self.create_coin("₹1")
        coins = VGroup(two_rupee, one_rupee).arrange(RIGHT, buff=0.5)
        coins.move_to(ORIGIN)
        # Display coins
        self.play(FadeIn(coins))
        self.wait(1)
        # Add plus sign
        plus_sign = Text("+", font_size=36, color=WHITE).move_to(coins.get_center())
        self.play(FadeIn(plus_sign))
        self.wait(1)
        # Create result
        equals_sign = Text("=", font_size=36, color=WHITE).next_to(coins, RIGHT, buff=0.5)
        result_box = Square(side_length=1.0, color=WHITE).next_to(equals_sign, RIGHT, buff=0.5)
        result_text = Text("₹3", font_size=24, color=WHITE).move_to(result_box.get_center())
        # Display result
        self.play(FadeIn(equals_sign), FadeIn(result_box))
        
        self.wait(2)
        self.play(FadeIn(result_text))
        # Fade out everything
        self.play(FadeOut(text), FadeOut(coins), FadeOut(plus_sign), 
                  FadeOut(equals_sign), FadeOut(result_box), FadeOut(result_text))

    def create_coin(self, value):
        coin = Circle(radius=0.4, color=GREEN, fill_opacity=0.8)
        coin_text = Text(value, font_size=20, color=WHITE).move_to(coin.get_center())
        return VGroup(coin, coin_text)

   

    def Pricewithcoins(self):
        example_text = Text("Identify value of coins equal to the price", font_size=36, color=BLUE).to_edge(UP)
        pen_image = Text("✏").scale(1).shift(LEFT*2,UP*2)
        equals_text = Text("=", font_size=36, color=WHITE).next_to(pen_image, RIGHT, buff=0.5)
        coins_example = self.create_coins(["₹5", "₹1"]).next_to(equals_text,RIGHT,buff=0.5)
        price_example = Text("Rs. 6", font_size=28, color=BLUE).next_to(pen_image, DOWN, buff=0.5)
        imagegroup = VGroup(pen_image, price_example)
        example_group = VGroup(equals_text, coins_example)

        self.play(Create(example_text))
        self.wait(2)
        self.play(Write(imagegroup))
        self.wait(2)
        self.play(Write(example_group))

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