import os

for root, directories, files in os.walk(r'd:/pp2/lab5'):
    print(root)
    for x in directories:
        print(x)
    for y in files:
        print(y)