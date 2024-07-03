import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class ProbabilityAnim(AbstractAnim):

    
    def construct(self):
        self.RenderSkillbancLogo()
        self.Probability()
        self.Equal()
        self.Trial()
        self.Certain()
        self.Formula()
        self.Properties()
        self.Example()
        self.Example1()
        self.RealLife()
        self.GithubSourceCodeReference() 
        #self.fadeOut()
        #self.constructDataByJSON()
        # self.fadeOut()
        
    
    def Probability(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Probability","").setPosition([-6,0,0])
        p11=cvo.CVO().CreateCVO("Random experiment", "").setPosition([-3,0,0]).setangle(-TAU/4)
        p12=cvo.CVO().CreateCVO("Property", "More than one possible outcome").setPosition([3,2.5,0]).setangle(-TAU/4)
        p13=cvo.CVO().CreateCVO("Property", "Possible outcome cannot be predicted").setPosition([4.5,0,0]).setangle(-TAU/4)
        p14=cvo.CVO().CreateCVO("Example","Flipping a coin").setPosition([3,-2.5,0]).setangle(-TAU/4)
        
        
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
        p11.cvolist.append(p14)
        

        p12.setcircleradius(1.5)
        p13.setcircleradius(1.5)

        self.setNumberOfCirclePositions(4)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Equal(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Equally Likely Outcomes","").setPosition([-4,2,0])
        p11=cvo.CVO().CreateCVO("Definition","Having Equal Chances to occur").setPosition([3,2,0]).setangle(-TAU/4)  
        p12=cvo.CVO().CreateCVO("Example","Rolling a Dice").setPosition([-4,-2,0]).setangle(-TAU/4)
        p13=cvo.CVO().CreateCVO("Outcome","Each number has equal chance to occur").setPosition([3,-2,0]).setangle(-TAU/4)

        p10.cvolist.append(p11)
        p12.cvolist.append(p13)

        p11.setcircleradius(1.5)
        p13.setcircleradius(1.5)
        
        self.setNumberOfCirclePositions(4)
        self.construct1(p10,p10)
        self.construct1(p12,p12)
        self.fadeOutCurrentScene()

    def Trial(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Trial and Event","").setPosition([-2,0,0])
        p11=cvo.CVO().CreateCVO("Trial Definition","Performing an Experiment").setPosition([2,1.5,0]).setangle(-TAU/4)
        p12=cvo.CVO().CreateCVO("Event Definition","Outcomes of Experiment").setPosition([2,-1.5,0]).setangle(-TAU/4)
        
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)

        p11.setcircleradius(1.5)
        p12.setcircleradius(1.5)
        
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
    
    def Certain(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Certain Event","").setPosition([-2,2,0])
        p11=cvo.CVO().CreateCVO("Definition","Probability is equal to 1").setPosition([2,2,0]).setangle(-TAU/6)
        p12=cvo.CVO().CreateCVO("Impossible Event","").setPosition([-2,-2,0]).setangle(-TAU/6)
        p13=cvo.CVO().CreateCVO("Definition","Probability is equal to 0").setPosition([2,-2,0]).setangle(-TAU/6)
        
        p10.cvolist.append(p11)
        p12.cvolist.append(p13)
        
        self.setNumberOfCirclePositions(4)

        self.construct1(p10,p10)
        self.construct1(p12,p12)
        self.fadeOutCurrentScene()

    def Formula(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Probability","").setPosition([-2,2,0])
        p11=cvo.CVO().CreateCVO("Formula","Favourable outcomes / Total number of outcomes").setPosition([2,0,0]).setangle(-TAU/4)
 
        p10.cvolist.append(p11)
        

        p11.setcircleradius(1.5)
        
        
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Properties(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Probability","").setPosition([-2,0,0])
        p11=cvo.CVO().CreateCVO("Property","Sum of all probabilities is equal to 1").setPosition([2,1.5,0])
        p12=cvo.CVO().CreateCVO("Property","Probability lies between 0 and 1").setPosition([2,-1.5,0])
        
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)

        p11.setcircleradius(1.5)
        p12.setcircleradius(1.5)
        
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Example(self):
        
        title1 = Text("Probability",font_size=40,color=BLUE).scale(0.7).to_edge(UP)
        self.play(Write(title1))
        self.wait(1)


        title = Text("Example: Probability of Getting 3 on Rolling a Die",font_size=34).next_to(title1, DOWN)
        self.play(Write(title))
        self.wait(1)
        
        sample_space_text = Text("Sample Space, S = {1, 2, 3, 4, 5, 6}",font_size=32,color=GREEN).next_to(title, DOWN)
        self.play(Write(sample_space_text))
        self.wait(1)

        
        total_outcomes_text = Text("Total number of outcomes, n = 6",font_size=32,color=GREEN).next_to(sample_space_text, DOWN)
        self.play(Write(total_outcomes_text))
        self.wait(1)
        
        event_text = Text("Let A be the event of getting 3.",font_size=32,color=GREEN).next_to(total_outcomes_text, DOWN)
        self.play(Write(event_text))
        self.wait(1)
        
        favourable_outcomes_text = Text("Number of favourable outcomes, n(A) = 1",font_size=32,color=GREEN).next_to(event_text, DOWN)
        self.play(Write(favourable_outcomes_text))
        self.wait(1)
        
        event_set_text = Text("i.e. A = {3}",font_size=32,color=GREEN).next_to(favourable_outcomes_text, DOWN)
        self.play(Write(event_set_text))
        self.wait(1)
        
        probability_text = MathTex(r"P(A) = \frac{n(A)}{n} = \frac{1}{6}",font_size=32,color=GREEN).next_to(event_set_text, DOWN)
        self.play(Write(probability_text))
        self.wait(1)
        
        final_probability_text = Text("Hence, P(getting 3 on rolling a die) = 1/6",font_size=32,color=GREEN).next_to(probability_text, DOWN)
        self.play(Write(final_probability_text))
        self.wait(1)
        
        self.wait(2)
        self.fadeOutCurrentScene()

    def Example1(self):

        title = Text("Probability of spinner stopping at particular colors",font_size=40, color=BLUE).to_edge(UP)
        self.play(Write(title))

        spinner = Circle(radius=2)
        spinner.shift(RIGHT * 3)
        self.play(Create(spinner))

        # Create the sectors with clear division lines
        sectors = VGroup()
        colors = [RED, RED, YELLOW, GREEN, GREEN, GREEN, BLUE, BLUE]
        labels = ["Red", "Red", "Yellow", "Green", "Green", "Green", "Blue", "Blue"]
        angle = TAU / len(colors)

        for i, color in enumerate(colors):
            sector = Sector(outer_radius=2, angle=angle, start_angle=i * angle, fill_color=color, fill_opacity=0.6)
            sector.shift(RIGHT * 3)
            sectors.add(sector)

        self.play(Create(sectors),run_time = 0.2)

        # Draw the division lines from the center of the circle
        for i in range(len(colors)):
            line = Line(ORIGIN, np.array([np.cos(i * angle), np.sin(i * angle), 0]) * 2, color=BLACK).shift(RIGHT * 3)
            self.play(Create(line))

        # Add labels to the sectors
        for i, label in enumerate(labels):
            angle_pos = angle * i + angle / 2
            label_position = 2.2 * np.array([np.cos(angle_pos), np.sin(angle_pos), 0]) + np.array([3, 0, 0])
            label_text = Text(label, font_size=24).move_to(label_position)
            self.play(Write(label_text),run_time = 0.2)

        # Answering the questions, positioned side by side to avoid overlap

        # a) More likely to stop (Green - 3 sections)
        green_label = Text("Most Likely : Green (3/8)", font_size=24, color=GREEN).to_edge(LEFT).shift(RIGHT)
        self.play(Write(green_label))

        # b) Less likely to stop (Yellow - 1 section)
        yellow_label = Text("Least Likely : Yellow (1/8)", font_size=24, color=YELLOW).next_to(green_label, DOWN).align_to(green_label, LEFT)
        self.play(Write(yellow_label))

        # c) Equally likely to stop (Red and Blue - 2 sections each)
        equal_label = Text("Equally likely: Red and Blue (2/8 each)", font_size=24, color=PURPLE).next_to(yellow_label, DOWN).align_to(yellow_label, LEFT)
        self.play(Write(equal_label))


        self.fadeOutCurrentScene()

    def RealLife(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Probability","").setPosition([-2,0,0])
        p11=cvo.CVO().CreateCVO("Real Life Uses","Exit Poll in Elections").setPosition([2,0,0]).setangle(-TAU/4)
        

        p10.cvolist.append(p11)
        
        

        p11.setcircleradius(1.5)
        
        
        
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade10Chapter14Probability.py"

    def SetDeveloperList(self):  
        self.DeveloperList="Lagichetty Kushal"
    
if __name__ == "__main__":
    scene = ProbabilityAnim()
    scene.render()