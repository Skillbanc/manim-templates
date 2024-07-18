import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class DataHandling(AbstractAnim):
    def construct(self):
       self.RenderSkillbancLogo()
       self.Data()
       self.fadeOutCurrentScene()
       self.Table()
       self.fadeOutCurrentScene()
       self.Q1()
       self.fadeOutCurrentScene()
       self.Q2()
       self.fadeOutCurrentScene()
       self.Q3()
       self.fadeOutCurrentScene()
       self.Example()
       self.fadeOutCurrentScene()
       self.Question1()
       self.fadeOutCurrentScene()
       self.Question2()
       self.fadeOutCurrentScene()
       self.Question3()
       self.fadeOutCurrentScene()
       self.Question4()
       self.fadeOutCurrentScene()
       self.Question5()
       self.fadeOutCurrentScene()
       self.Question6()
       self.fadeOutCurrentScene()
       self.GithubSourceCodeReference()
             
  
    def Data(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Data Handling ","").setPosition([-3,0,0])
        p11=cvo.CVO().CreateCVO("Representation of Data", "").setPosition([3,0,0])
        p10.cvolist.append(p11)
        self.construct1(p10,p10)  

    def Table(self):
        text = Text("Example 1", color=YELLOW).scale(0.9)
        text.center()
        text.to_edge(UP)
        self.play(Write(text))

        circles = [Circle(radius=0.4, color=BLUE, fill_opacity =0.5) for _ in range(5)]
        squares = [Square(side_length=0.8, color=GREEN,fill_opacity =0.5) for _ in range(3)]
        triangles = [Polygon(
            np.array([0, 0.4, 0]), 
            np.array([-0.4, -0.4, 0]), 
            np.array([0.4, -0.4, 0]),
            color=RED,fill_opacity =0.5
        ) for _ in range(6)]
        stars = [Star(n=5, outer_radius=0.4, color=PURPLE,fill_opacity =0.5) for _ in range(7)]

        circ =VGroup(*circles).arrange_in_grid(cols=5, buff=0.3)
        sq = VGroup(*squares).arrange_in_grid(cols=3, buff=0.3)
        tri = VGroup(*triangles).arrange_in_grid(cols=6, buff=0.3)
        star = VGroup(*stars).arrange_in_grid(cols=7, buff=0.3)
        circ.center()
        circ.shift(UP )
        sq.center()
        sq.shift(DOWN * 0.5)
        tri.center()
        tri.shift(DOWN * 1.7)
        star.center()
        star.shift(DOWN *3)
        circ_title = Text("Circle").scale(0.7)
        sq_title = Text("Square").scale(0.7)
        tri_title = Text("Triangle").scale(0.7)
        star_title = Text("Star").scale(0.7)
        circ_title.center()
        sq_title.center()
        tri_title.center()
        star_title.center()
        circ_title.shift(UP,LEFT * 5.4)
        sq_title.shift(DOWN *0.4,LEFT * 5.4)
        tri_title.shift(DOWN * 1.7,LEFT * 5.4)
        star_title.shift(DOWN * 2.9,LEFT * 5.4)
        title=Text("Shapes").scale(0.7)
        title.center()
        title.shift(UP * 2.1,LEFT * 5.4)
        title2=Text("No. of  Shapes").scale(0.7)
        title2.center()
        title2.shift(UP * 2.1,RIGHT )

        start_point = np.array([0,2.5, 0])
        end_point = np.array([0,-3.7, 0])
        horizontal_line = Line(start=LEFT*7, end=RIGHT*5, color=WHITE, stroke_width=4)
        horizontal_line.shift(UP *1.7)
        h2 = Line(start=LEFT*7, end=RIGHT*5, color=WHITE, stroke_width=4)
        h2.shift(UP *2.5)
        vertical_line = Line(start=start_point, end=end_point, color=WHITE, stroke_width=4)
        vertical_line.shift(LEFT * 4)
        v2 = Line(start=start_point, end=end_point, color=WHITE, stroke_width=4)
        v2.shift(LEFT * 7)
        v3= Line(start=start_point, end=end_point, color=WHITE, stroke_width=4)
        v3.shift(RIGHT * 5)
        h3 = Line(start=LEFT*7, end=RIGHT*5, color=WHITE, stroke_width=4)
        h3.shift(DOWN * 3.7)

        self.play(Create(vertical_line),Create(horizontal_line),Create(h2),Create(v2),Create(v3),Create(h3))
        self.play(Write(title),Write(title2))
        self.play(Write(circ_title),Write(sq_title),Write(tri_title),Write(star_title),)
        self.play(Write(circ))
        self.play(Write(sq))
        self.play(Write(tri))
        self.play(Write(star))

        self.wait(7)

    def Q1(self):
        text = Text("Question and Answers", color=RED_C).scale(0.7)
        text.center()
        text.shift(UP * 3.6)
        self.play(Write(text))
        text2 =Text("(a). Which Shape is more in number the following table?",color=GREEN_C).scale(0.6)
        text2.center()
        text2.shift(UP * 2.9,LEFT)
        self.play(Write(text2))
        text3 =Text("Ans. Star - 7",color=PURPLE_A).scale(0.6)
        text3.center()
        text3.shift(UP * 2,LEFT * 5)
       
      
        circles = [Circle(radius=0.4, color=BLUE, fill_opacity =0.5) for _ in range(5)]
        squares = [Square(side_length=0.8, color=GREEN,fill_opacity =0.5) for _ in range(3)]
        triangles = [Polygon(
            np.array([0, 0.4, 0]), 
            np.array([-0.4, -0.4, 0]), 
            np.array([0.4, -0.4, 0]),
            color=RED,fill_opacity =0.5
        ) for _ in range(6)]
        stars = [Star(n=5, outer_radius=0.4, color=PURPLE,fill_opacity =0.5) for _ in range(7)]

        circ =VGroup(*circles).arrange_in_grid(cols=5, buff=0.3)
        sq = VGroup(*squares).arrange_in_grid(cols=3, buff=0.3)
        tri = VGroup(*triangles).arrange_in_grid(cols=6, buff=0.3)
        star = VGroup(*stars).arrange_in_grid(cols=7, buff=0.3)
        circ.center()
        circ.shift(UP )
        sq.center()
        sq.shift(DOWN * 0.5)
        tri.center()
        tri.shift(DOWN * 1.7)
        star.center()
        star.shift(DOWN *3)
        circ_title = Text("Circle").scale(0.7)
        sq_title = Text("Square").scale(0.7)
        tri_title = Text("Triangle").scale(0.7)
        star_title = Text("Star").scale(0.7)
        circ_title.center()
        sq_title.center()
        tri_title.center()
        star_title.center()
        circ_title.shift(UP,LEFT * 5.4)
        sq_title.shift(DOWN *0.4,LEFT * 5.4)
        tri_title.shift(DOWN * 1.7,LEFT * 5.4)
        star_title.shift(DOWN * 2.9,LEFT * 5.4)
        title=Text("Shapes").scale(0.7)
        title.center()
        title.shift(UP * 2.1,LEFT * 5.4)
        title2=Text("No. of  Shapes").scale(0.7)
        title2.center()
        title2.shift(UP * 2.1,RIGHT )

        start_point = np.array([0,2.5, 0])
        end_point = np.array([0,-3.7, 0])
        horizontal_line = Line(start=LEFT*7, end=RIGHT*5, color=WHITE, stroke_width=4)
        horizontal_line.shift(UP *1.7)
        h2 = Line(start=LEFT*7, end=RIGHT*5, color=WHITE, stroke_width=4)
        h2.shift(UP *2.5)
        vertical_line = Line(start=start_point, end=end_point, color=WHITE, stroke_width=4)
        vertical_line.shift(LEFT * 4)
        v2 = Line(start=start_point, end=end_point, color=WHITE, stroke_width=4)
        v2.shift(LEFT * 7)
        v3= Line(start=start_point, end=end_point, color=WHITE, stroke_width=4)
        v3.shift(RIGHT * 5)
        h3 = Line(start=LEFT*7, end=RIGHT*5, color=WHITE, stroke_width=4)
        h3.shift(DOWN * 3.7)
        group = VGroup(vertical_line, horizontal_line,h2,v2,v3,h3)
        group2= VGroup(title,title2,circ_title,sq_title,tri_title,star_title,circ,tri ,sq,star)
        group.scale(0.8)
        group2.scale(0.8)
        group.shift(DOWN * 0.5)
        group2.shift(DOWN * 0.5)
        self.add(group)
        self.add(group2)
        self.wait(5)
        rect2 = Rectangle(width=7.2, height=1, color= LIGHT_PINK ,fill_opacity =0.5)
        self.add(rect2)
        rect2.shift(DOWN * 3 , RIGHT * 0.2)
        star_large = star.copy().scale(1.2).set_color(YELLOW)
        star_large.move_to(star.get_center())
        self.play(Write(text3))
        self.play(Transform(star, star_large))
        self.wait(1)

        # Zoom out the star group
        self.play(Transform(star, star.copy().scale(1/1.5).set_color(PURPLE)))
        self.wait(3)
 
    def Q2(self):
        text = Text("(b).Which Shape is more in number - Circle or Triangle?", color=GREEN_C).scale(0.6)
        text.center()
        text.shift(UP * 2.9,LEFT)
        self.play(Write(text))
        text3 =Text("Ans. Triangle - 6",color=PURPLE_A).scale(0.6)
        text3.center()
        text3.shift(UP * 2,LEFT * 5)
       
      
        circles = [Circle(radius=0.4, color=BLUE, fill_opacity =0.5) for _ in range(5)]
        squares = [Square(side_length=0.8, color=GREEN,fill_opacity =0.5) for _ in range(3)]
        triangles = [Polygon(
            np.array([0, 0.4, 0]), 
            np.array([-0.4, -0.4, 0]), 
            np.array([0.4, -0.4, 0]),
            color=RED,fill_opacity =0.5
        ) for _ in range(6)]
        stars = [Star(n=5, outer_radius=0.4, color=PURPLE,fill_opacity =0.5) for _ in range(7)]

        circ =VGroup(*circles).arrange_in_grid(cols=5, buff=0.3)
        sq = VGroup(*squares).arrange_in_grid(cols=3, buff=0.3)
        tri = VGroup(*triangles).arrange_in_grid(cols=6, buff=0.3)
        star = VGroup(*stars).arrange_in_grid(cols=7, buff=0.3)
        circ.center()
        circ.shift(UP )
        sq.center()
        sq.shift(DOWN * 0.5)
        tri.center()
        tri.shift(DOWN * 1.7)
        star.center()
        star.shift(DOWN *3)
        circ_title = Text("Circle").scale(0.7)
        sq_title = Text("Square").scale(0.7)
        tri_title = Text("Triangle").scale(0.7)
        star_title = Text("Star").scale(0.7)
        circ_title.center()
        sq_title.center()
        tri_title.center()
        star_title.center()
        circ_title.shift(UP,LEFT * 5.4)
        sq_title.shift(DOWN *0.4,LEFT * 5.4)
        tri_title.shift(DOWN * 1.7,LEFT * 5.4)
        star_title.shift(DOWN * 2.9,LEFT * 5.4)
        title=Text("Shapes").scale(0.7)
        title.center()
        title.shift(UP * 2.1,LEFT * 5.4)
        title2=Text("No. of  Shapes").scale(0.7)
        title2.center()
        title2.shift(UP * 2.1,RIGHT )

        start_point = np.array([0,2.5, 0])
        end_point = np.array([0,-3.7, 0])
        horizontal_line = Line(start=LEFT*7, end=RIGHT*5, color=WHITE, stroke_width=4)
        horizontal_line.shift(UP *1.7)
        h2 = Line(start=LEFT*7, end=RIGHT*5, color=WHITE, stroke_width=4)
        h2.shift(UP *2.5)
        vertical_line = Line(start=start_point, end=end_point, color=WHITE, stroke_width=4)
        vertical_line.shift(LEFT * 4)
        v2 = Line(start=start_point, end=end_point, color=WHITE, stroke_width=4)
        v2.shift(LEFT * 7)
        v3= Line(start=start_point, end=end_point, color=WHITE, stroke_width=4)
        v3.shift(RIGHT * 5)
        h3 = Line(start=LEFT*7, end=RIGHT*5, color=WHITE, stroke_width=4)
        h3.shift(DOWN * 3.7)
        group = VGroup(vertical_line, horizontal_line,h2,v2,v3,h3)
        group2= VGroup(title,title2,circ_title,sq_title,tri_title,star_title,circ,tri ,sq,star)
        group.scale(0.8)
        group2.scale(0.8)
        group.shift(DOWN * 0.5)
        group2.shift(DOWN * 0.5)
        self.add(group)
        self.add(group2)
        self.wait(5)
        rect2 = Rectangle(width=7.2, height=1, color= LIGHT_PINK ,fill_opacity =0.5)
        self.add(rect2)
        rect2.shift(DOWN * 2, RIGHT * 0.2)
        star_large = tri.copy().scale(1.2).set_color(YELLOW)
        star_large.move_to(tri.get_center())
        self.play(Write(text3))
        self.play(Transform(tri, star_large))
        self.wait(1)

        # Zoom out the star group
        self.play(Transform(tri, tri.copy().scale(1/1.5).set_color(ORANGE)))
        self.wait(3)

    def Q3(self): 

        text3 =Text("(c). Which shape is the least in number?", color=GREEN_C).scale(0.6)
        text3.center()
        text3.shift(UP * 2.9,LEFT * 2)
        self.play(Write(text3))
        text3 =Text("Ans. Square - 3",color=PURPLE_A).scale(0.6)
        text3.center()
        text3.shift(UP * 2,LEFT * 4.3)
       
      
        circles = [Circle(radius=0.4, color=BLUE, fill_opacity =0.5) for _ in range(5)]
        squares = [Square(side_length=0.8, color=GREEN,fill_opacity =0.5) for _ in range(3)]
        triangles = [Polygon(
            np.array([0, 0.4, 0]), 
            np.array([-0.4, -0.4, 0]), 
            np.array([0.4, -0.4, 0]),
            color=RED,fill_opacity =0.5
        ) for _ in range(6)]
        stars = [Star(n=5, outer_radius=0.4, color=PURPLE,fill_opacity =0.5) for _ in range(7)]

        circ =VGroup(*circles).arrange_in_grid(cols=5, buff=0.3)
        sq = VGroup(*squares).arrange_in_grid(cols=3, buff=0.3)
        tri = VGroup(*triangles).arrange_in_grid(cols=6, buff=0.3)
        star = VGroup(*stars).arrange_in_grid(cols=7, buff=0.3)
        circ.center()
        circ.shift(UP )
        sq.center()
        sq.shift(DOWN * 0.5)
        tri.center()
        tri.shift(DOWN * 1.7)
        star.center()
        star.shift(DOWN *3)
        circ_title = Text("Circle").scale(0.7)
        sq_title = Text("Square").scale(0.7)
        tri_title = Text("Triangle").scale(0.7)
        star_title = Text("Star").scale(0.7)
        circ_title.center()
        sq_title.center()
        tri_title.center()
        star_title.center()
        circ_title.shift(UP,LEFT * 5.4)
        sq_title.shift(DOWN *0.4,LEFT * 5.4)
        tri_title.shift(DOWN * 1.7,LEFT * 5.4)
        star_title.shift(DOWN * 2.9,LEFT * 5.4)
        title=Text("Shapes").scale(0.7)
        title.center()
        title.shift(UP * 2.1,LEFT * 5.4)
        title2=Text("No. of  Shapes").scale(0.7)
        title2.center()
        title2.shift(UP * 2.1,RIGHT )

        start_point = np.array([0,2.5, 0])
        end_point = np.array([0,-3.7, 0])
        horizontal_line = Line(start=LEFT*7, end=RIGHT*5, color=WHITE, stroke_width=4)
        horizontal_line.shift(UP *1.7)
        h2 = Line(start=LEFT*7, end=RIGHT*5, color=WHITE, stroke_width=4)
        h2.shift(UP *2.5)
        vertical_line = Line(start=start_point, end=end_point, color=WHITE, stroke_width=4)
        vertical_line.shift(LEFT * 4)
        v2 = Line(start=start_point, end=end_point, color=WHITE, stroke_width=4)
        v2.shift(LEFT * 7)
        v3= Line(start=start_point, end=end_point, color=WHITE, stroke_width=4)
        v3.shift(RIGHT * 5)
        h3 = Line(start=LEFT*7, end=RIGHT*5, color=WHITE, stroke_width=4)
        h3.shift(DOWN * 3.7)
        group = VGroup(vertical_line, horizontal_line,h2,v2,v3,h3)
        group2= VGroup(title,title2,circ_title,sq_title,tri_title,star_title,circ,tri ,sq,star)
        group.scale(0.8)
        group2.scale(0.8)
        group.shift(DOWN * 0.5)
        group2.shift(DOWN * 0.5)
        self.add(group)
        self.add(group2)
        self.wait(5)
        rect2 = Rectangle(width=7.2, height=1, color= LIGHT_PINK ,fill_opacity =0.5)
        self.add(rect2)
        rect2.shift(DOWN , RIGHT * 0.2)
        star_large = sq.copy().scale(1.2).set_color(YELLOW)
        star_large.move_to(sq.get_center())
        self.play(Write(text3))
        self.play(Transform(sq, star_large))
        self.wait(1)

        # Zoom out the star group
        self.play(Transform(sq, sq.copy().scale(1/1.5).set_color(GREEN)))
        self.wait(3)

    def Example(self):
        text = Text("Example", color=YELLOW).scale(0.9)
        text.center()
        text.shift(UP * 3)
        self.play(Write(text))

      
        table_content = [
            ["Class", "Total Students", "Present", "Absent"],
            ["Class 1", "32", "25", "7"],
            ["Class 2", "40", "37", "3"],
            ["Class 3", "45", "44", "1"],
            ["Class 4", "48", "42", "6"],
            ["Class 5", "55", "53", "2"],
            ["Total", "220", "201", "19"]
        ]
        cell_height = 0.8
        cell_width = 3.3
      
        start_position = ORIGIN + UP * (len(table_content) * cell_height / 2)

        
        h_lines = VGroup(*[
            Line(
                start=start_position + np.array([-cell_width / 2, -j * cell_height - cell_height / 2, 0]),
                end=start_position + np.array([(len(table_content[0])) * cell_width - cell_width / 2, -j * cell_height - cell_height / 2, 0])
            )
            for j in range(len(table_content) + 1)
        ])

        extra_h_line_top = Line(
            start=start_position + np.array([-cell_width / 2, cell_height / 2, 0]),
            end=start_position + np.array([(len(table_content[0])) * cell_width - cell_width / 2, cell_height / 2, 0])
        )

        v_lines = VGroup(*[
            Line(
                start=start_position + np.array([i * cell_width - cell_width / 2, cell_height / 2, 0]),
                end=start_position + np.array([i * cell_width - cell_width / 2, -(len(table_content)) * cell_height + cell_height / 2, 0])
            )
            for i in range(len(table_content[0]) + 1)
        ])

        table_with_lines = VGroup( h_lines, v_lines, extra_h_line_top)
        table_with_lines.shift(LEFT * 5)
        table_with_lines.shift(DOWN)
        self.add(table_with_lines)

        table = VGroup(*[
            VGroup(*[
                Tex(content, color=BLUE if j == 0 or i == 0 else LIGHT_PINK).move_to(start_position + np.array([i * cell_width, -j * cell_height, 0]))
                for i, content in enumerate(row)
            ])
            for j, row in enumerate(table_content)
        ])
        table.shift(LEFT * 5 + DOWN )
        self.play(Create(table))
        self.wait(1)
        
        self.wait(5)

        self.wait(7)

    def Question1(self):
        text = Text("Question and Answers", color=RED_C).scale(0.7)
        text.center()
        text.to_edge(UP)
        self.play(Write(text))
        text2 =Text("(a). How many students are present in class 4?",color=GREEN_C).scale(0.7)
        text2.center()
        text2.shift(UP * 2.5,LEFT)
        self.play(Write(text2))
        text3 =Text("Ans. 42 Students",color=PURPLE).scale(0.7)
        text3.center()
        text3.shift(UP * 1.5,LEFT * 3.8)
       
     
        table_content = [
            ["Class", "Total Students", "Present", "Absent"],
            ["Class 1", "32", "25", "7"],
            ["Class 2", "40", "37", "3"],
            ["Class 3", "45", "44", "1"],
            ["Class 4", "48", "42", "6"],
            ["Class 5", "55", "53", "2"],
            ["Total", "220", "201", "19"]
        ]
        cell_height = 0.8
        cell_width = 3.3
      
        start_position = ORIGIN + UP * (len(table_content) * cell_height / 2)

        
        h_lines = VGroup(*[
            Line(
                start=start_position + np.array([-cell_width / 2, -j * cell_height - cell_height / 2, 0]),
                end=start_position + np.array([(len(table_content[0])) * cell_width - cell_width / 2, -j * cell_height - cell_height / 2, 0])
            )
            for j in range(len(table_content) )
        ])

        extra_h_line_top = Line(
            start=start_position + np.array([-cell_width / 2, cell_height / 2, 0]),
            end=start_position + np.array([(len(table_content[0])) * cell_width - cell_width / 2, cell_height / 2, 0])
        )

        v_lines = VGroup(*[
            Line(
                start=start_position + np.array([i * cell_width - cell_width / 2, cell_height / 2, 0]),
                end=start_position + np.array([i * cell_width - cell_width / 2, -(len(table_content)) * cell_height + cell_height / 2, 0])
            )
            for i in range(len(table_content[0]) + 1)
        ])

        table_with_lines = VGroup( h_lines, v_lines, extra_h_line_top)
        table_with_lines.shift(LEFT * 5)
        table_with_lines.shift(DOWN * 2)
        table_with_lines.scale(0.8)
        self.add(table_with_lines)

        table = VGroup(*[
            VGroup(*[
                Tex(content, color=BLUE if j == 0 or i == 0 else LIGHT_PINK).move_to(start_position + np.array([i * cell_width, -j * cell_height, 0]))
                for i, content in enumerate(row)
            ])
            for j, row in enumerate(table_content)
        ])
        table.shift(LEFT * 5 + DOWN *2 )
        self.add(table)
        table.scale(0.8)
        self.wait(3)
        self.play(Write(text3))
        rect2 = Rectangle(width=2.6, height=0.6, color= LIGHT_PINK ,fill_opacity =0.5)
        self.add(rect2)
        rect2.center()
        rect2.shift(DOWN * 2.25 , RIGHT* 1.25)
      
        cell = table[4][2] 
     
        cell_large = cell.copy().scale(1.5).set_color(YELLOW)

        cell_large.move_to(cell.get_center())

        self.play(Transform(cell, cell_large))
        self.wait(1)
        self.play(ReplacementTransform(cell_large, cell))
        self.wait(3)

    def Question2(self):

        text = Text(" (b). Which class has the highest number of absent students?", color=GREEN_C).scale(0.6)
        text.center()
        text.shift(UP * 2.8, LEFT * 0.5)
        self.play(Write(text))
        text3 =Text("Ans. Class 1 - 7 Students",color=PURPLE).scale(0.7)
        text3.center()
        text3.shift(UP * 1.7,LEFT * 3)
       
     
        table_content = [
            ["Class", "Total Students", "Present", "Absent"],
            ["Class 1", "32", "25", "7"],
            ["Class 2", "40", "37", "3"],
            ["Class 3", "45", "44", "1"],
            ["Class 4", "48", "42", "6"],
            ["Class 5", "55", "53", "2"],
            ["Total", "220", "201", "19"]
        ]
        cell_height = 0.8
        cell_width = 3.3
      
        start_position = ORIGIN + UP * (len(table_content) * cell_height / 2)

        
        h_lines = VGroup(*[
            Line(
                start=start_position + np.array([-cell_width / 2, -j * cell_height - cell_height / 2, 0]),
                end=start_position + np.array([(len(table_content[0])) * cell_width - cell_width / 2, -j * cell_height - cell_height / 2, 0])
            )
            for j in range(len(table_content) )
        ])

        extra_h_line_top = Line(
            start=start_position + np.array([-cell_width / 2, cell_height / 2, 0]),
            end=start_position + np.array([(len(table_content[0])) * cell_width - cell_width / 2, cell_height / 2, 0])
        )

        v_lines = VGroup(*[
            Line(
                start=start_position + np.array([i * cell_width - cell_width / 2, cell_height / 2, 0]),
                end=start_position + np.array([i * cell_width - cell_width / 2, -(len(table_content)) * cell_height + cell_height / 2, 0])
            )
            for i in range(len(table_content[0]) + 1)
        ])

        table_with_lines = VGroup( h_lines, v_lines, extra_h_line_top)
        table_with_lines.shift(LEFT * 5)
        table_with_lines.shift(DOWN * 2)
        table_with_lines.scale(0.8)
        self.add(table_with_lines)

        table = VGroup(*[
            VGroup(*[
                Tex(content, color=BLUE if j == 0 or i == 0 else LIGHT_PINK).move_to(start_position + np.array([i * cell_width, -j * cell_height, 0]))
                for i, content in enumerate(row)
            ])
            for j, row in enumerate(table_content)
        ])
        table.shift(LEFT * 5 + DOWN *2 )
        self.add(table)
        table.scale(0.8)
        self.wait(3)
        self.play(Write(text3))
        rect2 = Rectangle(width=2.6, height=0.6, color= LIGHT_PINK ,fill_opacity =0.5)
        self.add(rect2)
        rect2.center()
        rect2.shift( RIGHT* 3.9, DOWN *0.3)
      
        cell = table[1][3] 
     
        cell_large = cell.copy().scale(1.5).set_color(YELLOW)

        cell_large.move_to(cell.get_center())

        self.play(Transform(cell, cell_large))
        self.wait(1)
        self.play(ReplacementTransform(cell_large, cell))
        self.wait(3)

    def Question3(self): 
        text3 =Text("(c). Which class has the least number of absent students?", color=GREEN_C).scale(0.6)
        text3.shift(UP * 2.8)
        self.play(Write(text3))
        text3 =Text("Ans. Class 3 - 1 Student",color=PURPLE).scale(0.7)
        text3.center()
        text3.shift(UP * 1.8,LEFT * 3)
       
     
        table_content = [
            ["Class", "Total Students", "Present", "Absent"],
            ["Class 1", "32", "25", "7"],
            ["Class 2", "40", "37", "3"],
            ["Class 3", "45", "44", "1"],
            ["Class 4", "48", "42", "6"],
            ["Class 5", "55", "53", "2"],
            ["Total", "220", "201", "19"]
        ]
        cell_height = 0.8
        cell_width = 3.3
      
        start_position = ORIGIN + UP * (len(table_content) * cell_height / 2)

        
        h_lines = VGroup(*[
            Line(
                start=start_position + np.array([-cell_width / 2, -j * cell_height - cell_height / 2, 0]),
                end=start_position + np.array([(len(table_content[0])) * cell_width - cell_width / 2, -j * cell_height - cell_height / 2, 0])
            )
            for j in range(len(table_content) )
        ])

        extra_h_line_top = Line(
            start=start_position + np.array([-cell_width / 2, cell_height / 2, 0]),
            end=start_position + np.array([(len(table_content[0])) * cell_width - cell_width / 2, cell_height / 2, 0])
        )

        v_lines = VGroup(*[
            Line(
                start=start_position + np.array([i * cell_width - cell_width / 2, cell_height / 2, 0]),
                end=start_position + np.array([i * cell_width - cell_width / 2, -(len(table_content)) * cell_height + cell_height / 2, 0])
            )
            for i in range(len(table_content[0]) + 1)
        ])

        table_with_lines = VGroup( h_lines, v_lines, extra_h_line_top)
        table_with_lines.shift(LEFT * 5)
        table_with_lines.shift(DOWN * 2)
        table_with_lines.scale(0.8)
        self.add(table_with_lines)

        table = VGroup(*[
            VGroup(*[
                Tex(content, color=BLUE if j == 0 or i == 0 else LIGHT_PINK).move_to(start_position + np.array([i * cell_width, -j * cell_height, 0]))
                for i, content in enumerate(row)
            ])
            for j, row in enumerate(table_content)
        ])
        table.shift(LEFT * 5 + DOWN *2 )
        self.add(table)
        table.scale(0.8)
        self.wait(3)
        self.play(Write(text3))
        rect2 = Rectangle(width=2.6, height=0.6, color= LIGHT_PINK ,fill_opacity =0.5)
        self.add(rect2)
        rect2.center()
        rect2.shift(DOWN * 1.6 , RIGHT* 3.9)
      
        cell = table[3][3] 
     
        cell_large = cell.copy().scale(1.5).set_color(YELLOW)

        cell_large.move_to(cell.get_center())

        self.play(Transform(cell, cell_large))
        self.wait(1)
        self.play(ReplacementTransform(cell_large, cell))
        self.wait(3)

    def Question4(self):
        text2 =Text("(d). How many students were absent in class 1?",color=GREEN_C).scale(0.6)
        text2.center()
        text2.shift(UP * 2.8,LEFT)
        self.play(Write(text2))
             
        text3 =Text("Ans. 7 Students",color=PURPLE).scale(0.7)
        text3.center()
        text3.shift(UP * 1.8,LEFT * 3.8)
       
     
        table_content = [
            ["Class", "Total Students", "Present", "Absent"],
            ["Class 1", "32", "25", "7"],
            ["Class 2", "40", "37", "3"],
            ["Class 3", "45", "44", "1"],
            ["Class 4", "48", "42", "6"],
            ["Class 5", "55", "53", "2"],
            ["Total", "220", "201", "19"]
        ]
        cell_height = 0.8
        cell_width = 3.3
      
        start_position = ORIGIN + UP * (len(table_content) * cell_height / 2)

        
        h_lines = VGroup(*[
            Line(
                start=start_position + np.array([-cell_width / 2, -j * cell_height - cell_height / 2, 0]),
                end=start_position + np.array([(len(table_content[0])) * cell_width - cell_width / 2, -j * cell_height - cell_height / 2, 0])
            )
            for j in range(len(table_content) )
        ])

        extra_h_line_top = Line(
            start=start_position + np.array([-cell_width / 2, cell_height / 2, 0]),
            end=start_position + np.array([(len(table_content[0])) * cell_width - cell_width / 2, cell_height / 2, 0])
        )

        v_lines = VGroup(*[
            Line(
                start=start_position + np.array([i * cell_width - cell_width / 2, cell_height / 2, 0]),
                end=start_position + np.array([i * cell_width - cell_width / 2, -(len(table_content)) * cell_height + cell_height / 2, 0])
            )
            for i in range(len(table_content[0]) + 1)
        ])

        table_with_lines = VGroup( h_lines, v_lines, extra_h_line_top)
        table_with_lines.shift(LEFT * 5)
        table_with_lines.shift(DOWN * 2)
        table_with_lines.scale(0.8)
        self.add(table_with_lines)

        table = VGroup(*[
            VGroup(*[
                Tex(content, color=BLUE if j == 0 or i == 0 else LIGHT_PINK).move_to(start_position + np.array([i * cell_width, -j * cell_height, 0]))
                for i, content in enumerate(row)
            ])
            for j, row in enumerate(table_content)
        ])
        table.shift(LEFT * 5 + DOWN *2 )
        self.add(table)
        table.scale(0.8)
        self.wait(3)
        self.play(Write(text3))
        rect2 = Rectangle(width=2.6, height=0.6, color= LIGHT_PINK ,fill_opacity =0.5)
        self.add(rect2)
        rect2.center()
        rect2.shift( RIGHT* 3.9, DOWN *0.3)
      
        cell = table[1][3] 
     
        cell_large = cell.copy().scale(1.5).set_color(YELLOW)

        cell_large.move_to(cell.get_center())

        self.play(Transform(cell, cell_large))
        self.wait(1)
        self.play(ReplacementTransform(cell_large, cell))
        self.wait(3)

    def Question5(self):
        text = Text("(e).  How many students are absent in total ?", color=GREEN_C).scale(0.6)
        text.center()
        text.shift(UP * 2.8, LEFT * 1.3 )
        self.play(Write(text))
     
        text3 =Text("Ans. 19 Students",color=PURPLE).scale(0.7)
        text3.center()
        text3.shift(UP *2,LEFT * 3.6)
       
     
        table_content = [
            ["Class", "Total Students", "Present", "Absent"],
            ["Class 1", "32", "25", "7"],
            ["Class 2", "40", "37", "3"],
            ["Class 3", "45", "44", "1"],
            ["Class 4", "48", "42", "6"],
            ["Class 5", "55", "53", "2"],
            ["Total", "220", "201", "19"]
        ]
        cell_height = 0.8
        cell_width = 3.3
      
        start_position = ORIGIN + UP * (len(table_content) * cell_height / 2)

        
        h_lines = VGroup(*[
            Line(
                start=start_position + np.array([-cell_width / 2, -j * cell_height - cell_height / 2, 0]),
                end=start_position + np.array([(len(table_content[0])) * cell_width - cell_width / 2, -j * cell_height - cell_height / 2, 0])
            )
            for j in range(len(table_content) )
        ])

        extra_h_line_top = Line(
            start=start_position + np.array([-cell_width / 2, cell_height / 2, 0]),
            end=start_position + np.array([(len(table_content[0])) * cell_width - cell_width / 2, cell_height / 2, 0])
        )

        v_lines = VGroup(*[
            Line(
                start=start_position + np.array([i * cell_width - cell_width / 2, cell_height / 2, 0]),
                end=start_position + np.array([i * cell_width - cell_width / 2, -(len(table_content)) * cell_height + cell_height / 2, 0])
            )
            for i in range(len(table_content[0]) + 1)
        ])

        table_with_lines = VGroup( h_lines, v_lines, extra_h_line_top)
        table_with_lines.shift(LEFT * 5)
        table_with_lines.shift(DOWN * 2)
        table_with_lines.scale(0.8)
        self.add(table_with_lines)

        table = VGroup(*[
            VGroup(*[
                Tex(content, color=BLUE if j == 0 or i == 0 else LIGHT_PINK).move_to(start_position + np.array([i * cell_width, -j * cell_height, 0]))
                for i, content in enumerate(row)
            ])
            for j, row in enumerate(table_content)
        ])
        table.shift(LEFT * 5 + DOWN *2 )
        self.add(table)
        table.scale(0.8)
        self.wait(3)
        self.play(Write(text3))
        rect2 = Rectangle(width=2.6, height=0.6, color= LIGHT_PINK ,fill_opacity =0.5)
        self.add(rect2)
        rect2.center()
        rect2.shift(DOWN * 3.5 , RIGHT* 3.9)
      
        cell = table[6][3] 
     
        cell_large = cell.copy().scale(1.5).set_color(YELLOW)

        cell_large.move_to(cell.get_center())

        self.play(Transform(cell, cell_large))
        self.wait(1)
        self.play(ReplacementTransform(cell_large, cell))
        self.wait(3)
    
    def Question6(self):
        text3 =Text("(f). How many students are present in total?", color=GREEN_C).scale(0.7)
        text3.shift(UP  * 2.8)
        text3.shift(LEFT)
        self.play(Write(text3))
     
        text3 =Text("Ans. 201 Students",color=PURPLE).scale(0.7)
        text3.center()
        text3.shift(UP * 1.9,LEFT * 3.6)
       
     
        table_content = [
            ["Class", "Total Students", "Present", "Absent"],
            ["Class 1", "32", "25", "7"],
            ["Class 2", "40", "37", "3"],
            ["Class 3", "45", "44", "1"],
            ["Class 4", "48", "42", "6"],
            ["Class 5", "55", "53", "2"],
            ["Total", "220", "201", "19"]
        ]
        cell_height = 0.8
        cell_width = 3.3
      
        start_position = ORIGIN + UP * (len(table_content) * cell_height / 2)

        
        h_lines = VGroup(*[
            Line(
                start=start_position + np.array([-cell_width / 2, -j * cell_height - cell_height / 2, 0]),
                end=start_position + np.array([(len(table_content[0])) * cell_width - cell_width / 2, -j * cell_height - cell_height / 2, 0])
            )
            for j in range(len(table_content) )
        ])

        extra_h_line_top = Line(
            start=start_position + np.array([-cell_width / 2, cell_height / 2, 0]),
            end=start_position + np.array([(len(table_content[0])) * cell_width - cell_width / 2, cell_height / 2, 0])
        )

        v_lines = VGroup(*[
            Line(
                start=start_position + np.array([i * cell_width - cell_width / 2, cell_height / 2, 0]),
                end=start_position + np.array([i * cell_width - cell_width / 2, -(len(table_content)) * cell_height + cell_height / 2, 0])
            )
            for i in range(len(table_content[0]) + 1)
        ])

        table_with_lines = VGroup( h_lines, v_lines, extra_h_line_top)
        table_with_lines.shift(LEFT * 5)
        table_with_lines.shift(DOWN * 2)
        table_with_lines.scale(0.8)
        self.add(table_with_lines)

        table = VGroup(*[
            VGroup(*[
                Tex(content, color=BLUE if j == 0 or i == 0 else LIGHT_PINK).move_to(start_position + np.array([i * cell_width, -j * cell_height, 0]))
                for i, content in enumerate(row)
            ])
            for j, row in enumerate(table_content)
        ])
        table.shift(LEFT * 5 + DOWN *2 )
        self.add(table)
        table.scale(0.8)
        self.wait(3)
        self.play(Write(text3))
        rect2 = Rectangle(width=2.6, height=0.6, color= LIGHT_PINK ,fill_opacity =0.5)
        self.add(rect2)
        rect2.center()
        rect2.shift(DOWN * 3.5, RIGHT * 1.25)
      
        cell = table[6][2] 
     
        cell_large = cell.copy().scale(1.5).set_color(YELLOW)

        cell_large.move_to(cell.get_center())

        self.play(Transform(cell, cell_large))
        self.wait(1)
        self.play(ReplacementTransform(cell_large, cell))
        self.wait(3)


    def SetDeveloperList(self): 
       self.DeveloperList="Khanak Gupta" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade3Chapter11DataHandling.py"

if __name__ == "__main__":
    scene = DataHandling()
    scene.render()