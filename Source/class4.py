from manim import *

class WeddingPreparations(Scene):
    def construct(self):
        self.introduction()
        self.shopping_for_sarees()
        self.buying_sweets()
        self.clear()
        self.posting_cards()
        self.clear()
        self.preparing_journey()
        self.clear()
        self.leaving_for_wedding()
        self.clear()
        self.tea_and_juice()
        self.clear()
        self.purchasing_flowers()

    def introduction(self):
        title = Text("Maths Around Us: A Wedding Journey", font_size=48, color=BLUE)
        subtitle = Text("Let's explore math in wedding preparations!", font_size=32, color=GREEN)
        subtitle.next_to(title, DOWN)

        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))

    def shopping_for_sarees(self):
        section_title = Text("Shopping for Sarees", font_size=40, color=YELLOW)
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP))

        saree_prices = [1500, 1300, 850, 2000, 3200]
        sarees = VGroup(*[Rectangle(height=1.5, width=0.75, fill_opacity=0.8, color=color) 
                          for color in [RED, BLUE, GREEN, YELLOW, PURPLE]])
        sarees.arrange(RIGHT, buff=0.5)

        price_labels = VGroup(*[Text(f"₹{price}", font_size=24).next_to(saree, DOWN) 
                                for saree, price in zip(sarees, saree_prices)])

        self.play(Create(sarees), Write(price_labels))
        self.wait(1)

        total = sum(saree_prices)
        total_text = MathTex(f"{'+'.join(map(str, saree_prices))} = {total}", font_size=36)
        total_text.next_to(sarees, DOWN, buff=1)
        self.play(Write(total_text))
        self.wait(2)

        payment = 9000
        change = payment - total
        change_text = Text(f"Change: ₹{change}", font_size=32, color=GREEN).next_to(total_text, DOWN)
        self.play(Write(change_text))
        self.wait(2)

        self.play(FadeOut(section_title), FadeOut(sarees), FadeOut(price_labels), 
                  FadeOut(total_text), FadeOut(change_text))
    
    def buying_sweets(self):
        laddoo_box = Square(side_length=1).set_fill(YELLOW, opacity=0.8)
        badhushaw_box = Square(side_length=1).set_fill(ORANGE, opacity=0.8)
        
        laddoo_label = Text("Laddoo\n20 kg", font_size=24).next_to(laddoo_box, DOWN)
        badhushaw_label = Text("Badhushaw\n20 kg", font_size=24).next_to(badhushaw_box, DOWN)
        
        laddoo_group = VGroup(laddoo_box, laddoo_label).shift(LEFT*2)
        badhushaw_group = VGroup(badhushaw_box, badhushaw_label).shift(RIGHT*2)
        
        laddoo_price = Text("₹120/kg", font_size=20).next_to(laddoo_box, UP)
        badhushaw_price = Text("₹150/kg", font_size=20).next_to(badhushaw_box, UP)
        
        self.play(Create(laddoo_group), Create(badhushaw_group))
        self.play(Write(laddoo_price), Write(badhushaw_price))
        self.wait(2)

    def posting_cards(self):
        envelope = Rectangle(height=2, width=3).set_fill(WHITE, opacity=0.5)
        weight = Text("35g", font_size=24).next_to(envelope, DOWN)
        
        post_office = Rectangle(height=3, width=4).set_fill(BLUE, opacity=0.3)
        rate_chart = Text("Rate: ₹5 for every 20g or less", font_size=20).next_to(post_office, DOWN)
        
        self.play(Create(envelope), Write(weight))
        self.play(envelope.animate.shift(RIGHT*3))
        self.play(Create(post_office), Write(rate_chart))
        self.play(envelope.animate.next_to(post_office, LEFT))
        self.wait(2)

    def preparing_journey(self):
        bus = Rectangle(height=2, width=4).set_fill(RED, opacity=0.5)
        wheels = VGroup(Circle(radius=0.3), Circle(radius=0.3)).arrange(RIGHT, buff=3)
        bus_group = VGroup(bus, wheels).shift(DOWN)
        
        seats = VGroup(*[Square(side_length=0.3) for _ in range(15*4)]).arrange_in_grid(rows=15, cols=4)
        seats.set_fill(BLUE, opacity=0.5).scale(0.8).move_to(bus)
        
        self.play(Create(bus_group))
        self.play(Create(seats))
        self.wait(2)

    def leaving_for_wedding(self):
        clock = Circle(radius=1).set_fill(WHITE, opacity=0.1)
        clock_center = Dot()
        hour_hand = Line(ORIGIN, UP*0.6).rotate(angle=-PI/2)
        minute_hand = Line(ORIGIN, UP*0.8)
        clock_group = VGroup(clock, clock_center, hour_hand, minute_hand)
        
        map_outline = Rectangle(height=3, width=5).set_fill(GREEN, opacity=0.1)
        adilabad = Dot().shift(UP*1 + LEFT*2)
        warangal = Dot().shift(DOWN*1 + RIGHT*2)
        route = Line(adilabad, warangal)
        
        self.play(Create(clock_group), Create(map_outline))
        self.play(Create(adilabad), Create(warangal), Create(route))
        self.play(Rotate(hour_hand, angle=PI/6), Rotate(minute_hand, angle=PI), run_time=2)
        self.wait(2)

    def tea_and_juice(self):
        tea_cup = Triangle().scale(0.5).set_fill(GOLD_E, opacity=0.8)
        juice_bottle = Rectangle(height=2, width=1).set_fill(ORANGE, opacity=0.5)
        
        
        
        tea_label = Text("90 cups", font_size=24).next_to(tea_cup, DOWN)
        juice_label = Text("4 x 2.5L bottles", font_size=24).next_to(juice_bottle, DOWN)
        
        tea_group = VGroup(tea_cup, tea_label).shift(LEFT*3)
        juice_group = VGroup(juice_bottle, juice_label).shift(RIGHT*3)
        
        self.play(Create(tea_group), Create(juice_group))
        self.wait(2)

    def purchasing_flowers(self):
        garland = Circle(radius=1).set_stroke(WHITE, width=2)
    
    # Create points on the circle
        num_flowers = 20
        flower_points = [
        np.array([np.cos(2*PI/num_flowers * i), np.sin(2*PI/num_flowers * i), 0])
        for i in range(num_flowers)
        ]   
    
    # Create Dots at these points
        flowers = VGroup(*[Dot(point=p, radius=0.1).set_color(YELLOW) for p in flower_points])
    
        label = Text("35 cubits of jasmine", font_size=24).next_to(garland, DOWN)
    
        self.play(Create(garland), Create(flowers))
        self.play(Write(label))
        self.wait(2)

if __name__ == "__main__":
    scene = WeddingPreparations()
    scene.render()