import re

text = input()
res = re.search(r'[A-Z]{1}+_[a-z]+$', text)
print(res)