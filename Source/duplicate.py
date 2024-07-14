from manim import *

class TableScene(Scene):
    def construct(self):
        self.CubeRoot_table()


    
    def CubeRoot_table(self):

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
            h_buff=1.7,
            v_buff=0.4
        )
        
        # Change the color of the table lines to blue
        table.get_horizontal_lines().set_color(BLUE)
        table.get_vertical_lines().set_color(BLUE)

        # Change the color of the headings to pink
        table.get_entries((1, 1)).set_color(PINK)
        table.get_entries((1, 2)).set_color(PINK)


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
