from math import exp

from .. import constants, playback, Timeline, Signal, faders, toners

class String:
    def __init__(self):
        pass

    def get_playback(self, freq, samplerate=constants.SAMPLERATE):
        harmonics = constants.get_harmonics(freq, 10)
        t = Timeline()

        for i, h in enumerate(harmonics):
            ef = faders.ExpFader(exp(-i), 5)
            ct = toners.ConstToner(h)
            s = Signal(ef, ct, 2)
            t.add_sound(s, 0)

        return t.get_playback(samplerate)


