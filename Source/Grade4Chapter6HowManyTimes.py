from manim import *
from AbstractAnim import AbstractAnim
import cvo


class HowManyTimes(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.splitmultiply()
        self.fadeOutCurrentScene()
        self.multiplybig()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()


    def Introduction(self):
        self.setNumberOfCirclePositions(4)
        self.angleChoice = [TAU/4,TAU/4,TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("How Many Times","").setPosition([-5,0,0])
        p13=cvo.CVO().CreateCVO("Multiplication Methods","").setPosition([-1,0,0])
        p11=cvo.CVO().CreateCVO("Split Numbers and Multiply", "").setPosition([3,2,0])
        p12=cvo.CVO().CreateCVO("Multiplying bigger numbers", "").setPosition([3,-2,0])
        p11.setcircleradius(1.5)
        p12.setcircleradius(1.5)
        p10.cvolist.append(p13)
        p13.cvolist.append(p11)
        p13.cvolist.append(p12)
        self.construct1(p10,p10)

    def splitmultiply(self):
          # Title
        title = Text("Split Numbers and Multiply",font_size=39).to_edge(UP)
        
       # self.play(title.to_edge, UP)
        self.wait()
        underline = Line(
            start=title.get_left() + DOWN * 0.3,
            end=title.get_right() + DOWN * 0.3,
            color=YELLOW
        )
        self.play(Write(title))
        self.play(Create(underline))


        intro_text = Text(
            "Splitting a number into smaller numbers and multiplying\n"
            "makes multiplication easier.",
            font_size=30
        ).next_to(title,DOWN,buff=0.8)
        self.play(Write(intro_text))
        self.wait()

        intro_text1 = MathTex(
            "Example: 13 \\times 6 ",
            font_size=35
        ).next_to(intro_text,DOWN,buff=0.3)
        self.play(Write(intro_text1))
        self.wait()



        # Numbers to multiply
        num1 = 13
        num2 = 6

        # Split numbers
        part1 = 10
        part2 = 3

        step1_text = Text("Step 1: Numbers to multiply:", font_size=29).next_to(intro_text1, DOWN,buff=0.5)
        self.play(Write(step1_text))
        self.wait(1)
        # Display numbers
        num1_text = Text(f"{num1}").next_to(step1_text, DOWN)
        num2_text = Text(f"x {num2}").next_to(num1_text, RIGHT)
        self.play(Write(num1_text), Write(num2_text))
        self.wait(1)
        
        step2_text = Text("Step 2: Splitting the number:", font_size=29).next_to(num1_text, DOWN,buff=0.5)
        self.play(Write( step2_text))
        self.wait(1)
        # Split step
        split_text = Text(f"= ({part1} + {part2}) x {num2}").next_to(step2_text, DOWN)
        self.play( Write(split_text))
        self.wait(1)

        self.play( FadeOut(step1_text), FadeOut(num1_text),FadeOut(num2_text),
                  FadeOut(step2_text), FadeOut(split_text),
                   FadeOut(intro_text),FadeOut(intro_text1))

        step3_text = Text("Step 3: Multiply each part:", font_size=29).next_to(title, DOWN,buff=1)
        self.play(Write (step3_text))
        self.wait(1)
        # Show parts
        parts_text = Text(f"= ({part1} x {num2}) + ({part2} x {num2})").next_to(step3_text, DOWN)
        self.play(Write( parts_text))
        self.wait(1)
        

        step4_text = Text("Step 4: Calculate each product", font_size=29).next_to(parts_text, DOWN,buff=0.75)
        self.play(Write( step4_text))
        self.wait(1)
        
        # Calculate each part
        calculation1 = Text(f"= {part1 * num2} + {part2 * num2}").next_to(step4_text, DOWN)
        self.play(Write(calculation1))
        self.wait(1)

        step5_text = Text("Step 5: Sum the results", font_size=29).next_to(calculation1, DOWN,buff=0.75)
        self.play(Write (step5_text))
        self.wait(1)

        # Summing up
        final_result = Text(f"= {part1 * num2 + part2 * num2}").next_to(step5_text, DOWN)
        self.play( Write(final_result))
        self.wait(1)

    def multiplybig(self):
        title = Text("Multiplying Bigger Numbers Using Place Values", font_size=39).to_edge(UP)
        self.wait()
        underline = Line(
            start=title.get_left() + DOWN * 0.3,
            end=title.get_right() + DOWN * 0.3,
            color=YELLOW
        )
        self.play(Write(title))
        self.play(Create(underline))  

        intro_text = Text(
            "Splitting a number into its hundreds, tens, and ones place values, and \n"
            "multiplying each part and adding them  makes multiplication easier.",
            font_size=30
        ).next_to(title, DOWN, buff=1)
        self.play(Write(intro_text))
        self.wait()

        intro_text1 = MathTex(
            "Example: 325 \\times 3 ",
            font_size=35
        ).next_to(intro_text,DOWN,buff=0.5)
        self.play(Write(intro_text1))
        self.wait()

        # Numbers to multiply
        num1 = 325
        num2 = 3

        # Split numbers
        part1 = 300
        part2 = 20
        part3 = 5

        step1_text = Text("Step 1: Numbers to multiply:", font_size=29).next_to(intro_text1, DOWN, buff=0.5)
        self.play(Write(step1_text))
        self.wait(1)
        # Display numbers
        num1_text = Text(f"{num1}", font_size=36).next_to(step1_text, DOWN)
        num2_text = Text(f"x {num2}", font_size=36).next_to(num1_text, RIGHT)
        self.play(Write(num1_text), Write(num2_text))
        self.wait(1)
        
        step2_text = Text("Step 2: Splitting the number:", font_size=29).next_to(num1_text, DOWN, buff=0.5)
        self.play(Write(step2_text))
        self.wait(1)
        # Split step
        split_text = Text(f"= ({part1} + {part2} + {part3}) x {num2}", font_size=36).next_to(step2_text, DOWN)
        self.play(Write(split_text))
        self.wait(1)

        self.play(FadeOut(step1_text), FadeOut(num1_text), FadeOut(num2_text),
                  FadeOut(step2_text), FadeOut(split_text), FadeOut(intro_text),FadeOut(intro_text1))

        step3_text = Text("Step 3: Multiply each part:", font_size=29).next_to(title, DOWN, buff=1)
        self.play(Write(step3_text))
        self.wait(1)
        # Show parts
        parts_text = Text(f"= ({part1} x {num2}) + ({part2} x {num2}) + ({part3} x {num2})", font_size=36).next_to(step3_text, DOWN)
        self.play(Write(parts_text))
        self.wait(1)
        
        step4_text = Text("Step 4: Calculate each product", font_size=29).next_to(parts_text, DOWN, buff=0.8)
        self.play(Write(step4_text))
        self.wait(1)
        
        # Calculate each part
        calculation1 = Text(f"= {part1 * num2} + {part2 * num2} + {part3 * num2}", font_size=36).next_to(step4_text, DOWN)
        self.play(Write(calculation1))
        self.wait(1)

        step5_text = Text("Step 5: Sum the results", font_size=29).next_to(calculation1, DOWN, buff=0.8)
        self.play(Write(step5_text))
        self.wait(1)

        # Summing up
        final_result = Text(f" 325 X 3= {part1 * num2 + part2 * num2 + part3 * num2}", font_size=36).next_to(step5_text, DOWN)
        self.play(Write(final_result))
        self.wait(1)

        # Fade out
        self.play(FadeOut(title), FadeOut(underline), FadeOut(step3_text),
                  FadeOut(parts_text), FadeOut(step4_text), FadeOut(calculation1),
                  FadeOut(step5_text), FadeOut(final_result))



         

    def SetDeveloperList(self):  
        self.DeveloperList="Agraz Gopu"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade4Chapter6HowManyTimes.py"


if __name__ == "__main__":
        scene = HowManyTimes()  
        scene.render()
