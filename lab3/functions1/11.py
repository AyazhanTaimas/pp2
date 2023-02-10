def palindrome(s):
    if s[::-1] == s:
        return True
    return False

s = str(input())
if palindrome(s):
    print("Palindrome")
else:
    print("Not palindrom")