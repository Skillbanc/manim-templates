from manim import *
from AbstractAnim import AbstractAnim
import cvo

class SetOperations(AbstractAnim):
    def construct(self):
        self.isRandom=False
        self.positionChoice = [[-4,0,0],[4,2,0],[4,-2,0]]
        p10=cvo.CVO().CreateCVO("Prime Factorisation","Methods of Prime Factorisation").setangle(-TAU/5)
        p11=cvo.CVO().CreateCVO("","Division Method")
        p12=cvo.CVO().CreateCVO("","Factor Tree Method")

        p10.setcircleradius(1.25)
        p11.setcircleradius(1.25)
        p12.setcircleradius(1.25)
    
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)

        self.construct1(p10,p10)

if __name__ == "__main__":
    scene = SetOperations()
    scene.render()


    from manim import *
from AbstractAnim import AbstractAnim
import cvo

class SetOperations(AbstractAnim):
    def PrimeFactorization(self):
        self.show_factor_tree()
        self.wait(1)
        self.clear_screen()

        self.show_division_method()
        self.wait(1)
        self.clear_screen()
        
        self.isRandom=False
        self.positionChoice = [[-4,-2,0],[4,-2,0],[3,2,0],[-4,2,0]]
        p10=cvo.CVO().CreateCVO("Prime Factorisation","Methods of Prime Factorisation").setangle(-TAU/5)
        p11=cvo.CVO().CreateCVO("","Division Method")
        p12=cvo.CVO().CreateCVO("","Factor Tree Method")

        p10.setcircleradius(1.25)
        p11.setcircleradius(1.25)
        p12.setcircleradius(1.25)
    
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)

        self.construct1(p10,p10)

        def show_factor_tree(self):
            title = Text("Factor Tree").scale(0.6).to_edge(UP)
        
        lines = [
            "A factor tree breaks down a number into its prime factors.",
            "For example, the factor tree of 18:",]
        scene.clear_screen()
        lines = [
            "18",
            "/  \\",
            "2    9",
            "    / \\",
            "   3   3"
        ]
        self.show_concept(title, lines)

    def show_division_method(self):
        title = Text("Division Method").scale(0.6).to_edge(UP)
        lines = [
            "The division method finds the prime factors of a number by dividing it.",
            "For example, the division method for 18:",
            "18 ÷ 2 = 9",
            "9 ÷ 3 = 3",
            "3 ÷ 3 = 1",
            "So, the prime factors of 18 are 2 and 3."
        ]
        self.show_concept(title, lines)

if _name_ == "_main_":
    scene = SetOperations()
    scene.render()