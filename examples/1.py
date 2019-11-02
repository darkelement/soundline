#!/usr/bin/python

import sys
sys.path.append('.')
sys.path.append('..')

from pysoundline import signal, toners, faders, timeline, constants

sA3 = signal.Signal(faders.ExpFader(10), toners.ConstToner(constants.Note.A[3]), 1)
sA4 = signal.Signal(faders.ExpFader(10), toners.ConstToner(constants.Note.A[4]), 1)
sA5 = signal.Signal(faders.ExpFader(10), toners.ConstToner(constants.Note.A[5]), 1)

constants.Note.print_notes()
sA5.get_playback(10000).save('test1.wav')

t1 = timeline.Timeline()
t1.add_sound(sA4, 0)
t1.add_sound(sA5, 1)
t1.get_playback(10000).save('test2.wav')

t2 = timeline.Timeline()
for i, s in enumerate([
        signal.Signal(faders.ExpFader(30), toners.ConstToner(t), 0.2)
        for t in range(400, 900, 50)
    ]):
    t2.add_sound(s, 0.2 * i)
t2.get_playback(10000).save('test3.wav')

t3 = timeline.Timeline()
t3.add_sound(t1, -1)
t3.add_sound(t2, 0)
t3.add_sound(t1, 1)
t3.get_playback(10000).save('test4.wav')

s = signal.Signal(faders.ConstFader(0.5), toners.LineToner(100, 1000, 2), 2)
s.get_playback(40000).save('test5.wav')

t3.add_sound(s, t3.get_duration())
t3.get_playback(10000).save('test6.wav')
