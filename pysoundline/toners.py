
class BaseToner:

    def __init__(self):
        pass

    def __call__(self, time):
        return self.at(time)


class ConstToner(BaseToner):

    def __init__(self, freq):
        self.freq = float(freq)

    def at(self, time):
        return self.freq


class LineToner(BaseToner):

    def __init__(self, start_freq, stop_freq, duration):
        self.start_freq = float(start_freq)
        self.stop_freq = float(stop_freq)
        self.duration = float(duration)

    def at(self, time):
        return (self.stop_freq - self.start_freq) * time / self.duration + self.start_freq
