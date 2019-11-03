import numpy

class BaseFader:
    """Base class for Faders"""

    def __init__(self):
        pass

    def __call__(self, time):
        return self.at(time)

    def __repr__(self):
        return 'Fader()'

class ConstFader(BaseFader):
    """Constant Fader"""

    def __init__(self, amplitude):
        self.amplitude = amplitude

    def at(self, time):
        return self.amplitude

    def __repr__(self):
        return 'ConstFader(amplitude={0})'.format(self.amplitude)

class ExpFader(BaseFader):
    """Exponential fader"""

    def __init__(self, a, amplitude):
        self.a = abs(a)
        self.amplitude = amplitude

    def at(self, time):
        return self.amplitude * numpy.exp(-self.a * time)

    def __repr__(self):
        return 'ExpFader(amplitude={0},a={1})'.format(self.amplitude, self.a)

