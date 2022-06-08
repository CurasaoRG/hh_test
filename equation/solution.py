from math import sqrt


def solution(a,b,c):
    d = b**2 - 4*a*c
    if d > 0:
        return f"два корня: {-b + sqrt(d)}, {-b - sqrt(d)}"
    elif d == 0:
        return f"два совпадающих корня {-b}"
    else:
        return f"нет действительных корней"