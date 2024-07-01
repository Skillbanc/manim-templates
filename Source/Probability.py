from manim import *
from AbstractAnim import AbstractAnim
import cvo

class probability(AbstractAnim):

    def construct(self):
        '''self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.formula()
        self.fadeOutCurrentScene()
        self.probabilitydef()
        self.fadeOutCurrentScene()
        self.mutualevents()
        self.fadeOutCurrentScene()
        self.complimentary()
        self.fadeOutCurrentScene()
        self.impossible()
        self.fadeOutCurrentScene()
        self.die()
        self.fadeOutCurrentScene()
        self.DeckOfCards()'''
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
        p13=cvo.CVO().CreateCVO("P(A)", "Favourable Outcomes").setPosition([4,-2.5,0])
        p14=cvo.CVO().CreateCVO("P(S)","Total Outcomes").setPosition([4,0,0])
        p15.setcircleradius(1.5)
        p10.cvolist.append(p15)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p12.cvolist.append(p13)
        p12.cvolist.append(p14)
        self.construct1(p10,p10)


    def mutualevents(self):
        text = Text("MUTUALLY EXCLUSIVE EVENTS")
        text1 =  Text("Two or more events of an experiment, where occurence of an event prevents\noccurences of all other events, are called Mutually Exclusive Events.")
        text.scale(0.75)
        text.to_edge(UP)
        text1.scale(0.5)
        text1.shift(UP)
        self.play(Write(text))
        self.play(Write(text1))
        self.wait(3)


    def complimentary(self):
        text = Text("COMPLEMENTARY EVENTS AND PROBABILITY")
        text1 = Text("P(E) + P(F) = 1/3 + 2/3 = 1\n\nHere F is the same as 'not E' because there are only two events.\n\nWe denote the event 'not E' by E . This is called the complement event of event E.\n\nSo, P(E) + P(not E) = 1\n\ni.e., P(E) + P('E) = 1, which gives us P('E) = 1 - P(E).\n\nIn general, it is true that for an event E, P('E) = 1 – P(E)")
        text.scale(0.75)
        text.to_edge(UP)
        text1.scale(0.5)
        self.play(Write(text))
        self.play(Write(text1))
        self.wait(3)


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

        # Define dot positions for each face of the die
        dot_positions = [
            [ORIGIN],  # 1
            [LEFT, RIGHT],  # 2
            [LEFT + UP, ORIGIN, RIGHT + DOWN],  # 3
            [LEFT + UP, LEFT + DOWN, RIGHT + UP, RIGHT + DOWN],  # 4
            [LEFT + UP, LEFT + DOWN, ORIGIN, RIGHT + UP, RIGHT + DOWN],  # 5
            [LEFT + UP, LEFT, LEFT + DOWN, RIGHT + UP, RIGHT, RIGHT + DOWN],  # 6
        ]

        # Function to create dots for a given number
        def create_dots(number):
            dots = VGroup()
            for pos in dot_positions[number - 1]:
                dot = Dot(pos * 0.5)
                dots.add(dot)
            return dots

        # Create a die with the number 1
        die_number = 1
        dots = create_dots(die_number)

        # Group the die face and dots together
        die = VGroup(die_face, dots)

        # Add die to the scene
        self.add(die)

        # Animate changing die faces
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
        # Define suits and ranks
        suits = ["♠", "♥", "♦", "♣"]
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        
        # Create a list of all cards
        cards = [f"{rank}{suit}" for suit in suits for rank in ranks]
        
        # Define the grid parameters
        rows = 4
        cols = 13
        card_width = 1
        card_height = 1.5
        spacing = 0.2

        # Create cards
        for i, card in enumerate(cards):
            row = i // cols
            col = i % cols
            pos = LEFT * (cols / 2) + RIGHT * (col * (card_width + spacing)) + UP * (rows / 2) + DOWN * (row * (card_height + spacing))
            
            card_rect = Rectangle(width=card_width, height=card_height, color=WHITE).move_to(pos)
            card_text = Text(card, font_size=24).move_to(pos)
            
            self.add(card_rect)
            self.add(card_text)
        
        # Hold the final frame
        self.wait(2)


    def SetDeveloperList(self):
        self.DeveloperList="SURADHYA REDDY"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Probability.py"

if __name__ == "__main__":
    scene = probability()
    scene.render()