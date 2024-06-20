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

import cvo

class AlgebraicExpression(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderSkillbancLogo()
        self.AlgebraicExpression()
        self.fadeOutCurrentScene()
        self.ae()
        self.fadeOutCurrentScene()
        self.LikeUnliketermAnim()
        self.fadeOutCurrentScene()
        self.addition()
        self.fadeOutCurrentScene()
        self.Subtraction()
        self.fadeOutCurrentScene()
        self.Expression()
        self.fadeOutCurrentScene()
        self.Types()
        self.fadeOutCurrentScene()
        self.TypesAnim()
        self.fadeOutCurrentScene()
        self.Degree()
        self.fadeOutCurrentScene()
        self.DegreeOfMonomial()
        self.fadeOutCurrentScene()
        self.DegreeOfConstant()
        self.fadeOutCurrentScene()
        self.DegreeOfAE()
        self.fadeOutCurrentScene()
        self.simplification()
        self.fadeOutCurrentScene()
        self.SimplifyExpressionAnim()
        self.fadeOutCurrentScene()
        self.AEaddition()
        self.fadeOutCurrentScene()
        self.column()
        self.fadeOutCurrentScene()
        self.columnAnim()
        self.fadeOutCurrentScene()
        self.row()
        self.fadeOutCurrentScene()
        self.rowAnim()
        self.fadeOutCurrentScene()
        self.AEsubtraction()
        self.fadeOutCurrentScene()
        self.column1()
        self.fadeOutCurrentScene()
        self.column1Anim()
        self.fadeOutCurrentScene()
        self.row1()
        self.fadeOutCurrentScene()
        self.row1Anim()
        self.fadeOutCurrentScene()
        
     # render using CVO data object  
    def AlgebraicExpression(self):
        self.positionChoice = [[0,0,0],[-3,0,0],[3,0,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Algebraic Expression","2x-3")
        p11=cvo.CVO().CreateCVO("Algebric term","2x")
        p12=cvo.CVO().CreateCVO("Numeric term","3")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)

    def ae(self):
        self.positionChoice = [[0,0,0],[-3,0,0],[3,0,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Algebraic Expression","")
        p11=cvo.CVO().CreateCVO("like term","")
        p12=cvo.CVO().CreateCVO("unlike term","cannot perform operations")
        p12.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.setNumberOfCirclePositions(3)
        self.construct1(p10,p10)
   
    def LikeUnliketermAnim(self):
        # Title: LIKE AND UNLIKE TERMS
        title = Tex(r"\underline{\textbf{LIKE AND UNLIKE TERMS}}")
        title.scale(1.2)
        title.to_edge(UP)
        
        # LIKE TERMS section
        like_terms_header = Tex(r"\underline{LIKE TERMS}")
        like_terms_header.set_color(RED)
        like_terms_header.next_to(title, DOWN, buff=0.5)
        
        like_terms_text = VGroup(
            Tex(r"Like terms are defined as the terms that contain the same "),
            Tex(r"variable which is raised to the same power."),
            Tex(r"Examples are $x$, $4x$, $-2x$, and $7x$.")
        )
        like_terms_text.arrange(DOWN, buff=0.4)
        like_terms_text.next_to(like_terms_header, DOWN, buff=0.4)
        
        # UNLIKE TERMS section
        unlike_terms_header = Tex(r"\underline{UNLIKE TERMS}")
        unlike_terms_header.set_color(RED)
        unlike_terms_header.next_to(like_terms_text, DOWN, buff=0.5)
        
        unlike_terms_text = VGroup(
            Tex(r"Unlike terms do not have the same literal coefficients,"),
            Tex(r"and cannot be raised to the same power."),
            Tex(r"Examples are $4x + 9y$.")
        )
        unlike_terms_text.arrange(DOWN, buff=0.4)
        unlike_terms_text.next_to(unlike_terms_header, DOWN, buff=0.4)
        
        # Animation
        self.play(Write(title))
        self.wait(1)
        
        self.play(Write(like_terms_header))
        self.wait(0.5)
        for text in like_terms_text:
            self.play(Write(text))
            self.wait(0.3)
        
        self.play(Write(unlike_terms_header))
        self.wait(0.5)
        for text in unlike_terms_text:
            self.play(Write(text))
            self.wait(0.3)
        
        self.wait(2)

    def addition(self):
        self.positionChoice = [[-5,0,0],[-3,2,0],[-3,-2,0],[0,0,0],[3,0,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("like terms","5x and 7x")
        p11=cvo.CVO().CreateCVO("First term","5x")
        p12=cvo.CVO().CreateCVO("second term","7x")
        p13=cvo.CVO().CreateCVO("Addition","5x+7x")
        p14=cvo.CVO().CreateCVO("sum","12x") 
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        self.construct1(p14,p14)
        self.play(Create(CurvedArrow(p13.pos,p14.pos)))
 
    def Subtraction(self):
        self.positionChoice = [[-5,0,0],[-3,2,0],[-3,-2,0],[0,0,0],[3,0,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("like terms","2xy and 7xy")
        p11=cvo.CVO().CreateCVO("First term","2xy")
        p12=cvo.CVO().CreateCVO("second term","7xy")
        p13=cvo.CVO().CreateCVO("subtraction","2xy-7xy")
        p14=cvo.CVO().CreateCVO("Difference","-5xy")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)
        self.construct1(p13,p13)
        self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        self.construct1(p14,p14)
        self.play(Create(CurvedArrow(p13.pos,p14.pos)))
        
    def Expression(self):
        self.positionChoice = [[0,2.5,0],[4,2,0],[5,-2,0],[-3,-3,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Expression","3x+4")
        p11=cvo.CVO().CreateCVO("Coefficient","3")
        p12=cvo.CVO().CreateCVO("variable","x")
        p13=cvo.CVO().CreateCVO("Constant","4")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.construct1(p10,p10)
        
    def Types(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Expression types","")
        # p10namelist=["Monomial","Binomial","Trinomial","Multinomial"]
        # p10.extendOname(p10namelist)
        p11=cvo.CVO().CreateCVO("Monomial","x")
        p12=cvo.CVO().CreateCVO("Binomial","a+4x")
        p13=cvo.CVO().CreateCVO("Trinomial","$ax^2+4x+2$")
        p14=cvo.CVO().CreateCVO("Multinomial","$4x^2+2xy+cx+d$")
        p14.setcircleradius(1.25)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        self.setNumberOfCirclePositions(5)
        self.construct1(p10,p10)

    def TypesAnim(self):
         # Title: Types of Algebraic Expressions
        title = Tex(r"\underline{\textbf{Types Of Algebraic Expressions}}")
        title.scale(1.2)
        title.to_edge(UP)

        # Table headers
        header_terms = Tex(r"No. of terms").set_color(RED)
        header_name = Tex(r"Name of the Expression").set_color(RED)
        header_examples = Tex(r"Examples").set_color(RED)

        # Arrange headers
        header_terms.move_to(LEFT * 4)
        header_name.move_to(ORIGIN)
        header_examples.move_to(RIGHT * 4)

        # Headers group
        headers = VGroup(header_terms, header_name, header_examples)
        headers.arrange(RIGHT, buff=2)  # Adjust buff as needed
        headers.next_to(title, DOWN, buff=0.5)

        # Examples and characteristics
        term1 = Tex(r"One term",font_size=30)
        name1 = Tex(r"Monomial",font_size=30)
        example1 = Tex(r"x",font_size=30)

        term2 = Tex(r"Two unlike terms",font_size=30)
        name2 = Tex(r"Binomial",font_size=30)
        example2 = Tex(r"a+4x",font_size=30)

        term3 = Tex(r"Three unlike terms",font_size=30)
        name3 = Tex(r"Trinomial",font_size=30)
        example3 = Tex(r"$ax^2+4x+2$",font_size=30)

        term4 = Tex(r"More than one unlike term",font_size=30)
        name4 = Tex(r"Multinomial",font_size=30)
        example4 = Tex(r"$4x^2+2xy+cx+d$",font_size=30)

        # Arrange rows
        term1.next_to(headers, DOWN, buff=0.5, aligned_edge=LEFT)
        name1.next_to(term1, RIGHT*1.3, buff=4,aligned_edge=ORIGIN)
        example1.next_to(name1, RIGHT*1.3, buff=4,aligned_edge=RIGHT)

        term2.next_to(term1, DOWN, buff=0.5, aligned_edge=LEFT)
        name2.next_to(term2, RIGHT*1.02, buff=4,aligned_edge=ORIGIN)
        example2.next_to(name2, RIGHT*1.3, buff=4,aligned_edge=RIGHT)

        term3.next_to(term2, DOWN, buff=0.5, aligned_edge=LEFT)
        name3.next_to(term3, RIGHT*1, buff=4,aligned_edge=ORIGIN)
        example3.next_to(name3, RIGHT*1.1, buff=4,aligned_edge=RIGHT)

        term4.next_to(term3, DOWN, buff=0.5, aligned_edge=LEFT)
        name4.next_to(term4, RIGHT*0.7, buff=4,aligned_edge=ORIGIN)
        example4.next_to(name4, RIGHT*1.0, buff=4,aligned_edge=RIGHT)

        # Animation
        self.play(Write(title))
        self.wait(1)
        self.play(Write(headers))
        self.wait(1)
        self.play(Write(term1), Write(name1), Write(example1))
        self.wait(1)
        self.play(Write(term2), Write(name2), Write(example2))
        self.wait(1)
        self.play(Write(term3), Write(name3), Write(example3))
        self.wait(1)
        self.play(Write(term4), Write(name4), Write(example4))
        self.wait(1)
        self.wait(2)

    def Degree(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Degree","").setPosition([0,2,0])
        # p10namelist=["Monomial","constant","algebraic term"]
        # p10.extendOname(p10namelist)
        p11=cvo.CVO().CreateCVO("Monomial","$7x^2$").setPosition([-3,2,0])
        p12=cvo.CVO().CreateCVO("Constant","5").setPosition([-2,-2,0])
        p13=cvo.CVO().CreateCVO("Algebraic term","$2x^3+3x^2+4x^3+5$").setPosition([5,2,0])
        p111=cvo.CVO().CreateCVO("Degree","2").setPosition([-4,0,0])
        p122=cvo.CVO().CreateCVO("Degree","0").setPosition([2,-2,0])
        p133=cvo.CVO().CreateCVO("Degree","3").setPosition([5,-1,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p11.cvolist.append(p111)
        p12.cvolist.append(p122)
        p13.cvolist.append(p133)
        self.construct1(p10,p10)

    def DegreeOfMonomial(self):
        # Main title and subtitle
        main_title = Tex(r"\underline{\textbf{Degree Of Algebraic Expression}}", font_size=60)
        main_title.set_color(RED)
        main_title.to_edge(UP)

        subtitle = Tex(r"\underline{Degree of Monomial}")
        subtitle.next_to(main_title, DOWN, buff=1)

        # Texts
        definition = Tex(r"The sum of all exponents of the variables present in a monomial")
        definition.next_to(subtitle, DOWN)

        degree_definition = Tex(r"is called degree of the term or degree of the monomial.")
        degree_definition.next_to(definition, DOWN)

        example = Tex(r"Example: $7x^2$, variable = $x^2$, exponent = 2, degree = 2")
        example.next_to(degree_definition, DOWN)

        # Animation
        self.play(Write(main_title))
        self.wait(1)
        self.play(Write(subtitle))
        self.wait(1)
        self.play(Write(definition))
        self.wait(1)
        self.play(Write(degree_definition))
        self.wait(1)
        self.play(Write(example))
        self.wait(2)

        # Show example monomial and its parts
        monomial_example = Tex(r"$7x^2$")
        monomial_example.next_to(example, DOWN)

        degree_label = Tex(r"Degree = 2")
        degree_label.next_to(monomial_example, DOWN, buff=0.5)

        self.play(Write(monomial_example))
        self.wait(1)
        self.play(Write(degree_label))
        self.wait(2)

    def DegreeOfConstant(self):
        subtitle = Tex(r"\underline{Degree of Constant Terms}")
        subtitle.to_edge(UP)

        # Texts
        definition = Tex(r"A constant term does not contain any variable ")
        definition.next_to(subtitle, DOWN,buff=1)

        degree_definition1 = Tex(r"and is a fixed numerical value.")
        degree_definition1.next_to(definition, DOWN)
        degree_definition2 = Tex(r"The degree of a constant term in a polynomial is simply 0.")
        degree_definition2.next_to(degree_definition1, DOWN)

        example = Tex(r"Example: $5$")
        example.next_to(degree_definition2, DOWN)

        # Animation
        
        self.play(Write(subtitle))
        self.wait(1)
        self.play(Write(definition))
        self.wait(1)
        self.play(Write(degree_definition1))
        self.wait(1)
        self.play(Write(degree_definition2))
        self.wait(1)
        self.play(Write(example))
        self.wait(2)

        # Show example constant term and its degree
        constant_example = Tex(r"$5$")
        constant_example.next_to(example, DOWN, buff=0.5)

        degree_label = Tex(r"Degree = 0")
        degree_label.next_to(constant_example, DOWN, buff=0.5)

        self.play(Write(constant_example))
        self.wait(1)
        self.play(Write(degree_label))
        self.wait(2)

    def DegreeOfAE(self):
        subtitle = Tex(r"\underline{Degree of Algebraic Expression}")
        subtitle.to_edge(UP)
        

        # Texts
        definition = Tex(r"The degree of an algebraic expression is the highest ", font_size=48)
        definition.next_to(subtitle, DOWN)
        definition1 = Tex(r"degree of the terms with non-zero coefficients.",font_size=48)
        definition1.next_to(definition, DOWN,LEFT)

        degree_definition = Tex(r"For polynomials, the degree is simply the highest",font_size=48)
        degree_definition.next_to(definition1, DOWN)
        degree_definition1 = Tex(r"degree among its terms.",font_size=48)
        degree_definition1.next_to(degree_definition, DOWN,LEFT)
        

        example_expression = Tex(r"Expression: $2x^3 + 3x^2 + 4x^3 + 5$")
        example_expression.next_to(degree_definition1, DOWN,buff=0.8)

        combined_expression = Tex(r"Combining like terms: $2x^3 + 4x^3 + 3x^2 + 5$")
        combined_expression.next_to(example_expression, DOWN)

        degree_result = Tex(r"The highest degree term is $4x^3$,Degree = 3")
        degree_result.next_to(combined_expression, DOWN)
        # Animation
        
        self.play(Write(subtitle))
        self.wait(1)
        self.play(Write(definition))
        self.wait(1)
        self.play(Write(definition1))
        self.wait(1)
        self.play(Write(degree_definition))
        self.wait(1)
        self.play(Write(degree_definition1))
        self.wait(1)
        
        self.play(Write(example_expression))
        self.wait(1)
        self.play(Write(combined_expression))
        self.wait(1)
        self.play(Write(degree_result))
        self.wait(1)
 
    def simplification(self):
       self.positionChoice = [[-3,2,0],[2,2,0],[4,0,0],[-3,-2,0]]
       self.isRandom = False
       p10=cvo.CVO().CreateCVO("simplification of Expression","")
       p11=cvo.CVO().CreateCVO("step1","write expression")
       p12=cvo.CVO().CreateCVO("step2","group like terms")
       p13=cvo.CVO().CreateCVO("step3","add like terms")
       p11.setcircleradius(1.25)
       p12.setcircleradius(1.25)
       p13.setcircleradius(1.25)
       p10.cvolist.append(p11)
       p10.cvolist.append(p12)
       p10.cvolist.append(p13)
       self.construct1(p10,p10)

    def SimplifyExpressionAnim(self):
       # Title: Simplification of an algebraic expression (bold)
        title = Tex(r"\underline{\textbf{Simplification of an algebraic expression}}")
        title.to_edge(UP)
        
        # Additional line below the title
        expression_intro = Tex(r"Consider the expression $9x^2 - 4xy + 5y^2 + 2xy - y^2 - 3x^2 + 6xy$")
        expression_intro.set_color(BLUE)
        expression_intro.next_to(title, DOWN, buff=0.5)
        
        # Step 1: Write down the expression
        step_1_text = Tex(r"Step 1: Write down the expression")
        step_1_text.set_color(RED)
        expression = Tex(r"$9x^2 - 4xy + 5y^2 + 2xy - y^2 - 3x^2 + 6xy$")
        step_1_text.next_to(expression_intro, DOWN, buff=0.5)
        expression.next_to(step_1_text, DOWN, buff=0.3)
        
        # Step 2: Group the like terms together
        step_2_text = Tex(r"Step 2: Group the like terms together")
        step_2_text.set_color(RED)
        grouped_expression = Tex(r"$(9x^2 - 3x^2) + (2xy - 4xy + 6xy) + (5y^2 - y^2)$")
        step_2_text.next_to(expression, DOWN, buff=0.3)
        grouped_expression.next_to(step_2_text, DOWN, buff=0.3)
        
        # Step 3: Adding the like terms
        step_3_text = Tex(r"Step 3: Add the like terms")
        step_3_text.set_color(RED)
        simplified_expression = Tex(r"$(9 - 3)x^2 + (2 - 4 + 6)xy + (5 - 1)y^2$")
        final_expression = Tex(r"$= 6x^2 + 4xy + 4y^2$")
        step_3_text.next_to(grouped_expression, DOWN, buff=0.3)
        simplified_expression.next_to(step_3_text, DOWN, buff=0.3)
        final_expression.next_to(simplified_expression, DOWN, buff=0.3)
        
        # Animation
        self.play(Write(title))
        self.wait(1)
        self.play(Write(expression_intro))
        self.wait(1)
        self.play(Write(step_1_text))
        self.play(Write(expression))
        self.wait(1)
        self.play(Write(step_2_text))
        self.play(Write(grouped_expression))
        self.wait(1)
        self.play(Write(step_3_text))
        self.play(Write(simplified_expression))
        self.play(Write(final_expression))
        self.wait(2)

    

    def AEaddition(self):
         self.positionChoice = [[-4,0,0],[2,2,0],[2,-2,0]]
         self.isRandom = False
         p10=cvo.CVO().CreateCVO("Addition of expression","")
         p11=cvo.CVO().CreateCVO("Column method","")
         p12=cvo.CVO().CreateCVO("Row method","")
         p10.cvolist.append(p11)
         p10.cvolist.append(p12)
         self.construct1(p10,p10)
         
    def column(self):
         self.positionChoice = [[-3,2,0],[2,2,0],[2,-2.5,0],[-4,-2,0]]
         self.isRandom = False
         p10=cvo.CVO().CreateCVO("Column method","")
         p11=cvo.CVO().CreateCVO("step 1","express in standard form")    
         p12=cvo.CVO().CreateCVO("step 2","write one below the other ")   
         p13=cvo.CVO().CreateCVO("step 3","Add like terms column wise and write result") 
         p11.setcircleradius(1.7)
         p12.setcircleradius(1.7)
         p13.setcircleradius(1.7)
         p10.cvolist.append(p11)
         p10.cvolist.append(p12)
         p10.cvolist.append(p13)
         self.construct1(p10,p10)

    def columnAnim(self):
        # Title
        title = Tex(r"\underline{\textbf{Column or Vertical Method}}", font_size=48, color=WHITE).to_edge(UP)
        title.set_color(RED)
        self.play(Write(title))
        self.wait(1)

        # Intro
        intro = Tex(r"Add $3x^2 + 5x - 4$ and $6 + 6x^2$")
        intro.set_color(BLUE)
        intro.next_to(title, DOWN)
        self.play(Write(intro))
        self.wait(2)

        # Step 1
        step1 = Text("STEP 1: Write the expressions in standard form", color=YELLOW, font_size=30).next_to(intro, DOWN)
        expr1 = Tex(r"(i) \ $3x^2 + 5x - 4 = 3x^2 + 5x - 4$", font_size=30).next_to(step1, DOWN)
        expr2 = Tex(r"(ii) \ $6 + 6x^2 = 6x^2 + 6$", font_size=30).next_to(expr1, DOWN)
        self.play(Write(step1))
        self.play(Write(expr1), Write(expr2))
        self.wait(2)

        # Step 2
        step2 = Text("STEP 2: Write the expressions one below the other", color=YELLOW, font_size=30).next_to(expr2, DOWN)
        aligned_expr1 = Tex(r"$3x^2 + 5x - 4$", font_size=30).next_to(step2, DOWN)
        aligned_expr2 = Tex(r"$6x^2 \ \ \ \ + 6$", font_size=30).next_to(aligned_expr1, DOWN)
        self.play(Write(step2))
        self.play(Write(aligned_expr1), Write(aligned_expr2))
        self.wait(2)

        # Step 3
        step3 = Text("STEP 3: Add column-wise and write the result", color=YELLOW, font_size=30).next_to(aligned_expr2, DOWN)
        result1 = Tex(r"$3x^2 + 5x - 4$", font_size=30).next_to(step3, DOWN)
        result2 = Tex(r"$6x^2 \ \ \ \ +6$", font_size=30).next_to(result1, DOWN)
        result3 = Tex(r"$9x^2 + 5x + 2$", font_size=30).next_to(result2, DOWN)
        self.play(Write(step3))
        self.wait(2)
        self.play(Write(result1))
        self.wait(2)
        self.play(Write(result2))
        self.wait(2)
        self.play(Write(result3))
        self.wait(2)
        line = Line(color=WHITE).scale(6).next_to(result3, UP, buff=0.1)
        underline = Line(color=WHITE).scale(6).next_to(result3, DOWN, buff=0.1)
        result_with_lines = VGroup(line, result3, underline)
        self.play(Write(result_with_lines))
        self.wait(2)

    def row(self):
         self.positionChoice = [[-3,2,0],[2,2,0],[4,0,0],[2,-2.5,0],[-4,-2,0]]
         self.isRandom = False
         p10=cvo.CVO().CreateCVO("Row method","")
         p11=cvo.CVO().CreateCVO("step 1","express with add symbol between them")    
         p12=cvo.CVO().CreateCVO("step 2","rearrange grouping like terms ")   
         p13=cvo.CVO().CreateCVO("step 3","simplify coefficients")
         p14=cvo.CVO().CreateCVO("step 4","note result in standard form") 
         p11.setcircleradius(1.5)
         p12.setcircleradius(1.7)
         p13.setcircleradius(1.6)
         p14.setcircleradius(1.8)
         p10.cvolist.append(p11)
         p10.cvolist.append(p12)
         p10.cvolist.append(p13)
         p10.cvolist.append(p14)
         self.construct1(p10,p10)

    def rowAnim(self):
        # Title
        title = Tex(r"\underline{\textbf{Row or Horizontal Method}}", font_size=48, color=WHITE).to_edge(UP)
        title.set_color(RED)
        self.play(Write(title))
        self.wait(1)

        # Intro
        intro = Tex(r"Add $3x^2 + 5x - 4$ and $6 + 6x^2$")
        intro.set_color(BLUE)
        intro.next_to(title, DOWN)
        self.play(Write(intro))
        self.wait(2)

        # Step 1
        step1 = Text("STEP 1 :-Write expressions with addition symbol in between them", color=YELLOW, font_size=30).next_to(intro, DOWN)
       
        expression1 = Tex(r"$3x^2 + 5x - 4 + 6 + 6x^2$", font_size=36).next_to(step1, DOWN)
        self.play(Write(step1))
        self.wait(2)
        self.play(Write(expression1))
        self.wait(2)
        # Step 2
        step_2 = Text("STEP 2: Rearrange the terms by grouping like terms together", color=YELLOW,font_size=30).next_to(expression1, DOWN)
        expression2 = MathTex("(3x^2 + 6x^2) + (5x) + (-4 + 6)").next_to(step_2, DOWN)
        self.play(Write(step_2))
        self.wait(2)
        self.play(Write(expression2))
        self.wait(2)

        # Step 3
        step_3= Text("STEP 3: Simplify the expression coefficients together", color=YELLOW, font_size=30).next_to(expression2, DOWN)
        expression3= MathTex("(3 + 6)x^2 + 5x + 2").next_to(step_3, DOWN)
        self.play(Write(step_3))
        self.wait(2)
        self.play(Write(expression3))
        self.wait(2)

        # Step 4
        step_4 = Text("STEP 4: Write the resultant expression in standard form", color=YELLOW, font_size=30).next_to(expression3, DOWN)
        expression4 = MathTex("9x^2 + 5x + 2").next_to(step_4, DOWN)
        self.play(Write(step_4))
        self.wait(2)
        self.play(Write(expression4))
        self.wait(2)

    def AEsubtraction(self):
         self.positionChoice = [[-4,0,0],[2,2,0],[2,-2,0]]
         self.isRandom = False
         p10=cvo.CVO().CreateCVO("Subtraction of expression","")
         p11=cvo.CVO().CreateCVO("Column method","")
         p12=cvo.CVO().CreateCVO("row method","")
         p10.cvolist.append(p11)
         p10.cvolist.append(p12)
         self.construct1(p10,p10)
         
    def column1(self):
         self.positionChoice = [[-3,2,0],[2,2,0],[4,0,0],[2,-2.5,0],[-4,-2,0]]
         self.isRandom = False
         p10=cvo.CVO().CreateCVO("Column method","")
         p11=cvo.CVO().CreateCVO("step 1","express in standard form")    
         p12=cvo.CVO().CreateCVO("step 2","write one below the other ")   
         p13=cvo.CVO().CreateCVO("step 3","change sign of every term in second row") 
         p14=cvo.CVO().CreateCVO("step 4","Add like terms column wise and note result") 
         p11.setcircleradius(1.6)
         p12.setcircleradius(1.7)
         p13.setcircleradius(1.6)
         p14.setcircleradius(1.7)
         p10.cvolist.append(p11)
         p10.cvolist.append(p12)
         p10.cvolist.append(p13)
         p10.cvolist.append(p14) 
         self.construct1(p10,p10)

    def column1Anim(self):
        # Title
        title = Tex(r"\underline{\textbf{Column or Vertical Method}}", font_size=48, color=WHITE).to_edge(UP)
        title.set_color(RED)
        self.play(Write(title))
        self.wait(1)

        # Intro
        intro = Tex(r"Subtract 3a+4b-2c and 3c+6a-2b ", font_size = 40)
        intro.set_color(BLUE)
        intro.next_to(title, DOWN)
        self.play(Write(intro))
        self.wait(2)

        # Step 1
        step1 = Text("STEP 1: Write the expressions in standard form", color=YELLOW, font_size=25).next_to(intro, DOWN,buff=0.5)
        expr1 = Tex(r"3c + 6a - 2b = 6a - 2b + 3c", font_size=30).next_to(step1, DOWN,buff=0.1)
        expr2 = Tex(r"3a + 4b - 2c = 3a + 4b - 2c", font_size=30).next_to(expr1, DOWN,buff=0.1)
        self.play(Write(step1))
        self.play(Write(expr1), Write(expr2))
        self.wait(2)

        # Step 2
        step2 = Text("STEP 2: Write the expressions one below the other ", color=YELLOW, font_size=25).next_to(expr2, DOWN,buff=0.1)
        aligned_expr1 = Tex(r"6a - 2b + 3c", font_size=30).next_to(step2, DOWN,buff=0.1)
        aligned_expr2 = Tex(r"3a + 4b - 2c", font_size=30).next_to(aligned_expr1, DOWN,buff=0.1)
        self.play(Write(step2))
        self.play(Write(aligned_expr1), Write(aligned_expr2))
        self.wait(2)

        # Step 3
        step3 = Text("STEP 3: change the sign of every term in second row", color=YELLOW, font_size=25).next_to(aligned_expr2, DOWN,buff=0.1)
        result1 = Tex(r"6a - 2b + 3c", font_size=30).next_to(step3, DOWN,buff=0.1)
        result2 = Tex(r"3a + 4b - 2c", font_size=30).next_to(result1, DOWN,buff=0.1)
        result3 = Tex(r"(-) \ \ \ (-) \ \ \ (+)", font_size=30).next_to(result2, DOWN,buff=0.1)
        self.play(Write(step3))
        self.wait(2)
        self.play(Write(result1))
        self.wait(2)
        self.play(Write(result2))
        self.wait(2)
        self.play(Write(result3))
        self.wait(2)

        #step 4
        step4 = Text("STEP 4: Add like terms and write resultant column-wise", color=YELLOW, font_size=25).next_to(result3, DOWN,buff=0.1)
        result_1 = Tex(r"6a - 2b + 3c", font_size=30).next_to(step4, DOWN,buff=0.1)
        result_2 = Tex(r"3a + 4b - 2c", font_size=30).next_to(result_1, DOWN,buff=0.1)
        result_3 = Tex(r"(-) \ \ \ \ (-) \ \ \ \ (+)", font_size=30).next_to(result_2, DOWN,buff=0.1)
        result_4 = Tex(r"3a - 6b + 5c", font_size=30).next_to(result_3,DOWN,buff=0.2)   
        self.play(Write(step4))
        self.wait(2)
        self.play(Write(result_1))
        self.wait(2)
        self.play(Write(result_2))
        self.wait(2)
        self.play(Write(result_3))
        self.wait(2)
        self.play(Write(result_4))
        self.wait(2)

        line = Line(color=WHITE).scale(6).next_to(result_4, UP, buff=0.2)
        underline = Line(color=WHITE).scale(6).next_to(result_4, DOWN, buff=0.2)
        result_with_lines = VGroup(line, result_4, underline)
        self.play(Write(result_with_lines))
        self.wait(2)


    def row1(self):
         self.positionChoice = [[-3,2,0],[2,2,0],[4,0,0],[2,-2.5,0],[-4,-2,0]]
         self.isRandom = False
         p10=cvo.CVO().CreateCVO("Row method","")
         p11=cvo.CVO().CreateCVO("step 1","express within brackets")    
         p12=cvo.CVO().CreateCVO("step 2","add additive inverse")   
         p13=cvo.CVO().CreateCVO("step 3","group like terms and add or sub")
         p14=cvo.CVO().CreateCVO("step 4","express in standard form ") 
         p11.setcircleradius(1.5)
         p12.setcircleradius(1.5)
         p13.setcircleradius(1.5)
         p14.setcircleradius(1.6)
         p10.cvolist.append(p11)
         p10.cvolist.append(p12)
         p10.cvolist.append(p13)
         p10.cvolist.append(p14)
         self.construct1(p10,p10)

    def row1Anim(self):
         # Title
        title = Tex(r"\underline{\textbf{Row or Horizontal Method}}", font_size=48, color=WHITE).to_edge(UP)
        title.set_color(RED)
        self.play(Write(title))
        self.wait(1)

        # Intro
        intro = Tex(r"Subtract 3a+4b-2c and 3c+6a-2b")
        intro.set_color(BLUE)
        intro.next_to(title, DOWN)
        self.play(Write(intro))
        self.wait(2)

        # Step 1
        step1 = Text("STEP 1 :-Write expression to subtract in bracket and assign -ve sign ", color=YELLOW, font_size=30).next_to(intro, DOWN)
       
        expression1 = Tex(r"3c+6a-2b-(3a+4b-2c)", font_size=36).next_to(step1, DOWN)
        self.play(Write(step1))
        self.wait(2)
        self.play(Write(expression1))
        self.wait(2)
        # Step 2
        step_2 = Text("STEP 2: Add additive inverse of second expression to first", color=YELLOW,font_size=30).next_to(expression1, DOWN)
        expression2 = MathTex("3c+6a-2b-3a-4b+2c").next_to(step_2, DOWN)
        self.play(Write(step_2))
        self.wait(2)
        self.play(Write(expression2))
        self.wait(2)

        # Step 3
        step_3= Text("STEP 3: Group like terms and add or subtract ", color=YELLOW, font_size=30).next_to(expression2, DOWN)
        expression3= MathTex("(3c+2c)+(6a-3b)+(-2b-4b)").next_to(step_3, DOWN)
        expression_3= MathTex("=5c+3a-6b").next_to(expression3, DOWN)
        self.play(Write(step_3))
        self.wait(2)
        self.play(Write(expression3))
        self.wait(2)
        self.play(Write(expression_3))
        self.wait(2)

        # Step 4
        step_4 = Text("STEP 4: Write the resultant expression in standard form", color=YELLOW, font_size=30).next_to(expression_3, DOWN)
        expression4 = MathTex("3a-6b+5c").next_to(step_4, DOWN)
        self.play(Write(step_4))
        self.wait(2)
        self.play(Write(expression4))
        self.wait(2)

if __name__ == "__main__":
    scene = AlgebraicExpression()
    scene.render()
    