from manim import *
from AbstractAnim import AbstractAnim
import cvo

class Numbers(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.method()
        self.fadeOutCurrentScene()
        self.beads_method()
        self.fadeOutCurrentScene()
        self.number_line_method()
        self.fadeOutCurrentScene()
        self.NumberLine1()
        self.fadeOutCurrentScene()
        self.NumberLine2()
        self.fadeOutCurrentScene()
        self.expansion()
        self.fadeOutCurrentScene()
        self.place()
        self.fadeOutCurrentScene()
        self.names()
        self.fadeOutCurrentScene()
        self.compare()
        self.fadeOutCurrentScene()
        
        self.GithubSourceCodeReference()

    def method(self):
        self.isRandom = False
        self.positionChoice = [[-4,-2,0],[2,2,0],[4,-1,0]]
        p10=cvo.CVO().CreateCVO("Identifying Numbers","")
        p11=cvo.CVO().CreateCVO("Beads Chain Method", "")
        p12=cvo.CVO().CreateCVO("Numberline Method", "")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        self.construct1(p10,p10)

    def create_bead(self, position, color):
        """Creates a single bead."""
        return Circle(radius=0.1, fill_opacity=1, fill_color=color).move_to(position)

    def tie_tag(self, bead_index, text, color=YELLOW):
        """Creates a square box with a number inside it below the specified bead and attaches a line."""
        bead_position = LEFT * 6 + RIGHT * 0.4 * (bead_index - 1)  # Adjust index to match the bead position
        box = Square(side_length=0.5, fill_opacity=1, fill_color=color, color=color)
        number = Text(str(text), font_size=20, color=BLACK)
        number.move_to(box.get_center())
        box_group = VGroup(box, number).next_to(bead_position, DOWN * 2)

        # Draw a line from the bead to the center of the box
        line = Line(start=bead_position, end=box_group.get_top(), color=color)
        
        return VGroup(box_group, line)

    def beads_method(self):
        """Creates and displays a beads chain with numbers in boxes under specific beads."""
        # Title
        title = Text("Identifying Numbers Using Beads Chain", font_size=36).to_edge(UP)
        ex=Text("Example: 10,14,25,27",font_size=30).next_to(title,DOWN)
        self.play(Write(title))
        self.play(Write(ex))
        self.wait(1)

        # Beads chain
        num_beads = 30
        beads = VGroup()
        colors = [BLUE, RED]  # Alternating colors
        
        for i in range(num_beads):
            color = colors[i // 10 % 2]  # Change color every 10 beads
            bead = self.create_bead(LEFT * 6 + RIGHT * 0.4 * i, color)
            beads.add(bead)
        
        self.play(FadeIn(beads))
        
        # Initial tags at 10 and 25
        tags_positions = [10, 25]
        initial_tags = VGroup(*[self.tie_tag(i, i) for i in tags_positions])
        self.play(FadeIn(initial_tags))
        
        # Additional tags at 14 and 27
        extra_tags_positions = [14, 27]
        extra_tags = VGroup(*[self.tie_tag(i, i, color=GREEN) for i in extra_tags_positions])
        self.play(FadeIn(extra_tags))

        self.wait(4)

        # Fade out all elements
        self.play(FadeOut(beads), FadeOut(initial_tags), FadeOut(extra_tags), FadeOut(title),FadeOut(ex))

    def number_line_method(self):
        # Number Line Method
        title = Text("Identifying Numbers Using a Number Line", font_size=48).to_edge(UP)
        ex=Text("Example: To represent 6 on a numerline",font_size=35).next_to(title,DOWN)
        self.play(Write(title))
        self.play(Write(ex))
        self.wait(1)
        # Draw number line
        number_line = NumberLine(x_range=[0, 10, 1], length=10, include_numbers=True)
        self.play(Create(number_line))
        
        # Place point on number line
        point = Dot().move_to(number_line.n2p(6))
        label = Text("6", font_size=24).next_to(point, UP)
        self.play(FadeIn(point), Write(label))
        
        # Highlight the interval
        interval = Line(number_line.n2p(0), number_line.n2p(6), color=BLUE, stroke_width=4)
        self.play(Create(interval))
        self.wait(2)
        
        self.play(FadeOut(interval), FadeOut(point), FadeOut(label), FadeOut(number_line),(FadeOut(title)),FadeOut(ex))

    def create_number_line(self, start, end, step, unit_size, x_shift=0):
        """Creates a number line from start to end with a given step and unit size."""
        number_line = NumberLine(
            x_range=[start, end, step],
            length=10 * unit_size,
            include_numbers=True,
            include_tip=True,
            label_direction=DOWN,
            tick_size=0.1,
            numbers_to_include=np.arange(start, end + step, step),
        ).shift(RIGHT * x_shift)
        
        return number_line

    def add_mark(self, number_line, number, color=YELLOW):
        """Adds a small dot and label to mark a specific number on the number line."""
        dot = Dot(point=number_line.n2p(number), color=color)
        number_label = Text(str(number), font_size=24, color=color)
        number_label.next_to(dot, UP)
        return VGroup(dot, number_label)

    def animate_number_line(self, number_line, marks):
        """Animates the creation of a number line and its labels."""
        self.play(Create(number_line))
        for mark in marks:
            self.play(FadeIn(mark))

    def NumberLine1(self):
        # Create number line
        number_line = self.create_number_line(0, 100, 10, 1)  # End value is 100 for 0,10,20,...,100

        # Add specific marks
        mark_12 = self.add_mark(number_line, 12, color=BLUE)
        mark_25 = self.add_mark(number_line, 25, color=RED)
        mark_37 = self.add_mark(number_line, 37, color=GREEN)

        # Title
        title = Text("Representing Numbers more than 10 on a Number Line", font_size=36).to_edge(UP)
        self.play(Write(title))
        text=Text("Example: To Represent 12,25,37",font_size=28).next_to(title,DOWN)
        self.play(Write(text))
        self.wait(1)


        # Animate number line and marks one after the other
        self.animate_number_line(number_line, [mark_12, mark_25, mark_37])

        self.wait(4)

        # Fade out all elements
        self.play(FadeOut(number_line), FadeOut(mark_12), FadeOut(mark_25), FadeOut(mark_37), FadeOut(text), FadeOut(title))

    def create_number_line(self, start, end, step, unit_size, x_shift=0):
        """Creates a number line from start to end with a given step and unit size."""
        number_line = NumberLine(
            x_range=[start, end, step],
            length=10 * unit_size,
            include_numbers=True,
            include_tip=True,
            label_direction=DOWN,
            tick_size=0.1,
            numbers_to_include=np.arange(start, end + step, step),
        ).shift(RIGHT * x_shift)
        
        return number_line

    def add_mark(self, number_line, number, color=YELLOW):
        """Adds a small dot and label to mark a specific number on the number line."""
        dot = Dot(point=number_line.n2p(number), color=color)
        number_label = Text(str(number), font_size=24, color=color)
        number_label.next_to(dot, UP)
        return VGroup(dot, number_label)

    def animate_number_line(self, number_line, marks):
        """Animates the creation of a number line and its labels."""
        self.play(Create(number_line))
        for mark in marks:
            self.play(FadeIn(mark))

    def NumberLine2(self):
        # Create number line
        number_line = self.create_number_line(0, 1000, 100, 1)  # Adjusted for 0 to 1000 with steps of 100

        # Add specific marks
        mark_50 = self.add_mark(number_line, 50, color=BLUE)
        mark_320 = self.add_mark(number_line, 320, color=RED)
        mark_780 = self.add_mark(number_line, 780, color=GREEN)

        # Title
        title = Text("Representing Numbers more than 100 on a Number Line", font_size=36).to_edge(UP)
        self.play(Write(title))
        text=Text("Example: To Represent 50,320,780",font_size=28).next_to(title,DOWN)
        self.play(Write(text))
        self.wait(1)

        # Animate number line and marks one after the other
        self.animate_number_line(number_line, [mark_50, mark_320, mark_780])

        self.wait(4)

        # Fade out all elements
        self.play(FadeOut(number_line), FadeOut(mark_50), FadeOut(mark_320), FadeOut(mark_780), FadeOut(text), FadeOut(title))

    def expansion(self):
        self.isRandom = False
        self.positionChoice = [[-4,-2,0],[0,-2,0],[-3,2,0],[3,0.5,0]]
        p10=cvo.CVO().CreateCVO("Number","399")
        p11=cvo.CVO().CreateCVO("Expanded form", "300 + 90 + 9")
        p12=cvo.CVO().CreateCVO("Expanded form", "3*100 + 9*10 + 9*1")
        p13=cvo.CVO().CreateCVO("Expanded form", "3 hundreds + 9 tens + 9 ones")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.construct1(p10,p10)
    
    def place(self):
        title = Text("Understanding Place Value",font_size=40).to_edge(UP)
        self.play(Write(title))
    
        number = Text("3482", font_size=64).next_to(title,DOWN*2)
        breakdown = VGroup(
            MathTex("3000 \quad \\implies Thousands", font_size=48),
            MathTex("400 \quad \\implies Hundreds", font_size=48),
            MathTex("80 \quad \\implies Tens", font_size=48),
            MathTex("2 \quad \\implies Ones", font_size=48),
        ).arrange(DOWN).next_to(number,DOWN*2)

        self.play(Write(number))
        self.wait(1)
        self.play(Write(breakdown))
        self.wait(2)
        self.play(FadeOut(breakdown),FadeOut(number),FadeOut(title))

    def names(self):
        self.setNumberOfCirclePositions(2)
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Number","127")
        p11=cvo.CVO().CreateCVO("Number Name","one hundred and twenty seven")
        p11.setcircleradius(2)
        p10.cvolist.append(p11)
        self.construct1(p10,p10)
        

    def compare(self):
        title = Text("Comparing Numbers",font_size=45).to_edge(UP)
        self.play(Write(title))

        num1 = Text("563", font_size=64).shift(LEFT*2)
        num2 = Text("475", font_size=64).shift(RIGHT*2)
        comparison = Text(">", font_size=64).next_to(num1, RIGHT*3)
        text=Text("563 is greater than 475",font_size=35).next_to(num1,DOWN*3)

        self.play(Write(num1), Write(num2))
        self.wait(1)
        self.play(Write(comparison))
        self.wait(1)
        self.play(Write(text))
        self.wait(1)
        self.play(FadeOut(num1), FadeOut(num2), FadeOut(comparison),FadeOut(title),FadeOut(text))

    def SetDeveloperList(self):  
        self.DeveloperList="Gayathri Veeramreddy"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="Numbers.py"

 

if __name__ == "__main__":
    scene = Numbers()
    scene.render() 