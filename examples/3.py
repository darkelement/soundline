#!/usr/bin/python

import sys
sys.path.append('.')
sys.path.append('..')

from pysoundline import toners, faders, constants, Timeline, Signal

class NoteDuration:
    WHOLE  = 1.0
    HALF   = 0.5
    QUATER = 0.25
    EIGTH  = 0.125

def make_note(frequency, duration):
    f = faders.ExpFader(1.0, 1.0/duration)
    t = toners.ConstToner(frequency)
    return Signal(f, t, 4.0*duration)

C4Q = make_note(constants.Note.C[4], NoteDuration.QUATER)
D4Q = make_note(constants.Note.D[4], NoteDuration.QUATER)
E4Q = make_note(constants.Note.E[4], NoteDuration.QUATER)
F4Q = make_note(constants.Note.F[4], NoteDuration.QUATER)
G4Q = make_note(constants.Note.G[4], NoteDuration.QUATER)

C4E = make_note(constants.Note.C[4], NoteDuration.EIGTH)
C4H = make_note(constants.Note.C[4], NoteDuration.HALF)
D4E = make_note(constants.Note.D[4], NoteDuration.EIGTH)
D4H = make_note(constants.Note.D[4], NoteDuration.HALF)
E4E = make_note(constants.Note.E[4], NoteDuration.EIGTH)
F4E = make_note(constants.Note.F[4], NoteDuration.EIGTH)

C3H = make_note(constants.Note.C[3], NoteDuration.HALF)
G3H = make_note(constants.Note.G[3], NoteDuration.HALF)
C3W = make_note(constants.Note.C[3], NoteDuration.WHOLE)
G3W = make_note(constants.Note.G[3], NoteDuration.WHOLE)


d = 0.3

ta = Timeline()
ta.add_sound(E4Q,  1*d)
ta.add_sound(E4Q,  2*d)
ta.add_sound(F4Q,  3*d)
ta.add_sound(G4Q,  4*d)
ta.add_sound(G4Q,  5*d)
ta.add_sound(F4Q,  6*d)
ta.add_sound(E4Q,  7*d)
ta.add_sound(D4Q,  8*d)
ta.add_sound(C4Q,  9*d)
ta.add_sound(C4Q, 10*d)
ta.add_sound(D4Q, 11*d)
ta.add_sound(E4Q, 12*d)
ta.add_sound(C3W,  1*d)
ta.add_sound(G3W,  5*d)
ta.add_sound(C3W,  9*d)

tb = Timeline()
tb.add_sound(E4Q, 1*d)
tb.add_sound(G3W, 1*d)
tb.add_sound(D4E, 2.5*d)
tb.add_sound(D4H, 3*d)

tc = Timeline()
tc.add_sound(D4Q, 1*d)
tc.add_sound(G3H, 1*d)
tc.add_sound(C4E, 2*d+d/2)
tc.add_sound(C4H, 3*d)
tc.add_sound(C3H, 3*d)


t3 = Timeline()
t3.add_sound(D4Q,  1*d)
t3.add_sound(D4Q,  2*d)
t3.add_sound(E4Q,  3*d)
t3.add_sound(C4Q,  4*d)
t3.add_sound(D4Q,  5*d)
t3.add_sound(E4E,  6*d)
t3.add_sound(F4E,  6.5*d)
t3.add_sound(E4Q,  7*d)
t3.add_sound(C4Q,  8*d)
t3.add_sound(D4Q,  9*d)
t3.add_sound(E4E, 10*d)
t3.add_sound(F4E, 10.5*d)
t3.add_sound(E4Q, 11*d)
t3.add_sound(D4Q, 12*d)
t3.add_sound(C4Q, 13*d)
t3.add_sound(D4Q, 14*d)
t3.add_sound(G3H, 15*d)
t3.add_sound(G3W,  1*d)
t3.add_sound(G3W,  5*d)
t3.add_sound(G3W,  9*d)
t3.add_sound(G3W, 13*d)


t1 = Timeline()
t1.add_sound(ta, 0)
t1.add_sound(tb, 12*d)

t2 = Timeline()
t2.add_sound(ta, 0)
t2.add_sound(tc, 12*d)

t = Timeline()
t.add_sound(t1, 0, volume=0.5)
t.add_sound(t2, 16*d)
t.add_sound(t3, 2*16*d)
t.add_sound(t2, 3*16*d)
t.get_playback().save('example_3.1.wav')

