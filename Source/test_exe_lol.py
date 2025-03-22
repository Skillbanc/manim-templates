from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo

class MathsAroundUsGrade4(AbstractAnim,Scene):
    def construct(self):
        self.RenderSkillbancLogo()
        self.topic1()
        self.fadeOutCurrentScene()
        self.introduction()
        self.shopping_for_sarees()
        self.buying_sweets()
        self.posting_marriage_cards()
        self.preparing_for_journey()
        self.journey_to_warangal()
        self.tea_and_juice_break()
        self.purchasing_flowers()
        self.conclusion()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

    
    def topic1(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("Maths Around Us","a magical toolbox that helps us solve problems and understand the world around us").setPosition([0,2.5,0])
         p11=cvo.CVO().CreateCVO("Topic ","we learn abt who it is useful for santosh sister marriage").setPosition([4,2,0])
         p12=cvo.CVO().CreateCVO("Maths used in various scenario","").setPosition([5,-2,0])
         p13=cvo.CVO().CreateCVO("shopping of sarees","").setPosition([-4,3,0]).setangle(-TAU/4)
         p14=cvo.CVO().CreateCVO("buying sweets","").setPosition([-4,1,0]).setangle(-TAU/4)
         p15=cvo.CVO().CreateCVO("posting marriage cards","").setPosition([-4,-1,0]).setangle(-TAU/4)
         p16=cvo.CVO().CreateCVO("preparing for journey","").setPosition([-4,-3,0]).setangle(-TAU/4)
         p17=cvo.CVO().CreateCVO("tea and juice break","").setPosition([-2,-3,0])
         p18=cvo.CVO().CreateCVO("purchasing flowers","").setPosition([-6,-3,0]).setangle(-TAU/4)
         p11.cvolist.append(p12)

         p12.cvolist.append(p17)
         p12.cvolist.append(p18)
         

         p10.cvolist.append(p11)
         p12.cvolist.append(p13)
         p12.cvolist.append(p14)
         p12.cvolist.append(p15)
         p12.cvolist.append(p16)
         
         self.construct1(p10,p10)
    
    
    
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
        section_title = Text("Buying Sweets", font_size=40, color=YELLOW)
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP))

        laddoo = Circle(radius=0.3, color=ORANGE, fill_opacity=0.8)
        badhushaw = Rectangle(width=0.6, height=0.3, color=YELLOW, fill_opacity=0.8)

        laddoo_group = VGroup(*[laddoo.copy() for _ in range(5)]).arrange(RIGHT, buff=0.2)
        badhushaw_group = VGroup(*[badhushaw.copy() for _ in range(5)]).arrange(RIGHT, buff=0.2)
        sweets_group = VGroup(laddoo_group, badhushaw_group).arrange(DOWN, buff=0.5)

        laddoo_text = Text("Laddoo: ₹120/kg", font_size=24).next_to(laddoo_group, LEFT)
        badhushaw_text = Text("Badhushaw: ₹150/kg", font_size=24).next_to(badhushaw_group, LEFT)

        self.play(Create(sweets_group), Write(laddoo_text), Write(badhushaw_text))
        self.wait(1)

        calculation = MathTex("(20 \\times 120) + (20 \\times 150) = 5400", font_size=36)
        calculation.next_to(sweets_group, DOWN, buff=0.5)
        self.play(Write(calculation))
        self.wait(2)

        boxes = Text("40 boxes of 0.5 kg laddoos", font_size=32, color=GREEN).next_to(calculation, DOWN)
        self.play(Write(boxes))
        self.wait(2)

        self.play(FadeOut(section_title), FadeOut(sweets_group), FadeOut(laddoo_text), 
                FadeOut(badhushaw_text), FadeOut(calculation), FadeOut(boxes))

    """def buying_sweets(self):
        section_title = Text("Buying Sweets", font_size=40, color=YELLOW)
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP))

        laddoo = Circle(radius=0.3, color=ORANGE, fill_opacity=0.8)
        badhushaw = Rectangle(width=0.6, height=0.3, color=YELLOW, fill_opacity=0.8)

        laddoo_group = Group(*[laddoo.copy() for _ in range(5)]).arrange(RIGHT, buff=0.2)
        badhushaw_group = Group(*[badhushaw.copy() for _ in range(5)]).arrange(RIGHT, buff=0.2)
        sweets_group = VGroup(laddoo_group, badhushaw_group).arrange(DOWN, buff=0.5)

        laddoo_text = Text("Laddoo: ₹120/kg", font_size=24).next_to(laddoo_group, LEFT)
        badhushaw_text = Text("Badhushaw: ₹150/kg", font_size=24).next_to(badhushaw_group, LEFT)

        self.play(Create(sweets_group), Write(laddoo_text), Write(badhushaw_text))
        self.wait(1)

        calculation = MathTex("(20 \\times 120) + (20 \\times 150) = 5400", font_size=36)
        calculation.next_to(sweets_group, DOWN, buff=0.5)
        self.play(Write(calculation))
        self.wait(2)

        boxes = Text("40 boxes of 0.5 kg laddoos", font_size=32, color=GREEN).next_to(calculation, DOWN)
        self.play(Write(boxes))
        self.wait(2)

        self.play(FadeOut(section_title), FadeOut(sweets_group), FadeOut(laddoo_text), 
                  FadeOut(badhushaw_text), FadeOut(calculation), FadeOut(boxes))
    """
    """def buying_sweets(self):
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
        self.wait(2)"""

    def posting_marriage_cards(self):
        section_title = Text("Posting Marriage Cards", font_size=40, color=YELLOW)
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP))

        envelope = Polygon([-0.5, 0, 0], [0.5, 0, 0], [0.5, 0.75, 0], [0, 0.5, 0], [-0.5, 0.75, 0], color=WHITE)
        scale_factor = 2
        envelope.scale(scale_factor)
        weight_text = Text("35 grams", font_size=24).next_to(envelope, DOWN)

        self.play(Create(envelope), Write(weight_text))
        self.wait(1)

        rate_text = Text("Rate: ₹5 for every 20 gm or less", font_size=28).next_to(envelope, RIGHT)
        self.play(Write(rate_text))
        self.wait(1)

        calculation = MathTex("200 \\times 5 = 1000", font_size=36)
        calculation.next_to(envelope, DOWN, buff=1)
        self.play(Write(calculation))
        self.wait(2)

        total_cost = Text("Total cost for 200 cards: ₹1000", font_size=32, color=GREEN).next_to(calculation, DOWN)
        self.play(Write(total_cost))
        self.wait(2)

        self.play(FadeOut(section_title), FadeOut(envelope), FadeOut(weight_text), 
                  FadeOut(rate_text), FadeOut(calculation), FadeOut(total_cost))

    def preparing_for_journey(self):
        section_title = Text("Preparing for the Journey", font_size=40, color=YELLOW)
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP))

        bus = Rectangle(width=4, height=1.5, color=BLUE, fill_opacity=0.5)
        seats = VGroup(*[Rectangle(width=0.2, height=0.2, color=WHITE) for _ in range(60)])
        seats.arrange_in_grid(rows=4, cols=15, buff=0.1)
        seats.scale(0.9).move_to(bus)
        bus_with_seats = VGroup(bus, seats)

        self.play(Create(bus_with_seats))
        self.wait(1)

        capacity_text = Text("Capacity: 60 people", font_size=28).next_to(bus_with_seats, DOWN)
        self.play(Write(capacity_text))
        self.wait(1)

        total_people = MathTex("40 \\times 4 = 160", "\\text{ people}", font_size=36)
        total_people.next_to(capacity_text, DOWN)
        self.play(Write(total_people))
        self.wait(1)

        buses_needed = MathTex("160 \\div 60 = 2.67", "\\approx 3 \\text{ buses}", font_size=36)
        buses_needed.next_to(total_people, DOWN)
        self.play(Write(buses_needed))
        self.wait(2)

        self.play(FadeOut(section_title), FadeOut(bus_with_seats), FadeOut(capacity_text), 
                  FadeOut(total_people), FadeOut(buses_needed))

    def journey_to_warangal(self):
        section_title = Text("Journey to Warangal", font_size=40, color=YELLOW)
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP))

        timeline = NumberLine(x_range=[7, 13, 1], length=10, include_numbers=True, 
                              include_tip=True, numbers_to_exclude=[])
        timeline_label = Text("Time (hours)", font_size=24).next_to(timeline, DOWN)
        self.play(Create(timeline), Write(timeline_label))
        self.wait(1)

        start_point = Dot(timeline.n2p(7), color=GREEN)
        end_point = Dot(timeline.n2p(12), color=RED)
        journey = Line(start_point.get_center(), end_point.get_center(), color=YELLOW)

        self.play(Create(start_point), Create(end_point), Create(journey))
        self.wait(1)

        start_text = Text("Start: 7:00 AM", font_size=24, color=GREEN).next_to(start_point, UP)
        end_text = Text("Arrive: 12:00 PM", font_size=24, color=RED).next_to(end_point, UP)
        self.play(Write(start_text), Write(end_text))
        self.wait(1)

        distance_text = Text("Total distance: 250 km", font_size=28).next_to(timeline, DOWN, buff=1)
        self.play(Write(distance_text))
        self.wait(2)

        self.play(FadeOut(section_title), FadeOut(timeline), FadeOut(timeline_label), 
                  FadeOut(start_point), FadeOut(end_point), FadeOut(journey), 
                  FadeOut(start_text), FadeOut(end_text), FadeOut(distance_text))

    def tea_and_juice_break(self):
        section_title = Text("Tea and Juice Break", font_size=40, color=YELLOW)
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP))
        
        tea_cup = Triangle(color=ORANGE, fill_opacity=0.8)
        juice_glass = Rectangle(width=0.5, height=0.8, color=PURPLE, fill_opacity=0.5)

        tea_group = VGroup(*[tea_cup.copy() for _ in range(3)]).arrange(RIGHT, buff=0.2)
        juice_group = VGroup(*[juice_glass.copy() for _ in range(3)]).arrange(RIGHT, buff=0.2)
        drinks_group = VGroup(tea_group, juice_group).arrange(DOWN, buff=0.5)

        self.play(Create(drinks_group))
        self.wait(1)

        tea_text = Text("90 cups of tea", font_size=24).next_to(tea_group, RIGHT)
        juice_text = Text("10 liters of juice", font_size=24).next_to(juice_group, RIGHT)
        self.play(Write(tea_text), Write(juice_text))
        self.wait(1)

        tea_calculation = MathTex("90 \\times 5 = 450", font_size=32)
        juice_calculation = MathTex("10 \\times 18 = 180", font_size=32)
        calculations = VGroup(tea_calculation, juice_calculation).arrange(DOWN, buff=0.5)
        calculations.next_to(drinks_group, DOWN, buff=1)
        self.play(Write(calculations))
        self.wait(2)

        total_cost = Text("Total cost: ₹630", font_size=32, color=GREEN).next_to(calculations, DOWN)
        self.play(Write(total_cost))
        self.wait(2)

        self.play(FadeOut(section_title), FadeOut(drinks_group), FadeOut(tea_text), 
                  FadeOut(juice_text), FadeOut(calculations), FadeOut(total_cost))

    def purchasing_flowers(self):
        section_title = Text("Purchasing Flowers", font_size=40, color=YELLOW)
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP))

        flower = VGroup(
            Circle(radius=0.2, color=WHITE, fill_opacity=0.8),
            *[Ellipse(width=0.2, height=0.4, color=WHITE, fill_opacity=0.8).rotate(angle) 
              for angle in np.linspace(0, 2*PI, 5, endpoint=False)]
        )
        flower_garland = VGroup(*[flower.copy().scale(0.5) for _ in range(10)])
        flower_garland.arrange(RIGHT, buff=0.1)
        self.play(Create(flower_garland))
        self.wait(1)

        garland_text = Text("35 cubits of jasmine garlands", font_size=28).next_to(flower_garland, DOWN)
        self.play(Write(garland_text))
        self.wait(2)

        arrival_time = Text("Arrived at Warangal: 1:30 PM", font_size=32, color=GREEN).next_to(garland_text, DOWN)
        self.play(Write(arrival_time))
        self.wait(2)

        self.play(FadeOut(section_title), FadeOut(flower_garland), FadeOut(garland_text), FadeOut(arrival_time))

    def conclusion(self):
        conclusion_text = Text("Math is everywhere in wedding preparations!", font_size=48, color=YELLOW)
        subtext = Text("From shopping to travel, we use math in many ways.", font_size=32, color=GREEN)
        subtext.next_to(conclusion_text, DOWN)

        self.play(Write(conclusion_text))
        self.play(FadeIn(subtext))
        self.wait(3)
        self.play(FadeOut(conclusion_text), FadeOut(subtext))
    
    
    def SetDeveloperList(self): 
       self.DeveloperList="dhanushofc" 
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName=".py"  
        
        
if __name__ == "__main__":
    scene = MathsAroundUsGrade4()
    scene.render()