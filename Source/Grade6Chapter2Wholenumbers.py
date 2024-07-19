from manim import *
from AbstractAnim import AbstractAnim
import cvo

class Grade6Chapter2Wholenumbers(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.topic1()
        self.Introduction1()
        self.fadeOutCurrentScene()
        self.Addition()
        self.fadeOutCurrentScene()
        self.Subtraction()
        self.fadeOutCurrentScene()
        self.Multiplication()
        self.fadeOutCurrentScene()
        self.Division()
        self.fadeOutCurrentScene()
        self.Introduction2()
        self.fadeOutCurrentScene()
       
        self.Commutativeproperty()
        self.fadeOutCurrentScene()
        self.Associativeproperty()
        self.fadeOutCurrentScene()
        self.Additiveidentity()
        self.fadeOutCurrentScene()
        
        self.GithubSourceCodeReference()

    def Introduction(self):
        self.setNumberOfCirclePositions(4)
        #self.angleChoice = [0,0,0]
        self.isRandom = False
        self.isRandom = False
        self.angleChoice = [TAU/2,TAU/3,-TAU/2]

        p10=cvo.CVO().CreateCVO(" Whole Numbers","").setPosition([0,2.5,0])
        p11=cvo.CVO().CreateCVO("Definition","any number between zero to infinity, not including decimals or fractions").setPosition([3,-1,0]) 
        p12=cvo.CVO().CreateCVO("Denoted by","W").setPosition([4,2,0])
        p13=cvo.CVO().CreateCVO("Representation", "W={0,1,2,3....}").setPosition([-4,2,0])
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.construct1(p10,p10)
        #self.construct1(p13,p13)
        #self.play(Create(CurvedArrow(p11.pos,p13.pos)),Create(CurvedArrow(p12.pos,p13.pos)))
        #self.play()

    
    def topic1(self):
        operations = [
            ("addition", 2, 3),
            ("subtraction", 5, 2),
            ("multiplication", 2, 3),
        ]
        for operation, a, b in operations:
            self.clear()
            number_line = self.create_number_line()
            self.play(Create(number_line))
            self.perform_operation(number_line, a, b, operation)
            self.wait()
        self.fadeOutCurrentScene()

    def create_number_line(self):
        return NumberLine(
            x_range=[-10, 10, 1],
            length=12,
            color=BLUE,
            include_numbers=True,
            label_direction=DOWN,
        )

    def create_jump_path(self, start, end):
        control_point = start + (end - start) / 2 + UP * 0.5
        path = CubicBezier(start, control_point, control_point, end)
        dashed_path = DashedVMobject(path, num_dashes=15, color=YELLOW)
        return path, dashed_path


    def perform_operation(self, number_line, a, b, operation):
        colors = {"addition": RED, "subtraction": BLUE, "multiplication": GREEN}
        dot = Dot(color=colors[operation]).scale(1.5)
        title = Text(f"{operation.capitalize()} Jumps", font_size=48).to_edge(UP)
        underline = Line(
            start=title.get_left() + DOWN * 0.3,
            end=title.get_right() + DOWN * 0.3,
            color=YELLOW
        )
        self.play(Write(title), Create(underline))
        self.wait(1)

        if operation == "addition":
            dot.move_to(number_line.number_to_point(a))
            explanation = f"A dot starts at {a} and jumps forward for {b} times."
            jumps = b
            step = 1
        elif operation == "subtraction":
            dot.move_to(number_line.number_to_point(a))
            explanation = f"A dot starts at {a} and jumps backward for {b} times."
            jumps = b
            step = -1
        elif operation == "multiplication":
            dot.move_to(number_line.number_to_point(0))
            explanation = f"A dot jumps {a} steps in a single jump. It jumps {b} times."
            jumps = b
            step = a

        explanation_text = Tex(explanation, font_size=35).next_to(number_line, DOWN, buff=1)
        self.play(Write(explanation_text))
        self.wait(1)
        self.play(FadeIn(dot))

        for i in range(jumps):
            start_position = number_line.number_to_point(a + i * step if operation != "multiplication" else i * step)
            end_position = number_line.number_to_point(a + (i + 1) * step if operation != "multiplication" else (i + 1) * step)
            jump_path, dashed_jump_path = self.create_jump_path(start_position, end_position)
            
            self.play(Create(dashed_jump_path), run_time=0.3)
            self.play(MoveAlongPath(dot, jump_path), run_time=0.3)
            self.wait(0.2)

        result_text = self.get_result_text(a, b, operation)
        result = Tex(result_text, font_size=35).next_to(explanation_text, DOWN, buff=0.6)
        self.play(Write(result))
        self.wait(1)
        self.play(FadeOut(dot, title, underline, explanation_text, result))
        #self.wait(1)

    def get_result_text(self, a, b, operation):
        if operation == "addition":
            return f"So the dot jumped a total of {a} + {b} = {a+b} steps"
        elif operation == "subtraction":
            return f"So the dot jumped a total of {a} - {b} = {a-b} steps"
        elif operation == "multiplication":
            return f"So the dot jumped a total of {a} * {b} = {a*b} steps"


    def Introduction1(self):
        self.setNumberOfCirclePositions(2)
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO(" Whole Numbers", "")
        p11 = cvo.CVO().CreateCVO("Operations", "")
        p11.extendOname(["Addition", "Subtraction", "Multiplication", "Division"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10, p10)
    
    def Addition(self):
        self.positionChoice=[[-4,0,0],[0,-2,0],[4,0,0]]        
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO(" Whole Numbers", "2,3")
        p11 = cvo.CVO().CreateCVO("Operation", "X+Y")
        p12 = cvo.CVO().CreateCVO("Sum", "5")
        

        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        self.construct1(p10, p10)
        self.fadeOutCurrentScene()

        title = Text("Addition").to_edge(UP)
        self.play(Write(title))

        examples = [
            r"X + Y \quad \text{example:}\quad 2+3 =5",
            r"X + Y \quad \text{example:}\quad 5+7 =12",
            r"X + Y \quad \text{example:}\quad 2+0 =2",
            r"X + Y \quad \text{example:}\quad 2+8 =10",
            
        ]
        example1 = MathTex(examples[0]).scale(0.8).next_to(title, DOWN, buff=1)
        example2 = MathTex(examples[1]).scale(0.8).next_to(example1, DOWN, aligned_edge=LEFT, buff=0.5)
        example3 = MathTex(examples[2]).scale(0.8).next_to(example2, DOWN, aligned_edge=LEFT, buff=0.5)
        example4 = MathTex(examples[3]).scale(0.8).next_to(example3, DOWN, aligned_edge=LEFT, buff=0.5)

        self.play(Write(example1))
        self.wait(1)
        self.play(Write(example2))
        self.wait(1)
        self.play(Write(example3))
        self.wait(1)
        self.play(Write(example4))
        self.wait(1)

        self.wait(3)

    def Subtraction(self):
        self.positionChoice=[[-4,0,0],[0,-2,0],[4,0,0]]        
        self.isRandom = False
        
        p10 = cvo.CVO().CreateCVO("Whole Numbers", "3,2")
        p11 = cvo.CVO().CreateCVO("Operation", "X-Y")
        p12 = cvo.CVO().CreateCVO("Difference", "1")
    
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        self.construct1(p10, p10)
        self.fadeOutCurrentScene()

        title = Text("Subtraction").to_edge(UP)
        self.play(Write(title))

        examples = [
        r"X - Y \quad \text{example:} \quad 3 - 2 = 1",
        r"X - Y \quad \text{example:} \quad 2 - 0 = 2",
        r"X - Y \quad \text{example:} \quad 5 - 3 = 2",
        r"X - Y \quad \text{example:} \quad 7 - 3 = 4",
       
         ]
        example1 = MathTex(examples[0]).scale(0.8).next_to(title, DOWN, buff=1)
        example2 = MathTex(examples[1]).scale(0.8).next_to(example1, DOWN, aligned_edge=LEFT, buff=0.5)
        example3 = MathTex(examples[2]).scale(0.8).next_to(example2, DOWN, aligned_edge=LEFT, buff=0.5)
        example4 = MathTex(examples[3]).scale(0.8).next_to(example3, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(Write(example1))
        self.wait(1)
        self.play(Write(example2))
        self.wait(1)
        self.play(Write(example3))
        self.wait(1)
        self.play(Write(example4))
        self.wait(1)
 
        self.wait(3)

    def Multiplication(self):
        self.positionChoice=[[-4,0,0],[0,-2,0],[4,0,0]]        
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Whole Numbers", "2,3")
        p11 = cvo.CVO().CreateCVO("Operation", "$ X \\times Y $")
        p12 = cvo.CVO().CreateCVO("Product", "6")
    
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        self.construct1(p10, p10)
        self.fadeOutCurrentScene()

        title = Text("Multiplication").to_edge(UP)
        self.play(Write(title))

        examples = [
            r"X \times Y \quad \text{example:} \quad 3 \times 2 = 6",
            r"X \times Y \quad \text{example:} \quad 5 \times 3 = 15",
            r"X \times Y \quad \text{example:} \quad 7 \times 4 = 28",
            r"X \times Y \quad \text{example:} \quad 9 \times 6 = 54",
            
            
        ]
        example1 = MathTex(examples[0]).scale(0.8).next_to(title, DOWN, buff=1)
        example2 = MathTex(examples[1]).scale(0.8).next_to(example1, DOWN, aligned_edge=LEFT, buff=0.5)
        example3 = MathTex(examples[2]).scale(0.8).next_to(example2, DOWN, aligned_edge=LEFT, buff=0.5)
        example4 = MathTex(examples[3]).scale(0.8).next_to(example3, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(Write(example1))
        self.wait(1)
        self.play(Write(example2))
        self.wait(1)
        self.play(Write(example3))
        self.wait(1)
        self.play(Write(example4))
        self.wait(1)
 
        self.wait(3)


    def Division(self):
        self.positionChoice=[[-4,0,0],[0,-2,0],[4,0,0]]        
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Whole Numbers", "6,3")
        p11 = cvo.CVO().CreateCVO("Operation", "$ X \\div Y $")
        p12 = cvo.CVO().CreateCVO("Quotient", "2")
    
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        self.construct1(p10, p10)
        self.fadeOutCurrentScene()

        title = Text("Division").to_edge(UP)
        self.play(Write(title))

        examples = [
        r"X \div Y \quad \text{example:} \quad 6 \div 3 = 2",
        r"X \div Y \quad \text{example:} \quad 9 \div 3 = 3",
        r"X \div Y \quad \text{example:} \quad 12 \div 3 = 4",
        r"X \div Y \quad \text{example:} \quad 12 \div 6 = 2",
        
        ]
        example1 = MathTex(examples[0]).scale(0.8).next_to(title, DOWN, buff=1)
        example2 = MathTex(examples[1]).scale(0.8).next_to(example1, DOWN, aligned_edge=LEFT, buff=0.5)
        example3 = MathTex(examples[2]).scale(0.8).next_to(example2, DOWN, aligned_edge=LEFT, buff=0.5)
        example4 = MathTex(examples[3]).scale(0.8).next_to(example3, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(Write(example1))
        self.wait(1)
        self.play(Write(example2))
        self.wait(1)
        self.play(Write(example3))
        self.wait(1)
        self.play(Write(example4))
        self.wait(1)
 
        self.wait(3)

    def Introduction2(self):
        self.setNumberOfCirclePositions(2)
        self.isRandom = False


        p10 = cvo.CVO().CreateCVO("Whole Numbers", "")
        p11 = cvo.CVO().CreateCVO("Properties of Whole Numbers", "")
        p11.extendOname([ "Commutative property", "Associative property", "Additive identity"])
        p11.setcircleradius(2.0)
        p10.cvolist.append(p11)
        self.construct1(p10, p10)

    


    def Commutativeproperty(self):
        self.positionChoice = [[-4,-2,0],[4,-2,0],[-4,2,0],[4,2,0],[0,0,0]]
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Commutative for 2 Whole Numbers", "2 , 3 ")
        p11 = cvo.CVO().CreateCVO("Commutative  of addition", "2 + 3 = 3 + 2 = 5")
        p12 = cvo.CVO().CreateCVO("Commutative  of multiplication", "2 * 3 = 3 * 2 = 6")
        p13 = cvo.CVO().CreateCVO("Commutative of subtraction", "not possible")
        p14 = cvo.CVO().CreateCVO("Commutative of division", "not possible")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        self.construct1(p10, p10)
        self.fadeOutCurrentScene()

        title = Text("Commutative Property for Two Numbers 4,5").to_edge(UP)
        self.play(Write(title))

        examples = [
        r"\text{For Addition :} X + Y = Y + X \quad \text{example:}\quad 4+5=5+4==9",
        r"\text{For Subtraction :} X - Y = Y - X \quad \text{not possible}",
        r"\text{For Multiplication :} X * Y = Y * X \quad \text{example:}\quad 4*5=5*4==20",
        r"\text{For Division :} X / Y = Y / X \quad \text{not possible}",
       
        
        ]
        example1 = MathTex(examples[0]).scale(0.8).next_to(title, DOWN, buff=1)
        example2 = MathTex(examples[1]).scale(0.8).next_to(example1, DOWN, aligned_edge=LEFT, buff=0.5)
        example3 = MathTex(examples[2]).scale(0.8).next_to(example2, DOWN, aligned_edge=LEFT, buff=0.5)
        example4 = MathTex(examples[3]).scale(0.8).next_to(example3, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(Write(example1))
        self.wait(1)
        self.play(Write(example2))
        self.wait(1)
        self.play(Write(example3))
        self.wait(1)
        self.play(Write(example4))
        self.wait(1)
 
        self.wait(3)
    

    def Associativeproperty(self):
        self.positionChoice = [[-4,-2,0],[4,-2,0],[-4,2,0],[4,2,0],[0,0,0]]
        self.isRandom = False
        p10 = cvo.CVO().CreateCVO("Associative for 3 Whole Numbers", "2,3,4")
        p11 = cvo.CVO().CreateCVO("Associative for additiion", "(2 + 3) + 4 = 2 + (3 + 4) = 9")
        p12 = cvo.CVO().CreateCVO("Associative for subtraction", "not possible")
        p13 = cvo.CVO().CreateCVO("Associative for multiplication", "(2 * 3) * 4 = 2 * (3 * 4) = 24")
        p14 = cvo.CVO().CreateCVO("Associative for division","not possible")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        self.construct1(p10, p10)
        self.fadeOutCurrentScene()

        title = Text("Associative Property for Three Numbers 5,6,1").to_edge(UP)
        self.play(Write(title))

        examples = [
        r"\text{For Addition :} (X+Y)+Z=X+(Y+Z)",
        r"\text{example:} \quad (5+6)+1=5+(6+1)==12",
        r"\text{For Subtraction :} (X - Y) - Z = X - (Y - Z) \quad \text{not possible}",
        r"\text{For Multiplication :}(X*Y)*Z=X*(Y*Z)",
        r"\text{example:}\quad (5*6)*1=5*(6*1)==30",
        r"\text{For Division :}(X / Y) / Z = X / (Y / Z) \quad \text{not possible}",
       
        
        ]
        example1 = MathTex(examples[0]).scale(0.8).next_to(title, DOWN, buff=1)
        example2 = MathTex(examples[1]).scale(0.8).next_to(example1, DOWN, aligned_edge=LEFT, buff=0.5)
        example3 = MathTex(examples[2]).scale(0.8).next_to(example2, DOWN, aligned_edge=LEFT, buff=0.5)
        example4 = MathTex(examples[3]).scale(0.8).next_to(example3, DOWN, aligned_edge=LEFT, buff=0.5)
        example5 = MathTex(examples[4]).scale(0.8).next_to(example4, DOWN, aligned_edge=LEFT, buff=0.5)
        example6 = MathTex(examples[5]).scale(0.8).next_to(example5, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(Write(example1))
        self.wait(1)
        self.play(Write(example2))
        self.wait(1)
        self.play(Write(example3))
        self.wait(1)
        self.play(Write(example4))
        self.wait(1)
        self.play(Write(example5))
        self.wait(1)
        self.play(Write(example6))
        self.wait(1)
 
        self.wait(3)


    def Additiveidentity(self):
        self.setNumberOfCirclePositions(5)
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("Identity of Whole Numbers", "2,x(identity element)")
        p11 = cvo.CVO().CreateCVO(" Identity of addition", "2 + 0 = 2")
        p12 = cvo.CVO().CreateCVO(" Identity of subtraction", "not applicable")
        p13 = cvo.CVO().CreateCVO(" Identity of multiplication", "2 * 1 = 2")
        p14 = cvo.CVO().CreateCVO(" Identity of division", "not applicable")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        self.construct1(p10, p10)
        self.fadeOutCurrentScene()

        title = Text("Identity of Whole Numbers").to_edge(UP)
        self.play(Write(title))

        examples = [
        r"\text{For Addition :} X + 0 = X \quad \text{example:}\quad 3+0=3",
        r"\text{For Subtraction :} \quad \text{not possible}",
        r"\text{For Multiplication :} X * 1 = X\quad \text{example:}\quad 3*1=3",
        r"\text{For Division :} \quad \text{not possible}",
       
        
        ]
        example1 = MathTex(examples[0]).scale(0.8).next_to(title, DOWN, buff=1)
        example2 = MathTex(examples[1]).scale(0.8).next_to(example1, DOWN, aligned_edge=LEFT, buff=0.5)
        example3 = MathTex(examples[2]).scale(0.8).next_to(example2, DOWN, aligned_edge=LEFT, buff=0.5)
        example4 = MathTex(examples[3]).scale(0.8).next_to(example3, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(Write(example1))
        self.wait(1)
        self.play(Write(example2))
        self.wait(1)
        self.play(Write(example3))
        self.wait(1)
        self.play(Write(example4))
        self.wait(1)
 
        self.wait(3)
   
    def SetDeveloperList(self): 
       self.DeveloperList="Medha Masanam" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade6Chapter2Wholenumbers.py"
    
  
if __name__ == "__main__":
    scene = Grade6Chapter2Wholenumbers()
    scene.render()