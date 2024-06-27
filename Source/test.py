from manim import *

class MoveImageeee(Scene):
    def construct(self):
        
        union = Text("Estimating And Rounding Off Numbers ", color=DARK_BROWN, font_size=37).to_edge(UP*1)
        sub_title1 = Text("We usually round off the numbers to the nearest 10's(Tens),", font_size=29).to_edge(UP*3)
        sub_title2 = Text("100's(Hundreds), 1000's (Thousands), 10000's (Ten Thousands)... etc.", font_size=29).to_edge(UP*4.75)
        sub_title3 = Text("Rounding off the numbers to the nearest tens:", font_size=30, color=GREY).to_edge(UP*6.5+LEFT *1)
        sub_title4 = Text("82 is near to 80 than 90, and 87 is near to 90 than 80.", font_size=29).to_edge(UP*8)
        sub_title5 = Text("85 is at equal distance from 80 and 90.", font_size=29).to_edge(UP*9.5)
        
        self.play(Write(union))
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)
        self.play(Write(sub_title3))
        self.wait(1)
        self.play(Write(sub_title4))
        self.wait(1)
        self.play(Write(sub_title5))
        self.wait(1)

        # Create number line from 80 to 90 with slower playback speed
        number_line = NumberLine(
            x_range=[80, 90, 1],
            length=10,
            include_numbers=True,
            label_direction=UP
        ).to_edge(UP*12)

        # Create circles for the numbers to be rounded
        circle_82 = Circle(radius=0.5, color=BLUE).move_to(number_line.n2p(82) + UP * 0.3)
        circle_85 = Circle(radius=0.5, color=BLUE).move_to(number_line.n2p(85) + UP * 0.2)
        circle_87 = Circle(radius=0.5, color=BLUE).move_to(number_line.n2p(87) + UP * 0.3)

        # Create curved arrows for rounding off 82 to 80
        arrow_82_to_80 = ArcBetweenPoints(
            start=circle_82.get_center() + UP * 0.5,
            end=number_line.n2p(80),
            angle=TAU / 4,
            color=PINK
        ).add_tip(tip_length=0.2)

        # Create curved arrows for rounding off 87 to 90
        arrow_87_to_90 = ArcBetweenPoints(
            start=circle_87.get_center() + UP * 0.5,
            end=number_line.n2p(90),
            angle=-TAU / 4,
            color=PINK
        ).add_tip(tip_length=0.2)

        # Create curved arrows for rounding off 85 to 80 and 90 (pointing downwards)
        arrow_85_to_80 = ArcBetweenPoints(
            start=circle_85.get_center() + DOWN * 0.5,
            end=number_line.n2p(80),
            angle=-TAU / 4,
            color=PINK
        ).add_tip(tip_length=0.2)

        arrow_85_to_90 = ArcBetweenPoints(
            start=circle_85.get_center() + DOWN * 0.5,
            end=number_line.n2p(90),
            angle=TAU / 4,
            color=PINK
        ).add_tip(tip_length=0.2)

        # Add all elements to the scene with adjusted run_time
        self.play(Create(number_line), run_time=3)  # Adjust run_time as needed
        self.wait(1)
        self.play(Create(circle_82))
        self.play(Create(circle_85))
        self.play(Create(circle_87))
        self.wait(1)
        self.play(Create(arrow_82_to_80))
        self.wait(1)
        self.play(Create(arrow_87_to_90))
        self.wait(1)
        self.play(Create(arrow_85_to_80))
        self.play(Create(arrow_85_to_90))

        # Wait before ending the scene
        self.wait(2)

        # Fade out everything before ending the scene
        self.play(FadeOut(VGroup(union, sub_title1, sub_title2, sub_title3, sub_title4, sub_title5, 
                                 number_line, circle_82, circle_85, circle_87, 
                                 arrow_82_to_80, arrow_87_to_90, arrow_85_to_80, arrow_85_to_90)))

        self.wait(2)

    
     

        union = Text("Rounding off the numbers to nearest hundreds : ", color=ORANGE, font_size=31).to_edge(UP*1+LEFT*1)
        sub_title1 = Text("220 is nearer to 200 than 300, so 220 is rounded off to 200.", font_size=29).to_edge(UP*6)
        sub_title2 = Text("280 is nearer to 300 than 200, so it is rounded off to 300.", font_size=29).to_edge(UP*7.5)
        sub_title3 = MarkupText(
            "<span foreground='grey'>Compare the last digit:</span>   If the last digit is 5 or greater, we round up.",
            font_size=29
        ).to_edge(UP*9+LEFT *1)
        sub_title4 = Text("If it's less than 5, we round down.", font_size=29).to_edge(UP*10.5+LEFT*10)
        sub_title5 = Text("Since the tens digit(250) is exactly 5, we round up to the next hundred.", font_size=29).to_edge(UP*12)
        sub_title6 = Text("Therefore, 250 is rounded off to 300 ", font_size=29).to_edge(UP*13.5)


    # Create number line from 200 to 300
        number_line = NumberLine(
            x_range=[200, 300, 10],
            length=10,
            include_numbers=True,
            label_direction=UP
        ).to_edge(UP*3.5)  # Adjusted to fit well within the scene

        # Create circles for the numbers to be rounded
        circle_220 = Circle(radius=0.5, color=BLUE).move_to(number_line.n2p(220) + UP * 0.3)
        circle_280 = Circle(radius=0.5, color=BLUE).move_to(number_line.n2p(280) + UP * 0.3)

        # Create curved arrows for rounding off 220 to 200
        arrow_220_to_200 = ArcBetweenPoints(
            start=circle_220.get_center() + UP * 0.5,
            end=number_line.n2p(200),
            angle=TAU / 4,
            color=PINK
        ).add_tip(tip_length=0.2)

        # Create curved arrows for rounding off 280 to 300
        arrow_280_to_300 = ArcBetweenPoints(
            start=circle_280.get_center() + UP * 0.5,
            end=number_line.n2p(300),
            angle=-TAU / 4,
            color=PINK
        ).add_tip(tip_length=0.2)


        self.play(Write(union))

        # Add all elements to the scene with adjusted run_time
        self.play(Create(number_line), run_time=3)  # Adjust run_time as needed
        self.wait(1)
        self.play(Create(circle_220))
        self.play(Create(circle_280))
        self.wait(1)
        self.play(Create(arrow_220_to_200))
        self.wait(1)
        self.play(Create(arrow_280_to_300))

        # Wait before ending the scene
        self.wait(2)
        self.play(Write(sub_title1))
        self.wait(1)
        self.play(Write(sub_title2))
        self.wait(1)
        self.play(Write(sub_title3))
        self.wait(1)
        self.play(Write(sub_title4))
        self.wait(1)
        self.play(Write(sub_title5))
        self.wait(1)
        self.play(Write(sub_title6))
        self.wait(1)




        # Fade out everything before ending the scene
        self.play(*[FadeOut(mob) for mob in self.mobjects])


if __name__ == "__main__":
    scene = MoveImageeee()
    scene.render()
