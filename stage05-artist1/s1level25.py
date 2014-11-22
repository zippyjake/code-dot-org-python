"""Stage 5: Puzzle 2 of 10

Now, draw a square. NOTE: tell the artist to use your favorite color pen
by assigning a color to the `artist.color` variable.

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level25')
a = artist

artist.color = 'red'
for count in range(4):
    a.fd(100)
    a.right(90)

artist.check()
