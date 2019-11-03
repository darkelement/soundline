from math import exp

from pysoundline import constants, playback, timeline, signal, faders, toners

class String:
    def __init__(self):
        pass

    def get_playback(self, freq, samplerate=constants.SAMPLERATE):
        harmonics = constants.get_harmonics(freq, 10)
        t = timeline.Timeline()

        for i, h in enumerate(harmonics):
            ef = faders.ExpFader(exp(-i), 5)
            ct = toners.ConstToner(h)
            s = signal.Signal(ef, ct, 2)
            t.add_sound(s, 0)

        return t.get_playback(samplerate)


