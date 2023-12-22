import pygame
from gtts import gTTS


def text_to_speech_and_play(text, language='uk'):
    tts = gTTS(text, lang=language)
    tts.save('audio/output.mp3')

    pygame.mixer.init()
    pygame.mixer.music.load('audio/output.mp3')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(1)


text = "Ви праві, і вибачте за непорозуміння."
text_to_speech_and_play(text)