import re
line = input()
line = line.title()
for i in range (len (line)):
      if line[i]!='_':
          print (line [i], end="")