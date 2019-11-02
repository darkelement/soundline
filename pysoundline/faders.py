import numpy

class BaseFader:

    def __init__(self):
        pass

    def __call__(self, time):
        return self.at(time)


class ConstFader(BaseFader):

    def __init__(self, amplitude):
        self.amplitude = amplitude

    def at(self, time):
        return self.amplitude


class ExpFader(BaseFader):

    def __init__(self, a):
        self.a = abs(a)

    def at(self, time):
        return numpy.exp(-self.a * time)

