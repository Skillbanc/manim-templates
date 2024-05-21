from manim import *
from manim_voiceover import VoiceoverScene
# from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.recorder import RecorderService

class VoiceOver(VoiceoverScene):
    def construct(self):
        # self.set_speech_service(GTTSService())
        self.set_speech_service(RecorderService())

        with self.voiceover(text="This circle is drawn as I speak.") as tracker:
            self.play(Create(Circle()))

if __name__=="__main__":
    scene=VoiceOver()
    scene.render()