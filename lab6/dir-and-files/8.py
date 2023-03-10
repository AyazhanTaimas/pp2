import os

path = "d:/pp2/lab6/dir-and-files/88.txt"

if not os.access(path, os.F_OK):
    print("does not exist")
elif not os.access(path, os.W_OK):
    print("not writable")
else:
    os.remove(path)