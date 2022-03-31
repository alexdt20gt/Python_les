import turtle as tt
from math import *

tt.speed(5)


def circ(r, n, m):
    alfa = 360 / n
    for i in m:
        tt.circle(r)
        tt.left(360/n)

circ(50, 8)
