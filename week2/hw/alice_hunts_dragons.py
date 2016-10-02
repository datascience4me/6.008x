from functools import reduce
import operator

print('======= Homework Problem: Alice Hunts Dragons =======')

X = range(1, 5)
Y = range(1, 4)


def f(x, y):
    if x == 3 or y == 2:
        return 0
    return x ** 2 + y ** 2


print('Finding normalization constant c')
s = 0
for x in X:
    for y in Y:
        s += f(x, y)
c = 1 / s
print('Normalization constant c = ', c)

print('Finding P(Y<X)')
P = 0
for x in X:
    for y in Y:
        if y < x:
            P += f(x, y)
P *= c
print('P(Y<X) = ', P)

print('Finding P(X<Y)')
P = 0
for x in X:
    for y in Y:
        if y > x:
            P += f(x, y)
P *= c
print('P(X<Y) = ', P)

print('Finding P(X=Y)')
P = 0
for x in X:
    for y in Y:
        if y == x:
            P += f(x, y)
P *= c
print('P(X=Y) = ', P)

print('Finding P(Y=3)')
P = 0
for x in X:
    for y in Y:
        if y == 3:
            P += f(x, y)
P *= c
print('P(Y=3) = ', P)


print('Calculating the probability tables for pX and pY')
p_x = {}
for x in X:
    p_x[x] = c * reduce(operator.add, map(lambda y: f(x, y), Y))
print(p_x)

p_y = {}
for y in Y:
    p_y[y] = c * reduce(operator.add, map(lambda x: f(x, y), X))
print(p_y)
