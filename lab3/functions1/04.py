def prime_numbers(n):
    if n<2:
        return False
    for x in range(2, (n//2)+1):
        if n % x == 0:
            return False
    return True

def filter_prime(num):
    ans = []
    for i in num :
        if prime_numbers(i)==True:
            ans.append(i)
    return ans

num = input().split()
pnum = []

for x in num : 
    pnum.append(int(x))

print(filter_prime(pnum))
