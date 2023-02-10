def hist(l):
    for x in l:
        for y in range(x):
            print("*",end="")
        print("")    


l = [ int(x) for x in input().split()]
hist(l)