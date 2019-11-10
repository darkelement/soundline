import math

SAMPLERATE = 44100

def get_harmonics(freq, size, o1=0, o2=0):
    return [math.pow(2, k + o2/12.0) * freq for k in range(o1, size+o1)]

def print_notes():
    def print_note(name, freqs):
        print('{0:3s}'.format(name), end='')
        for freq in freqs:
            print('{0:8.2f}'.format(freq), end='')
        print()

    print(' ', end='')
    for i in range(0, 9):
        print('       {0}'.format(i), end='')
    print()

    print_note('C ', Note.C)
    print_note('C#', Note.Cs)
    print_note('D ', Note.D)
    print_note('D#', Note.Ds)
    print_note('E ', Note.E)
    print_note('F ', Note.F)
    print_note('F#', Note.Fs)
    print_note('G ', Note.G)
    print_note('G#', Note.Gs)
    print_note('A ', Note.A)
    print_note('A#', Note.As)
    print_note('B ', Note.B)

class Note:
    C  = get_harmonics(440, 9, -4, -9)
    Cs = get_harmonics(440, 9, -4, -8)
    D  = get_harmonics(440, 9, -4, -7)
    Ds = get_harmonics(440, 9, -4, -6)
    E  = get_harmonics(440, 9, -4, -5)
    F  = get_harmonics(440, 9, -4, -4)
    Fs = get_harmonics(440, 9, -4, -3)
    G  = get_harmonics(440, 9, -4, -2)
    Gs = get_harmonics(440, 9, -4, -1)
    A  = get_harmonics(440, 9, -4,  0)
    As = get_harmonics(440, 9, -4,  1)
    B  = get_harmonics(440, 9, -4,  2)

