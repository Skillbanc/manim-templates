from manim import *
from AbstractAnim import AbstractAnim
import cvo


class Ratiosanim(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.ratio()
        self.fadeOutCurrentScene()
        self.proportion()
        self.fadeOutCurrentScene()
        self.law()
        self.fadeOutCurrentScene()
        self.percentage()
        self.fadeOutCurrentScene()
        self.example1()
        self.fadeOutCurrentScene()
        self.profit()
        self.fadeOutCurrentScene()
        self.example2()
        self.fadeOutCurrentScene()
        self.loss()
        self.fadeOutCurrentScene()
        self.example3()
        self.fadeOutCurrentScene()
        self.discount()
        self.fadeOutCurrentScene()
        self.example4()
        self.fadeOutCurrentScene()
        self.Simpleinterest()
        self.fadeOutCurrentScene()
        self.Simpleinterest1()
        self.fadeOutCurrentScene()
        self.example5()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

    def Introduction(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("RATIOS","")
        p11=cvo.CVO().CreateCVO("APPLICATIONS", "")
        p11.extendOname(["Proportions","Percentage","Profit and Loss","Discount","Simple Interest"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def ratio(self):
        self.setNumberOfCirclePositions(5)
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("RATIO","").setPosition([-5,0,0])
        p11=cvo.CVO().CreateCVO("Notation","a:b").setPosition([-2,0,0])
        p12=cvo.CVO().CreateCVO("Antecedent (a)","2").setPosition([2,2,0])
        p13=cvo.CVO().CreateCVO("Consequent (b)","3").setPosition([2,-2,0])
        p14=cvo.CVO().CreateCVO("Representation","2:3").setPosition([5,0,0])
       
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p11.cvolist.append(p13)
        p11.setcircleradius(1.5)
        p14.setcircleradius(1.5)
       
        self.construct1(p10,p10)
        self.construct1(p14,p14)
        self.play(Create(CurvedArrow(p12.pos,p14.pos)),Create(CurvedArrow(p13.pos,p14.pos)))


    def proportion(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("PROPORTION","")
        p11=cvo.CVO().CreateCVO("NOTATION","a:b::c:d")
        # p12=cvo.CVO().CreateCVO("LAW OF PROPORTION", "")
        # p12.extendOname(["Product of means","product of extremes"])
        #p12.setcircleradius(1.5)
        p10.cvolist.append(p11)
        
        self.construct1(p10,p10)

    def law(self):

        title = Text("Law of Proportion").scale(0.75).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        
        # Introducing proportion text
        proportion_text = Tex("If two ratios a:b and c:d are in proportion").scale(0.9).next_to(title,DOWN, buff=0.8)
        self.play(Write(proportion_text))
        self.wait(1)

        # Combining the ratios into a proportion equation
        proportion = MathTex(r"a : b :: c : d")
        proportion.scale(1.5).move_to(ORIGIN)

        #self.play(*[FadeOut(mob) for mob in self.mobjects if mob != title])
        self.play(Write(proportion))
        self.wait(1)

        # Get coordinates for b and c for means curved arrow
        b_coord = proportion[0][2].get_center()
        c_coord = proportion[0][5].get_center()

        # Get coordinates for a and d for extremes curved arrow
        a_coord = proportion[0][0].get_center()
        d_coord = proportion[0][7].get_center()

        # Create curved arrows for means (bc)
        arrow_means = CurvedArrow(
            start_point=b_coord + UP * 0.5,
            end_point=c_coord + UP * 0.5,
            color=YELLOW,
            angle=-PI
        )
        means_text = Text("Means", color=YELLOW).scale(0.5).next_to(arrow_means, UP, buff=0.1)

        # Create curved arrows for extremes (ad)
        arrow_extremes = CurvedArrow(
            start_point=a_coord + DOWN * 0.5,
            end_point=d_coord + DOWN * 0.5,
            color=YELLOW
        )
        extremes_text = Text("Extremes", color=YELLOW).scale(0.5).next_to(arrow_extremes, DOWN, buff=0.1)

        # Draw arrows and labels for means
        self.play(Create(arrow_means), Write(means_text))
        self.wait(1)

        # Draw arrows and labels for extremes
        self.play(Create(arrow_extremes), Write(extremes_text))
        self.wait(1)

        self.play(*[FadeOut(mob) for mob in self.mobjects if mob != title])
   
        conclusion = Tex(
            "Then , their the product of the means is equal to their product of the extremes."
        ).scale(0.8).move_to(ORIGIN + UP * 0.5)
        self.play(Write(conclusion))
        self.wait(2)

        # Cross multiplication explanation
        cross_multiplication = MathTex(r"b \cdot c = a \cdot d")
        cross_multiplication.scale(1.5).next_to(conclusion,DOWN)
        self.play(Write(cross_multiplication))
        self.wait(1)

        # Clean up
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1)
   

       
        
   
    def percentage(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [TAU/4]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("PERCENTAGE","")
        p11=cvo.CVO().CreateCVO("FORMULA","(Part/Whole)*100")
        #p12=cvo.CVO().CreateCVO("EXAMPLE"," 73 Marks in math = 73\%")
        #p12.SetIsMathText(True)
    
       
        p10.cvolist.append(p11)
        #p10.cvolist.append(p12)
        
        self.construct1(p10,p10)
        
        #self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))

    def example1(self):
         # # Title
        # title = Text("Finding Percentage", font_size=48)
        # title.to_edge(UP)
        # self.play(Write(title))
        
        # Example text
        example_text = Text("What percentage is 30 of 150?", font_size=36)
        #example_text.next_to(title, DOWN, buff=1)
        example_text.to_edge(UP)
        self.play(Write(example_text))

        # Formula introduction
        formula_intro = Text("Formula:", font_size=34)
        formula_intro.next_to(example_text, DOWN+LEFT, buff=1)
        self.play(Write(formula_intro))

        # Formula
        formula = MathTex(r"\text{Percentage} = \left( \frac{\text{Part}}{\text{Whole}} \right) \times 100")
        formula.next_to(formula_intro,RIGHT, buff=0.5)
        self.play(Write(formula))

        # Applying the formula to the example
        example_calculation = MathTex(r"\text{Percentage} = \left( \frac{30}{150} \right) \times 100 = 20\%")
        example_calculation.next_to(formula, DOWN, buff=1)
        self.play(Write(example_calculation))

        # Final answer
        final_answer = Text("So, 30 is 20% of 150.", font_size=36)
        final_answer.next_to(example_calculation, DOWN, buff=1)
        self.play(Write(final_answer))

        # Pause to show the final result
        self.wait(2)




    def profit(self):
        self.setNumberOfCirclePositions(3)
        self.angleChoice = [TAU/4,TAU/4]
        #self.angleChoice = [0,0,0]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("PROFIT","")
        p11=cvo.CVO().CreateCVO("FORMULA","S.P-C.P")
    
        #p12=cvo.CVO().CreateCVO("EXAMPLE ","50-40=10")
        p13=cvo.CVO().CreateCVO("Profit\%","(P/C.P)*100")
        p13.SetIsMathText(True)
        p10.cvolist.append(p11)
        #p10.cvolist.append(p12)
        p11.cvolist.append(p13)
       
        self.construct1(p10,p10)
        #self.play(Create(CurvedArrow(p10.pos,p11.pos)),Create(CurvedArrow(p11.pos,p12.pos)))

    def example2(self):
                # Title with example
        title = Text("Example: Cost Price $50, Selling Price $70", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Formula introduction
        formula_intro = Text("Formulas:", font_size=28)
        formula_intro.next_to(title, DOWN, buff=1)
        self.play(Write(formula_intro))

        # Profit formula
        profit_formula = MathTex(r"\text{Profit} = \text{Selling Price} - \text{Cost Price}")
        profit_formula.next_to(formula_intro, DOWN, buff=0.5)
        self.play(Write(profit_formula))

        # Profit Percentage formula
        profit_percent_formula = MathTex(r"\text{Profit \%} = \left( \frac{\text{Profit}}{\text{Cost Price}} \right) \times 100")
        profit_percent_formula.next_to(profit_formula, DOWN, buff=0.5)
        self.play(Write(profit_percent_formula))

        # Fade out the screen except the title
        self.play(FadeOut(formula_intro, profit_formula, profit_percent_formula))

        # Applying the formulas to the example
        example_calculation = MathTex(
            r"\text{Profit} = 70 - 50 = 20",
            r"\text{Profit \%} = \left( \frac{20}{50} \right) \times 100 = 40\%"
        )
        example_calculation.arrange(DOWN, buff=0.5)
        example_calculation.next_to(title, DOWN, buff=1)
        self.play(Write(example_calculation))

        # Final answer
        final_answer = Text("So, the profit is $20 and the profit percentage is 40%.", font_size=36)
        final_answer.next_to(example_calculation, DOWN, buff=1)
        self.play(Write(final_answer))

        # Pause to show the final result
        self.wait(2)


    def loss(self):
        self.setNumberOfCirclePositions(3)
        self.angleChoice = [TAU/4,TAU/4]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Loss","")
        p11=cvo.CVO().CreateCVO("FORMULA","C.P-S.P")
        #p12=cvo.CVO().CreateCVO("example ","60-50=10")
        p13=cvo.CVO().CreateCVO("Loss\%","(L/C.P)*100")
        
    
        p13.SetIsMathText(True)
       
        p10.cvolist.append(p11)
        #p10.cvolist.append(p12)
        p11.cvolist.append(p13)
       
        self.construct1(p10,p10)
        #self.play(Create(CurvedArrow(p10.pos,p11.pos)),Create(CurvedArrow(p11.pos,p12.pos)))

    def example3(self):
        # Title with example
        title = Text("Example: Cost Price $150, Selling Price $120", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
       
        # Formula introduction
        formula_intro = Text("Formulas:", font_size=28)
        formula_intro.next_to(title, DOWN, buff=1)
        self.play(Write(formula_intro))

        # Loss formula
        loss_formula = MathTex(r"\text{Loss} = \text{Cost Price} - \text{Selling Price}")
        loss_formula.next_to(formula_intro, DOWN, buff=0.5)
        self.play(Write(loss_formula))

        # Loss Percentage formula
        loss_percent_formula = MathTex(r"\text{Loss \%} = \left( \frac{\text{Loss}}{\text{Cost Price}} \right) \times 100")
        loss_percent_formula.next_to(loss_formula, DOWN, buff=0.5)
        self.play(Write(loss_percent_formula))

        # Fade out the screen
        self.play(FadeOut(formula_intro, loss_formula, loss_percent_formula))

        # Applying the formulas to the example
        example_calculation = MathTex(
            r"\text{Loss} = 150 - 120 = 30",
            r"\text{Loss \%} = \left( \frac{30}{150} \right) \times 100 = 20\%"
        )
        example_calculation.arrange(DOWN, buff=0.5)
        example_calculation.next_to(title, DOWN, buff=1)
        self.play(Write(example_calculation))

        # Final answer
        final_answer = Text("So, the loss is $30 and the loss percentage is 20%.", font_size=36)
        final_answer.next_to(example_calculation, DOWN, buff=1)
        self.play(Write(final_answer))

        # Pause to show the final result
        self.wait(2)


        

    def discount(self):
        self.setNumberOfCirclePositions(3)
        self.angleChoice = [TAU/4,TAU/4]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Discount","")
        p11=cvo.CVO().CreateCVO("Formula","M.P-S.P")
        #p12=cvo.CVO().CreateCVO(" Example ","100-60")
        p13=cvo.CVO().CreateCVO("Discount\%","(D/MP)*100")
        p13.SetIsMathText(True)
        p10.cvolist.append(p11)
        #p10.cvolist.append(p12)
        p11.cvolist.append(p13)
       
        self.construct1(p10,p10)

    def example4(self):
        title = Text("Example: Original Price $100, Discounted Price $80", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
       
        
        # Formula introduction
        formula_intro = Text("Formulas:", font_size=28)
        formula_intro.next_to(title, DOWN, buff=1)
        self.play(Write(formula_intro))

        # Discount formula
        discount_formula = MathTex(r"\text{Discount} = \text{Market Price} - \text{ SellingPrice}")
        discount_formula.next_to(formula_intro, DOWN, buff=0.5)
        self.play(Write(discount_formula))

        # Discount Percentage formula
        discount_percent_formula = MathTex(r"\text{Discount \%} = \left( \frac{\text{Discount}}{\text{Market Price}} \right) \times 100")
        discount_percent_formula.next_to(discount_formula, DOWN, buff=0.5)
        self.play(Write(discount_percent_formula))

        # Fade out the screen
        self.play(FadeOut(formula_intro, discount_formula, discount_percent_formula))

        # Applying the formulas to the example
        example_calculation = MathTex(
            r"\text{Discount} = 100 - 80 = 20",
            r"\text{Discount \%} = \left( \frac{20}{100} \right) \times 100 = 20\%"
        )
        example_calculation.arrange(DOWN, buff=0.5)
        example_calculation.next_to(title, DOWN, buff=1)
        self.play(Write(example_calculation))

        # Final answer
        final_answer = Text("So, the discount is $20 and the discount percentage is 20%.", font_size=36)
        final_answer.next_to(example_calculation, DOWN, buff=1)
        self.play(Write(final_answer))

        # Pause to show the final result
        self.wait(2)

        
       
    def Simpleinterest(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [TAU/4]
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Simple Interest","")
        p11=cvo.CVO().CreateCVO("FORMULA ","P*T*R")
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        
        self.construct1(p10,p10)

    def Simpleinterest1(self):
        self.setNumberOfCirclePositions(4)
        self.angleChoice = [TAU/4,TAU/4,TAU/4]
        self.isRandom = False

       
        p10=cvo.CVO().CreateCVO("FORMULA ","P*T*R")
        p11=cvo.CVO().CreateCVO(" Principle ","P")
        p12=cvo.CVO().CreateCVO("Interest","R\%")
        p13=cvo.CVO().CreateCVO("Time", "T")
        p12.SetIsMathText(True)
        p10.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        
        self.construct1(p10,p10)

    def example5(self):
        title = Text("Example: Principle = $1000, Time = 2 years, Rate = 5%", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        
        # Formula introduction
        formula_intro = Text("Formula:", font_size=28)
        formula_intro.next_to(title, DOWN, buff=1)
        self.play(Write(formula_intro))

        # Simple Interest formula
        interest_formula = MathTex(r"\text{Simple Interest} = P \times T \times R")
        interest_formula.next_to(formula_intro, DOWN, buff=0.5)
        self.play(Write(interest_formula))

        # Fade out the screen
        self.play(FadeOut(formula_intro, interest_formula))

        # Applying the formula to the example
        example_calculation = MathTex(
            r"\text{Simple Interest} = 1000 \times 2 \times \frac{5}{100} = 100"
        )
        example_calculation.next_to(title, DOWN, buff=1)
        self.play(Write(example_calculation))

        # Final answer
        final_answer = Text("So, the simple interest is $100.", font_size=36)
        final_answer.next_to(example_calculation, DOWN, buff=1)
        self.play(Write(final_answer))

        # Pause to show the final result
        self.wait(2)
    def SetDeveloperList(self):  
        self.DeveloperList="Agraz Gopu"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade7Chapter6Ratiosanim.py"

        
if __name__ == "__main__":
     scene = Ratiosanim()
     scene.render()