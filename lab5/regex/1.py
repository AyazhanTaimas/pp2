import re

text = input()
res = re.findall(r'ab*', text)
print(res)