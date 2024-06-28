from manim import *
from AbstractAnim import AbstractAnim
import cvo

class SmartTables1(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.theory()
        self.bar()
        self.Tables()
        self.GithubSourceCodeReference()

    def theory(self):

        Title=Text("Smart Tables").to_corner(UP)
        s_title =Text("It helps us to Organise and Group the Data").next_to(Title,DOWN).scale(0.5)
        s_title1 = Text("we can represent given data in tw0 ways").next_to(s_title,DOWN).scale(0.5)
        s_title3 = Text("1.Bar Chart").scale(0.6).move_to(DOWN)
        s_title2 =Text("2.Tally marks").scale(0.6).next_to(s_title3,DOWN)

        self.play(Write(Title),Write(s_title),Write(s_title1),Write(s_title3),Write(s_title2))
        self.wait(2)
        self.fadeOutCurrentScene()

    def bar(self):
        bar_graph_title = Text("Bar Graph Example", font_size=36)
        self.play(Write(bar_graph_title))
        self.wait(2)
        self.play(bar_graph_title.animate.to_edge(UP))
        
        years = ["2008", "2009", "2010", "2011", "2012"]
        production = [400, 500, 300, 600, 500]
        
        bars = BarChart(
            values=production,
            bar_names=years,
            y_range=[0, 700, 100],
            y_length=6,
            x_length=10,
            x_axis_config={"label_constructor": Text, "font_size": 24},
            y_axis_config={"label_constructor": Text, "font_size": 24},
            bar_colors=[BLUE, GREEN, RED, PURPLE, ORANGE]
        )
        self.play(Create(bars))
        self.wait(2)
        self.play(FadeOut(bars))
        self.play(FadeOut(bar_graph_title))

    def Tables(self):
        Title=Text("Tally Marks").to_corner(UP)
        data = [
            ["1", "|", "6", "卌 |"],
            ["2", "||", "7", "卌 ||"],
            ["3", "|||", "8", "卌 |||"],
            ["4", "||||", "9", "卌 ||||"],
            ["5", "卌 ", "10", "卌 卌 "],
        ]

        # Create MathTable
        table = Table(
            data,
            include_outer_lines=True,
            line_config={"color": WHITE}
        ).scale(0.8)

        # Animate the table creation
        self.play(Write(Title),Create(table))
        self.wait(2)
        self.fadeOutCurrentScene()

    def SetDeveloperList(self):
        self.DeveloperList="Bhaskar"

    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="SimpleTables.py"

if __name__ == "__main__":
    scene = SmartTables1()
    scene.render()

