import numpy

from . import playback

class Signal:
    __2pi = 2 * numpy.pi

    def __init__(self, fader, toner, duration):
        self.fader = fader
        self.toner = toner
        self.duration = duration

    def get_duration(self):
        return self.duration

    def get_playback(self, samplerate):
        time = numpy.arange(0, self.duration, 1.0 / samplerate)
        data = numpy.array([numpy.sin(self.toner(t) * self.__2pi * t) * self.fader(t) for t in time])
        return playback.Playback(data, samplerate)

