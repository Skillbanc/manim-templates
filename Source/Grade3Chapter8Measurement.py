from manim import *
from AbstractAnim import AbstractAnim
import cvo

class Grade3Chapter8Measurement(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.fadeOutCurrentScene()
        self.c1c2()
        self.fadeOutCurrentScene()
        self.StandardInstruments()
        self.fadeOutCurrentScene()
        self.StandardWeights()
        self.fadeOutCurrentScene()
        self.StandardLiter()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

    def c1c2(self):
        self.isRandom = False
        self.positionChoice = [[-3, 0, 0], [3, 2, 0], [3, -2, 0]]
        p10 = cvo.CVO().CreateCVO("Measurements", "")
        p11 = cvo.CVO().CreateCVO("Standard Instruments", "Scale,""Tape")
        p12 = cvo.CVO().CreateCVO("Standard Weights", "Kilograms")

        p10.setcircleradius(1.25)
        p11.setcircleradius(1.25)
        p12.setcircleradius(1.25)

        p10.cvolist.append(p11)
        p10.cvolist.append(p12)

        self.construct1(p10, p10)
        self.wait(1)
        self.fadeOutCurrentScene()

    def StandardInstruments(self):
        sub_title1 = Text("Standard Instruments", font_size=29, color=PINK).to_edge(UP * 1)
        sub_title2 = Text("Thus, if all of us use the same instrument to measure length,", font_size=29).to_edge(UP * 2.75)
        sub_title3 = Text("there will be no difference in the measurements", font_size=29).to_edge(UP * 4)
        sub_title4 = Text("Standard instruments like Scale, Tape etc. are used to measure length", font_size=29).to_edge(UP * 6 + LEFT * 1)

        self.play(Write(sub_title1))
        self.wait(2)
        self.play(Write(sub_title2))
        self.wait(3)
        self.play(Write(sub_title3))
        self.wait(3)
        self.play(Write(sub_title4))
        self.wait(3)

        # Create a scale (ruler)
        scale_length = 10
        scale = VGroup()
        for i in range(scale_length + 1):
            if i % 5 == 0:
                tick_length = 0.3
                label = Text(str(i), font_size=24).next_to(Line(ORIGIN, UP * tick_length), DOWN)
                label.shift(RIGHT * i)
                scale.add(label)
            else:
                tick_length = 0.15
            tick = Line(ORIGIN, UP * tick_length).shift(RIGHT * i)
            scale.add(tick)

        scale.shift(LEFT * scale_length / 2)

        # Create a border for the scale
        scale_border = SurroundingRectangle(scale, color=WHITE)

        # Label for the scale
        scale_label = Text("Scale (Ruler)", font_size=24).next_to(scale_border, DOWN)

        # Create a measuring tape
        tape_length = 10
        tape_width = 0.5
        tape = Rectangle(width=tape_length, height=tape_width, color=YELLOW, fill_opacity=0.5)

        # Adding markings to the measuring tape
        tape_markings = VGroup()
        for i in range(tape_length + 1):
            if i % 5 == 0:
                tick_length = tape_width / 2
                label = Text(str(i), font_size=24).next_to(Line(UP * tape_width / 2, UP * (tape_width / 2 + tick_length)), UP)
                label.shift(RIGHT * i - RIGHT * tape_length / 2)
                tape_markings.add(label)
            else:
                tick_length = tape_width / 4
            tick = Line(UP * tape_width / 2, UP * (tape_width / 2 + tick_length)).shift(RIGHT * i - RIGHT * tape_length / 2)
            tape_markings.add(tick)

        # Position the tape below the scale
        tape.shift(DOWN * 2)
        tape_markings.shift(DOWN * 2)

        # Create a border for the measuring tape
        tape_border = SurroundingRectangle(tape, color=WHITE)

        # Label for the tape
        tape_label = Text("Measuring Tape", font_size=24).next_to(tape_border, DOWN)

        # Adjust positions to ensure visibility
        scale_label.shift(DOWN * 0)
        tape_label.shift(DOWN * 0)

        # Add the scale and tape to the scene
        self.play(Create(scale))
        self.play(Create(scale_border))
        self.play(Write(scale_label))
        self.wait(1)
        self.play(Create(tape))
        self.play(Create(tape_border))
        self.play(Write(tape_label))
        self.wait(1)
        self.play(Create(tape_markings))
        self.wait(1)

        self.play(FadeOut(sub_title1), FadeOut(sub_title2), FadeOut(sub_title3), FadeOut(sub_title4), FadeOut(scale), FadeOut(scale_border), FadeOut(scale_label), FadeOut(tape), FadeOut(tape_border), FadeOut(tape_label), FadeOut(tape_markings))

         # Define the table data
        table_data = [
            ["S. No.", "Name of Object", "Length"],
            ["1.", "Pen", "13cm"],
            ["2.", "Chalk", "7.62cm"],
            ["3.", "Eraser", "5cm"],
            ["4.", "Duster", "14cm"],
            ["5.", "Pencil", "18cm"]
        ]

        # # Create the table with the title
        # table = Table(
        #     table_data,
        #     include_outer_lines=True,
        #     h_buff=1,
        #     v_buff=0.4
        # )

        # # Position the table at the center of the scene
        # table.scale(0.6)
        # table.move_to(ORIGIN)

        # # Add the title
        # title = Text("Measure the objects given in the table using a scale.", font_size=24)
        # title.next_to(table, UP * 0.5)

        # # Play the title and table together
        # self.play(Write(title), Create(table.get_horizontal_lines()), Create(table.get_vertical_lines()))
        # self.wait(1)

        # # Sequentially play each cell in the table
        # for row in table.get_entries():
        #     for cell in row:
        #         self.play(FadeIn(cell))
        #         self.wait(0.5)

        # self.wait(2)



    def StandardWeights(self):
        sub_title1 = Text("Standard Weights", font_size=29, color=PURPLE).to_edge(UP * 1)
        sub_title2 = Text("Standard weights are precisely defined reference weights used ", font_size=29).to_edge(UP * 2.75)
        sub_title3 = Text("to ensure accurate and consistent measurements.", font_size=29).to_edge(UP * 4.25)

        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(2)
        self.play(Write(sub_title3))
        self.wait(3)

        # Create weight stones
        weights = VGroup()
        weights_data = [
            {"weight": "1kg", "position": LEFT * 5, "scale": 0.7},
            {"weight": "2kg", "position": LEFT * 3, "scale": 0.9},
            {"weight": "5kg", "position": ORIGIN, "scale": 1.20},
            {"weight": "10kg", "position": RIGHT * 3, "scale": 1.65},
        ]

        for data in weights_data:
            stone = Rectangle(width=1, height=1, color=BLUE, fill_opacity=0.7)
            label = Text(data["weight"], font_size=24).move_to(stone.get_center())
            weight_stone = VGroup(stone, label).move_to(data["position"])
            weight_stone.scale(data["scale"])  # Scale the weight stone according to its weight
            weights.add(weight_stone)

        self.play(Create(weights))
        self.wait(2)

        self.play(FadeOut(sub_title2), FadeOut(sub_title1), FadeOut(sub_title3), FadeOut(weights))


        # Define the table content
        table_data = [
            ["Articles to buy", "Weights used to weigh"],
            ["2 kg of tamarind", "2 kg"],
            ["1 kg of groundnut", "1 kg"],
            ["3 kg of sugar", "2 kg, 1 kg"],
            ["6 kg of onions", "5 kg, 1 kg"],
            ["7 kg of wheat flour", "5 kg, 2 kg"],
            ["13 kg of rice", "10 kg, 2 kg, 1 kg"]
        ]
        
        #Create the table with the title
        table = Table(
            table_data,
            include_outer_lines=True,
            h_buff=1,
            v_buff=0.4
        )
        # Position the table at the center of the scene
        table.scale(0.6)
        table.move_to(ORIGIN)

      # Play the title and table together
        self.play(Create(table.get_horizontal_lines()), Create(table.get_vertical_lines()))
        self.wait(1)

        # Sequentially play each cell in the table
        for row in table.get_entries():
            for cell in row:
                self.play(FadeIn(cell))
                self.wait(0.5)

        self.wait(2)


    def StandardLiter(self):
        sub_title1 = Text("What is a Litre?", font_size=29, color=DARK_BROWN).to_edge(UP * 1)
        sub_title2 = Text("The standard unit used to measure liquids is Litre. ", font_size=29).to_edge(UP * 2.75)
        sub_title3 = Text("Different shapes, equal capacity if same amount of liquid has been poured", font_size=29).to_edge(UP * 4.25 + LEFT * 1)

        self.play(Write(sub_title1))
        self.wait(2)
        self.play(Write(sub_title2))
        self.wait(3)
        self.play(Write(sub_title3))
        self.wait(2)

        p10 = cvo.CVO().CreateCVO("Liquids", "").setangle(-TAU / 5).setPosition([-3, -1, 0])
        p11 = cvo.CVO().CreateCVO("Measurement", "").setPosition([0, -1, 0])
        p12 = cvo.CVO().CreateCVO("Standard Units", "Litre").setPosition([3, -1, 0])

        p10.setcircleradius(1)
        p11.setcircleradius(1)
        p12.setcircleradius(1)

        p10.cvolist.append(p11)
        p11.cvolist.append(p12)

        self.construct1(p10, p10)
        self.wait(1)
        self.fadeOutCurrentScene()



    def SetDeveloperList(self):
        self.DeveloperList = "Bommi Yaswanth"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName = "Grade3Chapter8Measurement.py"

if __name__ == "__main__":
    from manim import *
    scene = Grade3Chapter8Measurement()
    scene.render()
