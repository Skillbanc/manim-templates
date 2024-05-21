import requests
from manim import *

class MoveImageeee(Scene):
    def construct(self):
        # URL of the image
        image_url = "https://images.wagwalkingweb.com/media/daily_wag/blog_articles/hero/1685787498.877709/fun-facts-about-siberian-huskies-1.png"
        image_path = "image.png"
        
        # Download the image
        response = requests.get(image_url)
        with open(image_path, 'wb') as file:
            file.write(response.content)
        
        # Load the downloaded image
        image = ImageMobject(image_path)
        
        # Set the initial position
        image.to_edge(LEFT)
        
        # Display the image
        self.play(FadeIn(image), run_time=2)
        
        # Move the image to different positions
        self.play(image.animate.to_edge(RIGHT))
        self.play(image.animate.to_edge(UP))
        self.play(image.animate.to_edge(DOWN))
        self.play(image.animate.move_to(ORIGIN))
        
        # Scale the image
        self.play(image.animate.scale(2))
        

# To render the scene
if __name__ == "__main__":
    from manim import *
    scene = MoveImageeee()
    scene.render()
