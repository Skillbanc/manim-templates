from manim import *
from AbstractAnim import AbstractAnim
import cvo

class probability(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.probabilitydef()
        self.fadeOutCurrentScene()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.formula()
        self.fadeOutCurrentScene()
        self.mutualc1c2()
        self.fadeOutCurrentScene()
        self.mutualevents()
        self.fadeOutCurrentScene()
        self.complic1c2()
        self.fadeOutCurrentScene()
        self.complimentary()
        self.fadeOutCurrentScene()
        self.impossiblec1c2()
        self.fadeOutCurrentScene()
        self.impossible()
        self.fadeOutCurrentScene()
        self.die()
        self.fadeOutCurrentScene()
        self.deckc1c2()
        self.fadeOutCurrentScene()
        self.DeckOfCards()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()


    def Introduction(self):
        text = Text("PROBABILITY")
        text1 = Text("What Is Probability?")
        text2 = Text("Probability means possibility. It is a branch of mathematics that deals with\nthe occurrence of a random event.The value is expressed from zero to one.")
        text.scale(0.75)
        text.to_edge(UP)
        text1.scale(0.75)
        text1.shift(UP*2)
        text2.scale(0.5)
        #text2.shift(DOWN)
        self.play(Write(text))
        self.play(Write(text1))
        self.play(Write(text2))
        self.wait(3)


    def formula(self):
        text = Text("PROBABILITY - A THEORETICAL APPROACH")
        text1 = Text("FORMULA => P(T) = Number of trials in which the event happened\n\t\t\t\t\t\t\t\t\t\t\t_______________________________\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tTotal number of trials")
        text2 = Text("The theoretical probability also called classical probability of an event T,\n\nwritten as P(T)")
        text.to_edge(UP)
        text.scale(0.75)
        text1.scale(0.5)
        text1.shift(DOWN)
        text2.shift(UP)
        text2.scale(0.5)
        self.play(Write(text))
        self.play(Write(text2))
        self.play(Write(text1))
        self.wait(3)

    def probabilitydef(self):
        self.setNumberOfCirclePositions(5)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("PROBABILITY","").setPosition([-4,2,0])
        p15=cvo.CVO().CreateCVO("DEFINED BY","Pierre Simon Laplace").setPosition([-4,-2.5,0])
        p11=cvo.CVO().CreateCVO("DENOTED AS","P(T)").setPosition([-3,0,0])
        p12=cvo.CVO().CreateCVO("FORMULA","P(T)=P(A)/P(S)").setPosition([3,2,0])
        p13=cvo.CVO().CreateCVO("Favourable Outcomes", "P(A").setPosition([4,-2.5,0])
        p14=cvo.CVO().CreateCVO("Total Outcomes","P(S").setPosition([4,0,0])
        p15.setcircleradius(1.5)
        p10.cvolist.append(p15)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p12.cvolist.append(p13)
        p12.cvolist.append(p14)
        self.construct1(p10,p10)


    def mutualc1c2(self):

        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Mutual Exclusive Events","").setPosition([-4,0,0])
        p12=cvo.CVO().CreateCVO("P(A or B)","Getting 2 or more events").setPosition([0,0,0])
        p13=cvo.CVO().CreateCVO("P(A or B)", "P(A)+P(B)").setPosition([4,0,0])
        p10.cvolist.append(p12)
        p10.SetIsMathText(True)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p12.pos,p13.pos)))



    def mutualevents(self):

        text = Text("MUTUALLY EXCLUSIVE EVENTS")
        text1 =  Text("Two or more events of an experiment, where occurence of an event prevents\noccurences of all other events, are called Mutually Exclusive Events.")
        text.scale(0.75)
        text.to_edge(UP)
        text1.scale(0.5)
        text1.shift(UP * 2)
        self.play(Write(text))
        self.play(Write(text1))
        self.wait(3)

        circle_A = Circle(radius=1.5, color=BLUE, fill_opacity=0.5).shift(DOWN + LEFT * 2)
        label_A = Text("A").next_to(circle_A, UP)
        
        circle_B = Circle(radius=1.5, color=RED, fill_opacity=0.5).shift(DOWN + RIGHT * 2)
        label_B = Text("B").next_to(circle_B, UP)
        
        self.play(Create(circle_A), Write(label_A))
        self.play(Create(circle_B), Write(label_B))
        
        mutually_exclusive_text = Text("Mutually Exclusive Events").to_edge(DOWN * 2)
        self.play(Write(mutually_exclusive_text))
        
        intersection_cross = Cross(stroke_width=4, color=YELLOW).scale(1.5)
        self.play(Create(intersection_cross))
        
        self.wait(3)


    def complic1c2(self):

        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Comlimentary Events","P('E)").setPosition([-4,0,0])
        p12=cvo.CVO().CreateCVO("Denoted as","P('E),'not E'").setPosition([0,0,0])
        p13=cvo.CVO().CreateCVO("P('E)", "P(E)+P('E)=1").setPosition([4,0,0])
        p10.cvolist.append(p12)
        p10.SetIsMathText(True)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p12.pos,p13.pos)))


    def complimentary(self):

        text = Text("COMPLEMENTARY EVENTS AND PROBABILITY")
        text1 = Text("P(E) + P(F) = 1/3 + 2/3 = 1\n\nHere F is the same as 'not E' because there are only two events.\n\nWe denote the event 'not E' by 'E . This is called the complement event of event E.\n\nSo, P(E) + P(not E) = 1\n\ni.e., P(E) + P('E) = 1, which gives us P('E) = 1 - P(E).\n\nIn general, it is true that for an event E, P('E) = 1 – P(E)")
        text.scale(0.75)
        text.to_edge(UP)
        text1.scale(0.5)
        self.play(Write(text))
        self.play(Write(text1), run_time = 25)
        self.wait(3)


    def impossiblec1c2(self):

        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Impossible And Certain Events","").setPosition([-3,2,0])
        p12=cvo.CVO().CreateCVO("Impossible Events","P(A) = 0").setPosition([3,2,0])
        p13=cvo.CVO().CreateCVO("Certain Events", "P(A)=1").setPosition([0,-2,0])
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.construct1(p10,p10)
        self.wait(2)
        

    def impossible(self):
        text = Text("IMPOSSIBLE AND CERTAIN EVENTS")
        text1 =  Text("The probability of an event which is impossible to occur is 0.\nSuch an event is called an impossible event.")
        text2 = Text(" The probability of an event which is sure (or certain) to occur is 1.\nSuch an event is called a sure event or a certain event.")
        text.to_edge(UP)
        text.scale(0.75)
        text1.scale(0.5)
        text1.shift(UP)
        text2.shift(DOWN)
        text2.scale(0.5)
        self.play(Write(text))
        self.play(Write(text1))
        self.play(Write(text2))
        self.wait(3)


    def die(self):

        textt2 = Text("PROBABILITY OF PLAYING DICE")
        textt2.to_edge(UP)
        textt2.scale(0.75)
        self.play(Write(textt2))
        self.wait(2)

        
        die_face = Square(side_length=2)

        dot_positions = [
            [ORIGIN],  # 1
            [LEFT, RIGHT],  # 2
            [LEFT + UP, ORIGIN, RIGHT + DOWN],  # 3
            [LEFT + UP, LEFT + DOWN, RIGHT + UP, RIGHT + DOWN],  # 4
            [LEFT + UP, LEFT + DOWN, ORIGIN, RIGHT + UP, RIGHT + DOWN],  # 5
            [LEFT + UP, LEFT, LEFT + DOWN, RIGHT + UP, RIGHT, RIGHT + DOWN],  # 6
        ]

        def create_dots(number):
            dots = VGroup()
            for pos in dot_positions[number - 1]:
                dot = Dot(pos * 0.5)
                dots.add(dot)
            return dots

        die_number = 1
        dots = create_dots(die_number)

        die = VGroup(die_face, dots)

        self.add(die)

        for die_number in range(2, 7):
            new_dots = create_dots(die_number)
            self.play(Transform(dots, new_dots))
            self.wait(1)


        text = Text("Pobability of getting 1 = 1/6\n\nPobability of getting 2 = 1/6\n\nPobability of getting 3 = 1/6")
        text1 = Text("Pobability of getting 4 = 1/6\n\nPobability of getting 5 = 1/6\n\nPobability of getting 6 = 1/6")
        text.scale(0.5)
        text1.scale(0.5)
        text.shift(LEFT*4)
        text1.shift(RIGHT*4)
        self.play(Write(text))
        self.play(Write(text1))


    def DeckOfCards(self):

        text =  Text("DECK OF CARDS")
        text.to_edge(UP)
        text.scale(0.75)
        self.play(Write(text))
        self.wait(2)

        # Define suits and ranks
        suits = ["♠", "♥", "♦", "♣"]
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        cards = [f"{rank}{suit}" for suit in suits for rank in ranks]

        rows = 4
        cols = 13
        card_width = 0.7
        card_height = 1.2
        spacing = 0.2

        for i, card in enumerate(cards):
            row = i // cols
            col = i % cols
            pos = LEFT * (cols / 2 ) + RIGHT * (col * (card_width + spacing)) + UP * (rows / 2) + DOWN * (row * (card_height + spacing))
            
            card_rect = Rectangle(width=card_width, height=card_height, color=WHITE).move_to(pos)
            card_text = Text(card, font_size=24).move_to(pos)
            
            self.add(card_rect)
            self.add(card_text)
        
        # Hold the final frame
        self.wait(2)

    def deckc1c2(self):

        self.setNumberOfCirclePositions(5)
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Deck Of Cards","").setPosition([-4,2,0])
        p12=cvo.CVO().CreateCVO("Spades","13").setPosition([3,2,0])
        p13=cvo.CVO().CreateCVO("Hearts", "13").setPosition([4,0,0])
        p14=cvo.CVO().CreateCVO("Diamonds","13").setPosition([2,-3,0])
        p15=cvo.CVO().CreateCVO("Clubs", "13").setPosition([-4,-3,0])
        p12.SetIsMathText(True)
        p13.SetIsMathText(True)
        p14.SetIsMathText(True)
        p15.SetIsMathText(True)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        self.construct1(p10,p10)
        self.wait(3)



    def SetDeveloperList(self):
        self.DeveloperList="SURADHYA REDDY"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade10Chapter13Probability.py"

if __name__ == "__main__":
    scene = probability()
    scene.render()