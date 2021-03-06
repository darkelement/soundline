#!/usr/bin/python

import sys
sys.path.append('..')

from pysoundline import constants, instruments, Timeline

s = instruments.String()

pA3 = s.get_playback(constants.Note.A[3])
pA4 = s.get_playback(constants.Note.A[4])
pA5 = s.get_playback(constants.Note.A[5])

t1 = Timeline()
t1.add_sound(pA3, 0)
t1.add_sound(pA4, 1)
t1.add_sound(pA5, 2)
t1.get_playback().save('instruments_string.wav')

