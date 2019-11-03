#!/usr/bin/python

import sys
sys.path.append('.')
sys.path.append('..')

from pysoundline import constants, timeline, instruments

g = instruments.String()

pA3 = g.get_playback(constants.Note.A[3])
pA4 = g.get_playback(constants.Note.A[4])
pA5 = g.get_playback(constants.Note.A[5])

t1 = timeline.Timeline()
t1.add_sound(pA3, 0)
t1.add_sound(pA4, 1)
t1.add_sound(pA5, 2)
t1.get_playback(constants.SAMPLERATE).save('example_2.1.wav')

