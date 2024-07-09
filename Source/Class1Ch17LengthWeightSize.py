from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo


class class4_17test(AbstractAnim,Scene):
    
    
    
    
    def construct(self):
        self.RenderSkillbancLogo()
        self.topic1()
        self.fadeOutCurrentScene()
        self.topic2()
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
        self.fadeOutCurrentScene
        self.PurchaseSkillbancSubscription
        self.fadeOutCurrentScene
        self.GithubSourceCodeReference
        self.SubscribeYoutube
    
    def topic1(self):
        self.isRandom = False
        self.angleChoice = [-TAU/4,-TAU/4]
        
        p10=cvo.CVO().CreateCVO("Maths Around Us","a magical toolbox that helps us solve problems and understand the world around us").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Topic ","we learn abt who it is useful for santosh sister marriage").setPosition([4,2,0])
         
        p16=cvo.CVO().CreateCVO("Maths used in various scenario","").setPosition([-4,-3,0])
         

        
         

        p10.cvolist.append(p11)
         
        p11.cvolist.append(p16)
         
        self.construct1(p10,p10)
         
         
         
    def topic2(self):
        self.isRandom = False
        self.angleChoice = [TAU/4,TAU/4,-TAU/4,-TAU/4]
        p10=cvo.CVO().CreateCVO("Used basic Mathematics concepts","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Addition", "").setPosition([4,2,0])
        p12=cvo.CVO().CreateCVO("Subtraction", "").setPosition([5,-2,0])
        p13=cvo.CVO().CreateCVO("Multiplication", "").setPosition([-4,-3,0])
        p14=cvo.CVO().CreateCVO("Division", "").setPosition([-4,1,0])
        
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        
        
       
        
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
        total_text = Text(f"Total prices:₹1500+₹1300+₹850+₹2000+₹3200 = ₹{total}", font_size=36)
        total_text.next_to(sarees, DOWN, buff=1)
        self.play(Write(total_text))
        self.wait(2)

        self.play(FadeOut(section_title), FadeOut(sarees), FadeOut(price_labels), FadeOut(total_text))

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
        
        calculation_laddoo = Text("For:(20 kg × ₹120/kg) = ₹2400", font_size=36)
        calculation_laddoo.next_to(sweets_group, DOWN)
        self.play(Write(calculation_laddoo))
        self.wait(2)
        
        calculation_badhushaw = Text("For:(20 kg × ₹150/kg) = ₹3000", font_size=36)
        calculation_badhushaw.next_to(calculation_laddoo, DOWN)
        self.play(Write(calculation_badhushaw))
        self.wait(2)
          
        
        calculation = Text("Total cost: ₹2400 + ₹3000  = ₹5400", font_size=36)
        calculation.next_to(calculation_badhushaw, DOWN)
        self.play(Write(calculation))
        self.wait(2)

        self.play(FadeOut(section_title), FadeOut(sweets_group), FadeOut(laddoo_text), 
                  FadeOut(badhushaw_text),FadeOut(calculation_laddoo),FadeOut(calculation_badhushaw) ,FadeOut(calculation))

    def posting_marriage_cards(self):
        section_title = Text("Posting Marriage Cards", font_size=40, color=YELLOW)
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP))

        # Create a more realistic envelope shape
        envelope_width = 3
        envelope_height = 2
        flap_height = 0.8

        envelope_body = Polygon(
            [-envelope_width/2, -envelope_height/2, 0],  # Bottom left
            [envelope_width/2, -envelope_height/2, 0],   # Bottom right
            [envelope_width/2, envelope_height/2, 0],    # Top right
            [-envelope_width/2, envelope_height/2, 0],   # Top left
            color=WHITE
        )

        # Create a curved flap
        flap_curve = ArcBetweenPoints(
            start=[-envelope_width/2, envelope_height/2, 0],
            end=[envelope_width/2, envelope_height/2, 0],
            angle=PI/3
        )

        # Combine envelope body and flap
        envelope = VGroup(envelope_body, flap_curve)

        # Add a line to represent the flap fold
        fold_line = Line(
            [-envelope_width/2, envelope_height/2, 0],
            [envelope_width/2, envelope_height/2, 0],
            color=WHITE
        )

        envelope_group = VGroup(envelope, fold_line)

        weight_text = Text("35 grams", font_size=24).next_to(envelope_group, DOWN)

        self.play(Create(envelope_group), Write(weight_text))
        self.wait(1)

        rate_text = Text("Rate: ₹5 for every 20g or less", font_size=28).next_to(envelope_group, RIGHT)
        self.play(Write(rate_text))
        self.wait(1)

        calculation = Text("For:(200 cards × ₹5/card) = ₹1000", font_size=36).next_to(envelope_group, DOWN)
        calculation.next_to(weight_text, DOWN)
        self.play(Write(calculation))
        self.wait(2)

        self.play(FadeOut(section_title), FadeOut(envelope_group), FadeOut(weight_text), 
                FadeOut(rate_text), FadeOut(calculation))
    """def posting_marriage_cards(self):
        section_title = Text("Posting Marriage Cards", font_size=40, color=YELLOW)
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP))

        
        envelope = Polygon(
        [-0.5, 0, 0],     # Bottom left
        [0.5, 0, 0],      # Bottom right
        [0.5, 0.75, 0],   # Top right
        [0, 1, 0],        # Top center (flap point)
        [-0.5, 0.75, 0],  # Top left
        color=WHITE
        )
        line = Line([-0.5, 0.75, 0],[0.5, 0.75, 0], color=WHITE)
        envelope.scale(2)
        line.scale(2)
        
         
        weight_text = Text("35 grams", font_size=24).next_to(envelope, DOWN)

        self.play(Create(envelope), Write(weight_text))
        self.wait(1)

        rate_text = Text("Rate: ₹5 for every 20 gm or less", font_size=28).next_to(envelope, RIGHT)
        self.play(Write(rate_text))
        self.wait(1)

        calculation = Text("200 cards × ₹5/card = ₹1000", font_size=36).next_to(envelope, DOWN)
        calculation.next_to(weight_text, DOWN)
        self.play(Write(calculation))
        self.wait(2)

        self.play(FadeOut(section_title), FadeOut(envelope), FadeOut(weight_text), 
                  FadeOut(rate_text), FadeOut(calculation))"""

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

        capacity_text = Text("Capacity: 60 people per bus", font_size=28).next_to(bus_with_seats, DOWN)
        self.play(Write(capacity_text))
        self.wait(1)
        
        capacity_text1 = Text("since a has bus 15 rows and 4 cols , 15 × 4 = 60", font_size=28).next_to(bus_with_seats, DOWN)
        capacity_text1.next_to(capacity_text,DOWN)
        self.play(Write(capacity_text1))
        self.wait(1)
        
        total_people = Text("40 families × 4 people/family = 160 people", font_size=36)
        total_people.next_to(capacity_text1, DOWN)
        self.play(Write(total_people))
        self.wait(1)

        buses_needed = Text("160 people ÷ 60 people/bus ≈ 3 buses", font_size=36)
        buses_needed.next_to(total_people, DOWN)
        self.play(Write(buses_needed))
        self.wait(2)

        self.play(FadeOut(section_title), FadeOut(bus_with_seats), FadeOut(capacity_text), FadeOut(capacity_text1),
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

        tea_calculation = Text("90 cups × ₹5/cup = ₹450", font_size=32)
        juice_calculation = Text("10 liters × ₹18/liter = ₹180", font_size=32)
        calculations = VGroup(tea_calculation, juice_calculation).arrange(DOWN, buff=0.5)
        calculations.next_to(drinks_group, DOWN, buff=0.5)
        self.play(Write(calculations))
        self.wait(2)

        total_cost = Text("Total cost: ₹630", font_size=32, color=GREEN).next_to(tea_calculation, LEFT)
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
        self.wait(1)

        cubit_info = Text("(1 cubit ≈ 45 cm)", font_size=24, color=BLUE)
        cubit_info.next_to(garland_text, DOWN)
        self.play(Write(cubit_info))
        self.wait(1)

        calculation = Text("35 cubits × 0.45 m/cubit = 15.75 meters", font_size=32)
        calculation.next_to(cubit_info, DOWN)
        self.play(Write(calculation))
        self.wait(2)

        self.play(FadeOut(section_title), FadeOut(flower_garland), FadeOut(garland_text), 
                  FadeOut(cubit_info), FadeOut(calculation))

    def conclusion(self):
        conclusion_text = Text("Math is all around us, even in wedding preparations!", font_size=36, color=YELLOW)
        self.play(Write(conclusion_text))
        self.wait(2)
        self.play(FadeOut(conclusion_text))
    
    def SetDeveloperList(self):
        self.DeveloperList="Dhanush"
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Class1Ch17LengthWeightSize.py"

if __name__ == "__main__":
    scene = class4_17test()
    scene.render()