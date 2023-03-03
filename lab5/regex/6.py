r'[A-Z]{1}[a-z]*'
import re

text = input()
res = re.sub('[\s.,]',',', text)
print(res)