def f(n):
    while n >= 0:
        yield n
        n -= 1

a = int(input())
for i in f(a):
    print(i)