from manim import *
from manim_voiceover import VoiceoverScene
# from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.coqui import CoquiService

class AIVoiceOver(VoiceoverScene):
    def construct(self):
        # self.set_speech_service(GTTSService())
        self.set_speech_service(CoquiService(
           model_name= 'tts_models/en/jenny/jenny'
        ))

        with self.voiceover(text="This circle is drawn as I speak.") as tracker:
            self.play(Create(Circle()))

if __name__=="__main__":
    scene=AIVoiceOver()
    scene.render()