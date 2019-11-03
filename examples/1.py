#!/usr/bin/python

import sys
sys.path.append('.')
sys.path.append('..')

from pysoundline import constants, toners, faders, Signal, Timeline

sA3 = Signal(faders.ExpFader(1, 10), toners.ConstToner(constants.Note.A[3]), 1)
sA4 = Signal(faders.ExpFader(1, 10), toners.ConstToner(constants.Note.A[4]), 1)
sA5 = Signal(faders.ExpFader(1, 10), toners.ConstToner(constants.Note.A[5]), 1)

constants.print_notes()
sA5.get_playback().save('example_1.1.wav')

t1 = Timeline()
t1.add_sound(sA3, 0)
t1.add_sound(sA4, 1)
t1.add_sound(sA5, 2)
t1.get_playback().save('example_1.2.wav')

t2 = Timeline()
for i, s in enumerate([
        Signal(faders.ExpFader(1, 30), toners.ConstToner(t), 0.2)
        for t in range(400, 900, 50)
    ]):
    t2.add_sound(s, 0.2 * i)
t2.get_playback().save('example_1.3.wav')

t3 = Timeline()
t3.add_sound(t1, -1)
t3.add_sound(t2, 0)
t3.add_sound(t1, 1)
t3.get_playback().save('example_1.4.wav')

s = Signal(faders.ConstFader(0.5), toners.LineToner(100, 1000, 2), 2)
s.get_playback().save('example_1.5.wav')

t3.add_sound(s, t3.get_duration())
t3.get_playback().save('example_1.6.wav')
