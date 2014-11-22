"""Stage 5: Puzzle 7 of 10

Ok, let's make it a bit harder - see if you can draw these green
glasses. The squares are 100 pixels on each side, and they're 50 pixels
apart. Don't forget to draw in green! 

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level30')
a = artist

a.color = 'green'
a.right(90)
for count in range(4):
    a.fd(100)
    a.right(90)
a.left(180)
a.fd(50)
for count in range(4):
    a.fd(100)
    a.left(90)


artist.check()
