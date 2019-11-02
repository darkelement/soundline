import math

def calc_note_freqs(offset):
    return [math.pow(2, (offset+k*12)/12.0) * 440 for k in range(-4, 5)]

class Note:

    C  = calc_note_freqs(-9)
    Cs = calc_note_freqs(-8)
    D  = calc_note_freqs(-7)
    Ds = calc_note_freqs(-6)
    E  = calc_note_freqs(-5)
    F  = calc_note_freqs(-4)
    Fs = calc_note_freqs(-3)
    G  = calc_note_freqs(-2)
    Gs = calc_note_freqs(-1)
    A  = calc_note_freqs( 0)
    As = calc_note_freqs( 1)
    B  = calc_note_freqs( 2)

    @staticmethod
    def print_notes():

        def print_note(name, freqs):
            print('{0:4s}'.format(name), end='')
            for freq in freqs:
                print('{0:8.2f}'.format(freq), end='')
            print()

        print('         0        1        2        3        4', end='')
        print('       5        6        7        8')
        print_note('C',  Note.C)
        print_note('C#', Note.Cs)
        print_note('D',  Note.D)
        print_note('D#', Note.Ds)
        print_note('E',  Note.E)
        print_note('F',  Note.F)
        print_note('F#', Note.Fs)
        print_note('G',  Note.G)
        print_note('G#', Note.Gs)
        print_note('A',  Note.A)
        print_note('A#', Note.As)
        print_note('B',  Note.B)

