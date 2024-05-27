from manim import *

class MoveImage(Scene):
    def construct(self):
        # Load the image
        image_path = "Source\skillbanclogo.png"#relative path

        image = ImageMobject(image_path)
        
        # Set the initial position
        image.to_edge(LEFT)
        
        # Display the image
        self.play(FadeIn(image),run_time=2)
        
        # Move the image to different positions
        self.play(image.animate.to_edge(RIGHT))
        self.play(image.animate.to_edge(UP))
        self.play(image.animate.to_edge(DOWN))
        
        # Rotate the image
        self.play(image.animate.rotate(PI / 4))
        
        # Scale the image
        self.play(image.animate.scale(0.5))
        
        # Fade out the image
        self.play(FadeOut(image))

# To render the scene
if __name__ == "__main__":
    from manim import *
    scene = MoveImage()
    scene.render()
