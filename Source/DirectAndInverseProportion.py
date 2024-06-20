from manim import *
from AbstractAnim import AbstractAnim
import cvo


class DirectAndInverseProportion(AbstractAnim):

    def construct(self):
        self.RenderSkillbancLogo()
        self.Introduction()
        self.fadeOutCurrentScene()
        self.direct()
        self.fadeOutCurrentScene()
        self.direct_graph()
        self.fadeOutCurrentScene()
        self.inverse()
        self.fadeOutCurrentScene()
        self.inverse_graph()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()
     

    def Introduction(self):
        self.setNumberOfCirclePositions(2)
        self.angleChoice = [-TAU/4]
        self.isRandom = False
        p10 = cvo.CVO().CreateCVO("PROPORTIONS", "")
        p11 = cvo.CVO().CreateCVO("TYPES", "")
        p11.extendOname(["DIRECT", "INVERSE"])
        p11.setcircleradius(1.5)
        p10.cvolist.append(p11)
        self.construct1(p10, p10)

    def direct(self):
        self.setNumberOfCirclePositions(5)
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("DIRECT PROPORTION", "x/y=k \n and\n x=ky")
        p11 = cvo.CVO().CreateCVO("X variable", "4")
        p12 = cvo.CVO().CreateCVO("Y variable", "2")
        p14 = cvo.CVO().CreateCVO("K variable", "2")
        p13 = cvo.CVO().CreateCVO("Proportion\n", "x=ky => 4=2(2)")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p14)
        self.construct1(p10, p10)
        self.construct1(p13, p13)
        self.play(Create(CurvedArrow(p11.pos, p13.pos)), 
                  Create(CurvedArrow(p12.pos, p13.pos)), 
                  Create(CurvedArrow(p14.pos, p13.pos)))

    def direct_graph(self):
        axes = Axes(
            x_range=[0, 10, 1],  
            y_range=[0, 10, 1], 
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": np.arange(0, 11, 1)},
            y_axis_config={"numbers_to_include": np.arange(0, 11, 1)},
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        def direct_proportion(x):
            return 0.5 * x  # k = 0.5
        graph = axes.plot(direct_proportion, color=RED)
        dot = Dot(axes.c2p(0, 0), color=YELLOW)
        tracing_line = always_redraw(lambda: Line(axes.c2p(0, 0), dot.get_center(), color=YELLOW))
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(graph), run_time=2)
        self.play(MoveAlongPath(dot, graph), run_time=4, rate_func=linear)
        self.add(tracing_line)
        self.wait(2)

    def inverse(self):
        self.setNumberOfCirclePositions(5)
        self.isRandom = False

        p10 = cvo.CVO().CreateCVO("INVERSE PROPORTION", "x=k/y\n and\n xy=k")
        p11 = cvo.CVO().CreateCVO("X variable", "2")
        p12 = cvo.CVO().CreateCVO("Y variable", "2")
        p14 = cvo.CVO().CreateCVO("K variable", "4")
        p13 = cvo.CVO().CreateCVO("Proportion\n", "xy=k => 2(2)=4")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p14)
        self.construct1(p10, p10)
        self.construct1(p13, p13)
        self.play(Create(CurvedArrow(p11.pos, p13.pos)), 
                  Create(CurvedArrow(p12.pos, p13.pos)), 
                  Create(CurvedArrow(p14.pos, p13.pos)))  

    def inverse_graph(self):
        axes = Axes(
            x_range=[0.1, 10, 1],  
            y_range=[0.1, 10, 1],  
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": np.arange(1, 11, 1)},
            y_axis_config={"numbers_to_include": np.arange(1, 11, 1)},
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        def inverse_proportion(x):
            return 2 / x  # k = 2
        graph = axes.plot(inverse_proportion, color=RED)
        dot = Dot(axes.c2p(1, inverse_proportion(1)), color=YELLOW)
        tracing_line = always_redraw(lambda: Line(axes.c2p(1, 2), dot.get_center(), color=YELLOW))
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(graph), run_time=2)
        self.play(MoveAlongPath(dot, graph), run_time=4, rate_func=linear)
        self.add(tracing_line)
        self.wait(2)
        
    def SetDeveloperList(self): 
       self.DeveloperList="Snehith" 
    
    def SetSourceCodeFileName(self):
        self.SourceCodeFileName="DirectAndInverseProportion.py"

   

if __name__ == "__main__":
    scene = DirectAndInverseProportion()
    scene.render()
