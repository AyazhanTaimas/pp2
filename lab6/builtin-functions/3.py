def palindrome(a):
    return list(reversed(a)) == list(a)

a = input()
print(palindrome(a))