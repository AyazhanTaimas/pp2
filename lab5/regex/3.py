import re

text = input()
res = re.search(r'^[a-z]+_[a-z]+$', text)
print(res)