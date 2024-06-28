import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class fractionanim(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.TypesofFraction()
        self.fadeOutCurrentScene()
        self.Multiplication_of_frac()
        self.fadeOutCurrentScene()
        self.Reciprocal()
        self.fadeOutCurrentScene()
        self.Division_of_frac()
        self.fadeOutCurrentScene()
        self.Division_Examples()
        self.fadeOutCurrentScene()
        self.Decimals()
        self.fadeOutCurrentScene()
        self.ExpandedForm()
        self.fadeOutCurrentScene()
        self.Dec_addandsub()
        self.fadeOutCurrentScene()
        self.Dec_mul()
        self.fadeOutCurrentScene()
        self.Dec_div()
        self.fadeOutCurrentScene()
        self.Rational()
        self.fadeOutCurrentScene()
        self.EquivalentRationalNumbers()
        self.fadeOutCurrentScene()
        self.Rat_addsub()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

    def Introduction(self):
        text=Text("Fractions,Decimals and Rational Numbers").scale(0.8)
        self.play(Write(text))
        self.play(FadeOut(text))
        self.angleChoice=[TAU/4,TAU/4]
        p14=cvo.CVO().CreateCVO("Fraction","").setPosition([-3,0,0])
        p10=cvo.CVO().CreateCVO("Representation","p/q").setPosition([0.5,2.5,0])
        p13=cvo.CVO().CreateCVO("conditions","").setPosition([0.5,-2.5,0])
        p13onamelist=["p and q are whole numbers","$q \\neq 0$"]
        p14.cvolist.append(p10)
        p13.extendOname(p13onamelist)
        p14.cvolist.append(p13)
        self.construct1(p14,p14)
        self.fadeOutCurrentScene()
        # Create and display the first square with 1/2 shaded
        square1 = Square(side_length=2).shift(LEFT * 3 + UP * 1)
        shaded_half = Polygon(
            square1.get_corner(UL),  # Upper left corner
            square1.get_corner(UR),  # Upper right corner
            square1.get_corner(DL),  # Lower left corner
            fill_opacity=0.5,        # Fill opacity for shading
            fill_color=BLUE,         # Fill color
            stroke_width=0           # No border
        )
        text1 = MathTex(r"\frac{1}{2}").next_to(square1, DOWN, buff=0.5)
        self.play(Write(square1), FadeIn(shaded_half), Write(text1))
        self.wait(2)

        # Create and display the second square with 1/3 shaded
        square2 = Square(side_length=3).shift(RIGHT * 3 + UP * 1)
        shaded_rectangle = Rectangle(width=1, height=3, fill_opacity=0.5, fill_color=BLUE, stroke_width=0)
        shaded_rectangle.next_to(square2.get_left(), RIGHT, buff=0)
        text2 = MathTex(r"\frac{1}{3}").next_to(square2, DOWN, buff=0.5)
        self.play(Write(square2), FadeIn(shaded_rectangle), Write(text2))
        self.wait(2)

    def TypesofFraction(self):
        self.angleChoice=[TAU/4,TAU/4,TAU/4]
        p14=cvo.CVO().CreateCVO("Fraction","").setPosition([-5.5,0,0])
        p15=cvo.CVO().CreateCVO("Types","").setPosition([-3,0,0])
        p11=cvo.CVO().CreateCVO("Proper Fraction","$Numerator<Denominator$").setPosition([3,2,0])
        p12=cvo.CVO().CreateCVO("Improper Fraction","$Numerator>Denominator$").setPosition([3,-2,0])
        p14.cvolist.append(p15)
        p15.cvolist.append(p11)
        p15.cvolist.append(p12)
        self.construct1(p14,p14)
    
    def Multiplication_of_frac(self):
        self.angleChoice=[TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Multiplication","").setPosition([-3,0,0])
        p11=cvo.CVO().CreateCVO("Fraction by Whole number","").setPosition([3,2,0])
        p12=cvo.CVO().CreateCVO("Fraction with Fraction","").setPosition([3,-2,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.fadeOutCurrentScene()
        examples = [
            ("Multiplication of Fraction by Whole number",r"Example: (3 \times \frac{2}{5})", r"3 \times \frac{2}{5}", r"= \frac{3 \times 2}{5}", r"= \frac{6}{5}"),
            ("Multiplication of Fraction with a Fraction",r"Example: (\frac{3}{2} \times \frac{1}{4})", r"\frac{3}{2} \times \frac{1}{4}", r"= \frac{3 \times 1}{2 \times 4}", r"= \frac{3}{8}")
        ]

        for example in examples:
            title = Text(example[0],font_size=36).to_edge(UP)
            self.play(Write(title))

            if example==examples[1]:
                text = MathTex("Formula = \\frac{\\text{Product of Numerators}}{\\text{Product of Denominators}}").next_to(title,DOWN,buff=0.5).scale(0.75).set_color(YELLOW)
                self.play(Write(text))
            
            example_text = MathTex(example[1], font_size=36).to_edge(LEFT).shift(RIGHT*1)
            self.play(Write(example_text))
            
            frac = MathTex(example[2])
            self.play(Write(frac))
            self.wait(1)
            
            result = MathTex(example[3])
            self.play(Write(result.next_to(frac, RIGHT)))
            self.wait(1)
            
            final_result = MathTex(example[4]).next_to(frac, RIGHT).set_color(YELLOW)
            self.play(Transform(result, final_result))
            self.wait(2)
            self.play(FadeOut(title,example_text,frac,result,final_result))


    def Reciprocal(self):
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
            frac_tex = MathTex(frac).scale(0.75).next_to(previous_frac, DOWN, buff=0.8).set_color(YELLOW)
            recip_tex = MathTex(recip).scale(0.75).next_to(previous_recip, DOWN, buff=0.8).set_color(YELLOW)
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
            self.show_example_div(*example_info)
        
        self.play(FadeOut(self.title))
        
    # Helper function to animate the conversion and calculation process
    def show_example_div(self, intro_text_str, example, example_fraction, multiplication, result, final_result):
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
        final_result_tex = MathTex(final_result).next_to(example_frac, RIGHT).set_color(YELLOW)
        self.play(Write(result_tex))
        self.wait(1)
        self.play(Transform(result_tex, final_result_tex))
        self.wait(2)
        
        # Fade out the elements
        self.play(FadeOut(intro_text, example_text, conversion_text_obj, example_frac, result_tex))

    def Decimals(self):
        text = Text("Decimal Numbers").to_edge(UP)
        self.play(Write(text))
        examples = [
            ("1 unit","1",""),
            (r"\frac{1}{10}","0.1", r"10^{th}part"),
            (r"\frac{1}{100}","0.01", r"100^{th}part"),
            (r"\frac{1}{1000}","0.001", r"1000^{th}part"),
           ]
        
        for example in examples:
            
            if example==examples[0]:
                example_text = MathTex(example[0], font_size=40).to_edge(LEFT).shift(RIGHT*1).set_color(YELLOW)
                self.play(Write(example_text))
            else :
                example_text = MathTex(example[0], font_size=40).next_to(prev,RIGHT,buff=1).shift(RIGHT*1).set_color(YELLOW)
                self.play(Write(example_text))
            
            frac = MathTex(example[1]).next_to(example_text,DOWN,buff=0.5)
            self.play(Write(frac))
            self.wait(1)
            
            result = MathTex(example[2]).next_to(example_text, UP,buff=0.5)
            self.play(Write(result))
            self.wait(1)
            
            arr = Arrow(example_text.get_right(),example_text.get_right()+RIGHT*2)
            symbol = MathTex("\\div 10").next_to(arr,UP,buff=0.1).scale(0.65)
            self.play(Create(arr),Write(symbol))

            prev = example_text
        text1 = Text("and so on",font_size=26).to_edge(RIGHT)
        self.play(Write(text1))
    
    def ExpandedForm(self):
        text = Text("Expanded Form",font_size=40).to_edge(UP)
        self.play(Write(text))
        example = Text("Example : 21.75",font_size=40).shift(UP*1)
        self.play(Write(example))
        expanded = MathTex("2 \\times 10","+ 1 \\times 1","+ 7 \\times \\frac{1}{10}","+ 5 \\times \\frac{1}{100}").scale(1).next_to(example,DOWN,buff=0.5).set_color(YELLOW)
        self.play(Write(expanded))
        self.wait(3)

    def Dec_addandsub(self):
        intro_text = Text("Addition and Subtraction of Decimals").to_edge(UP)
        self.play(Write(intro_text))

        # Rules for addition and subtraction of decimals
        rules = [
            "1. While adding or subtracting decimal numbers,\n   the digits in the same places must be added or subtracted\n",
            "2. Decimal points must come one below the other\n",
            "3. Decimal places may be made equal by placing\n   zeroes on the right side of the decimal number"
        ]

        rules_text = VGroup(*[Text(rule).scale(0.5).set_color(YELLOW) for rule in rules]).arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT)

        # Example 1
        example1 = MathTex("Example:", font_size=36).to_edge(LEFT).shift(UP * 1, RIGHT * 1)
        self.play(Write(example1))

        var1 = MathTex("39.7").shift(LEFT * 4)
        var2 = MathTex("16.45").next_to(var1, DOWN).shift(RIGHT * 0.15)
        zero = MathTex("0").next_to(var1, RIGHT, buff=0.1).set_color(PINK)
        sign = MathTex("+").next_to(var2, LEFT)
        line1 = Line(var2.get_right(), var2.get_right() + RIGHT * 2).shift(DOWN * 0.5, LEFT * 1.5)
        line2 = Line(var2.get_right(), var2.get_right() + RIGHT * 2).shift(DOWN * 1.5, LEFT * 1.5)

        self.play(Write(var1), Write(var2), Write(sign), Write(line1), Write(line2))
        
        # Write the rules
        for rule_text in rules_text:
            self.play(Write(rule_text))
            self.wait(2)

        self.play(Write(zero))

        res1 = MathTex("56.15").next_to(var2, DOWN, buff=0.5)
        self.play(Write(res1))
        self.wait(2)

        # Transition to subtraction
        sign1 = MathTex("-").next_to(var2, LEFT)
        res2 = MathTex("23.25").next_to(var2, DOWN * 2)
        
        self.play(FadeOut(res1))
        self.play(Transform(sign, sign1))
        self.play(FadeIn(res2))
        self.wait(2)
    
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
    
    def Rational(self):
        self.angleChoice=[TAU/4,TAU/4,TAU/4]
        p10=cvo.CVO().CreateCVO("Rational number","").setPosition([-3,0,0])
        p12=cvo.CVO().CreateCVO("Representation","p/q").setPosition([0.5,2.5,0])
        p13=cvo.CVO().CreateCVO("conditions","").setPosition([0.5,-2.5,0])
        p13onamelist=["p and q are integers","$q \\neq 0$"]
        p13.extendOname(p13onamelist)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.construct1(p10,p10)
    
    def EquivalentRationalNumbers(self):
        # Introduction text
        intro_text = Text("Equivalent Rational Numbers",font_size=36).to_edge(UP)
        self.play(Write(intro_text))
        self.wait(2)

        # Example 1: Showing 1/2 is equivalent to 2/4
        example1_text = MathTex(r"\text{Example 1: } \frac{1}{2} \text{ and } \frac{2}{4}", font_size=36).to_edge(LEFT).shift(UP * 2)
        self.play(Write(example1_text))
        self.wait(2)

        frac1 = MathTex(r"\frac{1}{2}", font_size=48).shift(LEFT * 1,UP*1)
        frac2 = MathTex(r"\frac{2}{4}", font_size=48).shift(RIGHT * 3,UP*1)

        arrow1 = Arrow(frac1.get_right(), frac2.get_left(), buff=0.1)
        explanation1 = Text("Multiply numerator and denominator by 2", font_size=24).next_to(arrow1, UP, buff=0.5)

        self.play(Write(frac1), Write(frac2))
        self.wait(1)
        self.play(GrowArrow(arrow1), Write(explanation1))
        self.wait(2)

        # Example 3: Showing 4/6 is equivalent to 2/3
        example3_text = MathTex(r"\text{Example 3: } \frac{-4}{6} \text{ and } \frac{-2}{3}", font_size=36).to_edge(LEFT).shift(DOWN * 0.5)
        self.play(Write(example3_text))
        self.wait(2)

        frac5 = MathTex(r"\frac{-4}{6}", font_size=48).shift(LEFT * 1,DOWN*1)
        frac6 = MathTex(r"\frac{-2}{3}", font_size=48).shift(RIGHT * 3,DOWN*1)

        arrow3 = Arrow(frac5.get_right(), frac6.get_left(), buff=0.1)
        explanation3 = Text("Divide numerator and denominator by 2", font_size=24).next_to(arrow3, UP, buff=0.5)

        self.play(Write(frac5), Write(frac6))
        self.wait(1)
        self.play(GrowArrow(arrow3), Write(explanation3))
        self.wait(2)

        # Concluding text
        conclusion_text1 = MathTex("\\text{Hence }\\frac{1}{2}\\equiv\\frac{2}{4} \\text{ and } \\frac{-4}{6}\\equiv\\frac{-2}{3}", font_size=40).to_edge(DOWN).shift(UP*0.5).set_color(YELLOW)
        self.play(Write(conclusion_text1))

    def Rat_addsub(self):
        intro_text = Text("Addition and Subtraction of Rational Numbers", font_size=36).to_edge(UP)
        self.play(Write(intro_text))
        example_text = MathTex("Example: (\\frac{1}{3} + \\frac{2}{5})", font_size=36).shift(UP*2,LEFT*1.5)
        self.play(Write(example_text))
        self.wait(2)
        fraction1 = MathTex(r"\frac{1}{3} + \frac{2}{5}").next_to(example_text,DOWN).shift(RIGHT*1)
        self.play(Write(fraction1))
        self.wait(2)
        steps = VGroup(
            Text("Step 1: Find LCM of denominators", font_size=30),
            Text("Step 2: Divide the LCM with each of the denominators seperately", font_size=30),
            Text("Step 3: Multiply with corresponding numerators and denominators", font_size=30),
            Text("Step 4: Add/Subtract the numerators", font_size=30) 
                            ).next_to(fraction1, DOWN).shift(DOWN*1.5).set_color(YELLOW)
        self.play(Write(steps[0]))
        self.wait(1)
        common_denominator = MathTex(r"\text{LCM: } 15").next_to(steps[0], DOWN)
        self.play(Write(common_denominator))
        self.wait(2)
        converted_fractions = VGroup(
            MathTex(r"15 \div 3 = 5",r"\text{ , }15 \div 5 = 3"),
            MathTex(r"\frac{1\times 5}{3\times 5} + \frac{2\times 3}{5\times 3}"),
            MathTex(r"\frac{5}{15} + \frac{6}{15} = \frac{5 + 6}{15}"),
            MathTex(r"= \frac{11}{15}")
            ).shift(UP*0.5,LEFT*1)
        self.play(Transform(steps[0], steps[1]))
        self.wait(2)
        self.play(Transform(fraction1, converted_fractions[0]))
        self.wait(2)
        self.play(Transform(steps[0], steps[2]))
        self.wait(2)
        self.play(Transform(fraction1, converted_fractions[1]))
        self.wait(2)
        self.play(Transform(steps[0], steps[3]))
        self.wait(2)
        self.play(Transform(fraction1, converted_fractions[2]))
        self.wait(2)
        self.play(Transform(fraction1, converted_fractions[3]))
        self.wait(2)
        
    def SetDeveloperList(self):
        self.DeveloperList="Sindhu"
    
    def SetSourceCodeFilename(self):
        self.SourceCodeFilename="Grade7FractionsDecimalsandRationalnumbers.py"

              
if __name__ == "__main__":
    scene = fractionanim()
    scene.render()