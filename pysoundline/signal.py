import random
import numpy

from . import constants, playback

class Signal:
    """
    Tree main characteristics of a sound are its
      * volume - which describes how laud the sound is
      * frequency and its change in time (here called the sounds "tone")
      * duration in time

    The signal is composed of these three elements. Volume is represented by special object -
    `fader` and tone is represented by `toner`.
    """

    _2pi = 2 * numpy.pi

    def __init__(self, fader, toner, duration):
        self.fader = fader
        self.toner = toner
        self.duration = duration

    def get_duration(self):
        return self.duration

    def get_playback(self, samplerate=constants.SAMPLERATE):
        time = numpy.arange(0, self.duration, 1.0 / samplerate)
        phase = random.uniform(0.0, self._2pi)
        data = numpy.array([
            numpy.sin(self.toner(t) * self._2pi * t + phase) * self.fader(t)
            for t in time
        ])
        return playback.Playback(data, samplerate)

    def __repr__(self):
        return 'Signal({0})'.format(str(self.fader))

