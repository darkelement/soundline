#!/usr/bin/python

import sys
sys.path.append('..')

from pysoundline import toners, faders, constants, Timeline, Signal

NAME = 'example_3_signals.'

sA3 = Signal(faders.ExpFader(1, 10), toners.ConstToner(constants.Note.A[3]), 1)
sA4 = Signal(faders.ExpFader(1, 10), toners.ConstToner(constants.Note.A[4]), 1)
sA5 = Signal(faders.ExpFader(1, 10), toners.ConstToner(constants.Note.A[5]), 1)

constants.print_notes()

# Simple timeline
t1 = Timeline()
t1.add_sound(sA3, 0)
t1.add_sound(sA4, 1)
t1.add_sound(sA5, 2)
t1.get_playback().save(NAME + '1.wav')

# Simple toners and faders
t2 = Timeline()
for i, s in enumerate([
         Signal(faders.ExpFader(1, 30), toners.ConstToner(t), 0.2)
         for t in constants.Note.C]):
    t2.add_sound(s, 0.2*i)

# More complex timeline
t3 = Timeline()
t3.add_sound(t1, -1)
t3.add_sound(t2,  0)
t3.add_sound(t1,  1)
t3.get_playback().save(NAME + '2.wav')

# Annother toner
s = Signal(faders.ConstFader(0.5), toners.LineToner(100, 600, 2), 2)

t3.add_sound(s, t3.get_duration())
t3.get_playback().save(NAME + '3.wav')


