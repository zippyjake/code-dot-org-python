"""Stage 5: Puzzle 5 of 10

Now, for practice, draw a triangle and then a square to draw an envelope.
Hint: delete the 'pass' (which does nothing) with your code.

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level28')
a = artist

for count in range(3):
    a.fd(100)
    a.right(120)
for count in range(4):
    a.fd(100)
    a.right(90)

artist.check()
