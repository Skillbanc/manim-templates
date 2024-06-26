import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class fractionanim(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.Multiplication_of_frac()
        self.reciprocal()
        self.Division_of_frac()
        self.Decimals()
        self.Dec_addandsub()
        self.Dec_mul()
        self.Dec_div()
        self.Rational()
        self.Rat_add()
        self.Rat_sub()
        self.GithubSourceCodeReference()

    def Introduction(self):
        text=Text("Fractions,Decimals and Rational Numbers").scale(0.8)
        self.play(Write(text))
        self.play(FadeOut(text))
        self.angleChoice=[TAU/4,TAU/4]
        p14=cvo.CVO().CreateCVO("Fraction","").setPosition([-3,0,0])
        p10=cvo.CVO().CreateCVO("Representation","p/q").setPosition([0.5,2.5,0])
        p13=cvo.CVO().CreateCVO("conditions","").setPosition([4,0.5,0])
        p13onamelist=["p and q are whole numbers","$q \\neq 0$"]
        p14.cvolist.append(p10)
        p13.extendOname(p13onamelist)
        p14.cvolist.append(p13)
        self.construct1(p14,p14)
        self.fadeOutCurrentScene()
        self.angleChoice=[TAU/4,TAU/4,TAU/4]
        p14=cvo.CVO().CreateCVO("Fraction","").setPosition([-5.5,0,0])
        p15=cvo.CVO().CreateCVO("Types","").setPosition([-3,0,0])
        p11=cvo.CVO().CreateCVO("Proper Fraction","$Numerator<Denominator$").setPosition([3,2,0])
        p12=cvo.CVO().CreateCVO("Improper Fraction","$Numerator>Denominator$").setPosition([3,-2,0])
        p14.cvolist.append(p15)
        p15.cvolist.append(p11)
        p15.cvolist.append(p12)
        self.construct1(p14,p14)
        self.fadeOutCurrentScene()
    
    def Multiplication_of_frac(self):
        self.angleChoice=[TAU/4]
        p10=cvo.CVO().CreateCVO("Multiplication of Fraction","").setPosition([-3,2,0])
        p15=cvo.CVO().CreateCVO("Formula","$\\frac{\\text{product of numerator}}{\\text{product of denominators}}$").setPosition([3,2,0])
        p10.cvolist.append(p15)
        self.construct1(p10,p10)
        example1 = MathTex("Example:(\\frac{3}{2} \\times \\frac{1}{4})", font_size=36).to_edge(LEFT)
        self.play(Write(example1))
        frac= MathTex(r"\frac{3}{2} \times \frac{1}{4}")
        self.play(Write(frac))
        self.wait(1)
    
        result = MathTex(r"= \frac{3 \times 1}{2 \times 4}")
        self.play(Write(result.next_to(frac,RIGHT)))
        self.wait(1)
        
        final_result = MathTex(r"= \frac{3}{8}").next_to(frac,RIGHT)
        self.play(Transform(result, final_result))
        self.wait(2)
        self.fadeOutCurrentScene()

    def reciprocal(self):
        title = Text("Fraction to Reciprocal Conversion").scale(0.8).to_edge(UP)
        self.play(Write(title))
        
        # Headers for Fraction and Reciprocal
        fraction_text = Text("Fraction", font_size=30).to_edge(LEFT).shift(RIGHT*2 + UP*2)
        reciprocal_text = Text("Reciprocal", font_size=30).to_edge(RIGHT).shift(LEFT*2 + UP*2)
        self.play(Write(fraction_text), Write(reciprocal_text))
        
        # Define fractions and their reciprocals
        fractions = [r"\frac{2}{3}", r"\frac{23}{7}", "3"]
        reciprocals = [r"\frac{3}{2}", r"\frac{7}{23}", r"\frac{1}{3}"]
        
        previous_frac = fraction_text
        previous_recip = reciprocal_text
        
        # Loop through the fractions and reciprocals
        for frac, recip in zip(fractions, reciprocals):
            # Create MathTex objects for fractions and reciprocals
            frac_tex = MathTex(frac).scale(0.65).next_to(previous_frac, DOWN, buff=0.8)
            recip_tex = MathTex(recip).scale(0.65).next_to(previous_recip, DOWN, buff=0.8)
            arrow = Arrow(frac_tex.get_right(), recip_tex.get_left())
            
            # Animate the writing and arrow creation
            self.play(Write(frac_tex), Write(recip_tex))
            self.play(Create(arrow))
            
            # Update previous_frac and previous_recip for the next iteration
            previous_frac = frac_tex
            previous_recip = recip_tex

        self.play(FadeOut(title, fraction_text, reciprocal_text, 
                          *self.mobjects))

    def Division_of_frac(self):
        p10=cvo.CVO().CreateCVO("Division","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("whole number by fraction","").setPosition([-3.5,0,0])
        p12=cvo.CVO().CreateCVO("fraction by whole number","").setPosition([0,-2.5,0])
        p13=cvo.CVO().CreateCVO("fraction by fraction","").setPosition([3.5,0,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Division_Examples(self):
        # Title
        self.title = Text("Division").to_edge(UP)
        self.play(Write(self.title))

        # Examples information
        examples = [
            ("Whole number by Fraction", "Example:(5 \div \\frac{3}{2})",
             r"5 \div \frac{3}{2}", r"5 \times \frac{2}{3}",
             r"= \frac{5 \times 2}{3}", r"= \frac{10}{3}"),

            ("Fraction by Whole number", "Example:(\\frac{1}{2} \div 3)",
             r"\frac{1}{2} \div 3", r"\frac{1}{2} \times \frac{1}{3}",
             r"= \frac{1 \times 1}{2 \times 3}", r"= \frac{1}{6}"),

            ("Fraction by Fraction", "Example:(\\frac{4}{5} \div \\frac{3}{2})",
             r"\frac{4}{5} \div \frac{3}{2}", r"\frac{4}{5} \times \frac{2}{3}",
             r"= \frac{4 \times 2}{5 \times 3}", r"= \frac{8}{15}")
        ]

        # Loop through the examples
        for example_info in examples:
            self.show_example(*example_info)
        
        self.play(FadeOut(self.title))
        
    # Helper function to animate the conversion and calculation process
    def show_example(self, intro_text_str, example, example_fraction, multiplication, result, final_result):
        # Introductory text
        intro_text = Text(intro_text_str, font_size=30).next_to(self.title, DOWN, buff=0.75).set_color(YELLOW)
        self.play(Write(intro_text))

        # Display the example
        example_text = MathTex(example, font_size=45).to_edge(LEFT).shift(UP * 1)
        self.play(Write(example_text))
        self.wait(2)
        
        # Conversion text
        conversion_text = "Convert division to multiplication by the reciprocal:"
        conversion_text_obj = Text(conversion_text, font_size=30).next_to(example_text, DOWN, buff=0.75).shift(RIGHT * 3)
        self.play(Write(conversion_text_obj))
        self.wait(1)

        # Display example fraction and transform it to multiplication
        example_frac = MathTex(example_fraction).next_to(conversion_text_obj, DOWN, buff=1).shift(RIGHT * 1)
        multiplication_tex = MathTex(multiplication).next_to(conversion_text_obj, DOWN, buff=1).shift(RIGHT * 1)
        self.play(Write(example_frac))
        self.wait(1)
        self.play(Transform(example_frac, multiplication_tex))
        self.wait(1)
        
        # Display result and final result
        result_tex = MathTex(result).next_to(example_frac, RIGHT)
        final_result_tex = MathTex(final_result).next_to(example_frac, RIGHT)
        self.play(Write(result_tex))
        self.wait(1)
        self.play(Transform(result_tex, final_result_tex))
        self.wait(2)
        
        # Fade out the elements
        self.play(FadeOut(intro_text, example_text, conversion_text_obj, example_frac, result_tex))

    def Decimals(self):
        self.colorChoice=[BLUE,ORANGE,PINK,PURPLE,ORANGE,PINK,PURPLE,]
        self.angleChoice=[TAU/4,TAU/4,TAU/4,TAU/4,TAU/4,TAU/4,TAU/4]
        p16=cvo.CVO().CreateCVO("Decimal number","").setPosition([-5.5,0,0])
        p10=cvo.CVO().CreateCVO("Example","16.95").setPosition([-4,-2,0])
        p11=cvo.CVO().CreateCVO("tens","1*10").setPosition([-3,2,0])
        p12=cvo.CVO().CreateCVO("ones","6*1").setPosition([0.5,2.5,0])
        p13=cvo.CVO().CreateCVO("decimal point",".").setPosition([2.75,2,0])
        p14=cvo.CVO().CreateCVO("tenths","9*1/10").setPosition([4,0.5,0])
        p15=cvo.CVO().CreateCVO("hundredths","5*1/100").setPosition([3,-2,0])
        p16.cvolist.append(p10)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        p10.cvolist.append(p15)
        self.construct1(p16,p16)
        self.fadeOutCurrentScene()

    def Dec_addandsub(self):
        intro_text = Text("Addtion and Subratction of Decimals").to_edge(UP)
        self.play(Write(intro_text))
        example1 = MathTex("Example:", font_size=36).to_edge(LEFT).shift(UP*1,RIGHT*1)
        self.play(Write(example1))
        var1 = MathTex("39.70").shift(UP*1)
        var2 = MathTex("6.45").next_to(var1, DOWN)
        sign = MathTex("+").next_to(var2, LEFT)
        line = Line(var2.get_right(), var2.get_right() + RIGHT * 2).shift(DOWN*0.5,LEFT*1.5)
        line1 = Line(var2.get_right(), var2.get_right() + RIGHT * 2).shift(DOWN*1.5,LEFT*1.5)
        self.play(Write(var1),Write(var2),Write(sign),Write(line),Write(line1))
        res1 = MathTex("46.15").next_to(var2, DOWN*2)
        self.play(Write(res1))
        self.wait(2)
        sign1 = MathTex("-").next_to(var2, LEFT)
        res2 = MathTex("33.25").next_to(var2, DOWN*2)
        self.play(FadeOut(res1))
        self.play(Transform(sign,sign1))
        self.play(FadeIn(res2))
        self.fadeOutCurrentScene()
    
    def Dec_mul(self):
        text2 = Text("Multiplcation",font_size=30).to_edge(UP)
        self.play(Write(text2))
        example = MathTex("Example:1.2*0.5", font_size=36).to_edge(LEFT).shift(UP*1,RIGHT*1)
        self.play(Write(example))
        self.wait(1)
        decimal1 = MathTex(r"1.2=\frac{12}{10}").next_to(example, DOWN).shift(RIGHT*1)
        self.play(Write(decimal1))
        self.wait(1)
        decimal2 = MathTex(r"0.5=\frac{5}{10}").next_to(decimal1, DOWN)
        self.play(Write(decimal2))
        self.wait(1)
        mul = MathTex(r"=\frac{12}{10} \times \frac{5}{10}").next_to(example,RIGHT).shift(RIGHT*2)
        self.play(Write(mul))
        self.wait(1)
        
        result1= MathTex(r"= \frac{60}{100}").next_to(example,RIGHT).shift(RIGHT*2)
        self.play(Transform(mul, result1))
        self.wait(2)

        final_result = MathTex(r"=0.6")
        self.play(Write(final_result.next_to(result1,RIGHT)))
        self.wait(1)       
        self.fadeOutCurrentScene()

    def Dec_div(self):
        text2 = Text("Division",font_size=30).to_edge(UP)
        self.play(Write(text2))
        example = MathTex("Example:1.5 \div 1.2", font_size=36).to_edge(LEFT).shift(UP*1,RIGHT*1)
        self.play(Write(example))
        self.wait(1)
        decimal1 = MathTex(r"1.5=\frac{15}{10}").next_to(example, DOWN).shift(RIGHT*1)
        self.play(Write(decimal1))
        self.wait(1)
        decimal2 = MathTex(r"1.2=\frac{12}{10}").next_to(decimal1, DOWN)
        self.play(Write(decimal2))
        self.wait(1)
        mul = MathTex(r"=\frac{15}{10} \div \frac{12}{10}").next_to(example,RIGHT).shift(RIGHT*2)
        self.play(Write(mul))
        self.wait(1)
        result1 = MathTex(r"= \frac{15 \times 10}{10 \times 12}").next_to(mul,DOWN)
        self.play(Write(result1))
        self.wait(1)
        result2= MathTex(r"= \frac{150}{120}").next_to(result1,DOWN)
        self.play(Transform(result1, result2))
        self.wait(2)
        final_result = MathTex(r"=1.25")
        self.play(Write(final_result.next_to(result2,RIGHT)))
        self.wait(1)       
        self.fadeOutCurrentScene()
    
    def Rational(self):
        self.angleChoice=[-TAU/4,TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Rational number","").setPosition([-2,0,0])
        p12=cvo.CVO().CreateCVO("Representation","p/q").setPosition([-5.5,0,0])
        p13=cvo.CVO().CreateCVO("conditions","").setPosition([2.75,2,0])
        p13onamelist=["p and q are integers","$q \\neq 0$"]
        p11=cvo.CVO().CreateCVO("Examples","").setPosition([3,-1.5,0])
        p11.setcircleradius(1.25)
        p11.onameList=["-7/3","0","1/4","6/1"]
        p13.extendOname(p13onamelist)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()

    def Rat_add(self):
        intro_text = Text("Addition of Rational Numbers", font_size=36).to_edge(UP)
        self.play(Write(intro_text))
        example_text = MathTex("Example: (\\frac{1}{3} + \\frac{2}{5})", font_size=36).shift(UP*2,LEFT*1.5)
        self.play(Write(example_text))
        self.wait(2)
        fraction1 = MathTex(r"\frac{1}{3} + \frac{2}{5}").next_to(example_text,DOWN).shift(RIGHT*1)
        self.play(Write(fraction1))
        self.wait(2)
        step2_text = Text("Step 1: Find LCM of denominators", font_size=30).next_to(fraction1, DOWN).shift(DOWN*1.5)
        self.play(Write(step2_text))
        self.wait(2)
        common_denominator = MathTex(r"\text{LCM: } 15").next_to(step2_text, DOWN)
        self.play(Write(common_denominator))
        self.wait(2)
        converted_fractions = MathTex(r"\frac{1}{3} = \frac{5}{15}, \frac{2}{5} = \frac{6}{15}").shift(UP*0.5,LEFT*1)
        self.play(Transform(fraction1, converted_fractions))
        self.wait(2)
        self.play(FadeOut(step2_text,common_denominator))
        step3_text = Text("Step 2: Add the numerators", font_size=30).next_to(fraction1, DOWN).shift(DOWN*1)
        self.play(Write(step3_text))
        self.wait(2)
        addition = MathTex(r"\frac{5}{15} + \frac{6}{15} = \frac{5 + 6}{15}").shift(UP*0.5)
        self.play(Transform(fraction1, addition))
        self.wait(2)
        result = MathTex(r"= \frac{11}{15}").shift(UP*0.5)
        self.play(Transform(fraction1, result))
        self.wait(2)
        self.fadeOutCurrentScene()

    def Rat_sub(self):
        intro_text = Text("Subtraction of Rational Numbers", font_size=36).to_edge(UP)
        self.play(Write(intro_text))
        example_text = MathTex("Example: (\\frac{2}{3} - \\frac{4}{7})", font_size=36).shift(UP*2,LEFT*1.5)
        self.play(Write(example_text))
        self.wait(2)
        fraction1 = MathTex(r"\frac{2}{3} - \frac{4}{7}").next_to(example_text,DOWN).shift(RIGHT*1)
        self.play(Write(fraction1))
        self.wait(2)
        step2_text = Text("Step 1: Find LCM of denominators", font_size=30).next_to(fraction1, DOWN).shift(DOWN*1.5)
        self.play(Write(step2_text))
        self.wait(2)
        common_denominator = MathTex(r"\text{LCM: } 21").next_to(step2_text, DOWN)
        self.play(Write(common_denominator))
        self.wait(2)
        converted_fractions = MathTex(r"\frac{2}{3} = \frac{6}{21}, \frac{4}{7} = \frac{12}{21}").shift(UP*0.5,LEFT*1)
        self.play(Transform(fraction1, converted_fractions))
        self.wait(2)
        self.play(FadeOut(step2_text,common_denominator))
        step3_text = Text("Step 2: Subtract the numerators", font_size=30).next_to(fraction1, DOWN).shift(DOWN*1)
        self.play(Write(step3_text))
        self.wait(2)
        addition = MathTex(r"\frac{6}{21} - \frac{12}{21} = \frac{6 - 12}{21}").shift(UP*0.5)
        self.play(Transform(fraction1, addition))
        self.wait(2)
        result = MathTex(r"= \frac{-6}{21}").shift(UP*0.5)
        self.play(Transform(fraction1, result))
        self.wait(2)
        self.fadeOutCurrentScene()

    def SetDeveloperList(self):
        self.DeveloperList="Sindhu"
    
    def SetSourceCodeFilename(self):
        self.SourceCodeFilename="fractionanim.py"

              
if __name__ == "__main__":
    scene = fractionanim()
    scene.render()