"""Stage 11: Puzzle 1 of 11

Hello. Me zombie artist. Me love drawing! Help me draw a square in a
special color.  Important note: you have all the same actions just
with a zombie artist now.

"""

import sys
sys.path.append('..')
import codestudio
zombie = codestudio.load('s1level59')
a = zombie
for count in range(4):
    a.fd(100)
    a.right(90)

zombie.check()
