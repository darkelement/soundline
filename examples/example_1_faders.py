#!/usr/bin/python

import sys
sys.path.append('..')

from pysoundline import toners, faders, constants, Timeline, Signal

L = 3.0
I = 4.0
ct = toners.ConstToner(constants.Note.A[3])

# Linear fader
fl = faders.LinearFader(2)

# Long exponential signal
fe = faders.SimpleExpFader(1, 5)

# Long exponential signal
fel = faders.ExpFader(1, 5, L/4.0)

# Short exponential signal
fes = faders.ExpFader(1, 5, 0.02)

# Slow Sine signal
fss = faders.SineFader(2.0)

# Fast Sine signal
fsf = faders.SineFader(30.0)

# Sine Exp signal
fse = faders.SineExpFader(1, 3, 30.0, 0.5, 0.05)

# Build timeline
t = Timeline()
for i, f in enumerate((fl, fe, fel, fes, fss, fsf, fse)):
    print(f)
    s = Signal(f, ct, L)
    t.add_sound(s, i*I)
t.get_playback().save('example_1_faders.wav')
