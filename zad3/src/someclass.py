from datetime import datetime


class SomeClass:
    def __init__(self):
        self.wav_was_played = False

    def getTime(self):
        time = datetime.now()
        hour = time.strftime("%H")
        return hour

    def playWavFile(self):
        self.wav_was_played = True

    def resetWav(self):
        self.wav_was_played = False
