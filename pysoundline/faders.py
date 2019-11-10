# Faders defines changes of volume in time of a sound.
# See: `signal`, `toners`.

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

class LinearFader(BaseFader):
    """Linear fader"""

    def __init__(self, raise_time):
        self.raise_time = float(raise_time)

    def at(self, time):
        if time < 0 or self.raise_time < time:
            return 0.0;

        return float(time) / self.raise_time

    def __repr__(self):
        return 'LinearFader(raise_time={})'.format(self.raise_time)


class SineFader(BaseFader):
    """Sine Fader"""

    def __init__(self, freq):
        self.freq = float(freq)

    def at(self, time):
        s = numpy.sin(numpy.pi * self.freq * time)
        return s*s

    def __repr__(self):
        return 'SineFader(freq={})'.format(self.freq)


class SimpleExpFader(BaseFader):
    """Simple Exponential fader"""

    def __init__(self, a, amplitude):
        self.a = abs(a)
        self.amplitude = amplitude

    def at(self, time):
        return self.amplitude * numpy.exp(-self.a * time)

    def __repr__(self):
        return 'SimpleExpFader(amplitude={},a={})'.format(self.amplitude, self.a)


class ExpFader(BaseFader):
    """Exponential fader"""

    def __init__(self, amplitude, a, raise_time=0.01):
        self.linear_fader = LinearFader(raise_time)
        self.simple_exp_fader = SimpleExpFader(amplitude, a)

    def at(self, time):
        if time < self.linear_fader.raise_time:
            return self.linear_fader.at(time)
        else:
            return self.simple_exp_fader.at(time - self.linear_fader.raise_time)

    def __repr__(self):
        return 'ExpFader(amplitude={},a={},raise_time={})' \
               .format(self.simple_exp_fader.amplitude,
                       self.simple_exp_fader.a,
                       self.linear_fader.raise_time)

class SineExpFader(BaseFader):
    """Sine Exponential fader"""

    def __init__(self, amplitude, a, freq, discord, raise_time=0.01):
        self.sine_fader = SineFader(freq)
        self.exp_fader = ExpFader(amplitude, a, raise_time)
        self.discord = float(discord)

    def at(self, time):
        sine = self.sine_fader.at(time)
        exp = self.exp_fader.at(time)
        return (self.discord*sine + (1.0-self.discord)) * exp

    def __repr__(self):
        return 'SineExpFader({},{})'.format(str(self.sine_fader), str(self.exp_fader))
