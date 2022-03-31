import turtle as tt
from math import *

n = 3


def poly(n, r):
    m = n
    a = 2 * r * sin(radians(360 / 2 / n))
    alfa = 360 / n
    d_alfa = 360 / (n-1)/2 + 360 / (n)/2
    tt.goto(0,0)
    tt.goto(r,0)

    tt.left(d_alfa)
    print('dalfa=', d_alfa)
    while m >= 1:
        tt.forward(a)
        tt.left(alfa)
        print(a)
        print(alfa)
        m -= 1


while n <= 6:
    poly(n, 10 * n)
    n += 1