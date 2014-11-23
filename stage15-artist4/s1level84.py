"""Stage 15: Puzzle 3 of 10

Draw triangular fences around the cats and a square fence around the
cow. Tip: test the program as you go along.

"""
import sys
sys.path.append('..')
import codestudio
z = codestudio.load('s1level84')

def draw_square(length):
    for count in range(4):
        z.move_forward(100)
        z.turn_right(90)

def draw_triangle(length):
    for count in range(3):
        z.move_forward(100)
        z.turn_right(120)

draw_triangle(100)
z.fd(100)
draw_square(100)
z.fd(100)
draw_triangle(100)

z.check()
