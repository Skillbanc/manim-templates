from manim import *
from AbstractAnim import AbstractAnim
import cvo

class Lengths(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.length()
        self.fadeOutCurrentScene()
        self.metre()
        self.fadeOutCurrentScene()
        self.metric()
        self.fadeOutCurrentScene()
        self.units()
        self.fadeOutCurrentScene()
        self.inc()
        self.fadeOutCurrentScene()
        self.units1()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
        


    def length(self):
        self.isRandom = False
        self.positionChoice = [[-4,0,0],[2,2,0],[2,-2,0]]
        p10=cvo.CVO().CreateCVO("Length","")
        p11=cvo.CVO().CreateCVO("Metric Units", "")
        p11.extendOname(["Millimetre(mm)","Centimetre(cm)","Decimetre(dm)","Metre(m)","Decametre(dam)","Hectometre(hm)","Kilometre(km)"])
        p11.setcircleradius(1)
        p12=cvo.CVO().CreateCVO("Non-Metric Units", "")
        p12.extendOname(["Inches(in)","Foot(ft)"])
        p12.setcircleradius(1)
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)


    def metre(self):
        self.isRandom = False
        self.positionChoice = [[-4,-2,0],[0,1,0],[4.5,-2,0],[0,-2,0]]
        self.angleChoice=[TAU/4,TAU/4,-TAU/4]
        title=Title("Metric Conversions").to_edge(UP)
        self.play(Write(title))
        p10=cvo.CVO().CreateCVO("Kilometre","")
        p11=cvo.CVO().CreateCVO("Metre", "1km=1000m")
        p12=cvo.CVO().CreateCVO("Centimetre", "1m=100cm")
        p13=cvo.CVO().CreateCVO("Millimetre", "1cm=10mm")
        p10.cvolist.append(p11)
        p11.cvolist.append(p12)
        p12.cvolist.append(p13)
        self.construct1(p10,p10)

    def metric(self):
        title = Text("Metric Conversion")
        title.to_edge(UP)
        self.play(Write(title))

        # Metric units
        units = ["km", "hm", "dam", "m", "dm", "cm", "mm"]
        positions = [LEFT*6, LEFT*4, LEFT*2, ORIGIN, RIGHT*2, RIGHT*4, RIGHT*6]
        
        # Create unit labels
        unit_labels = [Text(unit).move_to(pos) for unit, pos in zip(units, positions)]
        for label in unit_labels:
            self.play(Write(label))
        
        # Create number 1 label above "km"
        one_label = Text("1").next_to(positions[0], UP*2)
        self.play(Write(one_label))

        # Create number 10 labels above the other units
        ten_labels = [Text("10").next_to(pos, UP*2) for pos in positions[1:]]
        for label in ten_labels:
            self.play(Write(label))

        # Create curved arrows for multiplication (pointing downwards)
        multiply_arrows = [
            CurvedArrow(start_point=positions[i], end_point=positions[i+1], angle=-TAU/4).shift(DOWN)
            for i in range(len(positions) - 1)
        ]
        for arrow in multiply_arrows:
            self.play(Create(arrow))

        multiply_text = Text("Multiply by 10").next_to(multiply_arrows[len(multiply_arrows) // 2], DOWN)
        self.play(Write(multiply_text))

      
        divide_text = Text("Divide by 10").next_to(title,DOWN)
        self.play(Write(divide_text))

        # Create curved arrows for division (pointing upwards)
        divide_arrows = [
            CurvedArrow(start_point=positions[i+1], end_point=positions[i], angle=TAU/4).shift(UP)
            for i in range(len(positions) - 1)
        ]
        for arrow in divide_arrows:
            self.play(Create(arrow))
        
    
        self.wait(4)
        

    def units(self):
        title1=Text("Conversions").to_edge(UP)
        km = MathTex(r"Kilometers (km) \quad 1km = 1000m").next_to(title1,DOWN*2)
        m = MathTex("Meters (m) \quad 1m = 100cm \quad = \\frac{1}{1000} km").next_to(km, DOWN, buff=0.5)
        cm = MathTex("Centimeters (cm) \quad 1cm = 10mm \quad = \\frac{1}{100} m").next_to(m, DOWN, buff=0.5)
        mm = MathTex("Millimeters (mm) \quad 1mm = \\frac{1}{10} cm").next_to(cm, DOWN, buff=0.5)

        self.play(Write(title1))
        self.play(Write(km))
        self.wait(1.5)
        self.play(Write(m))
        self.wait(1.5)
        self.play(Write(cm))
        self.wait(1.5)
        self.play(Write(mm))
        self.wait(1.5)
        self.play(FadeOut(km),FadeOut(m),FadeOut(cm),FadeOut(mm),FadeOut(title1))

        # Examples for each conversion
        title=Text("Examples").to_edge(UP)
        example_km_to_m = MathTex("(1) 1.7 km = 1.7 \\times 1000 = 1700 m").scale(0.7).next_to(title,DOWN, buff=0.2)
        example_m_to_km = MathTex("(2)9000 m = 9000 \\div 1000 = 9 km").scale(0.7).next_to(example_km_to_m, DOWN, buff=0.5)
        example_m_to_mm = MathTex("(3)11 m = 11 \\times 1000 = 11000 mm").scale(0.7).next_to(example_m_to_km, DOWN, buff=0.5)
        example_mm_to_m = MathTex("(4)7000 mm = 7000 \\div 1000 = 7 m").scale(0.7).next_to(example_m_to_mm, DOWN, buff=0.5)
        example_m_to_cm = MathTex("(5)7.2 m = 7.2 \\times 100 = 720 cm").scale(0.7).next_to(example_mm_to_m, DOWN, buff=0.5)
        example_cm_to_m = MathTex("(6)1300 cm = 1300 \\div 100 = 13 m").scale(0.7).next_to(example_m_to_cm, DOWN, buff=0.5)
        example_cm_to_mm = MathTex("(7)4.7 cm = 4.7 \\times 10 = 47 mm").scale(0.7).next_to(example_cm_to_m, DOWN, buff=0.5)
        example_mm_to_cm = MathTex("(8)2000 mm = 2000 \\div 10 = 200 cm").scale(0.7).next_to(example_cm_to_mm, DOWN, buff=0.5)

        # Animations
        # Conversion examples
        self.play(Write(title))
        self.play(Write(example_km_to_m))
        self.wait(2)
        self.play(Write(example_m_to_km))
        self.wait(2)
        self.play(Write(example_m_to_mm))
        self.wait(2)
        self.play(Write(example_mm_to_m))
        self.wait(2)
        self.play(Write(example_m_to_cm))
        self.wait(2)
        self.play(Write(example_cm_to_m))
        self.wait(2)
        self.play(Write(example_cm_to_mm))
        self.wait(2)
        self.play(Write(example_mm_to_cm))
        self.wait(3)


    def inc(self):
        self.setNumberOfCirclePositions(2)
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Length in inches","1 inch = 1/12 feet")
        p11=cvo.CVO().CreateCVO("Length in foot","1 foot = 12 inches")    
        p10.setcircleradius(2)
        p11.setcircleradius(2)
        p10.cvolist.append(p11) 
        self.construct1(p10, p10)


    def units1(self):
        title1=Text("Conversions").to_edge(UP)
        ft = MathTex("feet (') \quad 1ft = 12in ").next_to(title1,DOWN*2)
        iN = MathTex("Inches (\") \quad 1in = \\frac{1}{12}ft = 0.0833ft ").next_to(ft, DOWN*2, buff=0.5)
       
        self.play(Write(title1))
        self.play(Write(ft))
        self.wait(1.5)
        self.play(Write(iN))
        self.wait(1.5)
       
        self.play(FadeOut(title1),FadeOut(ft),FadeOut(iN))

        # Examples for each conversion
        title=Text("Examples").to_edge(UP)
        text=Text("Feet to Inches:",font_size=30).next_to(title,DOWN*2)
        example_ft_to_in = MathTex("(1) 3.2 ft = 3.2 \\times 12  = 38.4in").scale(0.7).next_to(text,DOWN, buff=0.5)
        text1=Text("Inches to Feet:",font_size=30).next_to(example_ft_to_in,DOWN*3)
        example_in_to_ft = MathTex("(2) 60 in = 60 \\div 12 = 5ft").scale(0.7).next_to(text1, DOWN, buff=0.5)
       
        # Animations
        # Conversion examples
        self.play(Write(title))
        self.play(Write(text))
        self.wait(1)
        self.play(Write(example_ft_to_in))
        self.wait(2)
        self.play(Write(text1))
        self.wait(1)
        self.play(Write(example_in_to_ft))
        self.wait(2)


    def SetDeveloperList(self):  
        self.DeveloperList="Gayathri Veeramreddy"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Grade5Chapter4Lengths.py"

if __name__ == "__main__":
    scene = Lengths()
    scene.render() 