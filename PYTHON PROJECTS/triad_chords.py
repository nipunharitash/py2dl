
import itertools

def circ_slice(a, start, length):
    it = itertools.cycle(a)
    next(itertools.islice(it, start, length), None)
    return list(itertools.islice(it, length))

a = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
n = input("Enter Root Node: ")


if n.lower() == 'a':
    start = 0
    qnodes = circ_slice(a, start, 5)
    print(" The Triad Chord consists of these nodes" , qnodes[0],qnodes[2],qnodes[4])

elif n.lower() == 'a#':
    start = 1
    qnodes = circ_slice(a, start, 5)
    print(" The Triad Chord consists of these nodes", qnodes[0], qnodes[2],qnodes[4])

elif n.lower() == 'b':
    start = 2
    qnodes = circ_slice(a, start, 5)
    print(" The Triad Chord consists of these nodes", qnodes[0], qnodes[2],qnodes[4])

elif n.lower() == 'c':
    start = 3
    qnodes = circ_slice(a, start, 5)
    print(" The Triad Chord consists of these nodes", qnodes[0], qnodes[2], qnodes[4])
elif n.lower() == 'c#':
    start = 4
    qnodes = circ_slice(a, start, 5)
    print(" The Triad Chord consists of these nodes", qnodes[0], qnodes[2], qnodes[4])
elif n.lower() == 'd':
    start = 5
    qnodes = circ_slice(a, start, 5)
    print(" The Triad Chord consists of these nodes", qnodes[0], qnodes[2], qnodes[4])
elif n.lower() == 'd#':
    start = 6
    qnodes = circ_slice(a, start, 5)
    print(" The Triad Chord consists of these nodes", qnodes[0], qnodes[2], qnodes[4])
elif n.lower() == 'e':
    start = 7
    qnodes = circ_slice(a, start, 5)
    print(" The Triad Chord consists of these nodes", qnodes[0], qnodes[2], qnodes[4])
elif n.lower() == 'f':
    start = 8
    qnodes = circ_slice(a, start, 5)
    print(" The Triad Chord consists of these nodes", qnodes[0], qnodes[2], qnodes[4])
elif n.lower() == 'f#':
    start = 9
    qnodes = circ_slice(a, start, 5)
    print(" The Triad Chord consists of these nodes", qnodes[0], qnodes[2], qnodes[4])
elif n.lower() == 'g':
    start = 10
    qnodes = circ_slice(a, start, 5)
    print(" The Triad Chord consists of these nodes", qnodes[0], qnodes[2], qnodes[4])
elif n.lower() == 'g#':
    start = 11
    qnodes = circ_slice(a, start, 5)
    print(" The Triad Chord consists of these nodes", qnodes[0], qnodes[2], qnodes[4])
else:
        print("Invalid Entry")

