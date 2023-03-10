import os

path = r"D:\pp2\lab6\dir-and-files\55.txt"

mylist = ["Stray kids", "BTS", "EXO", "Blackpink"]
file = open(path, "w")
for i in mylist:
    file.write(i + ' ')
file.close()

file = open(path, "r")
print(file.read())