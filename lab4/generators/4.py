import math
def f(a, b):
    while a <= b:
        yield pow(a, 2)
        a += 1
x, y = map(int,input().split())
for i in f(x, y):
    print(i)