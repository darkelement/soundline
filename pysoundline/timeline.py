import math
import numpy

from . import constants, playback, signal

class SoundContainer:
    def __init__(self, sound, time, volume=1.0):
        self.sound = sound
        self.time = time
        self.volume = volume

class Timeline:

    def __init__(self):
        self.line = list()

    def add_sound(self, sound, time, volume=1.0):
        self.line.append(SoundContainer(sound, time, volume))

    def get_start_time(self):
        start_time = 0

        for item in self.line:
            item_start_time = item.time
            if hasattr(item, 'get_start_time'):
                item_start_time += item.sound.get_start_time()

            if item_start_time < start_time:
                start_time = item_start_time

        return start_time

    def get_stop_time(self):
        stop_time = 0

        for item in self.line:
            item_stop_time = item.time
            if hasattr(item, 'get_stop_time'):
                item_stop_time += item.sound.get_stop_time()
            else:
                item_stop_time += item.sound.get_duration()

            if item_stop_time > stop_time:
                stop_time = item_stop_time

        return stop_time

    def get_duration(self):
        self.start_time = self.get_start_time()
        self.stop_time = self.get_stop_time()
        self.duration = self.stop_time - self.start_time
        return self.duration

    def get_playback(self, samplerate=constants.SAMPLERATE):
        return playback.Playback(self._flatten(samplerate), samplerate)

    def _flatten(self, samplerate):
        self.get_duration()
        data = numpy.zeros(math.ceil(self.duration * samplerate))

        for item in self.line:
            item_data = self._get_data_from_sound(item.sound, samplerate)
            start = int((item.time - self.start_time) * samplerate)
            stop = start + len(item_data)

            a = data[:start]
            b = data[start:stop] + (item.volume * item_data)
            c = data[stop:]

            data = numpy.concatenate((a, b, c))

        return data

    def _get_data_from_sound(self, sound, samplerate):
        if isinstance(sound, Timeline):
            data = sound._flatten(samplerate)
        elif isinstance(sound, playback.Playback):
            if sound.get_samplerate() == samplerate:
                data = sound.get_data()
            else:
                data = list()
        elif isinstance(sound, signal.Signal):
            data = sound.get_playback(samplerate).get_data()
        else:
            data = list()

        return data

