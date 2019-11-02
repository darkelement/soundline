import numpy

from . import playback, signal

class SoundContainer:
    def __init__(self, sound, time):
        self.sound = sound
        self.time = time

class Timeline:

    def __init__(self):
        self.line = list()

    def add_sound(self, sound, time):
        self.line.append(SoundContainer(sound, time))

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
        self.duration = int(self.stop_time - self.start_time)
        return self.duration

    def get_playback(self, samplerate):
        return playback.Playback(self.__flatten(samplerate), samplerate)

    def __flatten(self, samplerate):
        self.get_duration()
        data = numpy.zeros(self.duration * samplerate)

        for item in self.line:
            item_data = self.__get_data_from_sound(item.sound, samplerate)
            start = int((item.time - self.start_time) * samplerate)
            stop = start + len(item_data)

            a = data[:start]
            b = data[start:stop] + item_data
            c = data[stop:]

            data = numpy.concatenate((a, b, c))

        return data

    def __get_data_from_sound(self, sound, samplerate):
        if isinstance(sound, Timeline):
            data = sound.__flatten(samplerate)
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

