# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla
# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla
import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
from manim import MarkupText
import cvo

config.max_files_cached = 800  # Change this number to your desired value

class Grade5Chapter17TripToGolkonda(AbstractAnim):
    
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.heading()
        self.fadeOutCurrentScene()
        self.introduction()
        self.fadeOutCurrentScene()
        self.intro1()
        self.fadeOutCurrentScene()
        self.intro2()
        self.fadeOutCurrentScene()
        self.daytrip()
        self.fadeOutCurrentScene()
        self.intro3()
        self.fadeOutCurrentScene()
        self.intro4()
        self.fadeOutCurrentScene()
        self.intro5()
        self.fadeOutCurrentScene()
        self.intro6()
        self.fadeOutCurrentScene()
        self.intro7()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
    
    def SetDeveloperList(self):
        self.DeveloperList="Vasudha"
        
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade5Chapter17TripToGolkondaFort"
        
    def heading(self):
        title = Text("Trip to the Golkonda Fort", font_size=48, color=PINK)
        
        # Animate the title text
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.to_edge(UP))
        
    def introduction(self):
        # Define text for the introduction
        intro_text = Text("The teachers of Gummadidala Primary School are\nplanning to take the children of\n"
                          "class 4 and 5 to Golkonda Fort.\nThe head teacher is estimating the expenditure for\n"
                          "the trip.").scale(0.6)
        
        # Define text for each expectation
        text1 = Text("The Golkonda Fort is about 56 km from our school.\n"
                     "The bus agency will charge ₹ 24 per km").scale(0.6)
        text2 = Text("61 students and 3 teachers will go for the trip.\n"
                     "The entry ticket at the Fort (including the sound and light show) is ₹ 40.").scale(0.6)
        text3 = Text("Rupees 20 per person on the snacks and food").scale(0.6)
        
        # # Position texts off-screen above the visible area
        # intro_text.move_to(UP * 3)
        # text1.move_to(UP * 3)
        # text2.move_to(UP * 3)
        # text3.move_to(UP * 3)
        
        # Animate texts to slide up to the center, then move up and out of the visible area
        self.play(intro_text.animate.move_to(ORIGIN), run_time=2)
        self.wait(2)
        self.play(AnimationGroup(intro_text.animate.move_to(UP * 6), text1.animate.move_to(ORIGIN), run_time=2)) # Move intro_text up and bring text1 to the center
        
        self.wait(2)
        self.play(AnimationGroup(text1.animate.move_to(UP * 6), text2.animate.move_to(ORIGIN), run_time=2)) # Move text1 up and bring text2 to the center
        
        self.wait(2)
        self.play(AnimationGroup(text2.animate.move_to(UP * 6), text3.animate.move_to(ORIGIN), run_time=2)) # Move text2 up and bring text3 to the center
        
        self.wait(2)
        self.play(text3.animate.move_to(UP * 6), run_time=2) # Move text3 up and out
        self.wait(2)
    
    def intro1(self):
        # Define heading for the amount to be paid to the bus agency
        heading = MarkupText("Q1:Amount to be paid to the bus agency", font_size=20, color=BLUE)
        heading.to_edge(UP + LEFT)
        self.play(FadeIn(heading))
        self.isRandom = False
        self.angleChoice = [TAU/2,TAU/4]
        p10=cvo.CVO().CreateCVO("distance ","56km(one way) x 2\n= 112km").setPosition([-4.5,-2,0])
        p11=cvo.CVO().CreateCVO("cost per km","24 INR").setPosition([-2.2,-2,0])
        p12=cvo.CVO().CreateCVO("Total bus cost","112km x 24INR/km\n= 2688INR").setPosition([-4.5,1,0]).setangle(-TAU/4)
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        
        self.construct1(p10,p10)
        
        # Define heading for the amount to be paid to the bus agency
        heading1 = MarkupText("Q2:Money required for the tickets at Golkonda Fort", font_size=20, color=BLUE)
        heading1.to_edge(UP + RIGHT)
        self.play(FadeIn(heading1))
        self.isRandom = False
        self.angleChoice = [-TAU/2,-TAU/4]
        p10=cvo.CVO().CreateCVO("total people ","61 students+\n3 students\n= 64").setPosition([4.6,-2,0])
        p11=cvo.CVO().CreateCVO("ticket cost per person","40 INR").setPosition([1.5,-2,0])
        p12=cvo.CVO().CreateCVO("Total ticket cost","64 people x 40 INR/person\n= 2560 INR").setPosition([3,1,0]).setangle(-TAU/4)
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        
        
        self.construct1(p10,p10)
        
    def intro2(self):    
        heading = Text("cont(Q1 and Q2)..so cost per head will be", font_size=22, color=BLUE)
        heading.to_edge(UP + LEFT)
        self.play(FadeIn(heading))
        self.isRandom = False
        self.angleChoice = [TAU/4,TAU/4,TAU/4,-TAU/2,-TAU/2]
        p10=cvo.CVO().CreateCVO("travel cost per person","2688 INR / 64 people\n=42 INR ").setPosition([-4,0,0])
        p11=cvo.CVO().CreateCVO("(1)travel cost","42 INR").setPosition([3.5,-2.5,0])
        p12=cvo.CVO().CreateCVO("(2) ticket cost","40 INR").setPosition([3.5,0,0])
        p13=cvo.CVO().CreateCVO("(3) additional cost","110 INR").setPosition([3.5,2.5,0])
        p14=cvo.CVO().CreateCVO("Total cost per person","40 + 42= 102 INR ").setPosition([0,0,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        # p11.cvolist.append(p14)
        # p12.cvolist.append(p14)
        
        self.construct1(p10,p10)
        self.construct1(p14,p14)
        self.play(Create(CurvedArrow(p11.pos,p14.pos)),Create(CurvedArrow(p12.pos,p14.pos)))
        
        
    def daytrip(self):
        # Title
        title = Text("Questions", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        def display_question_answer(question_text, answer_text, fade_out=True):
            # Question and answer box
            qa_box = Rectangle(width=7, height=4, color=YELLOW)
            qa_box.move_to(ORIGIN)

            # Question
            question = Text(question_text, font_size=18)
            question.move_to(qa_box.get_top() + DOWN * 0.5)

            # Answer
            answer = Text(answer_text, font_size=18)
            answer.next_to(question, DOWN, buff=0.5)

            # Fade in box, question, and answer
            self.play(Create(qa_box), Write(question))
            self.wait(1)
            
            self.play(Write(answer))  # Corrected line
            self.wait(1)
            
            if fade_out:
                # Fade out question and answer after waiting for some time
                self.wait(2)
                self.play(FadeOut(question), FadeOut(answer))

        # Display question and answer (a)
        display_question_answer(
            "(a) If the bus travels 5 km with one liter of diesel\nthen how much diesel is required for the trip?",
            "Total distance: 112 km (round trip)\n\nDiesel required: 112 km / 5 km per liter = 22.4 liters"
        )

        # Display question and answer (b)
        display_question_answer(
            "(b) If 1 liter of diesel costs ₹ 54 then how much will\nthe bus driver has to pay at the petrol pump?",
            "Total cost: 22.4 liters x 54 INR/liter = 1209.6 INR"
        )

        # Question (c) - no fading out
        # Question and answer box
        qa_box_c = Rectangle(width=7, height=4, color=YELLOW)
        qa_box_c.move_to(ORIGIN)

        # Question
        question_c_text = "(c) Represent the following on the timeline given below."
        question_c = Text(question_c_text, font_size=18)
        question_c.move_to(qa_box_c.get_top() + DOWN * 0.5)

        # Answer
        answer_c_text = "(i) The year in which the mud fort was made.\n(ii) The century in which the fort was made longer and stronger.\n(iii) The current year.\n(iv) The year in which your father was born."
        answer_c = Text(answer_c_text, font_size=18)
        answer_c.next_to(question_c, DOWN, buff=0.5)

        # Fade in box, question, and answer
        self.play(Create(qa_box_c), Write(question_c))
        self.wait(1)
        
        self.play(Write(answer_c))  # Corrected line
        self.wait(1)
        
         # Custom number line
        timeline = NumberLine(x_range=[1100, 2100, 100], length=10, color=WHITE)
        timeline.move_to(DOWN * 3)
        self.play(Create(timeline))
        
        years_heading = Text("Years", font_size=24)
        years_heading.next_to(timeline, UP + LEFT)
        self.play(Write(years_heading))

        # Add labels for each tick mark on the number line with slight offset downwards
        for number in range(1100, 2101, 100):
            label_text = Text(f"{number}", font_size=14)
            label_text.next_to(timeline.n2p(number), DOWN * 0.5)  # Adjusted offset downwards
            self.play(Write(label_text))

        # Annotations on the timeline
        annotations = {
            "Mud fort built": (1400, DOWN),
            "Century of fort expansion": (1600, UP),
            "Current year": (2024, DOWN),
            "Father's birth year": (1960, UP)
        }

        # Add annotations with markers
        for label, (year, direction) in annotations.items():
            label_text = Text(f"{label} ({year})", font_size=12)
            label_text.next_to(timeline.n2p(year), direction)
            year_marker = Dot(color=RED).move_to(timeline.n2p(year))
            self.play(Create(year_marker), Write(label_text))
            self.wait(0.5)
            
        self.wait(2)


    def intro3(self):
        # Define heading for the amount to be paid to the bus agency
        heading = Text("Places in Golkonda Fort", font_size=24, color=BLUE)
        heading.to_edge(UP + ORIGIN)
        self.play(FadeIn(heading))
        
        # Create points of interest
        p10 = cvo.CVO().CreateCVO("Golkonda Fort", "").setPosition([0, 2, 0])
        p11 = cvo.CVO().CreateCVO("Fateh Darwaza", "").setPosition([-3, 0, 0])
        p12 = cvo.CVO().CreateCVO("Mosque", "").setPosition([3, 0, 0])
        p13 = cvo.CVO().CreateCVO("Bala Hisar gate", "").setPosition([3, -3, 0])
        p14 = cvo.CVO().CreateCVO("Balahisar Pavilion", "").setPosition([0, -3, 0])
        p15 = cvo.CVO().CreateCVO("Nagina Bagh", "").setPosition([0, 0, 0])
        
        # Link points of interest
        p10.cvolist.extend([p11, p12, p13, p14, p15])
        
        # Call your custom construct1 method to handle the animation
        self.construct1(p10, p10)
        
    def intro4(self):
        # Define heading for the amount to be paid to the bus agency
        heading = MarkupText("Q3:If a square shaped patch has a 2m side then,\nwhat is its perimeter?", font_size=20, color=BLUE)
        heading.to_edge(UP + LEFT)
        self.play(FadeIn(heading))
        self.isRandom = False
        self.angleChoice = [TAU/2,TAU/4]
        p10=cvo.CVO().CreateCVO("formula ","4 x s").setPosition([-4.5,-2,0])
        p11=cvo.CVO().CreateCVO("side (s)","2m").setPosition([-2.2,-2,0])
        p12 = cvo.CVO().CreateCVO("perimeter", "4 x 2m = 8m").setPosition([-3.5, 1, 0])  # Adjusted position to have 3 components
        print("p12 position:", p12.pos)  # Add this line
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        
        self.construct1(p10,p10)
        
        # Define heading for the amount to be paid to the bus agency
        heading1 = MarkupText("Q4:If this patch is lined with bricks of length 25 cm each,\nthen how many such bricks are needed to line the patch?", font_size=20, color=BLUE)
        heading1.to_edge(UP + RIGHT)
        self.play(FadeIn(heading1))
        
        self.isRandom = False
        self.angleChoice = [-TAU/2]
        p10=cvo.CVO().CreateCVO("length of patch perimeter ","4 x 2m = 8m").setPosition([4.6,1,0])
        p11=cvo.CVO().CreateCVO("no.of bricks","8m/0.25m=32").setPosition([1.5,1,0])
        p10.cvolist.append(p11)
        
        self.construct1(p10,p10)
        
    def intro5(self):
         # Define heading for the amount to be paid to the bus agency
        heading = MarkupText("Q5:If there are 13 such patches\nthen how many bricks are needed?", font_size=20, color=BLUE)
        heading.to_edge(UP + LEFT)
        self.play(FadeIn(heading))
        self.isRandom = False
        self.angleChoice = [-TAU/2]
        p10=cvo.CVO().CreateCVO("no.of bricks ","32").setPosition([-4.5,1,0])
        p11=cvo.CVO().CreateCVO("total no.of bricks","13 x 32 = 416").setPosition([-4.5,-2,0])
        p10.cvolist.append(p11)
        
        self.construct1(p10,p10)
        
        # Define heading for the amount to be paid to the bus agency
        heading1 = MarkupText("Q6:If the rectangular shaped patch is 3 m long\nand 1m 50 cm wide then,\nwhat is its perimeter?", font_size=20, color=BLUE)
        heading1.to_edge(UP + RIGHT)
        self.play(FadeIn(heading1))
        self.isRandom = False
        self.angleChoice = [-TAU/2,-TAU/4]
        p10=cvo.CVO().CreateCVO("formula","2(l+b)").setPosition([4.6,-2,0])
        p11=cvo.CVO().CreateCVO("l,b","3,1.5").setPosition([1.5,-2,0])
        p12=cvo.CVO().CreateCVO("perimeter","2(3+1.5)=9m").setPosition([4,1,0])
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
      
        
        self.construct1(p10,p10)
    
    def intro6(self):
          # Define heading for the amount to be paid to the bus agency
        heading = MarkupText("Q7:If this patch is lined with bricks of length 25 cm,\nthen how many such bricks are\nneeded to line the patch?", font_size=20, color=BLUE)
        heading.to_edge(UP + LEFT)
        self.play(FadeIn(heading))
        self.isRandom = False
        self.angleChoice = [-TAU/2,-TAU/2,-TAU/4]
        p10=cvo.CVO().CreateCVO("formula","2(l+b)").setPosition([-4.5,1,0])
        p11=cvo.CVO().CreateCVO("l,b","3,1.5").setPosition([-2.2,1,0])
        p12=cvo.CVO().CreateCVO("perimeter","2(3+1.5)=9m").setPosition([-2.2,-2,0])
        p13=cvo.CVO().CreateCVO("no.of bricks","9m/0.25m=36").setPosition([-4.5,-2,0])
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        
        self.construct1(p10,p10)
        
        # Define heading for the amount to be paid to the bus agency
        heading1 = MarkupText("Q8:If there are 19 such patches\nthen how many bricks are needed?", font_size=20, color=BLUE)
        heading1.to_edge(UP + RIGHT)
        self.play(FadeIn(heading1))
        self.isRandom = False
        self.angleChoice = [-TAU/2]
        p10=cvo.CVO().CreateCVO("no.of bricks","36").setPosition([4,1,0])
        p11=cvo.CVO().CreateCVO("total number of bricks","19 x 36= 684").setPosition([4,-2,0])
        p10.cvolist.append(p11)
        
        self.construct1(p10,p10)
        
    
    def intro7(self):
         # Define heading for the amount to be paid to the bus agency
        heading = MarkupText("Q9:Estimate the perimeter of your school boundary.\nAbout how many times more is the perimeter of the fort?", font_size=20, color=BLUE)
        heading.to_edge(UP)
        self.play(FadeIn(heading))
        self.isRandom = False
        self.angleChoice = [-TAU/2]
        p10=cvo.CVO().CreateCVO("school boundary","l=100,b=100").setPosition([-4.5,1,0])
        p11=cvo.CVO().CreateCVO("perimeter","2(100+100)=400").setPosition([-4.5,-2,0])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        
        self.construct1(p10,p10)
        
        self.isRandom = False
        self.angleChoice = [-TAU/2]
        p12=cvo.CVO().CreateCVO("fort boundary ","l=3000,b=2000").setPosition([4.6,1,0])
        p13=cvo.CVO().CreateCVO("perimeter","2(3000+2000)=10000").setPosition([4.6,-2,0])
        p13.setcircleradius(1.5)
        p12.cvolist.append(p13)
        
        self.construct1(p12,p12)      
        
        p14=cvo.CVO().CreateCVO("times more ","fort perimeter/school perimeter=25 times").setPosition([0,0,0])
        
        self.construct1(p14,p14) 
        
        self.play(Create(CurvedArrow(p11.pos,p14.pos)),Create(CurvedArrow(p13.pos,p14.pos)))
        
if __name__ == "__main__":
    scene = Grade5Chapter17TripToGolkonda()
    scene.render()