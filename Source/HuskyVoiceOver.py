import requests
from manim import *
from manim_voiceover import VoiceoverScene
# from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.coqui import CoquiService
class HuskyVoiceOver(VoiceoverScene):
    def construct(self):
        # self.set_speech_service(GTTSService())
        # self.set_speech_service(RecorderService())
        self.set_speech_service(CoquiService(
           model_name= 'tts_models/en/jenny/jenny'
        ))
        image_url = "https://images.wagwalkingweb.com/media/daily_wag/blog_articles/hero/1685787498.877709/fun-facts-about-siberian-huskies-1.png"
        image_path = "image.png"

        response = requests.get(image_url)
        with open(image_path, 'wb') as file:
            file.write(response.content)

        # Load the downloaded image
            image = ImageMobject(image_path)
            
            # Set the initial position
            image.to_edge(LEFT)

        with self.voiceover(text="The picture of a husky dog is being displayed on the left side of screen.") as tracker:
            # Display the image
            self.play(FadeIn(image), run_time=tracker.duration)
        
        # Move the image to different positions
        with self.voiceover(text="Now the image is moving towards the right edge;") as tracker:
            self.play(image.animate.to_edge(RIGHT), run_time=tracker.duration)

        with self.voiceover(text="to the top edge;") as tracker:
            self.play(image.animate.to_edge(UP), run_time=tracker.duration)

        with self.voiceover(text="to the bottom edge;") as tracker:
            self.play(image.animate.to_edge(DOWN), run_time=tracker.duration)

        with self.voiceover(text="and finally to the center of the screen.") as tracker:
            self.play(image.animate.move_to(ORIGIN), run_time=tracker.duration)
        
        with self.voiceover(text="Now the size of the picture is scaled to twice the original size.") as tracker:
            self.play(image.animate.scale(2), run_time=tracker.duration)

if __name__=="__main__":
    scene=HuskyVoiceOver()
    scene.render()