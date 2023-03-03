import re

text = input()
res = re.findall(r'a.*b$', text)
print(res)