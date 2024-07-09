from manim import *



class Before(Scene):
  
    
    def construct(self):
        # Create the grid
        grid = VGroup(*[Square(side_length=1, color=BLUE, fill_opacity=0.1) for _ in range(15)])
        grid.arrange_in_grid(rows=5, cols=3, buff=0)
        grid.shift(LEFT * 1.5 + DOWN * 0.5)

        # Create the single purple square
        purple_square = Square(side_length=1, color=PURPLE, fill_opacity=0.1)
        purple_square.next_to(grid, DOWN, buff=0.5)

        # Create the number 1
        number = Text("1", color=RED).scale(0.8)
        number.move_to(grid[12])

        # Add everything to the scene
        self.add(grid, purple_square, number)

        # Animate the stacking
        for i in range(12, -1, -1):
            self.play(
                grid[i].animate.set_fill(BLUE, opacity=0.5),
                run_time=0.5
            )

        # Final pause
        self.wait(1)


       


if __name__ == "__main__":
    scene = Before()
    scene.render()