from manim import *
from AbstractAnim import AbstractAnim
import cvo


class Progression(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        #self.definition()
        self.fadeOutCurrentScene()
        self.AP()
        self.fadeOutCurrentScene()
        self.generalform()
        self.fadeOutCurrentScene()
        self.nthterm()
        self.fadeOutCurrentScene()
        self.formula()
        self.fadeOutCurrentScene()
        self.example1()
        self.fadeOutCurrentScene()
        self.sum()
        self.fadeOutCurrentScene()
        self.example2()
        self.fadeOutCurrentScene()
        #self.definition1()
        self.fadeOutCurrentScene()
        self.GP()
        self.fadeOutCurrentScene()
        self.generalform1()
        self.fadeOutCurrentScene()
        self.nthterm1()
        self.fadeOutCurrentScene()
        self.example3()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        

        
    

    def Introduction(self):
        self.setNumberOfCirclePositions(3)
        self.angleChoice = [TAU/4,TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Progression","")
        p11=cvo.CVO().CreateCVO("Arithematic Progression", "")
        p12=cvo.CVO().CreateCVO("Geometric Progression", "")
        
        p11.setcircleradius(1.5)
        p12.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)

    # def definition(self):


    #     title = Text("Arithmetic Progression", font_size=48).set_color(BLUE)
    #     self.play(Write(title))
    #     self.wait(1)
    #     self.play(title.animate.to_edge(UP))

    #     # Define the text
    #     text = Text(
    #         "Arithmetic progression is a sequence of numbers in which each\n"
    #         "term, except the first term, is obtained by adding a fixed\n"
    #         "number to the preceding term.",
    #         font_size=30,
    #         line_spacing=1.5
    #     ).set_color(WHITE).move_to(ORIGIN)

    #     # Display the text
    #     self.play(Write(text))
    #     self.wait(2)
    
    

    def AP(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Arithemetic Progression","")
        p11=cvo.CVO().CreateCVO("General form","a,a+d,a+2d,a+3d.....")
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)


    def generalform(self):
        self.setNumberOfCirclePositions(3)
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("General Form","a,a+d,a+2d,a+3d.....")
        p11=cvo.CVO().CreateCVO("First term","a")
        p12=cvo.CVO().CreateCVO("Common difference","d")
        p10.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        
        self.construct1(p10,p10)


    def nthterm(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("n^{th} term  of  AP ","")
        p11=cvo.CVO().CreateCVO("Formula", "a_n=a_1+(n-1)d")
        p11.setcircleradius(1.5)
        p10.SetIsMathText(True)
        p11.SetIsMathText(True)
       
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)
     

    def formula(self):
        self.setNumberOfCirclePositions(5)
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("Formula", "a_n=a_1+(n-1)d")
        p11=cvo.CVO().CreateCVO("n^{th} term","a_n")
        p12=cvo.CVO().CreateCVO("First term","a_1")
        p13=cvo.CVO().CreateCVO("number of terms","n")
        p14=cvo.CVO().CreateCVO("Common difference ","d").setPosition([0,0,0])
        p10.SetIsMathText(True)
        p11.SetIsMathText(True)
        p12.SetIsMathText(True)
        p10.setcircleradius(1.5)
       
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        p10.cvolist.append(p14)
        self.construct1(p10,p10)
       
    def example1(self):

        title = Text("Finding the 11th Term of AP: 24, 20, 16, ...").to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Given information
        a_text = Tex(r"First term (a) = 24").shift(UP)
        d_text = Tex(r"Common difference (d) = 20 - 24 = -4").shift(DOWN)
        
        self.play(Write(a_text))
        self.wait(2)
        self.play(Write(d_text))
        self.wait(2)
        
        # Formula for nth term
        formula = Tex(r"The $n^{th}$ term of an AP is calculated by :").shift(UP)
        formula2 = Tex(r"$a_n = a + (n-1) \cdot d$").next_to(formula, DOWN)
        
        self.play(Transform(a_text, formula), Transform(d_text, formula2))
        self.wait(3)
        
        # Substituting n = 11
        substitution = Tex(r"To find the 11th term ($a_{11}$):").shift(UP)
        substitution2 = Tex(r"$a_{11} = 24 + (11-1) \cdot (-4)$").next_to(substitution, DOWN)
        
        self.play(Transform(a_text, substitution), Transform(d_text, substitution2))
        self.wait(3)
        
        # Simplifying
        
        simplifying1 = Tex(r"$a_{11} = 24 + 10 \cdot (-4)$").shift(UP)
        simplifying2 = Tex(r"$a_{11} = 24 - 40$").next_to(simplifying1, DOWN)
        simplifying3 = Tex(r"$a_{11} = -16$").next_to(simplifying2, DOWN)
        simplifying=Tex("Simplifying :").next_to(simplifying1,LEFT)
        FadeIn(simplifying)
        self.play( FadeIn(simplifying),Transform(a_text, simplifying1), Transform(d_text, simplifying2))
        self.wait(2)
        self.play( FadeOut(simplifying),Transform(a_text, Tex("Therefore").shift(UP)),Transform(d_text, simplifying3) )
        self.wait(2)
        
        self.play(FadeOut(a_text),FadeOut(d_text), FadeOut(title))

    def sum(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Sum of first n terms of AP ","")
        p11=cvo.CVO().CreateCVO("Formula", "s_n=n/2[2a+(n-1)d]")
        
        p11.SetIsMathText(True)
       
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def example2(self):
        title = Text("Sum of First 12 Terms in AP :110,150,200,250..").to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Given information
        a_text = Tex(r"First term (a) = 110").shift(UP)
        d_text = Tex(r"Common difference (d) = 150 - 110 = 40").shift(DOWN)
        
        self.play(Write(a_text))
        self.wait(2)
        self.play(Write(d_text))
        self.wait(2)

        # Formula for sum of first n terms
        formula = Tex(r"The sum $S_n$ of the first $n$ terms of an AP is calculated by:").shift(UP)
        formula2 = Tex(r"$S_n = \frac{n}{2} \times (2a + (n-1) \cdot d)$").next_to(formula, DOWN)
        #Transform(a_text, formula)
        self.play(Transform(a_text, formula),Transform(d_text, formula2))
        self.wait(3)
        
        # Substituting n = 12
        substitution = Tex(r"To find $S_{12}$:").shift(UP)
        substitution2 = Tex(r"$S_{12} = \frac{12}{2} \times (2 \times 110 + (12-1) \cdot 40)$").next_to(substitution, DOWN)
        
        self.play(Transform(a_text, substitution), Transform(d_text, substitution2))
        self.wait(3)
        
        # Simplifying
        simplifying1 = Tex(r"$S_{12} = 6 \times (220 + 11 \times 40)$").shift(UP)
        simplifying2 = Tex(r"$S_{12} = 6 \times (220 + 440)$").next_to(simplifying1, DOWN)
        simplifying3 = Tex(r"$S_{12} = 6 \times 660$").next_to(simplifying2, DOWN)
        simplifying4 = Tex(r"$S_{12} = 3960$").next_to(simplifying3, DOWN)

        simplifying=Tex("Simplifying :").next_to(simplifying1,LEFT)
        FadeIn(simplifying)
        
        self.play( FadeIn(simplifying),Transform(a_text, simplifying1), Transform(d_text, simplifying2))
        self.wait(2)
        self.play( FadeOut(simplifying),Transform(a_text, Tex("Therefore").shift(UP)),Transform(d_text, simplifying3),Transform(d_text, simplifying4) )
        self.wait(2)
        
        self.play(FadeOut(a_text), FadeOut(title))

    # def definition1(self):


    #     title = Text("Geometric Progression", font_size=48).set_color(BLUE)
    #     self.play(Write(title))
    #     self.wait(1)
    #     self.play(title.animate.to_edge(UP))

    #     # Define the text
    #     text = Text(
    #         "Geometric progression is a sequence of numbers in which we get \n"
    #         "each term except by multiplying or divinding a particular number \n"
    #         "to the previous term except the first term.",
    #         font_size=30,
    #         line_spacing=1.5
    #     ).set_color(WHITE).move_to(ORIGIN)

    #     # Display the text
    #     self.play(Write(text))
    #     self.wait(2)








    def GP(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Geometric Progression","")

        p11=cvo.CVO().CreateCVO("General form","a,ar,ar^2,ar^3....")
        p11.setcircleradius(1.5)
        p11.SetIsMathText(True)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def generalform1(self):
        self.setNumberOfCirclePositions(3)
        self.isRandom = False

        p10=cvo.CVO().CreateCVO("General Form","a,ar,ar^2,ar^3....")
        p11=cvo.CVO().CreateCVO("First term","a")
        p12=cvo.CVO().CreateCVO("Common ratio","r")
        p10.SetIsMathText(True)
        p10.setcircleradius(1.5)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        
        self.construct1(p10,p10)

    def nthterm1(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [TAU/4]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("n^{th} term of GP","")
        p11=cvo.CVO().CreateCVO("Formula", "a_n=a*r^{n-1}")
        p10.SetIsMathText(True)
        p11.SetIsMathText(True)
       
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)

    def example3(self):
        # Title
        title = Text("Finding the 20th Term of GP: 2, 4, 8, ...").to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Given information
        a_text = Tex(r"First term (a) = 2").shift(UP)
        r_text = Tex(r"Common ratio (r) = 4 / 2 = 2").shift(DOWN)
        
        self.play(Write(a_text))
        self.wait(2)
        self.play( Write(r_text))
        self.wait(2)
        
        # Formula for nth term
        formula = Tex(r"The $n^{th}$ term of a GP is calculated by:").shift(UP)
        formula2 = Tex(r"$a_n = a \cdot r^{(n-1)}$").next_to(formula, DOWN)
        
        self.play(Transform(a_text, formula), Transform(r_text, formula2))
        self.wait(3)
        
        # Substituting n = 20
        substitution = Tex(r"To find the 20th term ($a_{20}$):").shift(UP)
        substitution2 = Tex(r"$a_{20} = 2 \cdot 2^{(20-1)}$").next_to(substitution, DOWN)
        
        self.play(Transform(a_text, substitution), Transform(r_text, substitution2))
        self.wait(3)
        
        # Simplifying
        simplifying1 = Tex(r"$a_{20} = 2 \cdot 2^{19}$").shift(UP)
        simplifying2 = Tex(r"$a_{20} = 2^{20}$").next_to(simplifying1, DOWN)
        simplifying3 = Tex(r"$a_{20} = 1,048,576$").next_to(simplifying2, DOWN)

        simplifying=Tex("Simplifying :").next_to(simplifying1,LEFT)
        FadeIn(simplifying)
        self.play( FadeIn(simplifying),Transform(a_text, simplifying1), Transform(r_text, simplifying2))
        self.wait(2)
        self.play( FadeOut(simplifying),Transform(a_text, Tex("Therefore").shift(UP)),Transform(r_text, simplifying3) )
        self.wait(2)
        
        # Final result
        result = Tex(r"The 20th term of the GP is $1,048,576$").shift(DOWN)
        self.play(Transform(a_text, result))
        self.wait(2)
        
        self.play(FadeOut(a_text), FadeOut(title))

    def SetDeveloperList(self):  
        self.DeveloperList="Agraz Gopu"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade10Chapter6Progression.py"









if __name__ == "__main__":
     
     scene = Progression()
     scene.render()