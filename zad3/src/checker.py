from zad3.src.someclass import SomeClass


class Checker:
    def __init__(self, sc: SomeClass):
        self.sc = sc

    def reminder(self):
        hour = self.sc.getTime()
        if hour >= 17:
            self.sc.playWavFile()
            return "File was played."
        return "File wasn't played."
