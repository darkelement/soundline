from math import exp

from .. import constants, faders, toners, Signal, Timeline

class String:
    def __init__(self):
        pass

    def get_playback(self, freq, samplerate=constants.SAMPLERATE):
        t = Timeline()

        for i in range(0, 7):
            ef = faders.ExpFader(exp(-10.0 * i * i), 5 * (i + 1) * (i + 1))
            ct = toners.ConstToner((i + 1) * freq)
            s = Signal(ef, ct, 2)
            t.add_sound(s, 0)

        return t.get_playback(samplerate)


