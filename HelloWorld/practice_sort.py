# _*_ coding: utf-8 _*_

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(L)

def by_name(t):
    return t[0].lower()

L2 = sorted(L, key=by_name)

print(L2)

def by_score(t):
    return t[1]

L3 = sorted(L, key=by_score, reverse=True)

print(L3)

def createCounter():
    def addOne():
        n = 0
        while True:
            n = n + 1
            yield n
    sum = addOne()
    def counter():
        return next(sum)
    return counter

counterA = createCounter()
print(counterA(), counterA())


Lt = list(filter(lambda x: x % 2 == 1, range(1, 20)))

print(Lt)
