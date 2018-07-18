# _*_ coding: utf-8 _*_
def is_palindrome(n):
    return str(n) == str(n)[::-1]

L = list(filter(is_palindrome, range(1000)))
print(L)
