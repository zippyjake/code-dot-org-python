"""Stage 7: Puzzle 1 of 11

Can you draw a triangle (with edges of 100 pixels) with only 3
lines of code? Hint: use a repeat (for) loop.

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level35')
a = artist

for count in range(3):
    a.fd(100)
    a.right(120)

artist.check()
