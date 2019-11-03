import numpy
import scipy.io.wavfile

class Playback:

    def __init__(self, data, samplerate):
        self.data = data
        self.samplerate = samplerate

    def get_duration(self):
        return len(self.data) / float(self.samplerate)

    def save(self, filename):
        self._normalize()
        data = numpy.int16(self.data / numpy.max(numpy.abs(self.data)) * 32767)
        scipy.io.wavfile.write(filename, self.samplerate, data)

    def get_data(self):
        return self.data

    def get_samplerate(self):
        return self.samplerate

    def _normalize(self):
        m = float(max(self.data))
        self.data = self.data / m
