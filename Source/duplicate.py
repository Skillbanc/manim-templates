from manim import *

class TableScene(Scene):
    def construct(self):
        self.vertical_addition_exercise_1()


    def vertical_addition_exercise_1(self):

        table_data = [
            ["Square", "Square roots"],
            ["1² = 1", "√1 = 1"],
            ["2² = 4", "√4 = 2"],
            ["3² = 9", "√9 = 3"],
            ["4² = 16", "√16 = 4"],
            ["5² = 25", "√25 = 5"], 
            ["6² = 36", "√36 = 6"],
            ["7² = 49", "√49 = 7"],
            ["8² = 64", "√64 = 8"],
            ["9² = 81", "√81 = 9"],
            ["10² = 100", "√100 = 10"],
        ]

        # Create the table with the title
        table = Table(
            table_data,
            include_outer_lines=True,
            h_buff=1.5,
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



        table_data =[
            ["Number", "Cube"],
            ["1", "1³ = 1 * 1 * 1 = 1"],
            ["2", "2³ = 2 * 2 * 2 = 8"],
            ["3", "3³ = 3 * 3 * 3 = 27"],
            ["4", "4³ = 4 * 4 * 4 = 64"],
            ["5", "5³ = 5 * 5 * 5 = 125"],
            ["6", "6³ = 6 * 6 * 6 = 216"],
            ["7", "7³ = 7 * 7 * 7 = 343"],
            ["8", "8³ = 8 * 8 * 8 = 512"],
            ["9", "9³ = 9 * 9 * 9 = 729"],
            ["10", "10³ = 10 * 10 * 10 = 1000"],
        ]

        # Create the table with the title
        table = Table(
            table_data,
            include_outer_lines=True,
            h_buff=1,
            v_buff=0.4
        )

        # Position the table at the center of the scene
        table.scale(0.6)
        table.move_to(ORIGIN)

        # Add the title
        title = Text("Measure the objects given in the table using a scale.", font_size=24)
        title.next_to(table, UP * 0.5)

        # Play the title and table together
        self.play(Write(title), Create(table.get_horizontal_lines()), Create(table.get_vertical_lines()))
        self.wait(1)

        # Sequentially play each cell in the table
        for row in table.get_entries():
            for cell in row:
                self.play(FadeIn(cell))
                self.wait(0.5)

        self.wait(2)


        table_data = [
            ["Cube",  "Cube roots"],
            ["1³ = 1", "∛1 = 1"],
            ["2³ = 8", "∛8 = 2"],
            ["3³ = 27", "∛27 = 3"],
            ["4³ = 64", "∛64 = 4"],
            ["5³ = 125", "∛125 = 5"],
            ["6³ = 216", "∛216 = 6"],
            ["7³ = 343", "∛343 = 7"],
            ["8³ = 512", "∛512 = 8"],
            ["9³ = 729", "∛729 = 9"],
            ["10³ = 1000", "∛1000 = 10"],
        ]
        
        # Create the table with the title
        table = Table(
            table_data,
            include_outer_lines=True,
            h_buff=1.5,
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


    



if __name__ == "__main__":
    scene = TableScene()
    scene.render()
