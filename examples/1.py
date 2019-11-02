#!/usr/bin/python

import sys
sys.path.append('.')
sys.path.append('..')

from pysoundline import signal, toners, faders, timeline

s400 = signal.Signal(faders.ExpFader(10), toners.ConstToner(400), 1)
s600 = signal.Signal(faders.ExpFader(10), toners.ConstToner(600), 1)
s800 = signal.Signal(faders.ExpFader(10), toners.ConstToner(800), 1)

s800.get_playback(10000).save('test1.wav')

t1 = timeline.Timeline()
t1.add_sound(s600, 0)
t1.add_sound(s800, 1)
t1.get_playback(10000).save('test2.wav')

t2 = timeline.Timeline()
for i, s in enumerate([signal.Signal(faders.ExpFader(30), toners.ConstToner(t), 0.2) for t in range(400, 900, 50)]):
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
