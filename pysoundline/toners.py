# Toners define change of frequency in time of a sound.
# See: `signal`, `faders`

class BaseToner:
    """Base class for Toners"""

    def __init__(self):
        pass

    def __call__(self, time):
        return self.at(time)


class ConstToner(BaseToner):
    """Constant Toner"""

    def __init__(self, freq):
        self.freq = float(freq)

    def at(self, time):
        return self.freq


class LineToner(BaseToner):
    """Linear Toner"""

    def __init__(self, start_freq, stop_freq, duration):
        self.start_freq = float(start_freq)
        self.stop_freq = float(stop_freq)
        self.duration = float(duration)

    def at(self, time):
        return (self.stop_freq - self.start_freq) * time / self.duration + self.start_freq
