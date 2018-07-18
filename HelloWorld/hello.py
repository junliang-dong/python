# _*_ coding: utf-8 _*_
import math
from collections import Iterable

def quadratic(a, b, c):
    x = math.sqrt(b ** 2 - 4 * a * c)
    q = (-b + x) / (2 * a)
    p = (-b - x) / (2 * a)
    return p,q
print(quadratic(2, 3, 1))

a = (-0.5, -1.0)
b = (-1.0, -0.5)
print(a != b)

def product(*args):
    sum = 1
    for arg in args:
        sum = sum * arg
    return sum

print(product(5, 6, 7, 8))

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
print(fact(10))

def trim(s):
    while s[:1] == " ":
        s = s[1:]
    while s[-1:] == " ":
        s = s[:-1]
    return s
print(trim("  sss     "))

l = list(range(10))
print(l[1])

def findMinAndMax(L):
    min = L[0]
    max = L[0]
    if isinstance(L, Iterable):
        for x in L:
            if x < min:
                min = x
            if x > max:
                max = x
    return min, max
print(findMinAndMax([7, 15, 11, 33, 6, 32]))

