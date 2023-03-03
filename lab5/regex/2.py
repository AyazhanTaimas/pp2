import re

text = input()
res = re.findall(r'ab{2,3}$', text)
print(res)