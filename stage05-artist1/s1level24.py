"""Stage 5: Puzzle 1 of 10

Hi meet the artist. You can write code to make the artist draw almost anything.
Run this code to see the goal. Then add a few lines of code to make the
artist draw over the grey lines of the goal.

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level24')

artist.move_forward(100)
artist.right()
artist.move(100)

artist.check()

